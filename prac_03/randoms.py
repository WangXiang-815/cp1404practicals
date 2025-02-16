import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

#What did you see on line 1?
#A: Random integer numbers between 5 and 20
#What was the smallest number you could have seen, what was the largest?
#A:5 and 20
#What did you see on line 2?
#A: Random numbers between 3 and 9, step by 2.
#What was the smallest number you could have seen, what was the largest?
#A: 3 and 9
#Could line 2 have produced a 4?
#A: Can't
#What did you see on line 3?
#A: some random floating-point numbers between 2.5 and 5.5
#What was the smallest number you could have seen, what was the largest?
#A:2.5 and 5.5

print(random.randint(1,100)) #produce a random number between 1 and 100 inclusive.