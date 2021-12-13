def levenshtein(a, b):
    if not a:
        return len(b)
    if not b:
        return len(a)
    return min(
        levenshtein(a[1:], b[1:]) + (a[0] != b[0]),
        levenshtein(a[1:], b) + 1,
        levenshtein(a, b[1:]) + 1
    )


a = 'sdfHello'
b = 'aHello'
print(levenshtein(a, b))

'''
The Levenshtein distance is a metric to calculate the distance between two strings. It helps you to quantify how “similar” two strings are. The Levenshtein distance is also called “edit distance” which describes precisely what it measures: the number of character edits (insertions, removals, or substitutions) that are needed to transform one string into another. The intuition is the following: the smaller the Levenshtein distance, the more similar the strings.

Before we dive into the code, let’s quickly explore an important Python trick we heavily exploit in the one-liner. In Python, every object has a truth value – while you are either good or bad in the world of Harry Potter, you are either True or False in the world of Python! Most objects are in fact True (normal people are usually good). Intuitively, you know the few objects that are False, don’t you?

0 is False
” is False
[] is False
{} is False

As a rule of thumb, Python objects are considered False if they are empty or zero. Equipped with this information, you can now easily understand the first part of the Levenshtein function:

We create a lambda function that returns the number of edits required to transform a string a into a string b. There are two trivial cases: Suppose string a is empty. In this case, the minimal edit distance is len(b) insertions of the characters in string b. We cannot do better. Similarly, if string b is empty, the minimal edit distance is len(a). Thus, we can directly return the correct edit distance if either of the strings is empty.

Let’s say both strings are non-empty (otherwise the solution is trivial as shown previously). Now, we can simplify the problem in three ways.

First, we ignore the leading characters of both strings a and b and calculate the edit distance from a[1:] to b[1:] in a recursive manner. If the leading characters a[0] and b[0] are different, we have to fix it by replacing a[0] by b[0]. Hence, we increment the edit distance by one if they are different.

Second, we remove the first character a[0]. Now, we check the minimal edit distance recursively for this smaller problem. As we have removed a character, we increment the result by one.

Third, we (conceptually) insert the character b[0] to the beginning of the word a. Now, we can reduce this problem to the smaller problem that arises if we remove the first character of b. As we have performed one edit operation (inserting), we increment the result by one.

Finally, we simply take the minimum edit distance of all three results (replace the first character, remove the first character, insert the first character).
'''
