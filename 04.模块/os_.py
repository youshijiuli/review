# os-- 操作系统接口模块 ： https://docs.python.org/zh-cn/3.6/library/os.html


'''
os.getegid()¶
返回当前进程的有效组ID。对应当前进程执行文件的 “set id” 位。

Availability: Unix.

os.geteuid()
返回当前进程的有效用户ID。

Availability: Unix.

os.getgid()
返回当前进程的实际组ID。

os.getpid()¶
返回当前进程ID

常用的文件操作
os.fdopen(fd, *args, **kwargs)
返回打开文件描述符 fd 对应文件的对象。类似内建 open() 函数，二者接受同样的参数。不同之处在于 fdopen() 第一个参数应该为整数

os.close(fd)
关闭文件描述符 fd。
注解 该功能适用于低级 I/O 操作，必须用于 os.open() 或 pipe() 返回的文件描述符。关闭由内建函数 open() ， popen() 或 fdopen() 返回的 “文件对象”，则使用其相应的 close() 方法。

删除文件
os.remove(path, *, dir_fd=None)
os.rename()重命名文件
os.chdir()改变目录
os.mkdir/makedirs 创建目录/多层目录
 os.rmdir/removedirs 删除目录/多层目录
 os.listdir()列出指定目录的文件
 os.getcwd()取得当前工作目录
 os.chmod()改变目录权限



'''

#  说明一下 os.path 和 sys.path 分别代表什么？
'''
os.path 主要是用于对系统路径文件的操作。
sys.path 主要是对 Python 解释器的系统环境参数的操作（动态的改变 Python 解释器搜索路径）
'''
