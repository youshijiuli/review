## day13 作业(张珵)

1. 看代码分析结果

```
func_list = []

for i in range(10):
    func_list.append(lambda :i)

v1 = func_list[0]()
v2 = func_list[5]()
print(v1,v2)

执行结果：
9 9
注：func_list=[lambda :i,lambda :i...]=[i,i...]，函数执行时i=9
```

1. 看代码分析结果

```
func_list = []

for i in range(10):
    func_list.append(lambda x:x+i)

v1 = func_list[0](2)
v2 = func_list[5](1)
print(v1,v2)

执行结果：
11 10
注：与上题同理
```

1. 看代码分析结果

```
func_list = []

for i in range(10):
    func_list.append(lambda x:x+i)

for i in range(0,len(func_list)):
    result = func_list[i](i)
    print(result)
    
执行结果：
0,2,4...,16,18
注：函数执行时，i分别等于0,1,2...9

类比另一题：
func_list = []

for i in range(10):
    func_list.append(lambda x:x+i)

for j in range(0,len(func_list)):
    result = func_list[j](j)
    print(result)

执行结果：
9,10,11...17,18
注：函数执行时，i=9
```

1. 看代码写结果（面试题）：

```
def func(name):
    v = lambda x:x+name
    return v

v1 = func('太白')
v2 = func('alex')
v3 = v1('银角')
v4 = v2('金角')
print(v1,v2,v3,v4)

执行结果：
<function func.<locals>.<lambda> at 0x000000000246BBF8> <function func.<locals>.<lambda> at 0x000000000246BC80> 银角太白 金角alex
注：
v1=lambda x:x+'太白'
v2=lambda x:x+'alex'
v3='银角太白'
v4='金角alex'
```

1. 看代码写结果【面试题】

```
result = []
for i in range(10):			#i=0,1,2...9
    func = lambda : i
    result.append(func)		#result=[lambda :i,lambda: i...]一共十个元素

print(i)
print(result)
v1 = result[0]()
v2 = result[9]()
print(v1,v2)

执行结果：
9
[第1个函数地址、第2个函数地址...第10个函数地址]
9 9
```

1. 看代码分析结果【面试题】

```
def func(num):
    def inner():
        print(num)
    return inner

result = []
for i in range(10):
    f = func(i)
    result.append(f)

print(i)
print(result)
v1 = result[0]()
v2 = result[9]()
print(v1,v2)

执行结果：
9
[第1个inner函数地址、第2个inner函数地址……第10个inner函数地址]
0
9
None None
=============================================================
i=0
f=func(0)=inner
result=[inner]

i=1
f=func(1)=inner
result=[inner,inner]

...

i=9
f=func(9)=inner
result=[inner,inner...inner]（共10个）

print(i)=9
result=[inner,inner...inner]（共10个）
inner函数没有返回值，所以v1,v2都是None
【问】为什么v1是0？
【答】由于i是通过func的参数的形式传到num的，不可变类型对象传参只传值，因此传的时候是多少就是多少，不会随着i的更新而更新
```

1. 看代码写结果【新浪微博面试题】

   ```
   def func():
       for num in range(10):
           pass
       v4 = [lambda :num+10,lambda :num+100,lambda :num+100,]
       result1 = v4[1]()
       result2 = v4[2]()
       print(result1,result2)
   func()
   
   执行结果：
   109 109
   ```

2. 请编写一个函数实现将IP地址转换成一个整数。【面试题，较难,可以先做其他题】

   ```
   如 10.3.9.12 转换规则为二进制：
           10            00001010
            3            00000011
            9            00001001
           12            00001100
   再将以上二进制拼接起来计算十进制结果：00001010 00000011 00001001 00001100 = ？
   ```

   方法一：张珵——基于二进制数字与十进制数字的转化原理
   
   ```
   def func(ip10_str):
       def bin2int(x):
           y = str(x)
           power = len(y) - 1
           s = 0
           for i in y:
               s = s + int(i) * (2 ** power)
               power -= 1
           return s
       ip10_str_list=ip10_str.split('.')                   	 #['182','64','63','222']
       ip10_int_list=[int(x.strip()) for x in ip10_str_list]      		 #[182,64,63,222]
       ip2_str_list=['0'*(8-len(bin(x)[2:]))+bin(x)[2:] for x in ip10_int_list]
       								#['10110110', '01000000', '00111111', '11011110']
       num2_str=''.join(ip2_str_list)			      #'10110110010000000011111111011110'
       num2_int=int(num2_str)						    #10110110010000000011111111011110
       return(bin2int(num2_int))
   print(func('182.64.63.222'))
   
   执行结果：3057663966
   ```
   
   方法二：纳钦——基于`int(字符串,base=0)`
   
   ```
   ip = '182.64.63.222'
   l1 = ip.split('.')
   b_count = 0
   l2 = []
   b = '0b'
   for i in l1:
       a = bin(int(i))
       length = len(a) - 2
       b +='0' * (8 - length) + a[2:]
   print(b,type(b))
   print(int(b,base=0))
   
   执行结果：
   0b10110110010000000011111111011110 <class 'str'>
   3057663966
   ```
   
   









1. 都完成的做一下作业（下面题都是用内置函数或者和匿名函数结合做出）：

   1. 用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb

    name=[‘oldboy’,'alex','wusir']

   ```
   方法一：
   print([n+'_sb' for n in name])
   
   方法二：
   ret = map(lambda x:x+'_sb',name)
   print(list(ret))
   
   ```

```
执行结果：
   ['oldboy_sb', 'alex_sb', 'wusir_sb']
```


```
   

   
1. 用map来处理下述l，然后用list得到一个新的列表，列表中每个人的名字都是sb结尾
   
   l = [{'name':'alex'},{'name':'y'}]
   
```
```
   l = [{'name':'alex'},{'name':'y'}]
   ret = map(lambda x:x['name']+'sb',l)
   print(list(ret))

执行结果：
   ['alexsb', 'ysb']
```



```
     
   1. 用filter来处理,得到股票价格大于20的股票名字
   
```
       shares={
      	'IBM':36.6,
      	'Lenovo':23.2,
      	'oldboy':21.2,
      	'ocean':10.2,
      }
      ret=filter(lambda x:shares[x]>20,shares)
      print(list(ret))
       
      执行结果：['IBM', 'Lenovo', 'oldboy']
   ```
   

   
   1. 有下面字典，得到购买每只股票的总价格，并放在一个迭代器中结果：list一下[9110.0, 27161.0,......]
   
   ```


```
  portfolio = [
     {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}]

   方法一：
   ret=(i['shares']*i['price'] for i in portfolio )
   print(list(ret))

   方法二：
   ret=map(lambda x:x['shares']*x['price'],portfolio)
   print(list(ret))

   执行结果：[9110.0, 27161.0, 4218.0, 1111.25, 735.7500000000001, 8673.75]
```















1. 还是上面的字典，用filter过滤出单价大于100的股票。

```
  portfolio = [
     {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}]

   ret=filter(lambda x:x['price']>100,portfolio)
   print(list(ret))

   执行结果：[{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}]
```
















   1. 有下列三种数据类型，

```
 l1 = [1,2,3,4,5,6]

 l2 = ['oldboy','alex','wusir','太白','日天']

 tu = ('**','***','****','*******')
```


写代码，最终得到的是（每个元祖第一个元素>2,第三个*至少是4个。）

`[(3, 'wusir', '****'), (4, '太白', '*******')]`这样的数据。 

```
方法一：分着写
l1 = [1, 2, 3, 4, 5, 6]
l2 = ['oldboy', 'alex', 'wusir', '太白', '日天']
tu = ('**', '***', '****', '*******')
ret = zip(l1,l2,tu)
li=list(ret)
f=filter(lambda x:x[0]>2 and len(x[2])>=4,li)
print(list(f))

执行结果：[(3, 'wusir', '****'), (4, '太白', '*******')]
```

```
方法二：方法一，不对ret进行list，直接迭代（迭代器一定是可迭代对象）
l1 = [1, 2, 3, 4, 5, 6]
l2 = ['oldboy', 'alex', 'wusir', '太白', '日天']
tu = ('**', '***', '****', '*******')
ret = zip(l1,l2,tu)
f=filter(lambda x:x[0]>2 and len(x[2])>=4,ret)
print(list(f))

执行结果：[(3, 'wusir', '****'), (4, '太白', '*******')]
```

```
方法三：将方法二合起来写
l1 = [1, 2, 3, 4, 5, 6]
l2 = ['oldboy', 'alex', 'wusir', '太白', '日天']
tu = ('**', '***', '****', '*******')
print(list(filter(lambda x:x[0]>2 and len(x[2])>=4,zip(l1,l2,tu))))

执行结果：[(3, 'wusir', '****'), (4, '太白', '*******')]
```


```

​	



1. 有如下数据类型(**实战题**)：

```
 l1 = [ {'sales_volumn': 0},

	{'sales_volumn': 108},
	
	{'sales_volumn': 337},
	
	{'sales_volumn': 475},
	
	{'sales_volumn': 396},
	
	{'sales_volumn': 172},
	
	{'sales_volumn': 9},
	
	{'sales_volumn': 58}, 
	
	{'sales_volumn': 272}, 
	
	{'sales_volumn': 456}, 
	
	{'sales_volumn': 440},
	
	{'sales_volumn': 239}]
```

​	将l1按照列表中的每个字典的values大小进行排序，形成一个新的列表。

```
```
l2=sorted(l1,key=lambda x:x['sales_volumn'])
print(l2)

执行结果：[{'sales_volumn': 0}, {'sales_volumn': 9}, {'sales_volumn': 58}, {'sales_volumn': 108}, {'sales_volumn': 172}, {'sales_volumn': 239}, {'sales_volumn': 272}, {'sales_volumn': 337}, {'sales_volumn': 396}, {'sales_volumn': 440}, {'sales_volumn': 456}, {'sales_volumn': 475}]
```


```







1. 求结果(**面试题**)

​```python
v = [lambda :x for x in range(10)]

print(v)

print(v[0])

print(v[0]())

执行结果：
[第1个函数地址,第2个函数地址...第10个函数地址]
第1个函数地址
9

解释：
v = [【lambda :x】 for x in range(10)]
v是列表推导式，列表里里面有10个元素，每个元素是一个lambda函数的内存地址（输出x）（函数只有在调用时才执行，所以此时尚未执行）
print(v[0])时输出第1个函数内存地址，依然不执行
print(v[0]())此时函数才开始执行，x已变为9
```









1. 求结果(**面试题**)

```
v = (lambda :x for x in range(10))

print(v)

print(v[0])

print(v[0]())

print(next(v))

print(next(v)())

执行结果：
<generator object <genexpr> at 0x0000000002428308>
报错
报错
<function <genexpr>.<lambda> at 0x000000000242AC80>
1

=================================
print(v)：生成器，v仅指向一个内存地址，未运行
print(v[0])：生成器尚未运行，没有v[0]，报错
print(v[0]())：生成器尚未运行，没有v[0]，报错
print(next(v))：第一个函数（输出的x为0）的内存地址
print(next(v)())：1，因为上一步已经执行了一个next，所以x从0变为1。为什么这题是1而上题是9？生成器表达式满足惰性机制一步一步执行，列表推导式是一次性全部执行
```







map(str,[1,2,3,4,5,6,7,8,9])输出是什么? (**面试题**)

答：输出一个生成器，输出的元素分别为'1'、'2'...'9'





13题：求结果：（**面试题，比较难，先做其他题**）

```
def num():
	return [lambda x:i*x for i in range(4)]
print([m(2)for m in num()])

执行结果：
[6, 6, 6, 6]
```











14题：有一个数组[34，1,2,5,6,6,5,4，3,3]请写一个函数，找出该数组中没有重复的数

的总和（上面数据的么有重复的总和为1+2=3)(**面试题**)

```
l=[34,1,2,5,6,6,5,4,3,3]
y=[]
for i in l:
    y.extend(str(i))
for j in range(len(y)):
    y[j]=int(y[j])
print(y)
sum=0
for k in range(10):
    if y.count(k)==1:
        sum+=k
print(sum)

执行结果：
[3, 4, 1, 2, 5, 6, 6, 5, 4, 3, 3]
3
```













1. 写一个函数完成三次登陆功能：
   - 用户的用户名密码从一个文件register中取出。
   
   - register文件包含多个用户名，密码，用户名密码通过|隔开，每个人的用户名密码占用文件中一行。
   
   - 完成三次验证，三次验证不成功则登录失败，登录失败返回False。
   
   - 登陆成功返回True。
   
     **方法一：使用字典保存用户名、密码更好，详见day14作业第2题**
   
     **方法二：每次输完都遍历搜索整个数据表，效率低**

```python
def login():
    code = 'qwer'
    time_left = 3
    while time_left>=1:
        username = input('请输入用户名：')
        password = input('请输入密码：')
        your_code = input('请输入验证码：')
        if your_code == code:
            with open('register.txt',encoding='gbk')as f:
                for line in f:
                    line=line.strip().split('|')
                    if username == line[0].strip() and password == line[1].strip():
                        print('登录成功')
                        return True
                else:
                    time_left = time_left - 1
                    print('账号或者密码错误，您还剩%d次机会' % (time_left))
        else:
            print('验证码错误')
    else:
        print('您已输错三次')
        return False
login()
```











1. 再写一个函数完成注册功能：
   - 用户输入用户名密码注册。
   - 注册时要验证（文件regsiter中）用户名是否存在，如果存在则让其重新输入用户名，如果不存在，则注册成功。
   - 注册成功后，将注册成功的用户名，密码写入regsiter文件，并以 | 隔开。
   - 注册成功后，返回True,否则返回False。

```python
def register():
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
register()
```









1. 用完成一个员工信息表的增删功能（**选做题，有时间做，没时间周末做**）。

文件存储格式如下：

id，name，age，phone，job

1,Alex,22,13651054608,IT

2,太白,23,13304320533,Tearcher

3,nezha,25,1333235322,IT

现在要让你实现两个功能：

第一个功能是实现给文件增加数据，用户通过输入姓名，年龄，电话，工作，给原文件增加数据（增加的数据默认追加到原数据最后一行的下一行），但id要实现自增（id自增有些难度，id是不需要用户输入的但是必须按照顺序增加）。

第二个功能是实现给原文件删除数据，用户只需输入id，则将原文件对应的这一条数据删除（删除后下面的id不变，比如此时你输入1，则将第一条数据删除，但是下面所有数据的id值不变，即太白，nezha的 id不变）。

```python
#读取本地txt数据，输出字典组成的列表l，以及id最大值max_id
#l的格式示例l=[{'id': '1', 'name': 'Alex', 'age': '22', 'phone': '13651054608', 'job': 'IT'}, {'id': '2', 'name': '太白', 'age': '23', 'phone': '13304320533', 'job': 'Tearcher'}, {'id': '3', 'name': 'nezha', 'age': '25', 'phone': '1333235322', 'job': 'IT'}]
def get_information_list():
    with open('员工信息表.txt',encoding='gbk')as f:
        title=f.readline().strip()
        title_list=title.split(',')
        for i in range(len(title_list)):
            title_list[i] = title_list[i].strip()
        l=[]
        max_id=0
        for line in f:
            dic = {}
            line_list=line.strip().split(',')
            for i in range(len(title_list)):
                #当字段为id、age、phone时，将数据转化为int格式
                if i==0 or i==2 or i==3:
                    line_list[i] = int(line_list[i].strip())
                else:
                    line_list[i]=line_list[i].strip()
                dic[title_list[i]]=line_list[i]
                #计算到目前为止的id最大值
                if i==0:
                    max_id=max(max_id,line_list[i])
            l.append(dic)
    return l,max_id
print(get_information_list())

#在文件末尾添加一条数据
def add_data():
    input_name=input('请输入姓名：').strip()
    input_age=input('请输入年龄：').strip()
    input_phone=input('请输入电话：').strip()
    input_job=input('请输入工作：').strip()
    information_list,max_id=get_information_list()
    with open('员工信息表.txt',encoding='gbk',mode='a')as f:
        line=f'{max_id+1},{input_name},{input_age},{input_phone},{input_job}\n'
        f.write(line)
        print('添加成功！')

#输入id，将对应的这条数据从源文件中删除
def delete_data():
    import os
    input_id=input('请输入要删除的id：').strip()
    #注意input_id不要转化成数字
    with open('员工信息表.txt',encoding='gbk')as f1, open('员工信息表.txt.bak',encoding='gbk',mode='w')as f2:
        for line in f1:
            if line.startswith(input_id+',')==False:
                f2.write(line)
    os.remove('员工信息表.txt')
    os.rename('员工信息表.txt.bak','员工信息表.txt')
    print('删除成功！')

#主程序
while 1:
    user_choice=input('1.增加数据\n2.删除数据\n3.退出程序\n请输入您的选择：').strip()
    if user_choice=='1':
        add_data()
    elif user_choice=='2':
        delete_data()
    elif user_choice=='3':
        print('程序退出！')
        break
    else:
        print('您的输入有误，请重新输入')
```