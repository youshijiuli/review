1、匹配一篇英文文章的标题 类似 The Voice Of China

```
[A-Z][A-Za-z]*( [A-Z][A-Za-z]*)*
```

2、【★】匹配一个网址

```
https?://www([.][\dA-Za-z]+){2,}
```

3、【★】匹配年月日日期 类似 2018-12-06 2018/12/06 2018.12.06

【年首位不为0，月、日可以是一位数或两位数】【连接符任意但是前后要一致】

```
[1-9]\d{3}(?P<tag>)(1[0-2]|0?[1-9])(?P=sub)([12]\d|3[01]|0?[1-9])
```

4、【★】匹配15位或者18位身份证号

```
^[1-9]\d{14}(\d{2}[\dx])?$
```



```
5、从lianjia.html（html文件在群文件中）中匹配出标题，户型和面积，结果如下：
[('金台路交通部部委楼南北大三居带客厅   单位自持物业', '3室1厅', '91.22平米'), ('西山枫林 高楼层南向两居 户型方正 采光好', '2室1厅', '94.14平米')]

import re
with open('lianjia.html',encoding='utf-8')as f:
    content=f.read()
    regex=r'data-sl="">(.*?)</a>.*?<span class="divide">/</span>(.*?厅)<span class="divide">/</span>(.*?平米)<span class="divide">'
    li=re.findall(regex,content,flags=re.S)
print(li)

执行结果：
[('金台路交通部部委楼南北大三居带客厅   单位自持物业', '3室1厅', '91.22平米'), ('西山枫林 高楼层南向两居 户型方正 采光好', '2室1厅', '94.14平米')]
```



```
6、1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
从上面算式中匹配出最内层小括号以及小括号内的表达式

答案：[(][^()]+?[)]
匹配结果：(-40/5)、(9-2*5/3+7/3*99/4*2998+10*568/14)、(-4*3)、(16-3*2)
```



```
7、从类似9-2*5/3+7/3*99/4*2998+10*568/14的表达式中匹配出乘法或除法

答案：\d+(([*]|/)\d+)+
匹配结果：2*5/3、7/3*99/4*2998、10*568/14
```



8、完成递归相关的题目、通读博客，完成三级菜单
http://www.cnblogs.com/Eva-J/articles/7205734.html

```python
# 递归相关
# 1.计算阶乘 100! = 100*99*98*97*96....*1
    
# 循环法
def fin(n):
	ret=1
	for i in range(1,n):
		ret=ret*i
	return ret
	
# 递归法
def f(n):
    if n ==1 :
        return n
    else:
        return n*f(n-1)
```



```python
# 2.os模块:查看一个文件夹下的所有文件,这个文件夹下面还有文件夹,不能用walk【要求：掌握】
import os
def show_file(path):
    name_list = os.listdir(path)
    for name in name_list:
        abs_path = os.path.join(path,name)
        if os.path.isfile(abs_path):
            print(name)
        else:
            show_file(abs_path)
show_file('D:\软件')
```



```python
# 3.os模块:计算一个文件夹下所有文件的大小.这个文件夹下面还有文件夹,不能用walk【要求：看懂，并知道实现方法】
import os
def dir_size(path):
    size=0
    name_list = os.listdir(path)
    for name in name_list:
        abs_path = os.path.join(path,name)
        if os.path.isfile(abs_path):
            size+=os.path.getsize(abs_path)
        else:
            size+=dir_size(abs_path)
    return size
print(dir_size('D:\软件'))

注：不可使用nonlocal size，报错SyntaxError: name 'size' is assigned to before nonlocal declaration
```



```python
# 4.计算斐波那契数列（要求：会写）
    # 找第100个数
    # 1 1 2 3 5...

#方法一：两个递归（有问题，不要写这个）
def f(n):
    if n==1 or n==2:
        return 1
    else:
        return f(n-1)+f(n-2)
# 由于调用了两个递归，使得计算量指数增长，算f(100)时等待的时间过长，不要写这个

#方法二：一个递归
def fib(n,a=1,b=1):
    if n == 1 or n == 2:
        return b
    else:
        a,b = b,a+b
        return fib(n-1,a,b)
print(fib(100))

#方法三：while【推荐】
def fib(n):
    a,b = 1,1
    while n>2:
        a,b = b,a+b
        n-=1
    return b
print(fib(100))
    
执行结果：
354224848179261915075
```

```python
第4题推广：扩展的数列，每一项等于前三项的和，如1,1,1,3,5,9,17....
def f(n):
    a,b,c=1,1,1
    while n>3:
        a,b,c=b,c,a+b+c
        n-=1
    return c
print(f(7))
```

```python
# 5.三级菜单 可能是n级【要求：看懂，并知道实现方法】
# 递归 循环
# https://www.cnblogs.com/Eva-J/articles/7205734.html#_label4
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}    

def func(x):
    while 1:
        for i in x.keys():
            print(i)
        key=input('请输入选项>>>').strip()
        if x.get(key):          # 如果x[key]有对应的值且值不为空
            ret = func(x[key])
            if ret==False:
                return False
        elif key.upper() == 'B':
            return True
        elif key.upper() == 'Q':
            return False
func(menu)
print('程序结束')
```





9、大作业：计算器

【待完成】

```
9-2*-6/3.33+7/3*99/4*2998+10*568/14-2*((60-30+(-40/-5.5)*(9-2*5/3+7/3*-99/4.25*2998+10*568/14))-(-4*3)/(16-3*2))
```

