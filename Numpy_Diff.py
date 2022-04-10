import numpy as np

a = np.array([[1, 2, 3], [2, 2, 2], [8, 8, 8]])

# Along the Column Axis, Calculate the difference Twice
diffs_axis1 = np.diff(a, n=2, axis=1)

# Along the Row Axis, Calculate the difference Twice
diffs_axis0 = np.diff(a, n=2, axis=0)

print(a, '\n')
print(diffs_axis1, '\n')
print(diffs_axis0)

'''
The numpy diff function calculates the difference between two subsequent values of a NumPy array.
Hence, an array with n elements results in a diff array with (n-1) elements.

When defining the parameter n, the diff function is applied n times to the output of the previous diff function execution.
Thus, the first row undergoes the following transformations:

[0 1 1] *diff*--> [1 0] *diff*--> [-1]

'''
