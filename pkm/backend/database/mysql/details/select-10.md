
### and

and表示并且，还有另一种写法：&&

案例：找出薪资大于等于3000并且小于等于5000的员工姓名、薪资。

```sql
mysql> select ename,sal from emp
    -> where
    -> sal >= 3000 and sal <= 5000;
+-------+---------+
| ename | sal     |
+-------+---------+
| SCOTT | 3000.00 |
| KING  | 5000.00 |
| FORD  | 3000.00 |
+-------+---------+
3 rows in set (0.001 sec)
```

