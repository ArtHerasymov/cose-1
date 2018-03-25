import xml.etree.ElementTree as ET
from xml.dom import minidom
from src import Store


def get_sites(filename, query):
    """Returns the list of Store objects"""
    try:
        tree = ET.parse(filename)
    except IOError:
        return None

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
            name, url, keyword_container,
            keyword_attribute, keyword_name, product_container,
            product_attribute, product_name, query]))
    return stores


def save_output(filename, results):
    """Finalizes the program by serializing computed data into xml file"""
    if results is None:
        return None

    root = ET.Element("sites")

    for result in results:
        site = ET.SubElement(root, "site")
        ET.SubElement(site, "store").text = result.name
        ET.SubElement(site, "product").text = result.product
        ET.SubElement(site, "lower").text = str(result.lower)
        ET.SubElement(site, "upper").text = str(result.upper)

    xmlstring = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")
    with open(filename, "w") as f:
        f.write(xmlstring)
