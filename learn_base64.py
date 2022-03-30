'''
Base64是一种任意二进制数据到文本字符串的编码方法(用64个字符来表示任意二进制数据 AKA 一种二进制到字符串的转换方法)，
常用于在URL、Cookie、网页中传输少量二进制数据。

Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。

Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示。

如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，
再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
'''
import base64

# Python内置的base64可以直接进行base64的编解码
b = b'binary\x00string'
print(base64.b64encode(b))  # b'YmluYXJ5AHN0cmluZw=='
print(type(base64.b64encode(b)))  # <class 'bytes'>
print(base64.b64decode(base64.b64encode(b)))  # b'binary\x00string'
print(type(base64.b64decode(base64.b64encode(b))))  # <class 'bytes'>

# urlsafe_b64encode & urlsafe_b64decode
'''
由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
'''
url = b'i\xb7\x1d\xfb\xef\xff'
decode_url = b'abcd--__'
print(base64.b64encode(url))  # b'abcd++//'
print(base64.urlsafe_b64encode(url))  # b'abcd--__'
print(base64.urlsafe_b64decode(decode_url))  # b'i\xb7\x1d\xfb\xef\xff'

# 去掉“=”的encode & decode
'''
由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉。

去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，
因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。
'''


def safe_base64_encode(s):
    return base64.b64encode(s).rstrip(b'=')


def safe_base64_decode(s):
    plus_equals = 0
    if len(s) % 4:
        plus_equals = 4 - len(s) % 4
    return base64.b64decode(s + '='*plus_equals)


# test
assert b'YmluYXJ5AHN0cmluZw' == safe_base64_encode(
    b'binary\x00string'), safe_base64_encode(b'binary\x00string')

assert b'abcd' == safe_base64_decode(
    'YWJjZA=='), safe_base64_decode('YWJjZA==')

print('Pass tests!')
