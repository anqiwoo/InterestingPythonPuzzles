# Create a str to int converter without str()/int().

from functools import reduce

DIGITS = {f'{i}': i for i in range(10)}


def char2int(ch):
    return DIGITS[ch]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2int, s))


# Test
s = '123456'
print(int(s) == str2int(s))
