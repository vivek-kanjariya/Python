# ⁡⁣⁢⁣𝗧𝗼𝗽𝗶𝗰𝘀 𝗖𝗼𝘃𝗲𝗿𝗲𝗱 
#               , File I/O Operations
#               , INPUTS,OUTPUTS Statements
#               , 𝗖𝗼𝗻𝘁𝗿𝗼𝗹 𝗦𝘁𝗮𝘁𝗲𝗺𝗲𝗻𝘁𝘀
#               , 𝗖𝗼𝗺𝗺𝗲𝗻𝘁𝘀
#               , 𝗜𝗗𝗘, 𝗣𝘆𝘁𝗵𝗼𝗻 𝟯⁡ 


# ​‌‍‌⁡⁢⁣⁣𝗖𝗼𝗻𝘁𝗿𝗼𝗹 𝗦𝘁𝗮𝘁𝗲𝗺𝗲𝗻𝘁𝘀⁡​


# ⁡⁣⁣⁢# 𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻𝗮𝗹 𝗦𝘁𝗮𝘁𝗲𝗺𝗲𝗻𝘁𝘀⁡

# if statement
x = 10
if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5

# if-else statement
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")  # Output: y is not greater than 5

# if-elif-else statement
z = 0
if z > 0:
    print("z is positive")
elif z == 0:
    print("z is zero")  # Output: z is zero
else:
    print("z is negative")

# ⁡⁣⁣⁢𝗟𝗼𝗼𝗽 𝗖𝗼𝗻𝘁𝗿𝗼𝗹 𝗦𝘁𝗮𝘁𝗲𝗺𝗲𝗻𝘁𝘀⁡

# for loop
for i in range(3):
    print(i)  # Output: 0 1 2

# while loop
n = 3
while n > 0:
    print(n)  # Output: 3 2 1
    n -= 1

# ⁡⁣⁣⁢𝗕𝗿𝗮𝗻𝗰𝗵𝗶𝗻𝗴 𝗦𝘁𝗮𝘁𝗲𝗺𝗲𝗻𝘁𝘀⁡

# break statement
for num in range(5):
    if num == 3:
        break
    print(num)  # Output: 0 1 2

# continue statement
for num in range(5):
    if num == 3:
        continue
    print(num)  # Output: 0 1 2 4

# pass statement
for num in range(3):
    pass  # Placeholder; does nothing

# else with loops
for num in range(3):
    print(num)  # Output: 0 1 2
else:
    print("Loop finished")  # Output: Loop finished



# # ⁡⁣⁣⁢┌───────────────┐
# # │ 𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻𝗮𝗹   │  𝗶𝗳, 𝗶𝗳-𝗲𝗹𝘀𝗲, 𝗶𝗳-𝗲𝗹𝗶𝗳-𝗲𝗹𝘀𝗲
# # └───────────────┘
# # ┌───────────────┐
# # │ 𝗟𝗼𝗼𝗽𝗶𝗻𝗴       │  𝗳𝗼𝗿, 𝘄𝗵𝗶𝗹𝗲
# # └───────────────┘
# # ┌───────────────┐
# # │ 𝗕𝗿𝗮𝗻𝗰𝗵𝗶𝗻𝗴     │  𝗯𝗿𝗲𝗮𝗸, 𝗰𝗼𝗻𝘁𝗶𝗻𝘂𝗲, 𝗽𝗮𝘀𝘀, 𝗲𝗹𝘀𝗲 𝘄𝗶𝘁𝗵 𝗹𝗼𝗼𝗽𝘀
# # └───────────────┘
# ⁡


# ​‌‌‍⁡⁢⁣⁣𝗜𝗡𝗣𝗨𝗧/𝗢𝗨𝗧𝗣𝗨𝗧 𝗦𝘁𝗮𝘁𝗲𝗺𝗲𝗻𝘁𝘀⁡​ 

# ​‌‍‌⁡⁣⁣⁢𝗶𝗻𝗽𝘂𝘁 𝘀𝘁𝗮𝘁𝗲⁡​

# Input from user
name = input("Enter your name: ")  # Prompt for user
print(f"Hello, {name}!")  # Output: Hello, <name entered by user>

# Converting input to a number
age = int(input("Enter your age: "))  # Converts the input to an integer
print(f"You are {age} years old.") #

# ​‌‍‌⁡⁣⁣⁢𝗢𝘂𝘁𝗽𝘂𝘁 𝗦𝘁𝗮𝘁𝗲⁡​

age = 25
print(f"{name} is {age} years old.")  # Output: Alice is 25 years old.


# ​‌‌‍⁡⁢⁣⁣ 𝗙𝗶𝗹𝗲 𝗜/𝗢 𝗢𝗽𝗲𝗿𝗮𝘁𝗶𝗼𝗻𝘀⁡​
# Python provides built-in functions to work with files: open(), read(), write(), and close().

# Open a file
file = open("filename", mode)

# Modes:

# 'r': Read mode (default)
# 'w': Write mode (overwrites)
# 'a': Append mode
# 'rb'/'wb': Binary modes
# 'r+'/'w+': Read/write mode

# Open a file in read mode
file = open("example.txt", "r")
content = file.read()  # Read entire file
print(content)
file.close()

# Open a file in write mode
file = open("example.txt", "w")
file.write("This is a test.")  # Write content to file
file.close()

# Open a file in append mode
file = open("example.txt", "a")
file.write("\nAdding another line.")
file.close()

# FOR READING LINE BY LINE

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # Output each line without extra spaces

with open("example.txt", "w") as file:
    file.write("Using with statement.") # Output each line without extra spaces

# EXAMPLEEEEE
# A program to take input and save it to a file
name = input("Enter your name: ")
age = input("Enter your age: ")

# Save input to a file
with open("user_data.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")

print("Data saved successfully!")

#for skipping an specific Iteration
for i in range(5):
    if i == 3:
        continue
    print(i)

#for breaking an specific Iteration/Out of loop
for i in range(5):
    if i == 3:
        break
    print(i)