print("""
----------------------------------------------

FUNCTION

- maximize code reuse and minimize redundancy
- procedural decomposition

----------------------------------------------
\n\n\n""")




"""


Note:

 def:
    creates a function object and assign it a name
    function itself does not exist until Python runs the def


"""

# function
def test():
    print("hello world")

# function with argument and default argument
def sum(a, b = 4):
     return a + b

# function arguments are pass by reference only
def update(x):
    x = 9
    print("x is " + str(x))


# Function example
test()
print("The sum is: " + str(sum(3, 3)))
print("The sum is: " + str(sum(3)))
x = 1
update(x)
printHello(True)
printHelloFor(4)
