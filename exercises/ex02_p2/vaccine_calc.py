"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730332705"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    days_n= days_to_target(population, doses, doses_per_day, target)
    futuro= future_date(days_n)
    print("We will reach " + str(target) + "%" + " vaccination in " + str(days_n) + " days, which falls on " + (futuro))
    

def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """A vaccination calculator."""
    vaccines_n: float = ((population) * (target / 100) * 2) - (doses)
    days_needed: int = round(vaccines_n / doses_per_day)
    return days_needed


def future_date(x:int) -> str:
    today: datetime = datetime.today()
    future: datetime = today + days_n
    return (future.strftime("%B %d, %Y"))


if __name__ == "__main__":
    main()
