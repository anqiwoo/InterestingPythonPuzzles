'''
# Conclusions
    - Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。
    - json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。
      但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，
      既做到了接口简单易用，又做到了充分的扩展性和灵活性。


# pickle:
我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
    -   序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
    -   反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

Python提供了pickle模块来实现序列化。
    -   pickle.dumps() / pickle.dump()：序列化（从内存到磁盘/网络）。前者接受一个Python对象，后者接受一个待dump的Python对象和dump到的一个file like object（接受write）。
    -   pickle.loads() / pickle.load()：反序列化（从磁盘/网络到内存）。前者接受一个bytes对象，后者接受一个支持read的file like object。
Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

# JSON:
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
    - json.dumps() / json.dump():将Python对象序列化成JSON格式（内存到磁盘/网络）,前者接受一个待dump的Python对象，后者接受一个待dump的Python对象和一个支持write的file like object。
    - json.loads()/json.load():将JSON格式反序列化为Python对象，前者接受JSON的字符串，后者从file-like Object中读取字符串并反序列化（磁盘/网络到内存）
    
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


# JSON Advanced - json.dumps(obj[, default=]) + json.loads(obj[, object_hook=])
'''
json.dumps()的可选参数default就是把任意一个对象变成一个可序列为JSON的对象。
'''


class Student():
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Alice', 18, 100)
# print(json.dumps(s)) # Got TypeError: Object of type Student is not JSON serializable without the std2dict


def std2dict(std):
    return {'name': std.name, 'age': std.age, 'score': std.score}


print('-'*85)
print(json.dumps(s, default=std2dict))

'''
不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict。
因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
'''
print('-'*85)
print(json.dumps(s, default=lambda obj: obj.__dict__))  # Same as the above


'''
同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
然后，我们传入的object_hook函数负责把dict转换为Student实例
'''


def dict2std(d):
    return Student(d['name'], d['age'], d['score'])


json_str = '{"name": "Alice", "age": 18, "score": 100}'
print('-'*85)
print(json.loads(json_str, object_hook=dict2std))  # 打印出的是反序列化的Student实例对象。


# 对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数
'''
If ``ensure_ascii`` is false, then the return value can contain non-ASCII
characters if they appear in strings contained in ``obj``. Otherwise, all
such characters are escaped in JSON strings.
'''
obj = dict(name='小明', age=20)
print('-'*85)
print(json.dumps(obj, ensure_ascii=True))
print('-'*85)
print(json.dumps(obj, ensure_ascii=False))
print('-'*85)
print(json.dumps(obj))  # In default, ensure_ascii sets to be True.
