# use "import_test" keyword to use modules (code)
# When print_test interpreter encounters an import_test keyword is search the modules in a predefined paths:
# current directory
# directory from PYTHONPATH shell variable
# your machine installation path, typically /usr/local/lib/print_test

# to import_test a specific attribute from a module use the "from ... import_test"


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
# print_test(peter.name)
#
# smith = Person.by_last_name("Smith")
# peter.info()
# Employee.count_people()
# john = Employee("John", 0)
# john.info()


# Thread with delay example
# def hello():
# #    print_test("hello, world")
# #
# #
# # def thread_delay_start(target, delay_in_seconds):
# #     if target is None or delay_in_seconds is None:
# #         return
# #
# #     thread_test = threading.Timer(delay_in_seconds, target)
# #     thread_test.start()
# #
# # thread_delay_start(hello, 4)


# Thread with timeout example
# def infinite_loop():
#     while True:
#         print_test(1, end='')
#         time.sleep(0.5)
#
#
# thread_test = threading.Thread(name="main", target=infinite_loop)
# thread_test.start()
# TIME_OUT_IN_SECONDS = 5
# thread_test.join(TIME_OUT_IN_SECONDS)

# thread_test delay example
# def thread_delay_example(target, delay_in_seconds):
#     if target is None or delay_in_seconds is None:
#         return
#
#     thread_test = threading.Timer(delay_in_seconds, target)
#     thread_test.start()
#
# def print_1():
#     print_test("1", end='')
#
# thread_delay_example(print_1, 3)


# repeating thread_test at interval example


(??)# class Interval(object):
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
#     print_test("Hello")
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
#     print_test(q.get())


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
# print_test(elapsed)


# scheduler that holds up thread_test example

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
