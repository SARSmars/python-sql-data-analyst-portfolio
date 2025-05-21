# Python can read and write files using the built-in open() function.
# For NumPy arrays, use np.loadtxt(), np.savetxt(), np.save(), and np.load() for efficient file operations.

# Writing to a text file
import numpy as np
# Create a NumPy array and save it to a text file
arr = np.array([1, 2, 3, 4, 5])
np.savetxt('array.txt', arr)

# Reading from a text file
arr_loaded = np.loadtxt('array.txt')
print(arr_loaded)
