# Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.
# Python is a high-level, interpreted, interactive and object-oriented scripting language.
# Web scripting
# 3d Modelling (Blender)
# Desktop Applications -`Games (Pygame)
# Scientific usage (SciPy/NumPy)
# Python source code is available under the GNU General Public License (GPL).
# There are two major Python versions, Python 2 and Python 3.

# Programming: A computer program is a set of instructions that tells your computer what to do.
# When you write a program you create a step-by-step instructions of what needs to be done to complete a task and
# when your computer executes the program it reads what you wrote and follows your instructions to the letter.
# Syntax: The rules for how each instruction is written.
# Semantics: The effect the instructions have.
# Script: A program that is short, simple, and can be written very quickly.

# Output to screen.
print("Hello World!")
# Taking Input from user
name = input("Enter your name: ")
x, y = input("Enter two values: ").split(",")  # taking two inputs separated by ','.
a = list(
    map(int, input("Enter multiple inputs separated by space: ").split())
)  # taking multiple inputs.
print(name)
print(x, y)
print(a)

# This is single line comment
"""
this 
is a
multiline comment.
"""

# Variables: Variables are containers for storing data values.

name = "Python"  # 'name' is the variable name
print(name)

# A variable can have a short name (like x and y) or a more descriptive name (age, car_name, total_volume).
# Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alphanumeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

x, y, z = "Orange", "Banana", "Cherry"  # Many Values to Multiple Variables
a = b = c = "Orange"  # One Value to Multiple Variables
fruits = ["apple", "banana", "cherry"]
l, m, n = fruits  # Unpack a Collection

# Global Variables
#  that are created outside a function are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.
# To create a global variable inside a function, you can use the global keyword.
