'''
psutil使得Python程序获取系统信息变得易如反掌。
psutil还可以获取用户信息、Windows服务等很多有用的系统信息，
具体请参考psutil的官网：https://github.com/giampaolo/psutil

用Python来编写脚本简化日常的运维工作是Python的一个重要用途。

在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。顾名思义，psutil = process and system utilities，它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。
'''
import psutil
print(psutil.cpu_count())  # CPU逻辑数量
print(psutil.cpu_count(logical=False))  # CPU物理核心

print(psutil.cpu_times())

print(psutil.disk_partitions())
print(psutil.disk_usage('C:\\'))
print(psutil.disk_usage('D:\\'))

print(psutil.net_connections())
