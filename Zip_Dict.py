d = {0: 'Peter', 1: 'Amy', 2: 'Bob'}

print(list(zip(d))[1])

'''
Using Python's built-in function zip() on a single iterable creates a list of tuples with one single element in each. 

When you use a dictionary in any function, the default value of the dictionary is its dict_keys iterable, 
in this case dict_keys([0, 1, 2]). 
Therefore the second entry in the result of zip(d) is the tuple (1,).
'''
