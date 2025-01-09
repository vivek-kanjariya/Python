# PROFILING AND OPTIMISATION
#Profiling and optimization in Python involve analyzing your code to identify performance bottlenecks and improving its efficiency.

# WHY ITS USED ?
# Optimize time-critical tasks in large programs.
# Reduce memory consumption.
# Improve the scalability of the application.

#HOW TO DO ITTTTTT

# cProfile: A built-in module to profile your code’s execution time.
import cProfile

def compute():
    result = sum(range(10**6))
    return result

cProfile.run('compute()')


# timeit Module: Measure the execution time of small code snippet
import timeit

code = "sum(range(10**6))"
time = timeit.timeit(code, number=100)
print(f"Time taken: {time} seconds")








# MEMORY PERFOLLINGGGGGGG
# memory_profiler: Analyze memory usage of Python code.

# Install using pip install memory_profiler.
# Use @profile to annotate functions.

# from memory_profiler import profile

# @profile
# def allocate_memory():
#     data = [i for i in range(10**6)]
#     return data

# allocate_memory()


# Garbage Collection Profiling Use the gc module to analyze object creation and deletion.
import gc
print(gc.collect()) #
print(gc.get_count())  # View the number of objects in generations













# Regular Expressions (re module)
# Regular expressions (regex) are a powerful tool for matching, searching, and manipulating text based on patterns. They are often underrated because they seem complex, but mastering them unlocks efficient text processing capabilities.

# Why Use Regular Expressions?
# Data Validation: Check if data matches a specific format (e.g., email, phone numbers).
# String Searching: Locate substrings within larger strings.
# Text Extraction: Pull out specific parts of a string (e.g., dates, prices).
# Substitution: Replace patterns in text efficiently.

# Common Functions
# re.match(): Checks for a match only at the beginning of the string.
# re.search(): Searches for the first occurrence of the pattern anywhere in the string.
# re.findall(): Returns all occurrences of the pattern as a list.
# re.sub(): Substitutes matches with a replacement string.


# Regex Syntax
# .: Matches any character (except newline).
# \d: Matches any digit.
# \w: Matches any word character (alphanumeric + underscore).
# \s: Matches any whitespace.
# *, +, ?: Quantifiers (0 or more, 1 or more, optional).
# [abc]: Matches any one of the characters inside the brackets.
# [^abc]: Matches any character not in the brackets.
# ^: Start of string; $: End of string


import re

# Match at the beginning
result = re.match(r'\d+', '123abc')
print(result.group())  # Output: '123'

# Search anywhere in the string
result = re.search(r'[a-z]+', '123abc')
print(result.group())  # Output: 'abc'

# Find all matches
result = re.findall(r'\d', 'a1b2c3')
print(result)  # Output: ['1', '2', '3']

# Replace matches
result = re.sub(r'\d', '#', 'a1b2c3')
print(result)  # Output: 'a#b#c#'




# Advanced Features
# Lookahead/Lookbehind: Match patterns before or after a specific condition without including it in the result.

# Positive Lookahead: Match "foo" followed by "bar"
result = re.search(r'foo(?=bar)', 'foobar')
print(result.group())  # Output: 'foo'

# Negative Lookbehind: Match "bar" not preceded by "foo"
result = re.search(r'(?<!foo)bar', 'bazbar')
print(result.group())  # Output: 'bar'


# Named Groups: Label matches for better readability.
result = re.search(r'(?P<area>\d{3})-(?P<number>\d{7})', '123-4567890')
print(result.group('area'))  # Output: '123'
print(result.group('number'))  # Output: '4567890'




#PRACTICALSSSSSS
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
email = "test@example.com"
print(bool(re.match(pattern, email)))  # Output: True

text = "Loving #Python and #Regex!"
hashtags = re.findall(r'#\w+', text)
print(hashtags)  # Output: ['#Python', '#Regex']