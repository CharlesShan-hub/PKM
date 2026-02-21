
### date_add函数

* date_add函数的作用：给指定的日期添加间隔的时间，从而得到一个新的日期。
* date_add函数的语法格式：date_add(日期, interval expr 单位)，例如：

```
mysql> select now(), date_add(now(), interval 3 day);
+---------------------+---------------------------------+
| now()               | date_add(now(), interval 3 day) |
+---------------------+---------------------------------+
| 2026-02-21 15:09:47 | 2026-02-24 15:09:47             |
+---------------------+---------------------------------+
1 row in set (0.001 sec)
```

  

以'2023-01-03'为基准，间隔3天之后的日期：'2023-01-06'

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672709436259-c6d671c6-ccc8-4109-9612-1f178801ef64.png#averageHue=%23121110&clientId=uc0e8c595-6b95-4&from=paste&height=171&id=ub0dc1d88&originHeight=171&originWidth=778&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11798&status=done&style=shadow&taskId=u06a7162d-aafa-4469-8f12-d3ea81c1f63&title=&width=778)

  

  

以'2023-01-03'为基准，间隔3个月之后的日期：'2023-04-03'

  

详细解释一下这个函数的相关参数：

  

  

- 日期：一个日期类型的数据

- interval：关键字，翻译为“间隔”，固定写法

- expr：指定具体的间隔量，一般是一个数字。**也可以为负数，如果为负数，效果和date_sub函数相同**。

- 单位

- year：年

- month：月

- day：日

- hour：时

- minute：分

- second：秒

- microsecond：微秒（1秒等于1000毫秒，1毫秒等于1000微秒）

- week：周

- quarter：季度

  

  

请分析下面这条SQL语句所表达的含义：

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672710673500-8afb96ad-3aa5-4adb-9160-9aaac4b4ff83.png#averageHue=%23131211&clientId=uc0e8c595-6b95-4&from=paste&height=162&id=u455ecd04&originHeight=162&originWidth=1036&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12957&status=done&style=shadow&taskId=u3148a05b-3fbe-432e-8492-373fde1d2db&title=&width=1036)

  

以上SQL表示：以2022-10-01 10:10:10为基准，在这个时间基础上添加-1微秒，也就是减去1微秒。

  

以上SQL也可以采用date_sub函数完成，例如：

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672710799157-9775a5b0-143f-493b-a6f0-cd8db5c6ca31.png#averageHue=%23131211&clientId=uc0e8c595-6b95-4&from=paste&height=159&id=u70af0451&originHeight=159&originWidth=990&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13185&status=done&style=shadow&taskId=u7bf2be69-c836-4951-bd99-69c09f553ec&title=&width=990)

  

另外，单位也可以采用复合型单位，例如：

  

  

- SECOND_MICROSECOND

  

- MINUTE_MICROSECOND

  

- MINUTE_SECOND：几分几秒之后

  

- HOUR_MICROSECOND

  

- HOUR_SECOND

  

- HOUR_MINUTE：几小时几分之后

  

- DAY_MICROSECOND

  

- DAY_SECOND

  

- DAY_MINUTE

  

- DAY_HOUR：几天几小时之后

  

- YEAR_MONTH：几年几个月之后

  

  

如果单位采用复合型的话，expr该怎么写呢？例如单位采用：day_hour，假设我要表示3天2小时之后，怎么写？

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672711325140-0a281589-4bc2-4fc8-bd7f-9a5ff180ba71.png#averageHue=%23121110&clientId=uc0e8c595-6b95-4&from=paste&height=171&id=u186c11d0&originHeight=171&originWidth=1009&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13317&status=done&style=shadow&taskId=u2827b5bf-37d2-486f-9db8-fa8b15ce510&title=&width=1009)

  

'3,2'这个应该很好理解，表示3天2个小时之后。'3,2'和day_hour是对应的。

  

  