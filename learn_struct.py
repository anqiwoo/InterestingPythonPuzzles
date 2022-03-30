'''
Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
尽管Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用struct就方便多了。

struct模块定义的数据类型可以参考Python官方文档：
https://docs.python.org/3/library/struct.html#format-characters
'''
import struct

# struct的pack函数把任意数据类型变成bytes
'''
pack的第一个参数是处理指令，'>I'的意思是：
>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
后面的参数个数要和处理指令一致。
'''
print(struct.pack('>I', 1024009))  # b'\x00\x0f\xa0\t'
print(type(struct.pack('>I', 1024009)))  # <class 'bytes'>

# unpack把bytes变成相应的数据类型
'''
根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
'''
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))  # (4042322160, 32896)
print(type(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')))  # <class 'tuple'>
