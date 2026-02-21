找出岗位是MANAGER的员工姓名和薪资，按照薪资升序排列。

```sql
mysql> select ename,sal from emp where job='MANAGER' order by sal asc;
+-------+---------+
| ename | sal     |
+-------+---------+
| CLARK | 2450.00 
| BLAKE | 2850.00 |
| JONES | 2975.00 |
+-------+---------+
3 rows in set (0.001 sec)
```