## day04作业

1.写代码，有如下列表，按照要求实现每一个功能

li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
计算列表的长度并输出

```
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
print(len(li))

输出结果：5
```

列表中追加元素"seven",并输出添加后的列表

```
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
li.append('seven')
print(li)

输出结果：['alex', 'WuSir', 'ritian', 'barry', 'wenzhou', 'seven']
```

请在列表的第1个位置插入元素"Tony",并输出添加后的列表

```
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
li.insert(0,'Tony')
print(li)

输出结果：['Tony', 'alex', 'WuSir', 'ritian', 'barry', 'wenzhou']
```

请修改列表第2个位置的元素为"Kelly",并输出修改后的列表

```
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
li[1]='Kelly'
print(li)

输出结果：['alex', 'Kelly', 'ritian', 'barry', 'wenzhou']
```

请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。

```
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
l2 = [1,"a",3,4,"heart"]
li.extend(l2)
print(li)

输出结果：['alex', 'WuSir', 'ritian', 'barry', 'wenzhou', 1, 'a', 3, 4, 'heart']
```

请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。

```
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
s = "qwert"
li.extend(s)
print(li)

输出结果：['alex', 'WuSir', 'ritian', 'barry', 'wenzhou', 'q', 'w', 'e', 'r', 't']
```

请删除列表中的元素"ritian",并输出添加后的列表

```
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
li.remove('ritian')
print(li)

输出结果：['alex', 'WuSir', 'barry', 'wenzhou']
```

请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表

```
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
print(li.pop(1))
print(li)

输出结果：
WuSir
['alex', 'ritian', 'barry', 'wenzhou']
```

请删除列表中的第2至4个元素，并输出删除元素后的列表

```
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
del li[1:4]
print(li)

输出结果：['alex', 'wenzhou']
```

2.写代码，有如下列表，利用切片实现每一个功能

li = [1, 3, 2, "a", 4, "b", 5,"c"]
通过对li列表的切片形成新的列表l1,l1 = [1,3,2]

```
li = [1, 3, 2, "a", 4, "b", 5,"c"]
print(li[:3])
```

通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]

```
li = [1, 3, 2, "a", 4, "b", 5,"c"]
print(li[3:6])
```

通过对li列表的切片形成新的列表l3,l3 = ["1,2,4,5]

```
li = [1, 3, 2, "a", 4, "b", 5,"c"]
print(li[::2])
```

通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]

```
li = [1, 3, 2, "a", 4, "b", 5,"c"]
print(li[1:-2:2])
```

通过对li列表的切片形成新的列表l5,l5 = ["c"]

```
li = [1, 3, 2, "a", 4, "b", 5,"c"]
print(li[-1:])
```

通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]

```
li = [1, 3, 2, "a", 4, "b", 5,"c"]
print(li[-3::-2])
```

3.写代码，有如下列表，按照要求实现每一个功能。

lis = [2, 30, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
将列表lis中的"tt"变成大写（用两种方式）。

```
lis = [2, 30, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][0]="TT"
print(lis)
```

```
lis = [2, 30, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][0]=lis[3][2][1][0].upper()
print(lis)
```

将列表中的数字3变成字符串"100"（用两种方式）。

```
lis = [2, 30, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][1]='100'
print(lis)
```

```
lis = [2, 30, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][1]=str(lis[3][2][1][1]+97)
print(lis)
```

将列表中的字符串"1"变成数字101（用两种方式）。

```
lis = [2, 30, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][2]=101
print(lis)
```

```
lis = [2, 30, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][2]=int(lis[3][2][1][2])+100
print(lis)
```

4.请用代码实现：
li = ["alex", "wusir", "taibai"]
利用下划线将列表的每一个元素拼接成字符串"alex_wusir_taibai"

```
li = ["alex", "wusir", "taibai"]
s = '_'.join(li)
print(s)

输出结果：alex_wusir_taibai
```

5.利用for循环和range打印出下面列表的索引。

li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]

```
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
for i in range(len(li)):
    print(i)
    
输出结果：
0
1
2
3
4
```

6.利用for循环和range找出100以内所有的偶数并将这些偶数插入到一个新列表中。

```
li=[]
for i in range(101):
    if i % 2 == 0:
        li.append(i)
print(li)

输出结果：[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
```

7.利用for循环和range 找出50以内能被3整除的数，并将这些数插入到一个新列表中。

```
li=[]
for i in range(51):
    if i % 3 == 0:
        li.append(i)
print(li)

输出结果：[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
```

8.利用for循环和range从100~1，倒序打印。

```
for i in range(100,0,-1):
    print(i)
```

9.利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来。

```
li=[]
for i in range(100,9,-1):
    if i % 2 == 0:
        li.append(i)
del li[1::2]
print(li)

输出结果：[100, 96, 92, 88, 84, 80, 76, 72, 68, 64, 60, 56, 52, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12]
```

10.利用for循环和range，将1-30的数字一次添加到一个列表中，并循环这个列表，将能被3整除的数改成*。

```
li=[]
for i in range(1,31):
    li.append(i)
for j in range(len(li)):
    if li[j] % 3 == 0:
        li[j]='*'
print(li)

输出结果：[1, 2, '*', 4, 5, '*', 7, 8, '*', 10, 11, '*', 13, 14, '*', 16, 17, '*', 19, 20, '*', 22, 23, '*', 25, 26, '*', 28, 29, '*']
```

11.查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，并添加到一个新列表中,最后循环打印这个新列表。
li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc"]

```python
li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc"]
new_li=[]
for x in li:
    y=x.strip()
    if y[0].upper()=="A" and y[-1]=="c":
        new_li.append(y)
print(new_li)

输出结果：['aqc']
```

12.开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
敏感词列表 li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
则将用户输入的内容中的敏感词汇替换成等长度的“*”（苍老师就替换成三个星），并添加到一个列表中；如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。

```python
li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
user_comment=input('请输入评论内容：')
new_comment_list=[]
for sensitive_word in li:
    if sensitive_word in user_comment:
        stars='*'*len(sensitive_word)	#生成与敏感词等长度的*
        user_comment=user_comment.replace(sensitive_word,stars)
new_comment_list.append(user_comment)
print(new_comment_list)

输出结果1：
请输入评论内容：哈哈哈哈
['哈哈哈哈']

输出结果2：
请输入评论内容：哈哈哈哈苍老师嘿嘿嘿波多野结衣啦啦啦啦
['哈哈哈哈***嘿嘿嘿*****啦啦啦啦']
```

13.有如下列表（选做题）
li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
循环打印列表中的每个元素，遇到列表则再循环打印出它里面的元素。
我想要的结果是：
1
3
4
"alex"
3
7,
8
"taibai"
5
ritian

```python
li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
for i in li:
    if type(i) == int:
        print(i)
    elif type(i) == str:
        if i.lower()=="ritian":
            print (i.lower())
        else:
            print('"'+str(i).lower()+'"')
    else:
        for j in i:
            if j == 7:
                print(str(j)+',')
            elif type(j)==int:
                print(j)
            else:
                print('"'+str(j).lower()+'"')
                
输出结果：
1
3
4
"alex"
3
7,
8
"taibai"
5
ritian
```
