import datetime

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
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects(projects)
        elif choice == 'a':
            add_projects(projects)
        elif choice == 'u':
            update_projects(projects)
        else:
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

        save_choice = input("Would you")

def save_projects(filename, projects):
    """Save the projects list to txt file"""
    with open(filename,'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")  # Write header
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")


def update_projects(projects):
    """Update the completion percentage, priority of projects"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
        print(project)

        new_percentage = input("New Percentage: ")
        new_priority = input("New Priority: ")

        if new_percentage:
            project.completion_percent = int(new_percentage)
        if new_priority:
            project.priority = int(new_priority)
    except(ValueError, IndexError):
        print("Invalid choice, please try again.")

def add_projects(projects):
    """Add a new project to the list"""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion_percentage = input("Percent complete: ")
    projects.append(Project(name, start_date, int(priority), float(cost_estimate), float(completion_percentage)))

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

def filter_projects(projects):
    """Filter and show projects after the date input, sorted by date"""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered = [project for project in projects if project.start_date > date]
        for project in sorted(filtered, key=lambda x:x.start_date): #__lt__ is defined in Class Project, compared by priority
            print(project)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")



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