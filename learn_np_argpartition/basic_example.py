'''
# Syntax
numpy.argpartition(a, kth[, axis=- 1[, kind='introselect'[, order=None]]])
'''

# Basic Example
import numpy as np
one_dim = np.array([3, 2, 1, 5, 4])
# kth=0 -> partition based on 2(zero index).
partitioned = np.argpartition(one_dim, 0)
print(f'Unpartitioned array: {one_dimg}')
print(f'Partitioned array index: {partitioned}')
print(f'Partitioned array: {one_dim[partitioned]}')
