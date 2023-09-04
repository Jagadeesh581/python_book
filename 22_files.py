# Python has several functions for creating, reading, updating, and deleting files.

# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition, you can specify if the file should be handled as binary or text mode:
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# to open a file for reading it is enough to specify the name of the file:

f = open("demo_file.txt")
print(f)

# The code above is the same as:
# f = open("demo_file.txt", "rt")
# Because "r" for read, and "t" for text are the default values, you do not need to specify them.

# Data from an opened file can be read using any of the methods: 'read', 'readline' and 'readlines'.
# Data can be written to a file using either 'write' or 'writelines' method.
# A file must be opened, before it is used for reading or writing.
fp = open("temp.txt", "r")  # opening
content = fp.read()  # reading
fp.close()  # closing

# The open() function returns a file object, which has a read() method for reading the content of the file
f = open("demo_file.txt", "r")
print(f.read())
f.close()

# If the file is located in a different location, you will have to specify the file path, like this
# f = open("D:\\myfiles\welcome.txt", "r")


# Read Only Parts of the File:
# By default the read() method returns the whole text, but you can also specify how many characters you want to return.

# Return the 5 first characters of the file:
f = open("demo_file.txt", "r")
print(f.read(5))
f.close()

# Read Lines:
# You can return one line by using the readline() method.
# Read one line of the file.
f = open("demo_file.txt", "r")
print(f.readline())
f.close()

# Read two lines of the file:
f = open("demo_file.txt", "r")
print(f.readline())
print(f.readline())
f.close()

# Read all the lines of the file and returns as list.
f = open("demo_file.txt", "r")
print(f.readlines())
f.close()

# By looping through the lines of the file, you can read the whole file, line by line:
f = open("demo_file.txt", "r")
for x in f:
    print(x)
f.close()

# Note: You should always close your files.


# Write to an Existing File:
# To write to an existing file, you must add a parameter to the open() function.
# "a" - Append - will append to the end of the file.
# "w" - Write - will overwrite any existing content.

f = open("temp.txt", "a")
f.write("Now the file has more content!")
f.close()
# open and read the file after the appending:
f = open("temp.txt", "r")
print(f.read())
f.close()

f = open("temp.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
# open and read the file after the appending:
f = open("temp.txt", "r")
print(f.read())
f.close()

# writelines
# file.writelines(list)
f = open("demofile.txt", "a")
f.writelines(["\nSee you soon!", "\nOver and out."])
f.close()

# open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())
f.close()

# Create a New File:
# To create a new file in Python, use the open() method, with one of the following parameters.

# "x" - Create - will create a file, returns an error if the file exist.
# "a" - Append - will create a file if the specified file does not exist.
# "w" - Write - will create a file if the specified file does not exist.


# Delete a File:
# To delete a file, you must import the OS module, and run its os.remove() function:
# import os
# os.remove("demo_file.txt")

# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:
import os

if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")

# Delete Folder:
# To delete an entire folder, use the os.rmdir() method:

# Remove the folder "myfolder":
# os.rmdir("myfolder")


# Note: You can only remove empty folders.


# Context Manager:
# allows a programmer to perform required activities, automatically, while entering or exiting a Context.
# opening a file, doing few file operations, and closing the file is manged using Context Manager as shown below.

with open("sample.txt", "r") as fp:
    content = fp.read()

# The keyword 'with' is used in Python to enable a context manager. It automatically takes care of closing the file.

# import sqlite3
# class DbConnect(object):
#     def __init__(self, dbname):
#         self.dbname = dbname
#     def __enter__(self):
#         self.dbConnection = sqlite3.connect(self.dbname)
#         return self.dbConnection
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.dbConnection.close()
# with DbConnect('TEST.db') as db:
#     cursor = db.cursor()
#     '''
#    Few db operations
#    ...
#     '''

# tell() gives you the current position.
# seek() changes the file position to the indicated byte in the file
