# Example of comparing different sequence types
l = [1, 2]
m = ['a']

try:
    print(l > m)
except Exception as e:
    print(e)


# Example of comparing same sequence types
capitals = {'uk': 'london', 'france': 'paris',
            'germany': 'berlin', 'china': 'beijing'}
print('\n', list(capitals) > list(capitals.values()))

'''
You can compare sequence objects to other objects with the same sequence type. 
The comparison uses lexicographical ordering to determine the result.

The comparison works as follows: 
you start by comparing the first elements of both sequences. 
If they are equal, the next two elements are compared, and so on, until either sequence is exhausted. 
If two elements to be compared are themselves sequences of the same type, the lexicographical comparison is carried out recursively. 
If all elements of two sequences compare equal, the sequences are considered equal. 
If one sequence is an initial sub-sequence of the other, the shorter sequence is the smaller (lesser) one. 
As soon as two item differ, the comparison stops, and the result can be determined.


In the puzzle, the first element of the first list is 'uk', and the first element of the second list is 'london'. 
Alphabetically, the former comes after the latter, so the first list is considered larger, and the comparison returns True.
'''
