# Tuple: Sequence of elements of any type, and are immutable.
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Tuples are written with round brackets or tuple() constructor
this_tuple = ("apple", "banana", "cherry")
print(this_tuple)
print(type(this_tuple))
this_list = ["apple", "banana", "cherry", "apple", "cherry"]
this_tuple = tuple(this_list)
print(this_tuple)
print(type(this_tuple))
print(len(this_tuple))

# Create Tuple With One Item
single_tuple = ("apple",)
# single_tuple = ("apple")  # type <str>
print(type(single_tuple))


# Access
print(this_tuple[1])
print(this_tuple[-1])
print(this_tuple[2:5])
print(this_tuple[:4])
print(this_tuple[2:])
print(this_tuple[-4:-1])

# Exists
print("apple" in this_tuple)


# Update
# Tuples are immutable, inorder to modify we need to convert tuple to a list modify the items and convert back to tuple.


x = ("apple", "banana", "cherry")
# Change item: We can not change items directly, first we need convert tuple into list then change items and convert back.
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
# Add: convert to list then add and convert back.
y = list(x)
y.append("orange")
x = tuple(y)
print(x)
# Remove: convert to list then remove and convert back.
y = list(x)
y.remove("apple")
x = tuple(y)
print(x)
# del will completely delete the tuple
del x
# print(x)  # name 'x' is not defined


# join
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# multiply
fruits = ("apple", "banana", "cherry")
my_tuple = fruits * 2
print(my_tuple)

# Unpack
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Using asterisk
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)


# Loop:
this_tuple = ("apple", "banana", "cherry")
for x in this_tuple:
    print(x)

# with range
for i in range(len(this_tuple)):
    print(this_tuple[i])

# while loop
i = 0
while i < len(this_tuple):
    print(this_tuple[i])
    i = i + 1

# Methods:
# count()
# index()


# tuple Comprehension
# new_tuple = (expression for item in iterable)
# new_tuple = (expression for item in iterable if condition == True)
# new_tuple = (if_expression if condition == True else else_expression for item in iterable)
