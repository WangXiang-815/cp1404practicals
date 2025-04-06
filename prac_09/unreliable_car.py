import random
from random import randint
from car import Car

class UnreliableCar(Car):
    """A special car that does not drive reliably"""

    def __init__(self,name, fuel, reliability):
        """Initialize an UnreliableCar with a random reliability percentage
        Args:
            name(str): name of car
            fuel(int): fuel of car
            reliability(int) : 0-100 percentage
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive car only when the random number is less than the car's reliability"""
        #generate random_number
        random_number = randint(0,100)
        if random_number >= self.reliability:
            distance = 0

        #Call parent Class's drive method
        drive_distance = super().drive(distance)
        return drive_distance
