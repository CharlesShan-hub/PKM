案例：查找工资大于平均工资的员工

```sql
mysql> select avg(sal) from emp;
+-------------+
| avg(sal)    |
+-------------+
| 2073.214286 |
+-------------+
1 row in set (0.004 sec)

-- 这样是不行滴！
mysql> select ename, sal from emp where sal > avg(sal);
ERROR 1111 (HY000): Invalid use of group function

mysql> select ename, sal from emp where sal > (select avg(sal) from emp);
+-------+---------+
| ename | sal     |
+-------+---------+
| JONES | 2975.00 |
| BLAKE | 2850.00 |
| CLARK | 2450.00 |
| SCOTT | 3000.00 |
| KING  | 5000.00 |
| FORD  | 3000.00 |
+-------+---------+
6 rows in set (0.004 sec)
```