# class
# re-useable blueprint with attributes and functions
class Person:
    # class_test variable shared by instances
    count = 0

    # special method called constructor/initialization method
    # to create an object from class_test blueprint
    def __init__(self, name):
        self._name = name  # private instance variable is preceded with a underscore _ to indicate private
        Person.count += 1


    # class_test method which can be called by class_test only
    # first argument must be cls
    # differs from static method in the way that it can be easily be use by child class_test
    # commonly used as inheritable alternative constructor
    @classmethod
    def by_last_name(cls, name):
        return cls(name)

    # override sequence protocol
    # callable by len()
    def __len__(self):
        return Person.count

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

    # indicate to be override by child class_test
    def speak(self):
        pass

# class_test
# inheritance
# wrap parent class_test with parenthesis after class_test name
class Employee(Person):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id

    # override parent class_test instance method
    def info(self):
        super().info()
        print("id: " + str(self.id))



print(len(Person("Darryl")))
print(len(Person("Darryl")))
print(len(Person("Darryl")))