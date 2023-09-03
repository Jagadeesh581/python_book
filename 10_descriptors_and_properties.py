# Python descriptors allow a programmer to create managed attributes.
# In other object-oriented languages, you will find getter and setter methods to manage attributes.
# Python allows a programmer to manage the attributes simply with the attribute name, without losing their protection.
# This is achieved by defining a descriptor class, that implements any of __get__, __set__, __delete__ methods.


class EmpNameDescriptor:
    """EmpNameDescriptor is defined to manage emp_name attribute."""

    def __get__(self, instance, owner):
        return self.__emp_name

    def __set__(self, instance, value):
        # It checks if the value of emp_name attribute is a string or not.
        if not isinstance(value, str):
            raise TypeError("emp_name must be a string.")
        self.__emp_name = value

    def __delete__(self, instance):
        if hasattr(instance, "emp_name"):
            del self.__emp_name


class EmpIdDescriptor:
    """EmpIdDescriptor is defined to manage emp_id attribute."""

    def __get__(self, instance, owner):
        return self.__emp_id

    def __set__(self, instance, value):
        if hasattr(instance, "emp_id"):
            raise ValueError("emp_id is a read-only attribute.")
        if not isinstance(value, int):
            raise TypeError("emp_id must be an integer.")
        self.__emp_id = value


class Employee:
    """Employee class is defined such that, it creates emp_id and emp_name attributes from descriptors EmpIdDescriptor
    and EmpNameDescriptor."""

    emp_name = EmpNameDescriptor()
    emp_id = EmpIdDescriptor()

    def __init__(self, empname, empid):
        self.emp_name = empname
        self.emp_id = empid


e1 = Employee("Jagadeesh", 123456)
print(e1.emp_id, "-", e1.emp_name)
e1.emp_name = "Jesse"
print(e1.emp_id, "-", e1.emp_name)
# e1.emp_id = 654321  # ValueError: emp_id is a read-only attribute.
del e1.emp_name


# AttributeError: 'EmpNameDescriptor' object has no attribute '_EmpNameDescriptor__emp_name'
# print(e1.emp_id, "-", e1.emp_name)


# Properties:
# Descriptors can also be created using property() type.
# It is easy to create a descriptor for any attribute using property().

# property(fget=None, fset=None, fdel=None, doc=None)
# fget : attribute get method
# fset : attribute set method
# fdel – attribute delete method
# doc – docstring


class Employee:
    def __init__(self, empname, empid):
        self.emp_name = empname
        self.emp_id = empid

    def get_emp_name(self):
        return self.__emp_name

    def set_emp_name(self, value):
        if not isinstance(value, str):
            raise TypeError("emp_name must be a string.")
        self.__emp_name = value

    def del_emp_name(self):
        del self.__emp_name

    def get_emp_id(self):
        return self.__emp_id

    def set_emp_id(self, value):
        if not isinstance(value, int):
            raise TypeError("emp_name must be an integer.")
        self.__emp_id = value

    emp_name = property(get_emp_name, set_emp_name, del_emp_name)
    emp_id = property(get_emp_id, set_emp_id)


e1 = Employee("Jagadeesh", 123456)
print(e1.emp_id, "-", e1.emp_name)
e1.emp_name = "Jesse"
print(e1.emp_id, "-", e1.emp_name)
e1.emp_id = 654321
print(e1.emp_id, "-", e1.emp_name)
del e1.emp_name


# AttributeError: 'EmpNameDescriptor' object has no attribute '_EmpNameDescriptor__emp_name'
# print(e1.emp_id, "-", e1.emp_name)


# Property Decorators:
# Descriptors can also be created with property decorators.
# using property decorators, an attribute's get method will be same as its name and will be decorated with property.
# In a case of defining any set or delete methods, they will be decorated with respective setter and deleter methods.
# Recommended Way.
class Employee:
    def __init__(self, empname, empid):
        self.emp_name = empname
        self.emp_id = empid

    @property
    def emp_name(self):
        return self.__emp_name

    @emp_name.setter
    def emp_name(self, value):
        if not isinstance(value, str):
            raise TypeError("emp_name must be a string.")
        self.__emp_name = value

    @emp_name.deleter
    def emp_name(self):
        del self.__emp_name

    @property
    def emp_id(self):
        return self.__emp_id

    @emp_id.setter
    def emp_id(self, value):
        if not isinstance(value, int):
            raise TypeError("emp_name must be an integer.")
        self.__emp_id = value


e1 = Employee("Jagadeesh", 123456)
print(e1.emp_id, "-", e1.emp_name)
e1.emp_name = "Jesse"
print(e1.emp_id, "-", e1.emp_name)
e1.emp_id = 654321
print(e1.emp_id, "-", e1.emp_name)
del e1.emp_name

# AttributeError: 'EmpNameDescriptor' object has no attribute '_EmpNameDescriptor__emp_name'
# print(e1.emp_id, "-", e1.emp_name)
