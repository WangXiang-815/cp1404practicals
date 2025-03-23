"""
Estimated time:25mins
Actual time: 50mins
"""

class Guitar:


    def __init__(self, name = "", year = 0, cost = 0):
        """
        Initialize Guitar
        Args:
        name (str): The name of the guitar (default is empty string).
        year (int): The year the guitar was made (default is 0).
        cost (float): The cost of the guitar (default is 0.0).
        """
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
