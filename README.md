# python-3
Python tutorial

# Tip
pip is a package management system used to install and manage software packages written in Python

To use another version of pip for python:

default version of pip                          pip --version

python version 2                                pip2 --version

python version 3                                pip3 --version                                   


install pip3:

sudo apt-get install python3-pip

## Comments
Start a line with sharp (#) to create a comment


## Code Conventions
Follow code conventions PEP8 at https://www.python.org/dev/peps/pep-0008/#type-variable-names
-newline to separate function/class from other code
-start a scope with colon : follow by indented code
-Function and variable names should be lowercase, with words separated by underscores as necessary to improve readability.
-Constants: all capital letters with underscores separating words.
            MAX_LEN = 9
            Comments:
-Write docstrings for all public modules, functions, classes, and methods.
-Single line comments:# Write comments after sharp and space
-Function and variable names should be lowercase, with words separated by underscores as necessary to improve readability.

# Tips
start a scope with colon : follow by indented code
python don't support constructor overload
python dont support static class, Python modules are sufficient for grouping related functions
if you have import error, make sure you don't have circular dependent imports



### use official documents:
https://docs.python.org/3/tutorial/index.html

### Interesting website
about function fix type : https://stackoverflow.com/questions/2489669/function-parameter-types-in-python
about if __main__==__name__: https://stackoverflow.com/questions/419163/what-does-if-name-main-do
module constants are public only, to show that constant was intended to be private start constant with underscore: https://stackoverflow.com/questions/1547145/defining-private-module-functions-in-python
python ternary operator: https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator
python does not have switch operator

is vs equal: https://stackoverflow.com/questions/2988017/string-comparison-in-python-is-vs 