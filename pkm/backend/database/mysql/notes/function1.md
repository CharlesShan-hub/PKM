# 数据处理函数
> MySQL提供了丰富的内置函数，主要分为以下几类：字符串函数、数值函数、日期时间函数、条件函数、转换函数和加密函数。熟练掌握这些函数可以大大提高SQL查询的灵活性和效率。
> 本章案例的数据初始化：[powerpoint-init-data](../details/powerpoint-init-data.md)

## 字符串相关


| 函数            | 语法                                      | 说明                                   |
| ------------- | --------------------------------------- | ------------------------------------ |
| **大小写转换**     |                                         | [string-01](../details/string-01.md) |
| UPPER         | `UPPER(str)`                            | 将字符串转换为大写                            |
| UCASE         | `UCASE(str)`                            | 将字符串转换为大写（同UPPER）                    |
| LOWER         | `LOWER(str)`                            | 将字符串转换为小写                            |
| LCASE         | `LCASE(str)`                            | 将字符串转换为小写（同LOWER）                    |
| **字符串截取**     |                                         | [string-02](../details/string-02.md) |
| SUBSTR        | `SUBSTR(str, start, length)`            | 从指定位置截取指定长度的字符串                      |
|               | `SUBSTR(str, start)`                    | 从指定位置截取到字符串末尾                        |
| ​​SUBSTRING​​ | `SUBSTRING(str, position[, length])`    | 从指定位置开始截取指定长度的字符(位置从1开始)             |
| ​​LEFT​       | `LEFT(string, length)`                  | 从字符串左侧截取指定长度的字符                      |
| **字符串长度**     |                                         | [string-03](../details/string-03.md) |
| LENGTH        | `LENGTH(str)`                           | 返回字符串的字节长度（汉字2字节）                    |
| CHAR_LENGTH   | `CHAR_LENGTH(str)`                      | 返回字符串的字符个数                           |
| **字符串拼接**     |                                         | [string-04](../details/string-04.md) |
| CONCAT        | `CONCAT(str1, str2, ...)`               | 连接多个字符串                              |
| **去除空白**      |                                         | [string-05](../details/string-05.md) |
| TRIM          | `TRIM(str)`                             | 去除字符串前后空白                            |
|               | `TRIM(LEADING 'x' FROM str)`            | 去除前缀字符                               |
|               | `TRIM(TRAILING 'x' FROM str)`           | 去除后缀字符                               |
|               | `TRIM(BOTH 'x' FROM str)`               | 去除前后字符                               |
| ​​LTRIM​​     | `LTRIM(string)`                         | 去除字符串前端的空格                           |
| ​​RTRIM​​     | `RTRIM(string)`                         | 去除字符串后端的空格                           |
| **字符集**       |                                         |                                      |
| ​​CHARSET​​   | `CHARSET(str)`                          | 返回字符串的字符集                            |
| **查找比较替换**    |                                         |                                      |
| ​​INSTR​​     | `INSTR(string, substring)`              | 返回子串在字符串中出现的位置(从1开始)，未找到则返回0         |
| ​​REPLACE​​   | `REPLACE(str, search_str, replace_str)` | 在字符串中用新字符串替换所有匹配的子串                  |
| ​​STRCMP​​    | `STRCMP(string1, string2)`              | 逐字符比较两个字符串的大小(返回-1,0,1)              |


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
| DATE_SUB             | `date_sub(日期, interval expr 单位)` | 给指定的日期减去间隔的时间                    |
| DAYOFYEAR            | `dayofyear(x)`                   | 一年中的第几天                          |
| DAYOFMONTH           | `dayofmonth(x)`                  | 一月中的第几天                          |
| DAYOFWEEK            | `dayofweek(x)`                   | 一周中的第几天                          |
| LAST_DAY             | `last_day(x)`                    | 日期所在月的最后一天                       |
| DATEDIFF             | `datediff(x,y)`                  | 两个日期之间所差天数                       |
| TIMEDIFF             | `timediff(x,y)`                  | 两个时间之间所差时间                       |
| **日期格式化**            |                                  | [date-06](../details/date-06.md) |
| DATE_FORMAT          | `date_format(x,y)`               | 日期格式化                            |
| STR_TO_DATE          | `str_to_date`                    |                                  |

---
## 条件函数

| 函数       | 语法                                              |
| -------- | ----------------------------------------------- |
| **if**   | [if](../details/if.md)                          |
| IF       | `if(x,y,z)`(如果x成了就y否则z)                         |
| **case** | [case](../details/case.md)                      |
| CASE     | `case.. when.. then.. when.. then.. else.. end` |

---
## cast函数

| 函数   | 语法                | 说明                   |
| ---- | ----------------- | -------------------- |
| cast | `cast(值 as 数据类型)` | 从一种数据类型转换为表达式中指定的另一种 |

案例：[cast](../details/cast.md)

---
## 加密函数

| 函数   | 语法     |
| ---- | ------ |
| md5  | 我这里用不了 |
| sha  | 我这里用不了 |
| sha2 | 这个可以用  |
案例：[md5](../details/md5.md)