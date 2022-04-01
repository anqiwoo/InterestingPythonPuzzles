'''
Hmac算法：Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。

Python内置的hmac模块实现了标准的Hmac算法，它利用一个key对message计算“杂凑”后的hash，
使用hmac算法比标准hash算法更安全，因为针对相同的message，不同的key会产生不同的hash。

'''

import hmac
import random

# 我们首先需要准备待计算的原始消息message，随机key，哈希算法，这里采用MD5
'''
可见使用hmac和普通hash算法非常类似。
hmac输出的长度和原始哈希算法的长度一致。
需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。
'''
message = '啊 Hi, hmac!'.encode('utf-8')
key = 'qq'.encode('utf-8')
h = hmac.new(key, message, digestmod='MD5')  # ffea5e2279c4646a2a5e48ef9bb32cca
print(h.hexdigest())
h.update('almost done...'.encode('utf-8'))  # e2b2a653fd2dda5808760525d3a20bcc
print(h.hexdigest())
print(len(h.hexdigest()))

# Application


def hmac_md5(key: str, s: str):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()


class User():
    def __init__(self, username: str, password: str):
        self.username = username
        self.key = ''.join([chr(random.randint(8, 85)) for i in range(18)])
        self.password = hmac_md5(self.key, password)


db = {
    'alice': User('alice', '12345'),
    'lisa': User('lisa', '54321'),
    'vicky': User('vicky', 'hahaha')
}


def login(username, password):
    user = db[username]
    return hmac_md5(user.key, password) == user.password


# Test
assert not login('alice', '11111')
assert not login('lisa', '543210')
assert not login('vicky', 'haha')
assert login('lisa', '54321')
assert login('vicky', 'hahaha')
assert login('alice', '12345')
print('Pass!')
