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

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2]) 

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4]) 

# NumPy Data Types

"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""

arr = np.array([1, 2, 3, 4])
print(arr.dtype) 

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype) 

arr = np.array([3.2, 2, 3, 4])
print(arr.dtype) 

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype) 

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype) 


# Convert Data Type


arr = np.array([1.1, 2.1, 3.1])
narr = arr.astype('i')
print(narr)
print(narr.dtype) 


arr = np.array([1.1, 2.1, 3.1])
narr = arr.astype(int)
print(narr)
print(narr.dtype) 


arr = np.array([1, 0, 3])
narr = arr.astype(bool)
print(narr)
print(narr.dtype) 


# NumPy Array Copy vs View

arr = np.array([1, 2, 3, 4, 5])
copy = arr.copy()
view = arr.view()
arr[0] = 42
view[0] = 8
copy[0] = 27
print(f"arr:  {arr}")
print(f"copy: {copy}") 
print(f"view: {view}") 

# NumPy Array Shape
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape) 

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape) 

# NumPy Array Reshaping

# Reshape From 1-D to 2-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
narr = arr.reshape(3, 5)
print(narr) 

# Reshape From 1-D to 3-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
narr = arr.reshape(2, 3, 3)
print(narr) 
print(narr.base) 

# Unknown Dimension
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
narr = arr.reshape(2, 3, -1)
print(narr) 


# Flattening

arr = np.array([[1, 2, 3], [4, 5, 6], [7,8,9]])
narr = arr.reshape(-1)
print(narr) 

# Iterating Arrays

arr = np.array([1, 2, 3, 4, 5])
for x in arr:
  print(x) 

# Iterating 2-D Arrays

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in arr:
  print(x) 

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in arr:
  for y in x:
    print(y) 

# Iterating 3-D Arrays
    
arr = np.array([[[1, 2, 3], [4, 5, 6]], [["a", "b", "c"], [10, 11, 12]]])
for x in arr:
  print(x) 

# nditer

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x) 

# ndenumerate

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x) 

# Joining NumPy Arrays

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr) 

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr) 

# Stacking Along Rows

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr) 

# Stacking Along Columns

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))

# Stacking Along Height (depth)


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr) 

# Splitting Arrays
arr = np.array([1, 2, 3, 4, 5, 6])
narr = np.array_split(arr, 3)
print(narr) 

arr = np.array([1, 2, 3, 4, 5, 6])
narr = np.array_split(arr, 4)
print(narr) 

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
narr = np.array_split(arr, 3)
print(narr[0])
print(narr[1])
print(narr[2]) 


arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
narr = np.array_split(arr, 3)
print(narr[0]) 
print(narr[1]) 
print(narr[2]) 

# Searching Arrays

arr = np.array([1, 2, 3, 4, 5, 4, 4, 5, 7, 4])
indexes = np.where(arr == 4)
print(indexes) 


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2])
indexes = np.where(arr % 2 == 0)
print(indexes) 

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
indexes = np.where(arr%2 == 1)
print(indexes) 