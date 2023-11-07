[TOC]

# 简述websocket协议及实现原理

 WebSocket协议是基于TCP的一种新的协议。WebSocket最初在HTML5规范中被引用为TCP连接，作为基于TCP的套接字API的占位符。它实现了浏览器与服务器全双工(full-duplex)通信。其本质是保持TCP连接，在浏览器和服务端通过Socket进行通信。



实现原理：

既然是基于浏览器端的web技术，那么它的通信肯定少不了http,websocket本身虽然也是一种新的应用层协议，但是它也不能够脱离http而单独存在。具体来讲，我们在客户端构建一个websocket实例，并且为它绑定一个需要连接到的服务器地址，当客户端连接服务端的时候，会向服务端发送一个类似下面的http报文

```
GET /chat HTTP/1.1Host: server.example.comUpgrade: websocketConnection: UpgradeSec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==Sec-WebSocket-Protocol: chat, superchatSec-WebSocket-Version: 13Origin: http://example.com
```

其中下面两个参数就是Websocket的核心了，告诉Apache、Nginx等服务器：发起的是websocket协议。

```
Upgrade: websocket
Connection: Upgrade
```



首先，Sec-WebSocket-Key 是一个Base64 encode的值，这个是浏览器随机生成的，告诉服务器：我要验证是不是真的是Websocket。

然后，Sec_WebSocket-Protocol 是一个用户定义的字符串，用来区分同URL下，不同的服务所需要的协议。

最后，Sec-WebSocket-Version 是告诉服务器所使用的Websocket Draft（协议版本），然后服务器会返回下列东西，表示已经接受到请求，成功建立Websocket

```
HTTP/1.1 101 Switching ProtocolsUpgrade: websocketConnection: UpgradeSec-WebSocket-Accept: HSmrc0sMlYUkAGmm5OPpG2HaGWk=Sec-WebSocket-Protocol: chat
```

依然是固定的，告诉客户端即将升级的是Websocket协议，而不是mozillasocket，lurnarsocket或者shitsocket。

然后，Sec-WebSocket-Accept 这个则是经过服务器确认，并且加密过后的 Sec-WebSocket-Key

后面的，Sec-WebSocket-Protocol 则是表示最终使用的协议。

返回的状态码为101，表示同意客户端协议转换请求，并将它转换为websocket协议。以上过程都是利用http通信完成的，称之为websocket协议握手(websocket Protocol handshake)，进过这握手之后，客户端和服务端就建立了websocket连接，以后的通信走的都是websocket协议了。所以总结为websocket握手需要借助于http协议，建立连接后通信过程使用websocket协议。同时需要了解的是，该websocket连接还是基于我们刚才发起http连接的那个TCP连接。一旦建立连接之后，我们就可以进行数据传输了，websocket提供两种数据传输：文本数据和二进制数据。

至此，HTTP已经完成它所有工作了，接下来的通信就是完全按照Websocket协议进行了。

websocket具有以下几个方面的优势：

1.  建立在 TCP 协议之上，服务器端的实现比较容易。
2.  与 HTTP 协议有着良好的兼容性。默认端口也是80和443，并且握手阶段采用 HTTP 协议，因此握手时不容易屏蔽，能通过各种 HTTP 代理服务器。
3.  数据格式比较轻量，性能开销小，通信高效。
4.  可以发送文本，也可以发送二进制数据。
5.  没有同源限制，客户端可以与任意服务器通信。
6. 协议标识符是ws（如果加密，则为wss），服务器网址就是 URL

**应用场景**

# 什么是sqlalchemy？

SQLAlchemy 是 Python 中一个通过 ORM 操作数据库的框架。

SQLAlchemy对象关系映射器提供了一种方法，用于将用户定义的Python类与数据库表相关联，并将这些类（对象）的实例与其对应表中的行相关联。它包括一个透明地同步对象及其相关行之间状态的所有变化的系统，称为"工作单元"，以及根据用户定义的类及其定义的彼此之间的关系表达数据库查询的系统。

# Django中如何实现websocket？

django中通过channel或者dwebsock模块来实现websocket通信，这里推荐channel来实现，因为dwebsocket比较老了，用起来也不如channel。

# 从输入http://www.baidu.com/到页面返回, 中间都是发生了什么？

第一步、浏览器中输入域名www.baidu.com

第二步、域名解析

浏览器会把输入的域名解析成对应的IP，过程如下：

1.  浏览器查找浏览器缓存，如果有域名对应的IP地址则返回，如果没有继续查找。

2.  浏览器查看本机的host文件，如果有域名对应的IP地址则返回，如果没有继续查找。

3.  然后是路由器缓存，路由器一般有自己的缓存，如果有域名对应的IP地址则返回，如果没有继续查找。
4.  接着是对本地DNS服务器进行递归查询，看是否有域名对应的IP。主机向本地域名服务器的查询一般都是采用递归查询。所谓递归查询就是如果主机所询问的本地域名服务器不知道被查询域名的IP地址，那么本地域名服务器就以DNS客户的身份，向其他根域名服务器继续发出查询请求报文，而不是让该主机自己进行下一步查询。（本地域名服务器地址是通过DHPC协议获取地址，DHPC是负责分配IP地址的）

5.  本地域名服务器采用迭代查询，它先向一个根域名服务器查询。本地域名服务器向根域名服务器的查询一般都是采用迭代查询。所谓迭代查询就是当根域名服务器收到本地域名服务器发出的查询请求报文后，要么告诉本地域名服务器下一步应该查询哪一个域名服务器，然后本地服务器自己进行后续的查询。（而不是替代本地服务器进行后续查询）。

6.  根域名服务器告诉本地域名服务器，下一次应查询的顶级域名服务器dns.com的IP地址。

7.  本地域名服务器向顶级域名服务器dns.com进行查询。

8. 顶级域名服务器dns.com告诉本地域名服务器，下一次应查询的权限域名服务器dns.baidu.com的IP地址。

9. 本地域名服务器向权限域名服务器dns.baidu.com进行查询。

10.  权限域名服务器dns.baidu.com告诉本地域名服务器，所查询的主机www.baidu.com的IP地址。

本地域名服务器最后把查询结果告诉主机。

第三步、浏览器与目标服务器建立TCP连接

1.  主机浏览器通过DNS解析得到了目标服务器的IP地址后，与服务器建立TCP连接。

2. TCP3次握手连接：浏览器所在的客户机向服务器发出连接请求报文；服务器接收报文后，同意建立连接，向客户机发出确认报文；客户机接收到确认报文后，再次向服务器发出报文，确认已接收到确认报文；此处客户机与服务器之间的TCP连接建立完成，开始通信。

第四步、浏览器通过http协议向目标服务器发送请求

请求行，请求头，请求实体内容。浏览器向主机发起一个HTTP-GET方法报文请求。请求中包含访问的URL，也就是http://www.baidu.com/ ，KeepAlive，长连接，还有User-Agent用户浏览器操作系统信息，编码等。值得一提的是Accep-Encoding和Cookies项。Accept-Encoding一般采用gzip，压缩之后传输html文件。Cookies如果是首次访问，会提示服务器建立用户缓存信息，如果不是，可以利用Cookies对应键值，找到相应缓存，缓存里面存放着用户名，密码和一些用户设置项。

第五步、服务器给出响应，将指定文件发送给浏览器

状态行，响应头，响应实体内容，返回状态码200 OK，表示服务器可以响应请求，返回报文，由于在报头中Content-type为“text/html”，浏览器以HTML形式呈现，而不是下载文件。

注意：但是，对于大型网站存在多个主机站点，往往不会直接返回请求页面，而是重定向。返回的状态码就不是200OK，而是301,302以3开头的重定向码，浏览器在获取了重定向响应后，在响应报文中Location项找到重定向地址，浏览器重新第一步访问即可。

补充一点的就是，重定向是为了负载均衡或者导入流量，提高SEO排名。利用一个前端服务器接受请求，然后负载到不同的主机上，可以大大提高站点的业务并发处理能力；重定向也可将多个域名的访问，集中到一个站点；由于baidu.com，www.baidu.com会被搜索引擎认为是两个网站，照成每个的链接数都会减少从而降低排名，永久重定向会将两个地址关联起来，搜索引擎会认为是同一个网站，从而提高排名。

第六步、TCP释放链接

1.  浏览器所在主机向服务器发出连接释放报文，然后停止发送数据；

2.  服务器接收到释放报文后发出确认报文，然后将服务器上未传送完的数据发送完；

3. 服务器数据传输完毕后，向客户机发送连接释放报文；

4. 客户机接收到报文后，发出确认，然后等待一段时间后，释放TCP连接；

第七步、浏览器显示页面中所有文本。

浏览器接收到返回的数据包，根据浏览器的渲染机制对相应的数据进行渲染。渲染后的数据，进行相应的页面呈现和脚步的交互。

# 请简述浏览器是如何获取一枚网页的？

其过程如下：

1.  在用户输入目的 URL 后，浏览器先向 DNS 服务器发起域名解析请求；

2. 在获取了对应的 IP 后向服务器发送请求数据包；

3. 服务器接收到请求数据后查询服务器上对应的页面，并将找到的页面代码回复给客户端；

4. 客户端接收到页面源代码后，检查页面代码中引用的其他资源，并再次向服务器请求该资源；

5. 在资源接收完成后，客户端浏览器按照页面代码将页面渲染输出显示在显示器上。





# Python web开发中, 跨域问题产生的原理和解决思路是?

早期的浏览器厂商，出于安全性问题的考虑，提出了同源策略的概念，即Web浏览器只有在同源（域）的时候，才可以让一个网页的脚本（script）访问另一个网页的数据。

而同源指的是（协议+域名+端口）三者都要相同的url

协议 http 、 https

域名 www.abc.com  blog.abc.com

端口 http://www.abc.com:8080 http://www.abc.com:80

 

为什么要跨域？

由于同源策略的限制，XHR 1.0(XMLHttpRequests) 不能对非当前域的网页发起 ajax 请求.但是对于一个公司有多个子域 或者 调用不同域的api 也有了限制。因此需要想办法跨域

 

跨域的解决办法：

1.  使用django-cors-headers

2. 使用JSONP

3. 在views中修改请求头，即修改views.py中对应API的实现函数，允许其他域通过Ajax请求数据





# POST 和 GET 请求的区别?

GET 请求，请求的数据会附加在 URL 之后，以?分割 URL 和传输数据，多个参数用&连接。URL 的编码格式采用的是 ASCII 编码，而不是 uniclde，即是说所有的非 ASCII 字符都要编码之后再传输。

POST 请求：POST 请求会把请求的数据放置在 HTTP 请求包的包体中。

因此，GET 请求的数据会暴露在地址栏中，而 POST 请求则不会。

 

**关于传输大小的限制：**

在 HTTP 规范中，没有对 URL 的长度和传输的数据大小进行限制。但是在实际开发过程中，对于 GET，特定的浏览器和服务器对 URL 的长度有限制。因此，在使用 GET 请求时，传输数据会受到 URL 长度的限制。

对于 POST，由于不是 URL 传值，理论上是不会受限制的，但是实际上各个服务器会规定对 POST提交数据大小进行限制，Apache、IIS 都有各自的配置。

 

**补充，关于get请求url长度的限制：**

IE: 2,083 字符

Firefox (Browser):：65536

Safari (Browser)： 80,000个字符

Opera (Browser)：190,000个字符

另外，网上也是众说纷纭，也有说Firefox、chrome、opera都是4089的.....

 

**安全性：**

POST 的安全性比 GET 的高。这里的安全是指真正的安全，而不同于上面 GET 提到的安全方法中的安全，上面提到的安全仅仅是不修改服务器的数据。比如，在进行登录操作，通过 GET 请求，用户名和密码都会暴露再 URL 上，因为登录页面有可能被浏览器缓存以及其他人查看浏览器的历史记录的原因，此时的用户名和密码就很容易被他人拿到了。除此之外，GET 请求提交的数据还可能会造成 Cross-site request frogery 攻击。

**效率：GET 比 POST 效率高。**

GET 请求的过程：

1.浏览器请求 tcp 连接（第一次握手）

2.服务器答应进行 tcp 连接（第二次握手）

3.浏览器确认，并发送 get 请求头和数据（第三次握手，这个报文比较小，所以 http 会在此时

进行第一次数据发送）

4.服务器返回 200 OK 响应

POST 请求的过程：

1.浏览器请求 tcp 连接（第一次握手）

2.服务器答应进行 tcp 连接（第二次握手）

3.浏览器确认，并发送 post 请求头（第三次握手，这个报文比较小，所以 http 会在此时进行

第一次数据发送）

4.服务器返回 100 continue 响应

5.浏览器开始发送数据

6.服务器返回 200 ok 响应



# cookie 和 session 的区别？

1.  cookie 数据存放在客户的浏览器上，session 数据放在服务器上。

2.  cookie 不是很安全，别人可以分析存放在本地的 cookie 并进行 cookie 欺骗考虑到安全应当使用 session。

3.  session 会在一定时间内保存在服务器上。当访问增多，会比较占用服务器的性能考虑到减轻服务器性能方面，应当使用 cookie。

4.  单个 cookie 保存的数据不能超过 4K，很多浏览器都限制一个站点最多保存 20 个 cookie。

5.  建议： 将登录信息等重要信息存放为 SESSION 其他信息如果需要保留，可以放在 cookie 中

具体示例参考：https://www.cnblogs.com/Neeo/articles/9590694.html

# Django的跨域(2021/4/6)

# Django的请求生命周期(4)

这个题也是常问的题：

-   中间件的请求生命周期
-   一个网页，从输入url回车后到渲染出页面中间的详细过程是什么样的？(后台用的是Django)

从用户输入url到用户看到网页的整个过程:

1.  用户输入网址，浏览器发起请求
2.  WSGI（服务器网关接口）创建socket服务端，接受请求
3.  中间件处理请求
4.  url路由，根据当前请求的url找到相应的视图函数
5.  进入view，进行业务处理，执行类或者函数，返回字符串
6.  再次通过中间件处理相应
7.  WSGI返回响应
8. 浏览器渲染



# Django的目录结构(2021/4/6)

项目文件夹下的组成部分：

manage.py 是项目运行的入口，指定配置文件路径。与项目同名的目录，包含项目的配置文件。

 init.py 是一个空文件，作用是这个目录可以被当作包使用。

settings.py 是项目的整体配置文件。

urls.py 是项目的URL配置文件。

wsgi.py 是项目与 WSGI 兼容的 Web 服务器。

# Django ORM常用方法以及聚合函数有哪些(2021/4/6)

```python
create()
p = Person(name="张开", age=18)
p.save()
.all()
get()
exclude()
valueslist()
orderby()
```



# django对数据查询结果排序怎么做, 降序怎么做？

使用order_by进行排序，如根据id排序：

1.  按照 id 从小到大查询数据

    Doc.objects.order_by('id')

2.  按照 id 从大到小查询数据，只需要在字段前加 - 即可

    Doc.objects.order_by('-id')

3.  随机排序，性能较差，不推荐

    Doc.objects.order_by('?')

# django的orm中如何查询 id 不等于5的记录？

```python
models.Project.objects.exclude(pk=5)
```

# 使用Django中model filter条件过滤方法,把下边sql语句转化成python代码

```sql
select * from company 
where title like "%abc%" or mecount>999 order by createtime desc;
```

参考：

```python
models.company.objects.filter(Q(title__contains='abc') or Q(weight__gt=999)).order_by('creatime').reverse()
```

# 写ORM

Django中有Model类User，查询`name="管理员"`的记录，如果有就返回结果集中的第一条记录，没有就返回None：

```python
models.User.objects.filter(name="管理员").first()
```



# django中的F的作用？

Django 提供 F() 来对两个字段的值做比较。

F() 的实例可以在查询中引用字段，来比较同一个 model 实例中两个不同字段的值。

# django中的Q的作用？

Q是用来做条件查询的

对于多个or 和多个and联合查询的情况也会使用Q查询

# django中如何执行原生SQL？

1.  通过 raw() 实现

     ```python
    models.Book.objects.raw('select * from app01_book')
     ```

2.  通过connection直接执行原生SQL

    ```python
    from django.db import connection
    
    cursor=connection.cursor()
    cursor.execute('select * from app01_book')
    result = cursor.fetchall()
    print(result)
    ```
```
    
    

# only和defer的区别？

defer('id', 'name'):取出对象,字段除了id和name都有，但如果询不在的字段，会再次查询数据库，造成数据库压力大

only('id', 'name'):取出对象, 只有id和name

# selectrelated和prefetchrelated的区别？

select_related通过多表join关联查询,一次性获得所有数据,只执行一次SQL查询

prefetch_related分别查询每个表,然后根据它们之间的关系进行处理,执行两次查询

# django中filter和exclude的区别

filter和exclude相当于Django的if/else

filter()表示匹配满足要求的数据，而exclude()则表示匹配不满足要求的数据。

需要注意的是filter()括号里面有很多的匹配选项

# django中values和values_list的区别？

返回一个ValuesQuerySet —— QuerySet 的一个子类，迭代时返回字典而不是模型实例对象。

每个字典表示一个对象，键对应于模型对象的属性名称。

values() 接收可选的位置参数*fields，它指定SELECT 应该限制哪些字段。如果指定字段，每个字典将只包含指定的字段的键/值。如果没有指定字段，每个字典将包含数据库表中所有字段的键和值

 

values_list与values() 类似，只是在迭代时返回的是元组而不是字典。每个元组包含传递给values_list() 调用的字段的值 —— 所以第一个元素为第一个字段，以此类推

# 如何使用django orm批量创建数据？

用bulk_create()

​```python
objs=[models.Book(title="图书{}".format(i+15)) for i in range(100)] # 100条数据列表
models.Book.objects.bulk_create(objs) # 一次批量插入
```

# django的Form和ModeForm的作用？

Form组件的主要功能如下：  

1.  生成页面可用的HTML标签。只能生成获取用户信息的那些input标签等  

2. 对用户提交的数据进行校验，返回错误提示信息  

3. 保留页面上用户输入的内容  



ModelForm组件：这个组件主要就是将model与Form组件的功能结合起来，可以更加便捷的对数据进行添加、编辑以及数据的验证操作。相对于单独的Form组价来说要方便很多。但是Form组件会比这个ModelForm组件更加灵活，如果在使用Django做web开发过程中验证的数据和数据库字段相关（可以对表进行增、删、改操，注意 Many to many字段，也可以级联操作第3张关系表；），建议优先使用ModelForm，用起来更方便些，但是在使用ModelForm的时候慎用fields='__all__'，获取数据库所有字段势必造成资源的浪费。

# 请简述http缓存机制

HTTP缓存有多种规则，根据是否需要重新向服务器发起请求来分类，大致可分为两类：

1.  强制缓存：强制缓存，在缓存数据未失效的情况下，可以直接使用缓存数据，浏览器通过Expires和Cache-Control这两个字段来判断缓存是否失效

2. 对比(协商)缓存：顾名思义，需要进行比较判断是否可以使用缓存。浏览器第一次请求数据时，服务器会将缓存标识与数据一起返回给客户端，客户端将二者备份至缓存数据库中。再次请求数据时，客户端将备份的缓存标识发送给服务器，服务器根据缓存标识进行判断，判断成功后，返回304状态码，通知客户端比较成功，可以使用缓存数据

 

两类缓存规则可以同时存在，强制缓存优先级高于对比缓存，也就是说，当执行强制缓存的规则时，如果缓存生效，直接使用缓存，不再执行对比缓存规则。

# 简述django下的(內建的)缓存机制

Django根据设置的缓存方式，浏览器第一次请求时，cache会缓存单个变量或整个网页等内容到硬盘或者内存中，同时设置response头部，当浏览器再次发起请求时，附带f-Modified-Since请求时间到Django，Django 发现f-Modified-Since 会先去参数之后，会与缓存中的过期时间相比较，如果缓存时间比较新，则会重新请求数据，并缓存起来然后返回response给客户端，如果缓存没有过期，则直接从缓存中提取数据，返回给response给客户端。

 

补充，Django中提供了6种缓存方式：

1.  开发调试：开发调试(此模式为开发调试使用,实际上不执行任何操作)

2.  内存：将缓存内容保存至内存区域中

3. 文件：把缓存数据存储在文件中

4. 数据库：把缓存数据存储在数据库中

5. Memcache缓存（python-memcached模块）：使用python-memcached模块连接memcache

6. Memcache缓存（pylibmc模块）：使用pylibmc模块连接memcache

 

补充：

Django提供了不同粒度的缓存,可以缓存某个页面,可以只缓存一个页面的某个部分,甚至可以缓存整个网站.

Django中三种不同粒度的缓存:

1. 全站缓存

2. 单页面缓存

3. 页面中某个部分的局部缓存

# django中使用memcached作为缓存的具体方法? 优缺点说明?

django中使用memcached作为缓存：

1.  memcached服务跑起来

2.  django settings中配置搞起来

```python
# 缓存配置
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',  # 使用memcached进行缓存    
        'LOCATION':
            [
                '127.0.0.1:11211'  # memcached默认的主机端口    
            ]
    }
}
```

3.  使用吧

memcached缓存有多种方式，可以在在视图上使用缓存装饰器将整个页面进行缓存，可以在视图中对某些数据进行缓存，可以在路由中进行缓存，此方法主要用在当多个路由指向同一个页面而又不想让这个页面对所有的路由都缓存时使用，还可以在模板中使用。

 

使用memcached的优缺点：

支持的数据类型少，只支持k:v格式的数据

集群是逆向集群，多主一从，无法备份

数据在内存中存储，性能高，存储结构简单处理起来相对容易

# django的缓存能使用redis吗？如果可以的话，如何配置？

配置：

1.  redis服务跑起来

2.  下载django-redis抹开

3. django settings配置CACHES参数
    -   可以在中间中配置全栈缓存
    -   在CACHES中配置单视图缓存
    -   在模板中配置页面的局部缓存

# 谈谈你所知道的Python web框架

1.  底层自定义协议网络框架——Twisted

2. 支持快速建站的框架——Flask

3. 高并发处理框架——Tornado

4. 企业级开发框架——Django

# django、flask、tornado框架的比较？

Flask:

Flask诞生于2010年，是Armin ronacher用Python语言基于Werkzeug工具箱编写的轻量级Web开发框架

Flask本身相当于一个内核，其他几乎所有的功能都要用到扩展

可以用Flask-extension加入ORM、窗体验证工具，文件上传、身份验证等

没有默认使用的数据库，你可以选择MySQL，也可以用NoSQL

核心基于Werkzeug WSGI工具 和jinja2 模板引擎

 

Django:

2005年,劳伦斯出版集团为开发新闻网站开发了Django，是基于python语言编写的开源web开发框架

Django基于自身框架结构形成了MVT设计，遵循MVC设计

Django是一个重量级框架功能齐全，提供一站式解决的思路，能让开发者不用在选择上花费大量时间

自带ORM和模板引擎，支持jinja等非官方模板引擎

最出名的是其全自动化的管理后台：只需要使用起ORM，做简单的对象定义，它就能自动生成数据库结构、以及全功能的管理后台

成熟，稳定，开发效率高，相对于Flask，Django的整体封闭性比较好，适合做企业级网站的开发

 

Tornado:

Tornado是2009年9月10日发布的一个用Python语言写成的Web服务器兼Web应用框架

Tornado在设计之初就考虑到了性能因素，旨在解决C10K问题，这样的设计使得其成为一个拥有非常高性能的框架

Tornado 和现在的主流 Web 服务器框架（包括大多数 Python 的框架）有着明显的区别：它是非阻塞式服务器，而且速度相当快

Tornado走的是少而精的方向，注重的是性能优越

Tornado应该运行在类Unix平台，在线上部署时为了最佳的性能和扩展性，仅推荐Linux和BSD（因为充分利用Linux的epoll工具和BSD的kqueue工具，是Tornado不依靠多进程/多线程而达到高性能的原因）

 

# Python 中三大框架各自的应用场景？

django:主要是用来搞快速开发的，他的亮点就是快速开发，节约成本，正常的并发量不过10000，如果要实现高并发的话，就要对django进行二次开发，比如把整个笨重的框架给拆掉，自己写socket实现http的通信，底层用纯c，c++写提升效率，ORM框架给干掉，自己编写封装与数据库交互的框 架，因为啥呢，ORM虽然面向对象来操作数据库，但是它的效率很低，使用外键来联系表与表之间的查询；

 

flask:轻量级，主要是用来写接口的一个框架，实现前后端分离，提升开发效率，Flask本身相当于一个内核，其他几乎所有的功能都要用到扩展（邮件扩展Flask-Mail，用户认证Flask-Login），都需要用第三方的扩展来实现。比如可以用Flask-extension加入ORM、窗体验证工具，文件上传、身份验 证等。Flask没有默认使用的数据库，你可以选择MySQL，也可以NoSQL。 其 WSGI 工具箱采用 Werkzeug（路由模块），模板引擎则使用 Jinja2。这两个也是Flask框架的核心。Python最出名的框架要数Django，此外还有Flask、Tornado等框架。虽然Flask不是最出名的框架，但是Flask应该算是最灵活的框架之一，这也是Flask受到广大开发者喜爱的原因。

 

tornado:Tornado是一种 Web 服务器软件的开源版本。Tornado 和现在的主流 Web 服务器框架（包括大多数 Python 的框架）有着明显的区别：它是非阻塞式服务器，而且速度相当快。 得利于其非阻塞的方式和对epoll的运用，Tornado 每秒可以处理数以千计的连接，因此 Tornado 是实时 Web 服务的一个 理想框架。

# 什么是wsgi？

WSGI的全称是Web Server Gateway Interface，翻译过来就是Web服务器网关接口。具体的来说，WSGI是一个规范，定义了Web服务器如何与Python应用程序进行交互，使得使用Python写的Web应用程序可以和Web服务器对接起来。WSGI一开始是在PEP-0333中定义的，最新版本是在Python的PEP-3333定义的。

对于初学者来说，上面那段就是废话，说了跟没说一样。本文的主要内容就是说清楚，WSGI到底是如何工作的。

 

为什么需要WSGI这个规范：

在Web部署的方案上，有一个方案是目前应用最广泛的：

首先，部署一个Web服务器专门用来处理HTTP协议层面相关的事情，比如如何在一个物理机上提供多个不同的Web服务（单IP多域名，单IP多端口等）这种事情。

然后，部署一个用各种语言编写（Java, PHP, Python, Ruby等）的应用程序，这个应用程序会从Web服务器上接收客户端的请求，处理完成后，再返回响应给Web服务器，最后由Web服务器返回给客户端。

 

那么，要采用这种方案，Web服务器和应用程序之间就要知道如何进行交互。为了定义Web服务器和应用程序之间的交互过程，就形成了很多不同的规范。这种规范里最早的一个是CGI][3，1993年开发的。后来又出现了很多这样的规范。比如改进CGI性能的FasgCGI，Java专用的Servlet规范，还有Python专用的WSGI规范等。提出这些规范的目的就是为了定义统一的标准，提升程序的可移植性。在WSGI规范的最开始的PEP-333中一开始就描述了为什么需要WSGI规范。

 

WSGI如何工作：

从上文可以知道，WSGI相当于是Web服务器和Python应用程序之间的桥梁。那么这个桥梁是如何工作的呢？首先，我们明确桥梁的作用，WSGI存在的目的有两个：

1.  让Web服务器知道如何调用Python应用程序，并且把用户的请求告诉应用程序。

2. 让Python应用程序知道用户的具体请求是什么，以及如何返回结果给Web服务器。

 

WSGI中都有哪些角色？

在WSGI中定义了两个角色：

1.  Web服务器端称为server或者gateway

2.  应用程序端称为application或者framework（因为WSGI的应用程序端的规范一般都是由具体的框架来实现的）

# 列举django的内置组件？

orm组件：

1.  对用户请求的数据进行校验

2.  生成HTML标签

信号：

Django的信号其实就是Django内部为开发者预留的一些自定制功能的钩子。只要在某个信号中注册了函数，那么Django内部执行的过程中就会自动触发注册在信号中的函数。

场景:

在数据库某些表中添加数据时，可以进行日志记录。

CSRF（跨站点请求伪造）:

目标：防止用户直接向服务端发起POST请求。

它与XSS非常不同，XSS利用站点内的信任用户，而CSRF则通过伪装来自受信任用户的请求来利用受信任的网站。

 

ContentType:

ContentType是Django的一个组件（app），为我们找到Django程序中所有app中的所有表并添加到记录中。可以使用它再加上表中的两个字段实现：一张表和N张表创建FK（字段）关系。（简单理解为进行多表之间的关联作用）

 

中间件：

对所有的请求进行批量处理，在视图函数执行前后进行自定义操作。

应用：用户登录校验

问题：为甚么不使用装饰器？

如果不使用中间件，就需要给每个视图函数添加装饰器，太繁琐

 

认证组件：

只有认证通过的用户才能访问指定的url地址，比如：购买物品信息，需要登录之后才能查看，没有登录，就不能查看，这时候需要用到认证组件

Auth模块是Django自带的用户认证模块

 

权限组件:

用户登录后，将权限放到session中，每次请求进来都在中间件里，根据当前的url去session中匹配，判断当前用户是否有权限访问当前url,有权限就继续访问，没有就返回，（检查的东西就可以放到中间件中进行统一处理）在process_request方法里面做的，我们的中间件是放在session后面，因为中间件需要到session里面取数据



# django中model的SlugField类型字段有什么用途

SlugField字段是将输入的内容中的空格都替换成‘-’之后保存，Slug 是一个新闻术语，通常是某些东西的短标签。一个slug只能包含字母、数字、下划线或者是连字符，通常用来作为短标签。通常它们是用来放在URL里的。

SlugField字段的Field.db_index自动设置为True。

通常根据另一个值自动生成slug来填充到SlugField的值

 

# django中想要验证表单提交是否格式正确需要用到form中的哪个方法

```
 A. form.save()
 B. form.save(commit=False)
 C. form.verify()
 D. form.is_valid()
```

答案是D

# django常见的线上部署方式有哪几种？

```
django+uwsgi+nginx+database
```



# django中如何在model保存前做一定的固定操作,比如写一句日志？

利用信号:https://www.cnblogs.com/Neeo/articles/11601851.html

延申，MySQL中如何实现？使用触发器

关于触发器：https://www.cnblogs.com/Neeo/articles/13677324.html



# 简述django FBV和CBV？

CBV是采用面向对象的方法写视图文件。

CBV的执行流程：

浏览器向服务器端发送请求，服务器端的urls.py根据请求匹配url,找到要执行的视图类，执行dispatch方法区分出是POST请求还是GET请求，执行views.py对应类中的POST方法或GET方法。

而FBV就是通过 url 来匹配 一个函数，这种方式叫做 function based view (BSV)。一个典型的使用方式就是通过在view.py里面定义一个函数，然后通过函数的request参数获取method的类型，比如直接刷新页面就是get方式，提交表单就是post方式，这样来根据提交的不同方式进行不同的处理。

# 如何给django CBV的函数设置添加装饰器？

CBV模式下，你可以：

1.  在类上

2. 在dispatch上

需要导入特殊的模块

```python
from django.views import Viewfrom django.utils.decorators import method_decorator
```

# django如何连接多个数据库并实现读写分离？

1.  settings中,DATABASES参数配置

```python
DATABASES = {
    "default": {},
    "slave1":{},
    "slave2":{},
}
```

2.  创建 db_router.py 实现读写分离

```python
class MasterSlaveDBRouter(object):
    """数据库主从读写分离路由"""
    
    def db_for_read(self, model, **hints):
        """读数据库"""
        return "slave"
 
    def db_for_write(self, model, **hints):
        """写数据库"""
        return "default"
 
    def allow_relation(self, obj1, obj2, **hints):
        """是否运行关联操作"""
        return True　　
```

3.  settings中配置读写分离

```python
DATABASE_ROUTERS = ['项目名.utils.db_router."自定义的类名称"']
```

上面就是自动读写分离，还可以配置手动读写分离

```python
from django.shortcuts import render, HttpResponse
from app001 import models
def write(request):                  
    models.User.objects.using('default').create(name='张三', pwd='123', phone=1234)    
    return HttpResponse('写成功')
def read(request):    
    obj = models.User.objects.filter(id=1).using('db2').first()
    return HttpResponse('读成功')
```

当你数据的读写操作过于频繁的时候，这个方法就会略显繁琐

# django的Form组件中，如果字段中包含choices参数，请使用两种方式实现数据源实时更新

```python
# 方式一：重写初始化方法，在构造方法中重新去数据库获取值
class UserForm(Form):      
    ut_id = fields.ChoiceField(choices=())      
    def __init__(self, *args, **kwargs):   
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['ut_id'].choices = models.UserType.objects.all().values_list('id', 'title')  
        
        
# 方式二: ModelChoiceField字段  
class UserForm(Form):      
    # 从另一张依赖表中提取数据
    ut_id = ModelChoiceField(queryset=models.UserType.objects.all())    　　  
# 依赖表：      
class UserType(models.Model):
    title = models.CharField(max_length=32)

```

# django的Model中的ForeignKey字段中的on_delete参数有什么作用？

删除关联表中的数据时,当前表与其关联的field的操作

django2.0之后，表与表之间关联的时候,必须要写on_delete参数,否则会报异常

# django中csrf的实现机制？

第一步：

  django第一次响应来自某个客户端的请求时,后端随机产生一个token值，把这个token保存在SESSION状态中;同时,后端把这个token放到cookie中交给前端页面

第二步：

  下次前端需要发起请求（比如发帖）的时候把这个token值加入到请求数据或者头信息中,一起传给后端；Cookies:{csrftoken:xxxxx}

第三步：

  后端校验前端请求带过来的token和SESSION里的token是否一致

# 基于django使用ajax发送post请求时，有哪种方法携带csrf token？

1.  在ajax发送请求时，在data中带着csrf_token，不过这需要在body中提前生成token值。

2.  使用jQuery.ajaxSetup()函数

3.  最后，还有一种放在request.META中，但是这种方式需要jquery.cookie.js文件搭配。

参考：https://www.cnblogs.com/Neeo/articles/11455271.html

# django路由系统中name的作用？

用于反向解析路由,相当于给url取个别名，只要这个名字不变,即使对应的url改变

通过该名字也能找到该条url

# django的模板中filter、simpletag、inclusiontag的区别？

filter：对django后台返回到模板中的数据、进行处理

-   可以与if标签来连用

-   自定义时需要写两个形参

simpletag:和自定义filter类似，只不过接收更灵活的参数

-   可以传多个参数,没有限制

-   不能与if标签来连用

inclusion_tag： 多用于返回html代码片段

# Django-debug-toolbar的作用？

django开发调试工具

django-debug-toolbar是一组可配置的面板，可现实有关当前请求/响应的各种调试信息，斌在单击时显示有关面板内容的更多详细信息

参考：https://www.cnblogs.com/Neeo/articles/14149781.html

# Django中如何实现单元测试？

Django支持python的单元测试（unit test）和文本测试（doc test），我们这里主要讨论单元测试的方式。这里不对单元测试的理论做过多的阐述，假设你已经熟悉了下列概念：test suite, test case, test/test action, test data， assert等等。

在单元测试方面，Django继承python的unittest.TestCase实现了自己的django.test.TestCase，编写测试用 例通常从这里开始。测试代码通常位于app的tests.py文件中(也可以在models.py中编写，但是我不建议这样做）。在Django生成的 app目录中，已经包含了这个文件，并且其中包含了一个测试用例的样例

示例：

```python
from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """Tests that 1 + 1 always equals 2."""
        self.assertEqual(1 + 1, 2)
```

可以有几种方式运行单元测试：

```bash
python manage.py test：执行所有的测试用例
python manage.py test app_name, 执行该app的所有测试用例
python manage.py test app_name.case_name: 执行指定的测试用例
python manage.py test--pattern="tests_*.py" 通配测试文件名
```

参考：https://www.cnblogs.com/Neeo/articles/14172562.html

# 解释orm中 db first 和 code first的含义？

都是数据持久化的方式：

db first基于已存在的数据库,生成模型

code first基于已存在的模型,生成数据库

# django中如何根据数据库表生成model类？

1.  在settings中设置要连接的数据库

2.  生成model模型文件

```
python manage.py inspectdb
```

3.  模型文件导入到models中

```
python manage.py inspectdb > app/models.py
```

# 使用orm和原生sql的优缺点？

1.orm的开发速度快,操作简单。使开发更加对象化

  执行速度慢。处理多表联查等复杂操作时,ORM的语法会变得复杂

2.sql开发速度慢,执行速度快。性能强

# django的contenttype组件的作用？

contenttype组件保存了项目中所有app和model的对应关系,每当我们创建了新的model并执行数据库迁移后，ContentType表中就会自动新增一条记录

当一张表和多个表FK关联,并且多个FK中只能选择其中一个或其中n个时,可以利用contenttypes

# Django 中哪里用到了线程?哪里用到了协程?哪里用到了进程？

1.  对于django中耗时的任务使用进程或者线程来解决，比如发邮件，定时任务等

# 对 cookie 与 session 的了解？他们能单独用吗？

1.cookie: cookie是保存在浏览器端的键值对,可以用来做用户认证

2.session：将用户的会话信息保存在服务端,key值是随机产生的自符串,value值时session的内容,依赖于cookie将每个用户的随机字符串保存到用户浏览器上

 

补充：

Django中session默认保存在数据库中：django_session表

flask,session默认将加密的数据写在用户的cookie中

# django 关闭浏览器，怎样清除 cookies 和 session？

SESSION_EXPIRE_AT_BROWSER_CLOSE 设置为 True，当浏览器关闭时，Django 会使 cookie 失效

# 接口的幂等性是什么意思？

1.是系统的接口对外一种承诺(而不是实现)

2.承诺只要调用接口成功,外部多次调用对系统的影响都是一致的,不会对资源重复操作

# Django 创建项目的命令？

```bash
# 创建项目
django-admin startproject project_name
# 创建app
django-admin startapp app_name
```

# 对 MVC,MVT 解读的理解？

**MVC**

 MVC设计模式核心：解耦，让不同的代码块之间降低耦合，增强代码的可扩展和可移植性，实现向后兼容。

M全拼为Model，主要封装对数据库层的访问，对数据库中的数据进行增、删、改、查操作。

V全拼为View，用于封装结果，生成页面展示的html内容。

C全拼为Controller，用于接收请求，处理业务逻辑，与Model和View交互，返回结果。

**MVT**

Django中MVT设计模式—Django框架遵循MVC设计。

M全拼为Model，与MVC中的M功能相同，负责和数据库交互，进行数据处理。

V全拼为View，与MVC中的C功能相同，接收请求，进行业务处理，返回应答。

T全拼为Template，与MVC中的V功能相同，负责封装构造要返回的html。



# 启动 Django 服务的方法？

1、python3 manage.py runserver

2、python3 manage.py runserver + ip（0.0.0.0）

3、python3 manage.py runserver +端口（8080）

# 怎样测试 django 框架中的代码？

可以通过以下几种方式：

1.  通过python的unittest、pytest库进行测试

2.  通过使用第三方组件进行测试，比如django-debug-toolbar

3. 通过django中单元测试进行测试

4. 通过其他的工具进行测试

    -   postman

    -   jmeter



# 有用过 Django REST framework 吗？谈谈你对它的理解

RESTful：

RESTful是一种开发理念 . REST是设计风格而不是标准

REST特点:url简洁,将参数通过url传到服务器.

称之为RESTful框架

1.具象的:资源

2.表现:格式

3.状态转换:数据变化

如果客服端想要操作服务器,必须通过某种手段,让服务器端发生"状态转换"

总结:

1.  每一个URL代表一种资源

2.  客服端和服务器端,传递这个资源的表现层

3.  客服端通过四个GTTP动词,对服务器端资源进行操作,实现"表现层状态转化"

    -   GET（SELECT）：从服务器取出资源（一项或多项）。

    -   POST（CREATE）：在服务器新建一个资源。
    -   PUT（UPDATE）：在服务器更新资源（客户端提供改变后的完整资源）。
    -   DELETE（DELETE）：从服务器删除资源。

 

Django REST framework：

序列化和反序列化可以复用

增:效验请求数据>执行反序列化过程>保存数据库>将保存的对象序列化并返回

删:判断要删除的数据是否存在.>执行数据库删除

改:判断要修改的数据是否存在>效验请求的参数>执行反序列化过程>保存数据库>将保存的对象序列化并返回

查:查询数据库>将数据序列化并返回

 

Django REST framework优点：

1.  提供了定义序列化器Serializer的方法,可以快速根据Django ORM 或者其他库自动序列化/反序列化

2.  提供了丰富的类视图\MIXIN扩展类,简化视图的编写

3.  丰富的定制层级:函数视图\类视图\试图结合到自动生成API,满足各种需要

4.  多种身份认证和权限认证方式的支持

5.  内置了限流系统

6.  直观的API web界面

7.  可扩展性 , 插件丰富

# Django HTTP 请求的处理流程?

在接受一个Http请求之前的准备：

1.  启动一个支持WSGI网关协议的服务器监听端口等待外界的Http请求，比如Django自带的开发者服务器或者uWSGI服务器。

2. 服务器根据WSGI协议指定相应的Handler来处理Http请求，并且初始化该Handler，在Django框架中由框架自身负责实现这一个Handler。

3.  此时服务器已处于监听状态，可以接受外界的Http请求

 

当一个http请求到达服务器的时候:

1. 服务器根据WSGI协议从Http请求中提取出必要的参数组成一个字典（environ）并传入Handler中进行处理。

2. 在Handler中对已经符合WSGI协议标准规定的http请求进行分析，比如加载Django提供的中间件，路由分配，调用路由匹配的视图等。

3. 返回一个可以被浏览器解析的符合Http协议的HttpResponse

# Django 里 QuerySet 的 get 和 filter 方法的区别？

get 的参数只能是model中定义的那些字段，只支持严格匹配

filter 的参数可以是字段，也可以是扩展的where查询关键字，如in，like等【返回值】

get 返回值是一个定义的model对象

filter 返回值是一个新的QuerySet对象，然后可以对QuerySet在进行查询返回新的QuerySet对象，支持链式操作QuerySet一个集合对象，可使用迭代或者遍历，切片等，但是不等于list类型(使用一定要注意)

 

get 只有一条记录返回的时候才正常,也就说明get的查询字段必须是主键或者唯一约束的字段。当返回多条记录或者是没有找到记录的时候都会抛出异常

filter 有没有匹配的记录都可以

# django 中当一个用户登录 A 应用服务器（进入登录状态），然后下次请求被 nginx代理到 B 应用服务器会出现什么影响？

如果用户在A应用服务器登陆的session数据没有共享到B应用服务器，那么之前的登录状态就没有了

# Django 对数据查询结果排序怎么做，降序怎么做，查询大于某个字段怎么做?

排序使用order_by()

降序需要在排序字段名前加-

查询字段大于某个值：使用filter(字段名_gt=值)

# Django 重定向你是如何实现的？用的什么状态码？

使用HttpResponseRedirect

redirect和reverse

状态码：302,301

# 生成迁移文件和执行迁移文件的命令是什么？

```bash
python manage.py makemigrations
python manage.py migrate
```



# 什么 csrf 攻击原理？如何解决？

CSRF 全拼为 Cross Site Request Forgery, 跨站请求伪造.CSRF指的是攻击者盗用了你的身份,以你的名义发送恶意的请求,给你造成个人隐私泄露及财产安全.

CSRF攻击的原理:

1.  用户正常登录A银行网站,

2. A网站返回cookie信息给用户,浏览器保存cookie信息

3.  在A网站没有退出登录的情况下(或者说cookie信息没过期), 登录了恶意网站B

4. 恶意网站B,提前准备好转账表单或者其它请求 ,将其隐藏. 把提交到A网站的按钮设置为一个"领取优惠券"的图片链接.用户 点击链接

5.  在用户主观未知的情况下,访问A网站,此时浏览器会自动携带cookie信息

6.  A网站识别到cookie信息,默认为是用户本人做出的请求,根据请求做出相应的操作.

7. 用户受到损失.

 

CSRF如何防范?

在请求参数中加入一个混淆字符串csrf_token.

简单来说,服务器在接受到请求后, 返回给用户两个csrf_token值, 一个放在cookie信息中,浏览器会保存,下次请求的时候浏览器自动携带. 一个放在前端页面中(例如:表单域或者ajax的请求头中), 当用户再次向服务器发送数据的时候, 服务器会对比cookie中和前端页面中的csrf_token值,如果一样,证明是用户操作,如果不一样,证明是非法操作.

恶意网站B因为页面是提前写好的,无法获取到csrf_token值(cookie同源策略),所以服务器接受到请求的时候,会显示非法操作,从而保证了用户个人信息的安全.解决了csrf攻击

在django中的防范

启用中间件

post请求

验证码

表单中添加{%csrf_token%}标签



# 代码优化从哪些方面考虑？有什么想法？

可以从以下几个方面着手回答：

（1）优化算法时间复杂度。

（2）减少冗余数据。

（3）合理使用 copy 与 deepcopy。

（4）使用 dict 或 set 查找元素。

（5）合理使用生成器（generator）和 yield

（6）优化循环。

（7）优化包含多个判断表达式的顺序。

（8）使用join合并迭代器中的字符串。

（9）选择合适的格式化字符方式。

（10）不借助中间变量交换两个变量的值。

（11）使用 if is

（12）终级大杀器：PyPy。

（13）使用性能分析工具

 

参考：https://www.cnblogs.com/Neeo/articles/13957549.html

# django 开发中数据库做过什么优化?

1.  设计表时，尽量少使用外键，因为外键约束会影响插入和删除性能

2.  使用缓存，减少对数据库的访问。

3.  在ORM框架下设置表时，能用varchar确定字段长度时，就不用text；

4.  可以给搜索频率高的字段属性，在定义时创建索引。如果对多个字段创建索引以后，注意查询的顺序遵循最左前缀原则。即创建的顺序是name,age,country,查询时可以是只查name，或者只查name,age，或者按顺序查找name,age,country，否则其他顺序都将进行全表扫描。

5.  Django ORM框架下的Queryset本来就是有缓存的。

6.  如果一个页面需要多次连接数据库，最好一次性取出所有数据，减少对数据库的查询次数。

7.  若页面只需要数据库里一两个字段时，可以用Queryset.values()

8.  在模板标签里使用with标签可以缓存Queryset的查询结果。

9.  对于多张表联合查询的，查询频率较高的字段可以在其关联的另一张表设置冗余字段，例如sales销量、评论量、默认图片地址default_img_url等，以空间换时间。根据具体项目权衡

10.  使用redis做缓存

 

# 谈一下你对 uWSGI 和 nginx 的理解？

uWSGI：

uWSGI 是一个 Web 服务器，它实现了 WSGI 协议、uwsgi、http 等协议。Nginx 中HttpUwsgiModule 的作用是与 uWSGI 服务器进行交换。WSGI 是一种 Web 服务器网关接口。它是一个 Web 服务器（如 nginx，uWSGI 等服务器）与 web 应用（如用 Flask 框架写的程序）通信的一种规范。

要注意 WSGI / uwsgi / uWSGI 这三个概念的区分。

WSGI 是一种通信协议。

uwsgi 是一种线路协议而不是通信协议，在此常用于在 uWSGI 服务器与其他网络服务器的数据通信。

uWSGI 是实现了 uwsgi 和 WSGI 两种协议的 Web 服务器。

 

NGINX:

nginx 是一个开源的高性能的 HTTP 服务器和反向代理：

1.作为 web 服务器，它处理静态文件和索引文件效果非常高；

2.它的设计非常注重效率，最大支持 5 万个并发连接，但只占用很少的内存空间；

3.稳定性高，配置简洁；

4.强大的反向代理和负载均衡功能，平衡集群中各个服务器的负载压力应用。

# 说说 nginx 和 uWISG 服务器之间如何配合工作的？

1.  首先浏览器发起http请求到Nginx服务器

2.  Nginx根据接收到请求包，进行url分析，判断访问的资源类型：如果是静态资源，直接读取静态资源返回给浏览器；如果请求的是动态资源就转交给uWSGI服务器。

3.  uWSGI服务器根据自身的uwsgi 和 WSGI协议，找到对应的Django框架

4.  Django框架下的应用进行逻辑处理后，将返回值发送到uWSGI服务器

5.  然后uWSGI服务器再返回给Nginx服务器

6.  最后Nginx将返回值返回给浏览器进行渲染显示给用户

# 验证码过期时间怎么设置？

将验证码保存到数据库或 session，设置过期时间为 1 分钟，然后页面设置一个倒计时(一般是前端js 实现这个计时)的展示，一分钟过后再次点击获取新的信息。

另外就是将验证码放到redis中，然后设置过期时间

# django 如何提升性能（高并发）

从三个方面进行优化：web前端性能优化，web服务器端的性能优化，运维部署的优化。

web前端优化：

1. 减少http请求，减少数据库的访问量，比如使用雪碧图

  雪碧图是根据CSS sprite音译过来的，就是将很多很多的小图标放在一张图片上，就称之为雪碧图。  

  使用雪碧图的目的：有时为了美观，我们会使用一张图片来代替一些小图标，但是一个网页可能有很多很多的小图标，浏览器在显示页面的时候，就需要像服务器发送很多次访问请求，这样一来，一是造成资源浪费，二是会导致访问速度变慢。这时候，把很多小图片（需要使用的小图标）放在一张图片上，按照一定的距离隔开，就解决了上述的两个问题。

2. 使用浏览器缓存，将一些常用的css/js/logo图标这些静态资源缓存到本地浏览器，通过设置http头中的cache-control 和expires属性，可设定浏览器缓存，缓存时间可以自定义。

3. 对html、css、js文件进行压缩，减少网络通信量。

 

web后端优化:

1. 使用合理的缓存技术，对一些常用到的动态数据，比如首页做一个缓存，或者某些常用的数据做缓存，设置一定的过期时间，这样减少了数据库的压力，提升网站性能。

2. 使用celery消息队列，将耗时的操作丢到队列里，让worker去监听队列的任务，实现异步操作，比如发短信、发邮件。

3. 代码上的优化，避免写冗余代码。

4. 数据库查询语句的优化，对于建了索引的字段查询时遵循最左原则，避免出现全表扫描。

 

运维部署优化:

1.  搭建nginx服务器，搭建服务器集群，充分利用nginx服务器的负载均衡和反向代理功能。

2.  数据库设置读写分离，可对读的那台数据库使用myisam引擎。写的那台使用innodb引擎。  

 

# 有过部署经验？用的什么技术？可以满足多少压力？

1有部署经验，在阿里云服务器上部署的

2.技术有：nginx + uwsgi 的方式来部署 Django 项目

3.无标准答案（例：压力测试500），而压测目前企业主要在乎QPS和TPS这两个指标

 

性能指标参考：https://www.cnblogs.com/Neeo/articles/12482772.html#%E5%93%8D%E5%BA%94%E6%97%B6%E9%97%B4rt



# 有没有用过Jieba 分词，谈谈jieba分词中的三种分词模式

jieba分词的三种分词模式：

1.  精确模式：试图将句子最精确地分开，适合文本分析

2. 全模式：把句子中所有的可以成词的词语都扫描出来，速度非常快，但是不能解决歧义

3. 搜索引擎模式：在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词

 ```python
import jieba

word = "他毕业于上海交通大学机电系，后来在一机部上海电器科学研究所工作"
print("全模式: " + "/".join(jieba.cut(word, cut_all=True)))
print("精确模式: " + "/".join(jieba.cut(word, cut_all=False)))
print("搜索引擎模式: " + "/".join(jieba.cut_for_search(word)))
"""
全模式: 他/毕业/于/上海/上海交通大学/交通/大学/机电/系/，/后来/在/一机部/上海/电器/科学/科学研究/研究/研究所/工作
精确模式: 他/毕业/于/上海交通大学/机电/系/，/后来/在/一机部/上海/电器/科学/研究所/工作
搜索引擎模式: 他/毕业/于/上海/交通/大学/上海交通大学/机电/系/，/后来/在/一机部/上海/电器/科学/研究/研究所/工作
"""
 ```

# 关系型数据库的关系包括哪些类型？

ForeignKey：一对多，将字段定义在多的一端中

ManyToManyField：多对多，将字段定义在两端中

OneToOneField：一对一，将字段定义在任意一端中

# 查询集返回列表的过滤器有哪些？

all()：返回所有数据

filter()：返回满足条件的数据

exclude()：返回满足条件之外的数据，相当于sql语句中where部分的not 关键字

order_by()：排序

# 判断查询集正是否有数据？

exists()：判断查询集中是否有数据，如果有则返回True，没有则返回False

# Django 本身提供了 runserver，为什么不能用来部署？

runserver 方法是调试 Django 时经常用到的运行方式，它使用 Django 自带的

WSGI Server 运行，主要在测试和开发中使用，并且 runserver 开启的方式也是单进程。

uWSGI 是一个 Web 服务器，它实现了 WSGI 协议、uwsgi、http 等协议。注意 uwsgi 是一种通信协议，而 uWSGI 是实现 uwsgi 协议和 WSGI 协议的Web 服务器。uWSGI 具有超快的性能、低内存占用和多 app 管理等优点，并且搭配着 Nginx就是一个生产环境了，能够将用户访问请求与应用 app 隔离开，实现真正的部署。相比来讲，支持的并发量更高，方便管理多进程，发挥多核的优势，提升性能。

# apache 和 nginx 的区别？

Apache和Nginx最核心的区别在于 apache 是同步多进程模型，一个连接对应一个进程；而 nginx 是异步的，多个连接（万级别）可以对应一个进程。

Nginx特点:

1、轻量级，采用C进行编写，同样的web服务，会占用更少的内存及资源。

2、抗并发，nginx以epollandkqueue作为开发模型，处理请求是异步非阻塞的，负载能力比apache高很多，而apache则是阻塞型的。在高并发下nginx能保持低资源低消耗高性能，而apache在php处理慢或者前端压力很大的情况下，很容易出现进程数飙升，从而拒绝服务的现象。 

3、nginx在开启时，会生成一个master进程，然后，master进程会fork多个worker子进程，最后每个用户的请求由worker的子线程处理。 

4、可以配置nginx的upstream实现nginx的反向代理。 

5、nginx作为负载均衡服务器，支持7层负载均衡。 

6、nginx处理静态文件好，静态处理性能比apache高三倍以上。

7、支持高并发连接，每秒最多的并发连接请求理论可以达到50000个。 

8、nginx配置简洁，正则配置让很多事情变得简单，而且改完配置能使用-t测试配置有没有问题，apache配置复杂，重启的时候发现配置出错了，会很崩溃。 

9、用线程处理用户请求，而线程是共享内存的，只需要开启少量进程，多个线程就可以共享进程的内存，占用内存小。 

10、一个进程死掉时，会影响到多个用户的使用，稳定性差。

11、nginx的设计高度模块化，编写模块相对简单。

12、nginx本身就是一个反向代理服务器，而且可以作为非常优秀的邮件代理服务器。

13、启动特别容易，并且几乎可以做到7*24不间断运行，即使运行数个月也不需要重新启动，还能够不间断服务的情况下进行软件版本的升级。

14、社区活跃，各种高性能模块出品迅速。

 

Apache特点 

1、select同步阻塞。

2、一个连接对应一个进程。

3、用进程处理用户请求，用MPM（多处理模块）来绑定到网络端口上，接受请求，调度子进程处理请求。

4、当用户请求过多时，开启的进程较多，占用内存大，每秒最多的并发连接请求最多不超过3000个。

5、一个进程死掉时，不会影响其他的用户

6、apache的rewrite比nginx强大，在rewrite频繁的情况下，用apache。 

7、apache发展到现在，模块超多，基本想到的都可以找到。 

8、apache更为成熟，少bug，nginx的bug相对较多。 

9、apache超稳定。 

10、apache对php支持比较简单，nginx需要配合其他后端用。 

11、apache在处理动态请求有优势，一般动态请求要apache去做，nginx适合静态和反向。

12、apache仍然是目前的主流，拥有丰富的特性，成熟的技术和开发社区

 

两者最核心的区别在于apache是同步多进程模型，一个连接对应一个进程，而nginx是异步的，多个连接（万级别）可以对应一个进程。一般来说，需要性能的web服务，用nginx。如果不需要性能只求稳定，更考虑apache，apache的各种功能模块实现比nginx好，例如ssl的模块就比nginx好，可配置项多。epoll（freebsd上是kqueue）网络IO模型是nginx处理性能高的根本理由，但并不是所有的情况下都是epoll大获全胜的，如果本身提供静态服务的就只有寥寥几个文件，apache的select模型或许比epoll更高性能。当然，这只是根据网络IO模型的原理作的一个假设，真正的应用还是需要实测。更为通用的方案是，前端nginx抗并发，后端apache集群，配合起来会更好

# 查询集两大特性？惰性执行？

django中的查询集有大特性：

1.  惰性执行

```python
books = BookInfo.objects.all() # 此时,数据库并不会进行实际查询
# 只有当真正使用时,如遍历的时候,才会真正去数据库进行查询
for b in books:
  print(b)
```

2.  缓存

```python
# 进行数据库实际查询遍历,保存结果到bs,会进行数据库实际交互
bs = [b.id for b in BookInfo.objects.all()]

# 再次调用缓存结果bs,不再进行数据库查询,而是使用缓存结果
print(bs) # [1, 2, 3, 4, 5, 6, 7, 10]
```



# django中csrf的实现机制?

第一步：django第一次响应来自某个客户端的请求时,后端随机产生一个token值，把这个token保存在SESSION状态中;同时,后端把这个token放到cookie中交给前端页面；

第二步：下次前端需要发起请求（比如发帖）的时候把这个token值加入到请求数据或者头信息中,一起传给后端；Cookies:{csrftoken:xxxxx}

第三步：后端校验前端请求带过来的token和SESSION里的token是否一致。

 

# django的Model中的ForeignKey字段中的on_delete参数有什么作用？

删除时的关联外键的模式。

需要注意的是，在Django1.x版本中，该参数是有默认参数`None`，也就是`models.CASCADE`，我们不指定该字段，但是，到了Django2.x版本中，就取消了默认参数，也就需要我们手动指定了。除了默认的，还有以下几个参数，供我们选用：

-   `CASCADE`：这就是默认的选项，级联删除，Django1.x中无需显式指定它。
-   `PROTECT`： 保护模式，如果采用该选项，删除的时候，会抛出`ProtectedError`错误。
-   `SET_NULL`： 置空模式，删除的时候，外键字段被设置为空，前提就是``blank=True`，`null=True`，定义该字段的时候，允许为空。
-   `SET_DEFAULT`：置默认值，删除的时候，外键字段设置为默认值，所以定义外键的时候注意加上一个默认值。

# ajax解决跨域的几种方式？线上如何解决跨域问题?

https://www.cnblogs.com/Neeo/articles/11455271.html

线上一般通过nginx进行配置。

# Django的中间件

django 中间件的使用，Django在中间件中，预留了几个方法？每个方法的作用？
Django 在中间件中预置了六个方法，这六个方法的区别在于不同的阶段执行，对输入或输出进行干预，方法如下：

1. 初始化：无需任何参数，服务器响应第一个请求的时候调用一次，用于确定是否启用当前中间件。

```python
def init(): pass
```
2. 处理请求前：在每个请求上调用，返回 None 或 HttpResponse 对象。

```python
def process_request(request): pass
```
3. 处理视图前：在每个请求上调用，返回 None 或 HttpResponse 对象。

```python
def process_view(request, view_func, view_args, view_kwargs): pass
```
4. 处理模板响应前：在每个请求上调用，返回实现了 render 方法的响应对象。

```python
def process_template_responose(request, response): pass
```
5. 处理响应后：所有响应返回浏览器之前被调用，在每个请求上调用，返回 HttpResponse 对象。

```python
def process_response(request, response): pass
```
6. 异常处理：当视图抛出异常时调用，在每个请求上调用，返回一个 HttpResponse 对象。

```python
def process_exception(request, exception): pass
```

# Django 中间件是如何使用的?

在settings中通过MIDDLEWARE进行配置，且中间件是有顺序的，从上到下依次通过，我们自定义的中间件如果使用的话也要按照正确的顺序添加到这里

而自定义中间需要继承

```python
from django.utils.deprecation import MiddlewareMixin
```

然后将自定义的中间件添加到settings的MIDDLEWARE列表中

# DRF相关

## 什么是restful风格？

rest(Representational State Transfer)，一种软件架构风格、设计风格，而不是标准，只是提供了一组设计原则和约束条件。满足这些条件和原则的应用程序或者设计就是resutful。

基于restful风格开发的软件可以更简洁，更有层次和更易实现缓存等机制。

restful特点：

1.  每一个URI代表一种资源，独一无二
2.  客户端和服务器之间，传递这种资源的某种表现层
3.  客户端通过四个HTTP动词，对服务器端资源进行操作，实现"表现层状态转化"。

## 简要介绍下restful

定义：restful API 是一种符合rest风格的接口，rest是一种架构风格，采用http协议。

作用：

-   前后端分离一般会使用restful接口
-   可以使前后端解耦，减少服务器压力，前后端分工明确，提高安全性

主要思想：

-   网络上的事务的都被抽象为资源
-   每个资源都有唯一的标识符，并且对资源的各自操作不会改变标识符
-   所有操作都是无状态的
-   同一个资源具有多种表现形式(xml/json等)，数据传输一般使用的格式是json（全是双引号），以前用的是webservice，数据传输格式是xml

## 使用restful api的一些建议

1.  建议使用https代替http，保证传输数据的安全
2.  url中要体现api标识
3.  url中要体现版本
4.  api接口一般使用名字不使用动词
5.  使用不同的方法来进行不同的操作
6.  给用户返回一些状态码
7.  不同的请求方法返回不同类型的返回值，添加和更新一般返回添加的数据，删除不返回数据，获取数据一般返回列表套字典的形式
8.  操作异常返回错误信息
9.  推荐在返回数据的时候，返回其他相关联的一些数据的接口网址，例如分页器可以返回上一页下一页的网址
    

## 如何设计符合 RESTful 风格的 API？

可以从以下几个方面着手：

1.  域名：	
    1.  将api部署在专用域名下：http://api.example.com1
    2.  或者将api放在主域名下：http://www.example.com/api/1

2.  版本：将API的版本号放在url中。
    -   http://www.example.com/app/1.0/info
    -   http://www.example.com/app/1.2/info

3.  路径：路径表示API的具体网址。每个网址代表一种资源。 资源作为网址，网址中不能有动词只能有名词，一般名词要与数据库的表名对应。而且名词要使用复数。

    -   错误示例：
        -   http://www.example.com/getGoods
        -   http://www.example.com/listOrders

    -   正确示例：
        -   获取单个商品：http://www.example.com/app/goods/1
        -   获取所有商品：http://www.example.com/app/goods1

4.  使用标准的HTTP方法：对于资源的具体操作类型，由HTTP动词表示。 常用的HTTP动词有四个。

    -   GET   SELECT ：从服务器获取资源。

    -   POST  CREATE ：在服务器新建资源。

    -   PUT   UPDATE ：在服务器更新资源。

    -   DELETE DELETE ：从服务器删除资源。
    -   示例：
        -   获取指定商品的信息GET http://www.example.com/goods/ID
        -   新建商品的信息POST http://www.example.com/goods
        -   更新指定商品的信息PUT http://www.example.com/goods/ID
        -   删除指定商品的信息DELETE http://www.example.com/goods/ID1

5.  过滤信息：如果资源数据较多，服务器不能将所有数据一次全部返回给客户端。API应该提供参数，过滤返回结果。 实例：

    -   指定返回数据的数量http://www.example.com/goods?limit=10

    -   指定返回数据的开始位置http://www.example.com/goods?offset=10

    -   指定第几页，以及每页数据的数量http://www.example.com/goods?page=2&per_page=201

6.  状态码：服务器向用户返回的状态码和提示信息，常用的有：
    -   200 OK ：服务器成功返回用户请求的数据
    -   201 CREATED ：用户新建或修改数据成功。
    -   202 Accepted：表示请求已进入后台排队。
    -   400 INVALID REQUEST ：用户发出的请求有错误。
    -   401 Unauthorized ：用户没有权限。
    -   403 Forbidden ：访问被禁止。
    -   404 NOT FOUND ：请求针对的是不存在的记录。
    -   406 Not Acceptable ：用户请求的的格式不正确。
    -   500 INTERNAL SERVER ERROR ：服务器发生错误。

7.  错误信息：一般来说，服务器返回的错误信息，以键值对的形式返回。

    ```python
    {
    	error:'Invalid API KEY'
    }
    ```

8.  响应结果：针对不同结果，服务器向客户端返回的结果应符合以下规范。

    - 返回商品列表GET  http://www.example.com/goods

    -   返回单个商品GET  http://www.example.com/goods/cup

    -   返回新生成的商品POST  http://www.example.com/goods

    -   返回一个空文档DELETE http://www.example.com/goods1

9.  使用链接关联相关的资源：在返回响应结果时提供链接其他API的方法，使客户端很方便的获取相关联的信息。

10.  其他：服务器返回的数据格式，应该尽量使用JSON，避免使用XML。

## 为什么要使用framework框架？

-   不是必须要使用，只不过使用了视图类可以更加的规范，让我们前后端降低耦合性，更加安全快捷。
-   增删改查的实现流程基本一样，使用视图类可以更快捷的开发。
-   在序列化的时候，操作数据不同，但是流程相似，可以继承 serializers.ModelSerializer类简写

## framework框架提供的组件

1.  序列化组件:serializers ，对queryset序列化以及对请求数据格式校验
2.  视图组件， 帮助开发者提供了一些类，并在类中提供了多个方法
3.  渲染器 定义数据如何渲染到到页面上,在渲染器类中注册(renderer_classes)
4.  解析器 选择对数据解析的类，在解析器类中注册(parser_classes)
5.  分页 对获取到的数据进行分页处理, pagination_class
6.  路由组件routers 进行路由分发
7.  认证组件 写一个类并注册到认证类(authentication_classes)，在类的的authticate方法中编写认证逻
8.  权限组件 写一个类并注册到权限类(permission_classes)，在类的的has_permission方法中编写认证逻辑
9.  频率限制 写一个类并注册到频率类(throttle_classes)，在类的的allow_request/wait 方法中编写认证逻辑
10.  版本 版本控制用来在不同的客户端使用不同的行为



# Flask

## flask请求钩子

flask请求钩子，before_first_request、before_request、after_request、teardown_request，这几种钩子都是何时执行？

flask请求钩子是通过装饰器的形式实现，flask支持如下四种请求钩子：

-   before_first_request：在处理第一个请求前执行。
-   before_request：在每次请求前执行，在该装饰器函数中，一旦return，视图函数不在执行。
-   after_request：如果没有抛出错误，在每次请求后执行，接收一个参数：视图函数做出的响应，在返回之前，可以对响应值做相应的处理之后再返回。
-   teardown_request：在每次请求后执行，接收一个参数，用来接收错误参数。










see also: [关于Django+Framework的最完整面试题（2）](https://blog.csdn.net/qq_40558166/article/details/107187090)