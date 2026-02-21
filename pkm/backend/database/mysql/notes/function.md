# 数据处理函数

## 字符串相关

| 函数          | 语法                            | 说明                                   |
| ----------- | ----------------------------- | ------------------------------------ |
| **大小写转换**   |                               | [string-01](../details/string-01.md) |
| UPPER       | `UPPER(str)`                  | 将字符串转换为大写                            |
| UCASE       | `UCASE(str)`                  | 将字符串转换为大写（同UPPER）                    |
| LOWER       | `LOWER(str)`                  | 将字符串转换为小写                            |
| LCASE       | `LCASE(str)`                  | 将字符串转换为小写（同LOWER）                    |
| **字符串截取**   |                               | [string-02](../details/string-02.md) |
| SUBSTR      | `SUBSTR(str, start, length)`  | 从指定位置截取指定长度的字符串                      |
|             | `SUBSTR(str, start)`          | 从指定位置截取到字符串末尾                        |
| **字符串长度**   |                               | [string-03](../details/string-03.md) |
| LENGTH      | `LENGTH(str)`                 | 返回字符串的字节长度（汉字2字节）                    |
| CHAR_LENGTH | `CHAR_LENGTH(str)`            | 返回字符串的字符个数                           |
| **字符串拼接**   |                               | [string-04](../details/string-04.md) |
| CONCAT      | `CONCAT(str1, str2, ...)`     | 连接多个字符串                              |
| **去除空白**    |                               | [string-05](../details/string-05.md) |
| TRIM        | `TRIM(str)`                   | 去除字符串前后空白                            |
|             | `TRIM(LEADING 'x' FROM str)`  | 去除前缀字符                               |
|             | `TRIM(TRAILING 'x' FROM str)` | 去除后缀字符                               |
|             | `TRIM(BOTH 'x' FROM str)`     | 去除前后字符                               |


## 数字相关

| 函数        | 语法              | 说明                               |
| --------- | --------------- | -------------------------------- |
| **生成随机数** |                 | [math-01](../details/math-01.md) |
| RAND      | `rand()`        | 生成0到1的随机浮点数                      |
|           | `rand(x)`       | 固定随机种子                           |
| **保留小数**  |                 | [math-02](../details/math-02.md) |
| ROUND     | `round(x)`      | 四舍五入                             |
|           | `round(x,y)`    | 四舍五入，保留y位小数                      |
| TRUNCARTE | `truncate(x,y)` | 截断，保留y位小数                        |
| CEIL      | `ceil(x)`       | 返回大于或等于数值x的最小整数                  |
| FLOOR     | `floor(x)`      | 返回小于或等于数值x的最大整数                  |


## 空处理

| 函数      | 语法            | 说明                         |
| ------- | ------------- | -------------------------- |
| **空处理** |               | [null](../details/null.md) |
| IFNULL  | `ifnull(x,y)` | 当x为NULL时，将x当做y处理           |


## 日期和时间相关函数

| 函数                   | 语法                               | 说明                               |
| -------------------- | -------------------------------- | -------------------------------- |
| **获取当前日期和时间**        |                                  | [date-01](../details/date-01.md) |
| NOW                  | `now()`                          | 获取的是执行select语句的时刻                |
| SYSDATE              | `sysdate()`                      | 获取的是执行sysdate()函数的时刻             |
| **获取当前日期**           |                                  | [date-02](../details/date-02.md) |
| CURDATE              | `curdate()`                      | 三个效果一样                           |
| CURRENT_DATE         | `current_date()`                 | `current_date`都可以                |
| **获取当前时间**           |                                  | [date-03](../details/date-03.md) |
| CURTIME              | `curtime()`                      | 三个效果一样                           |
| CURRENT_TIME         | `current_time()`                 | `current_time`都可以                |
| **获取单独的年、月、日、时、分、秒** |                                  | [date-04](../details/date-04.md) |
| YEAR                 | `year(x)`                        | 年                                |
| MONTH                | `month(x)`                       | 月                                |
| DAY                  | `day(x)`                         | 日                                |
| HOUR                 | `hour(x)`                        | 时                                |
| MINUTE               | `minute(x)`                      | 分                                |
| SECOND               | `second(x)`                      | 秒                                |
| **日期计算**             |                                  | [date-05](../details/date-05.md) |
| DATE_ADD             | `date_add(日期, interval expr 单位)` | 给指定的日期添加间隔的时间                    |
| **日期格式化**            |                                  | [date-06](../details/date-06.md) |
|                      |                                  |                                  |
|                      |                                  |                                  |
|                      |                                  |                                  |

### dayofweek、dayofmonth、dayofyear函数

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672719401783-7ea51704-954a-4f96-aa81-3a8da4b34582.png#averageHue=%23110f0e&clientId=uc0e8c595-6b95-4&from=paste&height=665&id=u1a4c7890&originHeight=665&originWidth=685&originalType=binary&ratio=1&rotation=0&showTitle=false&size=39505&status=done&style=shadow&taskId=u36f1ca0f-c525-47e4-8ccf-df5d8210281&title=&width=685)

  

dayofweek：一周中的第几天（1~7），周日是1，周六是7。

  

dayofmonth：一个月中的第几天（1~31）

  

dayofyear：一年中的第几天（1~366）

  

  

### last_day函数

  

获取给定日期所在月的最后一天的日期：

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672719572099-bba462b8-da22-42b7-9a40-9c2c545596ef.png#averageHue=%23121010&clientId=uc0e8c595-6b95-4&from=paste&height=163&id=u8cab6ec4&originHeight=163&originWidth=498&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8323&status=done&style=shadow&taskId=ucef40e03-23be-4936-a671-ac674c20438&title=&width=498)

  

### datediff函数

  

计算两个日期之间所差天数：

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672720897012-c5e7e6dd-29de-46b0-b2c1-e1de3e8d6e54.png#averageHue=%23121110&clientId=uc0e8c595-6b95-4&from=paste&height=169&id=u9b900968&originHeight=169&originWidth=865&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10814&status=done&style=shadow&taskId=ufb6d4060-84b9-44b3-8694-a9cf990bc54&title=&width=865)

  

时分秒不算，只计算日期部分相差的天数。

  

  

### timediff函数

  

计算两个日期所差时间，例如日期1和日期2所差10:20:30，表示差10小时20分钟30秒。

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672721193551-f65b470a-9060-4010-b172-b34eb1787e55.png#averageHue=%23121110&clientId=uc0e8c595-6b95-4&from=paste&height=168&id=u56a06c8e&originHeight=168&originWidth=987&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11553&status=done&style=shadow&taskId=ua81b206f-eb6b-47b3-ad2a-e4b048fdd31&title=&width=987)

  

  

## if函数

  

如果条件为TRUE则返回“YES”，如果条件为FALSE则返回“NO”：

  

```sql

  

SELECT IF(500<1000, "YES", "NO");

  

```

  

例如：如果工资高于3000，则输出1，反之则输出0

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672725980625-f929cbdc-41ec-49d4-a5de-bc753dfbe67e.png#averageHue=%230f0e0e&clientId=uc0e8c595-6b95-4&from=paste&height=536&id=ued7bfdee&originHeight=536&originWidth=747&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29371&status=done&style=shadow&taskId=uec5813f3-7f94-4ae2-9644-78e1fd281f6&title=&width=747)

  

再例如：如果名字是SMITH的，工资上调10%，其他员工工资正常显示。

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672726073468-51733168-6ebe-477d-9aba-267adcefd10a.png#averageHue=%23100f0e&clientId=uc0e8c595-6b95-4&from=paste&height=534&id=uf2148f3a&originHeight=534&originWidth=992&originalType=binary&ratio=1&rotation=0&showTitle=false&size=38069&status=done&style=shadow&taskId=u7679358d-9412-4000-b8cd-872e9980209&title=&width=992)

  

再例如：工作岗位是MANAGER的工资上调10%，是SALESMAN的工资上调20%，其他岗位工资正常。

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672726371265-19128e1a-47cf-46b0-9b80-310d37010535.png#averageHue=%23100f0e&clientId=uc0e8c595-6b95-4&from=paste&height=532&id=u575eb753&originHeight=532&originWidth=1441&originalType=binary&ratio=1&rotation=0&showTitle=false&size=55630&status=done&style=shadow&taskId=uf0e71940-399c-4edf-bd67-14f893e719e&title=&width=1441)

  

**上面这个需求也可以使用：case.. when.. then.. when.. then.. else.. end来完成：**

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672726864928-8206091b-3bd3-4f12-b784-173aff775d6f.png#averageHue=%23141210&clientId=uc0e8c595-6b95-4&from=paste&height=724&id=u37fc5544&originHeight=724&originWidth=561&originalType=binary&ratio=1&rotation=0&showTitle=false&size=57934&status=done&style=shadow&taskId=u812c7487-a5f1-4d90-a5bd-891e360d45b&title=&width=561)

  

  

## cast函数

  

cast函数用于将值从一种数据类型转换为表达式中指定的另一种数据类型

  

语法：cast(值 as 数据类型)

  

例如：cast('2020-10-11' as date)，表示将字符串'2020-10-11'转换成日期date类型。

  

在使用cast函数时，可用的数据类型包括：

  

  

- date：日期类型

  

- time：时间类型

  

- datetime：日期时间类型

  

- signed：有符号的int类型（有符号指的是正数负数）

  

- char：定长字符串类型

  

- decimal：浮点型

  

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672737293605-d7e38772-e9c3-40ab-a7ea-3311aa14a1a9.png#averageHue=%2311100f&clientId=uc0e8c595-6b95-4&from=paste&height=662&id=u174ddf1e&originHeight=662&originWidth=778&originalType=binary&ratio=1&rotation=0&showTitle=false&size=34283&status=done&style=shadow&taskId=u2531ed29-bfef-4efc-a5b0-6ff107330b6&title=&width=778)

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672737634602-96cdd564-1220-445e-9b18-b3f0a2a55379.png#averageHue=%2311100f&clientId=uc0e8c595-6b95-4&from=paste&height=435&id=ued100771&originHeight=435&originWidth=545&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18617&status=done&style=shadow&taskId=u559bfe74-f2ec-4e05-a37f-2cd08b29cde&title=&width=545)

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672737720321-3812fd42-d3a4-4985-96d2-629947d9ce48.png#averageHue=%23111010&clientId=uc0e8c595-6b95-4&from=paste&height=213&id=ua7df14ff&originHeight=213&originWidth=604&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10420&status=done&style=shadow&taskId=u66dc0647-a030-400f-8ec0-b3c2b22a844&title=&width=604)

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672737802812-d04d581c-138c-4e4e-97d4-c979558e9b2e.png#averageHue=%2311100f&clientId=uc0e8c595-6b95-4&from=paste&height=170&id=u214f15ff&originHeight=170&originWidth=714&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8572&status=done&style=shadow&taskId=ud2929b4c-8582-4dc3-a2ba-8de75b96e58&title=&width=714)

  

  

## 加密函数

  

md5函数，可以将给定的字符串经过md5算法进行加密处理，字符串经过加密之后会生成一个固定长度32位的字符串，md5加密之后的密文通常是不能解密的：

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672737046172-5ee0458a-60c6-4bae-b075-94b7dee440ab.png#averageHue=%23131110&clientId=uc0e8c595-6b95-4&from=paste&height=220&id=u6e900f32&originHeight=220&originWidth=568&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10865&status=done&style=shadow&taskId=uabd2a6f3-e59b-4dac-ba4c-bcc743fafad&title=&width=568)