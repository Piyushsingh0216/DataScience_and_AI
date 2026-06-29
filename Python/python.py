print("Hello, World!")

# Store name, age and branch in variables
name = "Piyush Singh"
age = 20
branch = "Computer Science Engineering"

# Swap two variables using a temporary variable
a = 5
b = 10
print(f"Before swapping: a = {a}, b = {b}")
c = a
a = b
b = c
print(f"After swapping: a = {a}, b = {b}")

# Swap two variables without using a temporary variable
x = 15
y = 25
print(f"Before swapping: x = {x}, y = {y}")
x = x + y
y = x - y
x = x - y
print(f"After swapping: x = {x}, y = {y}")

# Take user input and print a personalized greeting
user_name = input("Enter your name: ")
print(f"Hello, {user_name}! Welcome to the program.")

# Convert celcius to fahrenheit
celcius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celcius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")

# Convert kilometers to miles
kilometers = float(input("Enter distance in kilometers: "))
miles = kilometers * 0.621371
print(f"Distance in miles: {miles}")

# Calculate the area of a rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"Area of the rectangle: {area}")

# Calculate simple interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time (in years): "))
simple_interest = (principal * rate * time) / 100
print(f"Simple Interest: {simple_interest}")

# Display the data type of the variables using the type() function
print(f"Data type of name: {type(name)}")
print(f"Data type of age: {type(age)}")
print(f"Data type of branch: {type(branch)}")
print(f"Data type of celcius: {type(celcius)}")
print(f"Data type of fahrenheit: {type(fahrenheit)}")
print(f"Data type of kilometers: {type(kilometers)}")
print(f"Data type of miles: {type(miles)}")
print(f"Data type of length: {type(length)}")
print(f"Data type of width: {type(width)}")
print(f"Data type of area: {type(area)}")
print(f"Data type of principal: {type(principal)}")
print(f"Data type of rate: {type(rate)}")
print(f"Data type of time: {type(time)}")
print(f"Data type of simple_interest: {type(simple_interest)}")

# Check if a number is prime
Num = int(input("Enter a number: "))
if Num <= 1:
    print(f"{Num} is not a prime number.")
for i in range(2, int(Num**0.5) + 1):
    if Num % i == 0:
        print(f"{Num} is not a prime number.")
        break
else:
    print(f"{Num} is a prime number.")

# Print Prime Numbers (1-100)
for num in range(2, 101):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num)

# Fibonacci Series
a = int(input("Enter the number of terms in the Fibonacci series: "))
b = 0
c = 1
for _ in range(a):
    print(b, end=" ")
    b, c = c, b + c

# Armstrong Number
num = int(input("Enter a number: "))
sum_of_cubes = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_cubes += digit ** 3
    temp //= 10
if num == sum_of_cubes:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

# Palindrome number
num = int(input("Enter a number: "))
temp = num
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
if num == reverse:
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")

# Factorial using loop
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num}: {factorial}")

# factorial using recursion
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

print(f"Factorial of {num} (recursive): {factorial_recursive(num)}")

# Multiplication Table
num = int(input("Enter a number to display its multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Reverse a number
num = int(input("Enter a number to reverse: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print(f"Reversed number: {reverse}")

# Counts digits in a Number
num = int(input("Enter a number to count its digits: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print(f"Number of digits: {count}")