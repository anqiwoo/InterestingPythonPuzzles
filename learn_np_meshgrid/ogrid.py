import numpy as np

# numpy.meshgrid with sparse=True + indexing='ij'
print('numpy.meshgrid with sparse=True + indexing=\'ij\':')
x = np.arange(0, 3)
y = np.arange(2, 4)
xx, yy = np.meshgrid(x, y, sparse=True, indexing='ij')

print('Coordinate Vector - x:')
print(x)
print('Coordinate Vector - y:')
print(y)
print('Coordinate Matrix - xx:')
print(xx)
print('Coordinate Matrix - yy:')
print(yy)

# numpy.ogrid
print('-'*85)
print('numpy.ogrid:')
xx, yy = np.ogrid[0:3, 2:4]

print('Coordinate Vector - x:')
print(x)
print('Coordinate Vector - y:')
print(y)
print('Coordinate Matrix - xx:')
print(xx)
print('Coordinate Matrix - yy:')
print(yy)