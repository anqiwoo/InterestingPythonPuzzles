# # Syntax
# numpy.where(condition, [x, y, ]/)

import numpy as np

# basic example 1
x = np.arange(1, 4)
y = np.zeros(3)
print(np.where(x < 3, x, y))

# basic example 2
x = np.arange(1, 4)
print(np.where(x < 3))
