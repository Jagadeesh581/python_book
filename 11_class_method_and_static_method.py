# Class Methods:
# A method defined inside a class is bound to its object, by default.
# However, if the method is bound to a Class, then it is known as classmethod.

# Consider the following two examples:
# Example 1 defines the method getCirclesCount, bound to an object of Circle class.
# Example 2 defines the classmethod getCirclesCount, bound to class Circle.


# Example 1
class Circle:
    # class variable, shared across all the objects
    no_of_circles = 0

    def __init__(self, radius):
        self.__radius = radius
        Circle.no_of_circles += 1

    def get_circles_count(self):
        return Circle.no_of_circles


c1 = Circle(3.5)
c2 = Circle(5.2)
c3 = Circle(4.8)
print(c1.get_circles_count())  # -> 3
print(c2.get_circles_count())  # -> 3
print(Circle.get_circles_count(c3))  # -> 3


# print(Circle.getCirclesCount())  # -> TypeError

# In Example 1, getCirclesCount method is bound to objects of Circle.
# Hence, when calling it,
# on objects c1, and c2 resulted in 3.
# on class Circle with object c3 as argument resulted in 3 again.
# on class Circle without any object information resulted in TypeError.


# Example 2
class Circle:
    no_of_circles = 0

    def __init__(self, radius):
        self.__radius = radius
        Circle.no_of_circles += 1

    @classmethod
    def get_circles_count(cls):
        return Circle.no_of_circles


c1 = Circle(3.5)
c2 = Circle(5.2)
c3 = Circle(4.8)
print(c1.get_circles_count())  # -> 3
print(c2.get_circles_count())  # -> 3
print(Circle.get_circles_count())  # -> 3


# In Example 2, getCirclesCount is decorated with classmethod.
# Thus making it a class method, which bounds to class Circle.
# In Example 2, class Circle is passed as argument to getCirclesCount in both cases.
# i.e. when it is called on objects and the class.


# Static Method:
# A method defined inside a class and not bound to either a class or an object is known as Static Method.
# Decorating a method using @staticmethod decorator makes it a static method.
# Consider the following two examples:
# Example1 defines the method square, outside the class definition of Circle, and uses it inside the class Circle.
# Example2 defines the static method square, inside the class Circle, and uses it.


# Example 1
def square_of(x):
    return x**2


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.14 * square_of(self.__radius)


c1 = Circle(3.9)
print(c1.area())
print(square_of(10))


# In Example 1, square function is defined outside the class Circle.
# It determines square of a number, x.
# It can be used outside and also inside the class Circle.
# Though existing square function serves the purpose,
# it is not packaged properly and does not appear as integral part of class Circle.


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.14 * self.square(self.__radius)

    @staticmethod
    def square(x):
        return x**2


c1 = Circle(3.9)
print(c1.area())
# print(square(10))  # -> NameError
# In Example 2, the square method is defined inside the class Circle and decorated with staticmethod.
# Then it is accessed as self.square.
# You can also observe that square method is no longer accessible from outside the class Circle.
# However, it is possible to access the static method using Class or the Object as shown below.
print(Circle.square(10))  # -> 100
print(c1.square(10))  # -> 100
