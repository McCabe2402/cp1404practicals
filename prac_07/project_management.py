import os
from datetime import datetime

class Project:
    """A class to represent a project with its details."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percent):
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percent = float(completion_percent)

    def __str__(self):
        """Returns a string representation of the project."""
        return f"{self.name}\t{self.start_date}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percent}"

    def to_dict(self):
        """Returns a dictionary representation of the project."""
        return {
            "name": self.name,
            "start_date": self.start_date,
            "priority": self.priority,
            "cost_estimate": self.cost_estimate,
            "completion_percent": self.completion_percent
        }




