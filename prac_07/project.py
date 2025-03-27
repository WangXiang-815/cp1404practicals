"""
EST: 1.5 hrs
ACT: 2.5 hrs
Project class
"""
import datetime
class Project:

    def __init__(self, name, start_date, priority, cost_estimate, completion_percent):
        """Initialize Project
            Args:
                name(str): the name of project
                start_date(str): the start date of project
                priority(int): the priority of the project (1 being the highest)
                cost_estimate(float): the estimated cost of project
                completion_percent(float): 0-100 the percentage of completion
        """
        self.name = name
        #using the datetime module as expected
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percent = completion_percent

    def __str__(self):
        """Return a string representation of the project"""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percent}%"

    def is_complete(self):
        """Return Boolean True if completion is 100"""
        return self.completion_percent == 100

    def __lt__(self, other):
        """Comparison for sorting by priority"""
        return self.priority < other.priority