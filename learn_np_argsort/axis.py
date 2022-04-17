# import numpy as np

# # Here is the 2d array example with axis=0:
# two_dim = np.array([[1, 2, 3], [3, 2, 1]])
# sort_index = np.argsort(two_dim, axis=0)

# print(f"Unsorted array: {two_dim}")
# print(f"Sorted array index: {sort_index}")
# print(f"Sorted array: {np.take_along_axis(two_dim, sort_index, axis=0)}")


# # Here is the 2d array example with axis=1:
# import numpy as np

# two_dim = np.array([[1, 2, 3], [3, 2, 1]])
# sort_index = np.argsort(two_dim, axis=1)

# print(f"Unsorted array: {two_dim}")
# print(f"Sorted array index: {sort_index}")
# print(f"Sorted array: {np.take_along_axis(two_dim, sort_index, axis=1)}")

# Here is the 2d array example with axis=None:
import numpy as np

two_dim = np.array([[1, 2, 3], [3, 2, 1]])
sort_index = np.argsort(two_dim, axis=None)

print(f"Unsorted array: {two_dim}")
print(f"Sorted array index: {sort_index}")
print(f"Sorted array: {np.take_along_axis(two_dim, sort_index, axis=None)}")
