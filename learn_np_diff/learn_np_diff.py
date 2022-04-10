# Syntax
# numpy.diff(a[, n=1[, axis=-1[, prepend=<no value>[, append=<no value>]]])

# import numpy as np
# “0” difference and 1st difference example
'''
The first difference is given by out[i] = a[i+1] - a[i] along the given axis, 
higher differences are calculated by using diff recursively.
'''
# one_dim = np.array([1, 2, 4, 7, 12])
# it_self = np.diff(one_dim, n=0)
# one_diff = np.diff(one_dim, n=1)
# print(f'One dimensional array: {one_dim}')
# print(f'"0" difference: {it_self}')
# print(f'1st difference: {one_diff}')

# import numpy as np
# 2nd difference and 3rd difference example
# '''
# The first difference is given by out[i] = a[i+1] - a[i] along the given axis,
# higher differences are calculated by using diff recursively.
# '''
# one_dim = np.array([1, 2, 4, 9, 15, 20])
# one_diff = np.diff(one_dim, n=1)
# two_diff = np.diff(one_dim, n=2)
# three_diff = np.diff(one_dim, n=3)
# print(f'One dimensional array: {one_dim}')
# print(f'1st difference: {one_diff}')
# print(f'2nd difference: {two_diff}')
# print(f'3rd difference: {three_diff}')

import numpy as np
# 2nd difference in two-dimensional array example - axis=0
'''
The first difference is given by out[i] = a[i+1] - a[i] along the given axis,
higher differences are calculated by using diff recursively.
'''
two_dim = np.array([[1, 2, 4, 9, 15, 20],
                   [4, 2, 1, 0, 24, 8],
                   [3, 7, 5, 13, 17, 0]])
one_diff = np.diff(two_dim, n=1, axis=0)
two_diff = np.diff(two_dim, n=2, axis=0)
print(f'Two dimensional array: {two_dim}')
print('-'*85)
print(f'1st difference: {one_diff}')
print('-'*85)
print(f'2nd difference: {two_diff}')

# import numpy as np
# # 2nd difference in two-dimensional array example - axis=1
# '''
# The first difference is given by out[i] = a[i+1] - a[i] along the given axis,
# higher differences are calculated by using diff recursively.
# '''
# two_dim = np.array([[1, 2, 4, 9, 15, 20],
#                    [4, 2, 1, 0, 24, 8],
#                    [3, 7, 5, 13, 17, 0]])
# one_diff = np.diff(two_dim, n=1, axis=1)
# two_diff = np.diff(two_dim, n=2, axis=1)
# print(f'Two dimensional array: {two_dim}')
# print('-'*85)
# print(f'1st difference: {one_diff}')
# print('-'*85)
# print(f'2nd difference: {two_diff}')
