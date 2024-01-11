# day25作业

**1.面向对象中为什么要有继承?**

当两个类中有相同或相似的静态变量或绑定方法时，使用继承可以减少代码的重用，提高代码可读性，规范编程模式



**2.Python继承时，查找成员的顺序遵循什么规则?**

Python2中的经典类遵循深度优先规则，Python2和Python3中的新式类遵循广度优先规则



**3.看代码写结果**

```
class Base1:
    def f1(self):
        print('base1.f1')

    def f2(self):
        print('base1.f2')

    def f3(self):
        print('base1.f3')
        self.f1()


class Base2:
    def f1(self):
        print('base2.f1')


class Foo(Base1, Base2):
    def f0(self):
        print('foo.f0')
        self.f3()


obj = Foo()
obj.f0()

执行结果：
foo.f0
base1.f3
base1.f1

解释：
先搜索并执行Foo自己的f0
然后搜索Foo自己的f3，没找到。由于继承顺序是先Base1再Base2，因此先找Base1，找到了，于是执行Base1的f3。
然后搜索Foo自己的f1，没找到，找Base1，找到了，遂执行之
```
**4.看代码写结果**

```
class Base:
    def f1(self):
        print('base.f1')

    def f3(self):
        self.f1()
        print('base.f3')


class Foo(Base):
    def f1(self):
        print('foo.f1')

    def f2(self):
        print('foo.f2')
        self.f3()

obj = Foo()
obj.f2()

执行结果：
foo.f2
foo.f1
base.f3

解释：
先搜索Foo自己的f2，找到了，执行之，打印'foo.f2'。
然后搜索Foo自己的f3，没找到，找Base的，找到了...
然后搜索Foo自己的f1，找到了，打印'foo.f1'
然后回到Base的f3，打印'base.f3'
```
**5.补充代码实现下列需求**

```
#这个代码框里是题干
user_list = []  
while True: 
	user = input(“请输入用户名:”)  
	pwd = input(“请输入密码:”)  
	email = input(“请输入邮箱:”) 
    
"""
# 需求
1. while循环提示用户输 : 户名、密码、邮箱(正则满足邮箱格式)
2. 为每个用户创建1个对象，并添加到列表中。
3. 当列表中的添加 3个对象后，跳出循环并以此循环打印所有用户的姓名和邮箱
"""
```
```python
#这个代码框里是答案

import re

class User(object):
    user_list = []
    def __init__(self,u,p,e):
        self.username=u
        self.pwd=p
        self.email=e

while True:

    while True:
        username = input('请输入用户名:').strip()
        for i in User.user_list:
            if username == i.username:
                print('该用户名已存在，请重新输入！')
                break
        else:
            break

    pwd = input('请输入密码:').strip()

    while True:
        email = input('请输入邮箱:').strip()
        if re.search(r'^[-\w.]+@([-\da-zA-Z]+[.])+[\da-zA-Z]{2,6}$',email):
            for i in User.user_list:
                if email == i.email:
                    print('该邮箱已存在，请重新输入！')
                    break
            else:
                break
        else:
            print('您输入的邮箱格式错误，请重新输入！')

    User.user_list.append(User(username,pwd,email))
    print(f'用户{username}添加成功！')
    if len(User.user_list)==3:
        print('姓名','邮箱')
        for i in User.user_list:
            print(i.username,i.email)
        break
        
执行结果：
请输入用户名:aaa
请输入密码:123456
请输入邮箱:aaa@163.com
用户aaa添加成功！
请输入用户名:aaa
该用户名已存在，请重新输入！
请输入用户名:bbb
请输入密码:123456
请输入邮箱:123456
您输入的邮箱格式错误，请重新输入！
请输入邮箱:bbb@163.com
用户bbb添加成功！
请输入用户名:ccc
请输入密码:123456
请输入邮箱:ccc@163.com
用户ccc添加成功！
姓名 邮箱
aaa aaa@163.com
bbb bbb@163.com
ccc ccc@163.com
```

**6.补充代码，实现用户登录和注册（第一个代码框是题干，第二个代码框是答案）**

```
#这个代码框里是题干
class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd


class Account:
    def __init__(self):
        # 用户列表，数据格式：[user对象，user对象，user对象]
        self.user_list = []

    def login(self):
        """
        用户登录，输入用户名和密码然后去self.user_list中校验用户合法性
        :return:
        """
        pass

    def register(self):
        """
        用户注册，没注册一个用户就创建一个user对象，然后添加到self.user_list中，表示注册成功。
        :return:
        """
        pass

    def run(self):
        """
        主程序
        :return:
        """
        pass


if __name__ == '__main__':
    obj = Account()
    obj.run()
```
```python
# 这个代码框里是答案（已整合老师的标准答案）
class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

class Account:
    def __init__(self):
        # 用户列表，数据格式：[user对象，user对象，user对象]
        self.user_list = []

    def login(self):
        """
        用户登录，输入用户名和密码然后去self.user_list中校验用户合法性
        :return:
        """
        name = input('请输入用户名:').strip()
        pwd = input('请输入密码:').strip()
        for i in self.user_list:
            if name == i.name and pwd == i.pwd:
                print(f'用户{name}登陆成功！')
                break
        else:
            print('用户名或密码输入错误，登陆失败！')

    def register(self):
        """
        用户注册，每注册一个用户就创建一个user对象，然后添加到self.user_list中，表示注册成功。
        :return:
        """
        while True:
            name = input('请输入用户名:').strip()
            for i in self.user_list:
                if name == i.name:
                    print('该用户名已存在，请重新输入！')
                    break
            else:
                break

        #注册的时候需要输入两遍密码
        while True:
            pwd = input('请输入密码:').strip()
            pwd2 = input('请再次输入密码:').strip()
            if pwd == pwd2:
                break
            else:
                print('两次输入的密码不一致，请重新输入')

        user = User(name, pwd)
        self.user_list.append(user)

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
    obj = Account()
    obj.run()
```

**6.5 将第6题的需求进行修改，不用列表了，改成读取本地文件**

```
见day26作业第3题
```

**7.读代码写结果**

```
class Base:
    x = 1
    
obj = Base()

print(obj.x)
obj.y = 123
print(obj.y)
obj.x = 123
print(obj.x)
print(Base.x)

执行结果：
1
123
123
1
第一个，先在obj中找x，没找到，然后去Base里找x，找到了，x=1
obj.x = 123相当于在obj的命名空间中新建了一个x，值为123，它对Base中的x=1没有影响，所以第三个是123，第四个是1
```
8.**读代码写结果**

```
class Parent:
    x = 1
    
class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(Parent.x,Child1.x,Child2.x)
Child2.x = 2
print(Parent.x,Child1.x,Child2.x) 
Child1.x = 3
print(Parent.x,Child1.x,Child2.x)

执行结果：
1 1 1
1 1 2
1 3 2
```
9.**看代码写结果**

```
class Foo(object):
    n1 = '武沛齐'
    n2 = '金老板'
    def __init__(self):
        self.n1 = 'eva'

obj = Foo()
print(obj.n1)
print(obj.n2)

执行结果：
eva
金老板

解释：__init__中的n1是对象obj自己名称空间中的，因此print(obj.n1)时会优先从这里找，所以是'eva'。之后，由于obj自己名称空间中没有n2，会去父类Foo中找，所以第二个输出'金老板'
```
**10.看代码写结果，如果有错误，则标注错误即可，并且假设程序报错可以继续执行**

```
class Foo(object):
    n1 = '武沛齐'
    def __init__(self,name):
        self.n2 = name
obj = Foo('太白')
print(obj.n1)
print(obj.n2)
print(Foo.n1)
print(Foo.n2)

执行结果：
武沛齐
太白
武沛齐
报错（类中没有“对象指针”，不能从类向对象中找）
```