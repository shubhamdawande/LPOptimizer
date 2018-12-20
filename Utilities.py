from Globals import *

##
## Utility Functions
##

#
# Value function: depends upon customer type, Asset type, Asset class
# For no of asset of same type and no of dependent asset value decreases for subsequent asset, price point 
#
def update_val_function(testing):
    if testing:
        # Set manual values 
        value_of_items[:, 0, 0] = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 7]
        value_of_items[:, 1, 0] = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        value_of_items[:, 2, 0] = [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]

#
# Limit assets qty
#
def create_asset_bounds(room_type, customer_persona):

    mandatory_activity_list = room_activity_dict[room_type]
    
    for i in range(0, len(asset_categories)):

        # minimum 1 mandatory item to be selected
        if category_activity_dict[asset_categories[i]] in mandatory_activity_list:
             asset_lower_bounds[i, 0, 0] = 1
        else:
            asset_lower_bounds[i, 0, 0] = 0

    '''
    if room_type == "LivingRoom":
        for i in range(0, len(asset_categories)):

            ## Hardcoding to be removed later, Part of 'Room Planning Model'

            # 3 mandatory items for living room
            if (asset_categories[i] == "Lights") or (asset_categories[i] == "TV") or (asset_categories[i] == "Curtains") or (asset_categories[i] == "Carpet"):
                asset_lower_bounds[i, 0, 0] = 1
            else:
                asset_lower_bounds[i, 0, 0] = 0

            if (asset_categories[i] == "PillowSet") or (asset_categories[i] == "PillowCoverSet") or (asset_categories[i] == "Curtains") or (asset_categories[i] == "Lights") or (asset_categories[i] == "Plant") or (asset_categories[i] == "Planter"):
                asset_upper_bounds[i, 0, 0] = 10
            else:
                asset_upper_bounds[i, 0, 0] = 1
    '''
