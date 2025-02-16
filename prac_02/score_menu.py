# Function to get a valid score (0-100 inclusive)
def get_valid_score():
    while True:
        score = float(input("Enter score: "))
        if 0 <= score <= 100:
            return score
        else:
            print("Invalid score. Please enter a score between 0 and 100.")


# Function to determine the result based on score
def determine_result(score):
    if score < 50:
        return "Bad"
    elif score >= 50 and score < 90:
        return "Passable"
    elif score >= 90:
        return "Excellent"
    else:
        return "Invalid score"


# Function to print stars based on score
def show_stars(score):
    print('*' * int(score))  # Print the score number of stars


def main():
    # Get a valid score before entering the menu loop
    score = get_valid_score()

    # Main menu loop
    while True:
        # Display the menu
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        # Get user input
        choice = input(">>> ").upper()

        if choice == 'G':
            # Get a valid score again
            score = get_valid_score()
        elif choice == 'P':
            # Print the result based on the score
            result = determine_result(score)
            print(f"Result: {result}")
        elif choice == 'S':
            # Show stars based on the score
            show_stars(score)
        elif choice == 'Q':
            # Quit the program
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
