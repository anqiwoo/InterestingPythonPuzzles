import numpy as np

# edge_order = 1
one_dim = np.array([1, 2, 4, 8, 16], dtype=float)
gradient = np.gradient(one_dim, edge_order=1)
print(f'edge_order = 1 -> {gradient}')
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

import numpy as np
# edge_order = 2
one_dim = np.array([1, 2, 4, 8, 16], dtype=float)
gradient = np.gradient(one_dim, edge_order=2)
print(f'edge_order = 2 -> {gradient}')
'''
# * Underlying Gradient Calculation:
# edge_order = 2
gradient[0] = (4*one_dim[0+1] - one_dim[0+2*1] - 3*one_dim[0])/(2*1) 
            = (4*2. - 4. + 3*1.)/2 = 0.5 

# Interior points
gradient[1] = (one_dim[2] - one_dim[0])/2 = (4. - 1.)/2 = 1.5
gradient[2] = (one_dim[3] - one_dim[1])/2 = (8. - 2.)/2 = 3.
gradient[3] = (one_dim[4] - one_dim[2])/2 = (16. - 4.)/2 = 6.

# edge_order = 2
gradient[4] = (3*one_dim[4] + one_dim[4-2*1] - 4*one_dim[4-1])/(2*1) 
            = (3*16. + 4. - 4*8.)/2 
            = 10. 
'''
