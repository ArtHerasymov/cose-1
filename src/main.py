from src import xmlhandler, responsehandler

request = 'Iphone 7'
filename = '../sites.xml'

def main():
  data = xmlhandler.get_sites(filename, request)
  responsehandler.get_page(data[1][1], data[2][1], data[3][0], data[4][1])



main()
