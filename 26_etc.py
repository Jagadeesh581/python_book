def main():
    # map
    yell_without_map("This", "is", "CS50")
    yell_with_map("This", "is", "CS50")
    # type hint. infers that number is int and meows is str
    number: int = int(input("Number: "))
    meows: str = meow(number)
    print(meows, end="")
    # filter
    filter_fun()
    filter_fun_with_lambda()
    # enumerate
    enumerate_fun()


# type hint. infers meow function returns str
def meow(n: int) -> str:
    return "meow\n" * n


def yell_without_map(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


# Notice how *words allows for many arguments to be taken by the function.
# map allows you to map a function to a sequence of values. In practice, we can code as follows:


def yell_with_map(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


def filter_fun():
    # Using Python’s filter function allows us to return a subset of a sequence for which a certain condition is true.
    # In the text editor window, code as follows:
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
    ]

    def is_gryffindor(s):
        return s["house"] == "Gryffindor"

    gryffindors = filter(is_gryffindor, students)

    for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
        print(gryffindor["name"])


def filter_fun_with_lambda():
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
    ]

    gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

    for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
        print(gryffindor["name"])


def enumerate_fun():
    students = ["Hermione", "Harry", "Ron"]

    for i in range(len(students)):
        print(i + 1, students[i])

    # Notice how each student is enumerated when running this code.
    # Utilizing enumeration, we can do the same:
    for i, student in enumerate(students):
        print(i + 1, student)


if __name__ == "__main__":
    main()
