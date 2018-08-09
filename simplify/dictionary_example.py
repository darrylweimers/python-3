"""
Dictionary

is a mapping of unique keys to values

- unordered collection
- items are stored and fetched by key
- keys are unique
- item can be changed (mutable)
"""


print("""
----------------------------------------------

CREATE A DICTIONARY

Syntax:

    A)  dictionary = { key1: value1, key2: value2 }
    B)  dictionary = dict(key1=value1, key2=value2)

Example:
""")
key1 = "name"
value1 = "John"
print("Key:", key1, "\tValue:", value1)
key2 = "age"
value2 = 15
print("Key:", key2, "\tValue:", value2)
person_attributes = {key1: value1, key2: value2}
print("Dictionary:", person_attributes)
person_attributes = dict(name=value1, age=value2)
print("Dictionary:", person_attributes)

print("""
----------------------------------------------

SIZE OF DICTIONARY

Syntax:

    size = len(dictionary)

Example:
""")
print("Dictionary:", person_attributes)
print("Number of item in dictionary:", len(person_attributes))



print("""
----------------------------------------------

FETCH ALL KEYS

Syntax:

    for key in dictionary.keys():
        # use key

Example:
""")
print("Dictionary:", person_attributes)
print('Fetch keys:')
for key in person_attributes.keys():
    print("{}".format(key), end=", ")


print("""
----------------------------------------------

FETCH ALL VALUES

Syntax:

    for value in dictionary.values():
        # use value

Example:
""")
print("Dictionary:", person_attributes)
print('Fetch values:')
for value in person_attributes.values():
    print("{}".format(value), end=", ")



print("""
----------------------------------------------

FETCH ALL ITEMS

Syntax:

    for key, value in dictionary.items():
        # use key and value

Example:
""")
print("Dictionary:", person_attributes)
print('Fetch key and value:')
for key, value in person_attributes.items():
    print("({}: {})".format(key, value), end=", ")



print("""
----------------------------------------------

CHECK IF KEY EXISTS

Syntax:

    if key in dictionary.keys():
        # use key

Example:
""")
if key1 in person_attributes.keys():
    print('key:', key1, "is in keys:", list(person_attributes.keys()))
else:
    print('key:', key1, "is not in keys:", list(person_attributes.keys()))


print("""
----------------------------------------------

FETCH VALUE BY KEY

Syntax:

    A)  value = dictionary[key]
    B)  value =  dictionary.get(key)
                OR
        value =  dictionary.get(key, default)
    C)  value = dictionary.pop(key)
                OR
        value = dictionary.pop(key, default)

Note:
A) If key doesn't exist, program will crash.
B) If key doesn't exist, a default value will be returned.
    Default value is None by default, but a value may be supplied.
C) Same as option B with item being removed from dictionary


Example:
""")
print("Dictionary:", person_attributes)

print('A) Fetch value by key "{}": {}'.format(key1, person_attributes[key1]))
print("Dictionary:", person_attributes)

print('B) Fetch value by key "{}": {}'.format(key1, person_attributes.get(key1)))
print("Dictionary:", person_attributes)

print('C) Fetch value by key "{}": {}'.format(key1, person_attributes.pop(key1)))
print("Dictionary:", person_attributes)


print("""
----------------------------------------------

MERGE DICTIONARIES

Syntax:

    dictionary1.update(dictionary2)

Example:
""")
print("Dictionary 1:", person_attributes)
employee_attributes = {"id": 2347, 'age': 23, 'name': "George"}
print("Dictionary 2:", employee_attributes)
person_attributes.update(employee_attributes)
print("Dictionary 1:", person_attributes)



print("""
----------------------------------------------

UPDATE VALUE BY KEY OR ADD NEW ITEM

Syntax:

    dictionary[key] = value

Note:
    if key exist, update value
    if key doesn't, add item
Example:
""")
print("Dictionary:", person_attributes)

new_value = "Peter"
print("Update value", person_attributes[key1], "with new value", new_value, "using key:", key1)
person_attributes[key1] = new_value
print("Dictionary:", person_attributes)

person_attributes['mobile'] = "514-939-2069"
print("Dictionary:", person_attributes)


print("""
----------------------------------------------

REMOVE ITEM BY KEY

Syntax:

    del dictionary[key]

Example:
""")
print("Dictionary:", person_attributes)
print('Remove value "{}" by key "{}"'.format(person_attributes[key], key))
del person_attributes[key]
print("Dictionary:", person_attributes)


print("""
----------------------------------------------

REMOVE ALL ITEMS

Syntax:

    dictionary.clear()

Example:
""")
print("Dictionary:", person_attributes)
print("Remove all items from dictionary")
person_attributes.clear()
print("Dictionary:", person_attributes)




# advance
#D = {x: x*2 for x in range(10)}



