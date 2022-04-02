'''
并不是只有open()函数返回的fp对象才能使用with语句。
实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。


'''
from contextlib import contextmanager, closing
from urllib.request import urlopen

# 实现上下文管理是通过__enter__和__exit__这两个方法实现的。例如，下面的class实现了这两个方法


class Query():
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin...')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End!')

    def query(self):
        print(f"Query info about {self.name}...")


with Query('Vicky') as q:
    q.query()
'''
Begin...
Query info about Vicky...
End!
'''


# @contextmanager
'''
编写__enter__和__exit__仍然很繁琐，
因此Python的标准库contextlib提供了更简单的写法，
@contextmanager让我们通过编写generator来简化上下文管理。
上面的代码可以改写如下:
'''


class QQuery():
    def __init__(self, name):
        self.name = name

    def query(self):
        print(f"Query info about {self.name}...")


@contextmanager
def create_query(name):
    '''
    @contextmanager这个decorator接受一个generator，
    用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了
    '''
    print('Begin...')
    yield QQuery(name)
    print('End!')


with create_query('Lisa') as q:
    q.query()
'''
Begin...
Query info about Lisa...
End!
'''


# 很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。
@contextmanager
def tag(name):
    print(f'<{name}>')
    yield
    print(f'</{name}>')


with tag('h1'):
    print('hello')
    print('kitty')
'''
<h1>
hello
kitty
</h1>
'''
'''
代码的执行顺序是：

with语句首先执行yield之前的语句，因此打印出<h1>；
yield调用会执行with语句内部的所有语句，因此打印出hello和world；
最后执行yield之后的语句，打印出</h1>。
因此，@contextmanager让我们通过编写generator来简化上下文管理。
'''


# 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。
with closing(urlopen('https://www.anqiwu.one')) as page:
    print(type(page))  # <class 'http.client.HTTPResponse'>
    # for line in page:
    #    print(line)

# closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单


@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
