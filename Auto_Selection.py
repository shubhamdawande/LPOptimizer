from pulp import *
import numpy as np

# Custom imports
from Read_Input import read_customer_input, read_asset_data
from Globals import *
from Utilities import asset_bounds, asset_val_function

#
# main LP function
#
def lp_optimizer(testing, n_assets):

    ##
    ### 1. Required Input Data Retrival
    ##

    # Get customer input
    [customer_type, customer_budget, room_type, room_area] = read_customer_input(testing)

    # Asset upper/lower bounds
    asset_bounds(room_type)

    # Global value function
    asset_val_function(testing)

    # Retrieve asset data
    item_obj_list = read_asset_data(customer_type, room_type, n_assets, testing)

    ##
    ### 2. Formulize MILP optimization problem
    ##

    print("Forming the MILP problem....")
    prob = LpProblem("The Budget Optimization Problem", LpMaximize)

    # Hardcoding to be removed later
    total_val = 0
    item_indicator_list = []
    total_price = 0
    total_area = 0
    
    # Selected items for each type and class
    item_qty = [[0] * len(item_classes) for i in range(len(item_types))]
    
    for i in range(0, len(item_obj_list)):
    	
        item_indicator_list.append(LpVariable(
            item_obj_list[i].type_item + "_" + item_obj_list[i].class_item + "_" + str(item_obj_list[i].price_item) + "_"
            + str(item_obj_list[i].area_item) + "_" + str(i), 
            0,
            None, 
            LpInteger))

        # Maximization Equation
        total_val += item_obj_list[i].value_item * item_indicator_list[i]

        # Constraint 3
        total_price += item_obj_list[i].price_item * item_indicator_list[i]

        # Constraint 4
        total_area += item_obj_list[i].area_item * item_indicator_list[i]

        # Constraint 10
        item_qty[item_types.index(item_obj_list[i].type_item)][item_classes.index(item_obj_list[i].class_item)] += item_indicator_list[i]

    ##
    ### Define Objective and Constraints
    ##

    # Objective: Maximize value
    prob += total_val, "Maximize total value of selected items"

    # Constrain 1: number of items lower bound
    prob += sum(item_indicator_list) >= 0, "Total number of items selcted is positive"

    # number of items upper bound
    prob += sum(item_indicator_list) <= 5, "Total number of items selcted is finite"

    # Constraint 3: total price <= budget
    prob += total_price <= customer_budget, "Budget Requirement"

    # Constraint 4: total area <= available area
    prob += total_area <= room_area, "Area Requirement"

    ##################################################
    #
    ## Customizable constraints
    #
    
    # Constraint 2: qty of beds <= qty of mattresses
    #prob += sum(item_qty[item_types.index("Bed")][:]) <= sum(item_qty[item_types.index("Mattress")][:]), "Bed VS Mattress QTY"

    # Constraint 9: Console qty = tv qty
    #prob += n_consoles == n_tvs, "Console VS TV QTY"

    # Constraint 6
    #prob += n_plants == n_planters

    # Constraint 7
    #prob += n_pillows == n_pillowcovers

    # Constraint 8
    #prob += n_pillows >= n_mattresses
    ###################################################

    for i in range(0, len(item_qty)):

        # Constraint 10: mutually exclusive sets, Depends upon: item type, item class
        prob += int(item_qty[i][0] > 0) ^ int(item_qty[i][1] > 0) ^ int(item_qty[i][2] > 0) == 1
        #prob += (int(item_qty[i][0] > 0) & int(item_qty[i][1] > 0) & int(item_qty[i][2] > 0) == 0)

        # Constraint 11, 12: upper and lower bounds
        prob += item_qty[i][0] + item_qty[i][1] + item_qty[i][2] >= item_lower_bounds[i, room_types.index(room_type), customer_types.index(customer_type)]
        prob += item_qty[i][0] + item_qty[i][1] + item_qty[i][2] <= item_upper_bounds[i, room_types.index(room_type), customer_types.index(customer_type)]

    print ("\nDone formulating the problem")
    
    ##
    ### 3. Run MILP solver
    ##

    print("Solving the MILP optimization....\n")

    # The problem data is written to an .lp file
    prob.writeLP("data/BudgetOptimizationVersion1.lp")

    # The problem is solved using PuLP's cbc Solver
    prob.solve(PULP_CBC_CMD())
    print("Status: ", LpStatus[prob.status])

    total_price = 0
    total_area = 0
    for v in prob.variables():

        if v.varValue > 0:
            k = v.name
            k = k.split('_')
            total_price += int(k[2])*v.varValue
            total_area += int(k[3])*v.varValue
            print '%20s' % k[0] + ", " + "Class: " + '%7s' % k[1] + ", " + "Price: " + '%4s' % k[2] + ", " + "Area: "+ '%2s' % k[3] + " =", v.varValue

    print ("Covered price: ", total_price, " Customer budget: ", customer_budget)
    print ("Covered area:  ", total_area, " Available room area: ", room_area)
    print("Total value achieved = ", value(prob.objective))

# Entry function
if __name__ == "__main__":

    testing = True
    n_assets = 1000
    print("Number of assets: ", n_assets)
    
    lp_optimizer(testing, n_assets)