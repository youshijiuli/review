## day12 作业

1. 整理今天笔记，课上代码最少敲3遍。

2. 用列表推导式做下列小题

3. 过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母

   ```
   s=['aaaa','bbb','cc','d','eeee']
   print([i.upper() for i in s if len(i)<3])
   
   执行结果：['CC', 'D']
   ```

4. 求(x,y)其中x是0-5之间的偶数，y是0-5之间的奇数组成的元祖列表

   ```
   print([(x,y) for x in range(0,6) for y in range(0,6) if (x%2==0) and (y%2==1)])
   
   执行结果：[(0, 1), (0, 3), (0, 5), (2, 1), (2, 3), (2, 5), (4, 1), (4, 3), (4, 5)]
   ```

5. 求M中3,6,9组成的列表M = [[1,2,3],[4,5,6],[7,8,9]]

   ```
   方法1
   M = [[1,2,3],[4,5,6],[7,8,9]]
   print([j for i in M for j in i if j % 3==0])
   
   方法2
   M = [[1,2,3],[4,5,6],[7,8,9]]
   print([i[-1] for i in M])
   
   执行结果：[3, 6, 9]
   ```

6. 求出50以内能被3整除的数的平方，并放入到一个列表中。

   ```
   print([i**2 for i in range(1,51) if i % 3==0])
   
   执行结果：[9, 36, 81, 144, 225, 324, 441, 576, 729, 900, 1089, 1296, 1521, 1764, 2025, 2304]
   ```

7. 构建一个列表：['python1期', 'python2期', 'python3期', 'python4期', 'python6期', 'python7期', 'python8期', 'python9期', 'python10期']

   ```
   print([f'python第{i}期'for i in range(1,11)if i!=5])
   
   执行结果：['python第1期', 'python第2期', 'python第3期', 'python第4期', 'python第6期', 'python第7期', 'python第8期', 'python第9期', 'python第10期']
   ```

8. 构建一个列表：[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]

   ```
   print([(i,i+1)for i in range(0,6)])
   
   执行结果：
   [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
   ```

9. 构建一个列表：[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

   ```
   print([i for i in range(0,19,2)])
   ```

10. 有一个列表l1 = ['alex', 'WuSir', '老男孩', '太白']将其构造成这种列表['alex0', 'WuSir1', '老男孩2', '太白3']‘

   ```
   l1 = ['alex', 'WuSir', '老男孩', '太白']
   print([l1[i]+str(i) for i in range(len(l1))])
   
   执行结果：
   ['alex0', 'WuSir1', '老男孩2', '太白3']
   ```

11. 有以下数据类型：

```
x = {'name':'alex',
     'Values':[{'timestamp':1517991992.94,'values':100,},
               {'timestamp': 1517992000.94,'values': 200,},
            {'timestamp': 1517992014.94,'values': 300,},
            {'timestamp': 1517992744.94,'values': 350},
            {'timestamp': 1517992800.94,'values': 280}],}
```

将上面的数据通过列表推导式转换成下面的类型：[[1517991992.94, 100], [1517992000.94, 200], [1517992014.94, 300], [1517992744.94, 350], [1517992800.94, 280]]

方法一：

```
print([ [x['Values'][i]['timestamp'],x['Values'][i]['values']] for i in range(len(x['Values']))])

输出结果：
[[1517991992.94, 100], [1517992000.94, 200], [1517992014.94, 300], [1517992744.94, 350], [1517992800.94, 280]]
```

方法二：

【推荐用get写】

1. 用列表完成笛卡尔积

   什么是笛卡尔积？ 笛卡尔积就是一个列表，列表里面的元素是由输入的可迭代类型的元素对构成的元组，因此笛卡尔积列表的长度等于输入变量的长度的乘积。

​	a. 构建一个列表，列表里面是三种不同尺寸的T恤衫，每个尺寸都有两个颜色（列表里面的元素为元组类型)。

```
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirt=[(i,j) for i in colors for j in sizes]
print(tshirt)

执行结果：[('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
```

​	b. 构建一个列表,列表里面的元素是扑克牌除去大小王以后，所有的牌类（列表里面的元素为元组类型）。

```
l1 = [('A','spades'),('A','diamonds'), ('A','clubs'), ('A','hearts')......('K','spades'),('K','diamonds'), ('K','clubs'), ('K','hearts') ]
```

```
count=['A']+[i for i in range(2,11)]+list('JQK')
color=['spades','diamonds','clubs','hearts']
l1=[(i,j) for i in count for j in color]
print(l1)

输出结果：[('A', 'spades'), ('A', 'diamonds'), ('A', 'clubs'), ('A', 'hearts'), (2, 'spades'), (2, 'diamonds'), (2, 'clubs'), (2, 'hearts'), (3, 'spades'), (3, 'diamonds'), (3, 'clubs'), (3, 'hearts'), (4, 'spades'), (4, 'diamonds'), (4, 'clubs'), (4, 'hearts'), (5, 'spades'), (5, 'diamonds'), (5, 'clubs'), (5, 'hearts'), (6, 'spades'), (6, 'diamonds'), (6, 'clubs'), (6, 'hearts'), (7, 'spades'), (7, 'diamonds'), (7, 'clubs'), (7, 'hearts'), (8, 'spades'), (8, 'diamonds'), (8, 'clubs'), (8, 'hearts'), (9, 'spades'), (9, 'diamonds'), (9, 'clubs'), (9, 'hearts'), (10, 'spades'), (10, 'diamonds'), (10, 'clubs'), (10, 'hearts'), ('J', 'spades'), ('J', 'diamonds'), ('J', 'clubs'), ('J', 'hearts'), ('Q', 'spades'), ('Q', 'diamonds'), ('Q', 'clubs'), ('Q', 'hearts'), ('K', 'spades'), ('K', 'diamonds'), ('K', 'clubs'), ('K', 'hearts')]

```

1. 简述一下yield 与yield from的区别。
   + yield 后面可以接可迭代对象或不可迭代对象，yield from 后面只能接可迭代对象
   + yiled 把后面的对象作为生成器的结果进行返回，yield from把后面的可迭代对象中的每一个元素作为生成器的结果进行返回
2. 看下面代码，能否对其简化？说说你简化后的优点？

```
def chain(*iterables):
	for it in iterables:
		for i in it:
			yield i
g = chain('abc',(0,1,2))

print(list(g))  # 将迭代器转化成列表
```

原代码直接使用for循环加载所有输入变量，会导致内存耗费较大。简化后使用yield from，满足惰性机制，内存耗费较小。

```
def chain(*iterables):
    for it in iterables:
    	yield from it
g = chain('abc',(0,1,2))
print(list(g))
```

**【【【问题，此代码只能适应两层可迭代数据的情况，不能用于更多层数，拓展性较差，如何修改使适用与任意层可迭代数据？即：能否更改代码使之适用于任意层可迭代对象（比如，输入的变量有三层嵌套的列表）？】】】**

yield from优化内层循环，提高效率，节省时间，节省内存

1. 看代码求结果（**面试题**）：

```
v = [i % 2 for i in range(10)]
print(v)

v = (i % 2 for i in range(10))
print(v)

for i in range(5):
	print(i)
print(i)

执行结果：
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
<generator object <genexpr> at 0x0000000001FA9360>
0
1
2
3
4
4
```

1. 看代码求结果：（**面试题**）

```python
def demo():
    for i in range(4):
        yield i

g=demo()

g1=(i for i in g)
g2=(i for i in g1)

print(list(g1))
print(list(g2))

执行结果：
[0,1,2,3]
[]

解释：
print(list(g1))开始执行后，生成器的指针已到最后
list(g2)=list((i for i in g1))=[i for i in g1]，由于g1已经list过，所以g1的指针已在g1最后，所以[i for i in g1]的计算结果为[]





【【【类比】】】
def demo():
    for i in range(4):
        yield i

g=demo()

g1=(j for j in g)
g2=(k for k in g1)

print(list(g1))
print(list(g2))

执行结果：
[0,1,2,3]
[]

解释：把g1和g2对应的i换成j、k后，结果不变，跟i本身的值没关系，故此题不应该用i的值去解释
```

1. 看代码求结果：（**面试题**）

```python
def add(n,i):
    return n+i

def test():
    for i in range(4):
        yield i

g=test()
for n in [1,10]:
    g=(add(n,i) for i in g)

print(list(g))

执行结果：
[20, 21, 22, 23]

==============
for n in [1,10]两次循环执行
g=(add(n,i) for i in g)两次生成器不执行
生成器见next、list或生成器外的for才执行
```

![作业题12思路](D:\老男孩\day012\作业题12思路.png)