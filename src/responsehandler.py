from htmldom import htmldom

# Takes query url and keyword for searching dom element containing price tag
# Returns the value of a price tag
def get_prices(query, keyword):
    return htmldom.HtmlDom(query).createDom().find(keyword)[0].text()

