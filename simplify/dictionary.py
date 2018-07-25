"""
Dictionary

- unordered collections
- items are stored and fetched by key
- key is unique; it is a set

"""

D = {x: x*2 for x in range(10)}

# Create
key = "name"
value = "John"
person_attributes = {key: value, "age": 15}

# Fetch all keys
print('Fetch keys:')
for key in person_attributes.keys():
    print("{}".format(key), end=", ")
print()

# Fetch all values
print('Fetch values:')
for value in person_attributes.values():
    print("{}".format(value), end=", ")
print()

# Fetch all items
print('Fetch key and value:')
for key, value in person_attributes.items():
    print("({}: {})".format(key, value), end=", ")
print()

# Check if key exists
if key in person_attributes.keys():
    print('key:', key, "is in keys:", list(person_attributes.keys()))
else:
    print('key:', key, "is not in keys:", list(person_attributes.keys()))

# Fetch a value with key
print("Fetch", person_attributes[key], "with key:", key)

# Update value with key
new_value = "Peter"
person_attributes[key] = new_value
print("Update key:", key, "with value", new_value)
print("Fetch", person_attributes[key], "with key:", key)

# Remove value with key
print('Remove value:', person_attributes[key], 'using key', key)
del person_attributes[key]

if key in person_attributes.keys():
    print('key:', key, "is in keys:", list(person_attributes.keys()))
else:
    print('key:', key, "is not in keys:", list(person_attributes.keys()))


# Remove all
person_attributes.clear()
