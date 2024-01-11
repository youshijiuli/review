Day2作业及默写

1. # 判断下列逻辑语句的True,False.
   
   1）1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6

   =False or True or False and True and True or False
   
   =False or True or ( False and True and True ) or False
   
   =False or True or ( False and True ) or False
   
   =False or True or False or False
   
   =True or False or False
   
   =True of False
   
   =True
   
   2）not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6 
   
   = (not 2 > 1) and 3 < 4 or ( 4 > 5 and 2 > 1 and 9 > 8 ) or 7 < 6 
   
   = False and True or (False and True and True) or False
   
   = False and True or (False and True) or False
   
   = False and True or False or False
   
   = False or False or False
   
   = False or False
   
   = False
   
2. # 求出下列逻辑语句的值。
   
   1),8 or 3 and 4 or 2 and 0 or 9 and 7

   = 8 or (3 and 4) or (2 and 0) or (9 and 7)
   
   = 8 or 4 or 0 or 7
   
   = 8 or 0 or 7
   
   = 8 or 7
   
   = 8
   
   2),0 or 2 and 3 and 4 or 6 and 0 or 3
   
   = 0 or (2 and 3 and 4) or (6 and 0) or 3
   
   = 0 or (3 and 4) or 0 or 3
   
   = 0 or 4 or 0 or 3
   
   = 4 or 0 or 3
   
   = 4 or 3
   
   = 4
   
3. # 下列结果是什么？
   
   1)、6 or 2 > 1
   
   = 6 or True
   
   = 6
   
   2)、3 or 2 > 1
   
   = 3 or True

   =3
   
   3)、0 or 5 < 4
   
   = 0  or  False
   
   = False
   
   4)、5 < 4 or 3
   
   = False or 3
   
   =3
   
   5)、2 > 1 or 6
   
   =True or 6
   
   =True
   
   6)、3 and 2 > 1
   
   =3 and True
   
   =True
   
   7)、0 and 3 > 1
   
   =0 and True
   
   =0
   
   8)、2 > 1 and 3
   
   =True and 3
   
   =3
   
   9)、3 > 1 and 0
   
   =True and 0
   
   =0
   
   10)、3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2
   
   = True and 2 or True and 3 and 4 or True
   
   = (True and 2) or (True and 3 and 4) or True
   
   = 2 or (3 and 4) or True
   
   =2 or 4 or True
   
   =2 or True
   
   =2
   
4. # while循环语句基本结构？

   ```python
   while 条件:
       循环体
   ```

   

5. # 利用while语句写出猜大小的游戏：

   设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确，然后退出循环。

   ```python
   bingo=66
   while True:
       x = int(input('请输入猜测的数字：'))
       if x<bingo:
           print('猜测的结果小了')
       elif x>bingo:
           print('猜测的结果大了')
       elif x==bingo:
           print('猜测结果正确')
           break
   ```

6. # 在5题的基础上进行升级：

   给用户三次猜测机会，如果三次之内猜测对了，则显示猜测正确，退出循环，如果三次之内没有猜测正确，则自动退出循环，并显示‘太笨了你....’。

   ```python
   time=1
   bingo=66
   while time<=3:
       x = int(input('请输入猜测的数字：'))
       time = time + 1
       if x<bingo:
           print('猜测的结果小了')
       elif x>bingo:
           print('猜测的结果大了')
       else:
           print('猜测结果正确')
           break
   else:
       print('你太笨了...')
   ```

   

7. # 使用while循环输出 1 2 3 4 5 6 8 9 10

   ```python
   x=0
   y=''
   while x<=9:
       x = x + 1
       if x==7:
           continue
       else:
           y=y+' '+str(x)
   print(y)
   ```

   输出结果： 1 2 3 4 5 6 8 9 10

8. 求1-100的所有数的和

   ```python
   sum=0
   x=1
   while x<=100:
       sum=sum+x
       x=x+1
   print(sum)
   ```

   输出结果：5050

9. # 输出 1-100 内的所有奇数

   ```python
   x=1
   while x<=100:
       if x % 2 == 1:
           print(x)
       x=x+1
   ```

10. # 输出 1-100 内的所有偶数

    ```python
    x=1
    while x<=100:
        if x % 2 == 0:
            print(x)
        x=x+1
    ```

11. # 求1-2+3-4+5 ... 99的所有数的和

    ```python
    sum=0
    x=1
    y=1
    while x<=99:
        sum += y
        x=x+1
        y=x*((-1)**(x+1))
    print(sum)
    ```

    输出结果：50

12. # 用户登录（三次输错机会）且每次输错误时显示剩余错误次数（提示：使用字符串格式化）

    ```python
    code = 'qwer'
    time_left = 3
    while time_left>=1:
        username = input('请输入用户名：')
        password = input('请输入密码：')
        your_code = input('请输入验证码：')
        if your_code == code:
            if username == 'zhangcheng' and password == '123456':
                print('登录成功')
                break
            else:
                time_left = time_left - 1
                print('账号或者密码错误，您还剩%d次机会' % (time_left))
        else:
            print('验证码错误')
    else:
        print('已输错三次，自动退出')
    ```
    
13. # 简述ASCII、Unicode、utf-8编码

    ASCII：只包含英文字母，数字，特殊字符。均占8位（1字节）

    Unicode：万国码，包括世界上所有的文字，不论中文、英文或符号，每个字符均占32位（4字节）。浪费空间，浪费资源。

    utf-8：万国码升级版，英文占8位（1字节）、欧洲字符占16位（2字节）、中文字符站24位（3字节）

14. # 简述位和字节的关系？

    8位=1字节


