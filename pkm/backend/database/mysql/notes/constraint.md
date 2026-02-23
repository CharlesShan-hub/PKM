# 约束constraint

创建表时，可以给表的字段添加约束，可以保证数据的完整性、有效性。比如大家上网注册用户时常见的：用户名不能为空。对不起，用户名已存在。等提示信息。
约束通常包括：
- 非空约束：not null
- 检查约束：check
- 唯一性约束：unique
- 主键约束（PK）：primary key
- 外键约束（FK）：foreign key

---
## 非空约束
语法格式：
```sql
create table t_stu(
  no int,
  name varchar(255) not null,
  age int
);
```
name字段不能为空。插入数据时如果没有给name指定值，则报错。

---
## 检查约束
```sql
create table t_stu(
  no int,
  name varchar(255),
  age int,
  check(age > 18)
);
```

---
## 唯一性约束
语法格式：
```sql
create table t_stu(
  no int,
  name varchar(255),
  email varchar(255) unique
);
```
email字段设置为唯一性，唯一性的字段值是可以为NULL的。但不能重复。以上在字段后面添加的约束，叫做列级约束。
当然，添加约束还有另一种方式：表级约束：
```sql
create table t_stu(
  no int,
  name varchar(255),
  email varchar(255),
  unique(email)
);
```
使用表级约束可以为多个字段添加联合唯一。
```sql
create table t_stu(
  no int,
  name varchar(255),
  email varchar(255),
  unique(name,email)
);
```
创建约束时也可以给约束起名字，将来可以通过约束的名字来删除约束：
```sql
create table t_stu(
  no int,
  name varchar(255),
  email varchar(255),
  constraint t_stu_name_email_unique unique(name,email)
);
```
所有的约束都存储在一个系统表当中：table_constraints。这个系统表在这个数据库当中：information_schema

---
## 主键约束

1. 主键：**primary key**，简称**PK**
2. 主键约束的字段**不能为NULL，并且不能重复**。
3. 任何一张表都应该有主键，没有主键的表可以视为无效表。
4. 主键值是这行记录的身份证号，是唯一标识。在数据库表中即使两条数据一模一样，但由于主键值不同，我们也会认为是两条完全的不同的数据。
5. 主键分类：
   6. 根据字段数量分类：
      1. 单一主键（1个字段作为主键）==>建议的
      2. 复合主键（2个或2个以上的字段作为主键）
   7. 根据业务分类：
      1. 自然主键（主键和任何业务都无关，只是一个单纯的自然数据）===>建议的
      2. 业务主键（主键和业务挂钩，例如：银行卡账号作为主键）
8. 单一主键（建议使用这种方式）
```sql
create table t_student(
  id bigint primary key,
  sno varchar(255) unique,
  sname varchar(255) not null
)
```

7. 复合主键（很少用，了解）
```sql
create table t_user(
  no int,
  name varchar(255),
  age int,
  primary key(no,name)
);
```

8. 主键自增：既然主键值是一个自然的数字，mysql为主键值提供了一种自增机制，不需要我们程序员维护，mysql自动维护该字段
```sql
create table t_vip(
  no int primary key auto_increment,
  name varchar(255)
);
```

---
## 外键约束

1. 有这样一个需求：要求设计表，能够存储学生以及学校信息。
   2. 第一种方案：一张表

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679198700192-73c1c697-39a5-483e-b267-730fb808082d.png#averageHue=%23f2f58e&clientId=uf7a0608d-b7a1-4&from=paste&height=263&id=u385df011&originHeight=263&originWidth=881&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11603&status=done&style=shadow&taskId=u6a97350e-9ae3-4c6d-b1ec-963559ebf2e&title=&width=881)
这种方式会导致数据冗余，浪费空间。

   2. 第二种方案：两张表：一张存储学生，一张存储学校

t_school 表
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679198814824-520944e2-5b83-49ba-97e7-b8830286127a.png#averageHue=%23c9d481&clientId=uf7a0608d-b7a1-4&from=paste&height=85&id=ud1ad0346&originHeight=85&originWidth=471&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2397&status=done&style=shadow&taskId=u76cd09e9-9753-41f7-81d7-729db7c551a&title=&width=471)
t_student 表
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679198856678-a80be906-abc8-4bf7-ac5e-e6a59b11c48a.png#averageHue=%23f3f77a&clientId=uf7a0608d-b7a1-4&from=paste&height=264&id=ufa1ef2a6&originHeight=264&originWidth=532&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4445&status=done&style=shadow&taskId=u30eaa682-24a0-4b6f-a1c5-3eed3bc24cc&title=&width=532)
如果采用以上两张表存储数据，对于学生表来说，sno这个字段的值是不能随便填的，这个sno是学校编号，必须要求这个字段中的值来自学校表的sno。
为了达到要求，此时就必须要给t_student表的sno字段添加外键约束了。

2. 外键约束：foreign key，简称FK。
3. 添加了外键约束的字段中的数据必须来自其他字段，不能随便填。
4. 假设给a字段添加了外键约束，要求a字段中的数据必须来自b字段，b字段不一定是主键，但至少要有唯一性。
5. 外键约束可以给单个字段添加，叫做单一外键。也可以给多个字段联合添加，叫做复合外键。复合外键很少用。
6. a表如果引用b表中的数据，可以把b表叫做父表，把a表叫做子表。
   7. 创建表时，先创建父表，再创建子表。
   8. 插入数据时，先插入父表，在插入子表。
   9. 删除数据时，先删除子表，再删除父表。
   10. 删除表时，先删除子表，再删除父表。
11. 如何添加外键：
```sql
create table t_school( 
  sno int primary key, 
  sname varchar(255) 
); 
create table t_student( 
  no int primary key, 
  name varchar(255), 
  age int, 
  sno int, 
  constraint t_school_sno_fk foreign key(sno) references t_school(sno) 
);
```

8. 级联删除

创建子表时，外键可以添加：on delete cascade，这样在删除父表数据时，子表会级联删除。谨慎使用。
```sql
create table t_student( 
  no int primary key, 
  name varchar(255), 
  age int, 
  sno int, 
  constraint t_school_sno_fk foreign key(sno) references t_school(sno) on delete cascade 
);
```
```sql
###删除约束
alert table t_student drop foreign key t_student_sno_fk;
###添加约束
alert table t_student add constraint t_student_sno_fk foreign key(sno) references t_school(sno) on delete cascade;
```

9. 级联更新 
```sql
create table t_student( 
  no int primary key, 
  name varchar(255), 
  age int, 
  sno int, 
  constraint t_school_sno_fk foreign key(sno) references t_school(sno) on update cascade 
);
```

10. 级联置空
```sql
create table t_student( 
  no int primary key, 
  name varchar(255), 
  age int, 
  sno int, 
  constraint t_school_sno_fk foreign key(sno) references t_school(sno) on delete set null 
);
```

