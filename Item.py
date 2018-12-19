# Class for furniture Assets

class Item:
    # Item properties
    type_item = ""
    price_item = 0
    class_item = ""
    area_item = 0
    upperbound_item = 0
    lowerbound_item = 0
    value_item = 0

    def __init__(self, type_item, price_item, class_item, area_item, upperbound_item, lowerbound_item, value_item):
        self.type_item = type_item
        self.class_item = class_item
        self.area_item = area_item
        self.price_item = price_item
        self.upperbound_item = upperbound_item
        self.lowerbound_item = lowerbound_item
        self.value_item = value_item