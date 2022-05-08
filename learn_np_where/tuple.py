import numpy as np

x = np.arange(12).reshape(3, 4)
# x:
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# use the np.where() function to get the indices
a_tuple = np.where(x)
print(type(a_tuple))
print('-'*85)
print("Indices of elements that meets the condition for each dimension:")
print(np.where(x))

# use the zip() and list() function to get the coordinates
print('-'*85)
print("Coordinates (row, column) that meets the condition for each dimension:")
print(list(zip(*np.where(x))))
