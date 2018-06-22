
# create
a_dictionairy = {"Name": "John", "Age": "15"}

# access
print("First element: " + a_dictionairy["Name"])

# update
a_dictionairy["Name"] = "Peter"
print("Update First element: " + a_dictionairy["Name"])

# remove
del a_dictionairy["Name"]

# access all
for key in a_dictionairy.keys():
    print("key:" + key)
for key, value in a_dictionairy.values():
    print("value:" + value)
for key, value in a_dictionairy.items():
    print("key:" + key + "\nvalue:" + value)

# remove all
a_dictionairy.clear()
