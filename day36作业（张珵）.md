# day36作业

**1、什么是协程？常用的协程模块有哪些？**

协程本质就是一条线程，多个任务在一条线程上来回切换。常用的协程模块有gevent和asyncio



**2、协程中的join是用来做什么用的？它是如何发挥作用的？**

阻塞直到协程任务结束，本质上是为了产生I/O操作以便从当前线程切换到协程任务中去



**3、使用协程实现并发的tcp server端**

```python
import socket
print(socket.socket)
from gevent import monkey
monkey.patch_all()
import socket
import gevent

def func(conn):
    while True:
        msg = conn.recv(1024).decode('utf-8').upper()
        conn.send(msg.encode('utf-8'))

sk = socket.socket()
sk.bind(('127.0.0.1',9001))
sk.listen()

while True:
    conn,_ = sk.accept()
    gevent.spawn(func,conn)
```



**4、进程池、线程池的优势和特点** 

高计算的场景适合使用进程池，没有io（没有文件操作、没有数据库操作、没有网络操作、没有input）

其他场景适合使用线程池。



**5、线程和协程的异同?**

相同：都数据共享，不能利用多核

不同：
1.协程比线程开销更小
2.线程数据不安全(非原子性操作)
操作系统级别切换；协程数据安全(无须加锁)
用户级别切换

3.一些和文件操作相关的io只有操作系统能感知
（如print、input）
线程对于io操作的感知比协程更敏感；协程的所有的切换都基于用户，只有在用户级别能够感知到的io操作才会用协程模块做切换来规避（如socket，请求网页的，time.sleep）



**6、请列举一个python中数据安全的数据类型？**

Python中的队列基于管道（Pipe）和进程锁（Lock）来完成进程之间通信，队列传递的数据是安全的。此外，队列取值遵循先进先出，所有pickle支持的类型都可以放到队列中



**7、Python中如何使用线程池和进程池**

使用进程池：导入concurrent.futures中的ProcessPoolExecutor，实例化pp=ProcessPoolExecutor()，pp.submit(func, 参数)即可开启进程池。

使用线程池：导入concurrent.futures中的ThreadPoolExecutor，实例化tp=ThreadPoolExecutor()，tp.submit(func, 参数)即可开启线程池。



**8、什么是并行，什么是并发？**

并行指多个程序同时在多个cpu（多核）上执行

并发指只有一个cpu的情况下，多个程序轮流在一个cpu上执行



**9、请解释同步和异步这两个概念？**

同步：在做A事件的时候发起B事件，必须等待B事件结束之后才能继续做A事件（调用一个操作，要等待结果）

异步：在做A事件的时候发起B事件，不需要等待B事件结束就可以继续执行A事件（调用一个操作，不等待结果）



**10、请谈谈对异步非阻塞的了解？**

异步非阻塞调用一个函数不需要等待这个函数的执行结果，并且在执行这个函数的过程中CPU工作，如：开启一个进程或线程的start()方法、关闭一个进程的terminate()方法等



**11、用async关键字写一个最简单的协程函数**

```python
import asyncio

async def func(name):
    print('start',name)
    await asyncio.sleep(1)
    print('end')

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([func('alex'),func('太白')]))
```



**12、async和await这两个关键字是什么意思？**

await 后面接一个可能会发生阻塞的方法，await 关键字必须写在一个async函数里