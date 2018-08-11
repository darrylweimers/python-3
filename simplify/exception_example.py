print("""
----------------------------------------------

EXCEPTION

Unexpected exception , that is triggered by python compiler or user code,
can crash a program if not handle.

----------------------------------------------
\n\n\n""")

print("""
----------------------------------------------

RAISE EXCEPTION

Syntax:

    raise Exception("message")

Example:
""")

print("""
----------------------------------------------

HANDLE EXCEPTION

Syntax:

    try:
        statements
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
        statements to run with or without exception

Example:
""")




# try:
#     # Operation that may throw an exception
#     file = open('Testfile', "w")
#     file.write("Testing exception handler")
# except IOError:
#     # Execute this block when an exception is raised
#     print("Can't write to file")
# else:
#     # Execute this block if no exception
#     print("Written to file")
#     file.close()
# finally:
#     # Always execute
#     print("Done!")


# raise exception
# throw/raise an exception when certain condition occurs
def function_raise_exception():
    raise Exception("Illegal action")


# capture the exception
def capture_exception():
    try:
        function_raise_exception()
    except Exception as ex:
        print(ex)

# capture the exception and arguments


def capture_exception():
    try:
        function_raise_exception()
    except Exception as ex:
        print(ex)
