

# Every classs is a dictionary
class Class(object):
    def __init__(self):
        pass


print(Class().__dict__)

# print anything if file is called
print(" I am not main")


# Following will be call, only if this file is set as main file
if __name__ == '__main__':
    print("I am main")




# The closest equivalent to Java's toString is to implement __str__ for your class.
# Put this in your class definition:


class Foo(object):

    def __str__(self):
        return "foo"

    def __len__(self):
        return 1

foo = Foo()
print(Foo())
print(len(foo))


