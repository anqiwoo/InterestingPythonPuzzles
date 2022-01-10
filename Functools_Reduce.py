import functools

data = [2, 3, 4]
multiples = functools.reduce(lambda x, y: x*y, data, 100)
print(multiples)

'''
The reduce function has become more and more famous since 2009 due to the popularity
of Google's map-reduce framework for parallel distributed execution on commodity machines.
The idea is that given a sequence of values, we iteratively combine any two values to a single value
using the reduce function until only one value remains - the final result of the function.
The reduce function can be parallelized easily: suppose we have a list of one thousand values and two processors.
Now, we can reduce 500 values to a single value on both processors in parallel. As a final
step, we reduce the two reduced values from both processors to a single result value.
This would take approximately half the time compared to execution on a single processor.
Note that the reduce function is not a build-in function anymore since the release of Python 3 but is contained
in the packet functools.
'''
