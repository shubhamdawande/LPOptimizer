import numpy as np

##
## Global variables
##

# Customer related info
customer_personas = ["BachelorGamer", "Bachelor", "YoungCouple", "MiddleAgedFamily", "OldFamily"]
room_types    = ["LivingRoom", "BedRoom", "Kitchen"]

# Furniture asset types
asset_categories = ["Bed", "Mattress", "Wardrobe", "Lights", "Curtains", "Dressing",
                    "SideTable", "Carpet", "Bookshelf", "Vase", "Planter", "Plant",
                    "Shelf", "PillowSet", "PillowCoverSet", "TV", "GamingConsole", "LaptopTable", "Sofa"]

# Area: per asset type
asset_areas = [30, 30, 12, 0, 0, 6, 1, 2, 6, 0, 0, 0, 0, 0, 0, 0, 2, 0, 20]

# Asset classes
asset_classes = ["Economy", "Premium", "Luxury"]

# Value function: depends upon customer type, Asset type, Asset class
value_of_items = np.zeros((len(asset_categories), len(asset_classes), len(customer_personas)))

# Upper & lower bounds: depend upon room type, customer type, Asset type
asset_lower_bounds = np.zeros((len(asset_categories), len(room_types), len(customer_personas)))
asset_upper_bounds = np.zeros((len(asset_categories), len(room_types), len(customer_personas)))

# Activity attributes
activity_list = ["Sitting", "Sleeping", "Watching", "Eating", "Storage", "Display", "Lighting"]

# Mandatory functionalities per room
room_activity_dict = {
                        "LivingRoom": ["Sitting", "Watching", "Lighting"],
                        "BedRoom":    ["Sleeping", "Storage", "Lighting"],
                        "Kitchen":    ["Eating", "Storage", "Lighting"]
                     }

activity_array = np.zeros((len(activity_list), len(room_types), len(customer_personas)))

# for BachelorGamer and LivingRoom
#activity_array[:, 0, 0] = [1, 0, 1, 0, 1, 1, 1]

# Currently upper bounds rules not defined
asset_upper_bounds[:, 0, 0] = [1, 2, 2, 6, 6, 2, 2, 1, 1, 6, 6, 6, 2, 6, 6, 1, 1, 1, 3]

category_activity_dict = {
                            "Bed"           :"Sleeping",
                            "Mattress"      :"Sleeping",
                            "Wardrobe"      :"Storage",
                            "Lights"        :"Lighting",
                            "Curtains"      :"Display",
                            "Dressing"      :"Storage",
                            "SideTable"     :"Storage",
                            "Carpet"        :"Display",
                            "Bookshelf"     :"Storage",
                            "Vase"          :"Display",
                            "Planter"       :"Display",
                            "Plant"         :"Display",
                            "Shelf"         :"Storage",
                            "PillowSet"     :"Display",
                            "PillowCoverSet":"Display",
                            "TV"            :"Watching",
                            "GamingConsole" :"Watching",
                            "LaptopTable"   :"Sitting",
                            "Sofa"          :"Sitting"
                          }