# Python is an object-oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# Object-oriented programming can model real-life scenarios and suits developing large and complex applications.
# In real life, an object is something that you can sense and feel. For example Toys, Bicycles, Oranges and more.
# An object is a non-tangible entity, which holds some data and is capable of doing certain things.


# Defining Classes:

# Class: A Class is a template which contains:
# instructions to build an object.
# methods that can be used by the object to exhibit a specific behaviour.


# class keyword is used to define a class in Python.
# Syntax:
# class <ClassName>(<parent1>, ... ):
#     class_body
# Example:
class Person:
    pass


# Above example defines Person class without body.


# Creating Objects:
# An object is created by calling the class name followed by a pair of parenthesis.
p1 = Person()  # Creating the object 'p1'.
print(p1)  # -> '<__main__.Person object at 0x0A...>'
# The output of print on object p1, tell you what class it belongs to and hints on memory address it is referenced to.


# Setting Attributes:
# You can set attributes, one a time, to an instantiated object and access it using the dot notation.
# The value which is set to an attribute can be anything: a Python primitive, a built-in data type, another object.
# It can even be a function or a class.

# Example
p1 = Person()
p1.fname = "Jack"
p1.lname = "Simmons"
print(p1.fname, "-", p1.lname)  # -> 'Jack - Simmons'


# You can also set multiple attributes, at once, by defining the initializer method, '__init__', inside the class.
# This method is called by default, during an object creation.
# It takes values passed inside the parenthesis, during an object creation, as its arguments.
# It also takes 'self' as the first argument, which refers to the current object.
# 'self' parameter is a reference to the current instance of the class,
# and is used to access variables that belong to the class.
# It doesn't have to be named 'self', call it whatever, but it has to be first parameter of any function in the class.
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


p1 = Person("George", "Smith")
print(p1.fname, "-", p1.lname)


# Documenting a Class:
# Each class or a method definition can have an optional first line, known as docstring.


# Example
class Person:
    """Represents a person."""

    def __init__(self, fname, lname):
        """Initialises two attributes of a person."""
        self.fname = fname
        self.lname = lname


print(help(Person))


# The __str__() Function:
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age}."


p1 = Person("John", 36)

print(p1)


# Object Methods:
# Objects can also contain methods. Methods in objects are functions that belong to the object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()

# Modify Object Properties
print(p1.age)
p1.age = 40
print(p1.age)
# Delete Object Properties
del p1.age
# print(p1.age)  # AttributeError: 'Person' object has no attribute 'age'
# Delete Objects
del p1
# print(p1.name)  # NameError: name 'p1' is not defined


# Decorators:
# Properties can be utilized to harden our code.
# In Python, we define properties using function “decorators”, which begin with '@'.
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
