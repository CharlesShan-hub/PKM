### 获取当前日期

获取当前日期有三种写法，掌握任意一种即可：

- curdate()
- current_date()
- current_date

```sql
mysql> select curdate(), current_date, current_date();
+------------+--------------+----------------+
| curdate()  | current_date | current_date() |
+------------+--------------+----------------+
| 2026-02-21 | 2026-02-21   | 2026-02-21     |
+------------+--------------+----------------+
1 row in set (0.000 sec)
```