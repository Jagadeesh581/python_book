# Loops: for, while.
# Use 'for' loops when there's a sequence of elements that you want to iterate.
# Use 'while' loops when you want to repeat an action unit a condition changes.
# Infinite loop: A loop that keeps executing and never stops.

# while loops: Instructs your computer to continuously execute your code based on the value of a condition.

# Initializing: To give an initial value to a variable.

# initialize a variable
# while condition:
# ####body of while
# ####increase or decrease variable value (anything to make the while condition false)
i = 1
while i < 6:
    print(i)
    i += 1

# while True:
#     # Do something
#     # if some condition:
#         break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# break: break the loop.
# continue: skips the current iteration.
# pass: do nothing

# else: else statement runs a block of code when the condition no longer true.
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# for loop: Iterates over a sequence of values (that is either a list, a tuple, a dictionary, a set, or a string).
# for variable in sequence:
#     body

# list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# string
for x in "banana":
    print(x)

# break: With the break statement we can stop the loop before it has looped through all the items.
for x in fruits:
    print(x)
    if x == "banana":
        break

# continue : With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# range
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
# and ends at a specified number.
for x in range(6):
    print(x)

# range(2, 6), which means values from 2 to 6 (but not including 6)
for x in range(2, 6):
    print(x)

# Increment the sequence with 3 (default is 1)
for x in range(2, 30, 3):
    print(x)

# else:
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished
# Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")


# Nested Loop:
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop"
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
