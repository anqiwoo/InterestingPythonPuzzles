t = [0, 2, 2, 1]
x = t.pop() < t.pop() < t.pop() < t.pop()
print(x)
print(t)
t.append(x)
print('\n', len(t))  # 2
'''
The method pop() of the list class removes and returns the last element of a list.
However, in the puzzle the last call of pop() will not be executed since the comparison's result is already clear after the third call. Due to Short Circuiting the evaluation stops and the result is returned.
Therefore, there is still one element in list t before we append x to it which leads to the output 2.
'''
