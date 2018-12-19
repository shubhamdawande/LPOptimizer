import random
import numpy as np
import pickle

# Custom imports
from Item import Item
from Globals import *

# Read Customer Input
def read_customer_input(testing):

    if testing:
        # temporarily test inputs
        customer_type = "BachelorGamer"
        customer_budget = 100000
        room_type = "LivingRoom"
        room_area = 300
        return [customer_type, customer_budget, room_type, room_area]
    else:
        return 

## Retrieve available assets from server
def read_asset_data(customer_type, room_type, n_items, testing):
    
    ## Generate data for testing
    if testing:
        item_obj_list = []
        
        for i in range(0, n_items):

            # Item type
            random_item_type_index = np.random.randint(0, len(item_types))
            random_type = item_types[random_item_type_index]

            # Item area
            random_area = item_areas[random_item_type_index]

            # Item class
            random_class = random.choice(item_classes)

            # Item price
            random_price = 0
            if random_class == "Economy":
                random_price = random.randint(0, 3000)
            elif random_class == "Premium":
                random_price = random.randint(3000, 10000)
            elif random_class == "Luxury":
                random_price = random.randint(10000, 20000)

            # Item bounds
            lower_bound = item_lower_bounds[random_item_type_index, room_types.index(room_type), customer_types.index(customer_type)]
            upper_bound = item_upper_bounds[random_item_type_index, room_types.index(room_type), customer_types.index(customer_type)]

            # Item value
            if random_class == "Economy":
                item_value = value_of_items[random_item_type_index, 0, customer_types.index(customer_type)]
            else:
                item_value = value_of_items[random_item_type_index, 0, customer_types.index(customer_type)] * (
                1 + value_of_items[random_item_type_index, item_classes.index(random_class), customer_types.index(customer_type)] /100
                )

            item_obj = Item(random_type, random_price, random_class, random_area, upper_bound, lower_bound, item_value)

            item_obj_list.append(item_obj)

        # save as pickle file
        with open('data/item_obj_list'+ str(n_items), 'wb') as fp:
            pickle.dump(item_obj_list, fp)

        print("Generated random dataset of size " + str(n_items))

        return item_obj_list
        
    # Else read existing data
    else:
        # load existing pickle file
        with open('data/item_obj_list'+ str(n_items), 'rb') as fp:
            item_obj_list = pickle.load(fp)

        return item_obj_list
