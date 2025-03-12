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


