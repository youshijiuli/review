

1. 手写s=【1，2，3】w=[4,5,6] z=[(1,4),(2,5),{3,6}] 这个实现  
2. 手写socket服务客户端与客户     
3. 手写sql 分组计数  
4. 如何进行缓存  我有1kw的数据，想在redis里面缓存了最火的20w条数据  
5. 多线程与多进程的应用场景    
6. 有了全局锁(GIL)为什么还要LOCK？ 
7. 牵涉了粘包问题你怎么实现的 
8. 基本的linux命令   
9. git的基本命令 
10. 你用python的哪些框架



最开始问的项目
    然后主要问了redis,项目中怎么用redis的,Django-redis和redis你用哪种,区别
    怎么处理高并发
    怎么解决沾包
    TCP和udp的区别,简单说一下HTTP
    输入一个url到看到页面经历了啥
    RestfulAPI的规范,说完叫我说了一下常见的状态码
    看过Django源码吗？我跟他说了session 和admin的源码
    你了解服务器吗 Nginx和Apache,你选哪一个,区别
    我们发送get请求如何不使用缓存,从数据库里面取东西
    什么是二叉树，完全二叉树
    hash表的去重
    你平时遇到bug是怎么解决的,喜欢看什么技术网站,我想不起来,我说了restframework和RbbitMq和falsk的英文文档
    数据库的优化
    用过爬虫吗,怎么爬取谷歌浏览器上的数据,我回道的不太好,他跟我说怎么不考虑vpn因为中国上不了谷歌
    问了docker,我说我不会

    面完以后叫我手写代码
    1.给了一个需求,原材料,菜谱和菜，叫我实现Django的models设计,然后在views中写出他提供的要求,返回数据
    2.给定一个随机数组,随便输入一个数K,找出这个数组中低k大的数
      我用快排写了以后,他说时间复杂度高了,重新考虑一下时间复杂度为n的,
      letcode https://leetcode.com/problems/kth-largest-element-in-an-array/description/
    3.不好描述 是letcode91题https://leetcode.com/problems/decode-ways/description/
http://www.cnblogs.com/skiler/category/1008825.html




面试题
1. 说一下python的GIL锁
2. Linux熟悉吗？
3. Git熟练嘛？`git add a.txt`的时候，都干了什么？
4. 你是怎么使用Docker的？
5. 说说我们这个职位对应的业务？docker在里面起到什么作用？
5. MySQL高可用知道吗？
6. XSS攻击说一下
7. Tornado用过没？他与其它Web框架的区别？
8. 说一下快排如何实现
9. 你在学这些技术的过程中，觉得哪里亮点高？
10. Linux中你开一个进程，在里面打开了一个文件，那么当你创建一个子进程的时候，这个文件状态是什么样子的？
    - 后来发现这是个坑，回答完之后，他又问我：“那如果我现在在一个进程中创建一个网络连接，通过这个进程创建一个子进程，子进程中有这个网络连接吗？如果没有，为什么？如果有，如何实现通信的？”
11. 有没有看过什么源码？








1. python基础数据类型
2. lambda表达式
3. map,filter,reduce是什么
4. 写一个排序
5. 贪婪匹配和非贪婪匹配
6. 常用的编辑器以及快捷键




