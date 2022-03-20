'''
1. print()： the simplest way to debug. You can add print() to somewhere you think could go wrong.

2. assert: e.g. assert isinstance(n, int), 'n is not an integer!' 如果断言assert失败，assert语句本身就会抛出AssertionError。程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数(大写英文字母O)来关闭assert， e.g. 在命令行里输入python -O debug_way.py执行本文件会关闭assert。关闭后，你可以把所有的assert语句当成pass来看。

3. logging: 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件。
它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

4. pdb：以参数 -m pdb 启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。e.g. 在命令行中输入 python -m pdb debug_way.py就可以以本module以单步方式运行:
    - 输入命令l来查看代码
    - 输入命令n可以单步执行代码
    - 任何时候都可以输入命令p 变量名来查看变量
    - 输入命令q结束调试，退出程序
这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了，如果有一千行代码，要运行到第999行得敲多少命令啊。还好，我们还有另一种调试方法。

5. pdb.set_trace(): 只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点。运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行。这个方式比直接启动pdb单步调试效率要高很多，但也高不到哪去。

6. IDE：如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE，比如Visual Studio Code~虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。
'''

# Example 1 - assert


def cal(n):
    assert n != 0, 'n is zero!'
    return 85 / n


def main():
    cal(0)


main()
