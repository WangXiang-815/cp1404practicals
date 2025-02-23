"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subjects_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data=[]   #create a list to store parts.
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        data.append(parts) #Add parts to the list.
        print("----------")
    input_file.close()
    return data

def display_subjects_details(data):
    """Display subjects details in the required format,EG:CP1401 is taught by Ada Lovelace and has 192 students"""
    for subjects_details in data:
        print(f"{subjects_details[0]} is taught by {subjects_details[1]} and has {subjects_details[2]} students")

main()