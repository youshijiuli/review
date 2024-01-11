# day11作业（张珵）

1. 请写出下列代码的执行结果：﻿
   例一：

```
def func1():
	print('in func1')
def func2():
	print('in func2')
ret = func1
ret()
ret1 = func2
ret1()
ret2 = ret
ret3 = ret2
ret2()
ret3()

执行结果：
in func1
in func2
in func1
in func1
```

​	例二：

```
def func1():
	print('in func1')
def func2():
	print('in func2')
def func3(x,y):
	x()
	print('in func3')
	y()
print(111)
func3(func2,func1)
print(222)

执行结果：
111
in func2
in func3
in func1
222
```

​	例三（选做题）：

```
def func1():
	print('in func1')
def func2(x):
	print('in func2')
	return x
def func3(y):
	print('in func3')
	return y
ret = func2(func1)
ret()
ret2 = func3(func2)
ret3 = ret2(func1)
ret3()

执行结果：
in func2
in func1
in func3
in func2
in func1

注释：
ret=func1
ret2=func2
ret3=func2(func1)=func1
```

1. 看代码写结果：

   ```
   def func(arg):
       return arg.replace('苍老师', '***')
   def run():
       msg = "Alex的女朋友苍老师和大家都是好朋友"
       result = func(msg)
       print(result)
   run()
   
   执行结果：Alex的女朋友***和大家都是好朋友
   ```

   ```
   def func(arg):
       return arg.replace('苍老师', '***')
   def run():
       msg = "Alex的女朋友苍老师和大家都是好朋友"
       result = func(msg)
       print(result)
   data = run()
   print(data)
   
   执行结果：
   Alex的女朋友***和大家都是好朋友
   None
   ```

2. 看代码写结果：

   ```
   DATA_LIST = []
   def func(arg):
       return DATA_LIST.insert(0, arg)
   data = func('绕不死你')
   print(data)
   print(DATA_LIST)
   
   执行结果：
   None
   ['绕不死你']
   
   注释：insert语句无返回值，所以data是None
   ```

3. 看代码写结果：

   ```
   def func():
       print('你好呀')
       return '好你妹呀'
   
   
   func_list = [func, func, func]
   
   for item in func_list:
       val = item()
       print(val)
       
   执行结果：
   你好呀
   好你妹呀
   你好呀
   好你妹呀
   你好呀
   好你妹呀
   ```

4. 看代码写结果：

```
def func():
    print('你好呀')
    return '好你妹呀'
func_list = [func, func, func]
for i in range(len(func_list)):
    val = func_list[i]()
    print(val)

执行结果：
你好呀
好你妹呀
你好呀
好你妹呀
你好呀
好你妹呀
```

1. 看代码写结果：

```
def func():
    return '烧饼'
def bar():
    return '豆饼'
def base(a1, a2):
    return a1() + a2()
result = base(func, bar)
print(result)

执行结果：
烧饼豆饼
```

1. 看代码写结果：

```
for item in range(10):
    print(item)
    
print(item)
0
1
2
3
4
5
6
7
8
9
```

1. 看代码写结果：

```
def func():
    for item in range(10):
        pass
    print(item)
func()

执行结果：9
```

1. 看代码写结果：

```
item = '老男孩'
def func():
    item = 'alex'
    def inner():
        print(item)
    for item in range(10):
        pass
    inner()
func()

执行结果：9
```

1. 看代码写结果：

```
l1 = []
def func(args):
    l1.append(args)
    return l1
print(func(1))
print(func(2))
print(func(3))

执行结果：
[1]
[1,2]
[1,2,3]
```

1. 看代码写结果：

```
name = '太白'
def func():
    global name
    name = '男神'
print(name)
func()
print(name)

执行结果：
太白
男神
```

1. 看代码写结果：

```
name = '太白'
def func():
    print(name)
func()

执行结果：
太白
```

1. 看代码写结果：

```
name = '太白'
def func():
    print(name)
    name = 'alex'
func()

执行结果：报错
```

1. 看代码写结果：

```
def func():
    count = 1
    def inner():
        nonlocal count
        count += 1
        print(count)
    print(count)
    inner()
    print(count)
func()

执行结果：
1
2
2
```

1. 看代码写结果：

```
def extendList(val,list=[]):
	list.append(val)
	return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print('list1=%s'%list1)
print('list2=%s'%list2)
print('list3=%s'%list3)

执行结果：
list1=[10,'a']
list2=[123]
list3=[10,'a']
```

1. 看代码写结果：

```
def extendList(val,list=[]):
	list.append(val)
	return list
print('list1=%s'% extendList(10))
print('list2=%s'% extendList(123,[]))
print('list3=%s'% extendList('a'))
```

1. 用你的理解解释一下什么是可迭代对象，什么是迭代器。

   可迭代对象就是一个可以重复取值的实实在在的东西。

   迭代器是一个可以迭代取值的工具。

   

2. 如何判断该对象是否是可迭代对象或者迭代器？

   若该对象内部含有`__iter__`方法，则是可迭代对象。

   若该对象内部含有`__iter__`方法并且含有`__next__`方法。

   

3. 写代码：用while循环模拟for内部的循环机制（**面试题**）。

   ```
   s='a,b,c'
   obj = iter(s)
   while 1:
       try:
           print(next(obj))
       except StopIteration:
           break
           
   执行结果：
   a
   ,
   b
   ,
   c
   ```

   

4. 写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}﻿
   ﻿例如:min_max(2,5,7,8,4) 返回:{‘max’:8,’min’:2}(此题用到max(),min()内置函数)

   ```
   def min_max(*args):
       d={'max':max(args),'min':min(args)}
       return d
   print(min_max(1,2,3,4,5))
   
   输出结果：
   {'max': 5, 'min': 1}
   ```

5. 写函数，传入一个参数n，返回n的阶乘﻿
   ﻿例如:cal(7) 计算7*6*5*4*3*2*1

   ```
   def cal(n):
       p=1
       for i in range(1,n+1):
           p=p*i
       return p
   print(cal(7))
   
   执行结果：5040
   ```

6. 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组(**选做题**)﻿
   ﻿例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃’，‘A’)]

   **顺序排列法：**
   
   ```
   def poker():
       color=['红心','草花','方片','黑桃']
       num=[i for i in range(2,11)]+list('JQKA')
       result_list=[]
       for j in num:
           for i in color:
               result.append((i,j))
       print(result_list)
   poker()
   
   执行结果：[('红心', 2), ('草花', 2), ('方片', 2), ('黑桃', 2), ('红心', 3), ('草花', 3), ('方片', 3), ('黑桃', 3), ('红心', 4), ('草花', 4), ('方片', 4), ('黑桃', 4), ('红心', 5), ('草花', 5), ('方片', 5), ('黑桃', 5), ('红心', 6), ('草花', 6), ('方片', 6), ('黑桃', 6), ('红心', 7), ('草花', 7), ('方片', 7), ('黑桃', 7), ('红心', 8), ('草花', 8), ('方片', 8), ('黑桃', 8), ('红心', 9), ('草花', 9), ('方片', 9), ('黑桃', 9), ('红心', 10), ('草花', 10), ('方片', 10), ('黑桃', 10), ('红心', 'J'), ('草花', 'J'), ('方片', 'J'), ('黑桃', 'J'), ('红心', 'Q'), ('草花', 'Q'), ('方片', 'Q'), ('黑桃', 'Q'), ('红心', 'K'), ('草花', 'K'), ('方片', 'K'), ('黑桃', 'K'), ('红心', 'A'), ('草花', 'A'), ('方片', 'A'), ('黑桃', 'A')]
   ```

   ﻿**随机排列法：**
   
   ```
   def poker():
       color=['红心','草花','方片','黑桃']
       num=[i for i in range(2,11)]+list('JQKA')
       card_set=set()
       for j in num:
           for i in color:
               card_set.add((i,j))
       card_list=list(card_set)
       print(card_list)
   poker()
   
   执行结果：
   [('红心', 8), ('黑桃', 'K'), ('方片', 10), ('黑桃', 3), ('黑桃', 10), ('红心', 4), ('方片', 'K'), ('方片', 6), ('方片', 'Q'), ('草花', 8), ('黑桃', 6), ('草花', 7), ('方片', 2), ('黑桃', 2), ('草花', 3), ('红心', 7), ('黑桃', 'A'), ('方片', 7), ('黑桃', 9), ('草花', 6), ('红心', 3), ('方片', 3), ('红心', 10), ('黑桃', 'J'), ('方片', 8), ('黑桃', 5), ('草花', 2), ('红心', 6), ('方片', 4), ('红心', 'Q'), ('草花', 'J'), ('黑桃', 8), ('草花', 5), ('红心', 2), ('红心', 'K'), ('草花', 10), ('方片', 9), ('红心', 'A'), ('黑桃', 4), ('草花', 'K'), ('红心', 9), ('方片', 'A'), ('方片', 5), ('方片', 'J'), ('草花', 'Q'), ('红心', 'J'), ('草花', 4), ('红心', 5), ('草花', 9), ('草花', 'A'), ('黑桃', 7), ('黑桃', 'Q')]
   ```
   
   



1. 写代码完成99乘法表.(**选做题，面试题**)

1 * 1 = 1

2 * 1 = 2 2 * 2 = 4

3 * 1 = 3 3 * 2 = 6 3 * 3 = 9

......

9 * 1 = 9 9 * 2 = 18 9 * 3 = 27 9 * 4 = 36 9 * 5 = 45 9 * 6 = 54 9 * 7 = 63 9 * 8 = 72 9 * 9 = 81

```
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i} * {j} = {i*j}', end='')
        if i==j:
            print('')
        else:
            print(' ',end='')

执行结果：
1 * 1 = 1
2 * 1 = 2 2 * 2 = 4
3 * 1 = 3 3 * 2 = 6 3 * 3 = 9
4 * 1 = 4 4 * 2 = 8 4 * 3 = 12 4 * 4 = 16
5 * 1 = 5 5 * 2 = 10 5 * 3 = 15 5 * 4 = 20 5 * 5 = 25
6 * 1 = 6 6 * 2 = 12 6 * 3 = 18 6 * 4 = 24 6 * 5 = 30 6 * 6 = 36
7 * 1 = 7 7 * 2 = 14 7 * 3 = 21 7 * 4 = 28 7 * 5 = 35 7 * 6 = 42 7 * 7 = 49
8 * 1 = 8 8 * 2 = 16 8 * 3 = 24 8 * 4 = 32 8 * 5 = 40 8 * 6 = 48 8 * 7 = 56 8 * 8 = 64
9 * 1 = 9 9 * 2 = 18 9 * 3 = 27 9 * 4 = 36 9 * 5 = 45 9 * 6 = 54 9 * 7 = 63 9 * 8 = 72 9 * 9 = 81
```