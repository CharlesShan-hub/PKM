
### 获取当前时间

获取档期时间有三种写法，掌握其中一种即可：

- curtime()
- current_time()
- current_time

```sql
mysql> select curtime(), current_time, current_time();
+-----------+--------------+----------------+
| curtime() | current_time | current_time() |
+-----------+--------------+----------------+
| 15:02:31  | 15:02:31     | 15:02:31       |
+-----------+--------------+----------------+
1 row in set (0.000 sec)
```
  


  

  
