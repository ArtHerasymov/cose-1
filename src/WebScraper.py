import requests
from bs4 import BeautifulSoup
import re
from src import LogicalModule


def get_converted_prices(prices):
    converted_prices = []
    for x in range(0, len(prices)):
        pr = re.findall(r'\d+', prices[x].get_text())
        fnl = ""
        for p in pr:
            fnl += p
            converted_prices.append(int(fnl))

    return converted_prices


def get_livenshtein_couples(names, inquiry):
    couples = []
    for x in range(0, len(names)):
        currentLength = LogicalModule.trim(inquiry, names[x].text)
        if currentLength != -1:
            couples.append((x, currentLength))

    return couples


def filter_price_list(converted_prices, recommended_length , couples):
    filtered_rice_list = []
    for i in range(1, len(couples)):
        if couples[i][1] == recommended_length:
            filtered_rice_list.append(converted_prices[i])
    return filtered_rice_list


def get_price_range(store, inquiry):
    # Request html from url and getting dom out of it
    page = requests.get(store.url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Looking for prices and names inside dom object(soup)
    prices = soup.find_all(store.keyword_container, {store.keyword_attribute: store.keyword_name})
    names = soup.find_all(store.product_container, {store.product_attribute: store.product_name})

    # Converting dom data to integer prices
    converted_prices = get_converted_prices(prices)
    # Getting an object with minimal Levenshtein length
    couples = get_livenshtein_couples(names, inquiry)
    recommended_length = min(couples, key=lambda t: t[1])[1]
    # Filter price list to leave only those items that possess recommended LL
    filtered_price_list = filter_price_list(converted_prices, recommended_length, couples)
    return {"min":min(filtered_price_list), "max" : max(filtered_price_list)}
