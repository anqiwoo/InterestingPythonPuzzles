'''
Python的错误其实也是class，所有的错误类型都继承自BaseException。
常见的错误类型和继承关系看这里：
https://docs.python.org/3/library/exceptions.html#exception-hierarchy

当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块（在用except语句抓不同错误类型的时候，要注意上面提到的错误类型继承关系，比如UnicodeError是ValueError的子类，如果你先写了一个抓ValueError的except语句，这语句也会抓UnicodeError，所以如果你在后面再写抓UnicodeError的except语句，就相当于没有写哈）。
执行完except后，如果没有出错且有一个else语句，则执行else语句块。
执行完else语句块后，如果有finally语句块，则执行finally语句块。
至此，执行完毕。
'''

try:
    print('trying...')
    a = 10 / 0
except BaseException as e:
    print('Catch all errors...')
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print(f'result: {a}')
finally:
    print('finally!')
