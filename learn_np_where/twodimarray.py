import numpy as np

x = np.arange(1, 13).reshape(3, 4)
y = np.zeros(12).reshape(3, 4)
# x:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
# y:
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]


new_array = np.where(x > 6, x, y)
print(new_array)
# same as:
# new_array = np.where(x > 6, x, 0)
