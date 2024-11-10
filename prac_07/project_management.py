import os
from datetime import datetime
from html.parser import incomplete


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


def load_projects(file_path):
    """Load the projects from the file and return a list of Project objects."""
    projects = []
    if not os.path.exists(file_path):
        print("The file does not exist!")
        return projects

    with open(file_path, "r") as file:
        lines = file.readlines()
        header = lines[0]
        for line in lines [1:]:
            fields = line.strip().split("\t")
            if len(fields) == 5:
                name, start_date, priority, cost_estimate, completion_percent = fields
                project = Project(name, start_date, priority, cost_estimate, completion_percent)
                projects.append(project)
    return projects

def save_projects(file_path, projects):
    """Saves the projects to the file and returns the number of saved projects."""
    with open(file_path, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percent\n")
        for project in projects:
            file.write(f"{project}\n")


def display_projects(projects):
    """Displays incomplete and completed projects, both sorted by priority."""
    incomplete = sorted([project for project in projects if project.completion_percent < 100], key=lambda x: x.priority)
    completed = sorted([project for project in projects if project.completion_percent == 100], key=lambda x: x.priority)

    print("Incomplete Projects:")
    for project in incomplete:
        print(project)

    print("\nCompleted Projects:")
    for project in completed:
        print(project)
