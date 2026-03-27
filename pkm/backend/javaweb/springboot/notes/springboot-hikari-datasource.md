# spring.datasource.type=com.zaxxer.hikari.HikariDataSource # 无需指定，springboot默认就是使用这个连接池。

spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/springboot
spring.datasource.username=root
spring.datasource.password=123456

```

以上的配置属于连接池的配置，连接池使用的是Spring Boot默认的连接池：HikariCP

---

## 编写实体类Vip

表`t_vip`中的字段分别是：

+ id
+ name
+ card_number
+ birth

对应实体类`Vip`中的属性名分别是：

+ Long id;
+ String name;
+ String cardNumber;
+ String birth;

创建包 entity，在该包下新建Vip类，代码如下：

```java

package com.jkweilai.sb305springbootmybatis.entity;

public class Vip {
    private Long id;
    private String name;
    private String cardNumber;
    private String birth;

    public Vip() {
    }

    public Vip(Long id, String name, String cardNumber, String birth) {
        this.id = id;
        this.name = name;
        this.cardNumber = cardNumber;
        this.birth = birth;
    }

    public Vip(String name, String cardNumber, String birth) {
        this.name = name;
        this.cardNumber = cardNumber;
        this.birth = birth;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCardNumber() {
        return cardNumber;
    }

    public void setCardNumber(String cardNumber) {
        this.cardNumber = cardNumber;
    }

    public String getBirth() {
        return birth;
    }

    public void setBirth(String birth) {
        this.birth = birth;
    }

    @Override
    public String toString() {
        return "Vip{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", cardNumber='" + cardNumber + '\'' +
                ", birth='" + birth + '\'' +
                '}';
    }
}

```

以上代码可以使用第三方库Lombok进行改造，后面再说。

---

## 编写Mapper接口

创建`repository`包，在该包下新建`VipMapper`接口，代码如下：

```java

package com.jkweilai.sb305springbootmybatis.repository;

import com.jkweilai.sb305springbootmybatis.entity.Vip;

import java.util.List;

public interface VipMapper {
    /**
     * 插入会员信息
     * @param vip
     * @return 1表示插入成功，其他值表示失败
     */
    int insert(Vip vip);

    /**
     * 根据id删除会员信息
     * @param id 会员唯一标识
     * @return 1表示删除成功，其他值表示失败
     */
    int deleteById(Long id);

    /**
     * 更新会员信息（id不可更新）
     * @param vip 会员信息
     * @return 1表示更新成功，其他值表示更新失败。
     */
    int update(Vip vip);

    /**
     * 根据id查询会员信息
     * @param id 会员的唯一标识
     * @return 会员信息
     */
    Vip selectById(Long id);

    /**
     * 获取所有会员信息
     * @return
     */
    List<Vip> selectAll();
}

```

---

## 编写Mapper接口的XML配置文件

在`resources`目录下新建`mapper`目录，将来的`mapper.xml`配置文件放在这个目录下。

安装`MyBatisX`插件，该插件可以根据我们编写的`VipMapper`接口自动生成mapper的XML配置文件。

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729132285817-67182b8c-487e-4ef5-b061-da4b12174489.png" width="978" title="" crop="0,0,1,1" id="u1321ec4b" class="ne-image">

然后在`VipMapper`接口上：alt+enter

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764860020514-4b4abe00-5f98-4e8b-aa21-d642310a0b8e.png" width="544.8" title="" crop="0,0,1,1" id="u18680716" class="ne-image">

生成`mapper of xml`：需要选择一个生成的位置

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729132515796-a056a2c3-e464-4c6e-bf8c-c1a876e36b80.png" width="420" title="" crop="0,0,1,1" id="ub40b00fd" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729132546447-714f679f-9b8c-4482-9e8d-d1c7e525a3c5.png" width="247" title="" crop="0,0,1,1" id="uc0fb6b93" class="ne-image">

接下来，你会看到Mapper接口中方法报错了，可以在错误的位置上使用`alt+enter`，选择`Generate statement`：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729132763164-68d5a9b0-76ea-43fb-b89d-01050e82c4e6.png" width="396" title="" crop="0,0,1,1" id="u5a8310a0" class="ne-image">

这个时候在mapper的xml配置文件中便生成了对应的配置。

接下来就是编写SQL语句了，最终`VipMapper.xml`文件的配置如下：

```xml

<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd" >
<mapper namespace="com.jkweilai.sb305springbootmybatis.repository.VipMapper">
    <insert id="insert">
        insert into t_vip(id,name,card_number,birth) values(null,#{name},#{cardNumber},#{birth})
    </insert>
    <update id="update">
        update t_vip set name=#{name},card_number=#{cardNumber},birth=#{birth} where id=#{id}
    </update>
    <delete id="deleteById">
        delete from t_vip where id = #{id}
    </delete>
    <select id="selectById" resultType="com.jkweilai.sb305springbootmybatis.entity.Vip">
        select * from t_vip where id=#{id}
    </select>
    <select id="selectAll" resultType="com.jkweilai.sb305springbootmybatis.entity.Vip">
        select * from t_vip
    </select>
</mapper>

```

---

## 添加Mapper的扫描

在Spring Boot的入口程序上添加如下的注解，来完成`VipMapper`接口的扫描：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764860078496-72abb68d-2a4d-46a2-be4f-0a36d78e8ab9.png" width="352" title="" crop="0,0,1,1" id="ubc64b787" class="ne-image">

---

## 告诉MyBatis框架MapperXML文件的位置

在`application.properties`配置文件中进行如下配置：

```properties

mybatis.mapper-locations=classpath:mapper/*.xml

```

**注意：如果 SqlMapper.xml 文件的存放路径和 Mapper 接口在同一个目录下，以上配置可以去掉。**

---

## 测试整合MyBatis是否成功

在Spring Boot主入口程序中获取Spring上下文对象`ApplicationContext`，从Spring容器中获取`VipMapper`对象，然后调用相关方法进行测试：

```java

package com.jkweilai.sb305springbootmybatis;

import com.jkweilai.sb305springbootmybatis.entity.Vip;
import com.jkweilai.sb305springbootmybatis.repository.VipMapper;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;

@MapperScan(basePackages = {"com.jkweilai.sb305springbootmybatis.repository"})
@SpringBootApplication
public class Sb305SpringbootMybatisApplication {

    public static void main(String[] args) {
        // 获取Spring上下文
        ConfigurableApplicationContext applicationContext = SpringApplication.run(Sb305SpringbootMybatisApplication.class, args);
        // 根据id获取容器中的对象
        VipMapper vipMapper = applicationContext.getBean("vipMapper", VipMapper.class);
        Vip vip = vipMapper.selectById(1L);
        System.out.println(vip);
        // 关闭Spring上下文
        applicationContext.close();
    }

}

```

测试结果：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729135284617-032c08b9-07f8-4d73-ba82-4529aac1f2fb.png" width="653" title="" crop="0,0,1,1" id="u2aba6355" class="ne-image">

测试结果中可以看到`cardNumber`属性没有赋值成功，原因是：表中的字段名叫做`card_number`，和实体类`Vip`的属性名`cardNumber`对应不上。解决办法两个：

+ **第一种方式：查询语句使用as关键字起别名，让查询结果列名和实体类的属性名对应上。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764860129838-4fc2cced-d930-4e2a-970d-004512e69628.png" width="726.4" title="" crop="0,0,1,1" id="ua9460474" class="ne-image">

再次测试：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729135540950-be358277-5da0-4c5d-868f-075cd2ed8ea0.png" width="717" title="" crop="0,0,1,1" id="u59d75ab0" class="ne-image">

+ **第二种方式：通过配置自动映射**

在`application.properties`配置文件中进行如下配置：

```properties

mybatis.configuration.map-underscore-to-camel-case=true

```

map-underscore-to-camel-case 是一个配置项，主要用于处理数据库字段名与Java对象属性名之间的命名差异。在许多数据库中，字段名通常使用下划线（_）分隔单词，例如 first_name 或 last_name。而在Java代码中，变量名通常使用驼峰式命名法（camel case），如 firstName 和 lastName。

当使用MyBatis作为ORM框架时，默认情况下它会将SQL查询结果映射到Java对象的属性上。如果数据库中的字段名与Java对象的属性名不一致，那么就需要手动为每个字段指定相应的属性名，或者使用某种方式来自动转换这些名称。

map-underscore-to-camel-case 这个配置项的作用就是在查询结果映射到Java对象时，自动将下划线分隔的字段名转换成驼峰式命名法。这样可以减少手动映射的工作量，并提高代码的可读性和可维护性。

mapper的xml文件中的sql语句仍然使用`*`的方式：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764860151877-f791d6db-6e8d-4535-ab36-81cb31c71b06.png" width="443.2" title="" crop="0,0,1,1" id="u60391fb5" class="ne-image">

测试结果如下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729135946867-e2f2fda6-25fe-430c-af38-0831056571c9.png" width="700" title="" crop="0,0,1,1" id="u701e2557" class="ne-image">

---

## 测试其他方法是否正常

测试程序如下：

```java

package com.jkweilai.sb305springbootmybatis;

import com.jkweilai.sb305springbootmybatis.entity.Vip;
import com.jkweilai.sb305springbootmybatis.repository.VipMapper;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;

import java.util.List;

@MapperScan(basePackages = {"com.jkweilai.sb305springbootmybatis.repository"})
@SpringBootApplication
public class Sb305SpringbootMybatisApplication {

    public static void main(String[] args) {
        // 获取Spring上下文
        ConfigurableApplicationContext applicationContext = SpringApplication.run(Sb305SpringbootMybatisApplication.class, args);
        // 根据id获取容器中的对象
        VipMapper vipMapper = applicationContext.getBean("vipMapper", VipMapper.class);
        Vip vip = vipMapper.selectById(1L);
        System.out.println(vip);
        // 添加会员信息
        Vip newVip = new Vip("杰克", "1234567892", "1999-11-10");
        vipMapper.insert(newVip);
        // 查询所有会员信息
        List<Vip> vips = vipMapper.selectAll();
        System.out.println(vips);
        // 修改会员信息
        vip.setName("zhangsan");
        vipMapper.update(vip);
        // 查询所有会员信息
        List<Vip> vips2 = vipMapper.selectAll();
        System.out.println(vips2);
        // 删除会员信息
        vipMapper.deleteById(1L);
        // 查询所有会员信息
        List<Vip> vips3 = vipMapper.selectAll();
        System.out.println(vips3);
        // 关闭Spring上下文
        applicationContext.close();
    }

}

```

执行结果如下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729136373779-97569876-0b74-4774-b306-a6bbc838462e.png" width="1772" title="" crop="0,0,1,1" id="ubefcb5e9" class="ne-image">

到此为止，我们已经完成了Spring Boot整合MyBatis的操作。

---

## 总结 SpringBoot 整合 MyBatis 的配置

**注意：以下的配置项中通过 **`**logging.level.com.jkweilai.demo.mapper=DEBUG**`**添加显示 SQL 的日志。**

```properties
