'''
Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。

itertools模块提供的全部是处理迭代功能的函数，
它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。
'''

import itertools

# * 首先，我们看看itertools提供的几个“无限”迭代器
'''
因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。
'''
# natural = itertools.count(1)
# i = 0
# while i < 100000:
#     print(next(natural))
#     i += 1

# nn = itertools.takewhile(lambda x: x <= 10, natural)
# print(type(natural))  # <class 'itertools.count'>
# print(type(nn))  # <class 'itertools.takewhile'>
# print(list(nn))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
cycle()会把传入的一个序列无限重复下去;
注意字符串也是序列的一种
'''
# cyc = itertools.cycle('Hi')
# for c in cyc:
#     print(c)

'''
repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
'''
# rp = itertools.repeat('Hi', 8)
# for r in rp:
#     print(r)

# * itertools提供的几个迭代器操作函数更加有用

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('Hi', 'Happy'):
    print(c)
'''
H
i
H
a
p
p
y
'''

# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('HHHHHHHiiiHHHAAPPPPYYYYY'):
    print(key, list(group))
    # print(type(key))  # <class 'str'>
    # print(type(group))  # <class 'itertools._grouper'>
'''
H ['H', 'H', 'H', 'H', 'H', 'H', 'H']
i ['i', 'i', 'i']
H ['H', 'H', 'H']
A ['A', 'A']
P ['P', 'P', 'P', 'P']
Y ['Y', 'Y', 'Y', 'Y', 'Y']
'''

'''
实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，
这两个元素就被认为是在一组的，而函数返回值作为组的key。
如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key
'''
print('-'*85)
for key, group in itertools.groupby('AaaAbBbb', lambda c: c.upper()):
    print(key, list(group))
'''
A ['A', 'a', 'a', 'A']
B ['b', 'B', 'b', 'b']
'''


# Application: Calculate pi


def pi(N):
    '''
    Application: Calculate pi
    '''
    # create an odd series
    odd = itertools.count(1, 2)
    # take the first N items
    odd = itertools.takewhile(lambda x: (x+1)/2 <= N, odd)
    # use the formula and sum them up!
    pi_sum = 0
    for i, o in enumerate(odd):
        pi_sum += (-1) ** i * 4/o
    return pi_sum


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
