import numpy as np

# order: x -> y
print('order: x -> y')
one_dim = np.array([(1, 3), (2, 1), (1, 1), (2, 3)],
                   dtype=[('x', float), ('y', float)])
partitioned = np.argpartition(one_dim, kth=0, order=['x', 'y'])
# In this case, same as:
# partitioned = np.argpartition(one_dim, kth=0)
print(f'Unpartitioned array: {one_dim}')
print(f'Partitioned array index: {partitioned}')
print(f'Partitioned array: {one_dim[partitioned]}')


# order: y -> x
print('-'*85)
print('order: y -> x')
one_dim = np.array([(1, 3), (2, 1), (1, 1), (2, 3)],
                   dtype=[('x', float), ('y', float)])
partitioned = np.argpartition(one_dim, kth=0, order=['y', 'x'])
print(f'Unpartitioned array: {one_dim}')
print(f'Partitioned array index: {partitioned}')
print(f'Partitioned array: {one_dim[partitioned]}')
