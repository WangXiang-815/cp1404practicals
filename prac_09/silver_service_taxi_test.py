from silver_service_taxi import SilverServiceTaxi

def main():
    """Test the class SilverServiceTaxi's method"""

    #define a taxi with fanciness
    fancy_taxi = SilverServiceTaxi("Test taxi", 100, 2)
    fancy_taxi.drive(18)

    #print output
    print(fancy_taxi)
    print(fancy_taxi.get_fare())

    #use assert to check if correct
    assert round(fancy_taxi.get_fare(), 2) == 48.78 , "Calculation is not correct"


if __name__ == '__main__':
    main()