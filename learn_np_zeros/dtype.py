import numpy as np

# dtype unspecified:
shape = (2, 3)
first_output = np.zeros(shape)
print('previous first output:\n', first_output)
print('-' * 85)

# dtype = np.int8:
shape = (2, 3)
first_output = np.zeros(shape, dtype=np.int8)
print('present first output:\n', first_output)
