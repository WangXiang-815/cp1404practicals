numbers = [] #create list for further storing the numbers input
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
#Ask the user to input the number for 5 times
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

# Output the required value
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average number is {sum(numbers) / len(numbers)}")

#Authority checker
user_input = input("Enter your name: ")

#Check if input is authorized
if user_input in usernames:
    print("Access Granted!")
else:
    print("Access Denied!")