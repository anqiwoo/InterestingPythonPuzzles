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

'''
Numpy is a popular Python library for data science focusing on arrays, vectors, and matrices.

This puzzle shows an important application domain of matrix multiplication: Computer Graphics.

We create two matrices a and b. The first matrix a is the data matrix (e.g. consisting of two column vectors (1,1) and (1,0)). The second matrix b is the transformation matrix that transforms the input data. In our setting, the transformation matrix simply stretches the column vectors.

More precisely, the two column vectors (1,1) and (1,0) are stretched by factor 2 to (2,2) and (2,0). The resulting matrix is therefore [[2,2],[2,0]]. We access the first row and second column.

We use matrix multiplication to apply this transformation. Numpy allows two ways for matrix multiplication: the matmul function and the @ operator.

Comparing two equal-sized numpy arrays results in a new array with boolean values. As both matrices c and d contain the same data, the result is a matrix with only True values.
'''
