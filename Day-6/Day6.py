# ⁡⁢⁣⁣​‌‌‍𝘀𝘁𝗮𝗻𝗱𝗮𝗿𝗱 𝗹𝗶𝗯𝗿𝗮𝗿𝗶𝗲𝘀:
# 𝗺𝗮𝘁𝗵, 𝗿𝗮𝗻𝗱𝗼𝗺, 𝗱𝗮𝘁𝗲𝘁𝗶𝗺𝗲.​⁡


import math

# Square root and power
print(math.sqrt(25))        # Output: 5.0
print(math.pow(2, 3))       # Output: 8.0

# Trigonometric functions
angle_in_degrees = 90
angle_in_radians = math.radians(angle_in_degrees)
print(math.sin(angle_in_radians))  # Output: 1.0

# Constants
print(math.pi)  # Output: 3.141592653589793
print(math.e)   # Output: 2.718281828459045



import random

# Generate random numbers
print(random.random())  # Random float: 0.0 <= x < 1.0
print(random.randint(1, 6))  # Random integer: 1 to 6
print(random.uniform(5.5, 10.5))  # Random float: 5.5 <= x <= 10.5

# Random choices
colors = ["red", "green", "blue"]
print(random.choice(colors))  # Randomly selects a color

# Shuffle and sample
deck = list(range(1, 53))  # Simulating a deck of cards
random.shuffle(deck)
print(deck[:5])  # Output: Random 5 cards
print(random.sample(deck, 5))  # Output: Another random 5 cards


from datetime import datetime, date, timedelta

# Current date and time
now = datetime.now()
print(now)  # Output: e.g., 2024-12-27 14:30:00

# Formatting dates
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)  # Output: e.g., 2024-12-27 14:30:00

# Parsing dates
parsed_date = datetime.strptime("2024-12-27", "%Y-%m-%d")
print(parsed_date)  # Output: 2024-12-27 00:00:00

# Date arithmetic
today = date.today()
next_week = today + timedelta(days=7)
print(next_week)  # Output: Today's date + 7 days

# Extracting components
print(today.year, today.month, today.day)  # Output: e.g., 2024 12 27


# ⁡⁢⁣⁣​‌‌‍𝗘𝗿𝗿𝗼𝗿 𝗮𝗻𝗱 𝗘𝘅𝗰𝗲𝗽𝘁𝗶𝗼𝗻 𝗛𝗮𝗻𝗱𝗹𝗶𝗻𝗴 𝗶𝗻 𝗣𝘆𝘁𝗵𝗼𝗻​⁡
# In Python, error and exception handling allows developers to gracefully manage errors that might occur during program execution. This ensures the program does not crash unexpectedly and provides meaningful feedback or corrective measures.

try:
    # Code that may raise an exception
    risky_code()
except SomeException:
    # Code to handle the exception
    handle_exception()
else:
    # Code to execute if no exceptions are raised
    no_exceptions_occurred()
finally:
    # Code that always executes
    cleanup_operations()


# ⁡⁣⁣⁢​‌‌‍‍𝗖𝗼𝗺𝗺𝗼𝗻 𝗘𝘅𝗰𝗲𝗽𝘁𝗶𝗼𝗻𝘀 𝗶𝗻 𝗣𝘆𝘁𝗵𝗼𝗻​⁡
# ⁡⁣⁢⁢Exception	               Description
# ZeroDivisionError	       Raised when dividing by zero.
# ValueError	           Raised when an invalid value is used.
# TypeError	               Raised when an operation is applied to an invalid type.
# IndexError	           Raised when accessing a list with an out-of-range index.
# KeyError	               Raised when accessing a dictionary with a missing key.
# FileNotFoundError	       Raised when a file or directory is requested but not found.
# IOError	               Raised when an input/output operation fails.⁡

try:
    num = int("abc")  # Will raise ValueError
    result = 10 / num  # Could raise ZeroDivisionError
except ValueError:
    print("Error: Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Execution completed.")  # Always executes
    if 'file' in locals():
        file.close()


def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18.")
    return "Access granted."

try:
    print(check_age(16))
except ValueError as e:
    print(e)


try:
    file = open("example.txt", "r")
    process_file(file)
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()