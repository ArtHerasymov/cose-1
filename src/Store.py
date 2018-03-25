class Store(object):
    def __init__(self, data):
        self.name = data[0]
        self.url = data[1]
        # Prices
        self.keyword_container = data[2]
        self.keyword_attribute = data[3]
        self.keyword_name = data[4]
        #Names
        self.product_container = data[5]
        self.product_attribute = data[6]
        self.product_name = data[7]
