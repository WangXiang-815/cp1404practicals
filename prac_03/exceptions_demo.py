"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A: when input a letter or a symbol
2. When will a ZeroDivisionError occur?
A: the denominator is input to 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
A: the changes are below
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("can't divide by 0")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
