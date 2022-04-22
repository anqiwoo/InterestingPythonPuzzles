import numpy as np

# * Do not handle np.nan problem:
print('Do not handle np.nan problem:')
one_dim = np.array([2, 3, 1, np.nan, 5, 4, np.nan])
# kth=0 -> partition based on 2(zero index).
partitioned = np.argpartition(one_dim, 0)
print(f'Unpartitioned array: {one_dim}')
print(f'Partitioned array index: {partitioned}')
print(f'Partitioned array: {one_dim[partitioned]}')

# * Handle np.nan problem:
# np.nan is taken as an infinite large number in Python.
print('-'*85)
print('Handle np.nan problem:')
one_dim = np.array([2, 3, 1, np.nan, 5, 4, np.nan])
# If we want to get the N biggest element and index in an array:
print('(If we want to get the N biggest element and index in an array)')
N = 2
# get the number of np.nan
c = np.isnan(one_dim).sum()
partitioned_idx = np.argpartition(one_dim, -N-c)[-N-c:-c]
partitioned_val = one_dim[partitioned_idx]
print(f'Unpartitioned array: {one_dim}')
print(f'Partitioned array index: {partitioned_idx}')
print(f'Partitioned array: {partitioned_val}')
