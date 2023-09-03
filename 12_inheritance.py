# Python Inheritance:
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.


# Child class is the class that inherits from another class, also called derived class.
# Create a Parent Class
# Any class can be a parent class, so the syntax is the same as creating any other class
class Parent:
    pass


# To create a child class, specify the parent class name inside the pair of parenthesis, followed by its name.
class Child(Parent):
    pass


# In Python, every class uses inheritance and is inherited from object by default.
# Hence, the below two definitions of MySubClass are same.

# Definition 1
# class MySubClass:
#    pass

# Definition 2
# class MySubClass(object):
#     pass

# object is known as parent or super class.
# MySubClass is known as child or subclass or derived class.


# parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# child class
class Student(Person):
    pass


# Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()
x = Student("Mike", "Olsen")
x.printname()


# Add the __init__() Function
# So far we have created a child class that inherits the properties and methods from its parent.
# We want to add the __init__() function to the child class (instead of the pass keyword).


# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# The child's __init__() function overrides the inheritance of the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


x = Student("Mike", "Olsen")
x.printname()


# Use the super() Function:
# Python has a super() function that will make the child class inherit all the methods and properties from its parent.
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


x = Student("Mike", "Olsen")
x.printname()


# Add Properties:
# Add a property called graduation_year to the Student class:
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year


x = Student("Mike", "Olsen", 2019)
x.printname()


# Add Methods:
# Add a method called welcome to the Student class.
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year

    def welcome(self):
        print(
            "Welcome",
            self.firstname,
            self.lastname,
            "to the class of",
            self.graduation_year,
        )


x = Student("Mike", "Olsen", 2019)
x.printname()
x.welcome()


# Polymorphism allows a subclass to override or change a specific behavior, exhibited by the parent class
# for above example modifying __ini__ method


# In Python, there are five types of inheritance:

# 1. **Single Inheritance**:
#    - Single inheritance is the simplest form of inheritance in Python.
#    - In single inheritance, a subclass inherits from only one superclass.
#    - It forms a linear hierarchy where each subclass has only one immediate superclass.
#    - Example:
#      class Parent:
#          pass

#      class Child(Parent):
#          pass

# 2. **Multiple Inheritance**:
#    - Multiple inheritance allows a class to inherit from multiple superclasses.
#    - This means a class can inherit attributes and methods from more than one parent class.
#    - Python supports multiple inheritance by allowing a subclass to inherit from multiple superclasses separated by commas.
#    - Example:
#      class Parent1:
#          pass

#      class Parent2:
#          pass

#      class Child(Parent1, Parent2):
#          pass

# 3. **Multilevel Inheritance**:
#    - In multilevel inheritance, a class inherits from another class, which in turn inherits from another class.
#    - It forms a chain of inheritance where each subclass is derived from its superclass.
#    - Example:
#      class Grandparent:
#          pass

#      class Parent(Grandparent):
#          pass

#      class Child(Parent):
#          pass

# 4. **Hierarchical Inheritance**:
#    - Hierarchical inheritance involves multiple subclasses inheriting from a single superclass.
#    - It creates a tree-like structure where one superclass has multiple subclasses.
#    - Example:
#      class Parent:
#          pass

#      class Child1(Parent):
#          pass

#      class Child2(Parent):
#          pass

# 5. **Hybrid Inheritance**:
#    - Hybrid inheritance is a combination of two or more types of inheritance.
#    - It can involve a mix of single, multiple, multilevel, and hierarchical inheritance.
#    - Hybrid inheritance allows for greater flexibility but can be complex to manage.
#    - Example:
#      class A:
#          pass

#      class B(A):
#          pass

#      class C(A):
#          pass

#      class D(B, C):
#          pass


# Abstraction and Encapsulation:

# Abstraction means working with something you know how to use without knowing how it works internally.
# Encapsulation allows binding data and associated methods together in a unit i.e. class.
# These principles together allows a programmer to define an interface for applications,
# i.e. to define all tasks the program is capable to execute and their respective input and output data.

# A good example is a television set. We don’t need to know the inner workings of a TV, in order to use it.
# All we need to know is how to use the remote control (i.e. the interface for the user to interact with the TV).


# Abstracting Data:
# Direct access to data can be restricted by making required attributes or methods private,
# just by prefixing its name with one or two underscores.

# An attribute or a method starting with:
# no underscores is a public one.
# a single underscore is private, however, still accessible from outside.
# double underscores is strongly private and not accessible from outside.
