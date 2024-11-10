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


def filter_projects_by_date(projects, date):
    """Filters and displays projects that start after the given date, sorted by date."""
    filtered = [project for project in projects if datetime.strptime(project.start_date, "%d/%m/%Y") > date]
    filtered.sort(key=lambda x: datetime.strptime(x.start_date, "%d/%m/%Y"))

    for project in filtered:
        print(project)

def add_new_project(projects):
    """Adds a new project to the list of projects."""
    name = input("Project Name: ")
    start_date = input("Start Date (DD/MM/YYYY): ")
    priority = input("Project Priority (1-10): ")
    cost_estimate = input("Project Cost Estimate: ")
    completion_percent = input("Project Completion Percent: ")

    new_project = Project(name, start_date, priority, cost_estimate, completion_percent)
    projects.append(new_project)


def update_project(projects):
    """Update the priority and completion percentage of a selected project."""
    print("Select a project to update:")
    for idx, project in enumerate(projects):
        print(f"{idx + 1}. {project.name}")

    choice = int(input("Enter the number of the project to update: ")) - 1
    selected_project = projects[choice]

    print(f"Updating project: {selected_project.name}")
    new_priority = input(f"Enter new priority (current: {selected_project.priority}) or leave blank to keep the same: ")
    new_completion_percent = input(
        f"Enter new completion percentage (current: {selected_project.completion_percent}) or leave blank to keep the same: ")

    if new_priority:
        selected_project.priority = int(new_priority)

    if new_completion_percent:
        selected_project.completion_percent = float(new_completion_percent)
