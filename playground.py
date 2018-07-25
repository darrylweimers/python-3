# use "import" keyword to use modules (code)
# When python interpreter encounters an import keyword is search the modules in a predefined paths:
# current directory
# directory from PYTHONPATH shell variable
# your machine installation path, typically /usr/local/lib/python

# to import a specific attribute from a module use the "from ... import"


import threading
import queue
from collections import deque
from enum import Enum
import time
#Elapse time example
import datetime
# scheduler example
import sched
import time




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
# def hello():
# #    print("hello, world")
# #
# #
# # def thread_delay_start(target, delay_in_seconds):
# #     if target is None or delay_in_seconds is None:
# #         return
# #
# #     thread = threading.Timer(delay_in_seconds, target)
# #     thread.start()
# #
# # thread_delay_start(hello, 4)


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


# class_test Interval(object):
#
#     def __init__(self, interval, target):
#         super().__init__()
#         self._target = target
#         self._interval = interval
#
#     def start(self):
#         self._delay()
#
#     def stop(self):
#         self._interval = False
#
#     def _delay(self):
#         if self._interval:
#             self._target()
#             threading.Timer(self._interval, self._delay).start()
#
# def print_hello():
#     print("Hello")
#
# r = Interval(0.5, print_hello)
# r.start()
# r.interval = 1
# time.sleep(10)
# r.stop()




# Queue example
# q = queue.Queue()
#
# for i in range(5):
#     q.put(i)
#
# while not q.empty():
#     print(q.get())


# Enum example
# class_test OutputType(Enum):
#     DIGITAL = 1
#     ANALOG = 2

# circular buffer example
# class_test CircularBuffer(deque):
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


# Elapse time example


# start = datetime.datetime.now()
# time.sleep(5)
# end = datetime.datetime.now()
# elapsed = end - start
# print(elapsed)


# scheduler that holds up thread example

def print_event(name):
    print('EVENT:', time.time(), name)


scheduler = sched.scheduler(time.time, time.sleep)
print('START:', time.time())
scheduler.enter(10, 1, print_event, ('first',))
scheduler.run()
counter = 5
while counter != 0:
    print("running other stuff")
    time.sleep(0.5)
    counter -= 1
