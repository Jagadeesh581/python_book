# Function: pieces of code that perform a unit of work.
# def function_name(parameters):
# #### body
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.


# Creating a Function : In Python a function is defined using the 'def' keyword.
# Calling a Function: To call a function, use the function name followed by parenthesis.
def my_function():
    print("Hello from a function")


my_function()


# Arguments:
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want,
# just separate them with a comma.

# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called


# Number of Arguments
# By default, a function must be called with the correct number of arguments.
# Meaning if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "Refsnes")


# my_function("Emil")  # TypeError: my_function() missing 1 required positional argument: 'lname'


# Arbitrary Arguments, *args:
# If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# Keyword Arguments:
# You can also send arguments with the key = value syntax.
#
# This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
    print(f"Child1: {child1} and Child2: {child2}")


my_function(child1="Emil", child2="Tobias", child3="Linus")


# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly
def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


# Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value.
def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# Passing a List as an Argument:
# You can send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function
def my_function(food):
    for i in food:
        print(i)


fruits = ["apple", "banana", "cherry"]
my_function(fruits)


# Return Values:
# To let a function return a value, use the return statement.
def my_function(n):
    return 5 * n


print(my_function(3))
my_function_result = my_function(5)
print(my_function_result)


# Recursion: The repeated application of the same procedure to a smaller problem.
# Recursion lets us tackle complex problems by reducing the problem to a simpler one.
# In programming, recursion is a way of doing a repetitive task by having a function call itself.
# must include base case followed by a recursive case
def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:  # base case
        return 1
    result = n * factorial(n - 1)  # recursive case
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result


factorial(4)

# Lambda Function:
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression

# lambda arguments : expression

# Add 10 to argument 'a', and return the result
x = lambda a: a + 10
print(x(5))
# Multiply argument a with argument b and return the result
x = lambda a, b: a * b
print(x(5, 6))
# Summarize argument a, b, and c and return the result
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
