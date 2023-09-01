# Dictionary: List of key value pairs.
# dict.get(key, default) - Returns the element corresponding to key, or default if it's not present
# dict.keys() - Returns a sequence containing the keys in the dictionary
# dict.values() - Returns a sequence containing the values in the dictionary
# dict.update(other_dictionary) - Updates the dictionary with the items coming from the other dictionary.
# Existing entries will be replaced; new entries will be added.
# dict.clear() - Removes all the items of the dictionary

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# Dictionaries are created with curly brackets {}, and have keys and values or dict() constructor.
this_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(this_dict)
print(type(this_dict))
print(len(this_dict))
this_dict = dict(name="John", age=36, country="Norway")
print(this_dict)
print(type(this_dict))

# Copy
mydict = this_dict.copy()
print(mydict)
mydict = dict(this_dict)
print(mydict)

# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key
# Duplicate values will overwrite existing values
this_dict = {"brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020}
print(this_dict)

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets
x = this_dict["model"]
print(x)
# There is also a method called get() that will give you the same result
x = this_dict.get("model")
print(x)

# Get Keys
# The keys() method will return a list of all the keys in the dictionary
x = this_dict.keys()
print(x)

# Get Values
# The values() method will return a list of all the values in the dictionary.
x = this_dict.values()
print(x)

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
x = this_dict.items()
print(x)

# check key in dictionary.
print("model" in this_dict)  # True

# Modify
# You can change the value of a specific item by referring to its key name
this_dict["year"] = 2022
print(this_dict)
# Adding an item to the dictionary is done by using a new index key and assigning a value to it
this_dict["color"] = "red"
print(this_dict)

# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs
this_dict.update({"year": 2020})
print(this_dict)

# Removing Items
# The pop() method removes the item with the specified key name
this_dict.pop("model")
print(this_dict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
this_dict.popitem()
print(this_dict)

# The del keyword removes the item with the specified key name
# del this_dict["model"]  # KeyError: 'model'
del this_dict["brand"]
print(this_dict)

# The clear() method empties the dictionary
this_dict.clear()
print(this_dict)

# The del keyword can also delete the dictionary completely
del this_dict
# print(this_dict)  # NameError: name 'this_dict' is not defined


# Loop:

this_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# Print all key names in the dictionary, one by one
for x in this_dict:
    print(x, end=", ")
print()

# Print all values in the dictionary, one by one
for x in this_dict:
    print(this_dict[x], end=", ")
print()

# You can also use the values() method to return values of a dictionary
for x in this_dict.values():
    print(x, end=", ")
print()

# You can use the keys() method to return the keys of a dictionary
for x in this_dict.keys():
    print(x, end=", ")
print()

# Loop through both keys and values, by using the items() method.
for x, y in this_dict.items():
    print(x, y, end=", ")
print()

# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries
my_family = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011},
}
print(my_family)

# add three dictionaries into a new dictionary
child1 = {"name": "Emil", "year": 2004}
child2 = {"name": "Tobias", "year": 2007}
child3 = {"name": "Linus", "year": 2011}

my_family = {"child1": child1, "child2": child2, "child3": child3}
print(my_family)


# set defaults
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.setdefault("model", "Bronco")
print(x)
x = car.setdefault("color", "Black")
print(x)


# fromkeys()
# The fromkeys() method returns a dictionary with the specified keys and the specified value
# dict.fromkeys(keys, value)
# keys	Required. An iterable specifying the keys of the new dictionary
# value	Optional. The value for all keys. Default value is None
x = ("key1", "key2", "key3")
y = 0
this_dict = dict.fromkeys(x, y)
print(this_dict)
this_dict = dict.fromkeys(x)
print(this_dict)
