![day38作业图](D:\老男孩\day038\day38作业图.png)

```mysql
create table class(
	cid int primary key auto_increment,
    caption char(18) not null
);

create table teacher(
	tid int primary key auto_increment,
    tname char(18) not null
);

create table student(
	sid int primary key auto_increment,
    sname char(18) not null,
    gender enum('男','女') not null,
    class_id int not null,
    foreign key(class_id) references class(cid)		# 多对一
    on update cascade
);

create table course(
	cid int primary key auto_increment,
    cname char(18) not null,
    teacher_id int not null,
    foreign key(teacher_id) references teacher(tid)	# 多对一
    on update cascade
);

#因为学生表和课程表是多对多的关系，所以它们产生出了成绩表score
create table score(
	sid int primary key auto_increment,
    student_id int not null,
    foreign key(student_id) references student(sid)	# 多对一
    on update cascade,
    course_id int not null,
    foreign key(course_id) references course(cid)	# 多对一
    on update cascade,
    number int not null,
);

insert into class(caption) values ('三年二班'),('一年三班'),('三年一班');
insert into teacher(tname) values ('波多'),('苍空'),('饭岛');
insert into student(sname,gender,class_id) values ('钢蛋','女',1),('钢锤','女',1),('山炮','男',2);
insert into course(cname,teacher_id) values ('生物',1),('体育',2),('物理',2);
insert into score values (1,1,1,60),(2,1,2,59),(3,2,2,100);
```

![day38作业思路](D:\老男孩\day038\day38作业思路.png)