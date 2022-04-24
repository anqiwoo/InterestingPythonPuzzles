import numpy as np

# Cartesian Indexing (Default Indexing Method)
print('Cartesian Indexing (Default Indexing Method)\n')
x = np.linspace(0, 3, 3)
y = np.linspace(2, 4, 2)
xx, yy = np.meshgrid(x, y, indexing='xy')
# Same as:
# xx, yy = np.meshgrid(x, y)
print('Coordinate Vector - x:')
print(x)
print('Coordinate Vector - y:')
print(y)
print('Coordinate Matrix - xx:')
print(xx)
print('Coordinate Matrix - yy:')
print(yy)


# Matrix Indexing
print('-'*85)
print('Matrix Indexing\n')
x = np.linspace(0, 3, 3)
y = np.linspace(2, 4, 2)
xx, yy = np.meshgrid(x, y, indexing='ij')
print('Coordinate Vector - x:')
print(x)
print('Coordinate Vector - y:')
print(y)
print('Coordinate Matrix - xx:')
print(xx)
print('Coordinate Matrix - yy:')
print(yy)
