def lazy_sum(*args):
    '''在这个例子中，我们在函数lazy_sum中又定义了函数sum，
    并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
    当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
    这种称为“闭包（Closure）”的程序结构拥有极大的威力。'''
    def sum_up():
        s = 0
        for a in args:
            s += a
        return s
    return sum_up


f = lazy_sum(*[i for i in range(10)])
print(f)  # 返回的函数并没有立刻执行，而是直到调用了f()才执行。
print(f())

g = lazy_sum(*[i for i in range(10)])
print('\n', f == g)  # 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数,两次调用结果互不影响
