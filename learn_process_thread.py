'''
# Conclusion
    1. Python既支持多进程multi-processing，又支持多线程multi-threading（多线程在Python中只能交替执行）
    2. 线程是最小的执行单元，而进程由至少一个线程组成。
    3. 如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间。
    4. 多进程和多线程的程序涉及到同步、数据共享的问题，编写起来更复杂。
    5. 在Unix/Linux下，可以使用os.fork()调用实现多进程。
    6. 要实现跨平台的多进程，可以使用multiprocessing模块。
    7. 进程间通信是通过Queue、Pipes等实现的。
    8. 多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
    9. Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
    10. 多进程稳定性高于多线程，但前者在Windows上创建代价大；用事件驱动的异步IO编程模型实现多任务是趋势（协程 in Python）。

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

# 多线程
'''
由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，
并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。

Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。
绝大多数情况下，我们只需要使用threading这个高级模块。

# threading
启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行。

# 多核CPU
因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，
即使100个线程跑在100核CPU上，也只能用到1个核。

GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。

所以，在Python中，可以使用多线程，但不要指望能有效利用多核。
如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。

不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。
多个Python进程有各自独立的GIL锁，互不影响。

# ThreadLocal
在多线程环境下，每个线程都有自己的数据。
一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。
但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦。

ThreadLocal应运而生。一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。

# 进程 vs. 线程
首先，要实现多任务，通常我们会设计Master-Worker模式，Master负责分配任务，Worker负责执行任务，因此，多任务环境下，通常是一个Master，多个Worker。
    - 如果用多进程实现Master-Worker，主进程就是Master，其他进程就是Worker。
    - 如果用多线程实现Master-Worker，主线程就是Master，其他线程就是Worker。

- 多进程模式
    - 最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程。（当然主进程挂了所有进程就全挂了，但是Master进程只负责分配任务，挂掉的概率低）著名的Apache最早就是采用多进程模式。
    - 缺点是创建进程的代价大，在Unix/Linux系统下，用fork调用还行，在Windows下创建进程开销巨大。另外，操作系统能同时运行的进程数也是有限的，在内存和CPU的限制下，如果有几千个进程同时运行，操作系统连调度都会成问题。

- 多线程模式
    - 优点是通常比多进程快一点，但是也快不到哪去。
    - 致命的缺点就是任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存。

无论是多进程还是多线程，只要数量一多，效率肯定上不去。
    - 操作系统在切换进程或者线程时，它需要先保存当前执行的现场环境（CPU寄存器状态、内存页等），然后，把新任务的执行环境准备好（恢复上次的寄存器状态，切换内存页等），才能开始执行。这个切换过程虽然很快，但是也需要耗费时间。如果有几千个任务同时进行，操作系统可能就主要忙着切换任务，根本没有多少时间去执行任务了，这种情况最常见的就是硬盘狂响，点窗口无反应，系统处于假死状态。
    - 所以，多任务一旦多到一个限度，就会消耗掉系统所有的资源，结果效率急剧下降，所有任务都做不好。

是否采用多任务的第二个考虑是任务的类型。我们可以把任务分为计算密集型和IO密集型。
    - 计算密集型任务的特点是要进行大量的计算，消耗CPU资源，比如计算圆周率、对视频进行高清解码等等，全靠CPU的运算能力。这种计算密集型任务虽然也可以用多任务完成，但是任务越多，花在任务切换的时间就越多，CPU执行任务的效率就越低，所以，要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数。计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。Python这样的脚本语言运行效率很低，完全不适合计算密集型任务。对于计算密集型任务，最好用C语言编写。
    - 涉及到网络、磁盘IO的任务都是IO密集型任务，这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成（因为IO的速度远远低于CPU和内存的速度）。对于IO密集型任务，任务越多，CPU效率越高，但也有一个限度。常见的大部分任务都是IO密集型任务，比如Web应用。IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少，因此，用运行速度极快的C语言替换用Python这样运行速度极低的脚本语言，完全无法提升运行效率。对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差。

# 异步IO
考虑到CPU和IO之间巨大的速度差异，一个任务在执行的过程中大部分时间都在等待IO操作，单进程单线程模型会导致别的任务无法并行执行，因此，我们才需要多进程模型或者多线程模型来支持多任务并发执行。

现代操作系统对IO操作已经做了巨大的改进，最大的特点就是支持异步IO。如果充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务，这种全新的模型称为事件驱动模型，Nginx就是支持异步IO的Web服务器，它在单核CPU上采用单进程模型就可以高效地支持多任务。在多核CPU上，可以运行多个进程（数量与CPU核心数相同），充分利用多核CPU。由于系统总的进程数量十分有限，因此操作系统调度非常高效。用异步IO编程模型来实现多任务是一个主要的趋势。

对应到Python语言，单线程的异步编程模型称为协程，有了协程的支持，就可以基于事件驱动编写高效的多任务程序。我们会在后面讨论如何编写协程。

P.S. 
# POSIX
POSIX表示可移植操作系统接口（Portable Operating System Interface of UNIX，缩写为 POSIX ），
POSIX标准定义了操作系统应该为应用程序提供的接口标准。POSIX标准意在期望获得源代码级别的软件可移植性。
换句话说，为一个POSIX兼容的操作系统编写的程序，应该可以在任何其它的POSIX操作系统（即使是来自另一个厂商）上编译执行。

# Windows NT
windows(win2000,winxp,win2003,winvista,win2008,win7）其实是windows NT,
全称Microsoft Windows NT(New Technology)即视窗NT是由微软公司发行的操作系统。
'''

# 分布式进程
'''
在Thread和Process中，应当优选Process，因为Process更稳定，
而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。

Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。
一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。
由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。

Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。

注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。
比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，
由Worker进程再去共享的磁盘上读取文件。
'''




import os
import time
import random
from multiprocessing import Pool
from multiprocessing import Process
from multiprocessing import Queue
import subprocess
import threading
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
    # print(f'Parent Process: {os.getpid()}')
    # # 父进程创建Queue，并传给各个子进程：
    # q = Queue()
    # pw = Process(target=write, args=(q,))
    # pr = Process(target=read, args=(q,))
    # # 启动子进程pw，写入:
    # pw.start()
    # # 启动子进程pr，读取:
    # pr.start()
    # # 等待pw结束:
    # pw.join()
    # # pr进程里是死循环，无法等待其结束，只能强行终止:
    # pr.terminate()

    # * Thread
    '''
    由于任何进程默认就会启动一个线程，我们把该线程称为主线程MainThread，主线程又可以启动新的线程，
    Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。

    主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。
    名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
    '''
    # # 新线程执行的函数
    # def loop():
    #     print(f'thread {threading.current_thread().name} is running...')
    #     n = 0
    #     for i in range(5):
    #         n += 1
    #         print(f'thread {threading.current_thread().name} >> {i}')
    #         time.sleep(0.001)
    #     print(f'thread {threading.current_thread().name} ended!')

    # print(f'thread {threading.current_thread().name} started!')
    # # t = threading.Thread(target=loop, name='LoopThread')
    # t = threading.Thread(target=loop)  # default name = 'Thread-1'
    # t.start()
    # t.join()
    # print(f'thread {threading.current_thread().name} ended!')

    # * Lock
    '''
    多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
    而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
    因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

    由于线程的调度是由操作系统决定的+高级语言的一条语句在CPU执行时是若干条语句，
    所以一个线程在执行中可能中断，从而导致多个线程把同一个对象的内容改乱了。

    为了解决这个问题，我们可以上锁。由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，
    所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现。

    锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，
    坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。
    其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，
    既不能执行，也无法结束，只能靠操作系统强制终止。

    当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
    获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定会被释放。
    '''
    # balance = 0
    # lock = threading.Lock()

    # def change_it(n):
    #     global balance
    #     balance += n
    #     balance -= n

    # def run_thread(n):
    #     for i in range(850):
    #         # 先获得锁
    #         lock.acquire()
    #         try:
    #             # 放心改(锁确保了某段关键代码只能由一个线程从头到尾完整地执行)
    #             change_it(n)
    #         finally:
    #             # 改完后一定要释放锁
    #             lock.release()

    # t1 = threading.Thread(target=run_thread, args=(5,))
    # t2 = threading.Thread(target=run_thread, args=(8,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # print(balance)

    # * ThreadLocal - 解决一个线程内不同函数间传递参数的问题！
    '''
    ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
    这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
    '''
    # 创建全局ThreadLocal对象
    local_school = threading.local()

    def process_student():
        '''获取当前线程关联的student'''
        std = local_school.student
        print(f'Hi {std} (in {threading.current_thread().name})!')

    def process_thread(name):
        local_school.student = name
        process_student()

    t1 = threading.Thread(target=process_thread,
                          args=('Alice', ), name='Class_A')
    t2 = threading.Thread(target=process_thread,
                          args=('Bob', ), name='Class_B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('End!')
