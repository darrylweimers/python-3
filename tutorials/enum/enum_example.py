from enum import Enum


class Color(Enum):
    Red = 1
    Blue = 2
    Green = 3


# enum get name/value
print(type(Color.Blue))
print("Color", Color.Blue.name, " has value", Color.Blue.value)

# Convert int to enum
color = Color(Color.Blue.value)
print(color)