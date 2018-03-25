import xml.etree.ElementTree as ET

# Takes filename and searched product
# Returns the list of request queries
def get_sites(filename, query):
    tree = ET.parse(filename)
    root = tree.getroot()
    urls = []
    names = []
    keyword_containers = []
    keyword_attributes = []
    keyword_names = []

    productnames = []

    for child in root:
        name = child[0].text
        url = child[1].text.replace("{query}", query)
        keyword_container = child[2].text
        keyword_attribute = child[3].text
        keyword_name = child[4].text
        urls.append(url)
        names.append(name)
        keyword_containers.append(keyword_container)
        keyword_attributes.append(keyword_attribute)
        keyword_names.append(keyword_name)

    data = (names, urls, keyword_containers,keyword_attributes , keyword_names)
    return data
