案例：找出每个工作岗位的工资排名在前两名的。

substring_index函数的使用：
```sql
mysql> select substring_index('http://www.baidu.com','.',1);
+-----------------------------------------------+
| substring_index('http://www.baidu.com','.',1) |
+-----------------------------------------------+
| http://www                                    |
+-----------------------------------------------+
1 row in set (0.001 sec)
  
mysql> select substring_index('http://www.baidu.com','.',2);
+-----------------------------------------------+
| substring_index('http://www.baidu.com','.',2) |
+-----------------------------------------------+
| http://www.baidu                              |
+-----------------------------------------------+
1 row in set (0.000 sec)
```

group_concat函数的使用：
```sql
mysql> select group_concat(empno order by sal desc) from emp group by job;
+---------------------------------------+
| group_concat(empno order by sal desc) |
+---------------------------------------+
| 7902,7788                             |
| 7934,7876,7900,7369                   |
| 7566,7698,7782                        |
| 7839                                  |
| 7499,7844,7654,7521                   |
+---------------------------------------+
5 rows in set (0.001 sec)
```

```sql
mysql> select job, substring_index(group_concat(empno order by sal desc),',',2) as top2 from emp group by job;
+-----------+-----------+
| job       | top2      |
+-----------+-----------+
| ANALYST   | 7902,7788 |
| CLERK     | 7934,7876 |
| MANAGER   | 7566,7698 |
| PRESIDENT | 7839      |
| SALESMAN  | 7499,7844 |
+-----------+-----------+
5 rows in set (0.001 sec)
```

