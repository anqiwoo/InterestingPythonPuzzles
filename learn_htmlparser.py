'''
利用HTMLParser，可以把网页中的文本、图像等解析出来。

HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。
好在Python提供了HTMLParser来非常方便地解析HTML，只需简单几行代码。
'''
from html.parser import HTMLParser
from html.entities import name2codepoint
