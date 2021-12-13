# Binary Search Algorithm
def binary_search_algorithm(l, value):
    '''
    return the index of value in a given iterable
    '''
    l = sorted(l)
    lo, hi = 0, len(l)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if l[mid] < value:
            lo = mid + 1
        elif l[mid] > value:
            hi = mid - 1
        else:
            return mid


l = [1, 2, 3, 4, 5, 6]
value = 5
print(binary_search_algorithm(l, value))
