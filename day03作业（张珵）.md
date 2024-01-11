Day03作业及默写

1. # 有变量name = "aleX leNb" 完成如下操作：

   - 移除 name 变量对应的值两边的空格,并输出处理结果

   - ```
     name = "aleX leNb"
     print(name.strip())
     
     输出结果：aleX leNb
     ```

   - 判断 name 变量是否以 "al" 开头,并输出结果

   - ```python
     name = "aleX leNb"
     print(name.startswith('al'))
     
     输出结果：True
     ```

   - 判断name变量是否以"Nb"结尾,并输出结果

   - ```
     name = "aleX leNb"
     print(name.endswith('Nb'))
     
     输出结果：True
     ```

   - 将 name 变量对应的值中的所有的"l" 替换为 "p",并输出结果

   - ```
     name = "aleX leNb"
     print(name.replace('l','p'))
     
     输出结果：apeX peNb
     ```

   - 将name变量对应的值中的第一个"l"替换成"p",并输出结果

   - ```
     name = "aleX leNb"
     print(name.replace('l','p',1))
     
     输出结果：apeX leNb
     ```

     将 name 变量对应的值根据所有的"l" 分割,并输出结果。

   - ```
     name = "aleX leNb"
     print(name.split('l'))
     
     输出结果：['a', 'eX ', 'eNb']
     ```

   - 将name变量对应的值根据第一个"l"分割,并输出结果。

   - ```
     name = "aleX leNb"
     print(name.split('l',1))
     
     输出结果：['a', 'eX leNb']
     ```

     将 name 变量对应的值变大写,并输出结果

   - ```
     name = "aleX leNb"
     print(name.upper())
     
     输出结果：ALEX LENB
     ```

     将 name 变量对应的值变小写,并输出结果

     ```
     name = "aleX leNb"
     print(name.lower())
     
     输出结果：alex lenb
     ```

     判断name变量对应的值字母"l"出现几次，并输出结果

   - ```
     name = "aleX leNb"
     print(name.count('l'))
     
     输出结果：2
     ```

     如果判断name变量对应的值前四位"l"出现几次,并输出结果

     ```
     name = "aleX leNb"
     print(name.count('l',0,4))
     #实际判断的字符串为aleX
     
     输出结果：1
     ```

   - 请输出 name 变量对应的值的第 2 个字符?

   - ```
     name = "aleX leNb"
     print(name[1])
     
     输出结果：l
     ```

   - 请输出 name 变量对应的值的前 3 个字符?

   - ```
     name = "aleX leNb"
     print(name[:3])
     
     输出结果：ale
     ```

   - 请输出 name 变量对应的值的后 2 个字符?

   - ```
     name = "aleX leNb"
     print(name[-2:])
     
     输出结果：Nb
     ```

2.有字符串s = "123a4b5c"

- 通过对s切片形成新的字符串s1,s1 = "123"

- ```
  s = "123a4b5c"
  print(s[:3])
  ```

- 通过对s切片形成新的字符串s2,s2 = "a4b"

- ```
  s = "123a4b5c"
  print(s[3:6])
  ```

- 通过对s切片形成新的字符串s3,s3 = "1345"

- ```
  s = "123a4b5c"
  print(s[::2])
  ```

- 通过对s切片形成字符串s4,s4 = "2ab"

- ```
  s = "123a4b5c"
  print(s[1:6:2])
  ```

- 通过对s切片形成字符串s5,s5 = "c"

- ```
  s = "123a4b5c"
  print(s[-1])
  ```

- 通过对s切片形成字符串s6,s6 = "ba2"

- ```
  s = "123a4b5c"
  print(s[5:0:-2])
  ```

  或

  ```
  s = "123a4b5c"
  print(s[5::-2])
  ```

  使用while和for循环分别打印字符串s="asdfer"中每个元素。

  ```
  s="asdfer"
  i=0
  while i<=len(s)-1:
      print(s[i])
      i+=1
  ```

  ```
  s="asdfer"
  for i in s:
      print(i)
  ```

1. 使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"。

   ```
   s="asdfer"
   for i in s:
       print(s)
   ```

2. 使用for循环对s="abcdefg"进行循环，每次打印的内容是每个字符加上sb， 例如：asb, bsb，csb,...gsb。

   ```
   s="abcdefg"
   for i in s:
       print(i+'sb')
   ```

3. 使用for循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。

   ```
   s="321"
   for i in s:
       print('倒计时'+i+'秒')
   print('出发！')
   ```

4. 实现一个整数加法计算器(两个数相加)：

如：content = input("请输入内容:") 用户输入：5+9或5+ 9或5 + 9，然后进行分割再进行计算。

```
content = input("请输入内容:")

#去掉字符串中的所有空格
content2 = content.replace(' ','')

#按+对字符串进行切割
content3 = content2.split('+')    

#把content3每个元素转化为int，然后相加
print(int(content3[0])+int(content3[1]))
```



1. **选做题**：实现一个整数加法计算器（多个数相加）：

如：content = input("请输入内容:") 用户输入：5+9+6 +12+ 13，然后进行分割再进行计算。

```python
content = input("请输入内容:")

#去掉字符串中的所有空格
content2 = content.replace(' ','')

#按+对字符串进行切割
content3 = content2.split('+')

#获取content3中的元素个数
N=len(content3)

i=0
sum=0
while i <= N-1:
    sum = sum + int(content3[i])	#别忘把字符串格式的数字转化为int
    i += 1
print(sum)
```

1. 计算用户输入的内容中有几个整数（以个位数为单位）。

 如：content = input("请输入内容：") # 如fhdal234slfh98769fjdla

```python
content = input("请输入内容：")
n=0
for i in content:
    if i.isdecimal():
        n += 1
print(n)
```

1. **选做题**：写代码，完成下列需求：

用户可持续输入（用while循环），用户使用的情况：

输入A，则显示走大路回家，然后在让用户进一步选择：

是选择公交车，还是步行？

选择公交车，显示10分钟到家，并退出整个程序。

选择步行，显示20分钟到家，并退出整个程序。

输入B，则显示走小路回家，并退出整个程序。

输入C，则显示绕道回家，然后在让用户进一步选择：

是选择游戏厅玩会，还是网吧？

选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。

选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。

```python
while True:
    x = input('请输入A、B或C：')
    if x=='A':
        xa = input('走大路回家，请输入“公交车”或“步行：”')
        if xa=='公交车':
            print('10分钟到家')
            break
        else:
            print('20分钟到家')
            break
    elif x=='B':
        print('走小路回家')
        break
    else:
        xc = input('绕道回家，请输入“游戏厅”或“网吧”：')
        if xc == '游戏厅':
            print('一个半小时到家，爸爸在家，拿棍等你。')
        else:
            print('两个小时到家，妈妈已做好了战斗准备。')
```

1. 写代码：计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和？

   ```
   sum=0
   x=1
   y=1
   while x<=99:
       if y!=-88:
           sum += y
       x=x+1
       y=x*((-1)**(x+1))
   print(sum)
   
   输出结果：138
   ```

2. **选做题：**选做题：判断一句话是否是回文. 回文: 正着念和反着念是一样的. 例如, 上海自来水来自海上

   ```
   x=input('请输入一句话：')
   y=x[::-1]
   if x==y:
       print('这是回文')
   else:
       print('这不是回文')
   ```

3. 制作趣味模板程序需求：等待用户输入名字、地点、爱好，根据用户的名字和爱好进行任意现实 如：敬爱可亲的xxx，最喜欢在xxx地方干xxx

   方法1

   ```python
   x=input('请输入名字：')
   y=input('请输入地点：')
   z=input('请输入爱好：')
   msg = '敬爱可亲的{name}，最喜欢在{where}地方干{hobby}'.format(name=x,where=y,hobby=z)
   print(msg)
   ```

   方法2

   ```python
   x=input('请输入名字：')
   y=input('请输入地点：')
   z=input('请输入爱好：')
   msg = '敬爱可亲的{0}，最喜欢在{1}地方干{2}'.format(x,y,z)
   print(msg)
   ```



