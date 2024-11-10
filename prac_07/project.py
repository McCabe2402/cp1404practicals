from project_management import Project, add_new_project, update_project, load_or_save_projects, display_projects, filter_projects_by_date
from datetime import datetime


def main():
    """Main menu for the project management program."""
    projects = []
    menu_options = {
        '1': "Load projects",
        '2': "Save projects",
        '3': "Display projects",
        '4': "Filter projects by date",
        '5': "Add new project",
        '6': "Update project",
        '7': "Exit"
    }

    choice = None
    while choice != '7':
        print("\nMenu:")
        for option, description in menu_options.items():
            print(f"{option}. {description}")

        choice = input("Select an option: ").strip()

        if choice == '1':
            file_path = input("Enter filename to load projects: ").strip()
            projects = load_or_save_projects(file_path, mode='load')
            if projects:
                print(f"Loaded {len(projects)} projects from {file_path}.")
            else:
                print("No projects loaded or file not found.")

        elif choice == '2':
            if not projects:
                print("No projects to save. Please add or load projects first.")
                continue
            file_path = input("Enter filename to save projects: ").strip()
            load_or_save_projects(file_path, mode='save', projects=projects)
            print(f"Projects saved to {file_path}.")

        elif choice == '3':
            if not projects:
                print("No projects to display. Please add or load projects first.")
                continue
            display_projects(projects)

        elif choice == '4':
            try:
                date_input = input("Enter date to filter projects (DD/MM/YYYY): ").strip()
                date = datetime.strptime(date_input, "%d/%m/%Y")
                filter_projects_by_date(projects, date)
            except ValueError:
                print("Invalid date format. Please use DD/MM/YYYY.")

        elif choice == '5':
            add_new_project(projects)
            print("New project added successfully.")

        elif choice == '6':
            if not projects:
                print("No projects to update. Please add or load projects first.")
                continue
            update_project(projects)
            print("Project updated successfully.")

        elif choice != '7':
            print("Invalid choice, please try again.")

    print("Exiting program. Goodbye!")


if __name__ == "__main__":
    main()
