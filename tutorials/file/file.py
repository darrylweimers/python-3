import os

# absolute path of current file
print("absolution path of current file: ", os.path.abspath(__file__))

# absolute path of file in the same folder of this file
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
print(path)

# current working directory
print(os.getcwd())
