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
1. __slots__:用tuple定义允许绑定的属性名称，用以限制绑定实例的属性
1. 多重继承:
2. 定制类:
3. 元类:
'''


class Animal:
    count = 0
    __slots__ = ('name', 'age')

    def __init__(self, name: str):
        self.name = name
        Animal.count += 1

    def run(self):
        print('Animal is running...')

    def __len__(self):
        return len(self.name)


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()


a = Animal('Aliceee')
print(a.count)
b = Dog('Dylaaaan')
print(b.count)
c = Cat('Cathyyyyyyy')
print(c.count)

# a.color = 'red'

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
# manipulate the attributes
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
