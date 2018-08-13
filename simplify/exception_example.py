print("""
----------------------------------------------

EXCEPTION

    definition:

        Exceptions are triggered automatically on errors from your code.
        If exception is not intercepted, python interpreter will crash program and show error.

    purpose:

        A way to intercept and handle error
        Event notification without the need to create result flags
        


""")

print("""
----------------------------------------------

RAISE AN EXCEPTION

    A way for a developer to signal python interpreter of an existent exception.

Syntax:

    raise Exception("message")

Example:
""")
print('raise Exception("Testing exception")')
#raise Exception("Testing exception")



print("""
----------------------------------------------

RAISE AN EXCEPTION

    A way for a developer to signal python interpreter of an existent exception.

Syntax:

    raise Exception("message")

Example:
""")
print('raise Exception("Testing exception")')
#raise Exception("Testing exception")


print("""
----------------------------------------------

EXCEPTION TRIGGER BY PYTHON INTERPRETER

Example:
""")
print('divide_by_zero = 8 / 0')
# divide_by_zero = 8 / 0


print("""
----------------------------------------------

HANDLE EXCEPTION

Syntax:

    try:
        statements that may raise exception
    except Exception_1:
        handler_1
    except (Exception_2, Exception_3):
        handler_2_and_3
    except Exception_4 as variable:
        handler_4
    except:
        general_handler
    else:
        statements if no exception
    finally:
        statements with or without exception

note:

Example:
""")

numbers = [1, 2, 3]
try:
    index = 0
    print("*FETCH OPERATION*")
    print('list:', numbers)
    print('Fetch number at index {index}:'.format(index=index))
    number = numbers[index]
# except IndexError:
#     print("Encounter index error exception")
# except IndexError as exception:
#     print("Encounter index error exception:", exception)
except Exception as exception:
    print("Encounter generalize exception:", exception)
else:
    print('Result:', number)
finally:
    print('*END OF OPERATION*')







print("""
----------------------------------------------

ASSERT

    Assert is exception
    Use assert to raise exception from the start of a long sequences of statements

Syntax:

    A) assert test, data
    B) assert test

note:

If test is false, compiler raise assert exception.
Optionally, print data if provided.

Example:
""")
x = 8
assert x != 0, "divide by zero error"
y = 5 / x
print('result:', y)




with open(r'C:\misc\data') as myfile:
    for line in myfile:
        print(line)