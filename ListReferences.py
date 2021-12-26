t = [0]
s1 = s2 = t

s1 = s1 + [1]  # create a copyied list of s1
s2 += [1]  # not create a copyied list of s2

print(t)
print(s1)
print(s2)

print(t is s1)
print(t is s2)

'''
This puzzle is really tricky because it goes into the details of Python.
In general you can say that x += 1 is the short form of x = x + 1.
However, if you work with non-primitive data types like lists, this is not always true.
In the puzzle we have a variable t which points to a list. 
Then, we create two more variable which point to the same list in memory. 
The interesting thing comes in the third line. Writing s1 = s1 + [1] creates a copy of list s1 and appends [1] to this copied list. 
In the fourth line where we write s2 += [1] the append happens without creating a new list! 
Therefore the value is appended to the list to which t and s2 are still pointing to. So the final output is [0, 1] and s1 = [0, 1] also. 
However t is s2 is True whereas t is s1 is False! Bear in mind: When working with lists += is different from +!
'''
