
* `between...and...`等同于 `>= and <=` 。他们只是在写法结构上有区别，执行原理和效率方面没有区别。（注意，包含左右两个边界值。）
* 支持数字、日期、字符串等数据类型。
* between...and...在使用时一定是**左小右大**。左大右小时无法查询到数据。

案例：找出薪资在1600到3000的员工姓名、薪资

```sql
mysql> select ename, sal from emp where sal between 1600 and 3000;
+-------+---------+
| ename | sal     |
+-------+---------+
| ALLEN | 1600.00 |
| JONES | 2975.00 |
| BLAKE | 2850.00 |
| CLARK | 2450.00 |
| SCOTT | 3000.00 |
| FORD  | 3000.00 |
+-------+---------+
6 rows in set (0.001 sec)
```

案例：查询在1982-01-23到1987-04-19之间入职的员工
```sql
mysql> select ename, sal from emp 
    -> where
    -> hiredate between '1982-01-23' and '1987-04-19';
+--------+---------+
| ename  | sal     |
+--------+---------+
| SCOTT  | 3000.00 |
| MILLER | 1300.00 |
+--------+---------+
2 rows in set (0.001 sec)
```
注意：以上SQL语句中日期需要加上单引号。

  
