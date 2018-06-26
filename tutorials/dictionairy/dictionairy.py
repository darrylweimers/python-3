

# create
a_dictionary = {"Name": "John", "Age": "15"}

# check if key exists
if "Name" in a_dictionary.keys():
    print(True)

# access
print("First element: " + a_dictionary["Name"])

# update
a_dictionary["Name"] = "Peter"
print("Update First element: " + a_dictionary["Name"])

# remove
del a_dictionary["Name"]

# access all
for key in a_dictionary.keys():
    print("key:" + key)
for key, value in a_dictionary.values():
    print("value:" + value)
for key, value in a_dictionary.items():
    print("key:" + key + "\nvalue:" + value)

# remove all
a_dictionary.clear()


#if __name__ == "__main__":