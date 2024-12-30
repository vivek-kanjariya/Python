# ⁡⁢⁣⁣​‌‌‍𝗙𝗨𝗡𝗖𝗧𝗜𝗢𝗡𝗦 ​⁡ # Call the function with argument

# ⁡⁣⁣⁢# 𝗗𝗲𝗳𝗶𝗻𝗶𝗻𝗴 𝗙𝘂𝗻𝗰𝘁𝗶𝗼𝗻𝘀⁡
def greet():
    print(f"Hello, world!")
# Calling the function
greet()

# ⁡⁣⁣⁢# 𝗣𝗮𝗿𝗮𝗺𝗲𝘁𝗲𝗿𝘀 𝗮𝗻𝗱 𝗔𝗿𝗴𝘂𝗺𝗲𝗻𝘁𝘀⁡
def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice! ('Alice' is an argument)

# ⁡⁣⁣⁢𝗧𝘆𝗽𝗲𝘀 𝗼𝗳 𝗮𝗿𝗴𝘂𝗺𝗲𝗻𝘁𝘀⁡
#  positional
def add(a, b):
    return a + b
print(add(3, 5))  # Output: 8

# Default
def greet(name="World"):
    print(f"Hello, {name}!")
greet()         # Output: Hello, World!
greet("Alice")  # Output: Hello, Alice!

# Keyword
def describe_pet(animal_type, pet_name):
    print(f"{pet_name} is a {animal_type}.")
describe_pet(pet_name="Buddy", animal_type="dog")  # Output: Buddy is a dog.

# Arbinary Arguments
def sum_all(*numbers):
    return sum(numbers)
print(sum_all(1, 2, 3, 4))  # Output: 10


# ​‌‍‌⁡⁣⁣⁢𝗥𝗲𝘁𝘂𝗿𝗻 𝗧𝘆𝗽𝗲⁡​

def square(num):
    return num * num
result = square(4)
print(result)  # Output: 16

def calculate(a, b):
    return a + b, a - b
add, subtract = calculate(10, 5)
print(add, subtract)  # Output: 15 5


# ​‌‍‌⁡⁣⁣⁢𝗟𝗮𝗺𝗯𝗱𝗮 𝗙𝘂𝗻𝗰𝘁𝗶𝗼𝗻𝘀⁡​
# lambda arguments: expression

square = lambda x: x * x
print(square(5))  # Output: 25

# Using with map, filter, reduce
nums = [1, 2, 3, 4]
squared_nums = list(map(lambda x: x ** 2, nums))
print(squared_nums)  # Output: [1, 4, 9, 16]


# ⁡⁣⁣⁢​‌‍‌𝗙𝘂𝗻𝗰𝘁𝗶𝗼𝗻 𝗦𝗰𝗼𝗽𝗲​⁡
# Local Variables: Declared inside a function and only accessible within it.
# Global Variables: Declared outside a function and accessible globally.

x = 10  # Global variable

def update_x():
    global x  # Modify the global variable
    x = 20

update_x()
print(x)  # Output: 20


# ⁡⁣⁣⁢​‌‍‌𝗥𝗲𝗰𝘂𝗿𝘀𝗶𝗼𝗻​⁡
# Recursion: A function that calls itself to solve a problem recursively.
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120


# ⁡⁣⁣⁢​‌‍‌𝗡𝗲𝘀𝘁𝗲𝗱 𝗙𝘂𝗻𝗰𝘁𝗶𝗼𝗻𝘀​⁡
def outer_function(msg):
    def inner_function():
        print(msg)
    inner_function()

outer_function("Hello from inner!")  # Output: Hello from inner!


# ⁡⁣⁣⁢​‌‍‌‍𝗗𝗲𝗰𝗼𝗿𝗮𝘁𝗼𝗿𝘀​⁡
# Functions that modify the behavior of another function.
def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before the function call
# Hello!
# After the function call

# ⁡⁣⁣⁢​‌‍‌𝗖𝗹𝗼𝘀𝘂𝗿𝗲𝘀​⁡
# Functions that return another function.
# A closure is a function that remembers variables from its enclosing scope.
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

closure = outer_function("Hello from closure!")
closure()  # Output: Hello from closure!


# ⁡⁣⁣⁢​‌‍‌𝗛𝗶𝗴𝗵𝗲𝗿-𝗢𝗿𝗱𝗲𝗿 𝗙𝘂𝗻𝗰𝘁𝗶𝗼𝗻𝘀​⁡
# Functions that take other functions as arguments or return them.
def apply_function(func, value):
    return func(value)

print(apply_function(lambda x: x ** 2, 5))  # Output: 25


# ⁡⁣⁣⁢​‌‍‌‍𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗼𝗿 𝗙𝘂𝗻𝗰𝘁𝗶𝗼𝗻𝘀​⁡
# Generate a sequence of values using the yield keyword.
def generate_numbers(n):
    for i in range(n):
        yield i

for num in generate_numbers(5):
    print(num)
# Output: 0 1 2 3 4




# Feature	                           Description
# Scope	Local vs Global variables.
# Basic Functions	Use def to define reusable code blocks.
# Parameters        Positional, default, *args, **kwargs.
# Return Values     Return single or multiple values.
# Lambda           	Anonymous, one-liner functions.
# Recursion      	A function calling itself for smaller problems.
# Decorators	    Modify behavior of other functions.
# Closures	        Inner functions with memory of enclosing scope.
# Generators	    Efficiently yield sequences of data.