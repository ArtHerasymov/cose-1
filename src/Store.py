class Store(object):
    """Serves as a container for the data about a single web store"""

    def __init__(self, data):
        if not data:
            raise Exception("None argument")

        self.name = data[0]
        self.url = data[1]
        # Prices
        self.keyword_container = data[2]
        self.keyword_attribute = data[3]
        self.keyword_name = data[4]
        # Names
        self.product_container = data[5]
        self.product_attribute = data[6]
        self.product_name = data[7]
        # Range
        self.lower = None
        self.upper = None
        # Product
        self.product = data[8]

    def set_range(self, lower, upper):
        self.lower = lower
        self.upper = upper

