# day41作业（张珵）

# 原始数据

```mysql
mysql> show tables;
+--------------------+
| Tables_in_homework |
+--------------------+
| class              |
| course             |
| score              |
| student            |
| teacher            |
+--------------------+
5 rows in set (0.00 sec)

mysql> select * from class;
+-----+--------------+
| cid | caption      |
+-----+--------------+
|   1 | 三年二班     |
|   2 | 三年三班     |
|   3 | 一年二班     |
|   4 | 二年九班     |
+-----+--------------+
4 rows in set (0.00 sec)

mysql> select * from course;
+-----+--------+------------+
| cid | cname  | teacher_id |
+-----+--------+------------+
|   1 | 生物   |          1 |
|   2 | 物理   |          2 |
|   3 | 体育   |          3 |
|   4 | 美术   |          2 |
+-----+--------+------------+
4 rows in set (0.01 sec)

mysql> select * from score;
+-----+------------+-----------+-----+
| sid | student_id | course_id | num |
+-----+------------+-----------+-----+
|   1 |          1 |         1 |  10 |
|   2 |          1 |         2 |   9 |
|   5 |          1 |         4 |  66 |
|   6 |          2 |         1 |   8 |
|   8 |          2 |         3 |  68 |
|   9 |          2 |         4 |  99 |
|  10 |          3 |         1 |  77 |
|  11 |          3 |         2 |  66 |
|  12 |          3 |         3 |  87 |
|  13 |          3 |         4 |  99 |
|  14 |          4 |         1 |  79 |
|  15 |          4 |         2 |  11 |
|  16 |          4 |         3 |  67 |
|  17 |          4 |         4 | 100 |
|  18 |          5 |         1 |  79 |
|  19 |          5 |         2 |  11 |
|  20 |          5 |         3 |  67 |
|  21 |          5 |         4 | 100 |
|  22 |          6 |         1 |   9 |
|  23 |          6 |         2 | 100 |
|  24 |          6 |         3 |  67 |
|  25 |          6 |         4 | 100 |
|  26 |          7 |         1 |   9 |
|  27 |          7 |         2 | 100 |
|  28 |          7 |         3 |  67 |
|  29 |          7 |         4 |  88 |
|  30 |          8 |         1 |   9 |
|  31 |          8 |         2 | 100 |
|  32 |          8 |         3 |  67 |
|  33 |          8 |         4 |  88 |
|  34 |          9 |         1 |  91 |
|  35 |          9 |         2 |  88 |
|  36 |          9 |         3 |  67 |
|  37 |          9 |         4 |  22 |
|  38 |         10 |         1 |  90 |
|  39 |         10 |         2 |  77 |
|  40 |         10 |         3 |  43 |
|  41 |         10 |         4 |  87 |
|  42 |         11 |         1 |  90 |
|  43 |         11 |         2 |  77 |
|  44 |         11 |         3 |  43 |
|  45 |         11 |         4 |  87 |
|  46 |         12 |         1 |  90 |
|  47 |         12 |         2 |  77 |
|  48 |         12 |         3 |  43 |
|  49 |         12 |         4 |  87 |
|  52 |         13 |         3 |  87 |
+-----+------------+-----------+-----+
47 rows in set (0.00 sec)

mysql> select * from student;
+-----+--------+----------+--------+
| sid | gender | class_id | sname  |
+-----+--------+----------+--------+
|   1 | 男     |        1 | 理解   |
|   2 | 女     |        1 | 钢蛋   |
|   3 | 男     |        1 | 张三   |
|   4 | 男     |        1 | 张一   |
|   5 | 女     |        1 | 张二   |
|   6 | 男     |        1 | 张四   |
|   7 | 女     |        2 | 铁锤   |
|   8 | 男     |        2 | 李三   |
|   9 | 男     |        2 | 李一   |
|  10 | 女     |        2 | 李二   |
|  11 | 男     |        2 | 李四   |
|  12 | 女     |        3 | 如花   |
|  13 | 男     |        3 | 刘三   |
|  14 | 男     |        3 | 刘一   |
|  15 | 女     |        3 | 刘二   |
|  16 | 男     |        3 | 刘四   |
+-----+--------+----------+--------+
16 rows in set (0.00 sec)

mysql> select * from teacher;
+-----+-----------------+
| tid | tname           |
+-----+-----------------+
|   1 | 张磊老师        |
|   2 | 李平老师        |
|   3 | 刘海燕老师      |
|   4 | 朱云海老师      |
|   5 | 李杰老师        |
+-----+-----------------+
5 rows in set (0.00 sec)
```

1、查询没有学全所有课的同学的学号、姓名；

```mysql
# 课程总门数
select count(*) from course;
+----------+
| count(*) |
+----------+
|        4 |
+----------+
1 row in set (0.08 sec)

# 学全所有课的同学学号
select student_id from score group by student_id having count(*) = (select count(*) from course);
+------------+
| student_id |
+------------+
|          3 |
|          4 |
|          5 |
|          6 |
|          7 |
|          8 |
|          9 |
|         10 |
|         11 |
|         12 |
+------------+
10 rows in set (0.00 sec)

# 没有学全所有课的同学的学号
select sid, sname from student where sid not in (
    select student_id from score group by student_id having count(*) = (
        select count(*) from course
    )
);
+-----+--------+
| sid | sname  |
+-----+--------+
|   1 | 理解   |
|   2 | 钢蛋   |
|  13 | 刘三   |
|  14 | 刘一   |
|  15 | 刘二   |
|  16 | 刘四   |
+-----+--------+
6 rows in set (0.00 sec)
```

2、查询和“002”号的同学学习的课程完全相同的其他同学学号和姓名；

**【更改为：查询和“003”号的同学学习的课程完全相同的其他同学学号和姓名】**

**方法一：老师**（简单）

```mysql
# 先查询2号同学学了哪些课程
select * from score where student_id =2;
+-----+------------+-----------+-----+
| sid | student_id | course_id | num |
+-----+------------+-----------+-----+
|   6 |          2 |         1 |   8 |
|   8 |          2 |         3 |  68 |
|   9 |          2 |         4 |  99 |
+-----+------------+-----------+-----+
3 rows in set (0.00 sec)

# 找到学习了2号同学没学习课程的所有同学（找到所有和2号同学学习的课程不一样的同学）
select student_id from score where course_id not in (select course_id from score where student_id=2)
+------------+
| student_id |
+------------+
|          1 |
|          3 |
|          4 |
|          5 |
|          6 |
|          7 |
|          8 |
|          9 |
|         10 |
|         11 |
|         12 |
+------------+
11 rows in set (0.00 sec)

# 找到score表中所有的学生并且把 2号同学 以及（和2号同学学习的课程不一样的同学）排除出去
select student_id from score where student_id not in (select student_id from score where course_id not in (select course_id from score where student_id=2)) and student_id !=2

# 对剩余的和2号同学所选课程没有不同的同学所选课程数进行统计，如果和2号同学的课程数相同，就是选择了相同的课程
select student_id from score where student_id not in (select student_id from score where course_id not in (select course_id from score where student_id=2)) and student_id !=2
group by student_id having count(course_id)= (select count(course_id) from score where student_id=2);
```

**方法二：张珵**（复杂）

```mysql
# （1）“003”号的同学学习的课程编号
select course_id from score where student_id = 3;
+-----------+
| course_id |
+-----------+
|         1 |
|         3 |
|         4 |
+-----------+
3 rows in set (0.00 sec)

# （2）“003”号的同学学习的课程门数
select count(*) from score where student_id = 3;
+----------+
| count(*) |
+----------+
|        4 |
+----------+
1 row in set (0.00 sec)

# （3）找出学习课程门数与3号同学学习课程门数相同的人，用于剔除学习课程门数与3号同学学习课程门数不等的人，结果命名为t3
select student_id from score where student_id != 3 group by student_id having count(*) = (select count(*) from score where student_id = 3);
+------------+
| student_id |
+------------+
|          4 |
|          5 |
|          6 |
|          7 |
|          8 |
|          9 |
|         10 |
|         11 |
|         12 |
+------------+
9 rows in set (0.00 sec)

# （4）筛选出course_id in （1）结果的行，然后找出学习课程门数与3号同学学习课程门数相同的人，用于找出学习了3号同学学习的全部课程的人（可能跟3号同学学的相同，也可能比3号同学学的多），结果命名为t4
select student_id from score where student_id != 3 and course_id in (select course_id from score where student_id = 3) group by student_id having count(*) = (select count(*) from score where student_id = 3);
+------------+
| student_id |
+------------+
|          3 |
|          4 |
|          5 |
|          6 |
|          7 |
|          8 |
|          9 |
|         10 |
|         11 |
|         12 |
+------------+
10 rows in set (0.00 sec)

# （5）将（3）结果与（4）结果取交集，结果命名为t5
select t3.student_id from (
    select student_id from score where student_id != 3 group by student_id having count(*) = (select count(*) from score where student_id = 3)
    ) as t3 inner join (
    select student_id from score where student_id != 3 and course_id in (select course_id from score where student_id = 3) group by student_id having count(*) = (select count(*) from score where student_id = 3)
    ) as t4 on t3.student_id = t4.student_id

# （6）将（5）的结果加上学生姓名
select student_id, sname from(
    select t3.student_id from (
        select student_id from score where student_id != 3 group by student_id having count(*) = (select count(*) from score where student_id = 3)
        ) as t3 inner join (
        select student_id from score where student_id != 3 and course_id in (select course_id from score where student_id = 3) group by student_id having count(*) = (select count(*) from score where student_id = 3)
        ) as t4 on t3.student_id = t4.student_id
    ) as t5 left join student on student_id = sid;

+------------+--------+
| student_id | sname  |
+------------+--------+
|          4 | 张一   |
|          5 | 张二   |
|          6 | 张四   |
|          7 | 铁锤   |
|          8 | 李三   |
|          9 | 李一   |
|         10 | 李二   |
|         11 | 李四   |
|         12 | 如花   |
+------------+--------+
9 rows in set (0.00 sec)
```

**方法二：老师**



3、删除学习“叶平”老师课的SC表记录；

**【更改为】删除学习“李平老师”课的SC表记录；**

```mysql
# 李平老师教课列表
select cid from course inner join teacher on teacher_id = tid where tname='李平老师';

# 删除学习“李平”老师课的SC表记录
delete from score where class_id in (select cid from course inner join teacher on teacher_id = tid where tname='李平老师');
```

4、向SC表中插入一些记录，这些记录要求符合以下条件：①没有上过编号“002”课程的同学学号；②插入“002”号课程的平均成绩； 

```mysql
#“002”号课程的平均成绩
select avg(num) from score where course_id = 2;
+---------+
| avg_num |
+---------+
| 65.0909 |
+---------+
1 row in set (0.00 sec)

# 上过编号“002”课程的同学学号
select student_id from score where course_id = 2;
+------------+
| student_id |
+------------+
|          1 |
|          3 |
|          4 |
|          5 |
|          6 |
|          7 |
|          8 |
|          9 |
|         10 |
|         11 |
|         12 |
+------------+
11 rows in set (0.00 sec)

# 没上过编号“002”课程的同学学号
select sid from student where sid not in (select student_id from score where course_id = 2);
+-----+
| sid |
+-----+
|   2 |
|  13 |
|  14 |
|  15 |
|  16 |
+-----+

# 拼出要添加的表格
select sid, 2, (select avg(num) from score where course_id = 2) as avg_num from student where sid not in (select student_id from score where course_id = 2);
+-----+---+---------+
| sid | 2 | avg_num |
+-----+---+---------+
|   2 | 2 | 65.0909 |
|  13 | 2 | 65.0909 |
|  14 | 2 | 65.0909 |
|  15 | 2 | 65.0909 |
|  16 | 2 | 65.0909 |
+-----+---+---------+
5 rows in set (0.00 sec)

insert into score(student_id,course_id,num) select sid, 2, (select avg(num) from score where course_id = 2) as avg_num from student where sid not in (select student_id from score where course_id = 2);
Query OK, 5 rows affected (0.07 sec)
Records: 5  Duplicates: 0  Warnings: 0

select * from score;
+-----+------------+-----------+-----+
| sid | student_id | course_id | num |
+-----+------------+-----------+-----+
|   1 |          1 |         1 |  10 |
|   2 |          1 |         2 |   9 |
|   5 |          1 |         4 |  66 |
|   6 |          2 |         1 |   8 |
|   8 |          2 |         3 |  68 |
|   9 |          2 |         4 |  99 |
|  10 |          3 |         1 |  77 |
|  11 |          3 |         2 |  66 |
|  12 |          3 |         3 |  87 |
|  13 |          3 |         4 |  99 |
|  14 |          4 |         1 |  79 |
|  15 |          4 |         2 |  11 |
|  16 |          4 |         3 |  67 |
|  17 |          4 |         4 | 100 |
|  18 |          5 |         1 |  79 |
|  19 |          5 |         2 |  11 |
|  20 |          5 |         3 |  67 |
|  21 |          5 |         4 | 100 |
|  22 |          6 |         1 |   9 |
|  23 |          6 |         2 | 100 |
|  24 |          6 |         3 |  67 |
|  25 |          6 |         4 | 100 |
|  26 |          7 |         1 |   9 |
|  27 |          7 |         2 | 100 |
|  28 |          7 |         3 |  67 |
|  29 |          7 |         4 |  88 |
|  30 |          8 |         1 |   9 |
|  31 |          8 |         2 | 100 |
|  32 |          8 |         3 |  67 |
|  33 |          8 |         4 |  88 |
|  34 |          9 |         1 |  91 |
|  35 |          9 |         2 |  88 |
|  36 |          9 |         3 |  67 |
|  37 |          9 |         4 |  22 |
|  38 |         10 |         1 |  90 |
|  39 |         10 |         2 |  77 |
|  40 |         10 |         3 |  43 |
|  41 |         10 |         4 |  87 |
|  42 |         11 |         1 |  90 |
|  43 |         11 |         2 |  77 |
|  44 |         11 |         3 |  43 |
|  45 |         11 |         4 |  87 |
|  46 |         12 |         1 |  90 |
|  47 |         12 |         2 |  77 |
|  48 |         12 |         3 |  43 |
|  49 |         12 |         4 |  87 |
|  52 |         13 |         3 |  87 |
|  53 |          2 |         2 |  65 |
|  54 |         13 |         2 |  65 |
|  55 |         14 |         2 |  65 |
|  56 |         15 |         2 |  65 |
|  57 |         16 |         2 |  65 |
+-----+------------+-----------+-----+
52 rows in set (0.00 sec)
```

5、按平均成绩从低到高显示所有学生的“语文”、“数学”、“英语”三门的课程成绩，按如下形式显示： 学生ID,语文,数学,英语,有效课程数,有效平均分；

**【更改为】按平均成绩从低到高显示所有学生的“生物”、“物理”、“体育”、"美术"四门的课程成绩，按如下形式显示： 学生ID,生物,物理,体育,美术,有效课程数,有效平均分；**

**方法一：老师（简单）**

```mysql
# 查看每个学生的数学成绩

select student_id,num from score where course_id = (select cid from course where cname = '数学');

#  查看每个学生的语文成绩

select student_id,num from score where course_id = (select cid from course where cname = '语文');

#  查看每个学生的英语成绩

select student_id,num from score where course_id = (select cid from course where cname = '英语');

# 查看每个学生的平均成绩、课程数

select student_id,avg(num),count(num) from score group by student_id;

# 将上面的几张表拼接起来,为了生成所有学生的信息，用student表作为左连接的第一张表

select sid 学生ID,t2.num 语文,t1.num 数学, t3.num 英语,t4.count_course 有效课程数,t4.avg_num 有效平均分 from student 

 left join (select student_id,num from score where course_id = (select cid from course where cname = '数学')) t1

 on student.sid = t1.student_id

 left join (select student_id,num from score where course_id = (select cid from course where cname = '语文')) t2

 on student.sid = t2.student_id

 left join (select student_id,num from score where course_id = (select cid from course where cname = '英语')) t3

 on student.sid = t3.student_id

 left join (select student_id,avg(num) avg_num,count(num) count_course from score group by student_id)  t4

 on student.sid = t4.student_id
```

**方法二：张珵（复杂）**

```mysql
# （1）构造每个学生的有效课程数、有效平均分表t
select student_id, count(*) ,avg(num) from score group by student_id;
+------------+----------+----------+
| student_id | count(*) | avg(num) |
+------------+----------+----------+
|          1 |        3 |  28.3333 |
|          2 |        3 |  58.3333 |
|          3 |        4 |  82.2500 |
|          4 |        4 |  64.2500 |
|          5 |        4 |  64.2500 |
|          6 |        4 |  69.0000 |
|          7 |        4 |  66.0000 |
|          8 |        4 |  66.0000 |
|          9 |        4 |  67.0000 |
|         10 |        4 |  74.2500 |
|         11 |        4 |  74.2500 |
|         12 |        4 |  74.2500 |
|         13 |        1 |  87.0000 |
+------------+----------+----------+
13 rows in set (0.00 sec)

# （2）构造生物表t1、物理表t2、体育表t3、美术表t4
# t1_inner、t2_inner、t3_inner、t4_inner：Every derived table must have its own alias
select sid, num from student left join (select student_id, num from score inner join course on cid = course_id where cname='生物') as t1_inner on sid = student_id;
+-----+------+
| sid | num  |
+-----+------+
|   1 |   10 |
|   2 |    8 |
|   3 |   77 |
|   4 |   79 |
|   5 |   79 |
|   6 |    9 |
|   7 |    9 |
|   8 |    9 |
|   9 |   91 |
|  10 |   90 |
|  11 |   90 |
|  12 |   90 |
|  13 | NULL |
|  14 | NULL |
|  15 | NULL |
|  16 | NULL |
+-----+------+
16 rows in set (0.10 sec)

select sid, num from student left join (select student_id, num from score inner join course on cid = course_id where cname='物理') as t2_inner on sid = student_id;
结果略
select sid, num from student left join (select student_id, num from score inner join course on cid = course_id where cname='体育') as t3_inner on sid = student_id;
结果略
select sid, num from student left join (select student_id, num from score inner join course on cid = course_id where cname='美术') as t4_inner on sid = student_id;
结果略

# （3）构造t1、t2、t3、t4的笛卡尔积，筛选sid相同的行，将结果表命名为t1234
select t1.sid as '学生ID', t1.num as '生物',  t2.num as '物理', t3.num as '体育', t4.num as '美术' from (select sid, num from student left join (select student_id, num from score inner join course on cid = course_id where cname='生物') as t1_inner on sid = student_id) as t1, (select sid, num from student left join (select student_id, num from score inner join course on cid = course_id where cname='物理') as t2_inner on sid = student_id) as t2, 
(select sid, num from student left join (select student_id, num from score inner join course on cid = course_id where cname='体育') as t3_inner on sid = student_id) as t3, 
(select sid, num from student left join (select student_id, num from score inner join course on cid = course_id where cname='美术') as t4_inner on sid = student_id) as t4 where t1.sid=t2.sid and t2.sid=t3.sid and t3.sid=t4.sid;
+----------+--------+--------+--------+--------+
| 学生ID   | 生物   | 物理   | 体育   | 美术   |
+----------+--------+--------+--------+--------+
|        1 |     10 |      9 |   NULL |     66 |
|        2 |      8 |   NULL |     68 |     99 |
|        3 |     77 |     66 |     87 |     99 |
|        4 |     79 |     11 |     67 |    100 |
|        5 |     79 |     11 |     67 |    100 |
|        6 |      9 |    100 |     67 |    100 |
|        7 |      9 |    100 |     67 |     88 |
|        8 |      9 |    100 |     67 |     88 |
|        9 |     91 |     88 |     67 |     22 |
|       10 |     90 |     77 |     43 |     87 |
|       11 |     90 |     77 |     43 |     87 |
|       12 |     90 |     77 |     43 |     87 |
|       13 |   NULL |   NULL |     87 |   NULL |
|       14 |   NULL |   NULL |   NULL |   NULL |
|       15 |   NULL |   NULL |   NULL |   NULL |
|       16 |   NULL |   NULL |   NULL |   NULL |
+----------+--------+--------+--------+--------+
16 rows in set (0.00 sec)

# （4）t1234 和 t 进行连表，并按每个学生的平均成绩排序
select 学生ID, 生物, 物理, 体育, count_star as 有效课程数, avg_num as 有效平均分 from (
    select t1.sid as '学生ID', t1.num as '生物',  t2.num as '物理', t3.num as '体育', t4.num as '美术' from (select sid, num from student left join (select student_id, num from score inner join course on cid = course_id where cname='生物') as t1_inner on sid = student_id) as t1, (select sid, num from student left join (select student_id, num from score inner join course on cid = course_id where cname='物理') as t2_inner on sid = student_id) as t2, (select sid, num from student left join (select student_id, num from score inner join course on cid = course_id where cname='体育') as t3_inner on sid = student_id) as t3, (select sid, num from student left join (select student_id, num from score inner join course on cid = course_id where cname='美术') as t4_inner on sid = student_id) as t4 where t1.sid=t2.sid and t2.sid=t3.sid and t3.sid=t4.sid) as t1234 left join (select student_id, count(*) as count_star ,avg(num) as avg_num from score group by student_id
    ) as t on student_id = 学生ID order by 有效平均分;
+----------+--------+--------+--------+-----------------+-----------------+
| 学生ID   | 生物   | 物理   | 体育   | 有效课程数      | 有效平均分      |
+----------+--------+--------+--------+-----------------+-----------------+
|       14 |   NULL |   NULL |   NULL |            NULL |            NULL |
|       15 |   NULL |   NULL |   NULL |            NULL |            NULL |
|       16 |   NULL |   NULL |   NULL |            NULL |            NULL |
|        1 |     10 |      9 |   NULL |               3 |         28.3333 |
|        2 |      8 |   NULL |     68 |               3 |         58.3333 |
|        4 |     79 |     11 |     67 |               4 |         64.2500 |
|        5 |     79 |     11 |     67 |               4 |         64.2500 |
|        7 |      9 |    100 |     67 |               4 |         66.0000 |
|        8 |      9 |    100 |     67 |               4 |         66.0000 |
|        9 |     91 |     88 |     67 |               4 |         67.0000 |
|        6 |      9 |    100 |     67 |               4 |         69.0000 |
|       10 |     90 |     77 |     43 |               4 |         74.2500 |
|       11 |     90 |     77 |     43 |               4 |         74.2500 |
|       12 |     90 |     77 |     43 |               4 |         74.2500 |
|        3 |     77 |     66 |     87 |               4 |         82.2500 |
|       13 |   NULL |   NULL |     87 |               1 |         87.0000 |
+----------+--------+--------+--------+-----------------+-----------------+
16 rows in set (0.00 sec)
```

6、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；

```mysql
select course_id 课程ID, max(num) 最高分, min(num) 最低分 from score group by course_id;
+----------+-----------+-----------+
| 课程ID   | 最高分    | 最低分    |
+----------+-----------+-----------+
|        1 |        91 |         8 |
|        2 |       100 |         9 |
|        3 |        87 |        43 |
|        4 |       100 |        22 |
+----------+-----------+-----------+
4 rows in set (0.00 sec)
```

7、按各科平均成绩从低到高和及格率的百分数从高到低顺序；

```mysql
# 方法一（好，简单）
#计算各科平均分和总人数，将结果命名为t1
select course_id, avg(num) as 平均分, count(*) as 总人数 from score group by course_id; 
+-----------+-----------+-----------+
| course_id | 平均分     | 总人数     |
+-----------+-----------+-----------+
|         1 |   53.4167 |        12 |
|         2 |   65.0909 |        11 |
|         3 |   64.4167 |        12 |
|         4 |   85.2500 |        12 |
+-----------+-----------+-----------+
4 rows in set (0.00 sec)

# 创建所有及格成绩组成的表，并统计各科及格人数，将结果命名为t2
select course_id, count(*) as 及格人数 from score where num>=60 group by course_id; 
+-----------+----------+
| course_id | 及格人数 |
+-----------+----------+
|         1 |        7 |
|         2 |        8 |
|         3 |        9 |
|         4 |       11 |
+-----------+----------+
4 rows in set (0.00 sec)

# 将t1和t2进行连表
select t1.course_id, 平均分, 及格人数/总人数 as 及格率 from (select course_id, avg(num) as 平均分, count(*) as 总人数 from score group by course_id) as t1 left join (select course_id, count(*) as 及格人数 from score where num>=60 group by course_id) as t2 on t1.course_id  = t2.course_id order by 平均分, 及格率 desc;
+-----------+-----------+-----------+
| course_id | 平均分     |   及格率   |
+-----------+-----------+-----------+
|         1 |   53.4167 |    0.5833 |
|         3 |   64.4167 |    0.7500 |
|         2 |   65.0909 |    0.7273 |
|         4 |   85.2500 |    0.9167 |
+-----------+-----------+-----------+
4 rows in set (0.00 sec)
```

```mysql
# 方法二：select ... case法
# 计算score中每行数据的分数是否及格，结果表命名为t
select
	course_id,
	num,
	(
		case
        when num>=60 then
        	1
        else
        	0
        end
	) as 是否及格
from score;
+-----------+-----+--------------+
| course_id | num | 是否及格     |
+-----------+-----+--------------+
|         1 |  10 |            0 |
|         2 |   9 |            0 |
|         4 |  66 |            1 |
|         1 |   8 |            0 |
|         3 |  68 |            1 |
|         4 |  99 |            1 |
|         1 |  77 |            1 |
|         2 |  66 |            1 |
|         3 |  87 |            1 |
|         4 |  99 |            1 |
|         1 |  79 |            1 |
|         2 |  11 |            0 |
|         3 |  67 |            1 |
|         4 | 100 |            1 |
|         1 |  79 |            1 |
|         2 |  11 |            0 |
|         3 |  67 |            1 |
|         4 | 100 |            1 |
|         1 |   9 |            0 |
|         2 | 100 |            1 |
|         3 |  67 |            1 |
|         4 | 100 |            1 |
|         1 |   9 |            0 |
|         2 | 100 |            1 |
|         3 |  67 |            1 |
|         4 |  88 |            1 |
|         1 |   9 |            0 |
|         2 | 100 |            1 |
|         3 |  67 |            1 |
|         4 |  88 |            1 |
|         1 |  91 |            1 |
|         2 |  88 |            1 |
|         3 |  67 |            1 |
|         4 |  22 |            0 |
|         1 |  90 |            1 |
|         2 |  77 |            1 |
|         3 |  43 |            0 |
|         4 |  87 |            1 |
|         1 |  90 |            1 |
|         2 |  77 |            1 |
|         3 |  43 |            0 |
|         4 |  87 |            1 |
|         1 |  90 |            1 |
|         2 |  77 |            1 |
|         3 |  43 |            0 |
|         4 |  87 |            1 |
|         3 |  87 |            1 |
+-----------+-----+--------------+

# 对t按照课程ID进行分组
select course_id as 课程ID, avg(num) as 平均成绩, sum(是否及格)/count(*) as 及格率 from
(
    select
        course_id,
        num,
        (
            case
            when num>=60 then
                1
            else
                0
            end
        ) as 是否及格
    from score
) as t group by course_id order by 平均成绩, 及格率 desc;
+----------+--------------+-----------+
| 课程ID   | 平均成绩     | 及格率    |
+----------+--------------+-----------+
|        1 |      53.4167 |    0.5833 |
|        3 |      64.4167 |    0.7500 |
|        2 |      65.0909 |    0.7273 |
|        4 |      85.2500 |    0.9167 |
+----------+--------------+-----------+
4 rows in set (0.00 sec)

```

8、查询各科成绩前三名的记录:(不考虑成绩并列情况) 

```mysql
#（1）构造 “sid,course_id,first_num,second_num,third_num” 表
select sid,course_id,
(select num from score as s2 where s2.course_id = s1.course_id order by num desc limit 0, 1) as first_num,
(select num from score as s2 where s2.course_id = s1.course_id order by num desc limit 1, 1) as second_num,
(select num from score as s2 where s2.course_id = s1.course_id order by num desc limit 2, 1) as third_num
from score as s1;
+-----+-----------+-----------+------------+-----------+
| sid | course_id | first_num | second_num | third_num |
+-----+-----------+-----------+------------+-----------+
|   1 |         1 |        91 |         90 |        90 |
|   6 |         1 |        91 |         90 |        90 |
|  10 |         1 |        91 |         90 |        90 |
|  14 |         1 |        91 |         90 |        90 |
|  18 |         1 |        91 |         90 |        90 |
|  22 |         1 |        91 |         90 |        90 |
|  26 |         1 |        91 |         90 |        90 |
|  30 |         1 |        91 |         90 |        90 |
|  34 |         1 |        91 |         90 |        90 |
|  38 |         1 |        91 |         90 |        90 |
|  42 |         1 |        91 |         90 |        90 |
|  46 |         1 |        91 |         90 |        90 |
|   2 |         2 |       100 |        100 |       100 |
|  11 |         2 |       100 |        100 |       100 |
|  15 |         2 |       100 |        100 |       100 |
|  19 |         2 |       100 |        100 |       100 |
|  23 |         2 |       100 |        100 |       100 |
|  27 |         2 |       100 |        100 |       100 |
|  31 |         2 |       100 |        100 |       100 |
|  35 |         2 |       100 |        100 |       100 |
|  39 |         2 |       100 |        100 |       100 |
|  43 |         2 |       100 |        100 |       100 |
|  47 |         2 |       100 |        100 |       100 |
|   8 |         3 |        87 |         87 |        68 |
|  12 |         3 |        87 |         87 |        68 |
|  16 |         3 |        87 |         87 |        68 |
|  20 |         3 |        87 |         87 |        68 |
|  24 |         3 |        87 |         87 |        68 |
|  28 |         3 |        87 |         87 |        68 |
|  32 |         3 |        87 |         87 |        68 |
|  36 |         3 |        87 |         87 |        68 |
|  40 |         3 |        87 |         87 |        68 |
|  44 |         3 |        87 |         87 |        68 |
|  48 |         3 |        87 |         87 |        68 |
|  52 |         3 |        87 |         87 |        68 |
|   5 |         4 |       100 |        100 |       100 |
|   9 |         4 |       100 |        100 |       100 |
|  13 |         4 |       100 |        100 |       100 |
|  17 |         4 |       100 |        100 |       100 |
|  21 |         4 |       100 |        100 |       100 |
|  25 |         4 |       100 |        100 |       100 |
|  29 |         4 |       100 |        100 |       100 |
|  33 |         4 |       100 |        100 |       100 |
|  37 |         4 |       100 |        100 |       100 |
|  41 |         4 |       100 |        100 |       100 |
|  45 |         4 |       100 |        100 |       100 |
|  49 |         4 |       100 |        100 |       100 |
+-----+-----------+-----------+------------+-----------+
47 rows in set (0.00 sec)

#（2）    
select t1.sid,t1.student_id,t1.course_id,t1.num from score t1
left join
    (
    select sid,course_id,
    (select num from score as s2 where s2.course_id = s1.course_id order by num desc limit 0, 1) as first_num,
    (select num from score as s2 where s2.course_id = s1.course_id order by num desc limit 1, 1) as second_num,
    (select num from score as s2 where s2.course_id = s1.course_id order by num desc limit 2, 1) as third_num
    from score as s1
    ) t2
on t1.sid = t2.sid
where t1.num = t2.first_num or t1.num = t2.second_num or t1.num = t2.third_num order by t1.course_id, t1.num desc;

+-----+------------+-----------+-----+
| sid | student_id | course_id | num |
+-----+------------+-----------+-----+
|  34 |          9 |         1 |  91 |
|  38 |         10 |         1 |  90 |
|  42 |         11 |         1 |  90 |
|  46 |         12 |         1 |  90 |
|  23 |          6 |         2 | 100 |
|  27 |          7 |         2 | 100 |
|  31 |          8 |         2 | 100 |
|  52 |         13 |         3 |  87 |
|  12 |          3 |         3 |  87 |
|   8 |          2 |         3 |  68 |
|  17 |          4 |         4 | 100 |
|  21 |          5 |         4 | 100 |
|  25 |          6 |         4 | 100 |
+-----+------------+-----------+-----+
13 rows in set (0.00 sec)
```

9、查询每门课程被选修的学生数；

```mysql
select course_id, count(*) from score group by course_id;
+-----------+----------+
| course_id | count(*) |
+-----------+----------+
|         1 |       12 |
|         2 |       11 |
|         3 |       12 |
|         4 |       12 |
+-----------+----------+
4 rows in set (0.00 sec)
```

10、查询同名同姓学生名单，并统计同名人数；

```mysql
select sname, count(*) as 出现次数 from student group by sname having 出现次数 > 1;
Empty set (0.00 sec)
```

11、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；

```mysql
select course_id, avg(num) as avg_num from score group by course_id order by avg_num, course_id desc;
+-----------+---------+
| course_id | avg_num |
+-----------+---------+
|         1 | 53.4167 |
|         3 | 64.4167 |
|         2 | 65.0909 |
|         4 | 85.2500 |
+-----------+---------+
4 rows in set (0.00 sec)
```

12、查询平均成绩大于85的所有学生的学号、姓名和平均成绩；

```mysql
select student_id, avg(num) as avg_num from score left join student on student_id = student.sid group by student_id having avg(num)>85;
+------------+----------+
| student_id |  avg_num |
+------------+----------+
|         13 |  87.0000 |
+------------+----------+
1 row in set (0.00 sec)

select student_id, sname, avg_num from (select student_id, avg(num) as avg_num from score left join student on student_id = student.sid group by student_id having avg(num)>85) as t left join student on student_id = student.sid;
+------------+--------+---------+
| student_id | sname  | avg_num |
+------------+--------+---------+
|         13 | 刘三   | 87.0000 |
+------------+--------+---------+
1 row in set (0.00 sec)
```

13、查询课程名称为“数学”，且分数低于60的学生姓名和分数；

**【更改为】查询课程名称为“生物”，且分数低于60的学生姓名和分数；**

```mysql
select student_id, num from score inner join course on course_id = cid where cname='生物' and num < 60;
+------------+-----+
| student_id | num |
+------------+-----+
|          1 |  10 |
|          2 |   8 |
|          6 |   9 |
|          7 |   9 |
|          8 |   9 |
+------------+-----+
5 rows in set (0.00 sec)

select sname, num from student right join (select student_id, num from score inner join course on course_id = cid where cname='生物' and num < 60) as t on student_id = sid;
+--------+-----+
| sname  | num |
+--------+-----+
| 理解   |  10 |
| 钢蛋   |   8 |
| 张四   |   9 |
| 铁锤   |   9 |
| 李三   |   9 |
+--------+-----+
5 rows in set (0.00 sec)
```

14、查询课程编号为003且课程成绩在80分以上的学生的学号和姓名；

```mysql
select student_id, sname from score left join student on student_id = student.sid where course_id = 3 and num > 80;
+------------+--------+
| student_id | sname  |
+------------+--------+
|          3 | 张三   |
|         13 | 刘三   |
+------------+--------+
2 rows in set (0.00 sec)
```

15、求选了课程的学生人数

```mysql
select count(*) from (select distinct(student_id) from score) as t;
+----------+
| count(*) |
+----------+
|       13 |
+----------+
1 row in set (0.00 sec)
```

