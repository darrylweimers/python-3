# Topic: Flow control/ Decision making

"""
Defintion: use for selecting an action base on condition
"""

"""general format
if condition1:
	execute statement1
elif condition2:
	execute statement2
else:
	execute statement3
"""

# Simple Example:
selected_plat = 'fries'

if selected_plat == 'hot dog':
   print(selected_plat, "will cost you $1.99")
elif selected_plat == "fries":
    print(selected_plat, "will cost you $0.99")
else:
    print("What would you like to eat?")

# Common usage:
plats = ['hot dog', "fries"]

if selected_plat in plats:
    print("We do sell", selected_plat)
else:
    print("We don't sell", selected_plat)


plats_cost = {'hot dog': 1.99, "fries": 0.99}



