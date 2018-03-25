import requests
from bs4 import BeautifulSoup
import re


def get_page(query, keyword_type, keyword_attribute, keyword_name):
    print(query)
    page = requests.get(query)
    soup = BeautifulSoup(page.content, 'html.parser')
    prices = soup.find_all(keyword_type, {keyword_attribute:keyword_name})
    int_prices = []
    for price in prices:
        pr = re.findall(r'\d+' , price.get_text())
        fnl = ""
        for p in pr:
            fnl += p
        print(int(fnl))

    return int_prices


def get_names(query, keyword_type, keyword_attribute, keyword_name):
    print(query)
    print(keyword_type, keyword_attribute, keyword_name)
    page = requests.get(query)
    soup = BeautifulSoup(page.content, 'html.parser')
    names = soup.find_all(keyword_type, {keyword_attribute: keyword_name})
    for name in names:
        print(name.get_text())
