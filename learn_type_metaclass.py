# -- Import class definition from other module --
from hello import Hello

h = Hello()
h.hello()
print(type(Hello))  # <class 'type'>
print(type(h))  # <class 'hello.Hello'>
print(type(h.hello))  # <class 'method'>
print('-'*85)


# -- Use type() function to create a class definition like the above --
'''
要创建一个class对象，type()函数依次传入3个参数：
    - class的名称；
    - 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    - class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
'''


def fn(self, name='world'):
    print(f'hello {name}!')


Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello()
print(type(Hello))  # <class 'type'>
print(type(h))  # <class '__main__.Hello'>
print(type(h.hello))  # <class 'method'>
print('-'*85)
'''
通过type()函数创建的类和直接写class是完全一样的，
因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，
也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，
要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。
'''

# -- metaclass example --
'''
除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
我们先定义一个metaclass，然后在一个class的定义过程中通过metaclass修改该class的创建行为，最后影响到该class创建出来的实例。
所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。

下面的例子是我们自定义的MyList增加一个add方法。
'''


class ListMetaclass(type):
    '''
    按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass。
    metaclass是类的模板，所以必须从`type`类型派生。
    '''
    def __new__(cls, name, bases, attrs):
        '''
        其实这个__new__方法的逻辑跟前面讲的type()函数创建一个class的逻辑很像！
            - cls跟metaclass的关系，就像好比一般class里面的self跟class的关系
            - name就是呼唤metaclass的class的名字，好比下面的MyList
            - bases就是呼唤metaclass的class的父类（们）集合，好比下面的(<class 'list'>,)
            - attrs就是呼唤metaclass的class的方法字典
        可以看到，
        上述metaclass的__new__方法创建class逻辑中后三个参数的功能，
        跟type()函数创建一个新class时三个参数的功能是一样的！（新类叫什么、新类的父类集合是什么、新类的方法字典是什么）
        '''
        print(cls, name, bases, attrs, sep='\n\n')
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    '''
    有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass。

    当我们传入关键字参数metaclass时，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
    在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
    __new__()方法接收到的参数依次是：
        - 当前准备创建的类的对象； # <class '__main__.ListMetaclass'>
        - 类的名字； # MyList
        - 类继承的父类集合； # (<class 'list'>,)
        - 类的方法集合。 # {'__module__': '__main__', '__qualname__': 'MyList', '__doc__': '······'}
    '''
    pass


# Test if we add a 'add' method to MyList class successfully.
print('-'*85)
L = MyList()
L.add(100)
print(L)  # [100]
