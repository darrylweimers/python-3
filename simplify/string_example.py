print(r"""
----------------------------------------------

DECLARE A STRING

Syntax:

 A) string_name = 'string value'
 B) string_name = "string value"

Example:
""")
a_string = 'Shop'
print('string:', a_string)
a_string = "Restaurant"
print('string:', a_string)

print("""
----------------------------------------------

SIZE

Syntax:

   size = len(string)

Example:
""")
print('string:', a_string)

print("Number of characters", len(a_string))



print(r"""
----------------------------------------------

ESCAPE SEQUENCE

  common: escape sequences
          newline       \n
          tab           \t
          single quote  \'
          double quote  \"

Syntax:

  string = '\tstring\tvalue\n'

Example:
""")
a_string = "Dear\tRamsay,\nI am writing this \"letter\"..."
print('string:', a_string)


print(r"""
----------------------------------------------

RAW STRING

  Like normal string with escape sequence ignored.

Syntax:

  string = r'\tstring\tvalue\n'

Example:
""")
a_string = r"Dear\tRamsay,\nI am writing this \"letter\"..."
print('string:', a_string)


print("""
----------------------------------------------

STRING FORMATTING

Syntax:

 A) Relative position

    string = "{} {}".format("Hello", "World")

 B) Position

    string = "{0} {1}".format("Hello", "World")

 C) Keyword
    string = "{hi} {world}".format(hi="hello", world="World")

Example:
""")
string_name = "{} {}".format("Hello", "World")
print(string_name)
string_name = "{0} {0} {1}".format("Hello", "World")
print(string_name)
string_name = "{intro} {to}".format(intro="Hello", to="World")
print(string_name)

print("""
----------------------------------------------

STRING CONCATENATION

Syntax:

 final_string = string1 + string2

Example:
""")
string1 = "Hello"
string2 = " World"
print("String 1:", string1)
print("String 2:", string2)
resultant_string = string1 + string2
print(string_name)


print("""
----------------------------------------------

REMOVE LEADING AND TRAILING WHITE SPACE

Syntax:

 some_string = " string "
 result = some_string.strip()

Example:
""")
a_string = " some string "
print('original string:' + a_string)
a_string = a_string.strip()
print('new string:' + a_string)



print("""
----------------------------------------------

FIND CHARACTER IN STRING

Syntax:

 some_string = " string "
 character = 's'
 result = some_string.find(character)

Example:
""")
a_string = "Awesome"
print("String:", a_string)
character = 's'
print("Character", character, 'was first found at index', a_string.find(character))



print("""
----------------------------------------------

REPLACEMENT

    replace all occurrence of a string

Syntax:

    resultant_string = string.replace('to replace', 'replacement')

Example:
""")
a_string = "Idealistic"
replace = "listic"
replacement = 'l'
print('string:', a_string)
print('Replace "{}" by "{}"'.format(replace, replacement))
resultant_string = a_string.replace(replace, replacement)
print('string:', resultant_string)



#
# # catch empty string
# empty_string = ""
# print("From string: ", empty_string)
# if not empty_string:
#     print("It is a empty string")
#
#
# # string to byte
# 'data'.encode('utf-8')