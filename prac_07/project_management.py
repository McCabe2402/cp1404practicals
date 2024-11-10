import os
from datetime import datetime


class Project:
    """A class to represent a project with its details."""

    DATE_FORMAT = "%d/%m/%Y"  # Class-level constant for date formatting

    def __init__(self, name, start_date, priority, cost_estimate, completion_percent):
        self.name = name
        self.start_date = datetime.strptime(start_date, Project.DATE_FORMAT)
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percent = float(completion_percent)

    def __str__(self):
        """Returns a formatted string representation of the project."""
        start_date_str = self.start_date.strftime(Project.DATE_FORMAT)
        return f"{self.name}\t{start_date_str}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percent}"

    def is_complete(self):
        """Checks if the project is complete (100% completion)."""
        return self.completion_percent == 100.0

    def to_dict(self):
        """Returns a dictionary representation of the project."""
        return {
            "name": self.name,
            "start_date": self.start_date.strftime(Project.DATE_FORMAT),
            "priority": self.priority,
            "cost_estimate": self.cost_estimate,
            "completion_percent": self.completion_percent
        }

    def __lt__(self, other):
        """Compares projects based on priority for sorting."""
        return self.priority < other.priority


def load_or_save_projects(file_path, projects=None, mode='load'):
    """Handles loading or saving projects depending on the mode."""
    if mode == 'load':
        if not os.path.exists(file_path):
            print("The file does not exist!")
            return []
        projects = []
        with open(file_path, "r") as file:
            for line in file.readlines()[1:]:  # Skip header
                fields = line.strip().split("\t")
                if len(fields) == 5:
                    name, start_date, priority, cost_estimate, completion_percent = fields
                    project = Project(name, start_date, priority, cost_estimate, completion_percent)
                    projects.append(project)
        return projects

    elif mode == 'save' and projects is not None:
        with open(file_path, "w") as file:
            file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percent\n")
            for project in projects:
                file.write(f"{project}\n")


def display_projects(projects):
    """Displays incomplete and completed projects, sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_complete()])
    completed = sorted([p for p in projects if p.is_complete()])

    print("\nIncomplete Projects:")
    for project in incomplete:
        print(project)

    print("\nCompleted Projects:")
    for project in completed:
        print(project)


def filter_projects_by_date(projects, date):
    """Filters and displays projects that start after the given date."""
    filtered = [p for p in projects if p.start_date > date]
    filtered.sort(key=lambda x: x.start_date)
    print("\nFiltered Projects:")
    for project in filtered:
        print(project)


def add_new_project(projects):
    """Adds a new project to the list of projects."""
    name = input("Project Name: ")
    start_date = input("Start Date (DD/MM/YYYY): ")
    priority = input("Project Priority (1-10): ")
    cost_estimate = input("Project Cost Estimate: ")
    completion_percent = input("Project Completion Percent: ")

    try:
        new_project = Project(name, start_date, priority, cost_estimate, completion_percent)
        projects.append(new_project)
        print(f"Project '{name}' added successfully!")
    except ValueError as e:
        print(f"Error adding project: {e}")


def update_project(projects):
    """Update the priority and completion percentage of a selected project."""
    if not projects:
        print("No projects available to update.")
        return

    for idx, project in enumerate(projects, 1):
        print(f"{idx}. {project.name}")

    try:
        choice = int(input("Enter the number of the project to update: ")) - 1
        selected_project = projects[choice]
        print(f"Updating project: {selected_project.name}")

        new_priority = input(f"Enter new priority (current: {selected_project.priority}): ")
        new_completion = input(f"Enter new completion percent (current: {selected_project.completion_percent}): ")

        if new_priority:
            selected_project.priority = int(new_priority)
        if new_completion:
            selected_project.completion_percent = float(new_completion)

        print(f"Project '{selected_project.name}' updated successfully!")
    except (ValueError, IndexError):
        print("Invalid selection or input.")
