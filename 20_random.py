# random is a library that comes with Python that you could import into your own project.
import random


# pick one from list.
coin = random.choice(["heads", "tails"])
print(coin)
# pick an integer from given range.
number = random.randint(1, 10)
print(number)
# shuffle list into random order.
cards = ["king", "queen", "jack"]
random.shuffle(cards)
print(cards)
# list of methods in random package.
print(dir(random))
