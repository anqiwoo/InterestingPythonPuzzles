'''
SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。

Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。

BTW, the smtp server for outlook emails: smtp-mail.outlook.com
for gmails: smtp.gmail.com & the port should be 587

使用Python的smtplib发送邮件十分简单，只要掌握了各种邮件类型的构造方法，正确设置好邮件头，就可以顺利发出。

构造一个邮件对象就是一个Messag对象，如果构造一个MIMEText对象，就表示一个文本邮件对象，
如果构造一个MIMEImage对象，就表示一个作为附件的图片，要把多个对象组合起来，就用MIMEMultipart对象，
而MIMEBase可以表示任何对象。它们的继承关系如下：

Message
+- MIMEBase
   +- MIMEMultipart
   +- MIMENonMultipart
      +- MIMEMessage
      +- MIMEText
      +- MIMEImage
这种嵌套关系就可以构造出任意复杂的邮件。你可以通过email.mime文档(https://docs.python.org/3/library/email.mime.html)查看它们所在的包以及详细的用法。
'''

# * text email
from email.utils import parseaddr, formataddr
from email.header import Header
from email import encoders
import smtplib
from email.mime.text import MIMEText

# msg = MIMEText('Hello, sent by Python!', 'plain', 'utf-8')
# '''
# 注意到构造MIMEText对象时，第一个参数就是邮件正文，
# 第二个参数是MIME的subtype，传入'plain'表示纯文本，
# 最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
# '''
# # 然后，通过SMTP发出去
# from_addr = input('From: ')
# password = input('Password: ')
# to_addr = input('To: ')
# smtp_server = input('SMTP Server: ')

# server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
# server.ehlo()
# server.starttls()
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()
'''
用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
SMTP协议就是简单的文本命令和响应。login()方法用来登录SMTP服务器，
sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，
邮件正文是一个str，as_string()把MIMEText对象变成str。

加上：
server.ehlo()
server.starttls()
能解决SMTP AUTH extension not supported by server的error

使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。
要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。
只需要在创建SMTP对象后，立刻调用starttls()方法，就创建了安全连接。

某些邮件服务商，例如Gmail，提供的SMTP服务必须要加密传输。
'''

# * Advanced Email Settings
'''
邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，
而是包含在发给MTA的文本中的，所以，我们必须把From、To和Subject添加到MIMEText中，才是一封完整的邮件
'''


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode('utf-8'), addr))


from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('Smtp Server: ')

msg = MIMEText('Hello again, send by Python!', 'plain', 'utf-8')
# msg['From'] = _format_addr(f'Python Enthusiast {from_addr}')
# msg['To'] = _format_addr(f'Admin {to_addr}')
msg['Subject'] = Header('Greetings from SMTP 嘻嘻', 'utf-8').encode('utf-8')

server = smtplib.SMTP(smtp_server, 25)
server.ehlo()
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
