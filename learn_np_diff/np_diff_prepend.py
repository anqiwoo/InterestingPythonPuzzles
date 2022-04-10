# import numpy as np

# # prepend with array - axis=0
# two_dim = np.array([[1, 2, 4, 9, 15, 20],
#                    [4, 2, 1, 0, 24, 8],
#                    [3, 7, 5, 13, 17, 0]])

# one_diff = np.diff(two_dim, n=1, axis=0, prepend=[[1] * two_dim.shape[1]])
# two_diff = np.diff(two_dim, n=2, axis=0, prepend=[[1] * two_dim.shape[1]])
# # one_diff = np.diff(two_dim, n=1, axis=0, prepend=[[1, 1, 1, 1, 1, 1]])
# # two_diff = np.diff(two_dim, n=2, axis=0, prepend=[[1, 1, 1, 1, 1, 1]])
# print(f'Two dimensional array: {two_dim}')
# print('-'*85)
# print(f'1st difference: {one_diff}')
# print('-'*85)
# print(f'2nd difference: {two_diff}')


# prepend with scalar values - axis=0
import numpy as np
two_dim = np.array([[1, 2, 4, 9, 15, 20],
                   [4, 2, 1, 0, 24, 8],
                   [3, 7, 5, 13, 17, 0]])

one_diff = np.diff(two_dim, n=1, axis=0, prepend=1)
two_diff = np.diff(two_dim, n=2, axis=0, prepend=1)
# one_diff = np.diff(two_dim, n=1, axis=0, prepend=[[1, 1, 1, 1, 1, 1]])
# two_diff = np.diff(two_dim, n=2, axis=0, prepend=[[1, 1, 1, 1, 1, 1]])
print(f'Two dimensional array: {two_dim}')
print('-'*85)
print(f'1st difference: {one_diff}')
print('-'*85)
print(f'2nd difference: {two_diff}')
