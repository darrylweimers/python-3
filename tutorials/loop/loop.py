

# while loop

# Repeat body until condition is not true
# else clause is run if the body of the loop is never executed,
count = 5

while count:
    print(count, end=", ")
    count -= 1
else:
    print("Can't count")

# find 3
count = 0
while True:
    count += 1
    if count == 3:
        break


"""
for target in object:       # Assign object items to target
    statements
if test: break              # exit repetition
if test: continue           # skip this iteration
else:                       # execute if for loop body never executes
statements
"""


# else clause
for index in range(0):
    print(index)
else:
    print("None evaluated")

# print event numbers
for number in range(0, 5):
    if number % 2 != 0:
        continue
    print(number, end=", ")

# for index in range(5):
#     print(index)
#
# for index in range(2, 5, 2):
#     print(index)

# list = [5, 4, 6, 7]

# for index in range(len(list)):
#     print(list[index], end="")

# for element in list:
#     print(element, end="")


# grocery_list = {"bacon": 3.99, "egg": 2.99, "bread": 1.99}
#
# for item in grocery_list:
#     print(item, end=", ")
#
# for item in grocery_list.keys():
#     print(item, end=",")
#
# for price in grocery_list.values():
#     print(price, end=", ")
#
# for item, price in grocery_list.items():
#     print(item, ":", price, end=", ")

