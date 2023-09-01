# Lists: Sequence of elements of any type, and are mutable.
# List: Lists are used to store multiple items in a single variable.
# List items are ordered, changeable, and allow duplicate values.

# create list with square brackets or list() method
x = ["Now", "we", "are", "cooking!"]
this_list = list(("apple", "banana", "cherry"))
print(type(this_list))
print(type(x))
print(this_list)
print(x)

print(len(x))
print("are" in x)
print("Today" in x)

# access items
print(x[0])
print(x[3])
# print(x[4])  # IndexError

# slice
print(x[1:3])
print(x[:2])
print(x[2:])

# Modifying the contents of a list.
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
print(fruits)

# insert at end of a list
fruits.append("Kiwi")
print(fruits)

# insert at a specified index position
fruits.insert(0, "Orange")
print(fruits)
fruits.insert(25, "Peach")
print(fruits)

# remove item with item name
fruits.remove("Melon")
print(fruits)
# fruits.remove("Pear")  # ValueError

# remove item with index
fruits.pop(3)
print(fruits)
# remove last item
fruits.pop()
print(fruits)

# empties the list
this_list.clear()
print(this_list)

# removes item with specified index
this_list = ["apple", "banana", "cherry"]
del this_list[0]
print(this_list)
# deletes entire list
del this_list
# print(this_list)  # NameError: name 'this_list' is not defined

# modify
fruits[2] = "Strawberry"
print(fruits)
fruits[1:3] = ["watermelon"]
print(fruits)

# copy
# You cannot copy a list simply by typing list2 = list1,
# because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
# copy a list with copy() method or list() method
this_list = ["apple", "banana", "cherry"]
mylist = this_list.copy()
print(mylist)
mylist = list(this_list)
print(mylist)


# join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
# with extend
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
list1.extend(list2)
print(list1)
# with '+'
list3 = list1 + list2
print(list3)
# with append
for x in list2:
    list1.append(x)

print(list1)


# Loop List:
this_list = ["apple", "banana", "cherry"]
for x in this_list:
    print(x)
for i in range(len(this_list)):
    print(this_list[i])

i = 0
while i < len(this_list):
    print(this_list[i])
    i = i + 1

# List Comprehension
# newlist = [expression for item in iterable]
# newlist = [expression for item in iterable if condition == True]
# newlist = [if_expression if condition == True else else_expression for item in iterable]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# Above can be written as
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# with if condition
newlist = [x for x in fruits if "a" in x]
print(newlist)
# Without if condition
newlist = [x for x in fruits]
print(newlist)
# with if else condition
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)
newlist = ["hello" for x in fruits]
print(newlist)

# With range
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)

# sort
fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

this_list = [100, 50, 65, 82, 23]
print(this_list)
this_list.sort()
print(this_list)
this_list.sort(reverse=True)
print(this_list)

# case insensitive
fruits = ["banana", "Orange", "Kiwi", "cherry"]
fruits.sort(key=str.lower)
print(fruits)

# reverse: reverse the order of a list, regardless of the alphabet
fruits = ["banana", "Orange", "Kiwi", "cherry"]
fruits.reverse()
print(fruits)


# customized sort
def myfunc(n):
    return abs(n - 50)


this_list = [100, 50, 65, 82, 23]
this_list.sort(key=myfunc)
print(this_list)

# count
# The count() method returns the number of elements with the specified value.
# list.count(value)
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
print(points.count(9))

# index
# The index() method returns the position at the first occurrence of the specified value.
# list.index(elmnt)
print(points.index(9))
