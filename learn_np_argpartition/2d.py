import numpy as np

# axis = 0 [partial sort along the axis = 0. In this case, row-like.]
print('axis = 0')
two_dim = np.array([[1, 4, 3], [3, 2, 1]])
partitioned = np.argpartition(two_dim, kth=0, axis=0)
print(f'Unpartitioned array: {two_dim}')
print(f'Partitioned array index: {partitioned}')
print(f'Partitioned array: {np.take_along_axis(two_dim, partitioned, axis=0)}')

# axis = 1 [partial sort along the axis = 1. In this case, column-like.]
print('-'*85)
print('axis = 1')
two_dim = np.array([[1, 4, 3], [3, 2, 1]])
partitioned = np.argpartition(two_dim, kth=0, axis=1)
print(f'Unpartitioned array: {two_dim}')
print(f'Partitioned array index: {partitioned}')
print(f'Partitioned array: {np.take_along_axis(two_dim, partitioned, axis=1)}')
