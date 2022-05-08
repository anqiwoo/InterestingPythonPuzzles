import numpy as np

x = np.arange(12).reshape(3, 4)
y = np.zeros(12).reshape(3, 4)
# x:
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# just to focus on the multiple conditions first!
conditions1 = (x > 3) & (x < 8)
conditions2 = (x < 3) | (x > 8)

# conditions are bool ndarray
print(f'condition 1:\n {conditions1}\n')
print(f'condition 2:\n {conditions2}\n')

# use the np.where() function
print(f'np.where(conditions1, x, y):\n {np.where(conditions1, x, y)}\n')
print(f'np.where(conditions2, x, y):\n {np.where(conditions2, x, y)}')
