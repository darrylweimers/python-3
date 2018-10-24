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




async 

Async 
Tasks, Futures, Couroutines 
Small snippets 


Async feature:
-execute method partially 
-halting execution 
Maintain object stack and exception 



Asyncio 
Python 3.5  

Single Thread 
No race condition 
Async code must run inside event loop 

Keywords: 
async: use a async keyword to declare a function as a coroutine function  
	   coroutine object is created when coroutine function is callled  

	   		coroutine: 
	   		it can be suspended during execution to wait for external processing (some routine in I/O) and return from the point it had stopped when the external processing is done.



await: use async keyword to block event loop until coroutine object is completed 

Execute a coroutine object using either: 
-await 
-schedule with 
				asyncio.ensure_future(coroutine_object)  				   Note: accepts any awaitable 
                or 
                asyncio.get_event_loop.create_task(coroutine object)       Note: accepts coroutine only 


Futures: 
The asyncio module defines its own object Future. Futures represent a processing that has still not been accomplished.

Tasks: This is a subclass of asyncio.Future to encapsulate and manage coroutines.
-is a way to arrange for a coroutine to be executed by an event loop, while also providing the caller a way to find out what the result was.
-a task is automatically scheduled for execution when it is created.
-supervise coroutine run state     

Running event loop:
We have a number of options for running our event loops:
-asyncio.get_event_loop.run_forever() which will subsequently run our event loop until the stop() function is called, 
-run_until_complete(future) and only run our event loop until whatever future object we’ve passed in has completed it’s execution.

Future 

A future is an object that represents something uncompleted. 

Arrange for something to be called when the future becomes done: You can add lots of callbacks. They’ll all be called (one at a time).

When the future is done, mark it done and set its result: The callbacks can call future.result() to find out what the result was if they care.
Tasks



