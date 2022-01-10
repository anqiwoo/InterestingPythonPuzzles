import numpy as np

# Save $15,000 each month
x = 15000
goal = 130000
months = np.arange(0, goal, x)

# How long to save >$130,000?
print(len(months))

'''
Numpy is a popular Python library for data science focusing on linear algebra.

This puzzle is about the NumPy arange function. 
The arange function is everywhere in data science.

You might know the Python built-in range(x,y,z) function that creates a sequence of linear progressing values. 
The sequence starts from x, increases the values linearly by z, and ends if the value becomes larger than y.

The arange(x,y,z) function is similar but creates a NumPy array and works with float numbers as well.

Note that a common mistake in this puzzle is to not account for the first value of the array: 0.
'''
