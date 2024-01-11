**day07 作业（张珵）**

1. 看代码写结果

   ```
   v1 = [1,2,3,4,5]
   v2 = [v1,v1,v1]
   
   v1.append(6)
   print(v1)
   print(v2)
   
   输出结果：
   [1,2,3,4,5,6]
   [[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]
   ```

2. 看代码写结果

   ```
   v1 = [1,2,3,4,5]
   v2 = [v1,v1,v1]
   
   v2[1][0] = 111
   v2[2][0] = 222
   print(v1)
   print(v2)
   
   输出结果：
   [222, 2, 3, 4, 5]
   [[222, 2, 3, 4, 5], [222, 2, 3, 4, 5], [222, 2, 3, 4, 5]]
   ```

3. 看代码写结果，并解释每一步的流程。

   ```
   v1 = [1,2,3,4,5,6,7,8,9]
   v2 = {}
   
   for item in v1:
       if item < 6:
           continue
       if 'k1' in v2:
           v2['k1'].append(item)
   	else:
           v2['k1'] = [item ]
   print(v2)
   
   解释：
   v1=1，continue
   v1=2，continue
   v1=3，continue
   v1=4，continue
   v1=5，continue
   v1=6，v2={'k1':[6]}
   v1=7，v2={'k1':[6,7]}
   v1=8，v2={'k1':[6,7,8]}
   v1=9，v2={'k1':[6,7,8,9]}
   ```

4. 简述深浅拷贝？

   浅拷贝：拷贝目标可变对象（list, dict, set）时，仅为第一层可变对象分配新的内存地址，第二层及以上的可变对象沿用之前对象的内存地址，此外所有层的不可变对象（int, str, bool, tuple）均沿用之前对象的内存地址。

   深拷贝：拷贝目标可变对象（list, dict, set）时，为所有层的可变对象分配新的内存地址，此外所有层的不可变对象（int, str, bool, tuple）均沿用之前对象的内存地址。

5. 看代码写结果

   ```
   import copy
   
   v1 = "alex"
   v2 = copy.copy(v1)
   v3 = copy.deepcopy(v1)
   
   print(v1 is v2)
   print(v1 is v3)
   
   输出结果：
   True
   True
   类型为str，因此无论深浅拷贝，内存指向都相同
   ```

6. 看代码写结果

   ```
   import copy
   
   v1 = [1,2,3,4,5]
   v2 = copy.copy(v1)
   v3 = copy.deepcopy(v1)
   
   print(v1 is v2)
   print(v1 is v3)
   
   输出结果：
   False
   False
   ```

7. 看代码写结果

   ```
   import copy
   
   v1 = [1,2,3,4,5]
   
   v2 = copy.copy(v1)
   v3 = copy.deepcopy(v1)
   
   print(v1[0] is v2[0])
   print(v1[0] is v3[0])
   print(v2[0] is v3[0])
   
   输出结果：
   True
   True
   True
   由于列表中的元素都是int，因此无论深浅拷贝，内存指向都相同
   ```

8. 看代码写结果

   ```
   import copy
   
   v1 = [1,2,3,4,[11,22]]
   v2 = copy.copy(v1)
   v3 = copy.deepcopy(v1)
   
   print(v1[-1] is v2[-1])
   print(v1[-1] is v3[-1])
   print(v2[-1] is v3[-1])
   
   输出结果：
   True
   False
   False
   ```

9. 看代码写结果

   ```
   import copy
   
   v1 = [1,2,3,{"name":'太白',"numbers":[7,77,88]},4,5]
   v2 = copy.copy(v1)
   
   print(v1 is v2)
   
   print(v1[0] is v2[0])
   print(v1[3] is v2[3])
   
   print(v1[3]['name'] is v2[3]['name'])
   print(v1[3]['numbers'] is v2[3]['numbers'])
   print(v1[3]['numbers'][1] is v2[3]['numbers'][1])
   
   输出结果：
   False
   True
   True
   True
   True
   True
   ```

10. 看代码写结果

    ```
    import copy
    
    v1 = [1,2,3,{"name":'太白',"numbers":[7,77,88]},4,5]
    
    v2 = copy.deepcopy(v1)
    
    print(v1 is v2)
    
    print(v1[0] is v2[0])
    print(v1[3] is v2[3])
    
    print(v1[3]['name'] is v2[3]['name'])
    print(v1[3]['numbers'] is v2[3]['numbers'])
    print(v1[3]['numbers'][1] is v2[3]['numbers'][1])
    
    输出结果：
    False
    True
    False
    True
    False
    True
    ```

11. 请说出下面a,b,c三个变量的数据类型。

```
​```python
a = ('太白金星')
b = (1,)
c = ({'name': 'barry'})
​```
a是str，b是tuple，c是dict
```

1. 按照需求为列表排序：

   ```
   l1 = [1, 3, 6, 7, 9, 8, 5, 4, 2]
   # 从大到小排序
   l1.sort(reverse=True)
   
   # 从小到大排序
   l1.sort()
   
   # 反转l1列表
   l1.reverse()
   ```

2. 利用python代码构建一个这样的列表(**升级题**)：

   ```
   [['_','_','_'],['_','_','_'],['_','_','_']]
   
   ['_']*3是['_','_','_']
   [['_']*3]*3是[['_','_','_'],['_','_','_'],['_','_','_']]
   ```

3. 看代码写结果：

   ```
   l1 = [1,2,]
   l1 += [3,4]
   print(l1)
   
   输出结果：[1, 2, 3, 4]
   ```

4. 看代码写结果：

```
​```python 
dic = dict.fromkeys('abc',[])
dic['a'].append(666)
dic['b'].append(111)
print(dic)
​```

输出结果：{'a': [666, 111], 'b': [666, 111], 'c': [666, 111]}
```

1. l1 = [11, 22, 33, 44, 55]，请把索引为奇数对应的元素删除（不能一个一个删除，此l1只是举个例子，里面的元素不定）

   ```
   l1 = [11, 22, 33, 44, 55]
   del l1[1::2]
   print(l1)
   
   输出结果：[11, 33, 55]
   ```

2. dic = {'k1':'太白','k2':'barry','k3': '白白', 'age': 18} 请将字典中所有键带k元素的键值对删除.

   ```
   dic = {'k1':'太白','k2':'barry','k3': '白白', 'age': 18}
   dic_new={}
   for i in dic.keys():
       if 'k' not in i:
           dic_new.setdefault(i,dic[i])
   print(dic_new)
   
   输出结果：{'age': 18}
   ```

3. bytes数据类型是python的基础数据类型，bytes类型存在的意义是什么？

   由于在计算机内存中，除bytes外，所有的数据都是Unicode编码，当需要将数据保存到硬盘或者需要网络传输的时候，需要转换为非Unicode编码，因此需要将目标数据转换为非Unicode编码的bytes（字节文本），以用于网络的数据传输与数据存储。

4. 列举bytes类型与str类型的三个不同点？

   bytes编码方式为非Unicode，str编码方式为Unicode

   bytes组成形式为b'' 或者 b""  或者 b''' ''' 或者 b""" """，str组成形式为'' 或者 "" 或者 ''' ''' 或者 """ """

   bytes组成单位是字节，str组成单位是字符

5. 完成下列需求：

   ```
   s1 = '太白金星'
   # 将s1转换成utf-8的bytes类型。
   b1 = s1.encode('utf-8')
   
   # 将s1转化成gbk的bytes类型。
   b2 = s1.encode('gbk')
   
   b = b'\xe5\xa4\xaa\xe7\x99\xbd\xe6\x9c\x80\xe5\xb8\x85'
   # b为utf-8的bytes类型，请转换成gbk的bytes类型。
   b_gbk=b.decode('utf-8').encode('gbk')
   ```

6. 用户输入一个数字，判断一个数是否是水仙花数。

   水仙花数是一个三位数, 三位数的每一位的三次方的和还等于这个数. 那这个数就是一个水仙花数,

   ```
   例如: 153 =1**3 + 5**3 + 3**3
   ```

   ```python
   x=input('请输入一个三位数：').strip()
   if x.isdecimal():
       x=int(x)
       if x>=100 and x<=999:
           a=x//100
           b=(x-a*100)//10
           c=x-a*100-b*10
           if x==a**3+b**3+c**3:
               print('该数字是水仙花数！')
           else:
               print('该数字不是水仙花数！')
       else:
           print('您输入的不是三位数！')
   else:
       print('您输入的不是纯数字！')
   ```

7. 把列表中所有姓周的人的信息删掉(此题有坑, 请慎重):

   lst = ['周老二', '周星星', '麻花藤', '周扒皮']

   结果: lst = ['麻花藤']

   方法一：添加补集

   ```
   lst = ['周老二', '周星星', '麻花藤', '周扒皮']
   lst2=[]
   for i in lst:
       if i[0]!='周':
           lst2.append(i)
   print(lst2)
   
   输出结果：['麻花藤']
   ```

   方法二：倒序删除

   ```
   lst = ['周老二', '周星星', '麻花藤', '周扒皮']
   for i in range(len(lst)-1,-1,-1):
       if lst[i][0]=='周':
           lst.pop(i)
   print(lst)
   ```

8. 车牌区域划分, 现给出以下车牌. 根据车牌的信息, 分析出各省的车牌持有量. (**选做题**)

   cars = ['鲁A32444','鲁B12333','京B8989M','黑C49678','黑C46555','沪B25041'.....]

   locals = {'沪':'上海', '黑':'黑龙江', '鲁':'山东', '鄂':'湖北', '湘':'湖南'.....}

   结果: {'黑龙江':2, '山东': 1, '北京': 1}

   【推荐方法二：在循环中给字典动态添加键值对的思想——没有键则创建键，有此键则值加1】
   
   方法一：
   
   ```
   cars = ['鲁A32444','鲁B12333','京B8989M','黑C49678','黑C46555','沪B25041']
   locals = {'沪':'上海', '黑':'黑龙江', '鲁':'山东', '鄂':'湖北', '湘':'湖南', '京':'北京'}
   heads=[]    #cars字头组成的列表
   for i in cars:
       heads.append(i[0])
   heads_no_repeat=list(set(heads))    #cars字头组成的列表（剔除重复项）
   result={}
   for j in heads_no_repeat:
       result[locals[j]]=heads.count(j)
   print(result)
   
   输出结果：{'黑龙江': 2, '上海': 1, '山东': 2, '北京': 1}
   ```
   
   方法二：在循环中给字典动态添加键值对的思想——没有键则创建键，有此键则值加1
   
   ```
   cars = ['鲁A32444','鲁B12333','京B8989M','黑C49678','黑C46555','沪B25041']
   locals = {'沪':'上海', '黑':'黑龙江', '鲁':'山东', '鄂':'湖北', '湘':'湖南', '京':'北京'}
   result={}
   for i in cars:
   	if locals[i[0]] in result:
   		result[locals[i[0]]] += 1
   	else:
   		result[locals[i[0]]] = 1
   print(result)
   
   输出结果：{'山东': 2, '北京': 1, '黑龙江': 2, '上海': 1}
   ```
   
   方法三：适用面窄
   
   ```
   cars = ['鲁A32444','鲁B12333','京B8989M','黑C49678','黑C46555','沪B25041']
   locals = {'沪':'上海', '黑':'黑龙江', '鲁':'山东', '鄂':'湖北', '湘':'湖南', '京':'北京'}
   result={}
   for i in cars:
       result[locals[i[0]]]=result.get(locals[i[0]],0)+1
   print(result)
   
   输出结果：{'山东': 2, '北京': 1, '黑龙江': 2, '上海': 1}
   ```
   
   



