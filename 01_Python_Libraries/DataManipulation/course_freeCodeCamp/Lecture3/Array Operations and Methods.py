# reshape(), sum(), max(), min(), sqrt(), sin(), exp(), etc.

# Check dimensions with .ndim, data type with .dtype, and shape with .shape.
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.reshape(3, 2))  # Reshape array
print(np.sum(arr))        # Sum of all elements
print(arr.ndim)           # Number of dimensions
