#Question1
names = input("Enter name: ")

file = open("name.txt",'w')
file.write(names)
file.close()
#Question2

file = open("name.txt", 'r')
names_in_file = file.read()
file.close()

print(f"Hi {names_in_file}!")
#Question3
with open("numbers.txt",'r') as file:
    num1 = int(file.readline())
    num2 = int(file.readline())
results = num1 + num2
print(results)

#Question4
total_results = 0

with open("numbers.txt",'r') as file:
    for line in file:
        total_results += int(line.strip())

print(total_results)

