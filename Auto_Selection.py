import pulp
import numpy as np

# Custom imports
from Read_Input import read_customer_input, read_asset_data
from Globals import *
from Utilities import create_asset_bounds, update_val_function

#
# main LP function
#
def lp_optimizer(testing, n_assets):

    ##
    ### 1. Required Data Retrival
    ##

    # Get customer input
    customer = read_customer_input(testing)

    # Set asset upper/lower bounds
    create_asset_bounds(customer._room._type, customer._persona)

    # Set global value function: Customer behaviour modelling
    update_val_function(testing)

    # Retrieve asset data
    item_obj_list = read_asset_data(customer._persona, customer._room._type, n_assets, testing)

    ##
    ### 2. Formulize MILP optimization problem
    ##

    print("Forming the MILP problem....")
    prob = pulp.LpProblem("The Budget Optimization Problem", pulp.LpMaximize)

    total_val = 0
    item_indicator_list = []
    total_price = 0
    total_area = 0
    
    # Selected items for each type and class
    item_qty = [[0] * len(asset_classes) for i in range(0, len(asset_categories))]
    
    for i in range(0, len(item_obj_list)):
    	
        item_indicator_list.append(pulp.LpVariable(
            item_obj_list[i]._category + "_" + item_obj_list[i]._class + "_" + str(item_obj_list[i]._price) + "_"
            + str(item_obj_list[i]._area) + "_" + str(item_obj_list[i]._value) + "_" + str(i), 
            0,
            None, 
            pulp.LpInteger))

        # Maximization Expression
        total_val += item_obj_list[i]._value * item_indicator_list[i]

        # Constraint 3
        total_price += item_obj_list[i]._price * item_indicator_list[i]

        # Constraint 4
        total_area += item_obj_list[i]._area * item_indicator_list[i]

        # Constraint 10
        item_qty[asset_categories.index(item_obj_list[i]._category)][asset_classes.index(item_obj_list[i]._class)] += item_indicator_list[i]

    ##
    ### Define Objective and Constraints
    ##

    # Objective: Maximize value
    prob += total_val, "Maximize total value of selected items"

    # Constrain 1: number of items lower bound
    prob += sum(item_indicator_list) >= 0, "Total number of items selcted is positive"

    # number of items upper bound
    prob += sum(item_indicator_list) <= 20, "Total number of items selcted is finite"

    # Constraint 3: total price <= budget
    prob += total_price <= customer._budget, "Budget Requirement"

    # Constraint 4: total area <= available area
    # Currently no effect since most objects have null areas, to be modified later
    #prob += total_area <= room_area/4, "Area Requirement"

    ##
    ### Customizable constraints
    ##
    
    # Constraint 2: qty of beds <= qty of mattresses
    prob += sum(item_qty[asset_categories.index("Bed")][:]) <= sum(item_qty[asset_categories.index("Mattress")][:]), "Bed VS Mattress QTY"

    # Constraint 9: Console qty = tv qty
    prob += sum(item_qty[asset_categories.index("GamingConsole")][:]) == sum(item_qty[asset_categories.index("TV")][:]), "Console VS TV QTY"

    # Constraint 6
    prob += sum(item_qty[asset_categories.index("Plant")][:]) == sum(item_qty[asset_categories.index("Planter")][:]), "QTY Plant equals Planter"

    # Constraint 7
    prob += sum(item_qty[asset_categories.index("PillowSet")][:]) == sum(item_qty[asset_categories.index("PillowCoverSet")][:]), "QTY Pillows equal Covers"

    # Constraint 8
    prob += sum(item_qty[asset_categories.index("PillowSet")][:]) >= sum(item_qty[asset_categories.index("Mattress")][:]), "QTY Pillows greater than Mattress"

    # Constraint 10 + 11,12: mutually exclusive sets, Depend upon: Asset type, Asset class
    for i in range(0, len(item_qty)):
        
        prob += item_qty[i][0] + item_qty[i][1] + item_qty[i][2] <= min(max(item_qty[i][0], item_qty[i][1], item_qty[i][2]), asset_upper_bounds[i, room_types.index(customer._room._type), customer_personas.index(customer._persona)])
        prob += item_qty[i][0] + item_qty[i][1] + item_qty[i][2] >= asset_lower_bounds[i, room_types.index(customer._room._type), customer_personas.index(customer._persona)]
    
    print ("Done")
    
    ##
    ### 3. Run MILP solver
    ##

    print("Solving the MILP optimization....\n")

    # The problem data is written to an .lp file
    prob.writeLP("data/BudgetOptimizationVersion1.lp")

    # The problem is solved using PuLP's cbc Solver
    prob.solve(pulp.PULP_CBC_CMD())
    #prob.solve()
    print ("Status: ", pulp.LpStatus[prob.status])
    print ("")

    total_price = 0
    total_area = 0
    for v in prob.variables():

        if v.varValue > 0:
            k = v.name
            k = k.split('_')
            total_price += int(k[2]) * v.varValue
            total_area += int(k[3]) * v.varValue
            print '%15s' % k[0] + ", " + "Class: " +'%7s' % k[1] + ", " + "Price: " + '%6s' % k[2] + ", " + "Area: "+ '%2s' % k[3] + ", " + "Value: " + '%4s'%k[4] + ", " + "Qty: " + '%d'%v.varValue

    print ("")
    print ("Customer Persona:    ", customer._persona)
    print ("Room Type:           ", customer._room._type)
    print ("Covered Price:       ", total_price)
    print ("Customer Budget:     ", customer._budget)
    print ("Covered Area:        ", total_area)
    print ("Available Room Area: ", customer._room._area)
    print ("Total value achieved:", pulp.value(prob.objective))

# Entry function
if __name__ == "__main__":

    # Test model
    testing = True
    n_assets = 1000
    print ("Number of assets: ", n_assets)
    
    lp_optimizer(testing, n_assets)