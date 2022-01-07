import numpy as np

# graphics data
a = [[1, 1],
     [1, 0]]
a = np.array(a)

# stretch vectors
b = [[2, 0],
     [0, 2]]
b = np.array(b)

c = a @ b
d = np.matmul(a, b)
print(c == d)
