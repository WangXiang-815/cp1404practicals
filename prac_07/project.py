"""
EST: 1.5 hrs
ACT:
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