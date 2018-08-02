


# create
person = {"name": "John", "age": "18"}

# add single element
person["height"] = "108"
print("height is", person["height"])

# update element
person["height"] = "180"
print("height is", person["height"])

# check if key exists
if "name" in person.keys():
    print("name", "is a key of person dictionary")
else:
    print("name", "is not a key of person dictionary")

# access value using key
print("name is", person["name"])

# remove key value pair
del person["name"]

# access all
for key in person.keys():
    print("key:" + key)
for value in person.values():
    print("value:" + value)
for key, value in person.items():
    print("key:" + key + "\nvalue:" + value)

# remove all
person.clear()


#if __name__ == "__main__":