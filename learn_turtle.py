'''
在1966年，Seymour Papert和Wally Feurzig发明了一种专门给儿童学习编程的语言——LOGO语言，
它的特色就是通过编程指挥一个小海龟（turtle）在屏幕上绘图。

海龟绘图（Turtle Graphics）后来被移植到各种高级语言中，Python内置了turtle库，
基本上100%复制了原始的Turtle Graphics的所有功能。

调用width()函数可以设置笔刷宽度，调用pencolor()函数可以设置颜色。更多操作请参考turtle库的说明。
绘图完成后，记得调用done()函数，让窗口进入消息循环，等待被关闭。否则，由于Python进程会立刻结束，将导致窗口被立刻关闭。

'''
from turtle import *

# 设置笔刷宽度:
width(4)

# 设置颜色
pencolor('pink')


def drawStar(x, y=0):
    pu()
    goto(x, y)
    pd()

    # set heading = 0
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)


for x in range(0, 250, 50):
    drawStar(x)

# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()
