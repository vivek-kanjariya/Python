# ⁡⁢⁣⁣​‌‌‍𝗦𝘁𝗿𝗶𝗻𝗴 𝗠𝗲𝘁𝗵𝗼𝗱𝘀, 𝗙𝗼𝗿𝗺𝗮𝘁𝘁𝗶𝗻𝗴, 𝗮𝗻𝗱 𝗠𝗮𝗻𝗶𝗽𝘂𝗹𝗮𝘁𝗶𝗼𝗻 𝗶𝗻 𝗣𝘆𝘁𝗵𝗼𝗻​⁡

# ⁡⁣⁣⁢​‌‍‌# 𝗦𝘁𝗿𝗶𝗻𝗴 𝗙𝗼𝗿𝗺𝗮𝘁𝘁𝗶𝗻𝗴​⁡

# a) Using f-strings
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alice and I am 25 years old.

# b) Using str.format()
name = "Bob"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is Bob and I am 30 years old.

# Positional or Keyword Arguments
print("{0} is from {1}".format("Alice", "Wonderland"))  # Positional
print("{name} is {age} years old.".format(name="Charlie", age=20))  # Keyword

# c) Using % Operator
name = "Dave"
age = 40
print("My name is %s and I am %d years old." % (name, age))
# Output: My name is Dave and I am 40 years old.


# ⁡⁣⁣⁢​‌‍‌𝗦𝘁𝗿𝗶𝗻𝗴 𝗦𝗹𝗶𝗰𝗶𝗻𝗴 𝗮𝗻𝗱 𝗜𝗻𝗱𝗲𝘅𝗶𝗻𝗴​⁡

# a) Accessing Characters
s = "Python"
print(s[0])  # Output: P
print(s[-1])  # Output: n

# b) Slicing Strings
# Use the syntax string[start:end:step] to slice strings.

# start: Starting index (inclusive).
# end: Ending index (exclusive).
# step: Step size (optional).
s = "Python"

# Basic slicing
print(s[0:3])  # Output: Pyt
print(s[:4])   # Output: Pyth (start is 0 by default)
print(s[2:])   # Output: thon (goes to the end)

# Using step
print(s[::2])  # Output: Pto (every second character)
print(s[::-1])  # Output: nohtyP (reversed string)

# Negative indices
print(s[-4:-1])  # Output: tho (from index -4 to -2)



# ⁡⁣⁣⁢​‌‍‌# 𝗦𝗽𝗹𝗶𝘁𝘁𝗶𝗻𝗴 𝗮𝗻𝗱 𝗝𝗼𝗶𝗻𝗶𝗻𝗴​⁡
s = "apple,banana,cherry"
# Splitting
fruits = s.split(",")
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Joining
new_s = "-".join(fruits)
print(new_s)  # Output: apple-banana-cherry



# ​‌‍‌⁡⁣⁣⁢‍𝗘𝘅𝗮𝗺𝗽𝗹𝗲𝘀⁡​

sentence = "the quick brown fox jumps over the lazy dog the fox"
words = sentence.split()
word_count = {word: words.count(word) for word in set(words)}
print(word_count)
# Output: {'dog': 1, 'the': 3, 'fox': 2, 'lazy': 1, 'jumps': 1, 'brown': 1, 'quick': 1, 'over': 1}

s = "hello world"
unique_chars = set(s.replace(" ", ""))  # Remove spaces and convert to set
print(unique_chars)  # Output: {'o', 'h', 'd', 'w', 'r', 'e', 'l'}


number = 1234567890
print(f"{number:,}")  # Output: 1,234,567,890

