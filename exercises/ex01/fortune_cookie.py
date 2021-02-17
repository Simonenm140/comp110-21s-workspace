"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730332705"

from random import randint

print("Your fortune cookie says...")

fortune: int = int(randint(1, 4))

if fortune == 1:
    print("You will not fail comp 110")
else:
    if fortune == 2:
        print("You might fail comp110")
    else:
        if fortune == 3:
            print("Grades are a capitalist construct")
        else:
            print("IDRK what I'm doing lolz")

print("Now, go spread positive vibes!")