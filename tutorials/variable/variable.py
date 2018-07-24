
# Multiple variable declaration
HOST, PORT = "localhost", 9999



# global variable
name = "Darryl"

def print_name():
    global name # declare using the global variable
    name = "John"
    print(name)

print_name()
print(name)
