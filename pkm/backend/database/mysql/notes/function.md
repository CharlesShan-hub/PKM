
# 数据处理函数

关于select语句，我们之前都是这样写：select 字段名 from 表名; 其实，这里的字段名可以看做“变量”，select后面既然可以跟变量，那么可以跟常量吗，尝试一下：

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668568118423-c5b5d189-4d32-41ab-a189-3f155d0d0efa.png#averageHue=%230e0d0d&clientId=u005f32df-cdfa-4&from=paste&height=502&id=uf4590195&originHeight=502&originWidth=866&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24621&status=done&style=shadow&taskId=u9bf03714-2a03-4e7b-98d7-9996316a176&title=&width=866)

通过以上sql的测试得知，select后面既可以跟变量，又可以跟常量。

以上三条SQL中前两条中100和'abc'都是常量，最后一条SQL的abc没有添加单引号，它会被当做某个表的字段名，因为没有这个字段所以报错。

  

## 字符串相关

### 转大写upper和ucase

```sql

# 查询所有员工名字，以大写形式展现

select upper(ename) as ename from emp;

```

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668565912887-88d14d6c-707b-4e50-ac47-f8ad61b40d14.png#averageHue=%230e0e0d&clientId=u005f32df-cdfa-4&from=paste&height=531&id=ud706ac81&originHeight=531&originWidth=711&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22988&status=done&style=shadow&taskId=ua5341942-dd96-4402-8f3e-05136a93880&title=&width=711)

还有一个和upper函数功能相同的函数ucase，也可以转大写，了解一下即可：

```sql

# 查询所有员工姓名，以大写形式展现

select ucase(ename) as ename from emp;

```

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668566229563-55802f88-f6d6-436a-b478-18832d7a0342.png#averageHue=%230f0e0d&clientId=u005f32df-cdfa-4&from=paste&height=534&id=uff6a6590&originHeight=534&originWidth=674&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23082&status=done&style=shadow&taskId=uface697c-6972-498a-86af-50b161e48cd&title=&width=674)

```sql

# 查询员工smith的岗位、薪资（假如你不知道数据库表中的人名是大写、小写还是大小写混合）

select ename, job, sal from emp where upper(ename) = 'SMITH';

```

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668566360054-6e77882a-21fc-4b6e-9a04-3e0098606db8.png#averageHue=%23100f0e&clientId=u005f32df-cdfa-4&from=paste&height=178&id=uf8993c00&originHeight=178&originWidth=982&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11947&status=done&style=shadow&taskId=u72025ccb-5725-4313-bf7b-3edebed799a&title=&width=982)

  

### 转小写lower和lcase

**很简单，不再赘述，直接上代码：**

```sql

# 查询员工姓名，以小写形式展现

select lower(ename) as ename from emp;

select lcase(ename) as ename from emp;

```

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668566699289-0a479f71-ecf4-4a3f-ac4c-8516a4f0fee8.png#averageHue=%230f0e0d&clientId=u005f32df-cdfa-4&from=paste&height=216&id=u0f889bef&originHeight=216&originWidth=646&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9493&status=done&style=shadow&taskId=u5f16833e-e425-424b-a769-1761dd7023f&title=&width=646)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668566716526-c8fac5f9-7079-4738-a3d1-2a5c3c5e1145.png#averageHue=%230f0e0d&clientId=u005f32df-cdfa-4&from=paste&height=189&id=ue19b9b87&originHeight=189&originWidth=643&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8007&status=done&style=shadow&taskId=u7fc1e3dd-17d7-4f33-b8ed-b88901fb087&title=&width=643)

  

### 截取字符串substr

语法：substr('被截取的字符串', 起始下标, 截取长度)

有两种写法：

第一种：substr('被截取的字符串', 起始下标, 截取长度)

第二种：substr('被截取的字符串', 起始下标)，当第三个参数“截取长度”缺失时，截取到字符串末尾

注意：起始下标从1开始，不是从0开始。（1表示从左侧开始的第一个位置，-1表示从右侧开始的第一个位置。）

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668567142258-6748508c-c3bb-440f-8ad7-c64df6c0028d.png#averageHue=%23100f0e&clientId=u005f32df-cdfa-4&from=paste&height=648&id=u521d5ef0&originHeight=648&originWidth=664&originalType=binary&ratio=1&rotation=0&showTitle=false&size=35242&status=done&style=shadow&taskId=u50bb124d-9e6b-4c8a-b48c-76594e0ec3c&title=&width=664)

  

练习：找出员工名字中第二个字母是A的

```sql

select ename from emp where substr(ename, 2, 1) = 'A';

```

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668567271612-710d3592-6111-4ab5-97c1-12f809ac7645.png#averageHue=%230f0e0d&clientId=u005f32df-cdfa-4&from=paste&height=254&id=u2313b4ee&originHeight=254&originWidth=854&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14523&status=done&style=shadow&taskId=u8ae9b244-f6d3-441c-89d0-4466eaa73e4&title=&width=854)

  

### 获取字符串长度length

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672736218451-70fddda1-2541-4c91-9f39-3f968a6b6e12.png#averageHue=%23100f0f&clientId=uc0e8c595-6b95-4&from=paste&height=167&id=u69789788&originHeight=167&originWidth=525&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7442&status=done&style=shadow&taskId=u39c20cea-67f3-49eb-9d8e-8c548360b72&title=&width=525)

注意：一个汉字是2个长度。

  

### 获取字符的个数char_length

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672736125194-177317bd-f65c-4c05-bda7-f58961b78fd7.png#averageHue=%2311100f&clientId=uc0e8c595-6b95-4&from=paste&height=168&id=uKcvT&originHeight=168&originWidth=582&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8283&status=done&style=shadow&taskId=u2abebb18-4522-415a-bf80-859153252d1&title=&width=582)

  

### 字符串拼接

语法：concat('字符串1', '字符串2', '字符串3'....)

拼接的字符串数量没有限制。

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668569810019-a8c939c4-518d-4ed9-961a-27d4440d13d0.png#averageHue=%2311100f&clientId=u005f32df-cdfa-4&from=paste&height=437&id=u00e5d696&originHeight=437&originWidth=860&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29849&status=done&style=shadow&taskId=ufbffbf88-a2ed-4341-a706-959748e2260&title=&width=860)

注意：在mysql8之前，双竖线||也是可以完成字符串拼接的。但在mysql8之后，||只作为逻辑运算符，不能再进行字符串拼接了。

```sql

select 'abc' || 'def' || 'xyz';

```

mysql8之后，|| 只作为“或者”运算符，例如：找出工资高于3000或者低于900的员工姓名和薪资：

```sql

select ename, sal from emp where sal > 3000 || sal < 900;

```

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669780282134-d3a16d8a-e0fc-4744-beff-83b3579f6161.png#averageHue=%230f0f0e&clientId=u6210fc1e-5e54-4&from=paste&height=196&id=uc7e77230&originHeight=196&originWidth=950&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11249&status=done&style=shadow&taskId=u19693054-9222-4df2-899e-3ed69a01a71&title=&width=950)

mysql中可以使用+进行字符串的拼接吗？不可以，在mysql中+只作加法运算，在进行加法运算时，会将加号两边的数据尽最大的努力转换成数字再求和，如果无法转换成数字，最终运算结果通通是0

  

### 去除字符串前后空白trim

```sql

select concat(trim(' abc '), 'def');

```

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570023583-bcf0b431-c34c-486b-9ee0-e571ff3c158d.png#averageHue=%2310100f&clientId=u005f32df-cdfa-4&from=paste&height=204&id=u800e8929&originHeight=204&originWidth=715&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12536&status=done&style=shadow&taskId=uc6e946c5-bd11-4f08-83a5-34b7d5e1a78&title=&width=715)

默认是去除前后空白，也可以去除指定的前缀后缀，例如：

去除前置0

```sql

select trim(leading '0' from '000111000');

```

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570194415-8f78ced1-8f36-42d3-a829-b81fc4132c85.png#averageHue=%23121110&clientId=u005f32df-cdfa-4&from=paste&height=214&id=u54da0ae5&originHeight=214&originWidth=706&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12307&status=done&style=shadow&taskId=u4bd5c984-5076-4b41-936e-2cb2934e2a0&title=&width=706)

去除后置0

```sql

select trim(trailing '0' from '000111000');

```

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570218215-c862c7d8-1ee3-4066-8e25-055767efee61.png#averageHue=%2312100f&clientId=u005f32df-cdfa-4&from=paste&height=207&id=ud1b70c2d&originHeight=207&originWidth=704&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11888&status=done&style=shadow&taskId=u3680db7d-b909-4cfe-8636-aef9213b9cb&title=&width=704)

前置0和后置0全部去除

```sql

select trim(both '0' from '000111000');

```

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570238062-dff388d3-3106-457d-a9ae-819f41821792.png#averageHue=%2311100f&clientId=u005f32df-cdfa-4&from=paste&height=203&id=uca889e8f&originHeight=203&originWidth=678&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10559&status=done&style=shadow&taskId=u39829e4b-560a-42a1-b27c-315e566e9ae&title=&width=678)

  

## 数字相关

### rand()和rand(x)

rand()生成0到1的随机浮点数。

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669797997130-63b2c8d0-6169-4ee8-9b6b-c3087e9d733b.png#averageHue=%2311100f&clientId=u57006619-2538-4&from=paste&height=432&id=uc1af8ae1&originHeight=432&originWidth=488&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21196&status=done&style=shadow&taskId=uf2b4c16d-fc16-42a5-91c6-c840e24096b&title=&width=488)

rand(x)生成0到1的随机浮点数，通过指定整数x来确定每次获取到相同的浮点值。

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669798044104-7fc0b727-ff91-4d3e-be33-9954d556afe2.png#averageHue=%23121110&clientId=u57006619-2538-4&from=paste&height=431&id=uddf41de3&originHeight=431&originWidth=404&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23014&status=done&style=shadow&taskId=uc8b8c1f9-b44d-4886-8442-9c6d0e0beb7&title=&width=404)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669798069147-75492782-759d-46d9-84c5-a83b3a63594c.png#averageHue=%23121110&clientId=u57006619-2538-4&from=paste&height=431&id=ud22d346e&originHeight=431&originWidth=417&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21817&status=done&style=shadow&taskId=u01cf1b31-7d8b-4bc0-8eba-573138f7c49&title=&width=417)

### round(x)和round(x,y)四舍五入

round(x) 四舍五入，保留整数位，舍去所有小数

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669798450055-e26955bd-ea2d-445a-be98-721b54d3ca35.png#averageHue=%2311100f&clientId=u57006619-2538-4&from=paste&height=427&id=u633ac709&originHeight=427&originWidth=438&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19800&status=done&style=shadow&taskId=u5ae99c90-04bd-47b9-9338-3be2146f355&title=&width=438)

round(x,y) 四舍五入，保留y位小数

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669798534269-9c494800-7878-4ccf-bacc-a8c4cdafbbe6.png#averageHue=%23100f0e&clientId=u57006619-2538-4&from=paste&height=656&id=ub44adc1f&originHeight=656&originWidth=467&originalType=binary&ratio=1&rotation=0&showTitle=false&size=30665&status=done&style=shadow&taskId=u06d2a339-d070-4c04-9d62-a6ca361ad3c&title=&width=467)

  

### truncate(x, y)舍去

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669798594158-7e51e7a5-27af-4f7f-8021-a751f425a316.png#averageHue=%2311100f&clientId=u57006619-2538-4&from=paste&height=220&id=u7586a0cc&originHeight=220&originWidth=492&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10521&status=done&style=shadow&taskId=u4aea8b0c-2612-4b7c-af22-e5b68687b80&title=&width=492)

以上SQL表示保留两位小数，剩下的全部舍去。

### ceil与floor

数字处理函数除了以上的之外，还有ceil和floor函数：

  

- ceil函数：返回大于或等于数值x的最小整数

- floor函数：返回小于或等于数值x的最大整数

  

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672735932932-f0dfc7de-1f77-4eb0-b6e9-b6c6c2ce7ae3.png#averageHue=%23100f0e&clientId=uc0e8c595-6b95-4&from=paste&height=433&id=ua803b791&originHeight=433&originWidth=402&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13778&status=done&style=shadow&taskId=uf4127f6b-bfd8-454a-8aa8-2e1fec9edab&title=&width=402)

  

## 空处理

ifnull(x, y)，空处理函数，当x为NULL时，将x当做y处理。

ifnull(comm, 0)，表示如果员工的津贴是NULL时当做0处理。

在SQL语句中，凡是有NULL参与的数学运算，最终的计算结果都是NULL：

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669798864111-5cffd59f-d15c-4f6c-a2d8-0b623ec1f16c.png#averageHue=%23100f0e&clientId=u57006619-2538-4&from=paste&height=658&id=ue1cf6783&originHeight=658&originWidth=408&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23225&status=done&style=shadow&taskId=ua42e9e3c-fa93-4f6c-979d-d5444c21108&title=&width=408)

看这样一个需求：查询每个员工的年薪。（年薪 = (月薪 + 津贴) * 12个月。注意：有的员工津贴comm是NULL。）

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669798945415-90bccaa6-1dda-4ebd-bc50-63ab5ba2b89a.png#averageHue=%23100f0e&clientId=u57006619-2538-4&from=paste&height=573&id=u514525d4&originHeight=573&originWidth=850&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36066&status=done&style=shadow&taskId=ubb59ae71-c22d-456f-85bf-df0182998af&title=&width=850)

  

以上查询结果中显示SMITH等人的年薪是NULL，这是为什么，这是因为SMITH等人的津贴comm是NULL，有NULL参与的数学运算，最终结果都是NULL，显然这个需要空处理，此时就用到了ifnull函数：

![image.png](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669799067232-4896fa47-5c64-409a-b970-dddc31e06050.png#averageHue=%23100f0e&clientId=u57006619-2538-4&from=paste&height=573&id=u59b02703&originHeight=573&originWidth=982&originalType=binary&ratio=1&rotation=0&showTitle=false&size=42887&status=done&style=shadow&taskId=u063b2776-3482-4b4f-888c-3623426b77b&title=&width=982)

  

## 日期和时间相关函数

### 获取当前日期和时间

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672707310711-3115e4af-385c-4565-89c7-25bad76e8a6a.png#averageHue=%23121110&clientId=uc0e8c595-6b95-4&from=paste&height=162&id=uc379723b&originHeight=162&originWidth=404&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7211&status=done&style=shadow&taskId=uedf1c447-2a71-4f9a-9f96-98b9f249622&title=&width=404)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672707382021-d8d296b7-9d9a-4072-b714-c99da604ac12.png#averageHue=%23151312&clientId=uc0e8c595-6b95-4&from=paste&height=163&id=ua9b22a07&originHeight=163&originWidth=377&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8104&status=done&style=shadow&taskId=u0aa13932-ae31-46ba-94b7-f5cee861153&title=&width=377)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672707469394-4fe3f0fb-ca9e-4484-b939-db716f6ddd38.png#averageHue=%23131211&clientId=uc0e8c595-6b95-4&from=paste&height=168&id=ue97dcb2c&originHeight=168&originWidth=801&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12054&status=done&style=shadow&taskId=uf047d345-596d-4f3c-a996-3d1f6850219&title=&width=801)

now()和sysdate()的区别：

  

- now()：获取的是执行select语句的时刻。

- sysdate()：获取的是执行sysdate()函数的时刻。

  

### 获取当前日期

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672707770762-e9723219-562f-4a53-9d8a-9055ee80c25d.png#averageHue=%2311100f&clientId=uc0e8c595-6b95-4&from=paste&height=543&id=ufc58343c&originHeight=655&originWidth=440&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29141&status=done&style=shadow&taskId=u707d5711-bda8-4f35-89c5-f39da3e879f&title=&width=365)

获取当前日期有三种写法，掌握任意一种即可：

  

- curdate()

- current_date()

- current_date

  

### 获取当前时间

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672707856778-8eec2322-c3c8-4ddc-94c4-3e08eea430a8.png#averageHue=%23121010&clientId=uc0e8c595-6b95-4&from=paste&height=653&id=u57a306e4&originHeight=653&originWidth=430&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28651&status=done&style=shadow&taskId=ua03065f0-48bc-43c2-ae47-b77fab8249f&title=&width=430)

获取档期时间有三种写法，掌握其中一种即可：

  

- curtime()

- current_time()

- current_time

  

### 获取单独的年、月、日、时、分、秒

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672708190559-a1d93032-699d-49dc-87cc-4ccb045bee28.png#averageHue=%23100f0e&clientId=uc0e8c595-6b95-4&from=paste&height=651&id=u5badb85c&originHeight=651&originWidth=456&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28555&status=done&style=shadow&taskId=u742f8377-b4d8-44e9-950d-da020890e07&title=&width=456)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672708242288-89a20209-4ca2-4d1c-a1b0-5ad5f1179841.png#averageHue=%2311100f&clientId=uc0e8c595-6b95-4&from=paste&height=653&id=u7cfcb11b&originHeight=653&originWidth=483&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28868&status=done&style=shadow&taskId=u43769b4b-00e8-4dfb-a085-19858d725f1&title=&width=483)

注意：这些函数在使用的时候，需要传递一个日期参数给它，它可以获取到你给定的这个日期相关的年、月、日、时、分、秒的信息。

一次性提取一个给定日期的“年月日”部分，可以使用date()函数，例如：

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672713926559-d9c4257b-3536-4124-b4f4-3fd3626a293e.png#averageHue=%2311100f&clientId=uc0e8c595-6b95-4&from=paste&height=168&id=u161f961c&originHeight=168&originWidth=438&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7552&status=done&style=shadow&taskId=ub9643e54-a1b4-424f-a2d7-e15c7538b83&title=&width=438)

一次性提取一个给定日期的“时分秒”部分，可以使用time()函数，例如：

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672721340191-9c568184-73b5-4c26-9035-95245016ba4f.png#averageHue=%2311100f&clientId=uc0e8c595-6b95-4&from=paste&height=161&id=u0bb5bc88&originHeight=161&originWidth=428&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7598&status=done&style=shadow&taskId=u09037fc7-e074-481b-bf6a-ccc8fc49cf6&title=&width=428)

  

### date_add函数

date_add函数的作用：给指定的日期添加间隔的时间，从而得到一个新的日期。

date_add函数的语法格式：date_add(日期, interval expr 单位)，例如：

![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672709352877-e64de4c0-d776-4e30-908b-4a96c04bc186.png#averageHue=%23121110&clientId=uc0e8c595-6b95-4&from=paste&height=174&id=ub79687f8&originHeight=174&originWidth=771&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11929&status=done&style=shadow&taskId=u79db77b4-bf0f-41ee-91ba-e6e48424d32&title=&width=771)

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

  
