from collections.abc import Iterable

s = 'abc'
l = [1, 2, 3]
i = 123
g = (i for i in l)

judge_list = [s, l, i, g]

print([isinstance(item, Iterable) for item in judge_list])
'''
 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
'''
