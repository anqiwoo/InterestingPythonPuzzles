from collections.abc import Iterable

s = 'abc'
l = [1, 2, 3]
i = 123

judge_list = [s, l, i]

print([isinstance(item, Iterable) for item in judge_list])
