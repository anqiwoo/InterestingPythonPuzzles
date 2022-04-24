'''
# Syntax
numpy.meshgrid(*xi[, copy=True[, sparse=False[, indexing='xy']]])
'''


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 5)
y = np.linspace(5, 10, 5)
xx, yy = np.meshgrid(x, y)
print('Coordinate Vector - x:')
print(x)
print('\nCoordinate Vector - y:')
print(y)
print('\nCoordinate Matrix - xx:')
print(xx)
print('\nCoordinate Matrix - yy:')
print(yy)

# Visualization

# coordinate vectors
plt.plot(x, np.zeros_like(x), color='g', marker='o', linestyle='none')
plt.plot(np.zeros_like(y), y, color='b', marker='*', linestyle='none')

# coordinate pairs
plt.scatter(xx, yy, color='r')
plt.show()
