

# Every class is a dictionary
class Class(object):
    def __init__(self):
        pass


print(Class().__dict__)

# print anything if file is called
print(" I am not main")


# Following will be call, only if this file is set as main file
if __name__ == '__main__':
    print("I am main")
