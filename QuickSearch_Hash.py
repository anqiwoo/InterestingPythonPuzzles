def quick_search_hash(string, pattern):
    n, m = len(string), len(pattern)
    hpattern = hash(pattern)
    for i in range(n-m+1):
        hs = hash(string[i:i+m])
        if hs == hpattern:
            if string[i:i+m] == pattern:
                return i
    return -1


s1 = 'Happy Coding Everyday!'
print(quick_search_hash(s1, 'Coding'))

'''
There’s a large body of literature concerning the efficient search of strings.

In Python, you can search a string s1 for a substring s2 simply by using the expression "s2 in s1". However, this does not tell you anything about how this actually works.

How does the algorithm work?

The naive string search algorithm simply iterates over all indices of the string s1. It then tries to match all characters of string s2. If it fails, it proceeds with the next index. However, this algorithm has O(len(s1) * len(s2)) worst-case time complexity.

The Rabin-Karb algorithm is more efficient. The improvement comes from using slicing to access the substring starting in index i and comparing the hash values instead of the substrings themselves. This is more efficient because calculating a hash value is much faster than checking equality of two strings. However, two different strings may result in the same hash value. Therefore, the Rabin-Karb algorithm needs to make sure to exclude this case.
'''
