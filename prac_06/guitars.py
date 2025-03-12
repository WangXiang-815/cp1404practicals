"""
Client program for Guitar
"""
from prac_06.guitar import Guitar


def main():
    "Ask input and append to a nested list"
    guitars =[]  #Define guitars to store lists

    print("My guitars!") #Print welcome message
    name = input("Name: ") #Ask user to input name

    #while loop to get year and cost input, when input is none, gets out of loop
    while name != '':
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, " added.")
        name = input("Name: ")

    #append 2 guitars mentioned in readme.md
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("These are my guitars! ")

    #calculate max width for name
    max_name_length = max(len(guitar.name) for guitar in guitars)
    #calculate max width for cost
    max_cost_length = max(len(str(guitar.cost)) for guitar in guitars)

    #for loop to check if vintage and print each guitar's info
    for i,guitar in enumerate(guitars,1):
        vintage_string = ' (vintage)' if guitar.is_vintage() else ''
        print(f"Guitar{i} : {guitar.name:>{max_name_length}} ({guitar.year}), worth ${guitar.cost:<{max_cost_length}}")




main()