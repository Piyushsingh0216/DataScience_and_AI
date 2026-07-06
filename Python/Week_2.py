# Square every number using map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# Keep only even numbers using filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Find the sum of a list using reduce()
from functools import reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)

# Convert a list of names to uppercase using map()
names = ["Alice", "Bob", "Charlie"]
uppercase_names = list(map(lambda name: name.upper(), names))
print(uppercase_names)

# Create squares from 1–20 using list comprehension
squares = [x**2 for x in range(1, 21)]

print(squares)

# Create a list of even numbers from 1–100
evens = list(range(2, 101, 2))

print(evens)

# Create a dictionary mapping numbers to their squares
square_dict = {x: x**2 for x in range(1, 11)}

print(square_dict)

# Remove duplicate words from a list using a set
words = ['apple', 'banana', 'orange', 'apple', 'grape', 'banana']

# Convert the list to a set to remove duplicates, then back to a list
unique_words = list(set(words))

print(unique_words)

# Convert a list of names to lowercase using list comprehension
names = ['Alice', 'BOB', 'Charlie', 'dAvId']

lowercase_names = [name.lower() for name in names]

print(lowercase_names)