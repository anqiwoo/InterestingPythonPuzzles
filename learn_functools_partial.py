import functools

int2 = functools.partial(int, base=2)
print(int2('100001'))

kw = {"base": 8}
int8 = functools.partial(int, **kw)
print(int8('100001'))

args = [1, 2, 3]
maxM = functools.partial(max, *args)
print(maxM(0))

'''
在介绍函数参数的时候，我们通过设定参数的默认值，可以降低函数调用的难度。
而偏函数也可以做到这一点。
当函数的参数个数太多，需要简化时，
使用functools.partial可以创建一个新的函数，
这个新函数可以固定住原函数的部分参数(通过类似于默认参数传参，给*args或者**kw的形式)，
从而在调用时更简单。
'''
