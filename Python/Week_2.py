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

# Function that accepts unlimited numbers and returns their sum
def sum_numbers(*args):
    """Returns the sum of any number of numeric arguments."""
    return sum(args)

# Examples:
print(sum_numbers(5, 10))             # Output: 15
print(sum_numbers(1, 2, 3, 4, 5))     # Output: 15
print(sum_numbers(100))               # Output: 100
print(sum_numbers())                  # Output: 0

# Function that accepts unlimited keyword arguments and prints them
def print_details(**kwargs):
    """Prints any number of keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Examples:
print_details(name="Alice", age=30)
# Output:
# name: Alice
# age: 30

print_details(role="Admin", active=True, location="Lucknow")
# Output:
# role: Admin
# active: True
# location: Lucknow

# Student profile using **kwargs
def display_student_profile(name, student_id, **kwargs):
    """
    Creates a student profile using required arguments (name, ID) 
    and any number of optional keyword arguments (**kwargs).
    """
    print(f"--- Profile: {name} ---")
    print(f"Student ID: {student_id}")
    
    # Check if any extra keyword arguments were provided
    if kwargs:
        print("Additional Details:")
        for key, value in kwargs.items():
            # Format the key to look cleaner (e.g., 'graduation_year' -> 'Graduation Year')
            clean_key = key.replace('_', ' ').title()
            print(f"  • {clean_key}: {value}")
    print("\n") # Add a blank line for readability

# --- Examples ---

# Example 1: A standard profile with just a major and GPA
display_student_profile(
    name="Emily Chen", 
    student_id="S10293", 
    major="Computer Science", 
    gpa=3.8
)

# Example 2: A highly detailed profile with lists and booleans
display_student_profile(
    name="Marcus Johnson", 
    student_id="S88472", 
    major="History", 
    minor="Political Science",
    graduation_year=2027,
    clubs=["Debate Team", "Model UN"],
    on_campus_housing=True
)

# Example 3: A bare-minimum profile using only required arguments
display_student_profile(
    name="Sarah Connor",
    student_id="S99384"
)

#Calculator using functions
def simple_calculator():
    print("--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid Input")

# Run the calculator
# simple_calculator()