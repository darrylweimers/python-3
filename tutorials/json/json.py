import json

"""
serialization
 transform date into series of bytes ( hence serial)

deserialization
 transfer series of bytes to data


json serialization 
 data to json using function:
 -dump: to file
 -dumps: to python string (json format)

python objects to JSON mapping 

Python                   JSON 
----------------------------------------
dict                    object
list, tuple             array 
str                     string
int, long, float        number
True                    true
False                   false
None                    null

json module does not encode customized data types by default
However, you can transform custom data types to JSON understandable types a shown in the mapping above 


"""

# Dictionary to json object as string
data = {"type": "type", "command": "cmd"}
json_string = json.dumps(data)
print(json_string)


# To increase readability, add indent of desired size to encoded/serialized json string
json_string = json.dumps(data, indent=2)
print(json_string)


# Deserialize json
data = json.loads(json_string)
print(data)


# Class to json object as string using special function __dict__
class Class(object):
    def __init__(self):
        pass


class_object = Class()
print(json.dumps(class_object.__dict__))


# Make a custom type json serializable

# Custom class
class Rectangle(object):
    def __init__(self, base, height):
        self._base = base
        self._height = height


META_DATA = "__" + Rectangle.__name__ + "__"


# solution: Make a custom encoder
#  - subclass of json.JSONEncoder
# - implement method default from json.JSONEncoder
class RectangleEncoder(json.JSONEncoder):
    # implements default from base class
    def default(self, obj):
        if isinstance(obj, Rectangle):
            dictionary = obj.__dict__                  # Pass minimum data required to rebuild your instance during deserializtion process. Customize your own, but must be python data types, which are recognizeable by json
            dictionary[META_DATA] = True               # add meta data for deserialization. key to indicate your class
            return obj.__dict__  # customize your own, but must be python data types, which are recognizeable by json
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


rectangle = Rectangle("5", "10")

# method 1
# call custom data type encoder encode method
encoded = RectangleEncoder().encode(rectangle)
print(encoded)

# method 2
# pass custom data type encoder to key argument cls
print(json.dumps(data, cls=RectangleEncoder))


# Deserialize custom data type

# Make your custom decoder

def rectangle_class_decoder(dictionary):
    if META_DATA in dictionary:
        return Rectangle(dictionary["_height"], dictionary["_base"])
    return dictionary


# intercede before json load tries to deserialize
# using object_hook key argument

rectangle_deserialized = json.loads(encoded, object_hook=rectangle_class_decoder)
print(rectangle_deserialized)
