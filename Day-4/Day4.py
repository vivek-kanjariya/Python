# ⁡⁢⁣⁣​‌‌‍𝗟𝗶𝘀𝘁𝘀, 𝘁𝘂𝗽𝗹𝗲𝘀, 𝘀𝗲𝘁𝘀, 𝗮𝗻𝗱 𝗱𝗶𝗰𝘁𝗶𝗼𝗻𝗮𝗿𝗶𝗲𝘀.​⁡



# ⁡⁣⁣⁢​‌‍‌𝗟𝗶𝘀𝘁𝘀​⁡
# Definition: A list is an ordered, mutable (modifiable) collection that allows duplicate elements.
# Syntax: Defined using square brackets [].
# Features:
# Ordered (maintains the insertion order).
# Mutable (can be modified after creation).
# Allows duplicate elements.
# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # Output: apple

# Modifying elements
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Adding elements
fruits.append("date")  # Add at the end
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date']

# Removing elements
fruits.remove("cherry")  # Remove by value
print(fruits)  # Output: ['apple', 'blueberry', 'date']

# Iterating over a list
for fruit in fruits:
    print(fruit)


# ⁡⁣⁣⁢​‌‍‌𝗧𝘂𝗽𝗹𝗲𝘀​⁡
# Definition: A tuple is an ordered, immutable collection that allows duplicate elements.
# Syntax: Defined using parentheses ().
# Features:
# Ordered.
# Immutable (cannot be modified after creation).
# Allows duplicate elements.
# Creating a tuple
colors = ("red", "green", "blue")

# Accessing elements
print(colors[1])  # Output: green

# Iterating over a tuple
for color in colors:
    print(color)

# Tuple unpacking
r, g, b = colors
print(r, g, b)  # Output: red green blue

# Immutability:
# Although tuples cannot be modified directly, you can create a new tuple by combining existing tuples:z
new_colors = colors + ("yellow",)
print(new_colors)  # Output: ('red', 'green', 'blue', 'yellow')




# ⁡⁣⁣⁢​‌‌‍ 𝗦𝗲𝘁𝘀​⁡
# Definition: A set is an unordered collection of unique elements.
# Syntax: Defined using curly braces {} or the set() function.
# Features:
# Unordered (no specific order of elements).
# Does not allow duplicates.
# Mutable (elements can be added or removed).
# Creating a set
numbers = {1, 2, 3, 4}

# Adding elements
numbers.add(5)
print(numbers)  # Output: {1, 2, 3, 4, 5}

# Removing elements
numbers.remove(2)
print(numbers)  # Output: {1, 3, 4, 5}

# Checking membership
print(3 in numbers)  # Output: True

# Iterating over a set
for num in numbers:
    print(num)


# ⁡⁣⁣⁢​‌‌‍
#  𝗗𝗶𝗰𝘁𝗶𝗼𝗻𝗮𝗿𝗶𝗲𝘀​⁡
# Definition: A dictionary is an unordered collection of key-value pairs.
# Syntax: Defined using curly braces {} with key: value pairs.
# Features:
# Keys must be unique and immutable (e.g., strings, numbers, tuples).
# Values can be mutable and can have duplicates.
# Unordered (insertion order is maintained in Python 3.7+).
# Creating a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}

# Accessing values
print(person["name"])  # Output: Alice

# Adding or updating key-value pairs
person["age"] = 26  # Update
person["country"] = "USA"  # Add
print(person)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}

# Removing key-value pairs
del person["city"]
print(person)  # Output: {'name': 'Alice', 'age': 26, 'country': 'USA'}

# Iterating over a dictionary
for key, value in person.items():
    print(f"{key}: {value}")



# ⁡⁢⁣⁢​‌‌‌𝗜𝗠𝗣​⁡

# ⁡⁣⁢⁣​‌‍‌𝘊𝘩𝘰𝘰𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘙𝘪𝘨𝘩𝘵 𝘋𝘢𝘵𝘢 𝘚𝘵𝘳𝘶𝘤𝘵𝘶𝘳𝘦
# 𝘜𝘴𝘦 𝘭𝘪𝘴𝘵𝘴 𝘧𝘰𝘳 𝘰𝘳𝘥𝘦𝘳𝘦𝘥, 𝘮𝘶𝘵𝘢𝘣𝘭𝘦 𝘤𝘰𝘭𝘭𝘦𝘤𝘵𝘪𝘰𝘯𝘴.
# 𝘜𝘴𝘦 𝘵𝘶𝘱𝘭𝘦𝘴 𝘧𝘰𝘳 𝘧𝘪𝘹𝘦𝘥, 𝘪𝘮𝘮𝘶𝘵𝘢𝘣𝘭𝘦 𝘤𝘰𝘭𝘭𝘦𝘤𝘵𝘪𝘰𝘯𝘴.
# 𝘜𝘴𝘦 𝘴𝘦𝘵𝘴 𝘧𝘰𝘳 𝘶𝘯𝘪𝘲𝘶𝘦 𝘦𝘭𝘦𝘮𝘦𝘯𝘵𝘴 𝘢𝘯𝘥 𝘴𝘦𝘵 𝘰𝘱𝘦𝘳𝘢𝘵𝘪𝘰𝘯𝘴 (𝘶𝘯𝘪𝘰𝘯, 𝘪𝘯𝘵𝘦𝘳𝘴𝘦𝘤𝘵𝘪𝘰𝘯).
# 𝘜𝘴𝘦 𝘥𝘪𝘤𝘵𝘪𝘰𝘯𝘢𝘳𝘪𝘦𝘴 𝘧𝘰𝘳 𝘬𝘦𝘺-𝘷𝘢𝘭𝘶𝘦 𝘱𝘢𝘪𝘳 𝘮𝘢𝘱𝘱𝘪𝘯𝘨𝘴.​⁡