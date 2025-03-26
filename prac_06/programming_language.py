"""
Estimate time: 25 mins
Start time: 13:59 10th March
Finish time:
Actual time:
"""


class ProgrammingLanguage:

    def __init__(self, name,typing, reflection, year):
        """Construct a ProgrammingLanguage in value listed in readme.md"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """return the Boolean value to check if a programming language's typing is dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of ProgrammingLanguage"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"


