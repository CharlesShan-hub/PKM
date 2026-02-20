案例1：查询月薪3000的员工编号及姓名
```sql
mysql> select ename, sal from emp where sal = 3000;
+-------+---------+
| ename | sal     |
+-------+---------+
| SCOTT | 3000.00 |
| FORD  | 3000.00 |
+-------+---------+
2 rows in set (0.001 sec)
```

案例2：查询员工FORD的岗位及月薪(mysql,所以虽然是小写的也能搜出来)（在Oracle数据库当中是查询不到数据的，Oracle的语法要比MySQL的语法严谨。对于SQL语句本身来说是不区分大小写的，但是对于表中真实存储的数据，大写A和小写a还是不一样的，这一点Oracle做的很好。MySQL的语法更随性。另外在Oracle当中，字符串是必须使用单引号括起来的，但在MySQL当中，字符串可以使用单引号，也可以使用双引号）
```sql
mysql> select ename, sal from emp where ename = 'ford';
+-------+---------+
| ename | sal     |
+-------+---------+
| FORD  | 3000.00 |
+-------+---------+
1 row in set (0.001 sec)
```

