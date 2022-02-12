def odd_iter():
    n = 3
    while True:
        yield n
        n += 2


def not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = odd_iter()  # initial series after 2.
    while True:
        n = next(it)  # first number in the present series.
        yield n
        it = filter(not_divisible(n), it)  # filter n's multiples


# print prime numbers that are under some number
some_number = 85
for n in primes():
    if n < some_number:
        print(n)
    else:
        break  # since primes() is an infinite series, we need a break here.
