import xml.etree.ElementTree as ET

# Takes filename and searched product
# Returns the list of request queries
def get_sites(filename, query):
    tree = ET.parse(filename)
    root = tree.getroot()
    urls = []
    names = []
    keywords = []

    for child in root:
        url = child[1].text.replace("{query}", query)
        name = child[0].text
        keyword = child[2].text
        urls.append(url)
        names.append(name)
        keywords.append(keyword)
    data = (names, urls, keywords)
    return data
