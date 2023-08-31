# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# Numbers: int, float, complex
x = 1
y = 2.4
z = 1j
print(type(x), type(y), type(z), sep=", ")

# Casting: Implicit, Explicit.
# Implicit Conversion: The interpreter automatically converts one data type into another.
print(4 + 2.2)  # 6.2
# Explicit Conversion: Convert between one data type to another data type manually.
x = float(x)
y = int(x)
z = str(z)
print(type(x), type(y), type(z), sep=", ")

# Boolean: True, False
print(10 > 9)
print(10 == 9)
print(10 < 9)
print(bool("Hello"))
print(bool(15))
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

# True
print(True)
print(bool(123))
print(bool(-1))
print(bool("abc"))
print(bool(("apple", "cherry", "banana")))
print(bool(["apple", "cherry", "banana"]))
print(bool({"apple": 4, "cherry": 2, "banana": 1}))

# False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
