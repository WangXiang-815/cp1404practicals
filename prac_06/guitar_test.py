"""
manual test for Guitar
"""
from prac_06.guitar import Guitar


def run_tests():
    "Test Guitar's is_vintage and get_age func"
    current_year = 2025
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 1512.90)

    #Test get_age()
    print(f"{guitar1.name} get_age() - Expected 103. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected 103. Got {guitar2.get_age()}")

    #Test is_vintage()
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")

#Call run_test func
if __name__ == '__main__':
    run_tests()