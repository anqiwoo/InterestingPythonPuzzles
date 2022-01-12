def factorial(n):
    assert n >= 0, 'Please enter a natural number!'
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(0))
print(factorial(4))
print(factorial(-1))
