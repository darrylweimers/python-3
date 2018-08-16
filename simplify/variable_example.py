print("""
----------------------------------------------

ASSIGN VALUE TO VARIABLE

Syntax:
    
    variable_identifier = value 
    
Example:
""")
name = "Peter"

print("""
----------------------------------------------

MULTIPLE ASSIGNMENT

Syntax:

    variable_identifier_1 = variable_identifier_2 = value 

Note: 
    
    variable_identifier_1 and variable_identifier_2 stores the same value 
    
Example:
""")
student_1 = student_2 = "Peter"
print("Student 1:", student_1)
print("Student 2:", student_2)

print("""
----------------------------------------------

MULTIPLE ASSIGNMENT

Syntax:

    variable_identifier_1, variable_identifier_2 = value_1, value_2 

Note: 

    variable_identifier_1 stores value_1
    variable_identifier_2 stores value_2 

Example:
""")

name, identification = "Peter", 43423789
print("Name:", name)
print("Identification:", identification)


print("""
----------------------------------------------

BUILT IN DATA TYPE

    Data stored in memory can be of many types. Python offers the following types:

    Numbers
        int
        float
        complex
    String
    List
    Tuple
    Dictionary

Example:
""")

integer_number = 10
float_number = 5.6
complex_number = 5j
string = "5"
a_list = [1, 2, 3]
a_tuple = (4, 5, 6)
a_dict = {"1": "one", "2": "two"}

print("int: value->{integer} type->{type}".format(integer=integer_number, type=type(integer_number)))
print("float: value->{float_num} type->{type}".format(float_num=float_number, type=type(float_number)))
print("complex: value->{complex_num} type->{type}".format(complex_num=complex_number, type=type(complex_number)))
print("string: value->{str} type->{type}".format(str=string, type=type(string)))
print("list: value->{list} type->{type}".format(list=a_list, type=type(a_list)))
print("tuple: value->{tuple} type->{type}".format(tuple=a_tuple, type=type(a_tuple)))
print("dict: value->{dict} type->{type}".format(dict=a_dict, type=type(a_dict)))



print("""
----------------------------------------------

DATA TYPE CONVERSION

    changes a variable from one data type to another

Example:
""")
integer_number = int(float_number)
float_number = float(integer_number)
complex_number = complex(integer_number)
string = str(integer_number)
a_list = list(a_tuple)
a_tuple = tuple(a_list)


print("int: value->{integer} type->{type}".format(integer=integer_number, type=type(integer_number)))
print("float: value->{float_num} type->{type}".format(float_num=float_number, type=type(float_number)))
print("complex: value->{complex_num} type->{type}".format(complex_num=complex_number, type=type(complex_number)))
print("string: value->{str} type->{type}".format(str=string, type=type(string)))
print("list: value->{list} type->{type}".format(list=a_list, type=type(a_list)))
print("tuple: value->{tuple} type->{type}".format(tuple=a_tuple, type=type(a_tuple)))
