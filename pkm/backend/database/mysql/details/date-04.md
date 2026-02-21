
### 获取单独的年、月、日、时、分、秒

```sql
mysql> select year(now()) 年, month(now()) 月, day(now()) 日, hour(now()) 时, minute(now()) 分, second(now()) 秒;
+------+------+------+------+------+------+
| 年   | 月   | 日   | 时   | 分   | 秒   |
+------+------+------+------+------+------+
| 2026 |    2 |   21 |   15 |    5 |   48 |
+------+------+------+------+------+------+
1 row in set (0.001 sec)
```


注意：这些函数在使用的时候，需要传递一个日期参数给它，它可以获取到你给定的这个日期相关的年、月、日、时、分、秒的信息。

  

一次性提取一个给定日期的“年月日”部分，可以使用date()函数，例如：

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672713926559-d9c4257b-3536-4124-b4f4-3fd3626a293e.png#averageHue=%2311100f&clientId=uc0e8c595-6b95-4&from=paste&height=168&id=u161f961c&originHeight=168&originWidth=438&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7552&status=done&style=shadow&taskId=ub9643e54-a1b4-424f-a2d7-e15c7538b83&title=&width=438)

  

一次性提取一个给定日期的“时分秒”部分，可以使用time()函数，例如：

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672721340191-9c568184-73b5-4c26-9035-95245016ba4f.png#averageHue=%2311100f&clientId=uc0e8c595-6b95-4&from=paste&height=161&id=u0bb5bc88&originHeight=161&originWidth=428&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7598&status=done&style=shadow&taskId=u09037fc7-e074-481b-bf6a-ccc8fc49cf6&title=&width=428)
