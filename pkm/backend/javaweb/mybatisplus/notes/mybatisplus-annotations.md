# MyBatis-Plus常用注解

---

## 实体类和表是如何对应的

在第一个`MyBatis-Plus`程序中可以看到，没有编写`Mapper xml`文件，仅仅只编写了`CarMapper`继承`BaseMapper`。那`MyBatis-Plus`底层是怎么让`实体类`和`表`对应起来的呢？原理如下：

`MyBatis-Plus`通过以下代码找到实体类`Car`：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744271336190-8eb901cc-9ca3-41ef-bd20-61086ffdb16d.png" width="556" title="" crop="0,0,1,1" id="ucd433b2d" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744271376349-0b925a4a-98d3-4dac-b8a4-a54b4c4f9675.png" width="347" title="" crop="0,0,1,1" id="u499e0ae2" class="ne-image" style="font-size: 16px">

**然后通过反射机制获取**`**Car**`**类的类名以及字段名，遵循**`****约定大于配置****`**的方式完成了**`**实体类**`**与**`**表**`**的对应，约定如下：**

+ **类名驼峰转下划线作为表名，例如：类名**`**UserInfo**`**，对应的表名**`**user_info**`
+ **自动将名字为**`**id**`**的字段作为主键**
+ **属性名驼峰转下划线作为字段名，例如：属性名**`**carType**`**，对应的字段名**`**car_type**`

**如果不符合约定就需要自己通过注解的方式来指定表名和字段名。**

---

## 常用注解

+ @TableName：指定表名的
+ @TableId：指定主键字段信息
+ @TableField：指定普通字段信息

这几个注解是比较常用的，还有一些其他注解，如果需要可以查一下官方文档：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744275406202-6c783a7a-71fe-48fd-b645-0485781c7d93.png" width="1563" title="" crop="0,0,1,1" id="u077fef2a" class="ne-image" style="font-size: 16px">

### @TableName

当`实体类名`和`表名`不符合mp的约定，此时就可以使用该注解来解决了，例如实体类名为`Car`，但是表名为`t_car`，则需要使用该注解：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744272072569-06b3b3c3-f08e-4244-962f-fd586c41d2d6.png" width="328" title="" crop="0,0,1,1" id="u1df7034b" class="ne-image" style="font-size: 16px">

### @TableId

**用该注解的原因：**

+ **默认约定**：**该注解用于标记实体类中的主键字段。如果你的主键字段名为 id，你可以省略这个注解。******（数据库表的主键字段名是 id，实体类的属性名恰好也是 id，该注解可以省略）****
+ **官方建议**：只要你属性名不是 `id`，最好都使用上 `@TableId`注解（**即使属性名和字段名能对应上，写上起码可读性强，而且还可以指定主键生成策略**）。

**使用方法：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744272770437-2b50b6b3-7f38-49dd-b0d0-b96dce60684e.png" width="446" title="" crop="0,0,1,1" id="u599fecde" class="ne-image" style="font-size: 16px">

+ value 属性用来指定表的主键名
+ type 属性用来指定主键的生成策略，如果数据库表中主键值是`auto_increment`，则采用`type = IdType.AUTO`。

**主键生成策略：**

+ IdType.AUTO：数据库自增（需数据库支持）。
+ IdType.ASSIGN_ID：雪花算法生成分布式ID（默认策略），这是mp自己提供的，底层调用了`IdentifierGenerator`接口的`nextId()`方法，实现类是`DefaultIdentifierGenerator`，雪花算法实现的（****雪花算法是一种分布式ID生成算法，通过组合********时间戳、机器ID和序列号********生成全局唯一、趋势递增的64位ID。占 8 个字节，********时钟回拨********或********机器 ID 全局不唯一********可能会导致 id 重复，但概率较低****）。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744273213286-e4f3cf01-59ec-46e6-a9ab-2019f8e5e8ec.png" width="488" title="" crop="0,0,1,1" id="u94e15b31" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744273262895-d9e37364-59fe-4caf-b0cc-5a0262cbc1a8.png" width="736" title="" crop="0,0,1,1" id="u87fd527e" class="ne-image" style="font-size: 16px">

+ IdType.INPUT：需要程序员手动赋值。

以上是比较常用的主键生成策略。

### @TableField

```sql

drop table if exists t_customer;
create table t_customer(
  id bigint primary key auto_increment,
  username varchar(255),
  is_vip varchar(255),
  `desc` varchar(255)
);

```

**什么情况下需要使用该注解：**

+ `属性名`和`字段名`不一致。
+ `属性名`以`is`开头，并且是布尔类型。（****>=3.4.0版本的MyBatis-Plus已经对is开头的属性名进行了处理。无需添加这个注解。****）
+ `属性名`与数据库中的关键字冲突了。
+ `属性名`不是数据库表中的字段。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744274649300-1aa69362-cc41-4b52-b173-bbd5dafd9fcb.png" width="596" title="" crop="0,0,1,1" id="u22f7c694" class="ne-image" style="font-size: 16px">
