s = ['cats', 'elephants', 'mammal', 'something']

min_unique_letters_word = min(s, key=lambda x: len(set(x)))
print(min_unique_letters_word)

'''
The code of this puzzle returns the string from a list of a string which is the shortest in terms of unique letters.
To implement this we leverage the possibility of the function min to pass it a key-function. The key-function is used to compute a key-value for each element. The function min uses these key-values to select the minimum element from the list.
To get the number of unique letters of each string we create a new set with each string. Since each element only occurs once in a set, the length of the set of a given string returns the number of unique letters in the string. And this is just what our key-function does. Therefore the output is mammal since it has only three unique letters.
'''
