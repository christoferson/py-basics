# Data Science: is a branch of computer science where we study how to store, use and analyze data for deriving information from it.

import numpy as np

print(np.__version__)

# From List
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# From Tuple
arr = np.array((1, 2, 3, 4, 5))
print(arr)

# 0-D Arrays or Scalars
arr = np.array(42)
print(arr)
print(arr.ndim)

# 1-D Arrays
arr = np.array([1, 2, 3, 4, 5])
print(arr) 
print(arr.ndim)

# 2-D Arrays # Matrix or 2nd Order Tensors # numpy.mat
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr) 
print(arr.ndim)

# 3-D arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[8, 7, 6], [5, 4, 3]]])
print(arr) 
print(arr.ndim)


# Higher Dimensional Arrays
arr = np.array([5, 4, 3, 2, 1], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim) 


# Access Array Elements
arr = np.array([1, 2, 3, 4])
print(arr[0]) 


arr = np.array([[10,9,8,7,6], [5,4,3,2,1]])
print('5th element on 2nd row: ', arr[1, 4]) 

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2]) 

# NumPy Array Slicing

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5]) 

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2]) 

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2]) 

# Slicing 2-D Arrays

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4]) 