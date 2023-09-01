# Branching: The ability of a program to alter its execution sequence.

a = 33
b = 200
# if condition:
# ####body of if block
# The body of the if block will only execute when the condition evaluates to true; otherwise it's skipped.
if b > a:
    print("b is greater than a")

# if condition:
# ####body of if block
# else:
# ####body of else block
# The body of else block will only execute when the condition of if evaluates to false.
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

# if condition:
# ####body of if block
# elif:
# ####body of elif block
# else:
# ####body of else block
# First checks the if condition, if the condition is false then checks elif condition.
if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")
else:
    print("b is greater than a")


# Nested if
x = 40

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")


# match
# Similar to if, elif, and else statements, match statements can be used to conditionally run code that matches certain values.
name = input("What's your name? ").lower()

match name:
    case "steve":
        print("Captain America")
    case "tony":
        print("Iron Man")
    case "thor":
        print("Thor")
    case "bruce":
        print("Hulk")
    case "clint":
        print("Hawkeye")
    case "natasha":
        print("Black Widow")
    case _:
        print("You are not an Avenger")
