
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

if __name__ == '__main__':
    main()