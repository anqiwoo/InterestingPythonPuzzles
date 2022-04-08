'''
用Python的poplib模块收取邮件分两步：
第一步是用POP3协议把邮件获取到本地，
第二步是用email模块把原始邮件解析为Message对象，然后，用适当的形式把邮件内容展示给用户即可。

收取邮件就是编写一个MUA作为客户端，从MDA把邮件获取到用户的电脑或者手机上。
收取邮件最常用的协议是POP协议，目前版本号是3，俗称POP3。

Python内置一个poplib模块，实现了POP3协议，可以直接用来收邮件。

注意到POP3协议收取的不是一个已经可以阅读的邮件本身，而是邮件的原始文本，这和SMTP协议很像，SMTP发送的也是经过编码后的一大段文本。

要把POP3收取的文本变成可以阅读的邮件，还需要用email模块提供的各种类来解析原始文本，变成可阅读的邮件对象。

所以，收取邮件分两步：
    - 第一步：用poplib把邮件的原始文本下载到本地；
    - 第二步：用email解析原始文本，还原为邮件对象。
'''

# * 通过POP3下载邮件
'''
用POP3获取邮件其实很简单，要获取所有邮件，只需要循环使用retr()把每一封邮件内容拿到即可。
真正麻烦的是把邮件的原始内容解析为可以阅读的邮件对象。
'''

from email.utils import parseaddr
from email.header import decode_header
from email.parser import Parser
import poplib
email = input('Email:')
password = input('Password:')
pop3_server = input('Pop3 Server: ')

server = poplib.POP3(pop3_server)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

server.user(email)
server.pass_(password)

print(server.stat())  # stat()返回邮件数量和占用空间
resp, mails, octets = server.list()  # list()返回所有邮件的编号
print(mails)

index = len(mails)
resp, lines, octets = server.retr(index)  # 获取最新一封邮件, 注意索引号从1开始

msg_content = b'\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)  # 只需要一行代码就可以把邮件内容解析为Message对象

server.quit()

# * 解析邮件

'''
只需要一行代码就可以把邮件内容解析为Message对象：

msg = Parser().parsestr(msg_content)
但是这个Message对象本身可能是一个MIMEMultipart对象，即包含嵌套的其他MIMEBase对象，嵌套可能还不止一层。

所以我们要递归地打印出Message对象的层次结构
'''
