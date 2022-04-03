'''
requests是一个Python第三方库，处理URL资源特别方便。
'''
import requests

db = requests.get('https://www.douban.com/')
print(db.status_code)
print('================================')
print(dir(db))
print('================================')
print(db.text)
