
# line continuation
a = True
b = False

if a is True and \
   b is False:
    print("Line continuation works")

# attribute name


def some_function():
    print("name attribute:", some_function.__name__)
    print("dictionary attribute:", some_function.__dict__)

some_function()


some_list = ["4", "two", "hi"]
dictionary = dict(some_list)

