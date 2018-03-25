from src import XMLHandler, WebScraper, LogicalModule

request = 'Iphone 7'
filename = '../sites.xml'


def main():
    stores = XMLHandler.get_sites(filename, request)
    results = []

    for store in stores:
        range = WebScraper.get_price_range(store, request)
        store.set_range(range["min"], range["max"])
        results.append(store)

    XMLHandler.save_output("../output.xml", results)


main()
