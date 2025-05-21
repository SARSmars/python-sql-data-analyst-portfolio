import numpy as np
# 5. Array Indexing and Slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Slice elements from index 1 to 4
print(arr[1:5])

# 2D array slicing
arr2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2d[1, 1:4])  # Elements 7, 8, 9 from the second row
print(arr2d[0:2, 1:4])  # Elements from the first two rows and columns 1 to 3
# First part define the row and second part define the column
# 3D array slicing
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3d[1, 0, 1])  # Element 6 from the second array
print(arr3d[0:2, 0, 1])  # Elements from the first two arrays and first row
print(arr3d[0:2, 0:2, 1])  # Elements from the first two arrays and second row
# 4D array slicing