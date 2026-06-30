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