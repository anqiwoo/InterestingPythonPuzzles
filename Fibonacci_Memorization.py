import time as t


def fib(n):
    if n in [0, 1]:
        return 1
    return fib(n-1) + fib(n-2)


memorized = {}


def fibm(n):
    if n in [0, 1]:
        return 1
    elif n in memorized:
        return memorized[n]
    else:
        fib_value = fibm(n-1) + fibm(n-2)
        memorized[n] = fib_value
        return fib_value


n = 100
t1 = t.time()
y1 = fib(n)
t2 = t.time()
y2 = fibm(n)
t3 = t.time()

print(y1 == y2)  # True

# True But if you set n too small, the difference is not significant.
print(t3 - t2 < t2 - t1)

'''
The Fibonacci series calculates the sum of the last two series values and appends the result to the series.
The x'th element of the series can be calculated recursively as shown in fib(x). However, the recursive computation will perform redundant work. Both instances fib(x-1) and fib(x-2) will calculate the value for, say x-3.

The idea of this puzzle is to show how this redundant work can be reduced with memoization. Memoization is a popular technique in computer science to exchange space against time efficiency.
It is simply a dictionary that saves the result of the i'th Fibonacci number after calculating it. Later instances can now reuse it instead of calculating it from scratch.

For example, fib_m(x-1) fills the dictionary with all the Fibonacci series elements, including x-2. The second call fib_m(x-2) now already finds the result in the dictionary. Instead of calculating it, it looks it up, which is much faster.
Therefore, the result is equal for both fib() and fib_m() but fib_m() is much faster for large inputs.
'''
