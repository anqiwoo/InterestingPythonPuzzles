# import numpy as np

# # axis = None (Default)
# two_dim = np.array([[1, 2, 4, 8, 16],
#                     [2, 5, 8, 10, 20]], dtype=float)
# gradient = np.gradient(two_dim, axis=None)
# # Same as:
# # gradient = np.gradient(two_dim)
# print(f'axis = None (Default): \n\n{gradient}')
# print('\n', type(gradient))


# import numpy as np

# # axis = int
# two_dim = np.array([[1, 2, 4, 8, 16],
#                     [2, 5, 8, 10, 20]], dtype=float)
# row_gradient = np.gradient(two_dim, axis=0)
# col_gradient = np.gradient(two_dim, axis=1)

# # Same as:
# # row_gradient = np.gradient(two_dim, axis=-2)
# # col_gradient = np.gradient(two_dim, axis=-1)

# print(f'axis = 0 or -2: \n\n{row_gradient}')
# print('-'*85)
# print(f'axis = 1 or -1: \n\n{col_gradient}')

import numpy as np

# axis = a tuple of ints
two_dim = np.array([[1, 2, 4, 8, 16],
                    [2, 5, 8, 10, 20]], dtype=float)
gradient = np.gradient(two_dim, axis=[0, 1])

print(f'axis = [0,1]: \n\n{gradient}')
