'''
Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。
doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。
只有测试异常的时候，可以用...表示中间一大段烦人的输出。

当模块正常导入时，doctest不会被执行。只有在命令行直接运行时，才执行doctest。
所以，不必担心doctest会在非测试环境下执行。

doctest非常有用，不但可以用来测试，还可以直接作为示例代码。通过某些文档生成工具，就可以自动把包含doctest的注释提取出来。用户看文档的时候，同时也看到了doctest。
'''


import doctest


def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1

    >>> fact(10)
    3628800

    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError
    '''
    if n < 0:
        raise ValueError
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)


if __name__ == '__main__':
    doctest.testmod()
    # fact(-1)
