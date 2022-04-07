'''
一封电子邮件的旅程:
发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人
    - MUA：Mail User Agent——邮件用户代理（电子邮件软件）
    - MTA：Mail Transfer Agent——邮件传输代（Email服务提供商）
    - MDA：Mail Delivery Agent——邮件投递代理（长期保存邮件的地方）

有了上述基本概念，要编写程序来发送和接收邮件，本质上就是：
    - 发送：编写MUA把邮件发到MTA；
    - 接收：编写MUA从MDA上收邮件。

1. 发邮件时，MUA和MTA使用的协议就是SMTP：Simple Mail Transfer Protocol，后面的MTA到另一个MTA也是用SMTP协议。
2. 收邮件时，MUA和MDA使用的协议有两种：
    - POP：Post Office Protocol，目前版本是3，俗称POP3；
    - IMAP：Internet Message Access Protocol，目前版本是4，优点是不但能取邮件，还可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱，等等。


邮件客户端软件在发邮件时，会让你先配置SMTP服务器，也就是你要发到哪个MTA上。
假设你正在使用163的邮箱，你就不能直接发到新浪的MTA上，因为它只服务新浪的用户，
所以，你得填163提供的SMTP服务器地址：smtp.163.com，为了证明你是163的用户，
SMTP服务器还要求你填写邮箱地址和邮箱口令，这样，MUA才能正常地把Email通过SMTP协议发送到MTA。

类似的，从MDA收邮件时，MDA服务器也要求验证你的邮箱口令，确保不会有人冒充你收取你的邮件，
所以，Outlook之类的邮件客户端会要求你填写POP3或IMAP服务器地址、邮箱地址和口令，
这样，MUA才能顺利地通过POP或IMAP协议从MDA取到邮件。

最后特别注意，目前大多数邮件服务商都需要手动打开SMTP发信和POP收信的功能，否则只允许在网页登录。
'''
