# Mybatis Introduction

---
## 资料

* 黑马mybatis教程: https://www.bilibili.com/video/BV1MT4y1k7wZ
* 动力节点: https://www.bilibili.com/video/BV1JP4y1Z73S
* 官网: https://mybatis.org/mybatis-3/zh_CN/index.html
* github:  https://github.com/mybatis/mybatis-3
* 中文文档: https://mybatis.net.cn/
* 语雀文档: https://www.yuque.com/dujubin/ltckqu/pozck9
* 大佬笔记: https://blog.csdn.net/m0_53022813/article/details/128563832
* MyBatis 是一个 ​**​Java 持久层框架​**​，它通过 XML 或注解将 SQL 与 Java 对象映射，避免了传统 JDBC 的复杂代码。

---
## 概述

### 框架

> 什么是框架
> 一句话总结，框架就是提前写好了一堆接口和类

- 在文献中看到的framework被翻译为框架
- Java常用框架：
	- SSM三大框架：Spring + SpringMVC + MyBatis
	- SpringBoot
	- SpringCloud
	- 等。。
- 框架其实就是对通用代码的封装，提前写好了一堆接口和类，我们可以在做项目的时候直接引入这些接口和类（引入框架），基于这些现有的接口和类进行开发，可以大大提高开发效率。
- 框架一般都以jar包的形式存在。(jar包中有class文件以及各种配置文件等。)
- SSM三大框架的学习顺序：MyBatis、Spring、SpringMVC（仅仅是建议）

### 三层架构

> 现在所有项目都是分层的，表现层、业务逻辑层、数据访问层。其中 MyBatis 就是数据访问层的框架之一。

- **表现层（UI）**：直接跟前端打交互（一是接收前端ajax请求，二是返回json数据给前端）
- **业务逻辑层（BLL）**：一是处理表现层转发过来的前端请求（也就是具体业务），二是将从持久层获取的数据返回到表现层。
- **数据访问层/持久层（DAL）**：直接操作数据库完成CRUD，并将获得的数据返回到上一层（也就是业务逻辑层）。
- Java持久层框架：
	- MyBatis
	- Hibernate（实现了JPA规范）
	- jOOQ
	- Guzz
	- Spring Data（实现了JPA规范）
	- ActiveJDBC
	- ......

### JDBC不足

缺点一：现在sql语句写死在java程序中。假如现在数据表发生改变，我需要重写 sql 语句，这就需要修改 java 代码，重新编译测试部署，这就违背了 OCP 原则。

```java
// ......
// sql语句写死在java程序中
String sql = "insert into t_user(id,idCard,username,password,birth,gender,email,city,street,zipcode,phone,grade) values(?,?,?,?,?,?,?,?,?,?,?,?)";
PreparedStatement ps = conn.prepareStatement(sql);
// 繁琐的赋值：思考一下，这种有规律的代码能不能通过反射机制来做自动化。
ps.setString(1, "1");
ps.setString(2, "123456789");
ps.setString(3, "zhangsan");
ps.setString(4, "123456");
ps.setString(5, "1980-10-11");
ps.setString(6, "男");
ps.setString(7, "zhangsan@126.com");
ps.setString(8, "北京");
ps.setString(9, "大兴区凉水河二街");
ps.setString(10, "1000000");
ps.setString(11, "16398574152");
ps.setString(12, "A");
// 执行SQL
int count = ps.executeUpdate();
// ......
```

缺点二：需要不停的new 对象，不停的 set，十分的繁琐。

```java
// ......
// sql语句写死在java程序中
String sql = "select id,idCard,username,password,birth,gender,email,city,street,zipcode,phone,grade from t_user";
PreparedStatement ps = conn.prepareStatement(sql);
ResultSet rs = ps.executeQuery();
List<User> userList = new ArrayList<>();
// 思考以下循环中的所有代码是否可以使用反射进行自动化封装。
while(rs.next()){
    // 获取数据
    String id = rs.getString("id");
    String idCard = rs.getString("idCard");
    String username = rs.getString("username");
    String password = rs.getString("password");
    String birth = rs.getString("birth");
    String gender = rs.getString("gender");
    String email = rs.getString("email");
    String city = rs.getString("city");
    String street = rs.getString("street");
    String zipcode = rs.getString("zipcode");
    String phone = rs.getString("phone");
    String grade = rs.getString("grade");
    // 创建对象
    User user = new User();
    // 给对象属性赋值
    user.setId(id);
    user.setIdCard(idCard);
    user.setUsername(username);
    user.setPassword(password);
    user.setBirth(birth);
    user.setGender(gender);
    user.setEmail(email);
    user.setCity(city);
    user.setStreet(street);
    user.setZipcode(zipcode);
    user.setPhone(phone);
    user.setGrade(grade);
    // 添加到集合
    userList.add(user);
}
// ......
```

### 了解 MyBatis

https://github.com/mybatis/mybatis-3

* MyBatis本质上就是对JDBC的封装，通过MyBatis完成CRUD。
* MyBatis在三层架构中负责持久层的，属于持久层框架。
- MyBatis的发展历程：【引用百度百科】
	- MyBatis本是apache的一个开源项目iBatis，2010年这个项目由apache software foundation迁移到了google code，并且改名为MyBatis。2013年11月迁移到Github。
	- iBATIS一词来源于“internet”和“abatis”的组合，是一个基于Java的持久层框架。iBATIS提供的持久层框架包括SQL Maps和Data Access Objects（DAOs）。
- 打开mybatis代码可以看到它的包结构中包含：ibatis
- ORM：对象关系映射
	- **O**（Object）：Java虚拟机中的Java对象
	- **R**（Relational）：关系型数据库
	- **M**（Mapping）：将Java虚拟机中的Java对象映射到数据库表中一行记录，或是将数据库表中一行记录映射成Java虚拟机中的一个Java对象。
	- MyBatis属于半自动化ORM框架。也需要编写 sql 语句。
	- Hibernate属于全自动化的ORM框架。不需要编写 sql 语句。
* 对应关系：java 程序和数据库彼此会有一些对应关系，java 对象和数据库表之间的互相转换就是 Mapping

	| java | 数据库 |
	| ---- | --- |
	| 类    | 数据表 |
	| 对象   | 数据行 |
	| 属性   | 字段  |

* MyBatis框架特点：
	- 支持定制化 SQL、存储过程、基本映射以及高级映射
	- 避免了几乎所有的 JDBC 代码中手动设置参数以及获取结果集
	- 支持XML开发，也支持注解式开发。【为了保证sql语句的灵活，所以mybatis大部分是采用XML方式开发。】
	- 将接口和 Java 的 POJOs(Plain Ordinary Java Object，简单普通的Java对象)映射成数据库中的记录
	- 体积小好学：两个jar包，两个XML配置文件。
	- 完全做到sql解耦合。
	- 提供了基本映射标签。
	- 提供了高级映射标签。
	- 提供了XML标签，支持动态SQL的编写。
	- ......

---
## mybatis 案例
### 数据准备

```sql
-- =============================================
-- 创建汽车信息数据库和表
-- 数据库名: car_info
-- 表名: car_info
-- =============================================

-- 1. 删除旧数据库（如果存在）
DROP DATABASE IF EXISTS car_info;

-- 2. 创建数据库（使用utf8mb4字符集）
CREATE DATABASE car_info 
DEFAULT CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- 3. 使用数据库
USE car_info;

-- 4. 创建表
CREATE TABLE IF NOT EXISTS `car_info` (
  `id` BIGINT NOT NULL AUTO_INCREMENT COMMENT '自然主键，和业务没有关系，自增',
  `car_num` VARCHAR(255) COMMENT '汽车编号',
  `brand` VARCHAR(255) COMMENT '汽车品牌',
  `guide_price` DECIMAL(10,2) COMMENT '厂商指导价',
  `produce_time` CHAR(10) COMMENT '生产日期',
  `car_type` VARCHAR(255) COMMENT '汽车类型：燃油车，新能源等',
  `create_time` DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  INDEX `idx_car_num` (`car_num`) COMMENT '汽车编号索引',
  INDEX `idx_brand` (`brand`) COMMENT '汽车品牌索引'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='汽车信息表';

-- 5. 插入测试数据
INSERT INTO `car_info` (`car_num`, `brand`, `guide_price`, `produce_time`, `car_type`) VALUES
('京A12345', '奔驰', 420000.00, '2023-05-01', '燃油车'),
('沪B23456', '特斯拉', 289900.00, '2023-06-15', '新能源'),
('粤C34567', '宝马', 385000.00, '2023-04-20', '燃油车'),
('浙D45678', '比亚迪', 209800.00, '2023-07-10', '新能源'),
('苏E56789', '奥迪', 318000.00, '2023-03-05', '燃油车');

-- 6. 验证数据
SELECT '=== 汽车信息表数据 ===' AS '';
SELECT * FROM `car_info`;

-- 7. 显示表结构
SELECT '=== 表结构 ===' AS '';
DESCRIBE `car_info`;
```

假设上边的文件保存成`init.sql`
那么首先进入 mysql 命令行模式，然后运行source命令
```shell
mysql> source /home/charles/project/learn_java/mybatis/introduction/src/resources/init.sql
```

### 依赖配置

pom.xml

```xml
<dependencies>
    <!--mybatis依赖-->
    <dependency>
        <groupId>org.mybatis</groupId>
        <artifactId>mybatis</artifactId>
        <version>3.5.17</version>
    </dependency>
    <!--mysql驱动依赖-->
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <version>8.0.30</version>
    </dependency>
</dependencies>
```

resources/mybatis-config.xml（约定俗成）一个工程就一个

* resources目录：放在这个目录当中的，一般都是资源文件，配置文件。直接放到resources目录下的资源，等同于放到了类的根路径下。

注意1：mybatis核心配置文件的文件名不一定是mybatis-config.xml，可以是其它名字。
注意2：mybatis核心配置文件存放的位置也可以随意。这里选择放在resources根下，相当于放到了类的根路径下。

```XML
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <environments default="development">
        <environment id="development">
            <transactionManager type="JDBC"/>
            <dataSource type="POOLED">
                <property name="driver" value="com.mysql.cj.jdbc.Driver"/>
                <property name="url" value="jdbc:mysql://localhost:3306/car_info"/>
                <property name="username" value="root"/>
                <property name="password" value="123456"/>
            </dataSource>
        </environment>
    </environments>
    <mappers>
        <!--resources会从根目录查找文件，所以直接写Carapper.xml就行了--> 
        <mapper resource="CarMapper.xml"/>
    </mappers>
</configuration>
```

resources/CarMapper.xml，一个表写一个

在这个配置文件当中编写SQL语句。这个文件名也不是固定的，放的位置也不是固定，我们这里给它起个名字，叫做：CarMapper.xml 把它暂时放到类的根路径下。

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<!--namespace先随意写一个-->
<mapper namespace="car">
    <!--insert sql：保存一个汽车信息-->
    <insert id="insertCar">
        insert into car_info
            (id,car_num,brand,guide_price,produce_time,car_type) 
        values
            (null,'京A00001,'丰田mirai',40.30,'2014-10-05','氢能源')
    </insert>
</mapper>
```


### 具体代码

* 在MyBatis当中，**负责执行SQL语句的那个对象**叫做什么呢？**SqlSession**。SqlSession是专门用来执行SQL语句的，**是一个Java程序和数据库之间的一次会话**。要想获取SqlSession对象，需要先获取SqlSessionFactory对象，通过SqlSessionFactory工厂来生产SqlSession对象。
* 怎么获取SqlSessionFactory对象呢？需要首先获取SqlSessionFactoryBuilder对象。通过SqlSessionFactoryBuilder对象的build方法，来获取一个SqlSessionFactory对象。
* mybatis的核心对象包括：
        SqlSessionFactoryBuilder
        SqlSessionFactory
        SqlSession
* SqlSessionFactoryBuilder --> SqlSessionFactory --> SqlSession

```java
package com.powernode.mybatis.test;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.FileInputStream;
import java.io.InputStream;

public class MyBatisIntroductionTest {
    public static void main(String[] args) throws Exception {

        // 获取SqlSessionFactoryBuilder对象
        SqlSessionFactoryBuilder sqlSessionFactoryBuilder = new SqlSessionFactoryBuilder();

        // 获取SqlSessionFactory对象
        InputStream is = Resources.getResourceAsStream("mybatis-config.xml"); // Resources.getResourceAsStream默认就是从类的根路径下开始查找资源。
        //InputStream is = Resources.getResourceAsStream("com/mybatis.xml");
        //InputStream is = new FileInputStream("d:\\mybatis-config.xml");

        //InputStream is = ClassLoader.getSystemClassLoader().getResourceAsStream("mybatis-config.xml");
        SqlSessionFactory sqlSessionFactory = sqlSessionFactoryBuilder.build(is); // 一般情况下都是一个数据库对应一个SqlSessionFactory对象。

        // 获取SqlSession对象
        SqlSession sqlSession = sqlSessionFactory.openSession(); // 如果使用的事务管理器是JDBC的话，底层实际上会执行：conn.setAutoCommit(false);
        // 这种方式实际上是不建议的，因为没有开启事务。
        //SqlSession sqlSession = sqlSessionFactory.openSession(true);

        // 执行SQL语句
        int count = sqlSession.insert("insertCar"); // 返回值是影响数据库表当中的记录条数。

        System.out.println("插入了几条记录：" + count);

        // 手动提交
        sqlSession.commit(); // 如果使用的事务管理器是JDBC的话，底层实际上还是会执行conn.commit();

    }
}
```

我们加载配置文件的时候也可以使用`InputStream is = new FileInputStream("d:\\mybatis-config.xml");`，但是这样可移植性不好。

我们使用的`InputStream is = Resources.getResourceAsStream("mybatis-config.xml");`,底层的源代码其实就是：`InputStream is = ClassLoader.getSystemClassLoader().getResourceAsStream("mybatis-config.xml");`


```java
package com.powernode.mybatis.test;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

/**
 * 采用正规的方式，写一个完整版的MyBatis程序。
 * @author 动力节点
 * @version 1.0
 * @since 1.0
 */
public class MyBatisCompleteTest {
    public static void main(String[] args) {
        SqlSession sqlSession = null;
        try {
            SqlSessionFactoryBuilder sqlSessionFactoryBuilder = new SqlSessionFactoryBuilder();
            SqlSessionFactory sqlSessionFactory = sqlSessionFactoryBuilder.build(Resources.getResourceAsStream("mybatis-config.xml"));
            // 开启会话（底层会开启事务）
            sqlSession = sqlSessionFactory.openSession();
            // 执行SQL语句，处理相关业务
            int count = sqlSession.insert("insertCar");
            System.out.println(count);
            // 执行到这里，没有发生任何异常，提交事务。终止事务。
            sqlSession.commit();
        } catch (Exception e) {
            // 最好回滚事务
            if (sqlSession != null) {
                sqlSession.rollback();
            }
            e.printStackTrace();
        } finally {
            // 关闭会话（释放资源）
            if (sqlSession != null) {
                sqlSession.close();
            }
        }
    }
}
```

### mybatis 的事务管理机制

* 在mybatis-config.xml文件中，可以通过以下的配置进行mybatis的事务管理
	`<transactionManager type="JDBC"/>`
* type属性的值包括两个：
	JDBC(jdbc)
	MANAGED(managed)
	type后面的值，只有以上两个值可选，不区分大小写。
* 在mybatis中提供了两种事务管理机制：
	第一种：JDBC事务管理器
	第二种：MANAGED事务管理器
* JDBC事务管理器：
	mybatis框架自己管理事务，自己采用原生的JDBC代码去管理事务：
		conn.setAutoCommit(false); 开启事务。
		....业务处理...
		conn.commit(); 手动提交事务
	使用JDBC事务管理器的话，底层创建的事务管理器对象：JdbcTransaction对象。

	如果你编写的代码是下面的代码：
		`SqlSession sqlSession = sqlSessionFactory.openSession(true);`
		表示没有开启事务。因为这种方式压根不会执行：conn.setAutoCommit(false);
		在JDBC事务中，没有执行conn.setAutoCommit(false);那么autoCommit就是true。
		如果autoCommit是true，就表示没有开启事务。只要执行任意一条DML语句就提交一次。

* MANAGED事务管理器：
	mybatis不再负责事务的管理了。事务管理交给其它容器来负责。例如：spring。
	我不管事务了，你来负责吧。

	对于我们当前的单纯的只有mybatis的情况下，如果配置为：MANAGED
	那么事务这块是没人管的。没有人管理事务表示事务压根没有开启。

	没有人管理事务就是没有事务。

* JDBC中的事务：
	如果你没有在JDBC代码中执行：`conn.setAutoCommit(false);`的话，默认的autoCommit是true。

* 重点：
	以后注意了，**只要你的autoCommit是true，就表示没有开启事务**。
	**只有你的autoCommit是false的时候，就表示开启了事务**。


---
## springboot+mybatis 案例

### 数据准备
```sql
-- =============================================
-- 创建数据库和用户表（MyBatis 快速入门示例）
-- 数据库名: mybatis_demo
-- 表名: user
-- =============================================

-- 1. 删除旧数据库（如果存在）
DROP DATABASE IF EXISTS mybatis_demo;

-- 2. 创建数据库（使用utf8mb4字符集）
CREATE DATABASE mybatis_demo 
DEFAULT CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- 3. 使用数据库
USE mybatis_demo;

-- 4. 创建用户表
CREATE TABLE IF NOT EXISTS `user` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `name` VARCHAR(50) NOT NULL COMMENT '用户名',
  `age` INT DEFAULT NULL COMMENT '年龄',
  `email` VARCHAR(100) DEFAULT NULL COMMENT '邮箱',
  `create_time` DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  INDEX `idx_name` (`name`) COMMENT '用户名索引'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';

-- 5. 插入测试数据
INSERT INTO `user` (`name`, `age`, `email`) VALUES
('张三', 25, 'zhangsan@example.com'),
('李四', 30, 'lisi@example.com'),
('王五', 28, 'wangwu@example.com'),
('赵六', 35, 'zhaoliu@example.com'),
('钱七', 22, 'qianqi@example.com');

-- 6. 验证数据
SELECT '=== 用户表数据 ===' AS '';
SELECT * FROM `user`;

-- 7. 显示表结构
SELECT '=== 表结构 ===' AS '';
DESCRIBE `user`;
```

假设上边的文件保存成`init.sql`
那么首先进入 mysql 命令行模式，然后运行source命令
```shell
mysql> source /home/charles/project/test/mybatis_demo/init.sql
```

### 依赖配置

本案例演示的是 springboot+mybatis。首先是 maven 的 pom.xml，加入 mysql 和 mybatis 的依赖，注意要加入`org.mybatis.spring.boot`！
```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.30</version>
</dependency>

<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis</artifactId>
    <version>3.5.17</version>
</dependency>

<dependency>
    <groupId>org.mybatis.spring.boot</groupId>
    <artifactId>mybatis-spring-boot-starter</artifactId>
    <version>3.0.3</version>
</dependency>
```

然后要创建 mybatis 自己的配置文件`mybatis-config.xml`，但是我们是 springboot 项目，所以换一个方式，直接在`application.yaml`配置就可以了。
```YAML
server:
  port: 8080

spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mybatis_demo
    username: root
    password: 123456
    driver-class-name: com.mysql.cj.jdbc.Driver

mybatis:
  mapper-locations: classpath:mapper/*.xml
  configuration:
    map-underscore-to-camel-case: true
```

对应的还要每一个 mapper 写一个xml
```XML
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "https://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.charlesshan.helloworld.mapper.UserMapper">
    <select id="selectAllUsers" resultType="com.charlesshan.helloworld.entity.User">
        select * from user;
    </select>
</mapper>
```

### 具体代码

Contorller：`HelloController.java`
```Java
package com.charlesshan.helloworld.controller;

import com.charlesshan.helloworld.entity.User;
import com.charlesshan.helloworld.mapper.UserMapper;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class HelloController {
    private final UserMapper userMapper;
    public HelloController(UserMapper userMapper) {
        this.userMapper = userMapper;
    }

    @GetMapping("/users")
    public List<User> selectAllUsers() {
        return userMapper.selectAllUsers();
    }
}
```

实体类：`User.java`
```Java
package com.charlesshan.helloworld.entity;

import java.util.Date;
import lombok.Data;

@Data
public class User {
    private Integer id;
    private String name;
    private Integer age;
    private String email;
    private Date createTime;
    private Date updateTime;
}
```

Mapper，用来连接 mybatis：`UserMapper.java`
```Java
package com.charlesshan.helloworld.mapper;

import com.charlesshan.helloworld.entity.User;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface UserMapper {
    List<User> selectAllUsers();
}
```

最后注意入口程序，需要用 MapperScan 指定 Mapper
```Java
package com.charlesshan.helloworld;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.charlesshan.helloworld.mapper")
public class HelloWorldApplication {
    public static void main(String[] args) {
        SpringApplication.run(HelloWorldApplication.class, args);
    }
}
```

访问http://localhost:8080/users，就可以得到
```json
[{"id":1,"name":"张三","age":25,"email":"zhangsan@example.com","createTime":"2025-07-01T11:51:18.000+00:00","updateTime":"2025-07-01T11:51:18.000+00:00"},{"id":2,"name":"李四","age":30,"email":"lisi@example.com","createTime":"2025-07-01T11:51:18.000+00:00","updateTime":"2025-07-01T11:51:18.000+00:00"},{"id":3,"name":"王五","age":28,"email":"wangwu@example.com","createTime":"2025-07-01T11:51:18.000+00:00","updateTime":"2025-07-01T11:51:18.000+00:00"},{"id":4,"name":"赵六","age":35,"email":"zhaoliu@example.com","createTime":"2025-07-01T11:51:18.000+00:00","updateTime":"2025-07-01T11:51:18.000+00:00"},{"id":5,"name":"钱七","age":22,"email":"qianqi@example.com","createTime":"2025-07-01T11:51:18.000+00:00","updateTime":"2025-07-01T11:51:18.000+00:00"}]
```

## 集成

### 集成Junit

pom.xml
```xml
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.13.2</version>
    <scope>test</scope>
</dependency>
```

以后我们的测试就都放在 test 里边了

```java
package com.charlesshan;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import org.junit.Test;

import java.io.InputStream;

public class CarMapperTest {
    @Test
    public void testCarMapper() {
        // 1. 创建SqlSessionFactoryBuilder对象
        SqlSessionFactoryBuilder sqlSessionFactoryBuilder = new SqlSessionFactoryBuilder();
        // 2. 创建SqlSessionFactory对象
        InputStream is = Thread.currentThread().getContextClassLoader().getResourceAsStream("mybatis-config.xml");
        SqlSessionFactory sqlSessionFactory = sqlSessionFactoryBuilder.build(is);
        // 3. 创建SqlSession对象
        SqlSession sqlSession = sqlSessionFactory.openSession();
        // 4. 执行sql
        int count = sqlSession.insert("insertCar"); // 这个"insertCar"必须是sql的id
        System.out.println("插入几条数据：" + count);
        // 5. 提交（mybatis默认采用的事务管理器是JDBC，默认是不提交的，需要手动提交。）
        sqlSession.commit();
        // 6. 关闭资源（只关闭是不会提交的）
        sqlSession.close();
    }
}
```

### 集成日志-logback

> https://mybatis.net.cn/configuration.html

 - 引入日志框架的目的是为了看清楚mybatis执行的具体sql。
 - mybatis常见的集成的日志组件有哪些呢？
        SLF4J（沙拉风）：沙拉风是一个日志标准，其中有一个框架叫做logback，它实现了沙拉风规范。
        LOG4J
        LOG4J2
        STDOUT_LOGGING
        ....
        注意：log4j log4j2 logback都是同一个作者开发的。
* mybatis支持的配置：SLF4J | LOG4J | LOG4J2 | JDK_LOGGING | COMMONS_LOGGING | STDOUT_LOGGING | NO_LOGGING。STDOUT_LOGGING是标准
 - 启用标准日志组件，只需要在`mybatis-config.xml`文件中添加以下配置：【可参考mybatis手册】

```xml
<settings>
  <setting name="logImpl" value="STDOUT_LOGGING" />
</settings>
```

* 这个标签在编写的时候要注意，它应该出现在environments标签之前。注意顺序。当然，不需要记忆这个顺序。因为有dtd文件进行约束呢。我们只要参考dtd约束即可。
* 集成logback日志框架。
        logback日志框架实现了slf4j标准。(沙拉风：日志门面。日志标准。)
        第一步：引入logback的依赖。(如下)
        第二步：引入logback所必须的xml配置文件。
            这个配置文件的名字必须叫做：logback.xml或者logback-test.xml，不能是其它的名字。
            这个配置文件必须放到类的根路径下。不能是其他位置。
            主要配置日志输出相关的级别以及日志具体的格式。

pom.xml
```xml
<!--引入logback的依赖，这个日志框架实现了slf4j规范-->
<dependency>
	<groupId>ch.qos.logback</groupId>
	<artifactId>logback-classic</artifactId>
	<version>1.2.11</version>
</dependency>
```

src/main/resources/logback.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>

<configuration debug="false">
    <!-- 控制台输出 -->
    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder">
            <!--格式化输出：%d表示日期，%thread表示线程名，%-5level：级别从左显示5个字符宽度%msg：日志消息，%n是换行符-->
            <pattern>[%thread] %-5level %logger{50} - %msg%n</pattern>
        </encoder>
    </appender>

    <!--mybatis log configure-->
    <logger name="com.apache.ibatis" level="TRACE"/>
    <logger name="java.sql.Connection" level="DEBUG"/>
    <logger name="java.sql.Statement" level="DEBUG"/>
    <logger name="java.sql.PreparedStatement" level="DEBUG"/>

    <!-- 日志输出级别,logback日志级别包括五个：TRACE < DEBUG < INFO < WARN < ERROR -->
    <root level="DEBUG">
        <appender-ref ref="STDOUT"/>
        <appender-ref ref="FILE"/>
    </root>

</configuration>
```