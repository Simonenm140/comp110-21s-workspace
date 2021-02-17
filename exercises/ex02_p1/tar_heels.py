"""Tar Heels exercise redux as a structured program."""

__author__ = "730332705"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))


def tar_heels(x: int) -> str:
    """An exercise in remainders and boolean logic."""
    if x % 2 == 0 and x % 7 != 0:
        return "TAR"
    if x % 7 == 0 and x % 2 != 0:
        return "HEELS"
    if x % 2 == 0 and x % 7 == 0:
        return "TAR HEELS"
    if x % 2 != 0 and x % 7 != 0:
        return "CAROLINA"


if __name__ == "__main__":
    main()