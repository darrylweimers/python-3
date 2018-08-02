print("""
----------------------------------------------

DECLARE A STRING

Syntax:

 string_name = 'string value'
 string_name = "string value"

Note:
 - string value is enclosed between single, double or triple double quote
Example:
""")
a_string = "string"
print('string:', a_string)
a_string = 'string'
print('string:', a_string)



print("""
----------------------------------------------

STRING FORMATTING

Syntax:

 string_name = "{} {}".format("Hello", "World")

Example:
""")
string_name = "{} {}".format("Hello", "World")
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