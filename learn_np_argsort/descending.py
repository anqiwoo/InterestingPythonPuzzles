import numpy as np

one_dim = np.array([1, 2, 3, 4, 5])
# use the [::-1] to reverse the ascending order to descending order.
sort_index = np.argsort(one_dim)[::-1]
print(f'Unsorted array: {one_dim}')
print(f'Sorted array index: {sort_index}')
print(f'Sorted array: {one_dim[sort_index]}')
