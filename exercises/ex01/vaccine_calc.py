"""A vaccination calculator."""

__author__ = "730332705"

from datetime import datetime, timedelta 

population: float = int(input("Population:"))
doses_a: int = int(input("Doses administered:"))
doses_d: int = int(input("Doses per day:"))
target_p: float = int(input("Target percent vaccinated:"))

vaccines_n: float = ((population) * (target_p / 100) * 2) - (doses_a)
days_needed: int = round(vaccines_n / doses_d)
time_until_target: timedelta = timedelta(days_needed)

today: datetime = datetime.today()
future: datetime = today + time_until_target

print("We will reach " + str(target_p) + "%" + " vaccination in " + str(days_needed) + " days, which falls on " + (future.strftime("%B %d, %Y")))