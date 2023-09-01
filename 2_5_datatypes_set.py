# A set is a collection which is unordered, unchangeable*, and un-indexed.
# Set items are unchangeable, but you can remove items and add new items.
# Sets are used to store multiple items in a single variable.

# Sets are created with curly brackets {} or set() constructor.
this_set = {"apple", "banana", "cherry"}
print(this_set)
print(type(this_set))
this_list = ["apple", "banana", "cherry"]
new_set = set(this_list)
print(new_set)
print(type(new_set))


# Duplicates Not Allowed
# Sets cannot have two items with the same value.
# Duplicate values will be ignored
this_set = {"apple", "banana", "cherry", "apple"}
print(this_set)


# Access Items
# You cannot access items in a set by referring to an index or a key.
this_set = {"apple", "banana", "cherry"}
for x in this_set:
    print(x)

print("banana" in this_set)


# Add items
# To add one item to a set use the add() method
this_set.add("orange")
print(this_set)

# To add items from another set into the current set, use the update() method.
tropical = {"pineapple", "mango", "papaya"}
this_set.update(tropical)
print(this_set)

# The object in the update() method does not have to be a set,
# it can be any iterable object (tuples, lists, dictionaries etc.).
mylist = ["kiwi", "orange"]
this_set.update(mylist)
print(this_set)

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method
this_set.remove("banana")
# If the item to remove does not exist, remove() will raise an error.
print(this_set)
this_set.discard("banana")
# If the item to remove does not exist, discard() will NOT raise an error.
print(this_set)
this_set.discard("mango")
print(this_set)

# Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# The clear() method empties the set
this_set.clear()
print(this_set)

# del keyword will delete the set completely
del this_set
# print(this_set)  # NameError: name 'this_set' is not defined


# Loop:
this_set = {"apple", "banana", "cherry"}
for x in this_set:
    print(x)


# join
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

# union
set3 = set1.union(set2)
print(set3)

# update
set1.update(set2)
print(set1)


# Keep ONLY the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# return a new set, that only contains the items that are present in both sets
z = x.intersection(y)
print(z)
# keep only the items that are present in both sets
x.intersection_update(y)
print(x)

# Keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# return a new set, that contains only the elements that are NOT present in both sets
z = x.symmetric_difference(y)
print(z)
# keep only the elements that are NOT present in both sets
x.symmetric_difference_update(y)
print(x)


# Return a set that contains the items that only exist in set x, and not in set y
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
x.difference_update(y)
print(x)


# Return True if no items in set x is present in set y
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

# Return True if all items in set x are present in set y
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

# Return True if all items set y are present in set x
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)


# set Comprehension
# new_set = {expression for item in iterable}
# new_set = {expression for item in iterable if condition == True}
# new_set = {if_expression if condition == True else else_expression for item in iterable}
