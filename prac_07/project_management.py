from re import split

from project import Project

def main():
    """Print menu and ask user to input"""
    filename = "projects.txt"
    print("Welcome to Pythonic Project Management")
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from projects.txt")


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