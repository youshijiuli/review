## day06 作业

 

1. 请用代码验证 "name" 是否在字典的键中？

   info = {'name':'王刚蛋','hobby':'铁锤','age':'18',...100个键值对}

   ```
   print('name' in info.keys())
   ```

2. 请用代码验证 "alex" 是否在字典的值中？

   info = {'name':'王刚蛋','hobby':'铁锤','age':'18',...100个键值对}

   ```
   print('alex' in info.values())
   ```

3. 有如下

   ```
   v1 = {'武沛齐','李杰','太白','景女神'}
   v2 = {'李杰','景女神}
   ```

   - 请得到 v1 和 v2 的交集并输出

     ```
     print(v1 & v2)
     
     输出结果：{'景女神', '李杰'}
     ```

   - 请得到 v1 和 v2 的并集并输出

   - ```
     print(v1 | v2)
     
     输出结果：{'武沛齐', '太白', '景女神', '李杰'}
     ```

   - 请得到 v1 和 v2 的 差集并输出

   - ```
     print(v1 - v2)
     
     输出结果：{'太白', '武沛齐'}
     ```

   - 请得到 v2 和 v1 的 差集并输出

   - ```
     print(v2 - v1)
     
     输出结果：set()
     ```

4. 循环提示用户输入，并将输入内容追加到列表中（如果输入N或n则停止循环）

   ```
   l=[]
   while 1:
       x=input('请输入内容：').strip()
       if x.upper()=='N':
           break
       else:
           l.append(x)
           print(l)
           
   输出结果：
   请输入内容：abc
   ['abc']
   请输入内容：1
   ['abc', '1']
   请输入内容：哈哈
   ['abc', '1', '哈哈']
   请输入内容：n
   ```

5. 循环提示用户输入，并将输入内容添加到集合中（如果输入N或n则停止循环）

   ```
   s=set()
   while 1:
       x=input('请输入内容：').strip()
       if x.upper()=='N':
           break
       else:
           s.add(x)
           print(s)
           
   输出结果：
   请输入内容：1
   {'1'}
   请输入内容：a
   {'a', '1'}
   请输入内容：b
   {'a', '1', 'b'}
   请输入内容：a
   {'a', '1', 'b'}
   请输入内容：n
   ```

   

6. 写代码实现

   ```
   v1 = {'alex','武sir','肖大'}
   v2 = []
   
   # 循环提示用户输入，如果输入值在v1中存在，则追加到v2中，如果v1中不存在，则添加到v1中。（如果输入N或n则停止循环）
   
   while 1:
       x=input('请输入内容：').strip()
       if x.upper()=='N':
           break
       elif x in v1:
           v2.append(x)
           print('v2=',v2)
       else:
           v1.add(x)
           print('v1=',v1)
   
   请输入内容：a
   v1= {'武sir', 'alex', 'a', '肖大'}
   请输入内容：alex
   v2= ['alex']
   请输入内容：肖大
   v2= ['alex', '肖大']
   请输入内容：n
   ```

7. 判断以下值那个能做字典的key ？那个能做集合的元素？

   - 1：能，能
   - -1：能，能
   - ""：能，能
   - None：能，能
   - [1,2]：不能，不能
   - (1,)：能，能
   - {11,22,33,4}：不能，不能
   - {'name':'wupeiq','age':18}：不能，不能

8. is 和 == 的区别？

   ==比较二者的值是否相同，is比较二者指向的内存地址是否相同

9. type使用方式及作用？

   type()，判断给定数据的数据类型

10. id的使用方式及作用？

    获取对象的内存地址

11. 看代码写结果并解释原因

    ```
    v1 = {'k1':'v1','k2':[1,2,3]}
    v2 = {'k1':'v1','k2':[1,2,3]}
    
    result1 = v1 == v2 
    result2 = v1 is v2 
    print(result1)
    print(result2)
    
    输出结果：
    True
    False
    ```

    ==比较二者的值是否相同，所以result1返回True

    is比较二者指向的内存地址是否相同，由于v1和v2数据类型为dict，不满足“同一个代码块内的缓存机制”的条件（所有int、所有bool、几乎所有str），因此v1和v2会被指向不同的内存地址。因此，result2返回结果False。

12. 看代码写结果并解释原因

    ```
    v1 = {'k1':'v1','k2':[1,2,3]}
    v2 = v1
    
    result1 = v1 == v2 
    result2 = v1 is v2 
    print(result1)
    print(result2)
    
    输出结果：
    True
    True
    ```

    ==比较二者的值是否相同，所以result1返回True

    is比较二者指向的内存地址是否相同，v2=v1使得v2和v1指向同一个内存地址，所以result2返回True

13. 看代码写结果并解释原因

    ```
    v1 = {'k1':'v1','k2':[1,2,3]}
    v2 = v1
    
    v1['k1'] = 'wupeiqi'
    print(v2)
    
    输出结果：{'k1': 'wupeiqi', 'k2': [1, 2, 3]}
    ```

    v2=v1使得v2与v1指向相同的内存地址，v1['k1'] = 'wupeiqi'仅改变v1的值未改变v1的指向

    

14. 看代码写结果并解释原因

    ```
    v1 = '人生苦短，我用Python'
    v2 = [1,2,3,4,v1]
    
    v1 = "人生苦短，用毛线Python"
    
    print(v2)
    
    输出结果：[1, 2, 3, 4, '人生苦短，我用Python']
    ```

    对v1重新赋值，仅改变了v1的内存指向，未改变v2[-1]的内存指向的值

    

15. 看代码写结果并解释原因

    ```
    info = [1,2,3]
    userinfo = {'account':info, 'num':info, 'money':info}
    
    info.append(9)
    print(userinfo)
    
    info = "题怎么这么多"
    print(userinfo)
    
    输出结果：{'account': [1, 2, 3, 9], 'num': [1, 2, 3, 9], 'money': [1, 2, 3, 9]}
    {'account': [1, 2, 3, 9], 'num': [1, 2, 3, 9], 'money': [1, 2, 3, 9]}
    ```

    info是list，属于可变类型数据，info.append(9)仅改变了info的值不改变其内存指向，但info = "题怎么这么多"这个赋值语句改变了info的指向，userinfo里面值的指向并未因此发生改变，故其值仍为[1,2,3,9]

    

16. 看代码写结果并解释原因

    ```
    info = [1,2,3]
    userinfo = [info,info,info,info,info]
    
    info[0] = '不仅多，还特么难呢'
    print(info,userinfo)
    
    输出结果：['不仅多，还特么难呢', 2, 3] [['不仅多，还特么难呢', 2, 3], ['不仅多，还特么难呢', 2, 3], ['不仅多，还特么难呢', 2, 3], ['不仅多，还特么难呢', 2, 3], ['不仅多，还特么难呢', 2, 3]]
    ```

    info是list，属于可变类型数据，info[0]仅改变了info的值不改变其内存指向，因此userinfo里的每一项都会跟着变

    

17. 看代码写结果并解释原因

    ```
    info = [1,2,3]
    userinfo = [info,info,info,info,info]
    
    userinfo[2][0] = '闭嘴'
    print(info,userinfo)
    
    输出结果：['闭嘴', 2, 3] [['闭嘴', 2, 3], ['闭嘴', 2, 3], ['闭嘴', 2, 3], ['闭嘴', 2, 3], ['闭嘴', 2, 3]]
    ```

    info是list，属于可变类型数据，userinfo [ 2 ] [ 0 ]仅改变了info的值不改变其内存指向，因此userinfo里的每一项都会跟着变

    

18. 看代码写结果并解释原因

    ```
    info = [1,2,3]
    user_list = []
    for item in range(10):
        user_list.append(info)
        
    info[1] = "是谁说Python好学的？"
    
    print(user_list)
    
    输出结果：[[1, '是谁说Python好学的？', 3], [1, '是谁说Python好学的？', 3], [1, '是谁说Python好学的？', 3], [1, '是谁说Python好学的？', 3], [1, '是谁说Python好学的？', 3], [1, '是谁说Python好学的？', 3], [1, '是谁说Python好学的？', 3], [1, '是谁说Python好学的？', 3], [1, '是谁说Python好学的？', 3], [1, '是谁说Python好学的？', 3]]
    ```

    info是list，属于可变类型数据，info[1]仅改变了info的值不改变其内存指向，因此user_list里的每一项都会跟着变

    

19. 看代码写结果并解释原因

    ```
    data = {}
    for i in range(10):
        data['user'] = i
    print(data)
    
    输出结果：{'user': 9}
    ```

    字典的键具有唯一性，i=0,1,2....9，每次给键赋值时，都会覆盖掉上一次的，因此最后留下的值是9

    

20. 看代码写结果并解释原因

    ```
    data_list = []
    data = {}
    for i in range(10):
        data['user'] = i
        data_list.append(data)
    print(data_list)
    
    输出结果：[{'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}, {'user': 9}]
    ```

    data数据类型是dict，是可变的数据类型，因此每次追加到data_list里的data指向都是相同的，每次迭代仅改变data的值，因此data_list里的十个字典最终将指向相同的内存地址。

    

21. 看代码写结果并解释原因

    ```
    data_list = []
    for i in range(10):
        data = {}
        data['user'] = i
        data_list.append(data)
    print(data_list)
    
    输出结果：[{'user': 0}, {'user': 1}, {'user': 2}, {'user': 3}, {'user': 4}, {'user': 5}, {'user': 6}, {'user': 7}, {'user': 8}, {'user': 9}]
    ```

    由于每次迭代都对data进行重新赋值，使得每次都指向一个新的内存地址，因此data_list里的十个data的指向各不相同

    

22. 使用循环打印出一下效果：

- ```
  for i in range(1,6):
      print('*'*i)
  ```

```
* 
** 
*** 
**** 
***** 
```

- ```
  for i in range(4,0,-1):
      print('*'*i)
  ```

```
**** 
***
** 
*
```

- ```
  for i in range(1,10,2):
      print('*'*i)
  ```

```
* 
*** 
***** 
******* 
*********
```

1. 敲七游戏. 从1开始数数. 遇到7或者7的倍数（不包含17,27,这种数）要在桌上敲一下. 编程来完成敲七. 给出一个任意的数字n. 从1开始数. 数到n结束. 把每个数字都放在列表中, 在数的过程中出现7或 者7的倍数（不包含17,27,这种数）.则向列表中添加一个'咣'

   例如, 输入10. lst = [1, 2, 3, 4, 5, 6, '咣', 8, 9, 10]

```
x=int(input('请输入数字：').strip())
lst=[]
for i in range(1,x+1):
    if i % 7 == 0:
        lst.append('咣')
    else:
        lst.append(i)
print(lst)

请输入数字：50
[1, 2, 3, 4, 5, 6, '咣', 8, 9, 10, 11, 12, 13, '咣', 15, 16, 17, 18, 19, 20, '咣', 22, 23, 24, 25, 26, 27, '咣', 29, 30, 31, 32, 33, 34, '咣', 36, 37, 38, 39, 40, 41, '咣', 43, 44, 45, 46, 47, 48, '咣', 50]

```