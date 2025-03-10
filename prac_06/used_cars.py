"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    #create a new car object named 'Limo' with 100 fuel.
    limo = Car(100)
    #add 20 fuel to limo
    limo.add_fuel(20)
    #print the current fuel of Limo
    print(limo.fuel)
    #drive limo 115km using the drive method
    limo.drive(115)


main()