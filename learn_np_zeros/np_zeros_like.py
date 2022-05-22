import numpy as np

# np.zeros way:
shape = (2, 3)
first_output = np.zeros(shape)
print('first output:\n', first_output)
print('-' * 85)

# np.zeros_like way:
# given a 2d array like thing
array_like = [[1, 2, 3], [4, 5, 6]]
second_output = np.zeros_like(array_like)
print('second output:\n', second_output)
