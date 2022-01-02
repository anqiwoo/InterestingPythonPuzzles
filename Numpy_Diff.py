import numpy as np
from numpy.lib.function_base import diff

a = np.array([[1, 2, 3], [2, 2, 2], [8, 8, 8]])

# Along the Column Axis, Calculate the difference Twice
diffs_axis1 = np.diff(a, n=2, axis=1)

# Along the Row Axis, Calculate the difference Twice
diffs_axis0 = np.diff(a, n=2, axis=0)

print(a, '\n')
print(diffs_axis1, '\n')
print(diffs_axis0)
