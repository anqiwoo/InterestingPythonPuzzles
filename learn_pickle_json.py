'''
我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
    -   序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
    -   反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

Python提供了pickle模块来实现序列化。
    -   pickle.dump()：序列化
    -   pickle.load()：反序列化
Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，
并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

JSON:
如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，
因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：

    JSON类型	Python类型
    {}	        dict
    []      	list
    "string"	str
    1234.56	    int或float
    true/false	True/False
    null	    None

Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。
    - json.dumps():将Python对象序列化成JSON格式
    - json.loads()/json.load():将JSON格式反序列化为Python对象，前者接受JSON的字符串，后者从file-like Object中读取字符串并反序列化
    
由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。
'''
import pickle
import json

# Pickle
d = {'name': 'Python', 'version': '3.10.1'}

with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)

with open('dump.txt', 'rb') as f:
    nd = pickle.load(f)
print(d)
print('-'*85)
print(nd)

# JSON
d = {'name': 'Python', 'version': '3.10.3'}
print('-'*85)
print(type(json.dumps(d)))
print(json.dumps(d))
print('-'*85)
print(json.loads(json.dumps(d)))
