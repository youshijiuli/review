[TOC]

### 什么是mongodb？

MongoDB是一个文档数据库，提供好的性能，领先的非关系型数据库。采用BSON存储文档数据。

BSON（）是一种类json的一种二进制形式的存储格式，简称Binary JSON.

相对于json多了date类型和二进制数组。

### 为什么用MOngoDB？

1.  架构简单

2.  没有复杂的连接

3.  深度查询能力,MongoDB支持动态查询。

4.  容易调试

5.  容易扩展

6.  不需要转化/映射应用对象到数据库对象

7.  使用内部内存作为存储工作区,以便更快的存取数据。

### mongodb的应用场景

1.  大数据
2.  内容管理系统
3.  移动端Apps
4.  数据管理

### mongodb的日志你是如何处理的？



### MongoDB中的命名空间是什么意思?

mongodb存储bson对象在丛集(collection)中。数据库名字和丛集名字以句点连结起来叫做名字空间(namespace)。一个集合命名空间又有多个数据域(extent)，集合命名空间里存储着集合的元数据，比如集合名称，集合的

第一个数据域和最后一个数据域的位置等等。而一个数据域由若干条文档(document)组成，每个数据域都有一个

头部，记录着第一条文档和最后一条文档的为知，以及该数据域的一些元数据。extent之间，document之间通过双向链表连接。索引的存储数据结构是B树，索引命名空间存储着对B树的根节点的指针。

### monogodb 中的分片什么意思

分片是将数据水平切分到不同的物理节点。当应用数据越来越大的时候，数据量也会越来越大。当数据量增长时，单台机器有可能无法存储数据或可接受的读取写入吞吐量。利用分片技术可以添加更多的机器来应对数据量增加以及读写操作的要求。

### Mongodb的一些基本操作命令（列举一些常用命令即可）？

1.  db.help(); Help 查看命令提示

2.  use yourDB; 切换/创建数据库

3.  show dbs; 查询所有数据库

4.  db.dropDatabase(); 删除当前使用数据库

5.  db.getName(); 查看当前使用的数据库

6.  db.version(); 当前 db 版本

7.  db.addUser("name"); 添加用户

8. db.addUser("userName", "pwd123", true);

9. show users; 显示当前所有用户

10. db.removeUser("userName"); 删除用户

11. db.yourColl.count(); 查询当前集合的数据条数

### 什么是集合(表)

集合就是一组 MongoDB 文档。它相当于关系型数据库（RDBMS）中的表这种概念。集合位于单独的一个数据库中。

一个集合内的多个文档可以有多个不同的字段。一般来说，集合中的文档都有着相同或相关的目的。

### 什么是文档(记录)

文档由一组key value组成。文档是动态模式,这意味着同一集合里的文档不需要有相同的字段和结构。在关系型数据库中table中的每一条记录相当于MongoDB中的一个文档。

### MongoDB和关系型数据库术语对比图

| Mongodb    | relational database |
| ---------- | ------------------- |
| database   | database            |
| collection | table               |
| document   | record/row          |
| field      | column              |

### Python 中调用 mongodb 数据库的包叫什么？

 Pymongo

详情参考：https://www.cnblogs.com/Neeo/articles/14271710.html

### MongoDB 成为优秀的 NoSQL 数据库的原因是什么?

类似的问题包括：使用 MongoDB 的优点？

以下特点使得 MongoDB 成为优秀的 NoSQL 数据库：

1.  面向文档，以 JSON 格式的文档保存数据

2.  高性能

3.  高可用性

4.  易扩展性

5.  丰富的查询语言

6.  可分片

7.  对数据存储友好

8.  任何属性都可以建立索引

### MongoDB支持主键外键关系吗

默认MongoDB不支持主键和外键关系。 用Mongodb本身的API需要硬编码才能实现外键关联，不够直观且难度较大

### MongoDB支持哪些数据类型

1.  String

2.  Integer

3.  Double

4.  Boolean

5.  Object

6.  Object ID

7.  Arrays

8.  Min/Max Keys

9.  Datetime

10. Code

11. Regular Expression等

### 为什么要在MongoDB中用"Code"数据类型

"Code"类型用于在文档中存储 JavaScript 代码。

### 为什么要在MongoDB中用"Regular Expression"数据类型

"Regular Expression"类型用于在文档中存储正则表达式

### 为什么在MongoDB中使用"Object ID"数据类型

"ObjectID"数据类型用于存储文档id

### "ObjectID"有哪些部分组成(2)

改题目也有这么问的：mongodb的objectid包含哪些信息？

一共有四部分组成：时间戳、客户端ID、客户进程ID、三个字节的增量计数器

### 在MongoDb中什么是索引

索引用于高效的执行查询,没有索引的MongoDB将扫描整个集合中的所有文档,这种扫描效率很低,需要处理大量的数据.  索引是一种特殊的数据结构,将一小块数据集合保存为容易遍历的形式.索引能够存储某种特殊字段或字段集的值,并按照索引指定的方式将字段值进行排序.

### mongodb索引基于什么数据结构实现？

>   https://docs.mongodb.com/v3.6/indexes/

答：B+tree

### 如何添加索引

使用db.collection.createIndex()在集合中创建一个索引

###  MongoDB索引有哪几种类型？

>   https://www.cnblogs.com/Neeo/articles/14325130.html

MongoDB中支持以下几种索引类型：

-   单列索引(Single Field)。
-   复合索引(Compound Indexes)。
-   多键索引(Multikey Indexes)。
-   文本索引(Text Indexes)。
-   哈希索引(Hashed Indexes)。

### 如何查询集合中的文档

```javascript
db.collectionName.find({key:value})
```

### 用什么方法可以格式化输出结果

```javascript
db.collectionName.find().pretty()
```

### 如何使用"AND"或"OR"条件循环查询集合中的文档

```javascript
db.mycol.find({   
    "$or": [key1: value1}, {key2:value2}]  
}).pretty()
```



### 更新数据

```javascript
db.collectionName.update({key:value},{$set:{newkey:newValue}})
```

### 如何删除文档

```javascript
db.collectionName.remove({key:value})
```

### 在MongoDB中如何排序

使用 1 和 -1 来指定排序方式，其中 1 表示升序，而 -1 表示降序。

```javascript
db.connectionName.find({key:value}).sort({columnName:1})
```

### 什么是聚合

聚合操作能够处理数据记录并返回计算结果。聚合操作能将多个文档中的值组合起来，对成组数据执行各种操作，返回单一的结果。它相当于 SQL 中的 count(*) 组合 group by。对于 MongoDB 中的聚合操作，应该使用aggregate()方法。

```javascript
db.COLLECTION_NAME.aggregate(AGGREGATE_OPERATION)
```

### 在MongoDB中什么是副本集（避免单点故障）

在MongoDB中副本集由一组MongoDB实例组成，包括一个主节点多个次节点，MongoDB客户端的所有数据都写入主节点(Primary),副节点从主节点同步写入数据，以保持所有复制集内存储相同的数据，提高数据可用性。

### 分析器在 MongoDB 中的作用是什么?

相似的问题：为什么要在MongoDB中使用分析器？

MongoDB 中包括了一个可以显示数据库中每个操作性能特点的数据库分析器。通过这个分析器你可以找到比预期慢的查询(或写操作);利用这一信息，比如，可以确定是否需要添加索引

### 怎么查看 MongoDB 正在使用的链接?

```javascript
db._adminCommand("connPoolStats");
```

### MongoDB支持存储过程吗？如果支持的话，怎么用？

MongoDB支持存储过程，它是javascript写的，保存在db.system.js表中。

### 如何理解MongoDB中的GridFS机制，MongoDB为何使用GridFS来存储文件？

GridFS是一种将大型文件存储在MongoDB中的文件规范。使用GridFS可以将大文件分隔成多个小文档存放，这样我们能够有效的保存大文档，而且解决了BSON对象有限制的问题

### 为什么MongoDB的数据文件很大？

MongoDB采用的预分配空间的方式来防止文件碎片。

### 当更新一个正在被迁移的块（Chunk）上的文档时会发生什么？

更新操作会立即发生在旧的块（Chunk）上，然后更改才会在所有权转移前复制到新的分片上。

###  如果用户移除对象的属性,该属性是否从存储层中删除?

是的,用户移除属性然后对象会重新保存(re-save()).

### 更新操作立刻fsync到磁盘?

不会,磁盘写操作默认是延迟执行的.写操作可能在两三秒(默认在60秒内)后到达磁盘.例如,如果一秒内数据库收到一千个对一个对象递增的操作,仅刷新磁盘一次.

### 如何执行事务/加锁?

mongodb没有使用传统的锁或者复杂的带回滚的事务,因为它设计的宗旨是轻量,快速以及可预计的高性能.可以把它类比成mysql mylsam的自动提交模式.通过精简对事务的支持,性能得到了提升,特别是在一个可能会穿过多个服务器的系统里.

 

### 启用备份故障恢复需要多久?

从备份数据库声明主数据库宕机到选出一个备份数据库作为新的主数据库将花费10到30秒时间.这期间在主数据库上的操作将会失败–包括写入和强一致性读取(strong consistent read)操作.然而,你还能在第二数据库上执行最终一致性查询(eventually consistent query)(在slaveok模式下),即使在这段时间里.

 

### 什么是master或primary?

它是当前备份集群(replica set)中负责处理所有写入操作的主要节点/成员.在一个备份集群中,当失效备援(failover)事件发生时,一个另外的成员会变成primary

### 我应该启动一个集群分片(sharded)还是一个非集群分片的 mongodb 环境?

(数据量大用集群分片,数据量小用非集群)

为开发便捷起见,我们建议以非集群分片(unsharded)方式开始一个 mongodb 环境,除非一台服务器不足以存放你的初始数据集.从非集群分片升级到集群分片(sharding)是无缝的,所以在你的数据集还不是很大的时候没必要考虑集群分片(sharding).

### 分片(sharding)和复制(replication)是怎样工作的?

每一个分片(shard)是一个分区数据的逻辑集合.分片可能由单一服务器或者集群组成,我们推荐为每一个分片(shard)使用集群.

 

### 数据在什么时候才会扩展到多个分片(shard)里?

mongodb 分片是基于区域(range)的.所以一个集合(collection)中的所有的对象都被存放到一个块(chunk)中.只有当存在多余一个块的时候,才会有多个分片获取数据的选项.现在,每个默认块的大小是 64mb,所以你需要至少 64 mb 空间才可以实施一个迁移.

### 如果在一个分片(shard)停止或者很慢的时候,我发起一个查询会怎样?

如果一个分片(shard)停止了,除非查询设置了“partial”选项,否则查询会返回一个错误.如果一个分片(shard)响应很慢,mongodb则会等待它的响应.

### 可以把movechunk目录里的旧文件删除吗?

没问题,这些文件是在分片(shard)进行均衡操作(balancing)的时候产生的临时文件.一旦这些操作已经完成,相关的临时文件也应该被删除掉.但目前清理工作是需要手动的,所以请小心地考虑再释放这些文件的空间.

### 如果块移动操作(movechunk)失败了,我需要手动清除部分转移的文档吗?

不需要,移动操作是一致(consistent)并且是确定性的(deterministic);一次失败后,移动操作会不断重试;当完成后,数据只会出现在新的分片里(shard).

 

### MySQL 与 MongoDB 本质之间最基本的差别是什么？

差别在多方面，例如：数据的表示、查询、关系、事务、模式的设计和定义、速度和性能。

MongoDB 是由 C++语言编写的，是一个基于分布式文件存储的开源数据库系统。在高负载的

情况下，添加更多的节点，可以保证服务器性能。

MongoDB 旨在为 WEB 应用提供可扩展的高性能数据存储解决方案。

MongoDB 将数据存储为一个文档，数据结构由键值(key=>value)对组成。MongoDB 文档类

似于 JSON 对象。字段值可以包含其他文档，数组及文档数组。

MongoDB 是一个面向文档的数据库，目前由 10gen 开发并维护，它的功能丰富齐全，所以完全可以替代 MySQL。

与 MySQL 等关系型数据库相比，MongoDB 的优点如下：

1.  弱一致性，更能保证用户的访问速度。

2.  文档结构的存储方式，能够更便捷的获取数据。

3.  内置 GridFS，支持大容量的存储。

4.  内置 Sharding。

5.  第三方支持丰富。(这是与其他的 NoSQL 相比，MongoDB 也具有的优势)

6.  性能优越

MongoDB 相对于MySQL，它还算比较年轻的一个产品，所以它的问题，就是成熟度肯定没有传统 MySQL那么成熟稳定。所以在使用的时候，第一，尽量使用稳定版，不要在线上使用开发版，这是一个大原则；

另外一点，备份很重要，MongoDB 如果出现一些异常情况，备份一定是要能跟上。除了通过传统的复制的方式来做备份，离线备份也还是要有，不管你是用什么方式，都要有一个完整的离线备份。往往最后出现了特殊情况，它能帮助到你；

另外，MongoDB 性能的一个关键点就是索引，索引是不是能有比较好的使用效率，索引是不是能够放在内存中，这样能够提升随机读写的性能。如果你的索引不能完全放在内存中，一旦出现随机读写比较高的时候，它就会频繁地进行磁盘交换，这个时候，MongoDB 的性能就会急剧下降，会出现波动。

另外，MongoDB 还有一个最大的缺点，就是它占用的空间很大，因为它属于典型空间换时间原则的类型。那么它的磁盘空间比普通数据库会浪费一些，而且到目前为止它还没有实现在线压缩功能，在 MongoDB 中频繁的进行数据增删改时，如果记录变了，例如数据大小发生了变化，这时候容易产生一些数据碎片，出现碎片引发的结果，一个是索引会出现性能问题，另外一个就是在一定的时间后，所占空间会莫明其妙地增大，所以要定期把数据库做修复，定期重新做索引，这样会提升 MongoDB 的稳定性和效率。

### mongodb分片集群的架构？

