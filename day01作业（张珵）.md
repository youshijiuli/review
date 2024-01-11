Day1作业及默写

# 1.简述变量命名规范

- 变量全部由数字、字母、下划线任意组合；
- 不能以数字开头； 
- 不能是python的关键字；
  - ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
- 不能使用中文；
- 不能过长。

# 2.name = input(“>>>”) name变量是什么数据类型？

name变量数据类型为字符串。

# 3.if条件语句的基本结构？

## 单独if

```python
if 条件:
    结果
```

## if else 二选一

```python
if 条件:
    结果1
else:
    结果2
```

## if elif elif .... 多选一

```python
if 条件1:
    结果1
elif 条件2:
    结果2
elif 条件3:
    结果3
......
```

## if elif elif .... else 多选一

```python
if 条件1:
    结果1
elif 条件2:
    结果2
elif 条件3:
    结果3
......
else:
    结果N
```

## 嵌套的if

```python
if 条件1:
    if 条件2:
	    结果A
    else:
	    结果B
else:
    结果C
```

# 4.用print打印出下面内容：

```python
a='''
文能提笔安天下, 
武能上马定乾坤. 
心存谋略何人胜, 
古今英雄唯是君.
'''
print(a)
```

或

```python
a="""
文能提笔安天下, 
武能上马定乾坤. 
心存谋略何人胜, 
古今英雄唯是君.
"""
print(a)
```

或

```python
print('''
文能提笔安天下, 
武能上马定乾坤. 
心存谋略何人胜, 
古今英雄唯是君.
''')
```

或

```python
print("""
文能提笔安天下, 
武能上马定乾坤. 
心存谋略何人胜, 
古今英雄唯是君.
""")
```

# 5.利用if语句写出猜大小的游戏：

设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确。

```python
bingo=66
x=int(input('请输入您猜测的结果：'))
if x>bingo:
    print('猜测的结果大了！')
elif x<bingo:
    print('猜测的结果小了！')
else:
    print('猜测结果正确！')
```

# 6.提示户输入他的年龄, 程序进行判断：

如果小于10, 提示小屁孩, 如果大于10, 小于20, 提示青春期叛逆的小屁孩. 如果大于20, 小于30. 提示开始定性, 开始混社会的小屁孩儿, 如果大于30, 小于40. 提示看老大不小了, 赶紧结婚小屁孩儿. 如果大于40, 小于50. 提示家里有个不听话的小屁孩儿. 如果大于50, 小于60. 提示自己马上变成不听话的老屁孩儿.如果大于60, 小于70. 提示活着还不错的老屁孩儿. 如果大于70, 小于90. 提示人生就快结束了的一个个老屁孩儿.如果大于90以上.提示.再见了这个世界.

```python
x=int(input('请输入您的年龄：'))
if x<10:
    print('小屁孩')
elif x>=10 and x<20:
    print('青春期叛逆的小屁孩')
elif x>=20 and x<30:
    print('开始定性, 开始混社会的小屁孩儿')
elif x>=30 and x<40:
    print('看老大不小了, 赶紧结婚小屁孩儿')
elif x>=40 and x<50:
    print('家里有个不听话的小屁孩儿')
elif x>=50 and x<60:
    print('自己马上变成不听话的老屁孩儿')
elif x>=60 and x<70:
    print('活着还不错的老屁孩儿')
elif x>=70 and x<90:
    print('提示人生就快结束了的一个老屁孩儿')
else:
    print('再见了这个世界')
```

# 7.单行注释以及多行注释？

```python
#单行注释
```

```python
'''
多行注释
多行注释
'''
```

```python
"""
多行注释
多行注释
"""
```

# 8.简述你所知道的Python3x和Python2x的区别？

+ 在Python3x中，无论用户通过input功能输入什么内容，均视为字符串；而在Python2x中，则视为表达式，若要在Python2x中也要将input输入的内容视为字符串，则应该使用raw_input。
+ 

# 9.提示用户输入麻花藤. 判断用户输入的对不对. 如果对, 提示真聪明, 如果不对，提示输入有误

```python
x=input('请输入麻花藤：')
if x=='麻花藤':
    print('真聪明！')
else:
    print('输入有误！')
```

# 10.用户输入一个月份，然后判断月份是多少月，根据不同的月份，打印出不同的饮食（根据个人习惯和老家习惯随意编写）

```python
x=input('养生饮食查询，请输入一个月份：')
if x=='1':
    print('一月适合吃梨、栗子')
elif x=='2':
    print('二月适合吃卷心菜、莴苣、韭菜、鳕鱼')
elif x=='3':
    print('三月适合吃扇贝、鲑鱼、豆瓣菜、椰菜')
elif x=='4':
    print('四月适合吃鸡蛋、萝卜、椰菜')
elif x=='5':
    print('五月适合吃芦笋、菠菜、豌豆')
elif x=='6':
    print('六月适合吃蔬菜沙拉、樱桃、草莓')
elif x=='7':
    print('七月适合吃茴香、西红柿、杏')
elif x=='8':
    print('八月适合吃果酱、泡菜、鲑鱼')
elif x=='9':
    print('九月适合吃鱿鱼、南瓜、草莓、黄瓜')
elif x=='10':
    print('十月适合吃蘑菇、螃蟹、牡蛎')
elif x=='11':
    print('十一月适合吃龙虾、螃蟹、苹果')
elif x=='12':
    print('十二月适合吃熏肉、腊肠')
else:
    print("输入的月份不合法，请检查后重新输入")
```

# 11.用户输入一个分数，根据分数来判断用户考试成绩的档次

```python
x=int(input('请输入一个0到100的分数：'))
if x>=90:
    print('A')
elif x>=80:
    print('B')
elif x>=70:
    print('C')
elif x>=60:
    print('D')
else:
    print('不及格')
```

