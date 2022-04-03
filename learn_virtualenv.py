'''
virtualenv为应用提供了隔离的Python运行环境，解决了不同应用间多版本的冲突问题。

每个应用可能需要各自拥有一套“独立”的Python运行环境。virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。

virtualenv是如何创建“独立”的Python运行环境的呢？
原理很简单，就是把系统Python复制一份到virtualenv的环境，
用命令source venv/bin/activate进入一个virtualenv环境时，
virtualenv会修改相关环境变量，让命令python和pip均指向当前的virtualenv环境。
'''

# 命令virtualenv就可以创建一个独立的Python运行环境，
# 我们还加上了参数--no-site-packages，
# 这样，已经安装到系统Python环境中的所有第三方包都不会复制过来，
# 我们就得到了一个不带任何第三方包的“干净”的Python运行环境。
'''
$ mkdir new_project
$ cd new_project
$ virtualenv --no-site-packages venv
$ source venv/bin/activate # mac/linux
$ source venv/Scripts/activate # windows
$ deactivate # 退出当前的venv环境，使用deactivate命令
'''
