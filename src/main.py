from src import XMLHandler, WebScraper, LogicalModule

request = 'Iphone 7'
filename = '../sites.xml'


def main():
   stores = XMLHandler.get_sites(filename, request)
   for store in stores:
       print(store.name)

   WebScraper.get_price_range(stores[1])

main()

