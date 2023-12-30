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

# 1-D Arrays
arr = np.array([1, 2, 3, 4, 5])
print(arr) 

#2-D Arrays # Matrix or 2nd Order Tensors # numpy.mat
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr) 
