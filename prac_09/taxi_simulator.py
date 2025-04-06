"""
Taxi_simulator exercise
EST:1.5hrs
ACT:
"""

from car import Car
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """A taxi simulator program matches readme.md's requirements"""
    total_bill = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo",100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxis_choice = input("Choose taxi: ")
        elif choice == "d":

def display_taxis(taxis):
    """Display taxis in specified format"""
    for i,taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

