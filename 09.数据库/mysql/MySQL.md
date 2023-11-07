[TOC]









### 你们公司是怎么测试mysql比redis在时间上处理结果快的

### 在MySQL中，utf8和utf8mb4的区别是什么？

MySQL在 5.5.3 之后增加了 `utf8mb4` 字符编码，mb4即 most bytes 4。简单说 utf8mb4 是 utf8 的超集并完全兼容utf8，能够用四个字节存储更多的字符。

但抛开数据库，标准的 UTF-8 字符集编码是可以用 1~4 个字节去编码21位字符，这几乎包含了是世界上所有能看见的语言了。然而在MySQL里实现的utf8最长使用3个字节，也就是只支持到了 Unicode 中的 [基本多文本平面](https://zh.wikipedia.org/wiki/Unicode字符平面映射)（U 0000至U FFFF），包含了控制符、拉丁文，中、日、韩等绝大多数国际字符，但并不是所有，最常见的就算现在手机端常用的表情字符 emoji和一些不常用的汉字，如 “墅” ，这些需要四个字节才能编码出来。

注：QQ里面的内置的表情不算，它是通过特殊映射到的一个gif图片。一般输入法自带的就是。

也就是当你的数据库里要求能够存入这些表情或宽字符时，可以把字段定义为 utf8mb4，同时要注意连接字符集也要设置为utf8mb4，否则在 [严格模式](http://seanlook.com/2016/04/22/mysql-sql-mode-troubleshooting/) 下会出现 `Incorrect string value: /xF0/xA1/x8B/xBE/xE5/xA2… for column 'name'`这样的错误，非严格模式下此后的数据会被截断。



### 备份语句(2021/5/2)

下面两个备份命名的意思是？以及两个命令的区别？

```bash
# 说明：world是数据库，其内有city、country、countrylanguage三张表
[root@cs ~]# mysqldump -uroot -p123 -S /tmp/mysql.sock world >/data/mysql_backup/world_all_table1.sql
[root@cs ~]# mysqldump -uroot -p123 -S /tmp/mysql.sock -B world >/data/mysql_backup/world_all_table2.sql
```

答案参考：上面两个命令都是备份指定库下所有表的到本地的指定文件中的备份语句。

区别：

-   第一个命令是针对表，也就是命令中省略了数据库后的所有表名，其完整的备份命令应该是：

    ```bash
    [root@cs ~]# mysqldump -uroot -p123 -S /tmp/mysql.sock world city country countrylanguage >/data/mysql_backup/world_all_table1.sql
    ```

    而针对表的意思是指，备份出的SQL文件，不包含建库和use语句，那么再根据这个备份文件做数据恢复时，需要手动建库和use到该数据库下，再进行恢复。

-   第二个命令相对于第一条命令，就专业多了，它也是备份指定的数据库，且备份文件包含建库和use语句，所以，遇到类似的业务场景，请选择第二条命令进行备份。

### 如何确认数据库是否开启了bin log？如何查看bin log的存储位置?(2021/4/23)

很明显面试官想考察的是你对bin log的掌握情况。

```sql
mysql> select @@log_bin;
+-----------+
| @@log_bin |
+-----------+
|         1 |
+-----------+
1 row in set (0.00 sec)

mysql> select @@log_bin_basename;
+-----------------------------------+
| @@log_bin_basename                |
+-----------------------------------+
| /data/mysql_data/binlog/mysql-bin |
+-----------------------------------+
1 row in set (0.00 sec)
```

更多参考：https://www.cnblogs.com/Neeo/articles/14006790.html

### 列举常见的关系型数据库和非关系型都有那些？

关系型数据库：

-   Oracle

-   MySQL

-   Microsoft sql server

-   IBM Db2

-   PostgreSQL

非关系型数据:

-   redis

-   mongodb

-   elasticsearch

### MySQL常见数据库引擎及区别？

主要区别：

-   InnoDB：提供ＡＣＩＤ事务，系统崩溃修复能力和多版本并发控制的行级锁，支持自增长序列，支持外键，mysql5.5之后默认数据库引擎

-   MyISAM：读取速度优越，常用于高读取的应用场景数据库，支持三种不同类型的存储结构：静态型、动态型、压缩型。不支持事务和外键。

区别：

-   InnoDB支持事务，MyISAM不支持，对于InnoDB每一条SQL语言都默认封装成事务，自动提交，这样会影响速度，所以最好把多条SQL语言放在begin和commit之间，组成一个事务；

-   InnoDB支持外键，而MyISAM不支持，对一个包含外键的InnoDB表转为MyISAM会失败；

-   InnoDB是聚集索引，数据文件是和索引绑在一起的，必须要有主键，通过主键索引效率很高，但是辅助索引需要两次查询，先查询到主键，然后再通过主键查询到数据，主键不应该过大，因为主键太大，其他索引也都会很大；而MyISAM是非聚集索引，数据文件是分离的，索引保存的是数据文件的指针，主键索引和辅助索引是独立的；

-   InnoDB不保存表的具体行数，执行select count(*) fron table 时需要全表扫描，而MyISAM用一个变量保存了整个表的行数，执行上述语句时只需要读出该变量即可，速度很快；

-   InnoDB不支持全文索引，而MyISAM支持全文索引，查询效率上MyISAM要高。

选择：

-   是否支持事务，如果要请选择InnoDB，如果不需要可以考虑MyISAM；

-   如果表中绝大多数都只是读查询，可以考虑MyISAM，如果既有读写也挺频繁的，请使用InnoDB；

-   系统崩溃后，MyISAM恢复起来更困难，能否接受；

-   MySQL5.5版本开始InnoDB已经成为MySQL的默认引擎（之前是MyISAM），说明其优势是有目共睹的，如果你不知道用什么，那就用InnoDB，至少不会差

### 事务相关(2020/11/29)

事务就是一个程序执行单元，里面的操作要么都做，要么都不做。

通常数据库事务具备四大特性(ACID)，分别是：
1、原子性
2、一致性
3、隔离性
4、持久性
所谓原子性：是指事务是一个最小单元，不可再分隔，成为一个整体。
所谓一致性：是指事务中的方法要么同时成功，要么都不成功。比如A向B转账，要不都成功，要不都失败。
所谓隔离性：是指当多个事务操作数据库中同一个记录或多个记录时，对事务进行隔离开来有序执行，避免同时对同一数据做操作。这时候就需要使用锁来解决这个问题了(后面讲)。
所谓持久性：即当成功插入一条数据库记录时，数据库必须保证有一条数据永久的写入到数据库磁盘中。



### 简述触发器、函数、视图、存储过程？

存储过程：把一段代码封装起来，当要执行这一段代码的时候，可以通过调用该存储过程来实现（经过第一次编译后再次调用不需要再次编译，比一个个执行sql语句效率高）

函数：将一段SQL逻辑进行封装，后续可以任意调用。

视图：视图是由查询结果形成的一张虚拟表，是表通过某种运算得到的一个投影，作用就是把复杂的查询语句封装起来,然后通过视图来进行查询

触发器：触发器是一个特殊的存储过程，它是MySQL在insert、update、delete的时候自动执行的代码块，注意，MySQL 的触发器中不能对本表进行 insert、update 和 delete 操作，否则会报错。



### MySQL索引种类

普通索引：仅加速查询

唯一索引：加速查询 + 列值唯一（可以有null）

主键索引：加速查询 + 列值唯一（不可以有null）+ 表中只有一个

组合索引：多列值组成一个索引，专门用于组合搜索，其效率大于索引合并

全文索引：对文本的内容进行分词，进行搜索

### 索引在什么情况下遵循最左前缀的规则？

在联合索引中，如果创建的联合索引是`index(a, b, c)`这样，那么a、a,b、a,b,c这三种查询类型会走联合索引。另外a,c也走联合索引，只不过走的是a列索引，不会走c列的索引。

### 列举创建索引但是无法命中索引的情况。



1.  如果条件中有 or ，即使其中有条件带索引也不会使用(这也是为什么尽量少用or的原因）。注意：要想使用or，又想让索引生效，只能将or条件中的每个列都加上索引，如果出现OR的一个条件没有索引时，建议使用 union ，拼接多个查询语句

2.  like查询是以%开头，索引不会命中

3.  如果列类型是字符串，那一定要在条件中将数据使用引号引用起来,否则不使用索引

4. 没有查询条件，或者查询条件没有建立索引

5. 查询条件中，在索引列上使用函数（+, - ,*,/）, 这种情况下需建立函数索引

6. 采用 not in, not exist

7. B-tree 索引 is null 不会走， is not null 会走

8. 连表时，如果关联字段的的编码不同，也不会走索引。如一个表时 utf8，另外一个表是utf8mb4

参考：[索引无法命中的情况](https://www.cnblogs.com/Neeo/articles/13602317.html#%E7%B4%A2%E5%BC%95%E6%97%A0%E6%B3%95%E5%91%BD%E4%B8%AD%E7%9A%84%E6%83%85%E5%86%B5)



### MySQL常见的函数？

-   聚合函数：avg，sum，count，max，min

-   数学函数：绝对值函数：abs(x)， 取模函数：mod(x,y)， 随机数函数：rand() 四舍五入函数：round(x,y)

-   字符串函数：合并字符串concat(str1,str2,str3…)。

-   比较字符串大小：strcmp(str1,str2)。

-   获取字符串字节数函数：length(str)

-   日期和时间函数：获取当前日期时间：now()

-   从日期中选择出月份数：month(date)，monthname(date)

-   从日期中选择出周数：week(date)

-   从时间中选择出小时数：hour(time)

-   从时间中选择出分钟数：minute(time)， year()，day()

-   条件判断函数： if 处理双分支、case 处理多分支

 

参考：https://www.cnblogs.com/Neeo/articles/13685832.html





### 数据库导入导出命令（结构+数据）？

导入：

mysql -uroot -p <school.sql

导出：

mysql -uroot -p >school.sql



### 你了解那些数据库优化方案？

 

合理的建立索引

分表,降低树的高度

优化数据结构，用char代替varchar

定长字段放在前面，变长放在后面

读写分离



### MySQL中having的作用(2021/4/6)

### 常见SQL的优化(2021/3/19-2)



### 数据库中有一条语句执行速度非常慢，请问如何优化(2021/3/9)



### char和varchar的区别及varchar(50)中50代表的含义？(2021/3/29)

char：定长，效率高，一般用于固定长度的表单提交数据存储 ；例如：身份证号，手机号，电话，密码等

varchar：不定长，效率偏低,

总的来说：

长度的区别，char范围是0～255，varchar最长是64k，但是注意这里的64k是整个row的长度,要考虑到其它的 column，还有如果存在not null的时候也会占用一位，对不同的字符集，有效长度还不一样，比如utf8的，最多21845。

varchar 编码长度限制：

字符类型若为gbk，每个字符最多占2个字节，最大长度不能超过32766;

字符类型若为utf8，每个字符最多占3个字节，最大长度不能超过21845。

若定义的时候超过上述限制，则varchar字段会被强行转为text类型，并产生warning。

在mql4中,50代表的是该字段可以存储的数据的最大长度是50个字节,使用utf-8存汉字时,最大只能存储6个汉字。

在mysql5中，varchar(50)代表着50个字符，最大65535个字节，也就是说使用utf-8存汉字时，最大21845个字符

### MySQL中，如何对查询结果去重？

使用distinct去重：

```sql
-- 查询世界上所有国家码
SELECT countrycode FROM city; -- 返回结果有重复
SELECT DISTINCT(countrycode) FROM city;  -- DISTINCT 去重
```

### 如何查看SQL的执行计划？

使用explain命令，如：

```sql
explain select * from user;
```

### 简述MySQL的执行计划的作用及使用方法？

通过执行计划可以了解MySQL选择了什么执行计划来执行SQL，并且SQL的执行过程到此结束，即并不会真正的往下交给执行器去执行；最终的目的还是优化MySQL的性能。

参考：https://www.cnblogs.com/Neeo/articles/13644285.html

### 1000w条数据，使用limit offset 分页时，为什么越往后翻越慢？如何解决？

当一个数据库表过于庞大，LIMIT offset, length中的offset值过大，则SQL查询语句会非常缓慢，你需增加order by，并且order by字段需要建立索引。

如果使用子查询去优化LIMIT的话，则子查询必须是连续的，某种意义来讲，子查询不应该有where条件，where会过滤数据，使数据失去连续性。

如果你查询的记录比较大，并且数据传输量比较大，比如包含了text类型的field，则可以通过建立子查询。

```sql
SELECT id,title,content FROM items WHERE id IN (SELECT id FROM items ORDER BY id limit 900000, 10);
```

### 什么是索引合并？

索引合并是把几个索引的范围扫描合并成一个索引。

索引合并的时候，会对索引进行并集，交集或者先交集再并集操作，以便合并成一个索引。

这些需要合并的索引只能是一个表的。不能对多表进行索引合并。

在使用explain对sql语句进行操作时，如果使用了索引合并，那么在输出内容的type列会显示 index_merge，key列会显示出所有使用的索引

### 什么是覆盖索引？

覆盖索引又可以称为索引覆盖:查询辅助索引的时候不需要进行回表操作,即你查询的内容刚好是你的索引.

就是select的数据列只用从索引中就能够取得，不必从数据表中读取，换句话说查询列要被所使用的索引覆盖

### 简述数据库读写分离？

读写分离，基本的原理是让主数据库处理事务性增、改、删操作（INSERT、UPDATE、DELETE），而从数据库处理SELECT查询操作。数据库复制被用来把事务性操作导致的变更同步到集群中的从数据库。

用一句话概括，读写分离是用来解决数据库的读性能瓶颈的。

其实就是将数据库分为了主从库，一个主库用于写数据，多个从库完成读数据的操作，主从库之间通过某种机制进行数据的同步，是一种常见的数据库架构。



### 普通索引和唯一索引的区别(2021/3/19)

普通索引只有加速功能；而唯一索引还对索引列有唯一约束功能。

### 简述binlog中三种日志记录格式

首先对于DML语句，通过log_format参数来控制日志的记录格式：

\- SBR

\- RBR

\- MBR

请你简述SBR与RBR模式的对比(区别)？

statement：可读性高，日志量小，但不够严谨

row：可读性低，日志量大，但足够严谨

现在有如下语句，问：如果有500w行记录，row模式是真么记录日志的？

update t1 set name="a" where id>1000;

上面的update语句基于row模式是如何记录binlog呢，它会逐行记录变更操作，所以非常严谨，但也导致了日志量大。而如果是statement模式则只记录一个语句，虽然日志量小，但不够严谨。

你推荐使用什么模式？

推荐是用row模式。

### 如何复制一张已存在表，并且包含表中的记录？

答案：

```sql
-- 法1，t4表已存在，且有数据
CREATE TABLE t5 SELECT * FROM t4;

-- 法2
CREATE TABLE t6 LIKE t4;
INSERT INTO t6 SELECT * FROM t4;
```

更多关于复制表，参考：https://www.cnblogs.com/Neeo/articles/13531059.html#%E5%A4%8D%E5%88%B6%E8%A1%A8

### union和union all的区别？

union：对两个结果集进行并集操作，不包括重复行，也就是带有去重功能，同时进行默认规则的排序，另外，带有去重就意味着有性能上的消耗。
union All：对两个结果集进行并集操作，包括重复行，也就是不去重，同时也不进行排序；

### 写SQL

已知有三张表：

t1:

| name | kecheng | fenshu |
| ---- | ------- | ------ |
| 张三 | 语文    | 81     |
| 张三 | 数学    | 75     |
| 李四 | 语文    | 76     |
| 李四 | 数学    | 90     |
| 王五 | 语文    | 81     |
| 王五 | 数学    | 100    |
| 王五 | 英语    | 90     |

t2:

| name | xuexiao  |
| ---- | -------- |
| 张三 | 二十三中 |
| 李四 | 育人中学 |
| 王五 | 人大附中 |

t3：

| xuexiao  | quyu   |
| -------- | ------ |
| 二十三中 | 东城区 |
| 育人中学 | 朝阳区 |
| 人大附中 | 海淀区 |

问题：

```sql
-- 自行创建三张表及添加数据
-- 查询每门课程都大于80分的学生
-- 查询出"育人中学"数学成绩高于80分的同学姓名
-- 列出成绩满分(100分)同学的"区域、学校、姓名、课程、分数"
```

参考答案：

```sql
-- 自行创建三张表及添加数据
DROP TABLE IF EXISTS `t1`;
CREATE TABLE `t1` (
  `name` varchar(255) DEFAULT NULL,
  `kecheng` varchar(255) DEFAULT NULL,
  `fenshu` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `t1` VALUES ('张三', '语文', '81');
INSERT INTO `t1` VALUES ('张三', '数学', '75');
INSERT INTO `t1` VALUES ('李四', '语文', '76');
INSERT INTO `t1` VALUES ('李四', '数学', '90');
INSERT INTO `t1` VALUES ('王五', '语文', '81');
INSERT INTO `t1` VALUES ('王五', '数学', '100');
INSERT INTO `t1` VALUES ('王五', '英语', '90');

DROP TABLE IF EXISTS `t2`;
CREATE TABLE `t2` (
  `name` varchar(255) DEFAULT NULL,
  `xuexiao` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `t2` VALUES ('张三', '二十三中');
INSERT INTO `t2` VALUES ('李四', '育人中学');
INSERT INTO `t2` VALUES ('王五', '人大附中');

DROP TABLE IF EXISTS `t3`;
CREATE TABLE `t3` (
  `xuexiao` varchar(255) DEFAULT NULL,
  `quyu` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `t3` VALUES ('二十三中', '东城区');
INSERT INTO `t3` VALUES ('育人中学', '朝阳区');
INSERT INTO `t3` VALUES ('人大附中', '海淀区');

-- 查询每门课程都大于80分的学生
-- 法1
SELECT name, GROUP_CONCAT(kecheng), GROUP_CONCAT(fenshu)
FROM t1
GROUP BY name
HAVING MIN(fenshu) > 80;
+------+-----------------------+----------------------+
| name | GROUP_CONCAT(kecheng) | GROUP_CONCAT(fenshu) |
+------+-----------------------+----------------------+
| 王五 | 语文,数学,英语        | 81,100,90            |
+------+-----------------------+----------------------+
1 row in set (0.00 sec)
-- 法2
SELECT *
FROM t1 AS tmp
WHERE NOT EXISTS(
	SELECT kecheng FROM t1 WHERE fenshu < 80 AND name = tmp.name
);
+------+---------+--------+
| name | kecheng | fenshu |
+------+---------+--------+
| 王五 | 语文    |     81 |
| 王五 | 数学    |    100 |
| 王五 | 英语    |     90 |
+------+---------+--------+

-- 查询出"育人中学"数学成绩高于80分的同学姓名
SELECT t1.name
FROM t1 LEFT JOIN t2 ON t1.name=t2.name
WHERE t1.fenshu > 80 and kecheng = "数学" and t2.xuexiao = "育人中学";
+------+
| name |
+------+
| 李四 |
+------+
-- 列出成绩满分(100分)同学的"区域、学校、姓名、课程、分数"
SELECT t3.quyu, t3.xuexiao, t1.name, t1.kecheng, t1.fenshu
from t1 LEFT JOIN t2 ON t1.name=t2.name LEFT JOIN t3 ON t2.xuexiao=t3.xuexiao
WHERE t1.fenshu = 100;
+--------+----------+------+---------+--------+
| quyu   | xuexiao  | name | kecheng | fenshu |
+--------+----------+------+---------+--------+
| 海淀区 | 人大附中 | 王五 | 数学    |    100 |
+--------+----------+------+---------+--------+
```







### 写SQL

已知信息表emp，部门表dept，工资表sal三张表。

emp：

| eid  | ename | bdate     | sex  | city |
| :--- | ----- | --------- | ---- | ---- |
| S001 | 张三  | 1970/6/1  | F    | 上海 |
| A001 | 李四  | 1990/6/1  | M    | 昆山 |
| P001 | 王五  | 1950/6/1  | M    | 苏州 |
| A002 | 赵六  | 1990/2/23 | M    | 上海 |
| P002 | 孙七  | 1999/2/23 | F    | 镇江 |
| S002 | 秦八  | 1980/5/27 | M    | 上海 |
| A003 | 赵九  | 1981/5/27 | M    | 苏州 |

dept：

| did  | dname  | dcity |
| ---- | ------ | ----- |
| D01  | 研发部 | 上海  |
| D02  | 技术部 | 上海  |
| D03  | 广告部 | 上海  |

sal：

| eid  | did  | startdate | salary |
| ---- | ---- | --------- | ------ |
| S001 | D03  | 1990/1/1  | 4040   |
| A001 | D01  | 2010/1/1  | 3000   |
| P001 | D02  | 2003/1/1  | 3500   |
| A002 | D01  | 2001/9/1  | 1900   |
| P002 | D02  | 2004/9/1  | 3100   |
| S002 | D03  | 2000/9/1  | 5100   |
| A003 | D03  | 2001/9/1  | 1100   |

```sql
-- 查询"研发" 部门的员工的所有基本信息
-- 列出员工编号以字母P或者S开头的所有员工信息，包括所在部门和薪资
-- 查询每个部门的人数
-- 查询每个部门的最高工资和最低工资
-- 查询部门人数大于等于3的每个部门的最高工资、最低工资
```

答案参考：

```sql
create table emp(
eid varchar(32),
ename varchar(32),
bdate date,
sex varchar(8),
city varchar(32)
) engine=innodb charset=utf8;

insert into emp values
('S001', '张三', '1970/6/1', 'F', '上海'),
('A001', '李四', '1990/6/1', 'M', '昆山'),
('P001', '王五', '1950/6/1', 'M', '苏州'),
('A002', '赵六', '1990/2/23', 'M', '上海'),
('P002', '孙七', '1999/2/23', 'F', '镇江'),
('S002', '秦八', '1980/5/27', 'M', '上海'),
('A003', '赵九', '1981/5/27', 'M', '苏州');


create table dept(
did varchar(32),
dname varchar(32),
dcity varchar(32)
) engine=innodb charset=utf8;


insert into dept values
('D01', '研发部', '上海'),
('D02', '技术部', '上海'),
('D03', '广告部', '上海');



create table sal(
eid varchar(32),
did varchar(32),
startdate date,
salary int
) engine=innodb charset=utf8;

insert into sal values
('S001', 'D03', '1990/1/1', 4040),
('A001', 'D01', '2010/1/1', 3000),
('P001', 'D02', '2003/1/1', 3500),
('A002', 'D01', '2001/9/1', 1900),
('P002', 'D02', '2004/9/1', 3100),
('S002', 'D03', '2000/9/1', 5100),
('A003', 'D03', '2001/9/1', 1100);


-- 查询"研发" 部门的员工的所有基本信息
SELECT
  *
FROM emp LEFT JOIN sal ON emp.eid=sal.eid LEFT JOIN dept ON sal.did=dept.did
WHERE dept.dname="研发部";
+------+-------+------------+------+------+------+------+------------+--------+------+--------+-------+
| eid  | ename | bdate      | sex  | city | eid  | did  | startdate  | salary | did  | dname  | dcity |
+------+-------+------------+------+------+------+------+------------+--------+------+--------+-------+
| A001 | 李四  | 1990-06-01 | M    | 昆山 | A001 | D01  | 2010-01-01 |   3000 | D01  | 研发部 | 上海  |
| A002 | 赵六  | 1990-02-23 | M    | 上海 | A002 | D01  | 2001-09-01 |   1900 | D01  | 研发部 | 上海  |
+------+-------+------------+------+------+------+------+------------+--------+------+--------+-------+

-- 列出员工编号以字母P或者S开头的所有员工信息，包括所在部门和薪资
SELECT 
  emp.eid,
  emp.ename,
  emp.bdate,
  emp.sex,
  emp.city,
  sal.salary,
  dept.dname
FROM emp LEFT JOIN sal ON emp.eid=sal.eid LEFT JOIN dept ON sal.did=dept.did
where emp.eid like "P%" or emp.eid like "S%";
+------+-------+------------+------+------+--------+--------+
| eid  | ename | bdate      | sex  | city | salary | dname  |
+------+-------+------------+------+------+--------+--------+
| P001 | 王五  | 1950-06-01 | M    | 苏州 |   3500 | 技术部 |
| P002 | 孙七  | 1999-02-23 | F    | 镇江 |   3100 | 技术部 |
| S001 | 张三  | 1970-06-01 | F    | 上海 |   4040 | 广告部 |
| S002 | 秦八  | 1980-05-27 | M    | 上海 |   5100 | 广告部 |
+------+-------+------------+------+------+--------+--------+


-- 查询每个部门的人数
select 
  dept.dname,
  count(dept.dname)
from dept INNER JOIN sal on dept.did=sal.did 
GROUP BY dept.dname;
+--------+-------------------+
| dname  | count(dept.dname) |
+--------+-------------------+
| 广告部 |                 3 |
| 技术部 |                 2 |
| 研发部 |                 2 |
+--------+-------------------+

-- 查询每个部门的最高工资和最低工资
SELECT 
  dept.dname,
  min(sal.salary),
  max(sal.salary)
FROM dept INNER JOIN sal ON dept.did=sal.did 
GROUP BY dept.dname;
+--------+-----------------+-----------------+
| dname  | min(sal.salary) | max(sal.salary) |
+--------+-----------------+-----------------+
| 广告部 |            1100 |            5100 |
| 技术部 |            3100 |            3500 |
| 研发部 |            1900 |            3000 |
+--------+-----------------+-----------------+


-- 查询部门人数大于等于3的每个部门的最高工资、最低工资
-- 法1
SELECT 
  dept.dname,
  min(sal.salary),
  max(sal.salary)
FROM dept INNER JOIN sal ON dept.did=sal.did 
GROUP BY dept.dname 
HAVING count(dept.dname) >= 3;
+--------+-----------------+-----------------+
| dname  | min(sal.salary) | max(sal.salary) |
+--------+-----------------+-----------------+
| 广告部 |            1100 |            5100 |
+--------+-----------------+-----------------+

-- 法2
select sal.did,min(salary), max(salary) from sal group by did having count(did) >= 3;
+------+-------------+-------------+
| did  | min(salary) | max(salary) |
+------+-------------+-------------+
| D03  |        1100 |        5100 |
+------+-------------+-------------+
```



### 写SQL

**写出每个人三科成绩的平均分**

### 写SQL

写查询语句

```sql
User table
id  	自增id
name	姓名
gender	性别

Pet	table
id			自增id
name 		昵称
category	种类
user_id		用户id
```

写SQL：

-   找出每个用户的宠物数量。

    ```sql
    select 
    	user.name, 
    	count(pet.user_id) as "宠物数量"
    from user LEFT JOIN pet on user.id = pet.user_id
    GROUP BY pet.user_id;
    ```

-   找到哪种宠物拥有的人最多。

    ```sql
    select category, count(category) from pet GROUP BY category desc;
    ```

    

### 写SQL

一共有语数英三门课程，用一条SQL语句，查询出每门课都大于70 分的学生姓名 name subject score(2021/4/9)

这个主要表结构是怎么设计的，学生表和分数表两张表？还是学生一张表就存完了？

下面参考示例是分为学生表和分数表两张表：

```sql
DROP TABLE IF EXISTS `score`;
CREATE TABLE `score` (
  `id` int(11) NOT NULL,
  `yu` float NOT NULL,
  `shu` float NOT NULL,
  `ying` float(255,0) NOT NULL,
  `stu_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `stu_id` (`stu_id`),
  CONSTRAINT `stu_id` FOREIGN KEY (`stu_id`) REFERENCES `student` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `score` VALUES ('1', '36', '88', '76', '1');
INSERT INTO `score` VALUES ('2', '88', '89', '98', '2');
INSERT INTO `score` VALUES ('3', '44', '55', '66', '3');
INSERT INTO `score` VALUES ('4', '99', '89', '82', '4');
INSERT INTO `score` VALUES ('5', '83', '60', '42', '5');

DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int(11) NOT NULL,
  `name` char(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `student` VALUES ('1', 'zhang3');
INSERT INTO `student` VALUES ('2', 'li4');
INSERT INTO `student` VALUES ('3', 'wang5');
INSERT INTO `student` VALUES ('4', 'zhao6');
INSERT INTO `student` VALUES ('5', 'zhu7');
```

查询语句参考，先联表，再查询：

```sql
select student.name, score.yu, score.shu, score.ying
from student LEFT JOIN score on student.id = score.stu_id
where score.shu > 70 and score.yu > 70 and score.ying > 70;
```







### 写SQL

**一张表scores包含字段，name,subject,score,分别记录不同学生的名字，科目，分数。请用sql统计每个科目及格(score >60分)的人数(2021/3/4)**



**一张表scores包含字段，name,subject,score,分别记录不同学生的名字，科目，分数。统计出及格(score >60分)人数大于20的科目，并且按照人数降序排序(2021/3/4)**

**一张表scores字段有subjectid,score, 表示科目ID，分数，另外一张表sujects记录了subjectid(科目ID)，subject（科目名称）。查询分数倒序第11到20对应的科目名(2021/3/4)**

### 索引操作

针对sql语句：SELECT * FROM obs_cost WHERE yearMonth = '201901' and id>100 GROUP BY yearMonth,productId, platformName 加上你认为最合适的索引(2021/3/4)





### 简要说说MySQL中的主从复制(2020/11/29)









### 简述数据库分库分表？（水平、垂直）

数据库分表：

把一张表按照一定的规则分解成不同的实体表。比如垂直划分和水平划分 垂直切分：把不同功能，不同模块的数据分别放到不同的表中，但是如果同一个模块的数据量太大就会存在性能瓶颈水平切分：垂直切分解决不了大表的瓶颈，如果同一个功能中表的数据量过大，就要对该表进行切分，为水平切分

通俗理解：垂直切分---分不同的模块表；水平切分---分同一个模块下的多个表

分库 将一堆数据放到不同的数据库中保存，上面说的都是在同一个数据库上，分库是分到不同的数据库上

垂直分表:经常查的字段放在一个表里

 

 

### 数据库锁的作用？

行级锁，表级锁。

一般是乐观锁,只有在修改的时候才加锁

数据库是一个多用户使用的共享资源。当多个用户并发地存取数据时，在数据库中就会产生多个事务同时存取同一数据的情况。若对并发操作不加控制就可能会读取和存储不正确的数据，破坏数据库的一致性。（类似于多线程并发的情况）

加锁是实现数据库[并发控制]的一个非常重要的技术。当事务在对某个数据对象进行操作前，先向系统发出请求，对其加锁。加锁后事务就对该数据对象有了一定的控制，在该事务释放锁之前，其他的事务不能对此数据对象进行更新操作。在数据库中有两种基本的锁类型：排它锁（Exclusive Locks，即X锁）和共享锁（Share Locks，即S锁）。当数据对象被加上排它锁时，其他的事务不能对它读取和修改。加了共享锁的数据对象可以被其他事务读取，但不能修改。数据库利用这两种基本的锁类型来对数据库的事务进行并发控制

 

### 请简述项目中优化sql语句执行效率的方法

连表查询代替子查询

尽量在where过滤

创建有效正确的索引

优化查询过程中的数据访问：

\- 访问数据太多导致性能下降

\- 不要使用select * 语句，因为select * 取出全部列，而且select * 会让优化器无法完成索引覆盖扫描的优化。

\- 确定应用程序是否在检索大量超过需要的数据，可能是太多行或列

### 叙述mysql半同步复制原理

主库在执行完客户端提交的事物后，不会立即返回给客户端,而是等至少一个从库接收并写到relaylog之后才返回客户端。

默认情况下，MySQL的复制功能是异步的，异步复制可以提供最佳的性能， 主库把binlog日志发送给从库，这一动作就结束了，并不会验证从库是否接收完毕，这一过程，也就意味着有可能出现当主服务器或从服务器端发生故障的时候，有可能从服务器没有接收到主服务器发送过来的binlog日志，这就会造成主服务器和从服务器的数据不一致，甚至在恢复时造成数据的丢失。

注意：半同步复制模式必须在主服务器和从服务器端同时开启，否则主服务器默认使用异步复制模式。

为了解决上述可能发生的错误，MySQL 5.5 引入了一种半同步复制模式。该模式可以确保从服务器接收完主服务器发送的binlog日志文件并写入到自己的中继日志relay log里，然后会给主服务器一个反馈，告诉主服务器已经接收完毕，这时主服务线程才返回给当前session告知操作完成。

当出现超时情况是，主服务器会暂时切换到异步复制模式，直到至少有一个从服务器从及时收到信息为止。

 

### mysql中怎么创建索引？

在执行CREATE TABLE语句时可以创建索引，也可以单独用CREATE INDEX或ALTER TABLE来为表增加索引。

1.  使用ALTER TABLE用来创建普通索引、UNIQUE索引或PRIMARY KEY索引。

    ```sql
    ALTER TABLE table_name ADD INDEX index_name (column_list);
    ```

2.  使用create index对表增加普通索引或UNIQUE索引。

    ```python
    CREATE INDEX index_name ON table_name (column_list);
    ```



 

### 请简述sql注入的攻击原理及如何在代码层面防止sql注入？

通过把sql命令插入到web表单递交或输入域名或页面请求的查询字符串，最终达到欺骗服务器执行恶意的sql命令。

1、对用户的输入进行校验，可以通过正则表达式，或限制长度，对单引号和双引号进行转换等。

2、不要使用动态拼装sql，可以使用参数化的sql或者直接使用存储过程进行数据查询存取。

3、不要使用管理员权限的数据库连接，为每个应用使用单独的权限有限的数据库连接。

4、不要把机密信息明文存放，一定要加密或者hash掉密码和敏感信息。

5、应用异常信息应该给出尽可能少的提示，最好使用自定义的错误信息对原始错误信息进行包装，把异常信息存放在独立的表中。

 

### 使用Python实现将数据库的student表中提取的数据写入db.txt？

在Python3中，使用pymysql进行连接数据库，

### 简述left join和right join的区别？

都是多表连接查询中的外连接方式

区别是：left join是左连接，优先显示左边中的全部记录

right join是右连接，优先显示右表中的全部记录

### 索引有什么作用,有那些分类, 有什么好处和坏处？

作用：加快查询，拖慢删除/添加的速度

分类：聚集索引：辅助索引

聚集索引：

\- 每张表只能有一个聚集索引

\- 叶子节点直接对应数据，所以找到索引就是找到数据

\- 数据的存储物理地址是按照索引顺序来存的，所以按照聚集索引列排序非常快

辅助索引(非聚集索引)：

\- 每张表可以有多个辅助索引，查询速度快，但占用更多磁盘空间，影响删除和添加的效率

\- 叶子节点不直接存放数据，而是存放数据的地址，所以找到叶子节点后还需再做一次IO操作

\- 数据的物理地址和索引顺序无关.

为了加快查询速度根据二分法速度快的原理，产生可平衡二叉树，但是b树高度高，查询次数多，就增加了分叉，形成了b-树：

l b-树：会把数据行存储在中间节点中，所以导致节点中能存储的数据太少

l b+树：中间节点不存放数据.innodb，myisam都是基于b+树创建索引

什么决定树的高度?数据的量和数据的长度。

什么是索引? 把数据的某个字段按照特殊的算法计算成一个树型结构，再根据树型结构提供的指针缩小范围，找到对应的磁盘块.通过这棵树，可以将我们每次的查询范围缩小1/3，加快了我们的查询速度，这棵树就是索引。

 

### 什么是MySQL慢日志？

MySQL的慢查询日志是MySQL提供的一种日志记录，它用来记录在MySQL中响应时间超过阀值的语句，具体指运行时间超过long_query_time值的SQL，则会被记录到慢查询日志中。long_query_time的默认值为10，意思是运行10S以上的语句。默认情况下，Mysql数据库并不启动慢查询日志，需要我们手动来设置这个参数，当然，如果不是调优需要的话，一般不建议启动该参数，因为开启慢查询日志会或多或少带来一定的性能影响。慢查询日志支持将日志记录写入文件，也支持将日志记录写入数据库表。

参考：https://www.cnblogs.com/Neeo/articles/14006790.html

### 在对name做了唯一索引前提下，简述以下区别

select * from tb where name = "zhangkai"

select * from tb where name = "zhangkai" limit 1

如果是唯一索引的话两者本质上没有什么区别，都是查询到一条数据后就不往下查询了，但是如果不是唯一索引的前提下，第二种加limit的当查询到一条数据后就不往下执行了，而第一种还是需要继续查询

### 存储过程和函数的区别?

存储过程与函数的区别：

-   存储过程可以有多个in,out,inout参数，而函数只有输入参数类型，而且不能带in.

-   存储过程实现的功能要复杂一些；而函数的单一功能性（针对性）更强。

-   存储过程可以返回多个值；存储函数只能有一个返回值。

-   存储过程一般独立的来执行；而存储函数可以作为其它sql语句的组成部分来出现。

-   存储过程可以调用存储函数。函数不能调用存储过程。



