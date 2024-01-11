# day22作业

# 二分查找：给定由小到大排列的有序列表，和待搜索元素值，返回索引号

```
#方法一：给定索引上下限，逐步迭代更新上下限，当x不是l的元素时会提示'指定的元素不存在!'
def func(l,x):
    a=0         #索引下限
    b=len(l)-1  #索引上限
    while 1:
        n=int((a+b)/2)
        if l[n]==x:
            return n
        elif a==b:
            return '指定的元素不存在!'
        elif l[n]>x:
            b=n
        elif l[n]<x:
            a=n+1
l=[10,12,16,24,25,36,37,48,59]
x=24
print(func(l,x))
```



```
#方法二：逐步从l中点切分给定列表l，当x超出边界值时给出提示'指定的元素不存在!'
def func(l,x):
    s=0     #用于每次截取列表时，保存累计索引号
    while 1:
        n=int(len(l)/2)
        if x<l[0] or x>l[len(l)-1]:
            return '指定的元素不存在!'
        elif l[n]==x:
            return n+s
        elif l[n]>x:
            l=l[:n]
        elif l[n]<x:
            l=l[n+1:]
            s+=n+1
l=[10,12,16,24,25,36,37,48,59]
x=24
print(func(l,x))
```



# **sys.argv练习**

写一个python脚本,在cmd里执行：
python xxx.py 用户名 密码 cp 文件路径 目的地址
python xxx.py alex sb cp D:\python_22\day22\1.内容回顾.py D:\python_22\day21【将一个已存在的文件复制到一个已存在的文件夹】
python xxx.py alex sb rm D:\python_22\day22
python xxx.py alex sb rename D:\python_22\day22  D:\python_22\day23

```python
# 已整合老师的标准答案并增加mv、mkdir模式
# 注意sys.argv[]索引号是从0开始的

import sys
import os
import shutil

if len(sys.argv) >= 5:
    if sys.argv[1] == 'oddgod' and sys.argv[2] == '123':
        # cp：将一个文件复制到一个已存在的文件夹，注意若文件夹不存在则不能直接copy2，否则报错！
        if sys.argv[3] == 'cp' and len(sys.argv) == 6:
            if os.path.exists(sys.argv[4]) and os.path.exists(sys.argv[5]):
                path = os.path.join(sys.argv[5], os.path.basename(sys.argv[4]))
                shutil.copy2(sys.argv[4], path)
        # rm：删除一个文件或文件夹
        elif sys.argv[3] == 'rm' and len(sys.argv) == 5:
            if os.path.exists(sys.argv[4]):
                if os.path.isfile(sys.argv[4]):
                    os.remove(sys.argv[4])
                else:
                    shutil.rmtree(sys.argv[4])
        # rn：将一个文件或文件夹重命名
        elif sys.argv[3] == 'rn' and len(sys.argv) == 6:
            if os.path.exists(sys.argv[4]):
                os.rename(sys.argv[4], sys.argv[5])
        # mv：将一个文件移动到一个已存在的文件夹
        elif sys.argv[3] == 'mv' and len(sys.argv) == 6:
            if os.path.exists(sys.argv[4]) and os.path.exists(sys.argv[5]):
                path = os.path.join(sys.argv[5], os.path.basename(sys.argv[4]))
                shutil.move(sys.argv[4], path, copy_function=shutil.copy2)
        # mkdir：新建一个文件夹
        elif sys.argv[3] == 'mkdir' and len(sys.argv) == 5:
            if not os.path.exists(sys.argv[4]):
                os.mkdir(sys.argv[4])
        else:
            print('输入错误！')
    else:
        print('用户名或密码错误！')
else:
    print('您输入的命令长度不足')

```

![作业cmd截图](D:\老男孩\day022\作业cmd截图.png)



# 使用walk来计算文件夹的总大小

```
import os
g = os.walk('D:\软件')
s=0
for i in g :
    path,dir_list,name_list = i
    for j in name_list:
        s+=os.path.getsize(os.path.join(path,j))
print(f'该文件夹大小为：{s/1024**2}MB')
```



**定义一个圆形类,半径是这个圆形的属性,实例化一个半径为5的圆形,一个半径为10的圆形**
**完成方法**
**计算圆形面积**
**计算圆形周长**

```
class Circle:
    def __init__(self, x):
        self.radius = x
    def area(self):
        return 3.1415926*self.radius**2
    def perimeter(self):
        return 2*3.1415926*self.radius

a = Circle(5)
b = Circle(10)

print(a.area())
print(a.perimeter())
print(b.area())
print(b.perimeter())

执行结果：
78.539815
31.415926
314.15926
62.831852
```



**定义一个用户类,用户名和密码是这个类的属性,实例化两个用户,分别有不同的用户名和密码**
**登陆成功之后才创建用户对象**
**设计一个方法 修改密码**

```python
#老师官方答案，因为是先login再实例化，所以login是一个跟类无关的独立函数
import os

def login(n,p,filepath = 'userinfo'):
    with open(filepath,encoding='utf-8') as f:
        for line in f:
            username,password = line.strip().split('|')
            if username == n and password == p:
                return True
        else:
            return False

class User(object):

    def __init__(self,u,p):
        self.user = u
        self.pwd = p

    def change_pwd(self):
        oldpwd = input('输入原密码 :')
        newpwd = input('输入新密码 :')
        flag = False
        with open('userinfo',encoding='utf-8') as f1,open('userinfo.bak',mode='w',encoding='utf-8') as f2:
            for line in f1:
                username,password = line.strip().split('|')
                if username == self.user and password == oldpwd:
                    line = f'{username}|{newpwd}\n'
                    flag = True
                f2.write(line)
        os.remove('userinfo')
        os.rename('userinfo.bak','userinfo')
        return flag

username = input('请输入用户名：')
password = input('请输入密码')

if login(username,password):
    print('登录成功')
    obj = User(username,password)
    if obj.change_pwd():
        print('修改成功')
    else:
        print('修改失败')
else:
    print('用户名或密码错误，登陆失败')
```