'''
摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
摘要算法在很多地方都有广泛的应用。
要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，
但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。


摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，
计算f(data)很容易，但通过digest反推data却非常困难。而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。

比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。

有没有可能两个不同的数据通过某个摘要算法得到了相同的摘要？
完全有可能，因为任何摘要算法都是把无限多的数据集合映射到一个有限的集合中。这种情况称为碰撞。

# 摘要算法应用
任何允许用户登录的网站都会存储用户登录的用户名和口令。如何存储用户名和口令呢？方法是存到数据库表中。
如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里。
此外，网站运维人员是可以访问数据库的，也就是能获取到所有用户的口令。

正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5。
当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，
如果一致，说明口令输入正确，如果不一致，口令肯定错误。

'''

import hashlib
import random

# MD5
'''
MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。

如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
'''
md5 = hashlib.md5()
print(md5)  # <md5 _hashlib.HASH object @ 0x000001E48C3F8AF0>
print(type(md5))  # <class '_hashlib.HASH'>

md5.update('learning md5...'.encode('utf-8'))
print(md5.hexdigest())  # cdc2844b1e82c1f50c0c1a1473d7ffc6
md5.update('almost done...'.encode('utf-8'))
print(md5.hexdigest())  # 7652c6fe9eb070cfc0725f0e7f0bd0ed
print(len(md5.hexdigest()))  # 32

# SHA1
'''
调用SHA1和调用MD5完全类似;
SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
'''
sha1 = hashlib.sha1()
print(sha1)  # <sha1 _hashlib.HASH object @ 0x0000018562A48BB0>
print(type(sha1))  # <class '_hashlib.HASH'>

sha1.update('learning sha1...'.encode('utf-8'))
print(sha1.hexdigest())  # 45fb13ef123a8fcd043dbd64d5d051d849bae0b5
sha1.update('almost done...'.encode('utf-8'))
print(sha1.hexdigest())  # afb85aded2c32c17c4fd1cea130729575369ed96
print(len(sha1.hexdigest()))  # 40

# 根据用户输入的口令，计算出存储在数据库中的MD5口令
'''
存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令。
'''


def get_md5(password):
    '''根据用户输入的password，计算出对应的md5摘要'''
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


# 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(username, password):
    '''设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False'''
    return get_md5(password) == db[username]


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

# 加盐
'''
由于常用口令的MD5值很容易被计算出来，所以，
要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，
这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”
'''


def cal_md5(password):
    return get_md5(password+'some_complex-salt!')


'''
经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。

但是如果有两个用户都使用了相同的简单口令比如123456，在数据库中，将存储两条相同的MD5值，
这说明这两个用户的口令是一样的。有没有办法让使用相同口令的用户存储不同的MD5呢？

如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。
'''

# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5


def register(username, password):
    db[username] = get_md5(password + username + 'some-salt')


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


class User():
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(8, 85)) for i in range(18)])
        self.password = get_md5(password + self.salt)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    user = db[username]
    return user.password == get_md5(password + user.salt)


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
