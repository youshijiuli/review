## day10 作业(张珵)

1. 写函数，函数可以支持接收任意数字（位置传参）并将所有数据相加并返回。

   ```
   def func(*args):
       sum=0
       for i in args:
           sum+=i
       return sum
   print(func(1,2,3,4,5,6,7,8,9,10))
   
   输出结果：55
   ```

   

2. 看代码写结果

   ```
   def func():
       return 1,2,3
   val = func()
   print( type(val) == tuple )
   print( type(val) == list )
   
   输出结果：
   True
   False
   python以元组形式返回函数的多个返回值
   ```

3. 看代码写结果

   ```
   def func(*args,**kwargs):
       pass
   
   # a. 请将执行函数，并实现让args的值为 (1,2,3,4)
   func(1,2,3,4)或func(*[1,2,3,4])
   
   # b. 请将执行函数，并实现让args的值为 ([1,2,3,4],[11,22,33])
   func([1,2,3,4],[11,22,33])
   
   # c. 请将执行函数，并实现让args的值为 ([11,22],33) 且 kwargs的值为{'k1':'v1','k2':'v2'}
   func([11,22],33,k1='v1',k2='v2')
   #注意k1、k2没有''
   
   # d. 如执行 func(*{'武沛齐','金鑫','女神'})，请问 args和kwargs的值分别是？
   func('武沛齐','金鑫','女神')
   args=('武沛齐','金鑫','女神')
   kwargs={}
   
   # e. 如执行 func({'武沛齐','金鑫','女神'},[11,22,33])，请问 args和kwargs的值分别是？
   args=({'武沛齐','金鑫','女神'},[11,22,33])
   kwargs={}
   
   # f. 如执行 func('武沛齐','金鑫','女神',[11,22,33],**{'k1':'栈'})，请问 args和kwargs的值分别是？
   func('武沛齐','金鑫','女神',[11,22,33],k1='栈')
   args=('武沛齐','金鑫','女神',[11,22,33])
   kwargs={'k1':'栈'}
   ```

4. 看代码写结果

   ```
   def func(name,age=19,email='123@qq.com'):
       pass
   
   # a. 执行 func('alex') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
   可以
   name='alex'
   age=19
   email='123@qq.com'
   
   # b. 执行 func('alex',20) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
   可以
   name='alex'
   age=20
   email='123@qq.com'
   
   # c. 执行 func('alex',20,30) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
   可以
   name='alex'
   age=20
   email=30
   
   # d. 执行 func('alex',email='x@qq.com') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
   可以
   name='alex'
   age=19
   email='x@qq.com'
   
   # e. 执行 func('alex',email='x@qq.com',age=99) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
   可以
   name='alex'
   age=99
   email='x@qq.com'
   
   # f. 执行 func(name='alex',99) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
   不可以
   关键字参数不能在位置参数之前
   
   # g. 执行 func(name='alex',99,'111@qq.com') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
   不可以
   关键字参数不能在位置参数之前
   ```

5. 看代码写结果

   ```
   def func(users,name):
   	users.append(name)
       return users
   
   result = func(['武沛齐','李杰'],'alex')
   print(result)
   
   输出结果：
   ['武沛齐','李杰','alex']
   ```

6. 看代码写结果

   ```
   def func(v1):
       return v1* 2
   
   def bar(arg):
       return "%s 是什么玩意？" %(arg,)
   
   val = func('你')	
   data = bar(val)
   print(data)
   
   输出结果：
   你你 是什么玩意？
   ```

   val='你你'

   

7. 看代码写结果

   ```
   def func(v1):
       return v1* 2
   
   def bar(arg):
       msg = "%s 是什么玩意？" %(arg,)
       print(msg) 
   
   val = func('你')
   data = bar(val)
   print(data)
   
   输出结果：
   你你 是什么玩意？
   None
   ```

8. 看代码写结果

   ```
   v1 = '武沛齐'
   
   def func():
       print(v1)
       
   func()
   v1 = '老男人'
   func()
   
   输出结果：
   武沛齐
   老男人
   ```

9. 看代码写结果

   ```
   v1 = '武沛齐'
   
   def func():
       v1 = '景女神'
       def inner():
           print(v1)
       v1 = '肖大侠'
       inner()
   func()
   v1 = '老男人'
   func()
   
   输出结果：
   肖大侠
   肖大侠
   ```

10. 看代码写结果【可选】

    ```
    def func():
        data = 2*2
        return data
    
    new_name = func
    val = new_name()
    print(val)
    
    # 注意：函数类似于变量，func代指一块代码的内存地址。
    
    输出结果：4
    ```

11. 看代码写结果【可选】

    ```
    def func():
        data = 2*2
        return data
    
    data_list = [func,func,func]
    for item in data_list:
        v = item()
        print(v)
    
    # 注意：函数类似于变量，func代指一块代码的内存地址。
    
    输出结果：
    4
    4
    4
    ```

12. 看代码写结果（函数可以做参数进行传递）【可选】

    ```
    def func(arg):
        arg()
        
    def show():
        print('show函数')
    
    func(show)
    
    输出结果：'show函数'
    ```

13. 写函数，接收n个数字，求这些参数数字的和。（动态传参）

```
def func(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(func(1,2,3,4,5,6,7,8,9,10))

输出结果：55
```



1. 读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？

```
a=10
b=20
def test5(a,b):
	print(a,b)
c = test5(b,a)
print(c)

输出结果：
20 10
None
c = test5(20,10)，因此在函数的局部空间内a=20、b=10。但是没有return所以c=None
```

1. 读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？

```
a=10
b=20
def test5(a,b):
	a=3
	b=5
	print(a,b)
c = test5(b,a)
print(c)

输出结果：
3 5
None
c=test5(20,10)，因此在函数的局部空间内a=20、b=10，但由于在函数的局部空间内又重新定义a=3、b=5，所以输出3、5。没有return所以c=None
```

1. 传入函数中多个列表和字典,如何将每个列表的每个元素依次添加到函数的动态参数args里面？如何将每个字典的所有键值对依次添加到kwargs里面？

   函数调用时，在每个列表左侧加*，在每个字典左侧加**

2. 写函数,接收两个数字参数,将较小的数字返回.

   ```
   def func(x,y):
       return x if x<y else y
   ```

3. 写函数,接收一个参数(此参数类型必须是可迭代对象),将可迭代对象的每个元素以’_’相连接,形成新的字符串,并返回.

   例如 传入的可迭代对象为[1,'老男孩','武sir']返回的结果为’1_老男孩_武sir’

   ```
   def func(x):
       for i in range(len(x)):
           x[i]=str(x[i])
       return '_'.join(x)
   print(func([1,'老男孩','武sir']))
   
   输出结果：
   1_老男孩_武sir
   注意：本题必须先将可迭代对象中的每个元素转换为str格式才能使用join()，否则报错！
   ```

   

19.有如下函数:

```
def wrapper():

	def inner():

		print(666)

 wrapper()
```

你可以任意添加代码,执行inner函数.

```
def wrapper():
	def inner():
		print(666)
	inner()
wrapper()

输出结果：666
```



1. 相关面试题：

写出下列代码结果：

```
def foo(a,b,*args,c,sex=None,**kwargs):

	print(a,b)

	print(c)

	print(sex)

	print(args)

	print(kwargs)



\# foo(1,2,3,4,c=6)
1 2
6
None
(3,4)
{}

\# foo(1,2,sex='男',name='alex',hobby='old_woman')
报错，因为未给c赋值


\# foo(1,2,3,4,name='alex',sex='男')
报错，因为未给c赋值


\# foo(1,2,c=18)
1 2
18
None
()
{}


\# foo(2, 3, [1, 2, 3],c=13,hobby='喝茶')
2 3
13
None
([1,2,3],)
{'hobby':'喝茶'}


\# foo(*[1, 2, 3, 4],**{'name':'太白','c':12,'sex':'女'})
先转化成foo(1,2,3,4,name='太白',c=12,sex='女')
1 2
12
女
(3,4)
{'name': '太白'}
```