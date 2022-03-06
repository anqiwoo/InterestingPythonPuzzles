import functools
from datetime import datetime


def log(func):
    @functools.wraps(func)  # 把原始函数的__name__等属性复制到wrapper()函数中
    # wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。
    def wrapper(*args, **kw):
        print(f"call {func.__name__}:")
        return func(*args, **kw)
    return wrapper


@log  # 借助Python的@语法，把decorator置于函数的定义处
def now():
    print(datetime.now())


now()  # 把@log放到now()函数的定义处，相当于执行了语句： now = log(now)
print(now.__name__)

'''
在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
本质上，decorator就是一个接受一个函数，然后返回一个函数的高阶函数。

在面向对象（OOP）的设计模式中，decorator被称为装饰模式。
OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，
直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。

decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。
'''
