#!usr/bin/env python3
# -*- coding: utf-8 -*-

'''
面向对象的设计思想是抽象出Class，根据Class创建Instance。
一个Class既包含数据，又包含操作数据的方法。
类是创建实例的模板，实例是一个个具体的对象，各个实例拥有的数据相互独立，互不影响。

数据封装、继承和多态是面向对象的三大特点。
1. 数据封装：类将自身的数据和逻辑封装在类的定义里，使得外部调用很容易（不用知道内部实现的细节）
2. 继承：子类继承父类的所有数据和功能，且前者的数据和功能可以覆盖后者。(继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。)
3. 多态：同一种方法在不同对象上实现的功能多样化；调用方只管调用，不管细节；对拓展开放（允许增加子类），对修改封闭（在增加子类的时候，不必修改依赖父类的方法/函数）。

面向对象高级编程:
1. __slots__:用tuple定义允许绑定的属性名称，用以限制绑定实例的属性。
2. Python内置的@property装饰器：负责把一个方法变成属性调用；@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查(setter),这样，程序运行时就减少了出错的可能性。
3. 多重继承:存在一个主要的类层次，然后需要另外功能的子类，就再继承别的父类，这种设计通常称之为MixIn。MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。通过多重继承，一个子类就可以同时获得多个父类的所有功能。我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。只允许单一继承的语言（如Java）不能使用MixIn的设计。
4. 定制类: Python的class允许定义许多定制方法，可以让我们非常方便地生成特定的类。__slots__ ; __str__和__repr__; __iter__和__next__; __getitem__;__getattr__; __call__; 更多参见Python官方文档。
5. 枚举类：Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。like
固定下来一个常量表！！！
3. 元类:动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。我们可通过元类metaclass修改类定义。metaclass是Python中非常具有魔术性的对象，它可以改变类创建时的行为。
'''

from subprocess import call
from types import MethodType


class Animal:
    count = 0
    __slots__ = ('name', 'age')

    def __init__(self, name: str):
        self.name = name
        Animal.count += 1

    def run(self):
        print('Animal is running...')

    def __call__(self):
        print(f'My name is {self.name}.')

    def __len__(self):
        return len(self.name)

    # 两者的区别是__str__()返回用户看到的字符串，
    # 而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
    def __str__(self):
        return f'Animal Object (name: {self.name})'
    # 通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：
    __repr__ = __str__


class Dog(Animal):
    # ----- @property: 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值;只定义getter方法，不定义setter方法就是一个只读属性;要特别注意：属性的方法名不要和实例变量重名，不然就会自己return自己，因栈溢出而报错哈。
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if not isinstance(value, str):
            raise ValueError('color must be a string!')
        self._color = value

    @property
    def color_length(self):
        return len(self._color)

    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


class FlyableMixIn():
    def fly(self):
        print('Flying...')

# 对于MixIn的父类，我们习惯上会在类名末尾加上MixIn，就像下面的FlyableMixIn。


class Bat(Animal, FlyableMixIn):
    pass


def run_twice(animal):
    animal.run()
    animal.run()


def set_age(self, age):
    self.age = age


a = Animal('Aliceee')
print(a.__slots__)  # class with __slots__ has no attribute '__dict__'
print('-'*85)
print(type(Animal))
print(type(a))
print(a.count)
print(a)  # __str__
a()  # __call__
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
print(callable(a))
print(callable('a'))
b = Dog('Dylaaaan')
print(b.count)
print(b)
b()
c = Cat('Cathyyyyyyy')
print(c.count)
bat = Bat('Batty')
bat.fly()
print(bat.count)

# ---------- Test @property in Dog class
b.color = 'red'
print(b.color)
print(b.color_length)


# ---------- Set Instance method and class method
b.set_age = MethodType(set_age, b)
b.set_age(2)
print(b.age)
# d = Dog('Bobbbb')
# d.set_age(22) # 会报错，因为给一个实例绑定的方法，对另一个实例是不起作用的
# 为了给所有实例都绑定方法，可以给class绑定方法（Python是动态语言）
Animal.set_age = set_age
d = Dog('Bobbbb')
d.set_age(22)
print(d.age)


# ---------- Test __slots__
# a.color = 'red' # 会报错，因为Animal类定义里使用了__slots__限制此类实例可绑定的属性
# 使用__slots__要注意，
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
d.color = 'black'
print(d.color)

run_twice(a)
run_twice(b)
run_twice(c)

print(len(a))
print(len(b))
print(len(c))

'''
通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，
拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。
'''
# ---------- manipulate the attributes
# check is an attribute exists.
print(hasattr(a, 'name'))
print(hasattr(a, 'age'))
# set an attribute
setattr(a, 'age', 1)
print(hasattr(a, 'age'))
# get an attribute
# 404 is the default value in case the attribute 'age' dose not exists.
print(getattr(a, 'age', 404))
print(a.age)
print(getattr(a, 'ag', 404))
# get a method
print(getattr(a, 'run', 404))
# assign the method to a variable
fn = getattr(a, 'run', 404)
fn()

'''
假设我们希望从文件流fp中读取图像，
我们首先要判断该fp对象是否存在read方法，
如果存在，则该对象是一个流，如果不存在，则无法读取。
hasattr()就派上了用场。

请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，
不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，
但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。
'''


def readImage(fp):
    if hasattr(fp, 'read'):
        return fp.read()
