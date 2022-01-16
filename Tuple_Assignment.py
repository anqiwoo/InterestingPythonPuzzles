t = 1, 1, 1 == (1, 1, 1)
print(t)  # (1,1,False)

'''
At first view the code might look a bit confusing. 
However if you add a pair of parenthesis it looks much simpler. 
Look at the right hand part of the assignment like this (1, 1, 1 == (1, 1, 1)). 
In words: the code assigns a tuple to the variable my_tuple. 
The tuple contains three values, which are two times one and the result of the comparison 1 == (1, 1, 1). 
Obviously this is not correct and evaluates to False. 
Therefore the code assigns (1, 1, False) to the variable my_tuple and prints it in the next line.
'''
