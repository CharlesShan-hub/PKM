
案例1：查询公司中所有员工编号
```sql
select empno from emp;
```

```sql
mysql> select empno from emp; 
+-------+
| empno |
+-------+
|  7369 |
|  7499 |
|  7521 |
|  7566 |
|  7654 |
|  7698 |
|  7782 |
|  7788 |
|  7839 |
|  7844 |
|  7876 |
|  7900 |
|  7902 |
|  7934 |
+-------+
14 rows in set (0.000 sec)
```

案例2：查询公司中所有员工姓名
```sql
SELECT ENAME FROM EMP;
```

```sql
mysql> select ename from emp;
+--------+
| ename  |
+--------+
| SMITH  |
| ALLEN  |
| WARD   |
| JONES  |
| MARTIN |
| BLAKE  |
| CLARK  |
| SCOTT  |
| KING   |
| TURNER |
| ADAMS  |
| JAMES  |
| FORD   |
| MILLER |
+--------+
14 rows in set (0.000 sec)
```
