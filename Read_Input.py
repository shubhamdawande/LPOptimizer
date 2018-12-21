import random
import numpy as np
import pickle

# Custom imports
from Asset import Asset
from Globals import *
from Room import Room
from Customer import Customer

##
## Query Customer and Asset Data
##

# Read Customer Input
def read_customer_input(testing):

    # test inputs
    if testing:
        customer_persona = "BachelorGamer"
        customer_budget = 10000
        room_category = "LivingRoom"
        room_area = 200

        room = Room(room_area, room_category)
        customer_test = Customer("customer_test", customer_persona, customer_budget, room)
        return customer_test

    else:
        return 

## Retrieve available assets from server
def read_asset_data(customer_category, room_category, n_items, testing):
    
    ## Generate data for testing
    if testing:

        item_obj_list = []
        
        for i in range(0, n_items):

            # Asset type
            random_category_index = np.random.randint(0, len(asset_categories))
            random_category = asset_categories[random_category_index]

            # Asset area
            random_area = asset_areas[random_category_index]

            # Asset class
            random_class = random.choice(asset_classes)

            # Asset price
            random_price = 0
            if random_class == "Economy":
                random_price = random.randint(0, 3000)
            elif random_class == "Premium":
                random_price = random.randint(3000, 10000)
            elif random_class == "Luxury":
                random_price = random.randint(10000, 20000)

            # Asset bounds
            lower_bound = asset_lower_bounds[random_category_index, room_types.index(room_category), customer_personas.index(customer_category)]
            upper_bound = asset_upper_bounds[random_category_index, room_types.index(room_category), customer_personas.index(customer_category)]

            # Asset value
            if random_class == "Economy":
                item_value = value_of_items[random_category_index, 0, customer_personas.index(customer_category)]
            else:
                item_value = value_of_items[random_category_index, 0, customer_personas.index(customer_category)] * (
                1 + value_of_items[random_category_index, asset_classes.index(random_class), customer_personas.index(customer_category)] /100
                )

            item_obj = Asset(random_category, random_price, random_class, random_area, upper_bound, lower_bound, item_value)

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
