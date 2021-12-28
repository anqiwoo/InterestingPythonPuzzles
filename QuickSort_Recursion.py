def sort_recursion(s):
    if len(s) < 2:
        return s
    else:
        return sort_recursion([x for x in s[1:] if x <= s[0]]) \
            + [s[0]]
        + sort_recursion([x for x in s[1:] if x > s[0]])
        # can only concatenate list (not "int") to list


print(sort_recursion([6, 3, 7, 2, 4, 1, 9]))

'''
This is one of the basic algorithms in computer science: Quicksort.
The algorithm sorts a sequence of elements.

Quicksort is an elegant way of solving the sorting problem via recursion.
It breaks the hard problem of sorting a large sequence into two
easier problems of sorting two smaller sequences. This works as follows:

We select a so-called pivot element which is the first element
in the sequence.

Then, we determine all elements in the large sequence
that are smaller than the pivot elements and put them into a new
sequence, say S1. Similarly, we put all elements that are greater or equal
than the pivot element into a new sequence, say S2.

Next, we apply the Quicksort algorithm recursively to both sequences.
Assume that both smaller sequences are already sorted. We can now return
the result as the sorted sequence S1 plus the pivot element plus the result
of the sorted sequence S2. Note that as all elements in S1 are smaller and
all elements in S2 are larger than the pivot, the combination is also sorted.

The recursion stops if only one element remains in the sequence.
'''
