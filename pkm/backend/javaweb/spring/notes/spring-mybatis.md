# Spring集成MyBatis

---

## 实现步骤

+ 第一步：准备数据库表
    - 使用t_act表（账户表）
+ 第二步：IDEA中创建一个模块，并引入依赖
    - spring-context
    - spring-jdbc
    - mysql驱动
    - mybatis
    - mybatis-spring：****mybatis提供的与spring框架集成的依赖****
    - HikariCP（连接池）
    - Lombok
    - Aspects 
    - junit5
+ 第三步：基于三层架构实现，所以提前创建好所有的包
    - com.jkweilai.bank.mapper
    - com.jkweilai.bank.service
    - com.jkweilai.bank.service.impl
    - com.jkweilai.bank.entity
+ 第四步：编写entity
    - Account，提供属性，使用 lombok 注解标注。
+ 第五步：编写mapper接口
    - AccountMapper接口，定义方法
+ 第六步：编写mapper配置文件
    - 在配置文件中配置命名空间，以及每一个方法对应的sql。
+ 第七步：编写service接口和service接口实现类
    - AccountService
    - AccountServiceImpl
+ 第八步：编写jdbc.properties配置文件
    - 数据库连接池相关信息
+ 第九步：编写mybatis-config.xml配置文件
    - 该文件可以没有，大部分的配置可以转移到spring配置文件中。
    - 如果遇到mybatis相关的系统级配置，还是需要这个文件。（**比如开启 mybatis 标准日志，自动下划线转驼峰映射**）
+ 第十步：编写spring.xml配置文件（**当然：配置文件也可以采用配置类完成**）
    - 组件扫描
    - 引入外部的属性文件
    - 数据源
    - SqlSessionFactoryBean配置
        * 注入mybatis核心配置文件路径
        * 指定别名包
        * 注入数据源
    - Mapper扫描配置器
        * 指定扫描的包
    - 事务管理器DataSourceTransactionManager
        * 注入数据源
    - 启用事务注解
        * 注入事务管理器
+ 第十一步：编写测试程序，并添加事务，进行测试

---

## 具体实现

### 第一步：准备数据库表

```sql
DROP TABLE IF EXISTS `t_act`;
CREATE TABLE `t_act`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `act_no` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `balance` decimal(10, 2) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

INSERT INTO `t_act` VALUES (1, 'act-001', 50000.00);
INSERT INTO `t_act` VALUES (2, 'act-002', 0.00);
```

### 第二步：IDEA中创建一个模块，并引入依赖

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.jkweilai</groupId>
    <artifactId>spring-016-sm</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <dependencies>
        <!--spring context-->
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context</artifactId>
            <version>6.2.13</version>
        </dependency>
        <!--AspectJ依赖-->
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-aspects</artifactId>
            <version>6.2.13</version>
        </dependency>
        <!--spring jdbc-->
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-jdbc</artifactId>
            <version>6.2.13</version>
        </dependency>
        <!--mysql驱动-->
        <dependency>
            <groupId>com.mysql</groupId>
            <artifactId>mysql-connector-j</artifactId>
            <version>8.4.0</version>
        </dependency>
        <!--mybatis依赖-->
        <dependency>
            <groupId>org.mybatis</groupId>
            <artifactId>mybatis</artifactId>
            <version>3.5.16</version>
        </dependency>
        <!--mybatis和spring集成的依赖-->
        <dependency>
            <groupId>org.mybatis</groupId>
            <artifactId>mybatis-spring</artifactId>
            <version>3.0.4</version>
        </dependency>
        <!--HikariCP连接池的依赖-->
        <dependency>
            <groupId>com.zaxxer</groupId>
            <artifactId>HikariCP</artifactId>
            <version>7.0.2</version>
        </dependency>
        <!--junit的依赖-->
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-api</artifactId>
            <version>5.11.0</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-test</artifactId>
            <version>6.2.13</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
    </properties>

</project>
```

### 第三步：基于三层架构实现，所以提前创建好所有的包

`com.jkweilai.bank.mapper`

`com.jkweilai.bank.entity`

`com.jkweilai.bank.impl`

### 第四步：编写 entity

```java
package com.jkweilai.bank.entity;

import lombok.Data;

import java.math.BigDecimal;

@Data
public class Account {
    private Long id;
    private String actNo;
    private BigDecimal balance;
}

```

### 第五步：编写mapper接口

```java
package com.jkweilai.bank.mapper;

import com.jkweilai.bank.entity.Account;

import java.util.List;

public interface AccountMapper {

    /**
     * 修改账户
     * @param account
     * @return
     */
    int update(Account account);

    /**
     * 根据账号查询账户
     * @param actno
     * @return
     */
    Account selectByActno(String actno);
}

```

### 第六步：编写mapper配置文件

一定要注意，在 `resources`目录下新建 `com/jkweilai/bank/mapper`目录时，是斜杠不是点儿。在resources目录下新建。并且要和Mapper接口包对应上。

如果接口叫做AccountMapper，配置文件必须是AccountMapper.xml

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.jkweilai.bank.mapper.AccountMapper">
    <update id="update">
        update t_act set balance = #{balance} where actno = #{actno}
    </update>
    <select id="selectByActno" resultType="Account">
        select * from t_act where actno = #{actno}
    </select>
</mapper>
```

### 第七步：编写service接口和service接口实现类

注意编写的service实现类纳入IoC容器管理：

```java
package com.jkweilai.bank.service;

public interface AccountService {
    /**
     * 转账
     * @param fromActno
     * @param toActno
     * @param money
     */
    void transfer(String fromActno, String toActno, double money);
}

```

```java
package com.jkweilai.bank.service.impl;

import com.jkweilai.bank.mapper.AccountMapper;
import com.jkweilai.bank.entity.Account;
import com.jkweilai.bank.service.AccountService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service("accountService")
public class AccountServiceImpl implements AccountService {

    @Autowired
    private AccountMapper accountMapper;

    @Override
    @Transactional
    public void transfer(String fromActno, String toActno, double money) {
        Account fromAct = accountMapper.selectByActno(fromActno);
        if (fromAct.getBalance() < money) {
            throw new RuntimeException("余额不足");
        }
        Account toAct = accountMapper.selectByActno(toActno);
        fromAct.setBalance(fromAct.getBalance() - money);
        toAct.setBalance(toAct.getBalance() + money);
        int count = accountMapper.update(fromAct);
        count += accountMapper.update(toAct);
        if (count != 2) {
            throw new RuntimeException("转账失败");
        }
    }
}

```

### 第八步：编写jdbc.properties配置文件

放在类的根路径下

```properties
jdbc.driver=com.mysql.cj.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:3306/spring
jdbc.username=root
jdbc.password=123456
```

### 第九步：编写mybatis-config.xml配置文件

放在类的根路径下，只开启日志，其他配置到spring.xml中。

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <settings>
        <setting name="logImpl" value="STDOUT_LOGGING"/>
    </settings>
</configuration>
```

### 第十步：编写spring.xml配置文件

****注意：当你在spring.xml文件中直接写标签内容时，IDEA会自动给你添加命名空间****

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context" xmlns:tx="http://www.springframework.org/schema/tx"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/context https://www.springframework.org/schema/context/spring-context.xsd http://www.springframework.org/schema/tx http://www.springframework.org/schema/tx/spring-tx.xsd">
  
    <!--组件扫描-->
    <context:component-scan base-package="com.jkweilai.bank"/>
  
    <!--外部属性配置文件-->
    <context:property-placeholder location="jdbc.properties"/>

    <!--数据源-->
    <bean id="dataSource" class="com.zaxxer.hikari.HikariDataSource">
        <property name="driverClassName" value="${jdbc.driver}"/>
        <property name="jdbcUrl" value="${jdbc.url}"/>
        <property name="username" value="${jdbc.username}"/>
        <property name="password" value="${jdbc.password}"/>
    </bean>

    <!--SqlSessionFactoryBean-->
    <bean class="org.mybatis.spring.SqlSessionFactoryBean">
        <!--mybatis核心配置文件路径-->
        <property name="configLocation" value="mybatis-config.xml"/>
        <!--注入数据源-->
        <property name="dataSource" ref="dataSource"/>
        <!--起别名-->
        <property name="typeAliasesPackage" value="com.jkweilai.bank.entity"/>
    </bean>

    <!--Mapper扫描器-->
    <bean class="org.mybatis.spring.mapper.MapperScannerConfigurer">
        <property name="basePackage" value="com.jkweilai.bank.mapper"/>
    </bean>

    <!--事务管理器-->
    <bean id="txManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
        <property name="dataSource" ref="dataSource"/>
    </bean>

    <!--开启事务注解-->
    <tx:annotation-driven transaction-manager="txManager"/>

</beans>
```

### 第十一步：编写测试程序，并添加事务，进行测试

```java
package com.jkweilai.spring.test;

import com.jkweilai.bank.service.AccountService;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class SMTest {

    @Test
    public void testSM(){
        ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring.xml");
        AccountService accountService = applicationContext.getBean("accountService", AccountService.class);
        try {
            accountService.transfer("act-001", "act-002", 10000.0);
            System.out.println("转账成功");
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("转账失败");
        }
    }

}
```

****最后大家别忘了测试事务！！！！****

---

## 配置类方式

以上的程序如果换成配置类的方式，代码如下：

```java
package com.jkweilai.bank.config;

import com.zaxxer.hikari.HikariDataSource;
import org.mybatis.spring.SqlSessionFactoryBean;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.*;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.Resource;
import org.springframework.jdbc.datasource.DataSourceTransactionManager;
import org.springframework.transaction.annotation.EnableTransactionManagement;

import javax.sql.DataSource;

@Configuration
@ComponentScan("com.jkweilai.bank")
@PropertySource("classpath:application.properties")
@EnableTransactionManagement
@EnableAspectJAutoProxy
@MapperScan("com.jkweilai.bank.mapper")
public class SpringMyBatisConfig {

    @Bean
    public DataSource dataSource(
            @Value("${spring.datasource.driver}")
            String driver,
            @Value("${spring.datasource.url}")
            String url,
            @Value("${spring.datasource.user}")
            String user,
            @Value("${spring.datasource.password}")
            String password) {
        HikariDataSource dataSource = new HikariDataSource();
        dataSource.setDriverClassName(driver);
        dataSource.setJdbcUrl(url);
        dataSource.setUsername(user);
        dataSource.setPassword(password);
        return dataSource;
    }

    @Bean
    public SqlSessionFactoryBean sqlSessionFactoryBean(
            DataSource dataSource,
            @Value("${mybatis.config.location}")
            String mybatisConfigLocation,
            @Value("${mybatis.type.aliases.package}")
            String typeAliasesPackage) {
        SqlSessionFactoryBean sqlSessionFactoryBean = new SqlSessionFactoryBean();
        Resource resource = new ClassPathResource(mybatisConfigLocation);
        sqlSessionFactoryBean.setConfigLocation(resource);
        sqlSessionFactoryBean.setDataSource(dataSource);
        sqlSessionFactoryBean.setTypeAliasesPackage(typeAliasesPackage);
        return sqlSessionFactoryBean;
    }

    @Bean
    public DataSourceTransactionManager transactionManager(DataSource dataSource) {
        DataSourceTransactionManager dataSourceTransactionManager = new DataSourceTransactionManager();
        dataSourceTransactionManager.setDataSource(dataSource);
        return dataSourceTransactionManager;
    }

}

```

测试程序如下：

```java
package com.jkweilai.bank.test;

import com.jkweilai.bank.config.SpringMyBatisConfig;
import com.jkweilai.bank.service.AccountService;
import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import java.math.BigDecimal;

public class BankTest {
    @Test
    public void test(){
        ApplicationContext context = new AnnotationConfigApplicationContext(SpringMyBatisConfig.class);
        AccountService accountService = context.getBean(AccountService.class);
        accountService.transfer("act-001", "act-002", new BigDecimal(10000.0));
    }
}

```

配置文件 `application.properties`如下：

```properties
spring.datasource.driver=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/spring
spring.datasource.user=root
spring.datasource.password=123456
mybatis.config.location=mybatis-config.xml
mybatis.type.aliases.package=com.jkweilai.bank.entity
```

---

## Spring配置文件的import

spring配置文件有多个，并且可以在spring的核心配置文件中使用import进行引入，我们可以将组件扫描单独定义到一个配置文件中，如下：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/context https://www.springframework.org/schema/context/spring-context.xsd">

    <!--组件扫描-->
    <context:component-scan base-package="com.jkweilai.bank"/>

</beans>
```

然后在核心配置文件中引入：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context" xmlns:tx="http://www.springframework.org/schema/tx"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/context https://www.springframework.org/schema/context/spring-context.xsd http://www.springframework.org/schema/tx http://www.springframework.org/schema/tx/spring-tx.xsd">

    <!--引入其他的spring配置文件-->
    <import resource="common.xml"/>

</beans>
```

****注意：在实际开发中，service单独配置到一个文件中，dao单独配置到一个文件中，然后在核心配置文件中引入，养成好习惯。****
