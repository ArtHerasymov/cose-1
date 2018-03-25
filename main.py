import src

request = 'Iphone 7'
input_file = '../sites.xml'
output_file = '../output.xml'


def main():
    print("AI processig ...")
    stores = src.XMLHandler.get_sites(input_file, request)
    results = []

    for store in stores:
        price_range = src.WebScraper.get_price_range(store, request)
        store.set_range(price_range["min"], price_range["max"])
        results.append(store)

    src.XMLHandler.save_output(output_file, results)
    print("Data is saved to", output_file)


main()
