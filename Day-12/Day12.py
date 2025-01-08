#  Iterators and Iterables

# What is an Iterable?
# Think of an iterable as something you can loop through (e.g., using a for loop). Examples include lists, strings, and tuples.

#example
my_list = [2,4,6,3,2]
for i in my_list:
    print(i) #print all elements
    
# What is an Iterator?
# An iterator is like a bookmark for an iterable. It helps keep track of where you are when looping. You create an iterator from an iterable using the iter() function.

#example
my_list = [1, 2, 3]
my_iterator = iter(my_list)
print(next(my_iterator))  # Prints 1
print(next(my_iterator))  # Prints 2 #prints one by one elements

# Key difference:

# An iterable can be looped over.
# An iterator remembers where you are in the loop and gives you one item at a time.










# Generators


# What is a Generator?
# A generator is like a factory that produces values one at a time instead of creating everything upfront. This saves memory!

# How to make one? Use the yield keyword instead of return.

def count_upto(s):
    counter = 0
    while counter <= s:
        yield counter
        counter += 1

for i in count_upto(5):
    print(i)        # Prints 1, 2, 3, 4, 5
    
# Why use Generators?
# Generators are memory-efficient because they don’t store all the data in memory at once. They generate items on-the-fly.











# Context Managers



# What is a Context Manager?
# A context manager is used to handle resources (like files) safely. It ensures resources are properly cleaned up, even if something goes wrong.


#example
with open("example.txt", "w") as file:
    file.write("Hello, world!")
# The with statement makes sure the file is closed automatically after writing.

#example
class ResourceManager:
    def __enter__(self):
        print("Resources Acquired")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("Resources Released")
        
with ResourceManager() as Manager:
    print("Using Resources")
    
#output
# Resources Acquired
# Using Resources
# Resources Released











# Coroutines and Asynchronous Programming


# What is Asynchronous Programming?
# Imagine you’re cooking pasta and you need to boil water. Instead of waiting for the water to boil, you start chopping vegetables. That’s asynchronous programming—doing multiple tasks at once.

# Key Terms:
# async: Declares an asynchronous function.
# await: Waits for an asynchronous task to finish.
# Event Loop: Manages and schedules asynchronous tasks.
#MAINLY USED IN API WRITING AND WEB DEVELOPMENT
import asyncio

async def Boil_water():
    print("Boiling water...")
    await asyncio.sleep(5)  # Simulate waiting for 5 seconds
    print("water is ready")
    
async def chop_vegetables():
    print("Chopping vegetables...")
    await asyncio.sleep(1)   # Simulate waiting for 1 second
    print("Vegetables are ready!")
    
async def cook():
    await asyncio.gather(   Boil_water(),
                            chop_vegetables()   )
    
asyncio.run(cook())












# Typing and Annotations


# Why Use Typing?
# In large projects, it helps to know what kind of data a function expects and returns.

# Basic Syntax:
# Use the typing module for type hints.

#example
from typing import List, Dict

def greet(name: str) -> str:
    return f"Hello, {name}!"

def add_numbers(numbers: List[int]) -> int:
    return sum(numbers)

print(greet("Alice"))  # Output: Hello, Alice!
print(add_numbers([1, 2, 3]))  # Output: 6

#GENERAL SYNTAX
# (INPUT ARGU TAG : INPUT DATA TYPE) -> RETURN DATA TYPE