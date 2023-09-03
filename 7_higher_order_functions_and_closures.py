# A Higher Order function is a function, which is capable of doing any one of the following things:
# It can be functioned as a data and be assigned to a variable.
# It can accept any other function as an argument.
# It can return a function as its result.

# The ability to build Higher order functions, allows a programmer to create Closures,
# which in turn are used to create Decorators.


# Function as a Data:
def greet():
    return "Hello Everyone!"


print(greet())
wish = greet  # 'greet' function assigned to variable 'wish'
print(type(wish))
print(wish())


# Function as an Argument:
def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def prod(x, y):
    return x * y


def do(func_name, x, y):
    return func_name(x, y)


print(do(add, 12, 4))  # 'add' as arg
print(do(sub, 12, 4))  # 'sub' as arg
print(do(prod, 12, 4))  # 'prod' as arg


# Returning a Function:
def outer():
    def inner():
        s = "Hello world!"

        return s

    return inner()


print(outer())  # 'Hello world!
# You can observe from the output that the return value of 'outer' function is the return value of 'inner' function.


def outer():
    def inner():
        s = "Hello world!"

        return s

    return inner  # Removed '()' to return 'inner' function itself


print(outer())  # returns 'inner' function
func = outer()
print(type(func))
print(func())  # calling 'inner' function
# Parenthesis after the inner function are removed so that the outer function returns inner function.


# Closures:
# In simplest terms, a Closure is a function returned by a higher order function,
# whose return value depends on the data associated with the higher order function.
def multiple_of(x):
    def multiple(y):
        return x * y

    return multiple


c1 = multiple_of(5)  # 'c1' is a closure
c2 = multiple_of(6)  # 'c2' is a closure
print(c1(4))
print(c2(4))


# You can observe from the example that the closure functions c1 and c2 hold the data passed to enclosing function,
# multiple_of, during their creation.
# the first closure function, c1 binds the value 5 to argument x and when called with an argument 4,
# it executes the body of multiple function and returns the product of 5 and 4.
# Similarly, c2 binds the value 6 to argument x and when called with argument 4 returns 24.
