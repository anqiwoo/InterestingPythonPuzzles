def initialize():
    global count, string
    count = 5
    string = 'g'


# Continue
initialize()
while count > 3:
    count -= 1
    if count == 3:
        continue
    string += 'o'
else:  # the else branch is executed if the loop terminates because the loop condition is not met anymore.
    string += 'd'
print('Continue: ', string)

# Break
initialize()
while count > 3:
    count -= 1
    if count == 3:
        break
    string += 'o'
else:
    string += 'd'
print('Break: ', string)

'''
The interesting twist in the puzzle is that there is an "else" branch of the while loop! 
This is a nice little Python trick that is not very well known: 
the else branch is executed if the loop terminates because the loop condition is not met anymore. 
The alternative would be a "forced" termination of the loop from within the body using the "break" statement.

In other words: 
The else branch executes only if the loop runs over all elements in the loop sequence without leaving it early (via the "break" statement).

This is the case for our first example, where there is no break statement. 
In the last loop body execution, the index variable is decremented and takes value "3". 
Thus, the interpreter executes the continue statement (just before appending the character 'o' once more) and goes to the loop condition to check whether it should execute it once more. This is not the case, so the program leaves the loop naturally and goes into the "else" branch where the character 'd' is appended to the string. The final result is, therefore:
'g' + 'o' + 'd' = 'god'.
'''
