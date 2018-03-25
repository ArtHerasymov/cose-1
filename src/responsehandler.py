import requests
from bs4 import BeautifulSoup


def get_page(query, keyword_type, keyword_attribute, keyword_name):
    print(query)
    page = requests.get(query)
    soup = BeautifulSoup(page.content, 'html.parser')
    prices = soup.find_all(keyword_type, {keyword_attribute:keyword_name})
    for price in prices:
        print(price.get_text())