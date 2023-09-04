# Command-Line Arguments
# argv is a function within the sys module that allows us to learn about what the user typed in at the command line.
import sys


def main():
    arg_fun()
    fun_3()
    fun_2()
    fun_1()


def fun_1():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")

    print("hello, my name is", sys.argv[1])


def fun_2():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")

    for arg in sys.argv[1:]:
        print("hello, my name is", arg)


def fun_3():
    if len(sys.argv) == 1:
        print("meow")
    elif len(sys.argv) == 3 and sys.argv[1] == "-n":
        n = int(sys.argv[2])
        for _ in range(n):
            print("meow")
    else:
        print("usage: meows.py [-n NUMBER]")


# How could we check all the arguments that could be inserted by the user?
# We might give up if we have more than a few command-line arguments!
# Luckily, argparse is a library that handles all the parsing of complicated strings of command-line arguments.
def arg_fun():
    import argparse

    parser = argparse.ArgumentParser(description="Meow like a cat")
    parser.add_argument("-n", default=1, help="number of times to meow", type=int)
    args = parser.parse_args()

    for _ in range(args.n):
        print("meow")


if __name__ == "__main__":
    main()
