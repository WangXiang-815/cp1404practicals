import datetime
from html.parser import incomplete

from project import Project

def main():
    """Print menu and ask user to input"""
    filename = "projects.txt"
    print("Welcome to Pythonic Project Management")
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from projects.txt")

    #Display menu
    print("""
    Please select an option:
    - (L)oad projects from file
    - (S)ave projects to file
    - (D)isplay projects
    - (F)ilter projects by start date
    - (A)dd new project
    - (U)pdate project details
    - (Q)uit
    """)
    #Ask input
    choice = input('>>> ').strip().lower()
    while choice != 'q':
        if choice == 'l':
           projects = load_projects(filename)
        elif choice == 's':
            save_projects(filename, projects) #TODO:write save_projects
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects(projects) #TODO: filter_projects
        elif choice == 'a':
            add_projects(projects)  #TODO: add_projects
        elif choice == 'u':
            update_projects(projects) #TODO: update_projects
        elif:
            print("Invalid input, please try again")

        print("""
            Please select an option:
            - (L)oad projects from file
            - (S)ave projects to file
            - (D)isplay projects
            - (F)ilter projects by start date
            - (A)dd new project
            - (U)pdate project details
            - (Q)uit
            """)
        choice = input('>>> ').strip().lower()

def display_projects(projects):
    """Display projects by completion status and sorted by priority"""
    #create two lists to group projects by completion status
    incomplete_projects = [project for project in projects if not project.is_complete()]
    complete_projects = [project for project in projects if project.is_complete()]

    #print sorted incomplete projects
    print("Incomplete projects: ")
    for project in sorted(incomplete_projects):
        print(' ', project) # ' ' to add indentation
    #print sorted complete projects
    print("Complete projects: ")
    for project in sorted(complete_projects):
        print(' ', project)


def load_projects(filename):
    """Load projects from file and return a list"""
    #create an empty nested list to store projects
    projects = []
    with open(filename,'r') as file:
        file.readline()  # remove header
        for line in file:
            parts = line.strip().split("\t") #Split by Tab
            name, start_date, priority, cost_estimate, completion_percent = parts
            projects.append(Project(name, start_date, int(priority), float(cost_estimate), float(completion_percent)))

    return projects


if __name__ == '__main__':
    main()