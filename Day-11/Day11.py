# Functional and Decorators
# Lambdas, map, filter, and reduce.
# Decorators and generators.
# itertools for advanced iteration.



# Lambdas
# Lambdas are small, anonymous functions that can be defined inline within a larger expression. They are useful when you need a short, one-time-use function.

add_five = lambda y: y+5+y #ANNOYUMS SINGLEINPUT ==> SINGLE OUTPUT
print(add_five(10))


# Map
# The map() function applies a given function to each item of an iterable (such as a list or tuple) and returns a new iterable with the results.

numbers = [1, 2, 3, 4, 5]
double_numbers = list(map(lambda x: x * 2, numbers))
print(double_numbers)  # Output: [2, 4, 6, 8, 10]


# Filter
# The filter() function constructs an iterator from elements of an iterable for which a function returns true.

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]


# Reduce
# The reduce() function applies a rolling computation to sequential pairs of values in an iterable.

import functools
numbers = [1, 2, 3, 4, 5]
product = functools.reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120




import itertools
#ADVANCED ITERATION
# itertools is a powerful module in Python that provides a variety of tools for advanced iteration. Here are some examples of what you can do with itertools:

#MAINLY USED TO FILTER AND GROUP BIG DATA SEQUENCES WHERE LOOPING CANT HANDLE


# 1. Infinite Iterators
# Generate an infinite sequence of numbers starting from 1
numbers = itertools.count(1)
for _ in range(10):
    print(next(numbers))  # Output: 1, 2, 3, ..., 10

    
# 2. Cyclic Iterators
# Create a cyclic iterator over the sequence [1, 2, 3]
numbers = itertools.cycle([1, 2, 3])
for _ in range(10):
    print(next(numbers))  # Output: 1, 2, 3, 1, 2, 3, ...
    

# 3. Accumulators
import operator
# Calculate the cumulative sum of the sequence [1, 2, 3, 4, 5]
numbers = [1, 2, 3, 4, 5]
cumulative_sum = itertools.accumulate(numbers, operator.add)
print(list(cumulative_sum))  # Output: [1, 3, 6, 10, 15]


# 4. Grouping
# Group a sequence of numbers by their parity (even or odd)
numbers = [1, 2, 3, 4, 5, 6]
groups = itertools.groupby(numbers, key=lambda x: x % 2)
for key, group in groups:
    print(key, list(group))
# Output:
# 1 [1, 3, 5]
# 0 [2, 4, 6]