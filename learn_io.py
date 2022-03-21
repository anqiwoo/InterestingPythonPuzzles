'''
IO指Input/Output。程序运行时数据在内存中驻留，由CPU执行计算，当涉及到数据交换时（如内存与磁盘、网络间），需要IO接口。

IO编程中，Stream（流）是一个很重要的概念，可以把流想象成一个水管，数据就是水管里的水，但是只能单向流动。
Input Stream就是数据从外面（磁盘、网络）流进内存，Output Stream就是数据从内存流到外面去。

由于CPU和内存的速度远远高于外设的速度，所以，在IO编程中，就存在速度严重不匹配的问题。有两种解决办法
    - 同步IO：CPU等着
    - 异步IO：CPU抓紧时间干别的事情
同步和异步的区别就在于是否等待IO执行的结果。
很明显，使用异步IO来编写程序性能会远远高于同步IO，但是异步IO的缺点是编程模型复杂。

操作IO的能力都是由操作系统提供的，每一种编程语言都会把操作系统提供的低级C接口封装起来方便使用，Python也不例外。

在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。
'''

from io import StringIO, BytesIO

# 读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。
'''
【like程序与磁盘之间有个操作系统做中介】
在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，
所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。
'''

'''
如果文件很小，read()一次性读取最方便；
如果不能确定文件大小，反复调用read(size)比较保险；
如果是配置文件，调用readlines()最方便
'''

'''
遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，
因为在文本文件中可能夹杂了一些非法编码的字符。
遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。
最简单的方式是直接忽略，在open函数参数表里设置 errors='ignore'
'''
with open('./learn_os_walk/1.txt') as f:
    data = f.read()


# File like object
'''
像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
除了file外，还可以是内存的字节流，网络流，自定义流等等。
file-like Object不要求从特定类继承，只要写个read()方法就行。

StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
StringIO顾名思义就是在内存中读写str的IO接口。BytesIO就是在内存中读写bytes的IO接口。

StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
'''
f = StringIO()
f.write('hello')
f.write('\n\n')
f.write('world')
print(f.getvalue())

f = StringIO('hello\n\nworld\n')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
g = f.getvalue()

g = BytesIO(g)
print(g.read().decode('utf-8'))
