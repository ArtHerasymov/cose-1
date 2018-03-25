import requests
from bs4 import BeautifulSoup
import re


def get_price_range(store):

    page = requests.get(store.url)
    soup = BeautifulSoup(page.content, 'html.parser')
    prices = soup.find_all(store.keyword_container, {store.keyword_attribute: store.keyword_name})
    names = soup.find_all(store.product_container, {store.product_attribute: store.product_name})
    ## Retrieving minimum price
    convertedPrices = []
    for x in range (0, len(prices)):
        pr = re.findall(r'\d+', prices[x].get_text())
        fnl = ""
        for p in pr:
            fnl += p
        convertedPrices.append(int(fnl))
        print(names[x].text)
        print(convertedPrices[x])
    print(len(names), len(prices))
    print('Minimum price : ' , min(convertedPrices))