1. # Authentic类的反射练习

```
class Authentic:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def register(self):
        pass
    def login(self):
        pass

l = [('登录','login'),('注册','register')]
# 循环这个列表
# 显示 序号 用户要做的操作
# 用户输入序号
# 你通过序号找到对应的login或者register方法
# 先实例化
```

```python
class Authentic:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def register(self):
        print('注册')		#注：本题主要为了练习反射，所以注册和登陆方法略写了，注册和登陆的代码详见今日第三题
    def login(self):
        print('登陆')
l = [('登陆','login'),('注册','register')]
a=Authentic('tom',18)
for i in range(len(l)):
    print(i+1,l[i][0])
while 1:
    choice=input('请输入您的选项序号>>>').strip()
    if not choice.isdecimal():
        print('您输入的数字格式错误，请重新输入！')
        continue
    choice = int(choice)
    if choice<1 or choice>len(l):
        print('您输入的数字超出范围，请重新输入！')
        continue
    if hasattr(a,l[choice-1][1]):
        if callable(getattr(a,l[choice-1][1])):
            getattr(a, l[choice - 1][1])()

执行结果1：
1 登陆
2 注册
请输入您的选项序号>>>1
登陆

执行结果2：
1 登陆
2 注册
请输入您的选项序号>>>2
注册
```

# 2.按照要求完成：

```
class User:
    def __init__(self,name,age,sex):
        self.name = name
        self.age  = age
        self.sex  = sex
    def eat(self):
        pass
    def sleep(self):
        pass

# 用户输入姓名、年龄、性别
# 实例化对象
# 用户任意输入内容 : 不能用异常处理
    # 如果输入的是属性名 打印属性值
    # 如果输入的是方法名 调用fangfa
    # 如果输入的什么都不是 不做操作
```

```python
class User:
    def __init__(self,name,age,sex):
        self.name = name
        self.age  = age
        self.sex  = sex
    def eat(self):
        print('正在吃')
    def sleep(self):
        print('正在睡')

name=input('请输入姓名：').strip()
age=input('请输入年龄：').strip()
sex=input('请输入性别：').strip()
user=User(name,age,sex)
while 1:
    command=input('请输入任意内容：').strip()
    if hasattr(user,command):
        if callable(getattr(user,command)):
            getattr(user, command)()			#如果是方法
        else:
            print(getattr(user,command))		#如果是属性
            
执行结果：
请输入姓名：tom
请输入年龄：8
请输入性别：male
请输入任意内容：name
tom
请输入任意内容：sex
male
请输入任意内容：age
8
请输入任意内容：eat
正在吃
请输入任意内容：sleep
正在睡
请输入任意内容：hahaha
请输入任意内容：
```

# 3.注册之后,重启所有的用户丢失,一次执行的注册行为,在之后所有执行中都能够正常登录,两个登录程序和面向对象的内容整理在一起,两个都要明白,都要记住

```python
import pickle
import os

class User(object):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

class Mypickle(object):
    def __init__(self,path):
        self.file = path
    def dump(self,obj):
        with open(self.file, 'ab') as f:
            pickle.dump(obj, f)
    def load(self):
        with open(self.file,'rb') as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break

class Account(object):
    def __init__(self):
        # 用户列表，数据格式：[user对象，user对象，user对象]
        self.path = 'data'

    def login(self):
        """
        用户登录，输入用户名和密码然后读取pickle文件校验用户合法性
        :return:
        """
        name = input('请输入用户名:').strip()
        pwd = input('请输入密码:').strip()

        for i in p.load():
            if name == i.name and pwd == i.pwd:
                print(f'用户{name}登陆成功！')
                break
        else:
            print('用户名或密码输入错误，登陆失败！')

    def register(self):
        """
        用户注册，每注册一个用户就创建一个user对象，然后将user对象写入pickle文件中，表示注册成功。
        :return:
        """
        name = input('请输入用户名:').strip()

        #注册的时候需要输入两遍密码
        while True:
            pwd = input('请输入密码:').strip()
            pwd2 = input('请再次输入密码:').strip()
            if pwd == pwd2:
                break
            else:
                print('两次输入的密码不一致，请重新输入')

        if os.path.isfile(path):
            for i in p.load():
                if name == i.name:
                    print('注册失败，该用户名已存在！')
                    break
            else:
                p.dump(User(name, pwd))
                print(f'用户{name}注册成功！')
        else:
            p.dump(User(name, pwd))
            print(f'用户{name}注册成功！')

    def run(self):
        """
        主程序
        :return:
        """

        option_list = ['注册', '登录', '退出']
        while True:
            for index, item in enumerate(option_list,1):
                print(index, item)
            choice = input('请输入您的选项>>>').strip()
            if choice == '1':
                self.register()
            elif choice == '2':
                self.login()
            elif choice == '3':
                return
            else:
                print('您输入的选项有误，请重新输入！')

if __name__ == '__main__':
    path='my_pickle_data'
    p = Mypickle(path)
    obj = Account()
    obj.run()
```

```
执行结果：
1 注册
2 登录
3 退出
请输入您的选项>>>1
请输入用户名:tom
请输入密码:123
请再次输入密码:123
用户tom注册成功！
1 注册
2 登录
3 退出
请输入您的选项>>>1
请输入用户名:jerry
请输入密码:123
请再次输入密码:456
两次输入的密码不一致，请重新输入
请输入密码:123
请再次输入密码:123
用户jerry注册成功！
1 注册
2 登录
3 退出
请输入您的选项>>>2
请输入用户名:tom
请输入密码:123
用户tom登陆成功！
1 注册
2 登录
3 退出
请输入您的选项>>>2
请输入用户名:jerry
请输入密码:456
用户名或密码输入错误，登陆失败！
1 注册
2 登录
3 退出
请输入您的选项>>>
```

# 4.写一个自定义模块,里面有你自己实现的mypickle和myjson,我只需要给你传递一个参数 'pickle'还是'json'【归一化设计】

```
【my_module.py】

import pickle
import json

class Mypickle(object):
    def __init__(self, pt):
        self.path = pt
    def dump(self,obj):
        with open(self.path, 'ab') as f:
            pickle.dump(obj, f)
    def load(self):
        with open(self.path,'rb') as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break

class Myjson(object):
    def __init__(self, pt):
        self.path = pt
    def dumps(self,x):
        with open(self.path, encoding='utf-8', mode='a') as f:
            f.write(json.dumps(x) + '\n')
    def loads(self):
        with open(self.path, encoding='utf-8') as f:
            for line in f:
                yield json.loads(line)

def serialization(method,path='my_serialization_file'):
    if method == 'pickle':
        return Mypickle(path)
    elif method=='json':
        return Myjson(path)
    else:
        print('输入的方法有误！')
```

```
【当前脚本：pickle的情况】

import my_module

s=my_module.serialization('pickle')
x=(1,2,3)
y='hello world'
s.dump(x)
s.dump(y)
for i in s.load():
    print(i)
    
执行结果：
(1, 2, 3)
hello world
```

```
【当前脚本：json的情况】

import my_module

s=my_module.serialization('json')
x=(1,2,3)
y='hello world'
s.dumps(x)
s.dumps(y)
for i in s.loads():
    print(i)

执行结果：
[1, 2, 3]
hello world
```

