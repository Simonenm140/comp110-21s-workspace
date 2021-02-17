"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730332705"

fortune: int = int(randint(1, 4))


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """Program that outputs one of at least four random, good fortunes."""
    if fortune == 1:
        return("You will not fail comp 110")
    else:
        if fortune == 2:
            return("You might fail comp110")
    if fortune == 3:
        return("Grades are a capitalist construct")
    else:
        return("IDRK what I'm doing lolz")


if __name__ == "__main__":
    main()
