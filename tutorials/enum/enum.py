from enum import Enum


class Color(Enum):
    Red = 1
    Blue = 2
    Green = 3


print(type(Color.Blue))
print("Color", Color.Blue.name, " has value", Color.Blue.value)
