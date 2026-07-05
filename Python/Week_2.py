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
