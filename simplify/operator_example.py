
print("""
----------------------------------------------
Operator

    a character which represents an action

""")


print("""
----------------------------------------------

Arithmetic Operators

     Name                   operator
    _____________________________________

    Addition                    +
    Subtraction                 -
    Multiplication              *
    Division                    /
    Floor                       //
    Exponent                    **
    Modulus                     %

Example:
""")


number_1 = 8
number_2 = 2

result = number_1 + number_2
print("Addition: {number1} + {number2} = {result}".format(number1=number_1, number2=number_2, result=result))

result = number_1 - number_2
print("Subtraction: {number1} - {number2} = {result}".format(number1=number_1, number2=number_2, result=result))

result = number_1 * number_2
print("Multiplication: {number1} * {number2} = {result}".format(number1=number_1, number2=number_2, result=result))

result = number_1 / number_2
print("Division: {number1} / {number2} = {result}".format(number1=number_1, number2=number_2, result=result))

result = number_1 // number_2
print("Division: {number1} // {number2} = {result}".format(number1=number_1, number2=number_2, result=result))

result = number_1 ** number_2
print("Exponent: {number1} ** {number2} = {result}".format(number1=number_1, number2=number_2, result=result))

result = number_1 % number_2
print("Modulus: {number1} % {number2} = {result}".format(number1=number_1, number2=number_2, result=result))


print("""
----------------------------------------------

Comparison (Relational) Operators

     Name                   operator
    _____________________________________

    Equal                   ==
    Not equal               !=
    greater than            >
    less than               <
    greater than or equal   >=
    less than or equal      <=

Compare two numbers with result given as true/false

Example:
""")


result = number_1 == number_2
print("Result of {one} == {two}: {result}".format(one=number_1, two=number_2, result=result))

result = number_1 != number_2
print("Result of {one} != {two}: {result}".format(one=number_1, two=number_2, result=result))

result = number_1 > number_2
print("Result of {one} > {two}: {result}".format(one=number_1, two=number_2, result=result))

result = number_1 < number_2
print("Result of {one} < {two}: {result}".format(one=number_1, two=number_2, result=result))

result = number_1 >= number_2
print("Result of {one} >= {two}: {result}".format(one=number_1, two=number_2, result=result))

number_2 = number_1
result = number_1 <= number_2
print("Result of {one} <= {two}: {result}".format(one=number_1, two=number_2, result=result))


print("""
----------------------------------------------

Assignment Operators
      operator      Syntax         equivalent
       = 
       +=          a += b         a = a + b  
       -=          a -= b         a = a - b 
       *=          a *= b         a = a * b
       /=          a /= b         a = a / b
       //=         a //= b        a = a // b
       **=         a **= b        a = a ** b
       %=          a %= b         a = a % b
       
Example:
""")

number_1 = 4
print("number_1: {number_1}\tnumber_2: {number_2}".format(number_1=number_1, number_2=number_2))
print("Execute: number1 += number2")
number_1 += number_2
print("number_1: {number_1}\tnumber_2: {number_2}\n".format(number_1=number_1, number_2=number_2))


number_1 = 4
print("number_1: {number_1}\tnumber_2: {number_2}".format(number_1=number_1, number_2=number_2))
print("Execute: number1 -= number2")
number_1 -= number_2
print("number_1: {number_1}\tnumber_2: {number_2}\n".format(number_1=number_1, number_2=number_2))

number_1 = 4
print("number_1: {number_1}\tnumber_2: {number_2}".format(number_1=number_1, number_2=number_2))
print("Execute: number1 *= number2")
number_1 *= number_2
print("number_1: {number_1}\tnumber_2: {number_2}\n".format(number_1=number_1, number_2=number_2))

number_1 = 4
print("number_1: {number_1}\tnumber_2: {number_2}".format(number_1=number_1, number_2=number_2))
print("Execute: number1 /= number2")
number_1 /= number_2
print("number_1: {number_1}\tnumber_2: {number_2}\n".format(number_1=number_1, number_2=number_2))

number_1 = 4
print("number_1: {number_1}\tnumber_2: {number_2}".format(number_1=number_1, number_2=number_2))
print("Execute: number1 //= number2")
number_1 //= number_2
print("number_1: {number_1}\tnumber_2: {number_2}\n".format(number_1=number_1, number_2=number_2))

number_1 = 4
print("number_1: {number_1}\tnumber_2: {number_2}".format(number_1=number_1, number_2=number_2))
print("Execute: number1 **= number2")
number_1 **= number_2
print("number_1: {number_1}\tnumber_2: {number_2}\n".format(number_1=number_1, number_2=number_2))


number_1 = 4
print("number_1: {number_1}\tnumber_2: {number_2}".format(number_1=number_1, number_2=number_2))
print("Execute: number1 %= number2")
number_1 %= number_2
print("number_1: {number_1}\tnumber_2: {number_2}\n".format(number_1=number_1, number_2=number_2))


print("""
----------------------------------------------


Logical Operators

    
    operator 
      and 
      or 
      not       reverse 

Example:
""")

a = True
b = False

print("a={a}\tb={b}".format(a=a, b=b), end="\n\n")

print('c = a and b ')
c = a and b
print('c=', c, end="\n\n")

print('c = a or b ')
c = a or b
print('c=', c, end="\n\n")

print('c = not a ')
c = not a
print('c=', c, end="\n\n")




print("""
----------------------------------------------

Bitwise Operators


Example:
""")


print("""
----------------------------------------------

Membership Operators
    
    not in 
    in 
    
Example:
""")

numbers = [1, 2, 3]
number = 1

result = number in numbers
print("Number '{number}' is in {list}. Answer: {result}".format(number=number, list=numbers, result=result))

result = number not in numbers
print("Number '{number}' is NOT in {list}. Answer: {result}".format(number=number, list=numbers, result=result))



print("""
----------------------------------------------

Identity Operators

Example:
""")

result = number in numbers
print("Number '{number}' is in {list}. Answer: {result}".format(number=number, list=numbers, result=result))


print(numbers is numbers)
print(number is numbers)