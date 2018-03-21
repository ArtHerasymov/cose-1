from src import xmlhandler, responsehandler

request = 'Canon 750D'
filename = '../sites.xml'


def main():
    xmldata = xmlhandler.get_sites(filename, request)

    print(xmldata[0][0])
    print(responsehandler.get_prices(xmldata[1][0], xmldata[2][0]))


main()
