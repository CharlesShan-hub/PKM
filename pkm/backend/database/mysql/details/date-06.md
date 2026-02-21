
### date_format日期格式化函数

  

将日期转换成具有某种格式的日期字符串，通常用在查询操作当中。（date类型转换成char类型）

  

语法格式：`date_format(日期, '日期格式')`

  

该函数有两个参数：

  

  

- 第一个参数：日期。这个参数就是即将要被格式化的日期。类型是date类型。

  

- 第二个参数：指定要格式化的格式字符串。

  

- %Y：四位年份

  

- %y：两位年份

  

- %m：月份（1..12）

  

- %d：日（1..30）

  

- %H：小时（0..23）

  

- %i：分（0..59）

  

- %s：秒（0..59）

  

  

例如：获取当前系统时间，让其以这个格式展示：2000-10-11 20:15:30

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672716928881-badddb77-c670-43f3-8b25-8e2eb4952a04.png#averageHue=%23121110&clientId=uc0e8c595-6b95-4&from=paste&height=168&id=uf1769116&originHeight=168&originWidth=790&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12687&status=done&style=shadow&taskId=u0936983e-6c2d-4e0f-96a9-905426534b9&title=&width=790)

  

注意：在mysql当中，默认的日期格式就是：%Y-%m-%d %H:%i:%s，所以当你直接输出日期数据的时候，会自动转换成该格式的字符串：

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672717081322-e99bdff0-76df-4fcc-958a-463bf9e65d9d.png#averageHue=%23131110&clientId=uc0e8c595-6b95-4&from=paste&height=164&id=udf0a9e15&originHeight=164&originWidth=369&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7005&status=done&style=shadow&taskId=ua8a7ba31-3b81-427d-8a55-a8a84114389&title=&width=369)

  

  

### str_to_date函数

  

该函数的作用是将char类型的日期字符串转换成日期类型date，通常使用在插入和修改操作当中。（char类型转换成date类型）

  

假设有一个学生表t_student，学生有一个生日的字段，类型是date类型：

  

```sql

  

drop table if exists t_student;

  

create table t_student(

  

name varchar(255),

  

birth date

  

);

  

desc t_student;

  

```

  

我们要给这个表插入一条数据：姓名zhangsan，生日85年10月1日，执行以下insert语句：

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672718111465-698c085a-b3f1-4523-9f3f-d27ceb4410d5.png#averageHue=%231b1815&clientId=uc0e8c595-6b95-4&from=paste&height=59&id=u816b6342&originHeight=59&originWidth=1163&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13327&status=done&style=shadow&taskId=u25e9289a-7274-49fc-9db5-e54cc764c7d&title=&width=1163)

  

错误原因：日期值不正确。意思是：birth字段需要一个日期，你给的这个字符串'10/01/1985'我识别不了。这种情况下，我们就可以使用str_to_date函数进行类型转换：

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672718492868-58ab55ff-a4e7-481f-9c58-9c81014d1762.png#averageHue=%2315100f&clientId=uc0e8c595-6b95-4&from=paste&height=83&id=u3cdb0924&originHeight=83&originWidth=1379&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12797&status=done&style=shadow&taskId=u619f99b1-3107-44e6-8738-542c8b9aaf8&title=&width=1379)

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672718610506-ec24a44e-7854-4037-8567-b42dfb9228c0.png#averageHue=%23121110&clientId=uc0e8c595-6b95-4&from=paste&height=159&id=uf93570e5&originHeight=159&originWidth=533&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8550&status=done&style=shadow&taskId=ua5be6705-7bc3-46b4-9922-15d9020df6e&title=&width=533)

  

当然，如果你提供的日期字符串格式能够被mysql解析，str_to_date函数是可以省略的，底层会自动调用该函数进行类型转换：

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672718807175-8b62c13a-e771-482d-a999-7548501da25e.png#averageHue=%23110f0e&clientId=uc0e8c595-6b95-4&from=paste&height=625&id=u14b85262&originHeight=625&originWidth=1088&originalType=binary&ratio=1&rotation=0&showTitle=false&size=66015&status=done&style=shadow&taskId=uae019b86-851f-4348-962a-a15199adc0f&title=&width=1088)

  

如果日期格式符合以上的几种格式，mysql都会自动进行类型转换的。

  