from enum import Enum

print("""
----------------------------------------------

ENUM

- define a set of constants

----------------------------------------------
\n\n\n""")


print("""
----------------------------------------------

CREATE

Syntax:

    class EnumName(Enum):
        Constant_Name_1 = integer
        Constant_Name_2 = integer
        Constant_Name_n = integer

Example:
""")


class Color(Enum):
    Red = 1
    Blue = 2
    Green = 3

print(Color)


print("""
----------------------------------------------

FETCH ITEM

Syntax:

    name = EnumName.Constant_Name.name
    value = EnuName.Constant_Name.value

Example:
""")
print('Integer "{value}" represents color "{color}"'.format(value=Color.Blue.value, color=Color.Blue.name))



print("""
----------------------------------------------

COMPARE

Syntax:

    EnumName.ConstantName

Example:
""")
color = Color.Green
if color == Color.Red:
    print("use", color.name)
elif color == Color.Blue:
    print("use", color.name)
elif color == Color.Green:
    print("use", color.name)

print("""
----------------------------------------------

CONVERT INT TO ENUM

Syntax:

    EnumItem = EnumName(Integer)

Example:
""")
color = Color(Color.Blue.value)
print(color)
