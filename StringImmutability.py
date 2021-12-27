import time as t


def f1(n):
    return ''.join([str(x) for x in range(n)])


def f2(n):
    s = ''
    for x in range(n):
        # string is immutable.
        # So this line of code is creating a string in every loop.
        s += str(x)
    return s


n = 10 ** 6
t1 = t.time()
f1(n)
t2 = t.time()
f2(n)
t3 = t.time()
print(t2 - t1)
print(t3 - t2)
print(t3 - t2 > t2 - t1)

'''
One of the most basic operations any Python programmer performs is building strings. Often you create large strings programmatically.

The second function creates the string via string concatenation. The problem with this approach is that strings are immutable. You can not change a string but only create a new one. Therefore, you create one million strings that are getting larger and larger.

The first function is not only more concise, it is also faster. Here, you create a list via the technique of list comprehension (the for loop within the list brackets). This creates only a single list object that is modified subsequently. Finally, you join the elements in the list to a large string. In summary, this function creates only a single list and a single string.
'''
