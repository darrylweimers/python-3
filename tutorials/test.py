#from tutorials.system import_test system
#from tutorials.list.list_test import *
#from tutorials.loop import_test loop
#from tutorials.json.json_test import *
#import tutorials.string.string
#import tutorials.special_variables.special_variables
from tutorials.enum.enum_example import *
#from tutorials.dictionairy import_test dictionairy
#from tutorials.config import_test config
#from tutorials.tuple import_test tuple
#import_test tutorials.type_conversion.TypeConversion
#import_test tutorials.other.other
#import_test tutorials.operator.operator
#import_test tutorials.file.file
#from tutorials.classs.classs import_test *
#import_test tutorials.async.async
#import_test tutorials.thread_test.thread_test
#import_test tutorials.variable.variable
#from tutorials.import_test.import_test import *
#import tutorials.print_test.print_test
#from tutorials.exception.exception import function_raise_exception, capture_exception


#
# import_test subprocess
#
# # calling subprocess
# # subprocess.call("echo $HOME", shell=True)
# # subprocess.call("ls -l", shell=True)
#
#
# # capture output
# output = subprocess.check_output("ls -l", shell=True)
# print_test(output)


# class Buffer(object):
#
#     def __init__(self, terminator: str = '\n'):
#         super().__init__()
#         self._terminator = terminator
#         self._buffer = []
#         self._remaining = None
#
#     def _store_remaining(self, buffer: list):
#         if len(buffer):
#             self._remaining = buffer.pop(-1)
#
#     def _concatenate_to_main_buffer(self, buffer: list):
#         if len(buffer):
#             self._buffer += buffer
#
#     def _add_remaining(self, data):
#         if self._remaining:
#             data = self._remaining + data
#             self._remaining = None
#             return data
#         return data
#
#     def append(self, data):
#         data = self._add_remaining(data)
#         temp_buffer = data.split(self._terminator)
#         self._store_remaining(temp_buffer)
#         self._concatenate_to_main_buffer(temp_buffer)
#
#     def pop_first_element(self):
#         if len(self._buffer):
#             return self._buffer.pop(0)
#         return None
#
#     def __len__(self):
#         return len(self._buffer)
#
#
# # data = "some\n"
# # buffer = data.split("\n")
# # if len(buffer):
# #     left_over = buffer[-1]
# #     print(buffer)
#
# data1 = "OTHERLINES\n"
# data2 = "OTHERLINES\nsdfjksjfkjsdkfjlsdjfjsfd"
# data3 = "OTHERLINES\njfksdjfkljdsf\nsdfhkjsdhf"
# data4 = "OTHERLINES"
#
# buffer = Buffer()
# buffer.append(data1)
# buffer.append(data2)
# buffer.append(data3)
# buffer.append(data4)
# print(buffer)
#
# print(buffer.pop_first_element())
# data5 = "12334234234234324234234\n"
# buffer.append(data5)
# print(len(buffer))


