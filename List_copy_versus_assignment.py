l = [1]

# copy method (shallow copy -- only copy the object references to the list elements and not the object itself)
nl = l.copy()
nl.append(2)
print(nl)
print(l)
print('\n')

# assignment method (pass the object itself)
nl = l
nl.append(2)
print(nl)
print(l)


'''
Definition and Usage: 
The list.copy() method copies all list elements into a new list. 
The new list is the return value of the method. 
It’s a shallow copy—you copy only the object references to the list elements and not the objects themselves.
'''
