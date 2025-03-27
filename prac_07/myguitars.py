
from guitar import Guitar
import csv

def main():
    """Main func load, sort, display and add guitars"""
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    #print guitars info using for loop
    print("These are my guitars:")
    for guitar in guitars:
        print(guitar)

    #print sorted guitars
    guitars.sort()
    print("\nSorted guitars:")
    for guitar in guitars:
        print(guitar)

    #Ask user to input info about new guitar
    print("\nInput new guitar's info: ")
    name = input("Name: ")
    #exit while loop when input is enter
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")

    #Call save_guitars func
    save_guitars(filename, guitars)
    print("Guitars saved!")

def load_guitars(filename):
    """Load guitars info from csv file, using csv reader"""
    #create am empty list to store guitars info
    guitars = []
    #open csv and read
    with open(filename,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row[0], int(row[1]), float(row[2])
            guitars.append(Guitar(name, year, cost))

    return guitars

def save_guitars(filename, guitars):
    """Save a list of guitars to CSV file"""
    with open(filename,'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([[guitar.name, guitar.year, guitar.cost] for guitar in guitars])


if __name__ == '__main__':
    main()