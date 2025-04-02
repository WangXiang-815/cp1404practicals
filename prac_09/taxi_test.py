"""taxi_test codes
EST:25mins
ACT:
"""
#import class Taxi
from taxi import Taxi

#create new object
my_taxi = Taxi("Prius 1",100)

#drive taxi 40 kms
my_taxi.drive(40)

#print current fare
print(my_taxi)
print(f"The current fare is {my_taxi.get_fare():.2f}")



