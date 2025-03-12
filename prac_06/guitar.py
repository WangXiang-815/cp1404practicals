"""
Estimated time:25mins
Actual time:
"""

class Guitar:


    def __init__(self, name, year, cost):
        "Initialize Guitar"
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        "Return a string representation of Guitar"
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        "Return a guitar's age"
        current_year = 2025
        return current_year - self.year

    def is_vintage(self):
        "Return True if guitar is over 50 years old"
        return self.get_age() >= 50
