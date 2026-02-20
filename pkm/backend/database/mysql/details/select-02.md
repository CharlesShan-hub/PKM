案例1：查询员工编号以及员工姓名。
```sql
mysql> select empno, ename from emp;
+-------+--------+
| empno | ename  |
+-------+--------+
|  7369 | SMITH  |
|  7499 | ALLEN  |
|  7521 | WARD   |
|  7566 | JONES  |
|  7654 | MARTIN |
|  7698 | BLAKE  |
|  7782 | CLARK  |
|  7788 | SCOTT  |
|  7839 | KING   |
|  7844 | TURNER |
|  7876 | ADAMS  |
|  7900 | JAMES  |
|  7902 | FORD   |
|  7934 | MILLER |
+-------+--------+
14 rows in set (0.001 sec)
```

案例2：修改顺序
```sql
mysql> select ename, empno from emp;
+--------+-------+
| ename  | empno |
+--------+-------+
| SMITH  |  7369 |
| ALLEN  |  7499 |
| WARD   |  7521 |
| JONES  |  7566 |
| MARTIN |  7654 |
| BLAKE  |  7698 |
| CLARK  |  7782 |
| SCOTT  |  7788 |
| KING   |  7839 |
| TURNER |  7844 |
| ADAMS  |  7876 |
| JAMES  |  7900 |
| FORD   |  7902 |
| MILLER |  7934 |
+--------+-------+
14 rows in set (0.001 sec)
```
