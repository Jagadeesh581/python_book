# A Coroutine is generator which is capable of constantly receiving input data,
# process input data and may or may not return any output.
# Coroutines are majorly used to build better Data Processing Pipelines.
# Similar to a generator, execution of a coroutine stops when it reaches yield statement.
# A Coroutine uses send method to send any input value, which is captured by yield expression.


# token_issuer is a coroutine function, which uses yield to accept name as input.
def token_issuer():
    token_id = 0

    while True:
        name = yield
        token_id += 1
        print(f"Token number of {name} : {token_id}")


t = token_issuer()
next(t)
t.send("JC")
t.send("Python")
t.send("Jagadeesh")
# Execution of coroutine function begins only when 'next' is called on coroutine t.
# This results in the execution of all the statements till a 'yield' statement is encountered.
# Further execution of function resumes when an input is passed using 'send',
# and processes all statements till next 'yield' statement.


def token_issuer(token_id=0):
    try:
        while True:
            name = yield
            token_id += 1
            print(f"Token number of {name} : {token_id}")
    except GeneratorExit:
        print(f"Last issued token is: {token_id}")


t = token_issuer(100)
next(t)
t.send("JC")
t.send("Python")
t.send("Jagadeesh")
t.close()
# The coroutine function token_issuer takes an argument, which is used to set a starting number for tokens.
# When coroutine t is closed, statements under GeneratorExit block are executed.


# Passing input to coroutine is possible only after the first 'next' function call.
# Many programmers may forget to do so, which results in error.
# Such a scenario can be avoided using a decorator.
def coroutine_decorator(func):
    def wrapper(*args, **kwargs):
        c = func(*args, **kwargs)
        next(c)
        return c

    return wrapper


@coroutine_decorator
def token_issuer(token_id=0):
    try:
        while True:
            name = yield
            token_id += 1
            print(f"Token number of {name} : {token_id}")
    except GeneratorExit:
        print(f"Last issued token is: {token_id}")


t = token_issuer(100)
t.send("JC")
t.send("Python")
t.send("Jagadeesh")
t.close()
# coroutine_decorator takes care of calling next on the created coroutine t.
