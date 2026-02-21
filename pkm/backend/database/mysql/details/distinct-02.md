测试一下，在distinct关键字前添加其它字段是否可以？

```sql
mysql> select distinct job, ename from emp;
+-----------+--------+
| job       | ename  |
+-----------+--------+
| CLERK     | SMITH  |
| SALESMAN  | ALLEN  |
| SALESMAN  | WARD   |
| MANAGER   | JONES  |
| SALESMAN  | MARTIN |
| MANAGER   | BLAKE  |
| MANAGER   | CLARK  |
| ANALYST   | SCOTT  |
| PRESIDENT | KING   |
| SALESMAN  | TURNER |
| CLERK     | ADAMS  |
| CLERK     | JAMES  |
| ANALYST   | FORD   |
| CLERK     | MILLER |
+-----------+--------+
14 rows in set (0.001 sec)
  

mysql> select ename, distinct jobfrom emp;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'distinct jobfrom emp' at line 1
```