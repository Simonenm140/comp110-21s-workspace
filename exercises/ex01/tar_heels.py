"""An exercise in remainders and boolean logic."""

__author__ = "730332705"

entry: int = int(input("Enter an int:")) 

if (entry % 2 == 0) and (entry % 7 != 0):
    print("TAR")
if (entry % 7 == 0) and (entry % 2 != 0):
    print("HEELS")
if (entry % 2 == 0) and (entry % 7 == 0):
    print("TAR HEELS")
if (entry % 2 != 0) and (entry % 7 != 0):
    print("CAROLINA")