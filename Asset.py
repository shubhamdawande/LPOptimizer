# Class for furniture Assets

class Asset:

    # Asset properties

    # product category
    _category = ""

    # product price
    _price = 0

    # product brand value
    _class = ""

    # product area
    _area = 0

    # product qty limits
    _upperbound = 0
    _lowerbound = 0

    # value provided by product
    _value = 0

    # product functionality
    _functionality = ""

    def __init__(self, asset_category, asset_price, asset_class, asset_area, asset_upperbound, asset_lowerbound, asset_value):
        self._category = asset_category
        self._class = asset_class
        self._area = asset_area
        self._price = asset_price
        self._upperbound = asset_upperbound
        self._lowerbound = asset_lowerbound
        self._value = asset_value