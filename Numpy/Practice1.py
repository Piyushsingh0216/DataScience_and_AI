import numpy as np

# Creating a 1D array from a list
my_list = [10, 20, 30, 40]
arr_1d = np.array(my_list)

# Creating a 2D array from a list of lists
my_matrix = [[1, 2, 3], [4, 5, 6]]
arr_2d = np.array(my_matrix)

print("1D Array:\n", arr_1d)
print("\n2D Array:\n", arr_2d)

# Create a 1D array with 5 zeros
zeros_1d = np.zeros(5)

# Create a 2D array with 3 rows and 4 columns
zeros_2d = np.zeros((3, 4))

print("Zeros 1D:\n", zeros_1d)
print("\nZeros 2D:\n", zeros_2d)

# Create a 2D array with 2 rows and 2 columns filled with ones
ones_2d = np.ones((2, 2))

# You can also specify the data type (e.g., integers instead of floats)
ones_int = np.ones((2, 3), dtype=int)

print("Ones (default float):\n", ones_2d)
print("\nOnes (integers):\n", ones_int)

# Values from 0 to 9 (stop value is exclusive)
arr1 = np.arange(10)

# Values from 5 to 14
arr2 = np.arange(5, 15)

# Values from 0 to 20, with a step size of 2
arr3 = np.arange(0, 21, 2)

print("0 to 9:\n", arr1)
print("5 to 14:\n", arr2)
print("Step of 2:\n", arr3)

# Generate exactly 5 numbers evenly spaced between 0 and 100
linear_arr = np.linspace(0, 100, 5)

# Generate 10 numbers between 0 and 1
smooth_arr = np.linspace(0, 1, 10)

print("5 points between 0 and 100:\n", linear_arr)
print("\n10 points between 0 and 1:\n", smooth_arr)

# Start with a 1D array of 12 elements
original = np.arange(12)
print("Original 1D:\n", original)

# Reshape into a 2D array: 3 rows, 4 columns
reshaped_3x4 = np.reshape(original, (3, 4))
# Note: You can also use original.reshape(3, 4)

# Reshape into a 3D array: 2 blocks, 2 rows, 3 columns
reshaped_3d = np.reshape(original, (2, 2, 3))

print("\nReshaped 3x4:\n", reshaped_3x4)
print("\nReshaped 3D:\n", reshaped_3d)

# Let's create a 3D array to test these attributes
# 2 blocks, 3 rows, 4 columns (Total = 24 elements)
practice_array = np.zeros((2, 3, 4))

print("Array:\n", practice_array)

print("\n--- Array Attributes ---")
print("Shape (Dimensions):", practice_array.shape) 
print("Size (Total Elements):", practice_array.size)  
print("Ndim (Number of Axes):", practice_array.ndim)

# Mini Exercise:
import numpy as np

# Create a 5×5 NumPy array
array = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

print("Original Array:")
print(array)

# First row
print("\nFirst Row:")
print(array[0])

# Last column
print("\nLast Column:")
print(array[:, -1])

# Diagonal elements
print("\nDiagonal Elements:")
print(np.diag(array))

# Sum of all elements
print("\nSum of All Elements:")
print(np.sum(array))

# Mean of all elements
print("\nMean of All Elements:")
print(np.mean(array))

# Create an array of 20 random integers between 1 and 100
arr = np.random.randint(1, 101, 20)
print(f"Original Array: {arr}")

# Even and Odd numbers using boolean indexing
print(f"Even numbers:   {arr[arr % 2 == 0]}")
print(f"Odd numbers:    {arr[arr % 2 != 0]}")

# Statistics
print(f"Maximum:        {arr.max()}")
print(f"Minimum:        {arr.min()}")
print(f"Average:        {arr.mean()}")

# Sorting and Uniques
print(f"Sorted array:   {np.sort(arr)}")
print(f"Unique values:  {np.unique(arr)}")

# 1. np.where(): Returns elements chosen from x or y depending on condition.
arr = np.array([10, 20, 30, 40])
# Replace values > 25 with 1, else 0
print(np.where(arr > 25, 1, 0)) 
# Output: [0 0 1 1]

# 2. np.unique(): Finds the sorted unique elements of an array.
arr_dup = np.array([1, 1, 2, 3, 3, 4])
print(np.unique(arr_dup)) 
# Output: [1 2 3 4]

# 3. np.sort(): Returns a sorted copy of an array.
arr_unsorted = np.array([5, 2, 9, 1])
print(np.sort(arr_unsorted)) 
# Output: [1 2 5 9]

# 4. np.concatenate(): Joins a sequence of arrays along an existing axis.
a = np.array([1, 2])
b = np.array([3, 4])
print(np.concatenate((a, b))) 
# Output: [1 2 3 4]

# 5. np.vstack(): Stacks arrays in sequence vertically (row wise).
print(np.vstack((a, b)))
# Output: 
# [[1 2]
#  [3 4]]

# 6. np.hstack(): Stacks arrays in sequence horizontally (column wise).
print(np.hstack((a, b)))
# Output: [1 2 3 4]

# 7. np.random.randint(): Returns random integers from `low` (inclusive) to `high` (exclusive).
print(np.random.randint(0, 10, size=5)) 
# Output: e.g., [3 8 2 0 9]

# 8. np.random.choice(): Generates a random sample from a given 1-D array.
choices = ['AI', 'Data Science', 'Web Dev']
print(np.random.choice(choices, size=2, replace=False)) 
# Output: e.g., ['Data Science' 'AI']

# Set a seed for reproducibility (optional)
np.random.seed(42)

# Generate 100 random student marks (between 0 and 100)
marks = np.random.randint(0, 101, size=100)

# Calculate statistics
max_mark = np.max(marks)
min_mark = np.min(marks)
mean_mark = np.mean(marks)
median_mark = np.median(marks)
std_dev = np.std(marks)

# Filter students based on conditions
# marks > 75 creates a boolean mask, which we use to index the original array
above_75 = marks[marks > 75]
below_35 = marks[marks < 35]

# Print Results
print("--- Student Marks Summary ---")
print(f"Maximum Mark:        {max_mark}")
print(f"Minimum Mark:        {min_mark}")
print(f"Mean Mark:           {mean_mark:.2f}")
print(f"Median Mark:         {median_mark}")
print(f"Standard Deviation:  {std_dev:.2f}")

print("\n--- Performance Thresholds ---")
print(f"Number of students scoring above 75: {len(above_75)}")
print(f"Marks > 75: {above_75}")

print(f"\nNumber of students scoring below 35: {len(below_35)}")
print(f"Marks < 35: {below_35}")

# Generate marks for 200 students (random integers between 0 and 100)
marks = np.random.randint(0, 101, size=200)

# Calculate statistics using your practice list
highest_marks = np.max(marks)
lowest_marks = np.min(marks)
average_marks = np.mean(marks)
std_dev = np.std(marks)

# Calculate counts using boolean indexing
above_80 = np.sum(marks > 80)
below_40 = np.sum(marks < 40)

# Display results
print(f"Highest marks: {highest_marks}")
print(f"Lowest marks: {lowest_marks}")
print(f"Average marks: {average_marks:.2f}")
print(f"Standard deviation: {std_dev:.2f}")
print(f"Number of students above 80: {above_80}")
print(f"Number of students below 40: {below_40}")