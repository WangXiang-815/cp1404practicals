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
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid choice")
        elif menu_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                drive_distance = float(input("Drive how far? "))
                current_taxi.drive(drive_distance)
                taxi_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${taxi_cost:.2f}")
                total_bill += taxi_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid menu choice")
        print(f"Bill to date: {total_bill:.2f}")
        print(MENU)
        menu_choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis now: ")
    display_taxis(taxis)

def display_taxis(taxis):
    """Display taxis in specified format"""
    for i,taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

if __name__ == '__main__':
    main()