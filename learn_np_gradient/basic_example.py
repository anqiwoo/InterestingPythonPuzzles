'''
# Syntax
numpy.gradient(f[, *varargs[, axis=None[, edge_order=1]]])
'''

import numpy as np

one_dim = np.array([1, 2, 4, 8, 16], dtype=float)
gradient = np.gradient(one_dim)
print(gradient)
