## day08 作业

 

1. 有如下文件，a1.txt，里面的内容为：

------

老男孩是最好的学校，

全心全意为学生服务，

只为学生未来，不为牟利。

我说的都是真的。哈哈

------



​	分别完成以下的功能：

​	a.将原文件全部读出来并打印。

```
with open('a1.txt',encoding='gbk') as f1:
    content=f1.read()
    print(content)
```

​	b,在原文件后面追加一行内容：信不信由你，反正我信了。

```
with open('a1.txt',encoding='gbk',mode='a') as f1:
    f1.write('信不信由你，反正我信了')
```

​	c,将原文件全部读出来，并在后面添加一行内容：信不信由你，反正我信了。

```
with open('a1.txt',encoding='gbk',mode='r+') as f1:
    print(f1.read())
    f1.write('信不信由你，反正我信了')
```

​	d,将原文件全部清空，换成下面的内容：

------

​	每天坚持一点，

​	每天努力一点，

​	每天多思考一点，

​	慢慢你会发现，

​	你的进步越来越大。

```
c='''每天坚持一点，
每天努力一点，
每天多思考一点，
慢慢你会发现，
你的进步越来越大。'''

with open('a1.txt',encoding='gbk',mode='w') as f1:
    f1.write(c)
```

```
c='每天坚持一点，\n每天努力一点，\n每天多思考一点，\n慢慢你会发现，\n你的进步越来越大。'

with open('a1.txt',encoding='gbk',mode='w') as f1:
    f1.write(c)
```

------

2.有如下文件，t1.txt,里面的内容为：

------

葫芦娃，葫芦娃，

一根藤上七个瓜

风吹雨打，都不怕，

啦啦啦啦。

我可以算命，而且算的特别准:

上面的内容你肯定是心里默唱出来的，对不对？哈哈

------

​	分别完成下面的功能：

​	a,以r的模式打开原文件，利用for循环遍历文件句柄。

```
with open('a1.txt',encoding='gbk') as f1:
    for line in f1:
        print(line)
        
输出结果：
葫芦娃，葫芦娃，

一根藤上七个瓜

风吹雨打，都不怕，

啦啦啦啦。

我可以算命，而且算的特别准:

上面的内容你肯定是心里默唱出来的，对不对？哈哈
```

​	b,以r的模式打开原文件，以readlines()方法读取出来，并循环遍历 readlines(),并分析b,与c 有什么区别？深入理解文件句柄与 readlines()结果的区别。

```
with open('a1.txt',encoding='gbk') as f1:
    print(f1.readlines())
    
输出结果：
['葫芦娃，葫芦娃，\n', '一根藤上七个瓜\n', '风吹雨打，都不怕，\n', '啦啦啦啦。\n', '我可以算命，而且算的特别准:\n', '上面的内容你肯定是心里默唱出来的，对不对？哈哈']
```

​	c,以r模式读取‘葫芦娃，’前四个字符。

```
with open('a1.txt',encoding='gbk') as f1:
    print(f1.read(4))
    
输出结果：
葫芦娃，
```

​	d,以r模式读取第一行内容，并去除此行前后的空格，制表符，换行符。

```
with open('a1.txt',encoding='gbk') as f1:
    print(f1.readline().strip())
    
输出结果：
葫芦娃，葫芦娃，
```

​	e,以a+模式打开文件，先追加一行：‘老男孩教育’然后在从最开始将 原内容全部读取出来。

```
with open('a1.txt',encoding='gbk',mode='a+') as f1:
    f1.write('老男孩教育')
    f1.seek(0)
    print(f1.read())
    
输出结果：
葫芦娃，葫芦娃，
一根藤上七个瓜
风吹雨打，都不怕，
啦啦啦啦。
我可以算命，而且算的特别准:
上面的内容你肯定是心里默唱出来的，对不对？哈哈老男孩教育
```

1. 文件a.txt内容：每一行内容分别为商品名字，价钱，个数。

------

apple 10 3

tesla 100000 1

mac 3000 2

lenovo 30000 3

chicken 10 3

------

​	通过代码，将其构建成这种数据类型：[{'name':'apple','price':10,'amount':3},{'name':'tesla','price':1000000,'amount':1}......] 并计算出总价钱。

```
#建立一个列表key_list，里面的每个元素都是字典的键，与line_list里面的每个元素一一对应
key_list=['name','price','amount']
result_list=[]
sum=0
with open('a.txt',encoding='gbk') as f:
    for line in f:
        line_list=line.strip().split()
        d={}
        for i in range(len(key_list)):
            if line_list[i].isdecimal():
                line_list[i]=int(line_list[i])
            d.setdefault(key_list[i],line_list[i])
        result_list.append(d)
        sum = sum +line_list[1]*line_list[2]
print(result_list)
print(sum)

输出结果：
[{'name': 'apple', 'price': 10, 'amount': 3}, {'name': 'tesla', 'price': 100000, 'amount': 1}, {'name': 'mac', 'price': 3000, 'amount': 2}, {'name': 'lenovo', 'price': 30000, 'amount': 3}, {'name': 'chicken', 'price': 10, 'amount': 3}]
196060
```



1. 有如下文件：

------

alex是老男孩python发起人，创建人。

alex其实是人妖。

谁说alex是sb？

你们真逗，alex再牛逼，也掩饰不住资深屌丝的气质。

------

将文件中所有的alex都替换成大写的SB（文件的改的操作）。

```
import os
with open('alex自述',encoding='gbk') as f1,\
        open('alex自述.bak',encoding='gbk',mode='w') as f2:
    for line in f1:
        new_line = line.replace('alex', 'SB')
        f2.write(new_line)
os.remove('alex自述')
os.rename('alex自述.bak','alex自述')
```



1. 文件a1.txt内容(**选做题**)

------

name:apple price:10 amount:3 year:2012

name:tesla price:100000 amount:1 year:2013

------

​	通过代码，将其构建成这种数据类型：

​	[{'name':'apple','price':10,'amount':3,year:2012},

​	{'name':'tesla','price':1000000,'amount':1}......]

​	并计算出总价钱。

```
result_list=[]
sum=0
with open('a1.txt',encoding='gbk') as f:
    for line in f:
        line_list=line.strip().split()
        d={}
        for i in line_list:
            key, value=i.split(':')
            if value.isdecimal():
                value=int(value)
            d.setdefault(key,value)
        sum+=d['price']*d['amount']
        result_list.append(d)
print(result_list)
print(sum)

输出结果：
[{'name': 'apple', 'price': 10, 'amount': 3, 'year': 2012}, {'name': 'tesla', 'price': 100000, 'amount': 1, 'year': 2013}]
100030
```



1. 文件a1.txt内容(**选做题**)

------

序号 部门 人数 平均年龄 备注

1 python 30 26 单身狗

2 Linux 26 30 没对象

3 运营部 20 24 女生多

.......

------

通过代码，将其构建成这种数据类型：

[{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'},

......]

```
count=0
keys_list=[]
class_list=[]
result_list=[]
with open('a1.txt',encoding='gbk') as f:
    for line in f:
        count += 1
        if count==1:
            keys_list=line.strip().split()
            continue
        else:
            class_list=line.strip().split() #['1','python','30','26','单身狗']
        d = {}
        for j in range(len(keys_list)):
            if class_list[j].isdecimal():
                d.setdefault(keys_list[j],int(class_list[j]))
            else:
                d.setdefault(keys_list[j], class_list[j])
        result_list.append(d)
    print(result_list)

输出结果：[{'序号': 1, '部门': 'python', '人数': 30, '平均年龄': 26, '备注': '单身狗'}, {'序号': 2, '部门': 'Linux', '人数': 26, '平均年龄': 30, '备注': '没对象'}, {'序号': 3, '部门': '运营部', '人数': 20, '平均年龄': 24, '备注': '女生多'}]
```