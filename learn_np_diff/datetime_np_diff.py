import numpy as np

'''
Generally, the type of the np.diff()’s output is the same as the type of the difference between any two elements of input array. 
A notable exception is datetime64, which results in a timedelta64 output array.
'''
# dates = np.arange('1100-10-01', '1100-10-05', dtype=np.datetime64)
# one_diff = np.diff(dates, n=1)
dates = np.arange('2066-10-13', '2066-10-16', dtype=np.datetime64)
one_diff = np.diff(dates, n=1)
print(f'Original dates: {dates}')
print('-'*85)
print(f'Original date\'s type: {dates.dtype}')
print('-'*85)
print(f'One difference: {one_diff}')
print('-'*85)
print(f'One difference\'s type: {one_diff.dtype}')
