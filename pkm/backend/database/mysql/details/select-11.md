
### or

or表示或者，还有另一种写法：||

案例：找出工作岗位是MANAGER和SALESMAN的员工姓名、工作岗位

```sql
mysql> select ename, job from emp where
    -> job = 'MANAGER' or job = 'SALESMAN';
+--------+----------+
| ename  | job      |
+--------+----------+
| ALLEN  | SALESMAN |
| WARD   | SALESMAN |
| JONES  | MANAGER  |
| MARTIN | SALESMAN |
| BLAKE  | MANAGER  |
| CLARK  | MANAGER  |
| TURNER | SALESMAN |
+--------+----------+
7 rows in set (0.001 sec)
```

注意：这个题目描述中有这样一句话：MANAGER和SALESMAN，有的同学一看到“和”，就直接使用“and”了，因为“和”对应的英文单词是“and”，如果是这样的话，就大错特错了，因为and表示并且，使用and表示工作岗位既是MANAGER又是SALESMAN的员工，这样的员工是不存在的，因为每一个员工只有一个岗位，不可能同时从事两个岗位。所以使用and是查询不到任何结果的。如下

```sql
mysql> select ename, job from emp where job = 'MANAGER' and job = 'SALESMAN';
Empty set (0.001 sec)
```

