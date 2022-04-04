'''
Python内置的Tkinter可以满足基本的GUI程序的要求，
如果是非常复杂的GUI程序，建议用操作系统原生支持的语言和库来编写。

Python支持多种图形界面的第三方库，包括：
    - Tk
    - wxWidgets
    - Qt
    - GTK
    等等。

但是Python自带的库是支持Tk的Tkinter，使用Tkinter，无需安装任何包，就可以直接使用。
我们编写的Python代码会调用内置的Tkinter，Tkinter封装了访问Tk的接口。

Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；
Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。
所以，我们的代码只需要调用Tkinter提供的接口就可以了。
'''
from tkinter import *
import tkinter.messagebox as messagebox

# * Application 1: simple hello Vicky GUI application
'''
在GUI中，每个Button、Label、输入框等，都是一个Widget。
Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。

pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。

在createWidgets()方法中，我们创建一个Label和一个Button，当Button被点击时，触发self.quit()使程序退出。
'''


class Application1(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, Vicky!')
        self.helloLabel.pack()  # Pack a widget in the parent widget.
        self.quitButton = Button(self, text='Bye!', command=self.quit)
        self.quitButton.pack()  # Pack a widget in the parent widget.


app1 = Application1()
app1.master.title('Hello, Vicky')  # Set the windows title
app1.mainloop()  # loop main message
'''
GUI程序的主线程负责监听来自操作系统的消息，并依次处理每一条消息。因此，如果消息处理非常耗时，就需要在新线程中处理。
'''

# * Application 2: Simple GUI app with a messagebox


class Application2(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        # name = 'Vicky' if the self.nameInput.get() evaluates False.
        name = self.nameInput.get() or 'Vicky'
        messagebox.showinfo('Message', f"Hello, {name}")


app2 = Application2()
app2.master.title('Hello, Vicky！')
app2.mainloop()
