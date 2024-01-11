# day40作业（张珵）

**用到的原始数据**

**注意：有三个同学是没选任何课的，它们影响到的题目有11、13题**

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

**1、查询男生、女生的人数；**

```mysql
select gender, count(sid) from student group by gender;
+--------+------------+
| gender | count(sid) |
+--------+------------+
| 女     |          6 |
| 男     |         10 |
+--------+------------+
2 rows in set (0.08 sec)
```

**2、查询姓“张”的学生名单；**

```mysql
select sname from student where sname like '张%';
+--------+
| sname  |
+--------+
| 张三   |
| 张一   |
| 张二   |
| 张四   |
+--------+
4 rows in set (0.00 sec)
```

**3、课程平均分从高到低显示**

```mysql
select cname, avg(num) avg_num from score inner join course on course_id = cid group by cid order by avg_num desc;
+--------+---------+
| cname  | avg_num |
+--------+---------+
| 美术   | 85.2500 |
| 物理   | 65.0909 |
| 体育   | 64.4167 |
| 生物   | 53.4167 |
+--------+---------+
4 rows in set (0.17 sec)
```

**4、查询有课程成绩小于60分的同学的学号、姓名；**

```mysql
select distinct student_id,sname from score inner join student on student_id = student.sid where num < 60;
+------------+--------+
| student_id | sname  |
+------------+--------+
|          1 | 理解   |
|          2 | 钢蛋   |
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
11 rows in set (0.03 sec)
```

**5、查询至少有一门课与学号为1的同学所学课程相同的同学的学号和姓名；**

```mysql
select distinct student_id, sname from score inner join student on student_id = student.sid where student_id != 1 and course_id in (select course_id from score where student_id = 1);
+------------+--------+
| student_id | sname  |
+------------+--------+
|          2 | 钢蛋   |
|          3 | 张三   |
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
11 rows in set (0.00 sec)
```

**6、查询出只选修了一门课程的全部学生的学号和姓名；**

```mysql
select student_id, sname from score inner join student on student_id = student.sid group by student_id having count(student_id) = 1;
+------------+--------+
| student_id | sname  |
+------------+--------+
|         13 | 刘三   |
+------------+--------+
1 row in set (0.00 sec)
```

**7、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；**

```mysql
select course_id, max(num), min(num) from score group by course_id;
+-----------+----------+----------+
| course_id | max(num) | min(num) |
+-----------+----------+----------+
|         1 |       91 |        8 |
|         2 |      100 |        9 |
|         3 |       87 |       43 |
|         4 |      100 |       22 |
+-----------+----------+----------+
4 rows in set (0.00 sec)
```

**8、查询课程编号“2”的成绩比课程编号“1”课程低的所有同学的学号、姓名；**

```mysql
# 构造辅助表t1
select student_id, num from score where course_id=1;
+------------+-----+
| student_id | num |
+------------+-----+
|          1 |  10 |
|          2 |   8 |
|          3 |  77 |
|          4 |  79 |
|          5 |  79 |
|          6 |   9 |
|          7 |   9 |
|          8 |   9 |
|          9 |  91 |
|         10 |  90 |
|         11 |  90 |
|         12 |  90 |
+------------+-----+
12 rows in set (0.00 sec)

# 构造辅助表t2
select student_id, num from score where course_id=2;
+------------+-----+
| student_id | num |
+------------+-----+
|          1 |   9 |
|          3 |  66 |
|          4 |  11 |
|          5 |  11 |
|          6 | 100 |
|          7 | 100 |
|          8 | 100 |
|          9 |  88 |
|         10 |  77 |
|         11 |  77 |
|         12 |  77 |
+------------+-----+
11 rows in set (0.00 sec)

# 查询课程编号“2”的成绩比课程编号“1”课程低的所有同学的学号
select t1.student_id from (select student_id, num from score where course_id=1) as t1 inner join (select student_id, num from score where course_id=2) as t2 on t1.student_id = t2.student_id where t1.num > t2.num;
+------------+
| student_id |
+------------+
|          1 |
|          3 |
|          4 |
|          5 |
|          9 |
|         10 |
|         11 |
|         12 |
+------------+
8 rows in set (0.03 sec)

# 查询课程编号“2”的成绩比课程编号“1”课程低的所有同学的学号、姓名；
select t.student_id,sname from (select t1.student_id from (select student_id, num from score where course_id=1) as t1 inner join (select student_id, num from score where course_id=2) as t2 on t1.student_id = t2.student_id where t1.num > t2.num) as t inner join student on t.student_id = student.sid;
+------------+--------+
| student_id | sname  |
+------------+--------+
|          1 | 理解   |
|          3 | 张三   |
|          4 | 张一   |
|          5 | 张二   |
|          9 | 李一   |
|         10 | 李二   |
|         11 | 李四   |
|         12 | 如花   |
+------------+--------+
8 rows in set (0.01 sec)
```

**9、查询“生物”课程比“物理”课程成绩高的所有学生的学号【第8题延伸】；**

```mysql
# 构造辅助表t1（生物）
select student_id, num from score inner join course on course_id = cid where cname='生物';
+------------+-----+
| student_id | num |
+------------+-----+
|          1 |  10 |
|          2 |   8 |
|          3 |  77 |
|          4 |  79 |
|          5 |  79 |
|          6 |   9 |
|          7 |   9 |
|          8 |   9 |
|          9 |  91 |
|         10 |  90 |
|         11 |  90 |
|         12 |  90 |
+------------+-----+
12 rows in set (0.00 sec)

# 构造辅助表t2（物理）
select student_id, num from score inner join course on course_id = cid where cname='物理';
+------------+-----+
| student_id | num |
+------------+-----+
|          1 |   9 |
|          3 |  66 |
|          4 |  11 |
|          5 |  11 |
|          6 | 100 |
|          7 | 100 |
|          8 | 100 |
|          9 |  88 |
|         10 |  77 |
|         11 |  77 |
|         12 |  77 |
+------------+-----+
11 rows in set (0.00 sec)

# 查询“生物”课程比“物理”课程成绩高的所有学生的学号
select t1.student_id from (select student_id, num from score inner join course on course_id = cid where cname='生物') as t1 inner join (select student_id, num from score inner join course on course_id = cid where cname='物理') as t2 on t1.student_id = t2.student_id where t1.num > t2.num;
+------------+
| student_id |
+------------+
|          1 |
|          3 |
|          4 |
|          5 |
|          9 |
|         10 |
|         11 |
|         12 |
+------------+
8 rows in set (0.00 sec)
```

**10、查询平均成绩大于60分的同学的学号和平均成绩;**

```mysql
select student_id,avg(num) avg_num from score group by student_id having avg_num>60;
+------------+---------+
| student_id | avg_num |
+------------+---------+
|          3 | 82.2500 |
|          4 | 64.2500 |
|          5 | 64.2500 |
|          6 | 69.0000 |
|          7 | 66.0000 |
|          8 | 66.0000 |
|          9 | 67.0000 |
|         10 | 74.2500 |
|         11 | 74.2500 |
|         12 | 74.2500 |
|         13 | 87.0000 |
+------------+---------+
11 rows in set (0.00 sec)
```

**11、查询所有同学的学号、姓名、选课数、总成绩【注意：含三个没选课的同学】；**

```mysql
select student.sid, sname, count(course_id), sum(num) from score right join student on student_id = student.sid group by student.sid;
+-----+--------+------------------+----------+
| sid | sname  | count(course_id) | sum(num) |
+-----+--------+------------------+----------+
|   1 | 理解   |                3 |       85 |
|   2 | 钢蛋   |                3 |      175 |
|   3 | 张三   |                4 |      329 |
|   4 | 张一   |                4 |      257 |
|   5 | 张二   |                4 |      257 |
|   6 | 张四   |                4 |      276 |
|   7 | 铁锤   |                4 |      264 |
|   8 | 李三   |                4 |      264 |
|   9 | 李一   |                4 |      268 |
|  10 | 李二   |                4 |      297 |
|  11 | 李四   |                4 |      297 |
|  12 | 如花   |                4 |      297 |
|  13 | 刘三   |                1 |       87 |
|  14 | 刘一   |                0 |     NULL |
|  15 | 刘二   |                0 |     NULL |
|  16 | 刘四   |                0 |     NULL |
+-----+--------+------------------+----------+
16 rows in set (0.00 sec)
```

**12、查询姓“李”的老师的个数；**

```mysql
select count(tid) from teacher where tname like '李%';
+------------+
| count(tid) |
+------------+
|          2 |
+------------+
1 row in set (0.04 sec)
```

**13、查询没学过“张磊老师”课的同学的学号、姓名【注意：含三个没选课的同学】；**

```python
# （1）张磊老师教的所有课的id
select cid from course inner join teacher on teacher_id = tid where tname='张磊老师';
+-----+
| cid |
+-----+
|   1 |
+-----+
1 row in set (0.03 sec)

# （2）学过“张磊老师”课的同学的学号（考虑到张磊老师将来可能教多门课，所以用了distinct、in）
select distinct student_id from score where course_id in (
	select cid from course inner join teacher on teacher_id = tid where tname='张磊老师');
+------------+
| student_id |
+------------+
|          1 |
|          2 |
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
12 rows in set (0.00 sec)

# （3）没学过“张磊老师”课的同学的学号、姓名
select sid, sname from student where sid not in (
	select distinct student_id from score where course_id in (
		select cid from course inner join teacher on teacher_id = tid where tname='张磊老师'));
+-----+--------+
| sid | sname  |
+-----+--------+
|  13 | 刘三   |
|  14 | 刘一   |
|  15 | 刘二   |
|  16 | 刘四   |
+-----+--------+
4 rows in set (0.00 sec)
```

**14、查询学过“1”并且也学过编号“2”课程的同学的学号、姓名；**

```mysql
# 选了课程1的学生学号
select student_id from score where course_id = 1;
+------------+
| student_id |
+------------+
|          1 |
|          2 |
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
12 rows in set (0.00 sec)

# 选了课程2的学生学号
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

# 学过“1”并且也学过编号“2”课程的同学的学号、姓名
select distinct student_id, sname from score inner join student on student_id = student.sid where student_id in (select student_id from score where course_id = 1) and student_id in (select student_id from score where course_id = 2);
+------------+--------+
| student_id | sname  |
+------------+--------+
|          1 | 理解   |
|          3 | 张三   |
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
11 rows in set (0.00 sec)
```

**15、查询学过“李平老师”所教的所有课的同学的学号、姓名；**

```mysql
# （1）李平老师教的所有课的id
select cid from course inner join teacher on teacher_id = tid where tname='李平老师';
+-----+
| cid |
+-----+
|   2 |
|   4 |
+-----+
2 rows in set (0.00 sec)

# （2）李平老师教的课程门数
select count(cid) from (select cid from course inner join teacher on teacher_id = tid where tname='李平老师') as t2;
+------------+
| count(cid) |
+------------+
|          2 |
+------------+
1 row in set (0.00 sec)

# （3）在score中筛选出“course_id in 第（1）问结果”的学号、课程编号
select student_id, course_id from score where course_id in (select cid from course inner join teacher on teacher_id = tid where tname='李平老师');
+------------+-----------+
| student_id | course_id |
+------------+-----------+
|          1 |         2 |
|          3 |         2 |
|          4 |         2 |
|          5 |         2 |
|          6 |         2 |
|          7 |         2 |
|          8 |         2 |
|          9 |         2 |
|         10 |         2 |
|         11 |         2 |
|         12 |         2 |
|          1 |         4 |
|          2 |         4 |
|          3 |         4 |
|          4 |         4 |
|          5 |         4 |
|          6 |         4 |
|          7 |         4 |
|          8 |         4 |
|          9 |         4 |
|         10 |         4 |
|         11 |         4 |
|         12 |         4 |
+------------+-----------+
23 rows in set (0.00 sec)

# （4）对第（3）问结果按student_id分组，统计每个student_id出现的次数，筛选这个次数=李平老师教的课程门数
select student_id from 
	(
    	select student_id, course_id from score where course_id in (select cid from course inner join teacher on teacher_id = tid where tname='李平老师')
	) as t3
	group by student_id having count(student_id) = 
	(
        select count(cid) from (select cid from course inner join teacher on teacher_id = tid where tname='李平老师') as t2
    );
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

# （5）为第（4）问结果加上名字
select student_id, sname from 
	(
    	select student_id, course_id from score where course_id in (select cid from course inner join teacher on teacher_id = tid where tname='李平老师')
	) as t3 inner join student on student_id = student.sid
	group by student_id having count(student_id) = 
	(
        select count(cid) from (select cid from course inner join teacher on teacher_id = tid where tname='李平老师') as t2
    );
+------------+--------+
| student_id | sname  |
+------------+--------+
|          1 | 理解   |
|          3 | 张三   |
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
11 rows in set (0.00 sec)
```

