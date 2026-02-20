### is null、is not null

在数据库中null不是一个值，不能用等号和不等号衡量，null代表什么也没有，没有数据，没有值
* 判断某个数据是否为null，不能使用等号，只能使用 is null
* 判断某个数据是否不为null，不能使用不等号，只能使用 is not null

案例1：找出津贴为空的员工姓名、薪资、津贴。

```sql
mysql> select ename,sal,comm from emp
    -> where
    -> comm is null;
+--------+---------+------+
| ename  | sal     | comm |
+--------+---------+------+
| SMITH  |  800.00 | NULL |
| JONES  | 2975.00 | NULL |
| BLAKE  | 2850.00 | NULL |
| CLARK  | 2450.00 | NULL |
| SCOTT  | 3000.00 | NULL |
| KING   | 5000.00 | NULL |
| ADAMS  | 1100.00 | NULL |
| JAMES  |  950.00 | NULL |
| FORD   | 3000.00 | NULL |
| MILLER | 1300.00 | NULL |
+--------+---------+------+
10 rows in set (0.001 sec)
```

我们使用等号，尝试一下：

```sql
mysql> select ename,sal,comm from emp where comm = null;
Empty set (0.001 sec)
```
查询不到任何数据，所以判断是否为空，不能用等号。

案例2：找出津贴不为空的员工姓名、薪资、津贴

```sql
mysql> select ename,sal,comm from emp where comm is not null;
+--------+---------+---------+
| ename  | sal     | comm    |
+--------+---------+---------+
| ALLEN  | 1600.00 |  300.00 |
| WARD   | 1250.00 |  500.00 |
| MARTIN | 1250.00 | 1400.00 |
| TURNER | 1500.00 |    0.00 |
+--------+---------+---------+
4 rows in set (0.001 sec)
```

  
