import functools
from time import perf_counter
import time

'''
要求：请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
'''


def exec_timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        t1 = perf_counter()
        func(*args, **kw)
        t2 = perf_counter()
        print(f"Execution time: {t2-t1:.12f} seconds")
    return wrapper


@exec_timer
def test_func():
    l = [i*i for i in range(100000)]


@exec_timer
def fast(x, y):
    time.sleep(0.0012)
    return x + y


test_func()
a = fast(1, 2)
