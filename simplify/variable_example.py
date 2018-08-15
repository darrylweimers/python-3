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

