def list_summary():
    print("""
    ----------------------------------------------

    LIST

    - ordered collection of objects
    - store and fetch by positional offset (0, 1, 3, ...)
    - nested to arbitrary depth
    - value can be updated (mutable)

    ----------------------------------------------
    \n\n\n""")


def create_a_list(a_list: list):
    print("""
    ----------------------------------------------

    CREATE A LIST

    Syntax:

     list_name = [ item-0 , item-1, item-2 ]

       index         0         1        2

    Note:
     - item (any data type including custom class object) separated by comma
     - list is denoted by square bracket []
     - index start from 0

    Example:
    """)
    print("list:", a_list)
    print("\n----------------------------------------------\n\n\n")

def fetch_all_items(computation):
    print("""
    ----------------------------------------------

    FETCH ALL ITEMS

    Syntax:

     for item in list:
        statement

    Example:
    """)
    a_list = [0, "b", 3.0, False]
    print("list:", a_list)
    print('Fetch items:')
    print(computation)
    print("\n----------------------------------------------\n\n\n")



a_list = [0, "b", 3.0, False]
create_a_list([9])


items = ""
for item in a_list:
    items += "{}, ".format(item)
fetch_all_items(items)
#
#
#
# print("""
# ----------------------------------------------
#
# Size of list
#
# Syntax:
#
#    size = len(list)
#
# Example:
# """)
# a_list = [0, "b", 3.0, False]
# print("list:", a_list)
# print("Number of item in list:", len(a_list))
# print("\n----------------------------------------------\n\n\n")
#
#
#
#
# print("""
# ----------------------------------------------
#
# FETCH A ITEM
#
# Syntax:
#
#     item = list[index]
#
# Example:
# """)
# a_list = [0, "b", 3.0, False]
# print("list:", a_list)
# print("First item:", a_list[0])
# print("Last item:", a_list[len(a_list) - 1])
# print("\n----------------------------------------------\n\n\n")
#
#
#
#
# print("""
# ----------------------------------------------
#
# Update/replace item
#
# Syntax:
#
#     list[index] = new_value
#
# Example:
# """)
# a_list = [0, "b", 3.0, False]
# print("list:", a_list)
# new_value = 4
# a_list[-1] = new_value
# print("Replace last item with", new_value)
# print("list:", a_list)
# print("\n----------------------------------------------\n\n\n")
#
#
#
#
#
# print("""
# ----------------------------------------------
#
# Delete item
#
# Syntax:
#
#     del list[index]
#
# Example:
# """)
# a_list = [0, "b", 3.0, 4]
# print("list:", a_list)
# del a_list[0]
# print("list:", a_list)
# print("\n----------------------------------------------\n\n\n")



#
# # Join list into a single string
# a_list = ["1", "2", "3", "4"]
#
# print(a_list)
# print(" ".join(a_list))
#
# # slice
# # Get part of a list
#
# # create a new list from a existing list
# # new list contains element 1 to last element -1  of existing list
# sub_list = a_list[1:-1]
# print(sub_list)
#
# # create a new list from a existing list
# # new list contains element 2 to end of list
# sub_list_2 = a_list[2:]
# print(sub_list_2)
#
# # create a new list from a existing list
# # new list contains element 1 to last element, at step of 2
# sub_list_2 = a_list[0::2]
# print(sub_list_2)
#
# # loop through element based on index
# names = ["Peter", "John", "Jeff", "Donald", "Adams", "Jackson"]
# for i in range(len(names)):
#     print("Names {}: {}".format(i + 1, names[i]))
#
# # join list of string with comma
# print("Here's your list:")
# new_list = ', '.join(names)
# print("{}".format(new_list))
#
# # if it contains non-string types (such as integers, floats, bools, None) then do:
# floats = [3.0, 4.5, 6.6, 7.89]
# new_list = ','.join(map(str, floats))
# print(new_list)
#
# # convert a list into a string and remove brace
# integers = [1, 2, 3, 4]
# integers_str = str(integers)
# integers_str_without_brace = integers_str.strip("[]")
# print(integers_str_without_brace)
#
#
# # more on slice
# # https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
#
