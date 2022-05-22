import numpy as np

# dtype unspecified:
shape = (3, 2)
output = np.zeros(shape, dtype=[('x', np.float64), ('y', np.int8)])
print('output:\n', output)
print('\noutput dtype:\n', output.dtype)
