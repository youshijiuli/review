# day09作业（张珵）

1.整理函数相关知识点,写博客。

2.写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。

```
def func(x):
    return list(x[1::2])

print(func(('a','b','c','d','e')))
print(func(['a']))

输出结果：
['b', 'd']
[]
```

3.写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。

方法一：

```
def func(x):
    if len(x)>5:
        return '大于5'
    else:
        return '不大于5'

print(func('abcdef'))
print(func('abcde'))

输出结果：
大于5
不大于5
```

方法二：

```
def func(x):
	return len(x)>5
```

4.写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。

```
def func(x):
    return x[:2]

print(func([1,2,3]))
print(func([1]))

输出结果：
[1, 2]
[1]
```

5.写函数，计算传入函数的字符串中,[数字]、[字母] 以及 [其他]的个数，并返回结果。

```
def func(x):
    a=0
    b=0
    for i in x:
        if i.isdecimal():
            a+=1
        elif i.isalpha():
            b+=1
    msg='该字符串中有%s个数字、%s个字母、%s个其他'%(a,b,len(x)-a-b)
    return msg
    
print(func('123abcd@#$%*'))
输出结果：该字符串中有3个数字、4个字母、5个其他
```

6.写函数，接收两个数字参数，返回比较大的那个数字。

```
def func(x,y):
    a=x if x>y else y
    return a
    
print(func(2,3))
print(func(4,3))
输出结果：
3
4
```

7.写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
PS:字典中的value只能是字符串或列表

```
def func(d):
    d_new={}
    for key,value in dic.items():
    	d_new[key]=value[:2]
    return d_new
    
dic= {"k1":"v1v1","k2":[11,22,33,44]}
print(func(dic))

输出结果：{'k1': 'v1', 'k2': [11, 22]}
```

8.写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为 {0:11,1:22,2:33}。

```
def func(l):
    if type(l)==list:
        d={}
        for i in range(len(l)):
            d.setdefault(i,l[i])
    else:
        return '输入数据类型必须是list'
    return d
l= [11,22,33]
print(func(l))
输出结果：{0: 11, 1: 22, 2: 33}
```

9.写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，然后将这四个内容传入到函数中，此函数接收到这四个内容，将内容追加到一个student_msg文件中。

```
def func(name,age,education,sex):
    with open('student_msg.txt',encoding='utf-8',mode='a') as f:
        content=str(name)+' '+str(sex)+' '+str(age)+' '+str(education)+'\n'
        f.write(content)
```

10.对第9题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。

写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（选做题）。

**三个参数：path, old_content, new_content**

```
import os

def func(filename,name,age,education,sex='男'):    
    with open(filename+'.txt',encoding='gbk',mode='r') as f1, open(filename+'bak.txt',encoding='gbk',mode='w') as f2:
        count=0 #计数器
        for line in f1:
            if line.strip().split()[0]==name:
                f2.write(str(name)+' '+str(age)+' '+str(education)+' '+str(sex)+'\n')
                count+=1
            else:
                f2.write(line)
        if count==0:
            f2.seek(0,2)
            f2.write(str(name)+' '+str(age)+' '+str(education)+' '+str(sex)+'\n')
    os.remove(filename+'.txt')
    os.rename(filename+'bak.txt',filename+'.txt')

filename=input('请输入要修改的文件名（输入q或Q退出)：')
filename=filename.strip()
if filename.upper()=='Q':
    print('系统退出')
else:
    while 1:
        student=input('请输入要修改的姓名、年龄、学历、性别，以空格分隔，性别默认为男（输入q或Q退出）：')
        student=student.strip()
        if student.upper()=='Q':
            print('系统退出')
            break
        else:
            student_list=student.split()
            if len(student_list)==4:
                func(filename,student_list[0],student_list[1],student_list[2],student_list[3])
            elif len(student_list)==3:
                func(filename,student_list[0], student_list[1], student_list[2])
            else:
                print('输入的数据格式不对，请重新输入！')

原始文件filename.txt：
张三 3 大专 男
李四四 44 本科 女
王五 5 中专 男

请输入要修改的文件名（输入q或Q退出)：filename
请输入要修改的姓名、年龄、学历、性别，以空格分隔，性别默认为男（输入q或Q退出）：李四四 10 小学 女
请输入要修改的姓名、年龄、学历、性别，以空格分隔，性别默认为男（输入q或Q退出）：诸葛亮 54 硕士
请输入要修改的姓名、年龄、学历、性别，以空格分隔，性别默认为男（输入q或Q退出）：q

更新后的文件filename.txt：
张三 3 大专 男
李四四 10 小学 女
王五 5 中专 男
诸葛亮 54 硕士 男
```

