# more on slice
# https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/

# create a list
a_list = ["a", "b", "c", "d"]

# access
print("Last element: " + a_list[len(a_list) - 1])

# update
a_list[0] = "e"
print("Update last element")

# remove
del a_list[0]

# access all
for value in a_list:
    print(value)


# Join list into a single string
a_list = ["1", "2", "3", "4"]

print(a_list)
print(" ".join(a_list))

# slice
# Get part of a list

# create a new list from a existing list
# new list contains element 1 to last element -1  of existing list
sub_list = a_list[1:-1]
print(sub_list)

# create a new list from a existing list
# new list contains element 2 to end of list
sub_list_2 = a_list[2:]
print(sub_list_2)

# create a new list from a existing list
# new list contains element 1 to last element, at step of 2
sub_list_2 = a_list[0::2]
print(sub_list_2)



