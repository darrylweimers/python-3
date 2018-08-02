"""
List

- ordered collection of objects
- objects are stored and fetched by positional offset
- nested to arbitrary depth
- item can be changed (mutable)

"""


# more on slice
# https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/

# Create a list
alphabets = ["a", "b", "c", "d"]

# Fetch all items
print('Fetch items:')
for value in alphabets:
    print(value)
print()

# Access
print("Last element: " + alphabets[len(alphabets) - 1])

# update
alphabets[0] = "e"
print("Update last element")

# remove
del alphabets[0]

# access all



# Join list into a single string
alphabets = ["1", "2", "3", "4"]

print(alphabets)
print(" ".join(alphabets))

# slice
# Get part of a list

# create a new list from a existing list
# new list contains element 1 to last element -1  of existing list
sub_list = alphabets[1:-1]
print(sub_list)

# create a new list from a existing list
# new list contains element 2 to end of list
sub_list_2 = alphabets[2:]
print(sub_list_2)

# create a new list from a existing list
# new list contains element 1 to last element, at step of 2
sub_list_2 = alphabets[0::2]
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


