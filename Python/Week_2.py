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

# Create:
#Student class
#Car class
#BankAccount class
#Employee class
class Student:
    # Constructor
    def __init__(self, name, student_id, major):
        # Attributes
        self.name = name
        self.student_id = student_id
        self.major = major
        self.grades = []

    # Method 1
    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"Grade {grade} added for {self.name}.")

    # Method 2
    def get_average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
        
    # Method 3
    def display_info(self):
        print(f"Student: {self.name} (ID: {self.student_id}) - Major: {self.major}")

class Car:
    # Constructor
    def __init__(self, make, model, year):
        # Attributes
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    # Method 1
    def accelerate(self, increment):
        self.speed += increment
        print(f"The {self.year} {self.make} {self.model} accelerates to {self.speed} mph.")

    # Method 2
    def brake(self, decrement):
        # Prevents speed from dropping below 0
        self.speed = max(0, self.speed - decrement)
        print(f"The {self.make} {self.model} slows down to {self.speed} mph.")

class BankAccount:
    # Constructor
    def __init__(self, account_holder, account_number, initial_balance=0.0):
        # Attributes
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance

    # Method 1
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    # Method 2
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

class Employee:
    # Constructor
    def __init__(self, name, employee_id, position, salary):
        # Attributes
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.salary = salary

    # Method 1
    def give_raise(self, percent_increase):
        raise_amount = self.salary * (percent_increase / 100)
        self.salary += raise_amount
        print(f"{self.name} received a {percent_increase}% raise. New salary: ${self.salary:.2f}")

    # Method 2
    def promote(self, new_position):
        self.position = new_position
        print(f"{self.name} has been promoted to {self.position}.")

#1. Library Class
class Library:
    def __init__(self):
        # Initialize an empty list to store books
        self.books = []

    def add_book(self, title):
        self.books.append(title)
        print(f"Added: '{title}'")

    def display_books(self):
        if not self.books:
            print("The library is currently empty.")
        else:
            print("Library Books:")
            for book in self.books:
                print(f"- {book}")

#2. Rectangle Class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def display_info(self):
        print(f"Rectangle[Length: {self.length}, Width: {self.width}]")
        print(f"Area: {self.get_area()}, Perimeter: {self.get_perimeter()}")

#3. Employee Class (with Class Variables)
class Employee:
    # Class variables: Shared by all instances of Employee
    company_name = "Global Tech Corp"
    total_employees = 0

    def __init__(self, name, salary):
        # Instance variables: Unique to each employee
        self.name = name
        self.salary = salary
        
        # Increment the class variable when a new employee is created
        Employee.total_employees += 1

    def display_details(self):
        print(f"Employee: {self.name}, Salary: ${self.salary}")
        print(f"Company: {Employee.company_name}")

#4. Student Class (Encapsulation with Getters/Setters)
class Student:
    def __init__(self, name, grade):
        # Private attributes
        self.__name = name
        self.__grade = grade

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            print("Invalid name provided.")

    # Getter for grade
    def get_grade(self):
        return self.__grade

    # Setter for grade (includes validation logic)
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Error: Grade must be between 0 and 100.")

