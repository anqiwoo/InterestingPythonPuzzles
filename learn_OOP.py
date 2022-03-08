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
'''


class Animal:
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()


a = Animal()
b = Dog()
c = Cat()

run_twice(a)
run_twice(b)
run_twice(c)
