# classs
# re-useable blueprint with attributes and functions
class Person:
    # classs variable shared by instances
    count = 0

    # special method called constructor/initialization method
    # to create an object from classs blueprint
    def __init__(self, name):
        self._name = name  # private instance variable is preceded with a underscore _ to indicate private
        Person.count += 1


    # classs method which can be called by classs only
    # first argument must be cls
    # differs from static method in the way that it can be easily be use by child classs
    # commonly used as inheritable alternative constructor
    @classmethod
    def by_last_name(cls, name):
        return cls(name)

    @staticmethod
    def count_people():
        print("Number of person object: " + str(Person.count))

    # instance method, which can only be called by an object of Person
    # first argument must be self to indicate that function is an instance method
    def info(self):
        print("name: " + self.name)     # Notation self.[instance-variable] to access instance variable

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    # indicate to be override by child classs
    def speak(self):
        pass

# classs
# inheritance
# wrap parent classs with parenthesis after classs name
class Employee(Person):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id

    # override parent classs instance method
    def info(self):
        super().info()
        print("id: " + str(self.id))


# Force user to create only a single object of this class
class Singleton:
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self


s = Singleton() # Ok
Singleton() # will raise exception
print(s)

s = Singleton.get_instance()
print(s)


# if __name__=='__main__':



# using setter
class Result(object):

    @property
    def state(self):
        return self._state

    # constructors
    def __init__(self, state: int):
        super().__init__()
        self._set_state(state)

    # Setters
    def _set_state(self, state):
        self._state = state
        print(state)

r = Result(3)
print(r.state)
print()
