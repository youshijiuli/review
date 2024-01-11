## 五一假期 额外作业，相关面试题

 

1. 如何实现字符串的反转？如： name = "wupeiqi" 请反转为 name ="iqiepuw"

   ```
   name = "wupeiqi"
   name = name[::-1]
   print(name)
   
   输出结果：iqiepuw
   ```

2. 如何实现 “1,2,3” 变成 [‘1’,’2’,’3’]

   ```
   x='1,2,3'
   print(x.split(','))
   
   输出结果：['1', '2', '3']
   ```

3. 如何实现[‘1’,’2’,’3’]变成[1,2,3]

   ```
   x=['1','2','3']
   for i in range(len(x)):
       x[i]=int(x[i])
   print(x)
   
   输出结果：[1, 2, 3]
   ```

4. 以下代码输出是什么? list=['a','b','c','d','e'] print list[10:]

   ```
   []
   ```

   

5. 现有一列表 alist, 请写出两种去除 alist 中重复元素的方法, 其中：（**难**）

   – 要求保持原有列表中元素的排列顺序。

   ```
   alist=['a','b','c','a','c','a','d','e','a','c']
   while 1:
       mark = 0
       for i in alist:
           if alist.count(i)>=2:
               alist.remove(i)
           else:
               mark=mark+1
       if mark==len(alist):
           break
   print(alist)
   
   输出结果：['b', 'd', 'e', 'a', 'c']
   ```

   – 无需考虑原有列表中元素的排列顺序（**超纲**）。

   ```
   不明白题干是啥意思。。。
   ```

6. 用 Python 实现 99 乘法表（**难**）

   ```
   print('   1  2  3  4  5  6  7  8  9')
   for i in range(1,10):
       print(i,end="")
       for j in range(1,10):
           if i*j<=9:
               print("  "+str(i*j),end="")
           else:
               print(" "+str(i*j),end="")
       print('\n')
       
   输出结果：
      1  2  3  4  5  6  7  8  9
   1  1  2  3  4  5  6  7  8  9
   
   2  2  4  6  8 10 12 14 16 18
   
   3  3  6  9 12 15 18 21 24 27
   
   4  4  8 12 16 20 24 28 32 36
   
   5  5 10 15 20 25 30 35 40 45
   
   6  6 12 18 24 30 36 42 48 54
   
   7  7 14 21 28 35 42 49 56 63
   
   8  8 16 24 32 40 48 56 64 72
   
   9  9 18 27 36 45 54 63 72 81
   ```