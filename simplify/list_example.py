"""
List

- ordered collection of objects
- store and fetched by positional offset
- nested to arbitrary depth
- mutable

"""


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

# loop through element based on index
names = ["Peter", "John", "Jeff", "Donald", "Adams", "Jackson"]
for i in range(len(names)):
    print("Names {}: {}".format(i + 1, names[i]))

# join list of string with comma
print("Here's your list:")
new_list = ', '.join(names)
print("{}".format(new_list))

# if it contains non-string types (such as integers, floats, bools, None) then do:
floats = [3.0, 4.5, 6.6, 7.89]
new_list = ','.join(map(str, floats))
print(new_list)

# convert a list into a string and remove brace
integers = [1, 2, 3, 4]
integers_str = str(integers)
integers_str_without_brace = integers_str.strip("[]")
print(integers_str_without_brace)


