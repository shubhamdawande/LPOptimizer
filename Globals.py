import numpy as np

##
## Global variables
##

# Customer related info
customer_types = ["BachelorGamer"]
room_types = ["LivingRoom"]

# Furniture asset types
item_types = ["Bed", "Mattress", "Wardrobe", "Lights", "Curtains", "Dressing", "SideTable", "Carpet", "Bookshelf",
              "Vase", "Planter", "Plant", "Shelf", "PillowsSet", "PillowCoverSet", "TV", "GamingConsole", "LaptopTable"]

# Area: per item type
item_areas = [30, 30, 12, 0, 0, 6, 1, 2, 6, 0, 0, 0, 0, 0, 0, 0, 2, 0]

# Item classes
item_classes = ["Economy", "Premium", "Luxury"]

# Value function: depends upon customer type, item type, item class
value_of_items = np.zeros((len(item_types), len(item_classes), len(customer_types)))

## Upper & lower bounds: depend upon room type, customer type, item type
item_lower_bounds = np.zeros((len(item_types), len(room_types), len(customer_types)))
item_upper_bounds = np.zeros((len(item_types), len(room_types), len(customer_types)))
