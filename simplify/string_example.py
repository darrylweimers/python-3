import  string



# Declare a string

a_string = "string"
print(a_string)
a_string = 'string'
print(a_string)

var = 4
var2 = 6.0
a_string = f"value {var} {var2}"
print(a_string)
# basic string format
CONST = "{}"
print(CONST.format("WORKS"))
# string to byte
'data'.encode('utf-8')

# use strip function
# remove trailing or leading whitespace
a_string = a_string.strip()
print(a_string)

# find a character in string
print("From string: ", a_string)
character = 's'
print("From string:", character, "result:", a_string.find(character))
character = 'm'
print("From string:", character, "result:", a_string.find(character))

# catch empty string
empty_string = ""
print("From string: ", empty_string)
if not empty_string:
    print("It is a empty string")

# string format

a_string = '{} {}'.format("Peter", "Pan")
print(a_string)
