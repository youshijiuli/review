[TOC]

### Redis的内存管理机制与GC？

### 如何使用Redis实现分布式锁？



### 持久化恢复问题

说明：

-   之前一直使用RDB进行数据持久化。
-   现在决定要使用AOF和RDB同时进行数据持久化。

现在的问题是：在开启AOF功能后，Redis在启动时会优先读取AOF文件进行数据恢复，但此时的AOF文件是空的，而数据都在RDB文件中，那启动后的Redis还是没有数据。请你尝试进行数据恢复。

**解决办法参考**

原因上面已经说了，AOF的优先级比RDB高，导致Redis启动时没有读取RDB文件进行恢复。

我的解决思路是：

-   将AOF持久化的所有参数都配置好，但保持配置文件中的`appendonly no`，这样做的目的让Redis认为没有开启AOF持久化，它在启动时仍会继续加载RDB文件进行数据恢复了。
-   经过上一步的动作，Redis启动后，数据恢复完毕。
-   现在要解决怎么在Redis运行时开启AOF持久化功能，我这里采用config命令执行：
    -   `config set appendonly yes`，热开启AOF持久化命令，现在AOF正常工作，根据你的AOF配置，产生了AOF文件，也将数据持久化到了该文件中。
    -   但有个问题，config命令是临时生效，即`appendonly yes`不会被同步到配置文件中，你还要想着去手动修改配置文件。当然，再介绍个命令：`config rewrite`，将最新的配置信息重写到配置文件中，真是简单方便。

来看过程：

```bash
# 刚开始，只开启了RDB
127.0.0.1:6379> config get appendonly    # AOF是关闭的
1) "appendonly"
2) "no"
127.0.0.1:6379> keys *     # 有数据
 1) "k1"
 2) "k7"
 3) "k9"
 4) "k3"
 5) "k2"
 6) "k8"
 7) "k4"
 8) "k6"
 9) "k10"
10) "k5"

# AOF文件也不存在
[root@cs 6379]# ls
dump.rdb  redis.conf  redis.log

# 配置文件: 
appendonly no
appendfilename "appendonly-6379.aof"
appendfsync everysec
```

现在，重启Redis，让它根据RDB文件进行数据恢复：

```bash
[root@cs 6379]# redis-cli shutdown
[root@cs 6379]# redis-server redis.conf    # 根据RDB文件进行数据恢复
[root@cs 6379]# redis-cli -p 6379
127.0.0.1:6379> keys *   #  数据都还在
 1) "k2"
 2) "k9"
 3) "k1"
 4) "k10"
 5) "k3"
 6) "k8"
 7) "k4"
 8) "k6"
 9) "k7"
10) "k5"
```

重要的操作来了：

```bash
127.0.0.1:6379> config get appendonly    # 起初AOF还是关闭的
1) "appendonly"
2) "no"
127.0.0.1:6379> config set appendonly yes  # 开启它
OK
127.0.0.1:6379> config get appendonly		# AOF开启了，但配置文件的该参数还是no状态
1) "appendonly"
2) "yes"
127.0.0.1:6379> config rewrite     	# 将最新的配置信息重写到配置文件中
OK
```

此时，AOF功能开启后，AOF文件也创建好了，这个时候，你就是把RDB文件删了，数据也能从AOF中进行恢复：

```bash
[root@cs 6379]# ls
appendonly-6379.aof  dump.rdb  redis.conf  redis.log
[root@cs 6379]# redis-cli shutdown			# 关闭Redis
[root@cs 6379]# rm -rf dump.rdb 			# 删除RDB文件
[root@cs 6379]# vim redis.conf 				# 我确认了下配置文件的appenonly 的确为 yes
[root@cs 6379]# redis-server redis.conf     # 启动Redis，它会根据AOF文件进行数据恢复
[root@cs 6379]# redis-cli -p 6379
127.0.0.1:6379> keys *  					# 数据都还在
 1) "k1"
 2) "k4"
 3) "k3"
 4) "k5"
 5) "k8"
 6) "k6"
 7) "k10"
 8) "k2"
 9) "k9"
10) "k7"
127.0.0.1:6379> save						# 手动save下，让它产生RDB文件
OK

[root@cs 6379]# ls							# 现在两个持久化文件都有了
appendonly-6379.aof  dump.rdb  redis.conf  redis.log
```

经过上面的一顿操作，数据恢复完毕，Redis再怎么重启也都有可以进行数据恢复了。





### 举例说明下Redis五种数据类型及应用场景(3)



### 什么是哨兵模式以及哨兵模式的作用(2021/4/6)



### 简述Redis的管道技术(2021/3/9)

### 在Redis中，什么时候需要用到pipeline？(2021/4/9)

### redis和memcached的区别？

1、Redis和Memcache都是将数据存放在内存中，都是内存数据库。不过memcache还可用于缓存其他东西，例如图片、视频等等；

2、Redis不仅仅支持简单的k/v类型的数据，同时还提供list，set，hash等数据结构的存储；

3、虚拟内存--Redis当物理内存用完时，可以将一些很久没用到的value 交换到磁盘；

4、过期策略--memcache在set时就指定，例如set key1 0 0 8,即永不过期。Redis可以通过例如expire 设定，例如expire name 10；

5、分布式--设定memcache集群，利用magent做一主多从;redis可以做一主多从。都可以一主一从；

6、存储数据安全--memcache挂掉后，数据没了；redis可以定期保存到磁盘（持久化）；

7、灾难恢复--memcache挂掉后，数据不可恢复; redis数据丢失后可以通过aof恢复；

8、Redis支持数据的备份，即master-slave模式的数据备份；

9、应用场景不一样：Redis出来作为NoSQL数据库使用外，还能用做消息队列、数据堆栈和数据缓存等；Memcached适合于缓存SQL语句、数据集、用户临时性数据、延迟查询数据和session等。

 

### 如何高效的找到redis中所有以zhang开头的key？



### 什么是一致性哈希？

参考：https://blog.csdn.net/qq_21125183/article/details/90019034

### 简述redis分布式锁？

为redis集群设计的锁,防止多个任务同时修改数据库,其本质就是为集群中的每个主机设置一个会超时的字符串,当集群中有一半多的机器设置成功后就认为加锁成功,直至锁过期或解锁不会有第二个任务加锁成功

### Redis 中 list 底层实现有哪几种？有什么区别？

列表对象的编码可以是 ziplist 或者 linkedlist

ziplist 是一种压缩链表，它的好处是更能节省内存空间，因为它所存储的内容都是在连续的内存区域当中的。当列表对象元素不大，每个元素也不大的时候，就采用 ziplist 存储。但当数据量过大时就 ziplist 就不是那么好用了。因为为了保证他存储内容在内存中的连续性，插入的复杂度是 O(N)，即每次插入都会重新进行 realloc。如下图所示，对象结构中 ptr 所指向的就是一个 ziplist。整个 ziplist只需要 malloc 一次，它们在内存中是一块连续的区域。

 

参考：https://blog.csdn.net/qq_26742855/article/details/105793947

### 怎样解决数据库高并发的问题？

解决数据库高并发的常见方案：

1.  缓存式的 Web 应用程序架构。在 Web 层和 DB(数据库)层之间加一层 cache 层，主要目的：减少数据库读取负担，提高数据读取速度。cache 存取的媒介是内存，可以考虑采用分布式的 cache 层，这样更容易破除内存容量的限制，同时增加了灵活性。

2.  增加 Redis 缓存数据库

3.  增加数据库索引

4.  页面静态化，效率最高、消耗最小的就是纯静态化的 html 页面，所以我们尽可能使我们的网站上的页面采用静态页面来实现，这个最简单的方法其实也是最有效的方法。用户可以直接获取页面，不用像 MVC结构走那么多流程，比较适用于页面信息大量被前台程序调用，但是更新频率很小的情况。\5.  使用存储过程：处理一次请求需要多次访问数据库的操作，可以把操作整合到储存过程，这样只要一次数据库访问就可以了\6.  MySQL 主从读写分离,当数据库的写压力增加，cache 层（如 Memcached）只能缓解数据库的读取压力。读写集中在一个数据库上让数据库不堪重负。使用主从复制技术（master-slave 模式）来达到读写分离，以提高读写性能和读库的可扩展性。读写分离就是只在主服务器上写，只在从服务器上读，基本原理是让主数据库处理事务性查询，而从数据库处理 select 查询，数据库复制被用于把事务性查询（增删改）导致的改变更新同步到集群中的从数据库。

    MySQL 读写分离提升系统性能：

    1.   主从只负责各自的读和写，极大程度缓解 X 锁和 S 锁争用。
    2.  slave 可以配置 MyISAM 引擎，提升查询性能以及节约系统开销。
    3.  master 直接写是并发的，slave 通过主库发送来的 binlog 恢复数据是异步的。
    4.  slave 可以单独设置一些参数来提升其读的性能。
    5.  增加冗余，提高可用性。

    实现主从分离可以使用 MySQL 中间件如：Atlas

7.  分表分库：在 cache 层的高速缓存，MySQL 的主从复制，读写分离的基础上，这时 MySQL 主库的写压力开始出现瓶颈，而数据量的持续猛增，由于 MyISAM 使用表锁，在高并发下会出现严重的锁问题，大量的高并发 MySQL 应用开始使用 InnoDB 引擎代替 MyISAM。采用 Master-Slave 复制模式的 MySQL 架构，只能对数据库的读进行扩展，而对数据的写操作还是集中在 Master 上。这时需要对数据库的吞吐能力进一步地扩展，以满足高并发访问与海量数据存储的需求。对于访问极为频繁且数据量巨大的单表来说，首先要做的是减少单表的记录条数，以便减少数据查询所需的时间，提高数据库的吞吐，这就是所谓的分表【水平拆分】。在分表之前，首先需要选择适当的分表策略（尽量避免分出来的多表关联查询），使得数据能够较为均衡地分布到多张表中，并且不影响正常的查询。分表能够解决单表数据量过大带来的查询效率下降的问题，但是却无法给数据库的并发处理能力带来质的提升。面对高并发的读写访问，当数据库 master 服务器无法承载写操作压力时，不管如何扩展 Slave 服务器都是没有意义的，对数据库进行拆分，从而提高数据库写入能力，即分库【垂直拆分】

8.  负载均衡集群，将大量的并发请求分担到多个处理节点。由于单个处理节点的故障不影响整个服务，负载均衡集群同时也实现了高可用性。负载均衡将是大型网站解决高负荷访问和大量并发请求采用的终极解决办法。

 

### Redis 集群实现？

类似的问题有：如何实现redis集群？

 

由于Redis出众的性能，其在众多的移动互联网企业中得到广泛的应用。Redis在3.0版本前只支持单实例模式，虽然现在的服务器内存可以到100GB、200GB的规模，但是单实例模式限制了Redis没法满足业务的需求（例如新浪微博就曾经用Redis存储了超过1TB的数据）。Redis的开发者Antirez早在博客上就提出在Redis 3.0版本中加入集群的功能，但3.0版本等到2015年才发布正式版。各大企业在3.0版本还没发布前为了解决Redis的存储瓶颈，纷纷推出了各自的Redis集群方案。这些方案的核心思想是把数据分片（sharding）存储在多个Redis实例中，每一片就是一个Redis实例。

Redis的集群方案：

1.  客户端分片：客户端分片是把分片的逻辑放在Redis客户端实现，通过Redis客户端预先定义好的路由规则，把对Key的访问转发到不同的Redis实例中，最后把返回结果汇集。

2.  Twemproxy：Twemproxy是由Twitter开源的Redis代理，其基本原理是：Redis客户端把请求发送到Twemproxy，Twemproxy根据路由规则发送到正确的Redis实例，最后Twemproxy把结果汇集返回给客户端。Twemproxy通过引入一个代理层，将多个Redis实例进行统一管理，使Redis客户端只需要在Twemproxy上进行操作，而不需要关心后面有多少个Redis实例，从而实现了Redis集群
3.  Redis 3.0集群：Redis 3.0集群采用了P2P的模式，完全去中心化。Redis把所有的Key分成了16384个slot，每个Redis实例负责其中一部分slot。集群中的所有信息（节点、端口、slot等），都通过节点之间定期的数据交换而更新。Redis客户端在任意一个Redis实例发出请求，如果所需数据不在该实例中，通过重定向命令引导客户端访问所需的实例

4.  云服务器上的集群服务：国内的云服务器提供商阿里云、UCloud等均推出了基于Redis的云存储服务。

详情参考：https://www.cnblogs.com/zhuifeng-mayi/p/9306852.html

### Redis 和 MongoDB 的优缺点

MongoDB 和 Redis 都是 NoSQL，采用结构型数据存储。二者在使用场景中，存在一定的区别，这也主要由于二者在内存映射的处理过程，持久化的处理方法不同。MongoDB 建议集群部署，更多的考虑到集群方案，Redis 更偏重于进程顺序写入，虽然支持集群，也仅限于主-从模式。

Redis 优点：

1.  读写性能优异

2.  支持数据持久化，支持 AOF 和 RDB 两种持久化方式

3.  支持主从复制，主机会自动将数据同步到从机，可以进行读写分离

4.  数据结构丰富：数据结构丰富：支持 string、hash、set、sortedset、list 等数据结构。

Redis 缺点：

1.  Redis 不具备自动容错和恢复功能，主机从机的宕机都会导致前端部分读写请求失败，需要等待机器重启或者手动切换前端的 IP 才能恢复。

2.  主机宕机，宕机前有部分数据未能及时同步到从机，切换 IP 后还会引入数据不一致的问题，降低了系统的可用性。

3.  Redis 的主从复制采用全量复制，复制过程中主机会 fork 出一个子进程对内存做一份快照，并将子进程的内存快照保存为文件发送给从机，这一过程需要确保主机有足够多的空余内存。若快照文件较大，对集群的服务能力会产生较大的影响，而且复制过程是在从机新加入集群或者从机和主机网络断开重连时都会进行，也就是网络波动都会造成主机和从机间的一次全量的数据复制，这对实际的系统运营造成了不小的麻烦。

4.  Redis 较难支持在线扩容，在集群容量达到上限时在线扩容会变得很复杂。为避免这一问题，运维人员在系统上线时必须确保有足够的空间，这对资源造成了很大的浪费。

 

MongoDB 优点:

1.  弱一致性（最终一致），更能保证用户的访问速度

2.  文档结构的存储方式，能够更便捷的获取数

3.  内置 GridFS，高效存储二进制大对象 (比如照片和视频)

4.  支持复制集、主备、互为主备、自动分片等特性

5.  动态查询

6.  全索引支持,扩展到内部对象和内嵌数组

MongoDB 缺点：

1.  不支持事务

2.  MongoDB 占用空间过大

3.  维护工具不够成熟

 

### Redis 默认端口，默认过期时间，Value 最多可以容纳的数据 长度？

默认端口：6379

默认过期时间：可以说永不过期，一般情况下，当配置中开启了超出最大内存限制就写磁盘的话，那么没有设置过期时间的 key 可能会被写到磁盘上。假如没设置，那么 REDIS 将使用 LRU机制，将内存中的老数据删除，并写入新数据。

Value 最多可以容纳的数据长度是：512M

关于LRU算法，参考：https://www.cnblogs.com/Neeo/articles/13882916.html

### Redis 数据库，内容是以何种结构存放在 Redis 中的？

String（字符串），Hash（哈希），List（列表），Set（集合）及 zset(sortedset：有序集合)。

### MySQL 和 Redis 高可用性体现在哪些方面？

1.  MySQL Replication 是 MySQL 官方提供的主从同步方案，用于将一个 MySQL 实例的数据，同步到另一个实例中。Replication 为保证 数据安全做了重要的保证，也是现在运用最广的 MySQL 容灾方案。Replication 用两个或以上的实例搭建了 MySQL 主从复制集群，提供 单点写入，多点读取的服务，实现了读的 scale out。

2.  Sentinel 是 Redis 官方为集群提供的高可用解决方案。在实际 项目中可以使用 sentinel去做 Redis 自动故障转移，减少人工介入的工作量。另外 sentinel 也给客户端提供了监控消息的通知，这样客户端就可根据消息类型去判断服务器的状态，去做对应的适配操作。

3.  下面是 Sentinel 主要功能列表：

    a.  Monitoring：Sentinel 持续检查集群中的 master、slave 状态，判断是否存活。

    b.  Notification：在发现某个 Redis 实例死的情况下，Sentinel 能通过 API 通知系统管理员或其他程序脚本。

    c.  Automatic failover：如果一个 master 挂掉后，sentinel 立马启动故障转移，把某个 slave 提升为 master。其他的 slave 重新配置指向新 master。

    d.  Configuration provider：对于客户端来说 sentinel 通知是有效可信赖的。客户端会连接sentinel 去请求当前 master 的地址，一旦发生故障 sentinel 会提供新地址给客户端。

 

### Redis 的使用场景有哪些？

1.  取最新 N 个数据的操作

2.  排行榜应用,取 TOP N 操作

3.  需要精准设定过期时间的应用

4.  计数器应用

5.  uniq 操作,获取某段时间所有数据排重值

6.  Pub/Sub 构建实时消息系统

7.  构建队列系统

8.  缓存

### Redis 的并发竞争问题怎么解决？

方案一：可以使用独占锁的方式，类似操作系统的 mutex 机制，不过实现相对复杂，成本较高。

方案二：使用乐观锁的方式进行解决（成本较低，非阻塞，性能较高）

如何用乐观锁方式进行解决？本质上是假设不会进行冲突，使用 redis 的命令 watch 进行构造条件

### redis是单进程还是单线程？

Redis是单线程的模式，它是利用队列技术将并发访问改为串行访问，消除传统的传统数据库的串行操作开销

### redis中数据库默认是多少个db 及作用？

Redis 一个实例下有 16 个：0 - 15

相当于不同的库

### 如果redis中的某个列表中的数据量非常大，如果实现循环显示每一个值？



### redis如何实现主从复制？以及数据同步机制？

在从服务器中配置 SLAVEOF 127.0.0.1：6380

 

### redis中的sentinel的作用？

监控主机状态,实现高可用

### redis中默认有多少个哈希槽？

16384

### 简述redis的有哪几种持久化策略及比较？

rdb:快照形式是直接把内存中的数据保存到一个dump文件中，定时保存，保存策略

aof：把所有的对redis的服务器进行修改的命令都存到一个文件里，命令的集合

 参考：https://www.cnblogs.com/Neeo/articles/10371306.html

### 列举redis支持的过期策略

1.  voltile-lru：从已设置过期时间的数据集（server.db[i].expires）中挑选最近最少使用的数据淘汰

2. volatile-ttl：从已设置过期时间的数据集（server.db[i].expires）中挑选将要过期的数据淘汰

3. volatile-random：从已设置过期时间的数据集（server.db[i].expires）中任意选择数据淘汰

4. allkeys-lru：从数据集（server.db[i].dict）中挑选最近最少使用的数据淘汰

5. allkeys-random：从数据集（server.db[i].dict）中任意选择数据淘汰

6. no-enviction（驱逐）：禁止驱逐数据

 

### MySQL 里有 2000w 数据，redis 中只存 20w 的数据，如何保证 redis 中都是热点数据？

redis内存数据级上升到一定大小时,就会实行数据淘汰策略,从数据集（server.db[i].dict）中挑选最近最少使用的数据淘汰

### 写代码，基于redis的列表实现 先进先出、后进先出队列、优先级队列。

```python
class Stack:

    def __init__(self, conn):
        self.conn = conn

    def push(self, val):
        self.conn.rpush('aaa', val)

    def pop(self):
        return self.conn.rpop('aaa')


class Heap:

    def __init__(self, conn):
        self.conn = conn

    def push(self, val):
        self.conn.rpush('bbb', val)

    def get(self):
        return self.conn.lpop('bbb')


class Pq:

    def __init__(self, conn):
        self.conn = conn

    def push(self, val, count):
        self.conn.zadd('ccc', val, count)

    def get(self):
        a = self.conn.zrange('ccc', 0, 0)[0]
        self.conn.zrem('ccc', a)
        return a
```



### 如何基于redis实现消息队列？

将列表维护成一个栈,设置获取数据的超时时间

参考：https://www.cnblogs.com/-wenli/p/12777703.html

### 如何基于redis实现发布和订阅？以及发布订阅和消息队列列的区别？

发送消息 : conn.publish(名称,消息)

接收消息 : conn.sunscribe(名称)

区别 : 消息队列,收到消息只会有一个处理者;发布订阅,所有的订阅者都会收到消息并进行处理

 

### 什么是codis？

豌豆荚团队提供的一个分布式 Redis 解决方案

### 什么是twemproxy？

Twemproxy 又称 nutcracker ，是一个memcache、redis协议的轻量级代理，一个用于sharding 的中间件。有了Twemproxy，客户端不直接访问Redis服务器，而是通过twemproxy 代理中间件间接访问。

作用 : 对redis数据分片处理

 

### redis如何实现事务？

1.  Redis 事务允许一组命令在单一步骤中执行。事务有两个属性，说明如下：

    a.  事务是一个单独的隔离操作：事务中的所有命令都会序列化、按顺序地执行。事务在执行的过程中，不会被其他客户端发送来的命令请求所打断

    b.  Redis 事务是原子的。原子意味着要么所有的命令都执行，要么都不执行

2.  一个事务从开始到执行会经历以下三个阶段：

    a.  开始事务

    b.  命令入队

    c.  执行事务

 参考：https://www.cnblogs.com/Neeo/articles/10371213.html#%E4%BA%8B%E5%8A%A1

### redis中的watch的命令的作用？

加锁

### 简述redis分布式锁和redlock的实现机制。

为redis集群设计的锁,防止多个任务同时修改数据库,其本质就是为集群中的每个主机设置一个会超时的字符串,当集群中有一半多的机器设置成功后就认为加锁成功,直至锁过期或解锁不会有第二个任务加锁成功

### 请设计一个商城商品计数器的实现方案？

字符串的decr可以实现自减操作

### 说说redis雪崩

https://blog.csdn.net/qq_29373285/article/details/88544299