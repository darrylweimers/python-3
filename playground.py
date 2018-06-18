# use "import" keyword to use modules (code)
# When python interpreter encounters an import keyword is search the modules in a predefined paths:
# current directory
# directory from PYTHONPATH shell variable
# your machine installation path, typically /usr/local/lib/python

# to import a specific attribute from a module use the "from ... import"

from scrapy.mail import MailSender

# Tips
# Start a line with sharp (#) to create a comment
# newline to seperate function/class from other code
# start a scope with colon : follow by indented code

# function
def test():
    print("hello world")

#function with argument and default argument
def sum(a, b = 4):
     return a + b

#function arguments are pass by reference only
def update(x):
    x = 9
    print("x is " + str(x))

#decision making: if and else
def printHello(value):
    if value is True:
        print("Hello world")
    else:
        print("Input true to print hello world")

#loops
def printHelloFor(numberOfTimes):
    while(numberOfTimes):
        print("Hello")
        numberOfTimes -= 1

#list
def printList():
    #create
    aList = ["a", "b", "c", "d"]
    #access
    print("Last element: " + aList[len(aList) - 1])
    #update
    aList[0] = "e"
    print("Update last element")
    #remove
    del aList[0]
    #access all
    for value in aList:
        print(value)

#tuple
def tupleExample():
    tup = (5, "kids")
    print("we have " + str(tup[0]) + " " + tup[1])


#dictionairy
def dictionairyExample():
    #create
    aDictionairy = {"Name": "John", "Age": "15"}
    #access
    print("First element: " + aDictionairy["Name"])
    #update
    aDictionairy["Name"] = "Peter"
    print("Update First element: " + aDictionairy["Name"])
    #remove
    del aDictionairy["Name"]
    #access all
    for key in aDictionairy.keys():
        print("key:" + key)
    for key, value in aDictionairy.values():
        print("value:" + value)
    for key, value in aDictionairy.items():
        print("key:" + key + "\nvalue:" + value)
    #remove all
    aDictionairy.clear()

#import send a mail using an imported module name "scrapy"
def sendMail():
    mailer = MailSender()
    mailer.send(to=["darrylweimers@gmail.com"], subject="Test", body="Body")

# exception handler
def exceptionHandlerExample():
    try:
        # Operation that may throw an exception
        file = open('Testfile', "w")
        file.write("Testing exception handler")
    except IOError:
        # Execute this block when an exception is raised
        print("Can't write to file")
    else:
        # Execute this block if no exception
        print("Written to file")
        file.close()
    finally:
        # Always execute
        print("Done!")


# class
# re-useable blueprint with attributes and functions
class Person:
    # class variable shared by instances
    count = 0

    # special method called constructor/initialization method
    # to create an object from class blueprint
    def __init__(self, name):
        self.name = name  # instance variable
        Person.count += 1


    # class method which can be called by class only
    # first argument must be cls
    # differs from static method in the way that it can be easily be use by child class
    # commonly used as inheritable alternative constructor
    @classmethod
    def by_last_name(cls, name):
        return cls(name)

    @staticmethod
    def count_people():
        print("Number of person object: " + str(Person.count))

    # instance method, which can only be called by an object of Person
    # first argument must be self to indicate that function is an instance method
    def info(self):
        print("name: " + self.name)     # Notation self.[instance-variable] to access instance variable


# class
# inheritance
# wrap parent class with parenthesis after class name
class Employee(Person):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id

    # override parent class instance method
    def info(self):
        super().info()
        print("id: " + str(self.id))


# Function example
# test()
# print("The sum is: " + str(sum(3, 3)))
# print("The sum is: " + str(sum(3)))
# x = 1
# update(x)
# printHello(True)
# printHelloFor(4)


# List example
# printList()

# Tuple exception
# tupleExample()

# Dictionary Exception
# dictionairyExample()

# Module example
# sendMail()

# Exception example
# exceptionHandlerExample()



# Class Example
peter = Person("Peter")
smith = Person.by_last_name("Smith")
peter.info()
Employee.count_people()
john = Employee("John", 0)
john.info()
