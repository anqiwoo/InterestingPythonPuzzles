l = [1, 2, 3]
l.extend([])
print(len(l))  # 3
l.append([[]])
print(len(l))  # 4

'''
In order to solve this puzzle correctly, you have to know how the list methods extend and append work.
1. extend() takes an iterable like a list or tuple and appends each single element from the iterable to the end of the list
2. append() takes one single element and appends it as it is to the end of the list.

In the puzzle we call extend([]) with an empty list as a parameter. 
Since the iterable doesn't contain elements, nothing is appended to the list.

When we call append([[]]) we pass a list with one element (the empty list) to the method. 
However appends simply appends the given parameter as it is to the end of the list.
Therefore, in the end the list looks like this [1, 2, 3, [[]]] and has a length of 4.
'''
