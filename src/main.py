from src import XMLHandler, ResponseHandler, LogicalModule

request = 'Iphone 7'
filename = '../sites.xml'


def main():
    #data = XMLHandler.get_sites(filename, request)
    #ResponseHandler.get_page(data[1][1], data[2][1], data[3][0], data[4][1])
    #ResponseHandler.get_names(data[1][0], data[5][0], data[6][0], data[7][0])

    # Testing trimming

    print(LogicalModule.trim("Iphone 7", "Смартфон 18"))


main()
