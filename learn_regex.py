'''
正则表达式是一种用来匹配字符串的强有力的武器。
它的设计思想是用一种描述性的语言来给字符串定义一个规则，
凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。

Python提供re模块，包含所有正则表达式的功能。
由于Python的字符串本身也用\转义,因此强烈建议使用Python的r前缀，就不用考虑字符串转义的问题了。

如果用户输入了一组标签，下次记得用正则表达式来把不规范的输入转化成正确的数组。
'''
from operator import is_
import re

# 如何用字符来描述字符
'''
-----------------匹配一个------------------------
\d可以匹配一个数字,
\w可以匹配一个字母或数字,
.可以匹配任意字符,
\s可以匹配一个空格(也包括Tab等空白符),
-----------------可变长--------------------------
*表示任意个字符(包括0个),
+表示至少一个字符，
?表示0个或1个字符,
{n}表示n个字符,
{n,m}表示n到m个字符
-----------------其他----------------------------
'\'表转义，
用[]表示范围,
A|B可以匹配A或B,所以(P|p)ython可以匹配'Python'或者'python'
^表示行的开头，^\d表示必须以数字开头,
$表示行的结束，\d$表示必须以数字结束,
'''

# 整行匹配py
line_py = '^py$'

# 可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量
variable_pattern = '[a-zA-Z\_][0-9a-zA-Z\_]*'

# re.match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。
print(re.match(variable_pattern, '1a'))
print(re.match(variable_pattern, 'a1'))


# re.split()方法切分字符串
s1 = 'a, b;               c'
print(s1.split())
print(re.split(r'[\s\,\;]+', s1))

# 分组与提取子串。用()表示的就是要提取的分组（Group）。
# group(0)永远是与整个正则表达式相匹配的字符串，group(1)、group(2)……表示第1、2、……个子串。
m = re.match(r'^(\d{3})-(\d{3,8})$', '001-12345')
print(m.groups())
print(m.group(0))
print(m.group(1))
print(m.group(2))

# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。
# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
print(re.match(r'^(\d+)(0*)$', '10230000').groups())  # ('10230000', '')
# 加个?就可以让\d+采用非贪婪匹配（也就是尽可能少匹配）
print(re.match(r'^(\d+?)(0*)$', '10230000').groups())  # ('1023', '0000')


# 编译
'''
当我们在Python中使用正则表达式时，re模块内部会干两件事情：
    - 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
    - 用编译后的正则表达式去匹配字符串。

如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，
编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。
接下来重复使用时就不需要编译这个步骤了，直接匹配。
'''
# Compile
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# Use
print(re_telephone.match('000-122345').groups())
print(re_telephone.match('111-54321').groups())


# Email Address Validation
re_email = re.compile(r'^[a-zA-Z0-9\.\_\-]+@[a-zA-Z0-9\.\_\-]+\.com')


def is_valid_email(addr):
    if re_email.match(addr):
        return True
    return False


print(is_valid_email('someone@gmail.com'))
print(is_valid_email('haha@haha.com'))
