# day23作业（张珵）

第一大题 : 读程序,标出程序的执行过程,画出内存图解,说明答案和为什么

请不要想当然,执行之后检查结果然后再确认和自己的猜想是不是一致

```
(1)
class A:
    Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
    def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
    def func1(self):
        print(self)

a = A('alex',83,'印度')
b = A('wusir',74,'泰国')
A.Country = '英国'
a.Country = '日本'
print(a.Country)
print(b.Country)
print(A.Country)

执行结果：
日本
英国
英国
解释：先为A定义静态变量Country = '中国'，但是由于__init__函数并未定义self.Country属性，因此即使输入了country参数也未使用它，因此a的'印度'和b的'泰国'都是无效的输入参数，后来A.Country = '英国'将A的静态变量Country从'中国'修改为'英国'，a.Country = '日本'则为a定义了Country属性并赋值'日本'，但是b并未定义Country属性值，因此输出b.Country时会去A的命名空间寻找Country，即修改后的'英国'，内存图如下所示：
```





![作业1](D:\老男孩\day023\作业1.JPG)

```
（2）
class A:
    Country = ['中国']     # 静态变量/静态属性 存储在类的命名空间里的
    def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
    def func1(self):
        print(self)

a = A('alex',83,'印度')
b = A('wusir',74,'泰国')
a.Country[0] = '日本'
print(a.Country)
print(b.Country)
print(A.Country)

执行结果：
['日本']
['日本']
['日本']
解释：由于a的命名空间并没有Country属性，因此执行a.Country[0] = '日本'时回去A的命名空间搜索Country并将其第0项修改为'日本'。修改列表的元素不会改变列表本身的内存地址，因此b.Country和A.Country也都是['日本']，内存如下图所示：
```

![作业2](D:\老男孩\day023\作业2.jpg)



```
（3）
class A:
    Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
    def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
        self.Country = country
    def func1(self):
        print(self)

a = A('alex',83,'印度')
b = A('wusir',74,'泰国')
A.Country = '英国'
a.Country = '日本'
print(a.Country)
print(b.Country)
print(A.Country)

执行结果：
日本
泰国
英国
解释：和前两题不同，这题多了self.Country = country，即输入的country被应用到了每个变量自己的属性Country中，因此a,b,A各改各的，各用各的，互不影响，内存图如下：
```

![作业3](D:\老男孩\day023\作业3.jpg)

```
（4）
class A:
    Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
    def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
    def Country(self):
        return self.Country

a = A('alex',83,'印度')
b = A('wusir',74,'泰国')
print(a.Country)
print(a.Country())

执行结果：
<bound method A.Country of <__main__.A object at 0x0000000002089C50>>
<bound method A.Country of <__main__.A object at 0x0000000002089C50>>

在定义类A时，先为A定义一个静态变量Country = '中国',然后又定义了一个方法Country，由于与刚才的静态变量重名，所以后定义的将先定义的覆盖了，Country最后指向了函数的内存地址。'印度'和'泰国“都是无效的输入参数，不再赘述。
开始执行a.Country时，由于a的命名空间里没有Country，因此到A的命名空间进行搜索，得到了这个函数的内存地址。
开始执行a.Country()时，由于a的命名空间里没有Country，因此到A的命名空间进行搜索，得到了这个函数的内存地址并且执行了它。返回self.Country，即在a的命名空间寻找Country，依然没找到，于是到A的空间继续找，再次得到了相同的函数的地址。
```

![作业4](D:\老男孩\day023\作业4.jpg)



第二大题:基于圆形类实现一个圆环类,要求接收参数 外圆半径和内圆半径
完成方法 :计算环形面积和环形周长(公式自己上网查)
要求,借助组合,要求组合圆形类的对象完成需求

```python
from math import pi
class Circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        return pi*self.radius**2
    def perimeter(self):
        return 2*pi*self.radius
class Annulus:
    def __init__(self,ro,ri):
        self.radius_outer=ro
        self.radius_inner=ri
    def area(self):
        return pi*(self.radius_outer**2-self.radius_inner**2)
    def perimeter(self):
        return 2*pi*(self.radius_outer+self.radius_inner)
outer_circle=Circle(100)
inner_circle=Circle(10)
my_annulus=Annulus(outer_circle.radius,inner_circle.radius)
print(my_annulus.area())
print(my_annulus.perimeter())

执行结果：
31101.767270538952
691.1503837897545
```



第三大题:继续完成计算器和优化工作

**已完成并测试验证完毕，已上传单独的md文件至码云**