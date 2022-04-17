'''
# syntax
numpy.argsort(a[, axis=-1[, kind=None[, order=None]]])
'''

import numpy as np

one_dim = np.array([1, 5, 4, 0, 3])
sort_index = np.argsort(one_dim)  # axis defaults to -1 (the last axis)
print(f'Unsorted array: {one_dim}')
print(f'Sorted array index: {sort_index}')
print(f'Sorted array: {one_dim[sort_index]}')
