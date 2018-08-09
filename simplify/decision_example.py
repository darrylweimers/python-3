"""
    Flow control/ Decision making
"""


print("""
----------------------------------------------

if else

TAKE ACTION BASE ON CONDITION


Syntax:

    if condition1:
        execute statement1
    elif condition2:
        execute statement2
    else:
        execute statement3

Example:
""")
selected_plat = 'fries'
print("Plat selected:", selected_plat)
if selected_plat == 'hot dog':
    print(selected_plat, "will cost you $1.99")
elif selected_plat == "fries":
    print(selected_plat, "will cost you $0.99")
else:
    print("What would you like to eat?")




print("""
----------------------------------------------

BETWEEN RANGE


Syntax:

    if 0 <= number <= 4:
        # do something

Example:
""")
number = 3
print("Number:", number)
if 0 <= number <= 4:
    print(number, "is between range of 0-4")



print("""
----------------------------------------------

ALL CONDITIONS SATISFY


Syntax:

    if condition1 and condition2:
        # do something

Example:
""")
have_passport = True
have_flight_ticket = True
print("Have passport:", have_passport)
print("Have flight ticket:", have_flight_ticket)
if have_flight_ticket and have_flight_ticket:
    print("You CAN board.")


print("""
----------------------------------------------

SOME CONDITION SATISFY


Syntax:

    if condition1 or condition2:
        # do something

Example:
""")
have_passport = True
have_flight_ticket = False
print("Have passport:", have_passport)
print("Have flight ticket:", have_flight_ticket)
if not have_flight_ticket or not have_flight_ticket:
    print("You CAN'T board.")

print("""
----------------------------------------------

ITEM IS IN LIST


Syntax:

    if item in list:
        # do something

Example:
""")
plats = ['hot dog', "fries"]
print("Plats:", plats)
print("Plat:", selected_plat)
if selected_plat in plats:
    print(selected_plat, "is available")




