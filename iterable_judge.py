from collections.abc import Iterable

s = 'abc'
l = [1, 2, 3]
i = 123
g = (i for i in l)

judge_list = [s, l, i, g]

print([isinstance(item, Iterable) for item in judge_list])
