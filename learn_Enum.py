from enum import Enum, unique
'''
Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
'''
print(type(Enum))

# In default, Enum automatically assigns enumeration values from 1.
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
             'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Jan.value)
print(type(Month))

# @unique: Ensure there are no duplicates. Basically, it raises an error if there are any duplicate enumeration values.


@unique
class Weekday(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7


print(type(Weekday))
for name, member in Weekday.__members__.items():
    print(name, '->', member, '->', member.value)

# Enum class Can Compare its members' values
print(max(Weekday.Monday.value, Weekday.Sunday.value))

# Enum class Cannot Change its members' values
try:
    Weekday.Monday = 0
except Exception as e:
    print(e)
