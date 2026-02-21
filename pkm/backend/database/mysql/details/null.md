### 空处理函数

`ifnull(x, y)`，空处理函数，当x为NULL时，将x当做y处理。

案例：如果员工的津贴是NULL时当做0处理。
```sql
mysql> select ename,comm from emp limit 5;
+--------+---------+
| ename  | comm    |
+--------+---------+
| SMITH  |    NULL |
| ALLEN  |  300.00 |
| WARD   |  500.00 |
| JONES  |    NULL |
| MARTIN | 1400.00 |
+--------+---------+
5 rows in set (0.001 sec)

mysql> select ename,ifnull(comm,0) from emp limit 5;
+--------+----------------+
| ename  | ifnull(comm,0) |
+--------+----------------+
| SMITH  |           0.00 |
| ALLEN  |         300.00 |
| WARD   |         500.00 |
| JONES  |           0.00 |
| MARTIN |        1400.00 |
+--------+----------------+
5 rows in set (0.001 sec)
```

在SQL语句中，凡是有NULL参与的数学运算，最终的计算结果都是NULL：
```sql
mysql> select null+0, null*10;
+--------+---------+
| null+0 | null*10 |
+--------+---------+
|   NULL |    NULL |
+--------+---------+
1 row in set (0.000 sec)
```

看这样一个需求：查询每个员工的年薪。（年薪 = (月薪 + 津贴) * 12个月。注意：有的员工津贴comm是NULL。）

```sql
mysql> select ename, 12*(sal+comm) 年薪 from emp limit 5;
+--------+----------+
| ename  | 年薪     |
+--------+----------+
| SMITH  |     NULL |
| ALLEN  | 22800.00 |
| WARD   | 21000.00 |
| JONES  |     NULL |
| MARTIN | 31800.00 |
+--------+----------+
5 rows in set (0.001 sec)
  
msql> select ename, 12*(sal+ifnull(comm,0)) 年薪 from emp limit 5;
+--------+----------+
| ename  | 年薪     |
+--------+----------+
| SMITH  |  9600.00 |
| ALLEN  | 22800.00 |
| WARD   | 21000.00 |
| JONES  | 35700.00 |
| MARTIN | 31800.00 |
+--------+----------+
5 rows in set (0.001 sec)
```

  

  