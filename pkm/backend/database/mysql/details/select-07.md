案例：找出薪资大于3000的员工姓名、薪资

```sql
mysql> select 
    -> ename, sal
    -> from
    -> emp
    -> where
    -> sal > 3000;
+-------+---------+
| ename | sal     |
+-------+---------+
| KING  | 5000.00 |
+-------+---------+
1 row in set (0.001 sec)
```

案例：找出薪资大于等于3000的员工姓名、薪资

```sql
mysql> select ename, sal from emp where sal >= 3000;
+-------+---------+
| ename | sal     |
+-------+---------+
| SCOTT | 3000.00 |
| KING  | 5000.00 |
| FORD  | 3000.00 |
+-------+---------+
3 rows in set (0.001 sec)
```

案例：找出薪资小于3000的员工姓名、薪资

```sql
mysql> select ename, sal from emp where sal < 3000;
+--------+---------+
| ename  | sal     |
+--------+---------+
| SMITH  |  800.00 |
| ALLEN  | 1600.00 |
| WARD   | 1250.00 |
| JONES  | 2975.00 |
| MARTIN | 1250.00 |
| BLAKE  | 2850.00 |
| CLARK  | 2450.00 |
| TURNER | 1500.00 |
| ADAMS  | 1100.00 |
| JAMES  |  950.00 |
| MILLER | 1300.00 |
+--------+---------+
11 rows in set (0.001 sec)
```

