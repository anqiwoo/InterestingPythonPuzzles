'''
urllib提供了一系列用于操作URL的功能。

urllib提供的功能就是利用程序去执行各种HTTP请求。
如果要模拟浏览器完成特定功能，需要把请求伪装成浏览器
伪装的方法是先监控浏览器发出的请求，再根据浏览器的请求头来伪装，User-Agent头就是用来标识浏览器的。
'''
from urllib import request

# with request.urlopen('https://www.anqiwu.one') as f:
#     data = f.read()
#     print(f"Status: {f.status}, {f.reason}")
#     for k, v in f.getheaders():
#         print(f'{k}: {v}')
# print(f"Data: {data.decode('utf-8')}")

# 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。
req = request.Request('https://www.anqiwu.one')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print(f'Status: {f.status}, {f.reason}')
    for k, v in f.getheaders():
        print(f'{k}: {v}')
    print(f"Data:\n{f.read().decode('utf-8')}")


# 如果要以POST发送一个请求，只需要把参数data以bytes形式传入,
# 比如：with request.urlopen(req, data=login_data.encode('utf-8'))：

# 如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理
