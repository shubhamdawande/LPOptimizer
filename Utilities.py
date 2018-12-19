from Globals import value_of_items, item_lower_bounds, item_upper_bounds, item_types

##
## Utility Functions
##

# Value function: depends upon customer type, item type, item class
def asset_val_function(testing):
    if testing:
        # Set manual values 
        value_of_items[:, 0, 0] = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10]
        value_of_items[:, 1, 0] = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        value_of_items[:, 2, 0] = [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]

        #value_of_items[:, 1, 0] = [6, 12, 6, 12, 2.4, 1.2, 3.6, 2.4, 6.5, 1.2, 2.4, 2.4, 9.6, 7.2, 3.6, 14.6, 14.6, 7.5]
        #value_of_items[:, 2, 0] = [6.5, 13, 6.5, 13, 2.5, 1.2, 3.75, 2.5, 6.75, 1.25, 2.5, 2.5, 10, 6, 3.75, 16, 16, 8]

# Handle asset quantity
def asset_bounds(room_type):

	
    if room_type == "LivingRoom":
        for i in range(0, len(item_types)):

            ## Hardcoding to be removed later, Part of 'Room Planning Model'
            ##
            # 3 mandatory items for living room
            if (item_types[i] == "Lights") or (item_types[i] == "TV") or (item_types[i] == "Curtains") or (item_types[i] == "Carpet"):
                item_lower_bounds[i, 0, 0] = 1
            else:
                item_lower_bounds[i, 0, 0] = 0

            if (item_types[i] == "PillowSet") or (item_types[i] == "PillowCoverSet") or (item_types[i] == "Curtains") or (item_types[i] == "Lights") or (item_types[i] == "Plant") or (item_types[i] == "Planter"):
                item_upper_bounds[i, 0, 0] = 10
            else:
                item_upper_bounds[i, 0, 0] = 2