'''
Python的错误其实也是class，所有的错误类型都继承自BaseException。
常见的错误类型和继承关系看这里：
https://docs.python.org/3/library/exceptions.html#exception-hierarchy

当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，
即except语句块（在用except语句抓不同错误类型的时候，要注意上面提到的错误类型继承关系，
比如UnicodeError是ValueError的子类，如果你先写了一个抓ValueError的except语句，
这语句也会抓UnicodeError，所以如果你在后面再写抓UnicodeError的except语句，就相当于没有写哈）。
执行完except后，如果没有出错且有一个else语句，则执行else语句块。
执行完else语句块后，如果有finally语句块，则执行finally语句块。
至此，执行完毕。
'''
import logging

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

'''
如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。
出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。
'''


'''
如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。

Python内置的logging模块可以非常容易地记录错误信息，同样是出错，但程序打印完错误信息后会继续执行，并正常退出。
通过配置，logging还可以把错误记录到日志文件里，方便事后排查。
'''


def main():
    try:
        b = 10 / 0
    except Exception as e:
        logging.exception(e)


main()
print('End!')
