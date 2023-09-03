# Exceptions:
# An exception is an error that occurs during execution of a program.
# Python allows a programmer to handle such exceptions using try ... except clauses, thus avoiding the program to crash.
# Some of the python expressions, though written correctly in syntax, result in error during execution.
# Such scenarios have to be handled.


# Handling Exception
# Python handles exceptions using code written inside try ... except blocks.
# A try block is followed by one or more except clauses.
# The code to be handled is written inside try clause and the code to be executed when
# an exception occurs is written inside except clause.

# single exception
try:
    print(x)
except:
    print("An exception occurred")

# Many Exceptions
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# else: else executes only when there is no exception.
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

try:
    a = pow(2, 4)
    print("Value of 'a' :", a)
    b = pow(2, "hello")  # results in exception
    print("Value of 'b' :", b)
except TypeError as e:
    print("oops!!!")
    print(e)
print("Out of try ... except.")

# finally: finally will always execute.
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")


# raise:
# The raise keyword is used to raise an exception.
x = "hello"
try:
    if not type(x) is int:
        raise TypeError("Only integers are allowed")
except TypeError as e:
    print(e)


# custom
class CustomError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


try:
    a = 2
    b = "hello"
    if not (isinstance(a, int) and isinstance(b, int)):
        raise CustomError("Two inputs must be integers.")
    c = a**b
except CustomError as e:
    print(e)


# The 'try' block lets you test a block of code for errors.
# The 'except' block lets you handle the error.
# The 'else' block lets you execute code when there is no error.
# The 'finally' block lets you execute code, regardless of the result of the try- and except blocks.
