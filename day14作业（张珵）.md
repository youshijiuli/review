## day14 作业（张珵）

1. 整理今天的笔记以及课上代码，完善昨天没有写完的作业。

2. 将课上模拟博客园登录的装饰器的认证的代码完善好，整清楚。

   ```python
   def get_user_dict(filename):
       result_dict = {}
       with open(filename, encoding='gbk') as f:
           for line in f:
               line_list = line.strip().split('|')
               result_dict[line_list[0].strip()] = line_list[1].strip()
       return result_dict
   
   #返回两个值：登陆成功时返回username,True、登陆失败时返回None,False
   def login():
       user_dict = get_user_dict('register.txt')
       code = 'qwer'
       time_left = 3
       while time_left>=1:
           username = input('请输入用户名：').strip()
           password = input('请输入密码：').strip()
           your_code = input('请输入验证码：').strip()
           if your_code == code:
               if username in user_dict and password == user_dict[username]:
                   print(f'{username}您好！您已登录成功！')
                   return username,True
               else:
                   time_left = time_left - 1
                   if time_left!=0:
                       print(f'账号或者密码错误，您还剩{time_left}次机会')
           else:
               print('验证码错误')
       else:
           print('您已输错三次，无法继续登陆！')
           return None,False
   
   def register():【尚未改成字典！！！】
       code='qwer'
       while 1:
           username = input('请输入用户名：').strip()
           password = input('请输入密码：').strip()
           your_code = input('请输入验证码：').strip()
           if your_code == code:
               with open('register.txt',encoding='gbk',mode='r+')as f:
                   for line in f:
                       line=line.strip().split('|')
                       if username == line[0].strip():
                           print('用户名已存在，请重新输入')
                           break
                   else:
                       f.write(username+'|'+password)
                       print('注册成功')
                       return True
           else:
               print('验证码错误')
   
   print('欢迎访问博客园！')
   login_result=login()
   status_dict={'username':login_result[0],'status':login_result[1]}
   
   #装饰器
   def auth(f):
       def inner(*args,**kwargs):
           if status_dict['status']==True:
               f(*args, **kwargs)
           else:
               print('您尚未登陆，无法查看相关页面！')
           return
       return inner
   
   @auth
   def article():
       print('欢迎访问文章页面')
   
   @auth
   def comment():
       print('欢迎访问评论页面')
   
   @auth
   def diary():
       print('欢迎访问日记页面')
   
   article()
   comment()
   diary()
   
   【执行结果1】
   欢迎访问博客园！
   请输入用户名：oddgod
   请输入密码：123456
   请输入验证码：qwer
   oddgod您好！您已登录成功！
   欢迎访问文章页面
   欢迎访问评论页面
   欢迎访问日记页面
   
   【执行结果2】
   欢迎访问博客园！
   请输入用户名：qwer
   请输入密码：qwer
   请输入验证码：qwer
   账号或者密码错误，您还剩2次机会
   请输入用户名：qwer
   请输入密码：qwer
   请输入验证码：qwer
   账号或者密码错误，您还剩1次机会
   请输入用户名：qwer
   请输入密码：qwer
   请输入验证码：qwer
   您已输错三次，无法继续登陆！
   您尚未登陆，无法查看相关页面！
   您尚未登陆，无法查看相关页面！
   您尚未登陆，无法查看相关页面！
   ```

3. 看代码写结果：

   不加语法糖时

   ```
   def wrapper(f):
       def inner(*args,**kwargs):
           print(111)
           r = f(*args,**kwargs)
           print(222)
           return r
       return inner
   
   def func():
       print(333)
   
   print(444)
   func()
   print(555)
   
   执行结果：
   444
   333
   555
   ```

   加入语法糖后：

   ```
   def wrapper(f):
       def inner(*args,**kwargs):
           print(111)
           r = f(*args,**kwargs)
           print(222)
           return r
       return inner
   
   @wrapper
   def func():
       print(333)
   
   print(444)
   func()
   print(555)
   
   执行结果：
   444
   111
   333
   222
   555
   ```

   

4. 编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码’。

   ```
   def wrapper(f):
       def inner(*args,**kwargs):
           print('每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码')
           r = f(*args,**kwargs)
           return r
       return inner
   
   @wrapper
   def func():
   	pass
   
   func()
   ```

   

5. 为函数写一个装饰器，把函数的返回值 +100 然后再返回。

   ```python
   def wrapper(f):
       def inner(*args, **kwargs):
           r = f(*args, **kwargs)
           return r + 100
       return inner
       
   @wrapper
   def func():
       return 7
   
   result = func()
   print(result)
   
   执行结果：
   107
   ```

6. 请实现一个装饰器，通过一次调用使函数重复执行5次。

   示例1：

   ```python
   def wrapper(f):
       def inner(*args, **kwargs):
           for i in range(5):
               f(*args, **kwargs)
           return
       return inner
   
   @wrapper
   def func():
       print('函数执行了一次')
   
   func()
   
   执行结果：
   函数执行了一次
   函数执行了一次
   函数执行了一次
   函数执行了一次
   函数执行了一次
   ```

   示例2：

   ```python
   def wrapper(f):
       def inner(*args, **kwargs):
           r = []
           for i in range(5):
               r.append(f(*args, **kwargs))
           return r
       return inner
   
   @wrapper
   def func():
       return(1)
   
   print(func())
   
   执行结果：
   [1, 1, 1, 1, 1]
   ```

7. 请实现一个装饰器，每次调用函数时，将函数名以及调用此函数的时间节点写入文件中。

   ```
   可用代码：
   import time
   struct_time = time.localtime()
   print(time.strftime("%Y-%m-%d %H:%M:%S",struct_time)) # 当前时间节点
   
   def wrapper():
       pass
   def func1(f):
       print(f.__name__)
   func1(wrapper)
   函数名通过： 函数名.__name__获取。
   ```

```python
import time

def wrapper(f):
    def inner(*args, **kwargs):
        write_name = f.__name__
        write_time = f(*args, **kwargs)
        with open('log.txt', encoding='utf-8', mode='a')as f1:
            line = f'{time.strftime("%Y-%m-%d %H:%M:%S", write_time)}\t{write_name}\n'
            f1.write(line)
        return
    return inner

@wrapper
def func():
    struct_time = time.localtime()
    return struct_time

func()

    
写入文件：
2019-05-16 20:36:02	func
2019-05-16 20:36:02	func
2019-05-16 20:36:03	func
2019-05-16 20:36:04	func
```