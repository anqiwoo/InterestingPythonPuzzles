d = {
    0: 'a',
    1 > 2: 'b',
    False: 'c',
    bool([]): 'd'
}  # If you pass duplicate keys to a dictionary in Python, the value of the last entry stays only.

print(d[0])
print(d)

'''
All the keys of the dictionary evaluate to False/0, hence the dictionary contains only one single entry.
The entry is the last one from the given entries because the entries are added starting from the upper most entry in the code. All these entries update the False/0 entry so that finally the value of the last entry stays.
'''
