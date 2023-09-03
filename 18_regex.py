# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.
# Python has a built-in package called re, which can be used to work with Regular Expressions.


# Search the string to see if it starts with "The" and ends with "Spain".
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("Match")
else:
    print("Not a Match")

# RegEx Functions:
# The re module offers a set of functions that allows us to search a string for a match.

# Function	Description
# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	    Returns a list where the string has been split at each match
# sub	    Replaces one or many matches with a string


# Metacharacters:
# Metacharacters are characters with a special meaning:
txt_2 = "That will be 59 dollars"
txt_3 = "hello world"
txt_4 = "The rain in Spain falls mainly in the plain!"

# []   -- A set of characters
# Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", txt)
print(x)

# \  --  Signals a special sequence (can also be used to escape special characters).
# Find all digit characters:
x = re.findall("\d", txt_2)
print(x)

# .  --  Any character (except newline character).
# Search for a sequence that starts with "he", followed by two (any) characters, and an "o".
x = re.findall("he..o", txt_3)
print(x)

# ^ -- Starts with.
x = re.search("^hello", txt_3)
if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")

# $ -- Ends with.
# Check if the string ends with 'world':
x = re.search("world$", txt_3)
if x:
    print("Yes, the string ends with 'planet'")
else:
    print("No match")

# *	Zero or more occurrences
# Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
x = re.findall("he.*o", txt_3)
print(x)

# +	One or more occurrences
# Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o".
x = re.findall("he.+o", txt_3)
print(x)

# ?	Zero or one occurrence	"he.?o"
# Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
x = re.findall("he.?o", txt_3)
print(x)

# {}	Exactly the specified number of occurrences	"he.{2}o"
# Search for a sequence that starts with "he", followed exactly 2 (any) characters, and an "o":
x = re.findall("he.{2}o", txt_3)
print(x)

# |	Either or	"falls|stays"
# Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt_4)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
# ()	Capture and group


# Special Sequences:
# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain" r"ain\b"
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain" r"ain\B"
# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"
# \D	Returns a match where the string DOES NOT contain digits	"\D"
# \s	Returns a match where the string contains a white space character	"\s"
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"
# \w	Returns a match where the string contains any word characters
# (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"


# Sets:
# A set is a set of characters inside a pair of square brackets [] with a special meaning.

# [arn]	Returns a match where one of the specified characters (a, r, or n) is present
# [a-n]	Returns a match for any lower case character, alphabetically between a and n
# [^arn]	Returns a match for any character EXCEPT a, r, and n
# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
# [0-9]	Returns a match for any digit between 0 and 9
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
# [+]	In sets, +, *, ., |, (), $,{} has no special meaning,
# so [+] means: return a match for any + character in the string


# The findall() Function:
# The findall() function returns a list containing all matches.
x = re.findall("ai", txt)
print(x)
# The list contains the matches in the order they are found.

# If no matches are found, an empty list is returned.
x = re.findall("Portugal", txt)
print(x)

# The search() Function:
# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned:
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

# If no matches are found, the value None is returned:
x = re.search("Portugal", txt)
print(x)

# The split() Function:
# The split() function returns a list where the string has been split at each match.
x = re.split("\s", txt)
print(x)

# You can control the number of occurrences by specifying the max-split parameter.
# Split the string only at the first occurrence:
x = re.split("\s", txt, 1)
print(x)

# The sub() Function:
# The sub() function replaces the matches with the text of your choice.
x = re.sub("\s", "9", txt)
print(x)

# You can control the number of replacements by specifying the count parameter:
# Replace the first 2 occurrences:
x = re.sub("\s", "9", txt, 2)
print(x)

# Match Object:
# A Match Object is an object containing information about the search and the result.
# Note: If there is no match, the value None will be returned, instead of the Match Object.

x = re.search("ai", txt)
print(x)  # this will print an object
# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

# Print the position (start- and end-position) of the first match occurrence.
# The regular expression looks for any words that starts with an upper case "S":
x = re.search(r"\bS\w+", txt)
print(x.span())

# Print the string passed into the function:
print(x.string)

# Print the part of the string where there was a match.
print(x.group())
