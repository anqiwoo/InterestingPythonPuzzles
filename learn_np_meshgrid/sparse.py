import numpy as np

# sparse = False (Default)
print('sparse=False:')
x = np.linspace(0, 3, 3)
y = np.linspace(2, 4, 2)
xx, yy = np.meshgrid(x, y, sparse=False)
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

# sparse = True
print('-'*85)
print('sparse=True:')
x = np.linspace(0, 3, 3)
y = np.linspace(2, 4, 2)
xx, yy = np.meshgrid(x, y, sparse=True)
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
