```sql
mysql> select count(*) from emp join dept on emp.deptno = dept.deptno;
+----------+
| count(*) |
+----------+
|       14 |
+----------+
1 row in set (0.001 sec)

mysql> select count(*) from emp join dept;
+----------+
| count(*) |
+----------+
|       56 |
+----------+
1 row in set (0.001 sec)
  
mysql> select count(*) from dept;
+----------+
| count(*) |
+----------+
|        4 |
+----------+
1 row in set (0.001 sec)
  
mysql> select count(*) from emp;
+----------+
| count(*) |
+----------+
|       14 |
+----------+
1 row in set (0.001 sec)
```