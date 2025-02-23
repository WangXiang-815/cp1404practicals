import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def main():
    """Main func ask user to input how many picks they want"""
    num_picks = int(input("How many picks? "))
    for i in range(num_picks):
        print(" ".join(f"{num:2}" for num in generate_pick()))

def generate_pick():
    """Generate sorted numbers for picks"""
    quick_pick =[] #create list to store
    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER,MAX_NUMBER)
        if number not in quick_pick:    #Avoid the repeated numbers
            quick_pick.append(number)
    quick_pick.sort()     #sort by ascending order
    return quick_pick     #return value

if __name__ == '__main__':
    main()