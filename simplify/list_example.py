print("""
----------------------------------------------

LIST

- ordered collection of objects
- store and fetch by positional offset (0, 1, 3, ...)
- nested to arbitrary depth
- value can be updated (mutable)

----------------------------------------------
\n\n\n""")



print("""
----------------------------------------------

CREATE A LIST

Syntax:

    list_name = [ item0 , item1, item2 ]

           index    0       1      2

Note:
 - item (any data type including custom class object) separated by comma
 - access by offset start from index 0

Example:
""")
print('list_1 = [0, "b", 3.0, False]')
list_1 = [0, "b", 3.0, False]
print("list:", list_1)

print("""
----------------------------------------------

SIZE OF LIST

Syntax:

   size = len(list)

Example:
""")
print("list:", list_1)

print("Number of item in list:", len(list_1))




print("""
----------------------------------------------

FETCH ALL ITEMS

Syntax:

 for item in list:
    # do something with item

Example:
""")
print("list:", list_1)

print('Fetch items:')
for item in list_1:
    print("{}".format(item), end=", ")


print("""
----------------------------------------------

FETCH ITEM

Syntax:

    item = list[index]

Example:
""")
print("list:", list_1)

print("First item:", list_1[0])
print("Last item:", list_1[len(list_1) - 1])




print("""
----------------------------------------------

UPDATE ITEM

Syntax:

    list[index] = new_value

Example:
""")
print("list:", list_1)

new_value = 4
list_1[-1] = new_value
print("Replace last item with", new_value)
print("list:", list_1)


print("""
----------------------------------------------

ADD ITEM

Syntax:

    A)  list.insert(index, new_item)
    B)  list.append(new_item)

Note
    A) Add new item to desired position in list
    B) Add new item to end of list

Example:
""")
print("list:", list_1)

print('A) list_2.insert(0, "item")')
list_1.insert(0, "item")
print("list:", list_1)

print('A) list_2.append("new item")')
list_1.append("new item")
print("list:", list_1)


print("""
----------------------------------------------

MERGE LIST

Syntax:

    new_list = list_1 + list_2

Example:
""")
print("list 1:", list_1)
list_2 = ["a", "b"]
print("list 2:", list_2)
resultant_list = list_1 + list_2
print("resultant list:", resultant_list)


print("""
----------------------------------------------

DELETE ITEM

Syntax:

    A)  del list[index]
    B)  list.remove(item)
    C)  item = list.pop(index)

Example:
""")
print("list:", list_1)

del list_1[0]
print("list:", list_1)

list_1.remove('b')
print("list:", list_1)

item = list_1.pop(0)
print("list:", list_1)
print("item pop:", item)

print("""
----------------------------------------------

REMOVE ALL ITEMS

Syntax:

    list.clear()

Example:
""")
print("list:", list_1)

print("Remove all items from list")
list_1.clear()
print("Dictionary:", list_1)



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
