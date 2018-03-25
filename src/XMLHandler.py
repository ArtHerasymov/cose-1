import xml.etree.ElementTree as ET
from src import Store


# Takes filename and searched product
# Returns the list of request queries
def get_sites(filename, query):
    tree = ET.parse(filename)
    root = tree.getroot()
    stores = []

    for child in root:
        name = child[0].text
        url = child[1].text.replace("{query}", query)
        keyword_container = child[2].text
        keyword_attribute = child[3].text
        keyword_name = child[4].text
        product_container = child[5].text
        product_attribute = child[6].text
        product_name = child[7].text

        stores.append(Store([
            name,url,keyword_container,
            keyword_attribute,keyword_name,product_container,
            product_attribute,product_name]))
    return stores
