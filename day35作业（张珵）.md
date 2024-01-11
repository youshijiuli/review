# day35作业（张珵）

# 进程

## 1、进程间内存是否共享？如何实现通讯？

进程间内存不共享，通过网络或者写文件的形式实现通讯：

+ 基于文件，仅适用于同一台机器上的IPC，包括队列、管道
+ 基于网络，适用于同一台机器或多台机器上的IPC，有许多第三方工具（消息中间件）：如memcache、redis、rabbitmq、kafka6

## 2、请聊聊进程队列的特点和实现原理？

进程队列基于socket的文件级别的通信、pickle模块和进程锁（Lock）来完成数据传递，取值遵循先进先出。因此所有pickle支持的类型都可以放到队列中，并且队列传递的数据是安全的。队列的底层是管道（Pipe）。

```
请聊聊进程队列的特点和实现原理？
    特点 :
        1.进程之间的通信
        2.数据安全
        3.先进先出
    实现原理:
        基于管道 + 锁
        管道 基于文件级别的socket + pickle实现的
```

## 3、请画出进程的三状态转换图

![进程三状态图](D:\老男孩\day035\进程三状态图.png)

4、你了解生产者模型消费者模型么？如何实现？

- 生产者将生产的数据放进一个容器，然后消费者从这个容器中取数据，其本质是让生产数据和消费数据的效率达到平衡并且最大化。即把生产数据和消费数据分开，根据生产和消费的效率不同，来规划生产者和消费者的个数。该模型提高了程序执行效率，降低了开启的并发数，减小了操作系统的压力）。
  生产者消费者模型把原本获取数据处理数据的完整过程进行了解耦：
  
  - 紧耦合的程序：程序所有的功能\代码都放在一起，不分函数不分类也不分文件（不好）
  - 松耦合的程序：把功能拆分得很清楚的程序（好）
  
```
      了解
      为什么了解? 工作经历
          采集图片/爬取音乐 :由于要爬取大量的数据,想提高爬取效率
          有用过一个生产者消费者模型,这个模型是我自己写的,消息中间件
          用的是xxx,获取网页的过程作为生产者,分析网页,获取所有歌曲链接
          作为消费者.
          自己写监控,或者是自己写邮件报警系统,监控程序作为生产者,一旦发现了
          有问题的程序就需要把这个需要发送的邮件信息交给消息中间件redis,
          消费者就从中间件中取值,然后来处理发邮件的逻辑.
      什么时候用过?
          项目 或者 例子
      在python中实现生产者消费者模型可以用哪些机制
          消息中间件
          celery : 定时发短信的任务
```

5、从你的角度说说进程在计算机中扮演什么角色？

进程是计算机中最小的资源分配单位，进程是由操作系统调度的，每个进程一启动时就会分配一块内存，相关的代码、数据都会存在这块内存里。

进程之间内存隔离

回收线程的资源

```
从你的角度说说进程在计算机中扮演什么角色？
    资源分配的最小单位
    进程与进程之间内存隔离
    进程是由操作系统负责调度的,并且多个进程之间是一种竞争关系
    所以我们应该对进程的三状态时刻关注,尽量减少进程中的io操作,或者在进程里开线程来规避io
    让我们写的程序在运行的时候能够更多的占用cpu资源.
```

线程
1、GIL锁是怎么回事?

GIL是全局解释器锁，其目的是为了完成GC机制，精准地统计每一个线程里有哪些数据需要回收处理，即对不同线程的引用计数的变化记录得更加精准。在CPython、PYPY解释器下GIL导致了同一个进程中的多个线程只能有一个线程真正被CPU执行，即无法利用多核；在JPython解释器下则可以利用多核



2、在python中是否线程安全？

单线程时安全，多线程时不安全

```
# 线程之间数据共享
# 多线程的情况下,
    # 如果在计算某一个变量的时候,还要进行赋值操作,这个过程不是由一条完整的cpu指令完成的
    # 如果在判断某个bool表达式的之后,再做某些操作,这个过程也不是由一条完整的cpu指令完成的
    # 在中间发生了GIL锁的切换(时间片的轮转),可能会导致数据不安全.
```

3、什么叫死锁？

死锁现象是指两个或两个以上的进程或线程在执行过程中，因争夺资源而造成的一种互相等待的现象，若无外力作用，它们都将无法推进下去。



4、logging模块是否是线程安全的？

logging模块是线程安全的



5、queue是否线程安全？

queue是线程安全的



6、程序从flag a执行到falg b的时间大致是多少秒？

```
import threading
import time
def _wait():
	time.sleep(60)
# flag a
t = threading.Thread(target=_wait,daemon = False)
t.start()
# flag b
```

0秒，因为是开线程是异步执行的，开完子线程后主线程会继续执行自己后面的代码。由于t不是守护线程，所以执行完flag b之后，主线程会等待t结束，然后再结束。



7、程序从flag a执行到falg b的时间大致是多少秒？

```
import threading
import time
def _wait():
	time.sleep(60)
# flag a
t = threading.Thread(target=_wait,daemon = True)
t.start()
# flag b
```

0秒，因为是开线程是异步执行的，开完子线程后主线程会继续执行自己后面的代码。由于t是守护线程，所以执行完flag b之后，主线程不会等待t结束，而是主线程立即结束，进而主进程立即结束，进而t也立即结束。



8、程序从flag a执行到falg b的时间大致是多少秒？

```
import threading
import time
def _wait():
	time.sleep(60)
# flag a
t = threading.Thread(target=_wait,daemon = True)
t.start()
t.join()
# flag b
```

60秒，因为加入了t.join()，所以主线程的代码会等待子线程 t 结束后再执行flag b。如果这里不加t.join()，主线程会立即结束，进而导致主进程立即结束，进而导致守护线程 t 立即结束。



9、读程序，请确认执行到最后number是否一定为0

```
import threading
loop = int(1E7)
def _add(loop:int = 1):
	global number
	for _ in range(loop):
		number += 1
def _sub(loop:int = 1):
	global number
	for _ in range(loop):
		number -= 1
number = 0
ta = threading.Thread(target=_add,args=(loop,))
ts = threading.Thread(target=_sub,args=(loop,))
ta.start()
ts.start()
ta.join()
ts.join()
```

不一定，ta和ts并发执行，+=、-=本身都不是原子性操作，是数据不安全的，再加上未加线程锁，因此存在两个线程同时操作number的可能，因此可能会导致数据不安全



10、读程序，请确认执行到最后number是否一定为0

```
import threading
loop = int(1E7)
def _add(loop:int = 1):
	global number
	for _ in range(loop):
		number += 1
def _sub(loop:int = 1):
	global number
	for _ in range(loop):
		number -= 1
number = 0
ta = threading.Thread(target=_add,args=(loop,))
ts = threading.Thread(target=_sub,args=(loop,))
ta.start()
ta.join()
ts.start()
ts.join()
```

一定为0，由于ts需要等待全部ta执行完毕再开始执行，所以即使未加线程锁，也一定是数据安全的，不存在两个进程同时操作number的可能



11、读程序，请确认执行到最后number的长度是否一定为1

```
import time
import threading
loop = int(1E7)
def _add(loop:int = 1):
	global numbers
	for _ in range(loop):
		numbers.append(0)
def _sub(loop:int = 1):
	global numbers
	for _ in range(loop):
		while not numbers:
			time.sleep(1E-8)
		numbers.pop()
numbers = [0]
ta = threading.Thread(target=_add,args=(loop,))
ts = threading.Thread(target=_sub,args=(loop,))
ta.start()
ta.join()
ts.start()
ts.join()
```

结果的长度一定为1。这是因为虽然while本身是数据不安全的，但是append和pop是数据安全的，再加上只开了一个pop线程，不存在while判断完CPU轮转到另一个pop线程等回来时列表已经为空的情况，所以该程序不会报错并且执行到最后number的长度一定为1



12、读程序，请确认执行到最后number的长度是否一定为1

```python
import time
import threading
loop = int(1E7)
def _add(loop:int = 1):
	global numbers
	for _ in range(loop):
		numbers.append(0)
def _sub(loop:int = 1):
	global number
	for _ in range(loop):
		while not numbers:
			time.sleep(1E-8)
		numbers.pop()
numbers = [0]
ta = threading.Thread(target=_add,args=(loop,))
ts = threading.Thread(target=_sub,args=(loop,))
ta.start()
ts.start()
ta.join()
ts.join()
```

结果的长度一定为1。

首先，append和pop是数据安全的。其次，虽然while是数据不安全的，但是由于只开了一个pop线程，不存在while判断完CPU轮转到另一个pop线程等回来时列表已经为空的情况，所以该程序不会报错并且执行到最后number的长度一定为1。

如果本题改成有两个pop线程，那就不一定为1了，因为两个pop线程同时执行的时候会造成数据不安全