# String: A Data type in python that's used to represent text in quotes. single or double quotes.
# Stings in python is immutable.
# Indexing: Allows you to access individual characters in a string.

# String operations
# len(string) - Returns the length of the string.
# for character in string - Iterates over each character in the string.
# if substring in string - Checks whether the substring is part of the string.
# string[i] - Accesses the character at index i of the string, starting at zero.
# string[i:j] - Accesses the substring starting at index i, ending at index j minus 1. If i is omitted,
# its value defaults to 0. If j is omitted, the value will default to len(string).

print("Python")
print("Python")
a = "python"
print(a)
a = """This is Multiline
Python String.
That can stored in a variable.
"""
print(a)
print(len("Python"))  # 6
print("Python" * 2)  # PythonPython
name = "Python"
print(name[1])  # y
print(name[0])  # P
# print(name[6])  # IndexError: string index out of range
print(name[-1])  # n
print(name[-2])  # o

# Slice: The portion of a string that can contain more than one character; also somtimes called a substring.
print(name[1:4])  # yth
print(name[:4])  # Pyth
print(name[1:])  # ython
print(name[-4:])  # thon

# Immutable: Can not change.
# name[0] = "p"  # TypeError: 'str' object does not support item assignment
name = "p" + name[1:]
print(name)  # python
name = "PYTHON"
print(name)  # PYTHON
name = "Python"
print(name)  # Python

# Escape:
txt = 'We are the so-called "Vikings" from the north.'
print(txt)

# Formatting:
# {:d} -- integer value -- '{:d}'.format(10.5) → '10'
# {:.2f} -- floating point with that many decimals -- '{:.2f}'.format(0.5) → '0.50'
# {:.2s} -- string with that many characters -- '{:.2s}'.format('Python') → 'Py'
# {:<6s} -- string aligned to the left that many spaces -- '{:<6s}'.format('Py') → 'Py    '
# {:>6s} -- string aligned to the right that many spaces -- '{:>6s}'.format('Py') → '    Py'
# {:^6s} -- string centered in that many spaces -- '{:^6s}'.format('Py') → '  Py  '
name = "Python"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))
print("Your lucky number is {number}, {name}.".format(name=name, number=number))
print("Hello {1}, your lucky number is {0}".format(number, name))
# f-string
print(f"Hello {name}, your lucky number is {number}")

price = 7.5
with_tax = price * 1.09
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

# f-string:
print(f"Hello {name}")
print(f"Base price: ${price:.2f}. With Tax: ${with_tax:.2f}")

# python built-in methods:
name = "python"
# capitalize()	Converts the first character to upper case
print(name.capitalize())  # Python
# casefold()	Converts string into lower case
print(name.casefold())  # python
# center()	Returns a centered string
print(name.center(10, "#"))  # ##python##
# count()	Returns the number of times a specified value occurs in a string
print(name.count("t"))  # 1
print(name.count("p", 1, -1))  # 0
# encode()	Returns an encoded version of the string
print(name.encode(encoding="utf-8"))  # b'python'
# endswith()	Returns true if the string ends with the specified value
print(name.endswith("on"))  # True
print(
    name.endswith("th", 1, 4)
)  # True starting index: 1, ending index: 4 i.e. till 3rd index
# expandtabs()	Sets the tab size of the string
print("p\ty\tth\ton".expandtabs(8))  # p       y       th      on
# find()	Searches the string for a specified value and returns the lowest position of where it was found
print(name.find("on"))  # 4
print(name.find("o", 2, -1))  # 4
print(name.find("x"))  # -1
# format()	Formats specified values in a string
print("Hi: {}".format(name))  # Hi: python
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
print(name.index("h"))  # 3
print(name.index("h", 2, 5))  # 3
# print(name.index("x"))  # ValueError: substring not found

# isalnum()	Returns True if all characters in the string are alphanumeric
print(name.isalnum())  # True
# isalpha()	Returns True if all characters in the string are in the alphabet
print(name.isalpha())  # True
# isdecimal()	Returns True if all characters in the string are decimals
print(name.isdecimal())  # False
# isdigit()	Returns True if all characters in the string are digits
print(name.isdigit())  # False
# isidentifier()	Returns True if the string is an identifier
print(name.isidentifier())  # True
# islower()	Returns True if all characters in the string are lower case
print(name.islower())  # True
# isnumeric()	Returns True if all characters in the string are numeric
print(name.isnumeric())  # False
# isprintable()	Returns True if all characters in the string are printable
print(name.isprintable())  # True
# isspace()	Returns True if all characters in the string are whitespaces
print(" ".isspace())  # True
# istitle()	Returns True if the string follows the rules of a title
print(name.istitle())  # False
# isupper()	Returns True if all characters in the string are upper case
print(name.isupper())  # False
# join() Joins the elements of an iterable to the end of the string
print(
    ", ".join(["python", "is", "a", "powerful", "language."])
)  # python, is, a, powerful, language.
# ljust()	Returns a left justified version of the string
print(name.ljust(10, "#"))  # python####
# lower()	Converts a string into lower case
print("PYTHON".lower())  # python
# lstrip()	Returns a left trim version of the string
print("#####python#####".lstrip("#"))  # python#####
# maketrans()	Returns a translation table to be used in translations
trans_name = name.maketrans("n", "N")
print(name.translate(trans_name))  # pythoN
# partition()	Returns a tuple where the string is parted into three parts
print(name.partition("t"))  # ('py', 't', 'hon')
# replace()	Returns a string where a specified value is replaced with a specified value
print(name.replace("p", "P"))  # Python
# rfind()	Searches the string for a specified value and returns the last position of where it was found
print("python book".rfind("o"))  # 9
# rindex()	Searches the string for a specified value and returns the last position of where it was found
print("python book".rindex("o"))  # 9
# rjust()	Returns a right justified version of the string
print(name.rjust(10, "#"))  # ####python
# rpartition()	Returns a tuple where the string is parted into three parts
print("python book".rpartition("o"))  # ('python bo', 'o', 'k')
# rsplit()	Splits the string at the specified separator, and returns a list
print("python book".rsplit("o"))  # ['pyth', 'n b', '', 'k']
# rstrip()	Returns a right trim version of the string
print("#####python#####".rstrip("#"))  # #####python
# split()	Splits the string at the specified separator, and returns a list
print("My name, is, python".split(","))  # ['My name', ' is', ' python']
# splitlines()	Splits the string at line breaks and returns a list
print(
    a.splitlines()
)  # ['This is Multiline', 'Python String.', 'That can stored in a variable.']
# startswith()	Returns true if the string starts with the specified value
print(name.startswith("p"))  # True
# strip()	Returns a trimmed version of the string
print("#####python######".strip("#"))  # python
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
print(name.swapcase())  # PYTHON
# title()	Converts the first character of each word to upper case
print(name.title())  # Python
# translate()	Returns a translated string
print(name.translate(trans_name))  # pythoN
# upper()	Converts a string into upper case
print(name.upper())  # PYTHON
# zfill()	Fills the string with a specified number of 0 values at the beginning
print(name.zfill(10))  # 0000python
