'''
datetime是Python处理日期和时间的标准库。
    - datetime模块里的datetime类表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
    - 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。
'''
import re
from datetime import datetime, timedelta, timezone

# * datetime.now()返回当前日期和时间，其类型是datetime。
now = datetime.now()
print(now)
print(type(now))
print(now.date())

# * 要指定某个日期和时间，我们直接用参数构造一个datetime实例
dt = datetime(2100, 8, 5, 12, 00)
print(dt)

# * datetime -> timestamp
'''
在计算机中，时间实际上是用数字表示的。
1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），
当前时间就是相对于epoch time的秒数，称为timestamp。

可见timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，
这就是为什么计算机存储的当前时间是以timestamp表示的，
因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。
'''
# 把一个datetime类型转换为timestamp只需要简单调用timestamp()方法
# 注意Python的timestamp是一个浮点数，整数位表示秒。
print(dt.timestamp())
print(now.timestamp())
print(type(now.timestamp()))  # <class 'float'>

# * timestamp -> datetime + 时区
'''
注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。
用datetime.fromtimestamp(t)可以把timestamp t转换成本地时间的datetime。
本地时间是指当前操作系统设定的时区。例如北京时区是东8区。

timestamp也可以直接被转换到UTC标准时区的时间：
datetime.utcfromtimestamp(t)
'''
t = now.timestamp()
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

# * str转换为datetime [parse]
# 转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串
one_day = datetime.strptime('2111-1-1 1:1:1', '%Y-%m-%d %H:%M:%S')
print(one_day)
# %Y之类的ref：https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

# * datetime转换为str [format]
now = datetime.now()
print(now)
print(now.strftime('%a, %b %d %H:%M'))

# * datetime加减
'''
对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。
加减可以直接用+和-运算符，不过需要导入timedelta这个类
'''
Beijing_now = datetime.now()
Seattle_now = Beijing_now - timedelta(hours=15)
print(Seattle_now.strftime('%a, %b %d %H:%M'))

# * 本地时间转换为UTC时间
'''
本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。

一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，
除非强行给datetime设置一个时区
'''
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8)
print(dt)

'''
如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。
'''

# * 时区转换
'''
我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间

时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换。
'''
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
tk_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(utc_dt)
print(bj_dt)
print(tk_dt)

# * Practice


def to_timestamp(dt_str, tz_str):
    '''
    假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，
    均是str，请编写一个函数将其转换为timestamp
    '''
    tz_hrs = int(re.match(r'^.*([\+\-]\d+)\:.*$', tz_str).group(1))
    dt = datetime.strptime(
        dt_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone(timedelta(hours=tz_hrs)))
    return dt.timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
