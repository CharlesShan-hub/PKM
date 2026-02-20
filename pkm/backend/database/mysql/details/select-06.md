
案例1：查询工资不是3000的员工编号、姓名、薪资
```sql
mysql> select
    -> empno,ename,sal
    -> from
    -> emp
    -> where
    -> sal <> 3000;
+-------+--------+---------+
| empno | ename  | sal     |
+-------+--------+---------+
|  7369 | SMITH  |  800.00 |
|  7499 | ALLEN  | 1600.00 |
|  7521 | WARD   | 1250.00 |
|  7566 | JONES  | 2975.00 |
|  7654 | MARTIN | 1250.00 |
|  7698 | BLAKE  | 2850.00 |
|  7782 | CLARK  | 2450.00 |
|  7839 | KING   | 5000.00 |
|  7844 | TURNER | 1500.00 |
|  7876 | ADAMS  | 1100.00 |
|  7900 | JAMES  |  950.00 |
|  7934 | MILLER | 1300.00 |
+-------+--------+---------+
12 rows in set (0.001 sec)
```

案例2：查询工作岗位不是MANAGER的员工姓名和岗位

```sql
mysql> select
    -> ename, job
    -> from
    -> emp
    -> where
    -> job <> 'MANAGER';
+--------+-----------+
| ename  | job       |
+--------+-----------+
| SMITH  | CLERK     |
| ALLEN  | SALESMAN  |
| WARD   | SALESMAN  |
| MARTIN | SALESMAN  |
| SCOTT  | ANALYST   |
| KING   | PRESIDENT |
| TURNER | SALESMAN  |
| ADAMS  | CLERK     |
| JAMES  | CLERK     |
| FORD   | ANALYST   |
| MILLER | CLERK     |
+--------+-----------+
11 rows in set (0.001 sec)
```

  