import numpy as np

# order = x -> y
one_dim = np.array([(1, 2), (1, 1), (2, 2), (2, 1)],
                   dtype=np.dtype([('x', int), ('y', int)]))
sort_index = np.argsort(one_dim)  # or np.argsort(x, order=('x', 'y'))
print(f'Unsorted array: {one_dim}')
print(f'Sorted array index: {sort_index}')
print(f'Sorted array: {one_dim[sort_index]}')
print('-' * 85)


# order = y -> x
one_dim = np.array([(1, 2), (1, 1), (2, 2), (2, 1)],
                   dtype=np.dtype([('x', int), ('y', int)]))
sort_index = np.argsort(one_dim, order=('y', 'x'))
print(f'Unsorted array: {one_dim}')
print(f'Sorted array index: {sort_index}')
print(f'Sorted array: {one_dim[sort_index]}')
