from unreliable_car import UnreliableCar

def unreliable_car_test():
    """Test the UnreliableCar class with drive attempts"""
    #Assume cars with 10% and 90% reliability
    unreliable_car = UnreliableCar("Bad car", 100, 10) #10% reliability
    reliable_car = UnreliableCar("Good car",100, 90) #90% reliability

    #drive multiple attempts to see randomness
    for i in range(1,11):
        print(f"Attempting drive {i} km:")
        print(f"{unreliable_car.name:12} drove {unreliable_car.drive(i):2} km")
        print(f"{reliable_car.name:12} drove {reliable_car.drive(i):2} km")

    #print final state of cars
    print(unreliable_car)
    print(reliable_car)

if __name__ == '__main__':
    unreliable_car_test()


