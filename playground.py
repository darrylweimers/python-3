# use "import" keyword to use modules (code)
# When python interpreter encounters an import keyword is search the modules in a predefined paths:
# current directory
# directory from PYTHONPATH shell variable
# your machine installation path, typically /usr/local/lib/python

# to import a specific attribute from a module use the "from ... import"

from scrapy.mail import MailSender

import threading
import queue
from collections import deque
from enum import Enum
import time


# Tips
# Start a line with sharp (#) to create a comment
# newline to seperate function/class from other code
# start a scope with colon : follow by indented code

"""
Code convention
Constants: all capital letters with underscores separating words.
            MAX_LEN = 9

Comments: 
    Write docstrings for all public modules, functions, classes, and methods.
    
Single line comments     
# Write comments after sharp and space 
    
"""

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
        self._name = name  # private instance variable is preceded with a underscore _ to indicate private
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

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


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
# peter = Person("Peter")
# print(peter.name)
#
# smith = Person.by_last_name("Smith")
# peter.info()
# Employee.count_people()
# john = Employee("John", 0)
# john.info()


# Thread with delay example
#def hello():
#    print ("hello, world")


#t = threading.Timer(5.0, hello)
#t.start() # after 30 seconds, "hello, world" will be printed


# Thread with timeout example
# def infinite_loop():
#     while True:
#         print(1, end='')
#         time.sleep(0.5)
#
#
# thread = threading.Thread(name="main", target=infinite_loop)
# thread.start()
# TIME_OUT_IN_SECONDS = 5
# thread.join(TIME_OUT_IN_SECONDS)



# thread delay example
# def thread_delay_example(target, delay_in_seconds):
#     if target is None or delay_in_seconds is None:
#         return
#
#     thread = threading.Timer(delay_in_seconds, target)
#     thread.start()
#
# def print_1():
#     print("1", end='')
#
# thread_delay_example(print_1, 3)


# repeating thread at interval example


class Interval(object):

    def __init__(self, interval, target):
        super().__init__()
        self._target = target
        self._interval = interval

    def start(self):
        self._delay()

    def stop(self):
        self._interval = False

    def _delay(self):
        if self._interval:
            self._target()
            threading.Timer(self._interval, self._delay).start()

def print_hello():
    print("Hello")

r = Interval(0.5, print_hello)
r.start()
r.interval = 1
time.sleep(10)
r.stop()


# Queue example
# q = queue.Queue()
#
# for i in range(5):
#     q.put(i)
#
# while not q.empty():
#     print(q.get())


# Enum example
# class OutputType(Enum):
#     DIGITAL = 1
#     ANALOG = 2

# circular buffer example
# class CircularBuffer(deque):
#     def __init__(self, size=0):
#         super().__init__(maxlen=size)
#
#     @property
#     def average(self):  # TODO: Make type check for integer or floats
#         return sum(self)/len(self)
#
#
# cb = CircularBuffer(size=10)
# for i in range(20):
#     cb.append(i)
#     print("%s" % (str(cb)))





