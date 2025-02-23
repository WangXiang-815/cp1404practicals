"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months_numbers = int(input("How many months? ")) #The variable stores the integer number of months

    for month in range(1, months_numbers + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print_income_report(incomes, months_numbers)

def print_income_report(incomes, months_numbers):
    """Print an income report function"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months_numbers + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


if __name__ == '__main__':
    main()


