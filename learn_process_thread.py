'''
# Conclusion
    1. Python既支持多进程multi-processing，又支持多线程multi-threading
    2. 线程是最小的执行单元，而进程由至少一个线程组成。
    3. 如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间。
    4. 多进程和多线程的程序涉及到同步、数据共享的问题，编写起来更复杂。
    5. 在Unix/Linux下，可以使用os.fork()调用实现多进程。
    6. 要实现跨平台的多进程，可以使用multiprocessing模块。
    7. 进程间通信是通过Queue、Pipes等实现的。

对于操作系统来说，一个任务就是一个进程（Process）。
在一个进程Process内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程（Thread）。
由于每个进程至少要干一件事，所以，一个进程Process至少有一个线程Thread。

什么叫“多任务”呢？简单地说，就是操作系统可以同时运行多个任务。
现在，多核CPU已经非常普及了，但是，即使过去的单核CPU，也可以执行多任务。
由于CPU执行代码都是顺序执行的，那么，单核CPU是怎么执行多任务的呢？:
    - 答案就是操作系统轮流让各个任务交替执行。表面上看，每个任务都是交替执行的，
      但是，由于CPU的执行速度实在是太快了，我们感觉就像所有任务都在同时执行一样。

真正的并行执行多任务只能在多核CPU上实现，但是，由于任务数量远远多于CPU的核心数量，
所以，操作系统也会自动把很多任务轮流调度到每个核心上执行。
    - 多线程的执行方式和多进程是一样的，也是由操作系统在多个线程之间快速切换，让每个线程都短暂地交替运行，
      看起来就像同时执行一样。当然，真正地同时执行多线程需要多核CPU才可能实现。

我们前面编写的所有的Python程序，都是执行单任务的进程，也就是只有一个线程。
如果我们要同时执行多个任务怎么办？
    1. 【多进程模式】启动多个进程，每个进程虽然只有一个线程，但多个进程可以一块执行多个任务。
    2. 【多线程模式】启动一个进程，在一个进程内启动多个线程，这样，多个线程也可以一块执行多个任务。
    3. 【多进程+多线程模式】启动多个进程，每个进程再启动多个线程，这样同时执行的任务就更多了。这种模型更复杂，实际很少采用。

同时执行多个任务通常各个任务之间并不是没有关联的，而是需要相互通信和协调
（比如电脑上播放视频，得一个线程播放视频，另一个线程播放音频），
有时，任务1必须暂停等待任务2完成后才能继续执行，有时，任务3和任务4又不能同时执行，
所以，多进程和多线程的程序的复杂度要远远高于我们前面写的单进程单线程的程序。
'''

# 多进程（multiprocessing）
'''
# Fork
有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，
常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。

如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。
由于Windows没有fork调用，难道在Windows上无法用Python编写多进程的程序？
由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。


# Process
multiprocessing模块就是跨平台版本的多进程模块。
multiprocessing模块提供了一个Process类来代表一个进程对象。
创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，
用start()方法启动，这样创建进程比fork()还要简单。
join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

# Pool
如果要启动大量的子进程，可以用进程池的方式批量创建子进程。
Pool的默认大小是CPU的核数。

# subprocess
很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。

# 进程间通信
Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。

# 关于Windows
在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。
由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，
父进程所有Python对象都必须通过pickle序列化再传到子进程去，
所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。

'''




import os
import time
import random
from multiprocessing import Pool
from multiprocessing import Process
from multiprocessing import Queue
import subprocess
def run_proc(name):
    print(f'Run child process: {name} ({os.getpid()})')


def long_run_task(name):
    print(f'Run Task {name} ({os.getpid()})')
    start = time.perf_counter()
    time.sleep(random.random()*5)
    end = time.perf_counter()
    print(f'Task {name} runs {(end-start):.2f} seconds')


def write(q):
    print(f'Process to write: {os.getpid()}')
    for value in ['A', 'B', 'C']:
        print(f'Put {value} to queue...')
        q.put(value)
        time.sleep(random.random())


def read(q):
    print(f'Process to read: {os.getpid()}')
    while True:
        value = q.get(True)
        print(f'Get {value} from queue.')


if __name__ == '__main__':
    # * Process Example
    # print(f'Parent process: {os.getpid()}')
    # p = Process(target=run_proc, args=('test',))
    # print('Child process will start.')
    # p.start()
    # p.join()
    # print('Child process end.')

    # * Pool Example
    '''
    Pool的默认大小是CPU的核数。Like 16核的CPU就会default设置Pool的大小是16。Pool的大小就是同时执行进程的个数。
    对Pool对象调用join()方法会等待所有子进程执行完毕，
    调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    '''
    # print(f'Parent process: {os.getpid()}')
    # p = Pool()
    # for i in range(18):
    #     p.apply_async(long_run_task, args=(i,))
    # print('Waiting for all subprocesses done...')
    # p.close()
    # p.join()
    # print('All subprocesses done!')

    # * subprocess Example
    '''
    如果子进程还需要输入，则可以通过communicate()方法输入。
    '''
    # print('$ nslookup www.anqiwu.one')
    # r = subprocess.call(['nslookup', 'www.anqiwu.one'])
    # print('Exit code:', r)

    # * 进程间通信
    print(f'Parent Process: {os.getpid()}')
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
