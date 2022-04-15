'''
# Syntax
numpy.gradient(f[, *varargs[, axis=None[, edge_order=1]]])
'''

import numpy as np

one_dim = np.array([1, 2, 4, 8, 16], dtype=float)
gradient = np.gradient(one_dim)
print(gradient)
'''
# * Underlying Gradient Calculation:
# Default edge_order = 1
gradient[0] = (one_dim[1] - one_dim[0])/1 = (2. - 1.)/1 = 1. 

# Interior points
gradient[1] = (one_dim[2] - one_dim[0])/2 = (4. - 1.)/2 = 1.5
gradient[2] = (one_dim[3] - one_dim[1])/2 = (8. - 2.)/2 = 3.
gradient[3] = (one_dim[4] - one_dim[2])/2 = (16. - 4.)/2 = 6.

# Default edge_order = 1
gradient[4] = (one_dim[4] - one_dim[3])/1 = (16. - 8.)/1 = 8. 
'''
