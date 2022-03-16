# If you concatenate two lists, you are actually creating a new list.
l = []
id1 = id(l)
l = l + [1]
id2 = id(l)
print(id1 == id2)  # False.

# If you append new elements to the original list, the list variable is still pointed to the original object.
l = []
id3 = id(l)
l.append(1)
id4 = id(l)
print(id3 == id4)  # True.

# The fact above can matter in case like:


def test_f(l):
    '''
    Can you tell the l is changed after the execution of this function or not?
        - l unchanged after execution.
        - Since only a new local variable is created in the function when concatenating two lists, the original list passed in stay unchanged.
    '''
    l = l + [1]


l = []
id5 = id(l)
test_f(l)
id6 = id(l)
print(id5 == id6)  # True.
