try:
    # Operation that may throw an exception
    file = open('Testfile', "w")
    file.write("Testing exception handler")
except IOError:
    # Execute this block when an exception is raised
    print("Can't write to file")
else:
    # Execute this block if no exception
    print("Written to file")
    file.close()
finally:
    # Always execute
    print("Done!")