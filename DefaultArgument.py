def f(a, l=[]):
    l.append(a)
    return l


f(1)
f(2)
print(f(3))

'''
This puzzle may be confusing at first. 
The Python interpreter evaluates default arguments only once, 
not each time the function is called. 
This is not a problem if the argument is immutable:
the integer value 1 always remains the integer value 1.
But if the argument is mutable--like a list, dictionary, or class instances--this becomes clear. 
The mutable object just collects all the values in the subsequent function calls.
'''
