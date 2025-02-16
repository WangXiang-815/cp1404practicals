#loop example, count odd numbers from 1-20
for i in range(1, 21, 2):
    print(i, end=' ')
print("\n")

#a. Count 10s from 0 to 100.
for i in range(0,101,10):
    print(i, end=' ')
print("\n")

#b. Count down from 20 to 1
for i in range(20,0,-1):
    print(i, end=' ')
print("\n")

#c. print n stars. Ask the user for a number, then print that many stars (*), all on one line.
n = int(input("Number of stars: "))
print("*"*n)

#d. print n lines of increasing stars
n = int(input("Number of lines: "))

for i in range(1, n + 1):
    print("*" * i)