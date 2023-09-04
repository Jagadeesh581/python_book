# Iterator:
# An Iterator is an object, which allows a programmer to traverse through all the elements of a collection,
# regardless of its specific implementation.
# Values of an Iterator can be accessed only once and in sequential order.
x = [6, 3, 1]
s = iter(x)
print(next(s))  # -> 6
print(next(s))  # -> 3
print(next(s))  # -> 1
# print(next(s))  # -> StopIteration Error

# Generator:
# A Generator object is an iterator, whose values are created at the time of accessing them.
# A generator can be obtained either from a generator expression or a generator function.
x = [6, 3, 1]
g = (i**2 for i in x)  # generator expression
print(next(g))  # -> 36
print(next(g))  # -> 9
print(next(g))  # -> 1


# print(next(g))  # StopIteration


def gen_number():  # generator function
    my_list = [6, 3, 1]
    for i in my_list:
        yield i**2


x = gen_number()
print(next(x))  # -> 36
print(next(x))  # -> 9
print(next(x))  # -> 1


# print(next(x))  # StopIteration


# Create an Iterator:
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

# The __iter__() method do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.


# Create an iterator that returns numbers, starts with 1, and each sequence increase by one (returning 1,2,3, etc.).


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        n = self.a
        self.a += 1
        return n


my_class = MyNumbers()
my_iter = iter(my_class)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


# StopIteration:
# The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
# To prevent the iteration to go on forever, we can use the StopIteration statement.

# In __next__() method add a terminating condition to raise an error if iteration is done a specified number of times.


# prime numbers below 20.
class MyNumbers:
    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self

    def is_prime(self, num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        # 6k +/- 1 rule
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def __next__(self):
        while True:
            if self.current > 20:
                raise StopIteration
            if self.is_prime(self.current):
                prime = self.current
                self.current += 1
                return prime
            self.current += 1


my_class = MyNumbers()
my_iter = iter(my_class)

for x in my_iter:
    print(x)
