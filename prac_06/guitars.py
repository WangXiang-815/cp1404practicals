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
        year = input("Year: ")
        cost = input("Cost: ")
        guitar_to_add = Guitar(name, year, cost)

