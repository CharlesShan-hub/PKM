### if

例如：如果工资高于3000，则输出1，反之则输出0
```sql
select ename, if(sal > 3000, 1, 0) from emp;
```

```shell
mysql> select ename, if(sal > 3000, 1, 0) from emp;
+--------+----------------------+
| ename  | if(sal > 3000, 1, 0) |
+--------+----------------------+
| SMITH  |                    0 |
| ALLEN  |                    0 |
| WARD   |                    0 |
| JONES  |                    0 |
| MARTIN |                    0 |
| BLAKE  |                    0 |
| CLARK  |                    0 |
| SCOTT  |                    0 |
| KING   |                    1 |
| TURNER |                    0 |
| ADAMS  |                    0 |
| JAMES  |                    0 |
| FORD   |                    0 |
| MILLER |                    0 |
+--------+----------------------+
14 rows in set (0.001 sec)
```

再例如：如果名字是SMITH的，工资上调10%，其他员工工资正常显示。

```sql
select ename, if(ename='SMITH', sal*1.1, sal) from emp;
```

```shell
+--------+---------------------------------+
| ename  | if(ename='SMITH', sal*1.1, sal) |
+--------+---------------------------------+
| SMITH  |                          880.00 |
| ALLEN  |                         1600.00 |
| WARD   |                         1250.00 |
| JONES  |                         2975.00 |
| MARTIN |                         1250.00 |
| BLAKE  |                         2850.00 |
| CLARK  |                         2450.00 |
| SCOTT  |                         3000.00 |
| KING   |                         5000.00 |
| TURNER |                         1500.00 |
| ADAMS  |                         1100.00 |
| JAMES  |                          950.00 |
| FORD   |                         3000.00 |
| MILLER |                         1300.00 |
+--------+---------------------------------+
14 rows in set (0.001 sec)
```
