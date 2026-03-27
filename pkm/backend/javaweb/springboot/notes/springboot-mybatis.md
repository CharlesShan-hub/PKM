# 整合持久层框架MyBatis

---

## 准备数据库表及数据

创建数据库：springboot

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729050319150-d942131f-2eb9-4baa-870f-3d15f4cd7479.png" width="310" title="" crop="0,0,1,1" id="u96bd303f" class="ne-image">

使用IDEA工具自带的mysql插件来完成表的创建和数据的准备：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729050185616-731cbd39-267f-45e1-81f3-1f07d621c514.png" width="753" title="" crop="0,0,1,1" id="u5727ecb3" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729050390076-57de6c2a-36c7-402f-8bc3-e4e4cb0d50f3.png" width="798" title="" crop="0,0,1,1" id="u243b2e94" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729050451224-c17b4676-0020-418d-80f9-f24738427fc6.png" width="679" title="" crop="0,0,1,1" id="u12ebecda" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729051111940-4a591196-a5d9-48c2-83b7-94d858595561.png" width="1024" title="" crop="0,0,1,1" id="u5de3bb4f" class="ne-image">

表创建成功后，为表准备数据，如下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729051234644-3deae02b-9aec-4017-8dbc-5f3337c5c179.png" width="728" title="" crop="0,0,1,1" id="uab8611e9" class="ne-image">

**或者直接执行 SQL 脚本：**

```sql
drop table if exists t_vip;
create table t_vip(
  id bigint primary key auto_increment,
  name varchar(255),
  card_number varchar(255),
  birth char(10)
);
insert into t_vip(name,card_number,birth) values('张三', '1234567890', '1980-11-10');
insert into t_vip(name,card_number,birth) values('李四', '1234567891', '1980-11-11');
select * from t_vip;
```

---

## 创建SpringBoot项目

使用脚手架创建Spring Boot项目

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764859671173-a0a919e2-3fbf-4d5c-9ca7-d6f6d844011f.png" width="721.6" title="" crop="0,0,1,1" id="u4d246a7c" class="ne-image">

引入mysql驱动以及mybatis的启动器

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729049442355-3e02c359-f9a7-4afb-93ec-0a314475c882.png" width="959" title="" crop="0,0,1,1" id="u53aac1e8" class="ne-image">

依赖如下：

```xml
<!--mybatis的启动器-->
<dependency>
    <groupId>org.mybatis.spring.boot</groupId>
    <artifactId>mybatis-spring-boot-starter</artifactId>
    <version>3.0.3</version>
</dependency>
<!--mysql的驱动依赖-->
<dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
    <scope>runtime</scope>
</dependency>
```

**注意，之前也提到过：**

+ **Spring Boot官方提供的启动器的名字规则：spring-boot-starter-xxx**
+ **第三方（非Spring Boot官方）提供的启动器的名字规则：xxx-spring-boot-starter**

---

## 编写数据源配置

前面提到过，Spring Boot配置统一可以编写到application.properties中，配置如下：

```properties
