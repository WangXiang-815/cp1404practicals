name = input("Enter name: ")

MENU = """(H)ello
(G)oodbye
(Q)uit"""

print(MENU)
choice = input(">>> ").upper()  #Capitalized the letter user input, make codes more user-friendly

while choice != "Q":
    if choice == "H":
        print(f"Hello, {name}")
    elif choice == "G":
        print(f"Goodbye, {name}")
    else:
        print("Invalid choice")

    print(MENU)
    choice = input(">>> ").upper()

print("Thanks for using!")
