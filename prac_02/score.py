import random

# Function to determine the result based on the score
def get_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

def main():
    # Get the user's score
    score = float(input("Enter score: "))
    # Get the result based on the user's score
    result = get_score_result(score)
    print(result)

    # Generate a random score between 0 and 100
    random_score = random.uniform(0, 100)
    print(f"Random score: {random_score:.2f}")
    # Get the result based on the random score
    random_result = get_score_result(random_score)
    print(random_result)

if __name__ == "__main__":
    main()
