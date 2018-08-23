"""
Dictionary

is a mapping of unique keys to values

- unordered collection
- items are stored and fetched by key
- keys are unique
- item can be changed (mutable)
"""

# print("""
# ----------------------------------------------
#
# CREATE A DICTIONARY
#
# Syntax:
#
#     A)  dictionary_identifier = { key1: value1, key2: value2 }
#     B)  dictionary_identifier = dict(key1=value1, key2=value2)
#
# Example:
# """)
#
# key_1 = "name"
# value_1 = "Peter"
#
# key_2 = "age"
# value_2 = 21
#
#
# print("key_1: {key}\t value_1: {value}".format(key=key_1, value=value_1))
# print("key_2: {key}\t value_2: {value}".format(key=key_2, value=value_2))
#
# print("Option A:")
# dictionary_1 = {key_1: value_1, key_2: value_2}
# print("dictionary_1:", dictionary_1)
#
# print("Option B:")
# dictionary_2 = dict(name=value_1, age=value_2)
# print("dictionary_2:", dictionary_2)













































#
# print("""
# ----------------------------------------------
#
# SIZE OF DICTIONARY
#
# Syntax:
#
#     size = len(dictionary_identifier)
#
# Example:
# """)
#
# print("dictionary_1:", dictionary_1)
# print("Number of items in dictionary_1:", len(dictionary_1))
















































# print("""
# ----------------------------------------------
#
# FETCH ALL KEYS
#
# Syntax:
#
#     for key in dictionary_identifier.keys():
#         statement(s)
#
# where
#          statement(s):   line(s) of code
# Example:
# """)
#
# print("dictionary_1:", dictionary_1)
#
# print("Fetch all keys:")
# for key in dictionary_1.keys():
#     print(key)
#















































# print("""
# ----------------------------------------------
#
# FETCH ALL VALUES
#
# Syntax:
#
#     for value in dictionary_identifier.values():
#         statement(s)
#
# where
#          statement(s):   line(s) of code
# Example:
# """)
#
# print("dictionary_1:", dictionary_1)
#
# print("Fetch all values:")
# for value in dictionary_1.values():
#     print(value)


















































# print("""
# ----------------------------------------------
#
# FETCH ALL ITEMS
#
# Syntax:
#
#     for key, value in dictionary_identifier.items():
#         statement(s)
#
# where
#          statement(s):   line(s) of code
# Example:
# """)
#
# print("dictionary_1:", dictionary_1)
#
# print("Fetch all items:")
# for key, value in dictionary_1.items():
#     print("{key}: {value}".format(key=key, value=value))
#
#















































# print("""
# ----------------------------------------------
#
# CHECK IF KEY EXISTS
#
# Syntax:
#
#     if key in dictionary_identifier.keys():
#         statement(s)
#
# where
#          statement(s):   line(s) of code
# Example:
# """)
#
#
# print("dictionary_1:", dictionary_1)
#
# if "name" in dictionary_1.keys():
#     print("among keys")
# else:
#     print("not among keys")
















































print("""
----------------------------------------------

FETCH VALUE BY KEY

Syntax:

    A)  value = dictionary_identifier[key]

    B)  value =  dictionary_identifier.get(key)

                OR

        value =  dictionary_identifier.get(key, default)

    C)  value = dictionary_identifier.pop(key)

                OR

        value = dictionary_identifier.pop(key, default)

Note:
A) If key doesn't exist, program will crash.
B) If key doesn't exist, a default value will be returned.
    Default value is None by default, but a value may be supplied.
C) Same as option B with item being removed from dictionary


Example:
""")

key_1 = "name"
value_1 = "Peter"

key_2 = "age"
value_2 = 21

dictionary_1 = {key_1: value_1, key_2: value_2}

print("dictionary_1:", dictionary_1)

print("Option A:")
print('Fetch value by key "{key}": {value}'.format(key=key,value=value)
# print("Dictionary:", person_attributes)
#
# print('A) Fetch value by key "{}": {}'.format(key1, person_attributes[key1]))
# print("Dictionary:", person_attributes)
#
# print('B) Fetch value by key "{}": {}'.format(key1, person_attributes.get(key1)))
# print("Dictionary:", person_attributes)
#
# print('C) Fetch value by key "{}": {}'.format(key1, person_attributes.pop(key1)))
# print("Dictionary:", person_attributes)















































# print("""
# ----------------------------------------------
#
# MERGE DICTIONARIES
#
# Syntax:
#
#     dictionary_identifier_1.update(dictionary_identifier_2)
#
# Note:
#
#     After operation, dictionary_identifier_2 items is added to
#     dictionary_identifier_1
#
#
# Example:
# """)
# print("Dictionary 1:", person_attributes)
# employee_attributes = {"id": 2347, 'age': 23, 'name': "George"}
# print("Dictionary 2:", employee_attributes)
# person_attributes.update(employee_attributes)
# print("Dictionary 1:", person_attributes)
















































# print("""
# ----------------------------------------------
#
# UPDATE VALUE BY KEY OR ADD NEW ITEM
#
# Syntax:
#
#     dictionary_identifier[key] = value
#
# Note:
#     if key exist, update value
#     if key doesn't, add item
#
# Example:
# """)
# print("Dictionary:", person_attributes)
#
# new_value = "Peter"
# print("Update value", person_attributes[key1], "with new value", new_value, "using key:", key1)
# person_attributes[key1] = new_value
# print("Dictionary:", person_attributes)
#
# person_attributes['mobile'] = "514-939-2069"
# print("Dictionary:", person_attributes)















































# print("""
# ----------------------------------------------
#
# REMOVE ITEM BY KEY
#
# Syntax:
#
#     del dictionary_identifier[key]
#
# Example:
# """)
# print("Dictionary:", person_attributes)
# print('Remove value "{}" by key "{}"'.format(person_attributes[key], key))
# del person_attributes[key]
# print("Dictionary:", person_attributes)















































# print("""
# ----------------------------------------------
#
# REMOVE ALL ITEMS
#
# Syntax:
#
#    dictionary_identifier.clear()
#
# Example:
# """)
# print("Dictionary:", person_attributes)
# print("Remove all items from dictionary")
# person_attributes.clear()
# print("Dictionary:", person_attributes)

























































# advance
#D = {x: x*2 for x in range(10)}



