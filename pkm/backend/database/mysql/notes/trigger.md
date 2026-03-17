# 触发器
MySQL 触发器是一种数据库对象，它是与表相关联的特殊程序。它可以在特定的数据操作（例如插入（INSERT）、更新（UPDATE）或删除（DELETE））触发时自动执行。MySQL 触发器使数据库开发人员能够在数据的不同状态之间维护一致性和完整性，并且可以为特定的数据库表自动执行操作。

触发器的作用主要有以下几个方面：

1.  强制实施业务规则：触发器可以帮助确保数据表中的业务规则得到强制执行，例如检查插入或更新的数据是否符合某些规则。 
2.  数据审计：触发器可以声明在执行数据修改时自动记日志或审计数据变化的操作，使数据对数据库管理员和 SQL 审计人员更易于追踪和审计。 
3.  执行特定业务操作：触发器可以自动执行特定的业务操作，例如计算数据行的总数、计算平均值或总和等。 

MySQL 触发器分为两种类型: BEFORE 和 AFTER。BEFORE 触发器在执行 INSERT、UPDATE、DELETE 语句之前执行，而 AFTER 触发器在执行 INSERT、UPDATE、DELETE 语句之后执行。


创建触发器的语法如下：

```plsql
CREATE TRIGGER trigger_name
BEFORE/AFTER INSERT/UPDATE/DELETE ON table_name FOR EACH ROW
BEGIN
-- 触发器执行的 SQL 语句
END;
```

其中：

- trigger_name：触发器的名称
- BEFORE/AFTER：触发器的类型，可以是 BEFORE 或者 AFTER
- INSERT/UPDATE/DELETE：触发器所监控的 DML 调用类型
- table_name：触发器所绑定的表名
- FOR EACH ROW：表示触发器在每行受到 DML 的影响之后都会执行
- 触发器执行的 SQL 语句：该语句会在触发器被触发时执行

需要注意的是，触发器是一种高级的数据库功能，只有在必要的情况下才应该使用，例如在需要实施强制性业务规则时。过多的触发器和复杂的触发器逻辑可能会影响查询性能和扩展性。

**关于触发器的NEW和OLD关键字：**
在 MySQL 触发器中，NEW 和 OLD 是两个特殊的关键字，用于引用在触发器中受到修改的行的新值和旧值。具体而言：

- NEW：在触发 INSERT 或 UPDATE 操作期间，NEW 用于引用将要插入或更新到表中的新行的值。
- OLD：在触发 UPDATE 或 DELETE 操作期间，OLD 用于引用更新或删除之前在表中的旧行的值。

通俗的讲，NEW 是指触发器执行的操作所要插入或更新到当前行中的新数据；而 OLD 则是指当前行在触发器执行前原本的数据。

在MySQL 触发器中，NEW 和 OLD 使用方法是相似的。在触发器中，可以像引用表的其他列一样引用 NEW 和 OLD。例如，可以使用 OLD.column_name 从旧行中引用列值，也可以使用 NEW.column_name 从新行中引用列值。

示例：

假设有一个名为 my_table 的表，其中包含一个名为 quantity 的列。当在该表上执行 UPDATE 操作时，以下触发器会将旧值 OLD.quantity 累加到新值 NEW.quantity 中：

```plsql
CREATE TRIGGER my_trigger
BEFORE UPDATE ON my_table
FOR EACH ROW
BEGIN
SET NEW.quantity = NEW.quantity + OLD.quantity;
END;
```

在此触发器中，OLD.quantity 引用原始行的 quantity 值（旧值），而 NEW.quantity 引用更新行的 quantity 值（新值）。在触发器执行期间，数据行的 quantity 值将设置为旧值加上新值。

需要注意的是，在使用 NEW 和 OLD 时，需要根据 DML 操作的类型进行判断，以确定哪个关键字表示新值，哪个关键字则表示旧值。

案例：当我们对dept表中的数据进行insert delete update的时候，请将这些操作记录到日志表当中，日志表如下：
```sql
drop table if exists oper_log;

create table oper_log(
  id bigint primary key auto_increment,
  table_name varchar(100) not null comment '操作的哪张表',
  oper_type varchar(100) not null comment '操作类型包括insert delete update',
  oper_time datetime not null comment '操作时间',
  oper_id bigint not null comment '操作的那行记录的id',
  oper_desc text comment '操作描述'
);
```

触发器1：向dept表中插入数据时，记录日志
```plsql
create trigger dept_trigger_insert 
after insert on dept
for each row
begin
    insert into oper_log(id,table_name,oper_type,oper_time,oper_id,oper_desc) values
(null,'dept','insert',now(),new.deptno,concat('插入数据：deptno=', new.deptno, ',dname=', new.dname,',loc=', new.loc));
end;
```

查看触发器：
```plsql
show triggers;
```

删除触发器：
```sql
drop trigger if exists dept_trigger_insert;
```

向dept表中插入一条记录：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1687250537958-36fdd3ce-6aa3-48e9-aa34-39dac470c82f.png#averageHue=%23f2f0ed&clientId=ua8e0f13a-20b6-4&from=paste&height=254&id=u2d5b23b7&originHeight=254&originWidth=327&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14090&status=done&style=shadow&taskId=u0b945c07-f0a0-4c61-b2e3-a27a514ddb8&title=&width=327)
日志表中多了一条记录：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1687250572044-f7216711-ee12-49bf-b687-b21b7b5856cd.png#averageHue=%23f3f1f0&clientId=ua8e0f13a-20b6-4&from=paste&height=145&id=u94fbdc8c&originHeight=145&originWidth=1014&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15305&status=done&style=shadow&taskId=u7fad2861-b2e6-4220-af3e-0a22c454cf0&title=&width=1014)

触发器2：修改dept表中数据时，记录日志
```plsql
create trigger dept_trigger_update
after update on dept
for each row
begin
    insert into oper_log(id,table_name,oper_type,oper_time,oper_id,oper_desc) values
(null,'dept','update',now(),new.deptno,concat('更新前：deptno=', old.deptno, ',dname=', old.dname,',loc=', old.loc, 
                                              ',更新后：deptno=', new.deptno, ',dname=', new.dname,',loc=', new.loc));
end;
```
更新一条记录：
```sql
update dept set loc = '北京' where deptno = 60;
```
日志表中多了一条记录：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1687250964502-f6af7d92-c4a5-4910-9efa-d08090647643.png#averageHue=%23f5f4f3&clientId=ua8e0f13a-20b6-4&from=paste&height=186&id=u505e3af3&originHeight=186&originWidth=1237&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19556&status=done&style=shadow&taskId=u9ffa318a-67b1-477d-b3c7-851a438b483&title=&width=1237)
**注意：更新一条记录则对应一条日志。如果一次更新3条记录，那么日志表中插入3条记录。**

触发器3：删除dept表中数据时，记录日志
```plsql
create trigger dept_trigger_delete
after delete on dept
for each row
begin
    insert into oper_log(id,table_name,oper_type,oper_time,oper_id,oper_desc) values
(null,'dept','delete',now(),old.deptno,concat('删除了数据：deptno=', old.deptno, ',dname=', old.dname,',loc=', old.loc));
end;
```

删除一条记录：
```sql
delete from dept where deptno = 60;
```

日志表中多了一条记录：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1687251196650-5527bf1a-370d-47c8-bf45-2b7babc5e1a5.png#averageHue=%23f4f3f1&clientId=ua8e0f13a-20b6-4&from=paste&height=186&id=u7fa2da22&originHeight=186&originWidth=1282&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22331&status=done&style=shadow&taskId=u82995139-6935-439b-b17e-5232b0195cf&title=&width=1282)
