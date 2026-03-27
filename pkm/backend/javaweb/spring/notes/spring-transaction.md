# Spring对事务的支持

---

## 事务概述

+ 什么是事务
    - 在一个业务流程当中，通常需要多条DML（insert delete update）语句共同联合才能完成，这多条DML语句必须同时成功，或者同时失败，这样才能保证数据的安全。
    - 多条DML要么同时成功，要么同时失败，这叫做事务。
    - 事务：Transaction（tx）
+ 事务的四个处理过程：
    - 第一步：开启事务 (start transaction)
    - 第二步：执行核心业务代码
    - 第三步：提交事务（如果核心业务处理过程中没有出现异常）(commit transaction)
    - 第四步：回滚事务（如果核心业务处理过程中出现异常）(rollback transaction)
+ 事务的四个特性：
    - A 原子性：事务是最小的工作单元，不可再分。
    - C 一致性：事务要求要么同时成功，要么同时失败。事务前和事务后的总量不变。
    - I 隔离性：事务和事务之间因为有隔离性，才可以保证互不干扰。
    - D 持久性：持久性是事务结束的标志。

---

## 引入事务场景

以银行账户转账为例学习事务。两个账户act-001和act-002。act-001账户向act-002账户转账10000，必须同时成功，或者同时失败。（一个减成功，一个加成功， 这两条update语句必须同时成功，或同时失败。）

采用三层架构搭建：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749727730298-3fbf26a7-40a4-4ee2-bd8b-6ed01adec552.png)

### 没有异常时

模块名：spring-013-tx-bank（将之前spring和mybatis集成的代码完全拷贝到当前模块中。）

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763901498342-1c544b5d-7f7c-4d3e-8b80-3fab3d9d7824.png)

数据变化：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1666497727323-b2ca34c9-99c6-4b23-8d3b-8dbe3009d3e9.png)

### 模拟异常后

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763901514771-99a5964c-e344-4ed6-b879-649b329fffd4.png)

数据库表中数据：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1666497824308-bdd8f11f-8f99-4195-81c4-c37721627f4c.png)

****丢了1万。****

****

---

## Spring对事务的支持

### Spring实现事务的两种方式

+ 编程式事务
    - 通过编写代码的方式来实现事务的管理。
+ 声明式事务
    - **基于注解方式（******掌握这种方式******）**
    - 基于XML配置方式

### Spring事务管理API

Spring对事务的管理底层实现方式是基于AOP实现的。采用AOP的方式进行了封装。所以Spring专门针对事务开发了一套API，API的核心接口如下：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1666504216275-1b6a9ac4-6958-4cdf-9323-7a79a08d059d.png)

PlatformTransactionManager接口：spring事务管理器的核心接口。在****Spring****中它有两个实现：

+ DataSourceTransactionManager：支持JdbcTemplate、MyBatis、Hibernate等事务管理。
+ JtaTransactionManager：支持分布式事务管理。

如果要在Spring中使用JdbcTemplate、MyBatis、Hibernate，就要使用DataSourceTransactionManager来管理事务。（Spring内置写好了，可以直接用。）

### 声明式事务之注解实现方式

+ 第一步：在spring配置文件中配置事务管理器。

```xml
<bean id="transactionManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
  <property name="dataSource" ref="dataSource"/>
</bean>
```

+ 第二步：在spring配置文件中引入tx命名空间。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:tx="http://www.springframework.org/schema/tx"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
                           http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd
                           http://www.springframework.org/schema/tx http://www.springframework.org/schema/tx/spring-tx.xsd">
```

+ 第三步：在spring配置文件中配置“事务注解驱动器”，开启注解的方式控制事务。

```xml
<tx:annotation-driven transaction-manager="transactionManager"/>
```

+ 第四步：在service类上或方法上添加@Transactional注解

在类上添加该注解，该类中所有的方法都有事务。在某个方法上添加该注解，表示只有这个方法使用事务。

```java
package com.jkweilai.bank.service.impl;

import com.jkweilai.bank.mapper.AccountMapper;
import com.jkweilai.bank.entity.Account;
import com.jkweilai.bank.service.AccountService;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service("accountService")
@Transactional
public class AccountServiceImpl implements AccountService {

    @Autowired
    private AccountMapper accountMapper;

    @Override
    public void transfer(String fromActno, String toActno, double money) {
        // 查询账户余额是否充足
        Account fromAct = accountMapper.selectByActno(fromActno);
        if (fromAct.getBalance() < money) {
            throw new RuntimeException("账户余额不足");
        }
        // 余额充足，开始转账
        Account toAct = accountMapper.selectByActno(toActno);
        fromAct.setBalance(fromAct.getBalance() - money);
        toAct.setBalance(toAct.getBalance() + money);
        int count = accountMapper.update(fromAct);

        // 模拟异常
        String s = null;
        s.toString();

        count += accountMapper.update(toAct);
        if (count != 2) {
            throw new RuntimeException("转账失败，请联系银行");
        }
    }
}

```

当前数据库表中的数据：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1666505321919-85dd9adb-bceb-49ef-826f-5a3ddf7699a0.png)

执行测试程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763901573349-937ac896-28c4-41a6-b719-d2f1c0f6a8d9.png)

虽然出现异常了，再次查看数据库表中数据：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1666505321919-85dd9adb-bceb-49ef-826f-5a3ddf7699a0.png)

通过测试，发现数据没有变化，事务起作用了。

### 事务属性

#### 事务属性包括哪些
![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1666506552984-8a4f9d42-73ba-4ded-853d-564d27340db5.png)

事务中的重点属性：

+ 事务传播行为
+ 事务隔离级别
+ 事务超时
+ 只读事务
+ 设置出现哪些异常回滚事务
+ 设置出现哪些异常不回滚事务

#### 事务传播行为
什么是事务的传播行为？

在service类中有a()方法和b()方法，a()方法上有事务，b()方法上也有事务，当a()方法执行过程中调用了b()方法，事务是如何传递的？合并到一个事务里？还是开启一个新的事务？这就是事务传播行为。

事务传播行为在spring框架中被定义为枚举类型：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1666505960049-06173489-15fc-4d16-94f3-1a9025f85d8c.png)

一共有七种传播行为：

+ REQUIRED：支持当前事务，如果不存在就新建一个(默认)****【没有就新建，有就加入】****
+ SUPPORTS：支持当前事务，如果当前没有事务，就以非事务方式执行****【有就加入，没有就不管了】****
+ MANDATORY：**必须运行在一个事务中，如果当前没有事务正在发生，将抛出一个异常******【有就加入，没有就抛异常】****
+ REQUIRES_NEW：**开启一个新的事务，如果一个事务已经存在，则将这个存在的事务挂起******【不管有没有，直接开启一个新事务，开启的新事务和之前的事务不存在嵌套关系，之前事务被挂起，********挂起就是把当前事务暂停，等新事务完成后，再恢复继续执行********】****
+ NOT_SUPPORTED：**以非事务方式运行，如果有事务存在，挂起当前事务******【不支持事务，存在就挂起】****
+ NEVER：**以非事务方式运行，如果有事务存在，抛出异常******【不支持事务，存在就抛异常】****
+ NESTED：**如果当前正有一个事务在进行中，则该方法应当运行在一个嵌套式事务中。被嵌套的事务可以独立于外层事务进行提交或回滚。如果外层事务不存在，行为就像REQUIRED一样。******【当前有事务的话，就在这个事务里再嵌套一个完全独立的事务，嵌套的事务可以独立的提交和回滚。当前没有事务就和REQUIRED一样。嵌套事务的特点是：外层回滚会导致内层回滚】****

**在代码中设置事务的传播行为：**

```java
@Transactional(propagation = Propagation.REQUIRED)
```

可以编写程序测试一下传播行为：**需要分成两个类来进行测试，在一个类中测不出来，主要原因是Spring的事务管理是基于AOP代理的，而在同一个类内部的方法调用不会经过事务拦截器。**

```java
@Transactional(propagation = Propagation.REQUIRED)
public void save(Account act) {

    // 这里调用dao的insert方法。
    accountDao.insert(act); // 保存act-003账户

    // 创建账户对象
    Account act2 = new Account("act-004", 1000.0);
    try {
        accountService.save(act2); // 保存act-004账户
    } catch (Exception e) {

    }
    // 继续往后进行我当前1号事务自己的事儿。
}
```

```java
@Override
//@Transactional(propagation = Propagation.REQUIRED)
@Transactional(propagation = Propagation.REQUIRES_NEW)
public void save(Account act) {
    accountDao.insert(act);
    // 模拟异常
    String s = null;
    s.toString();

    // 事儿没有处理完，这个大括号当中的后续也许还有其他的DML语句。
}
```

#### **事务隔离级别**
在Spring代码中如何设置隔离级别？

隔离级别在spring中以枚举类型存在：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1666508609641-2c838566-7334-4cf1-b452-0fed9aaebf3d.png)

```java
@Transactional(isolation = Isolation.READ_COMMITTED)
```

测试事务隔离级别：READ_UNCOMMITTED 和 READ_COMMITTED

怎么测试：一个service负责插入，一个service负责查询。负责插入的service要模拟延迟。

```java
package com.jkweilai.bank.service.impl;

import com.jkweilai.bank.mapper.AccountMapper;
import com.jkweilai.bank.entity.Account;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Isolation;
import org.springframework.transaction.annotation.Transactional;

@Service("i1")
public class IsolationService1 {

    @Autowired
    private AccountMapper accountMapper;

    // 1号
    // 负责查询
    // 当前事务可以读取到别的事务没有提交的数据。
    //@Transactional(isolation = Isolation.READ_UNCOMMITTED)
    // 对方事务提交之后的数据我才能读取到。
    @Transactional(isolation = Isolation.READ_COMMITTED)
    public void getByActno(String actno) {
        Account account = accountMapper.selectByActno(actno);
        System.out.println("查询到的账户信息：" + account);
    }

}

```

```java
package com.jkweilai.bank.service.impl;

import com.jkweilai.bank.mapper.AccountMapper;
import com.jkweilai.bank.entity.Account;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service("i2")
public class IsolationService2 {

    @Autowired
    private AccountMapper accountMapper;

    // 2号
    // 负责insert
    @Transactional
    public void save(Account act) {
        accountMapper.insert(act);
        // 睡眠一会
        try {
            Thread.sleep(1000 * 20);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

}

```

测试程序

```java
@Test
public void testIsolation1(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring.xml");
    IsolationService1 i1 = applicationContext.getBean("i1", IsolationService1.class);
    i1.getByActno("act-004");
}

@Test
public void testIsolation2(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring.xml");
    IsolationService2 i2 = applicationContext.getBean("i2", IsolationService2.class);
    Account act = new Account("act-004", 1000.0);
    i2.save(act);
}
```

通过执行结果可以清晰的看出隔离级别不同，执行效果不同。

#### 事务超时
代码如下：

```java
@Transactional(timeout = 10)
```

以上代码表示设置事务的超时时间为10秒。

****表示超过10秒如果该事务中所有的DML语句还没有执行完毕的话，最终结果会选择回滚。****

默认值-1，表示没有时间限制。

```java
@Service("i2")
public class IsolationService2 {

    @Autowired
    private AccountMapper accountMapper;

    @Transactional(timeout = 10)
    public void save(Account account) {
        accountMapper.insert(account);
        try {
            Thread.sleep(1000 * 20);
            // 注意，数据库操作会触发事务的超时检查，而纯Java代码不会触发超时检查。
            // 因此在事务结束之前需要执行一个数据库的操作,CRUD都行。
            accountMapper.selectByActNo("act-001");
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}

```

****

#### 只读事务

```java
@Transactional(readOnly = true)
```

**面试题：Spring 的事务如果设置为 **`**readOnly=true**`**有什么用？**

****核心答案：******“设置**`**readOnly=true**`**主要有两个核心作用：第一是为了******性能优化******，第二是为了******声明代码意图******。”**

****分点阐述：****

1. ****性能优化（最主要）：******“它是一个给数据库和ORM框架的******优化提示******。特别是对于Hibernate/JPA，它可以******跳过事务提交时的脏检查******，因为框架知道不会有数据更新，这能节省大量CPU资源。”**
2. ****声明意图与规范：******“它在代码层面清晰地标明了这是一个******只读查询方法******，增强了可读性。同时，它也能在数据库读写分离的架构中，作为路由信号，******将查询操作自动指向从库******，减轻主库压力。”**

****如果被追问“写了数据会怎样”：******“需要特别注意的是，它通常是一个******提示而非强制约束******。在大多数情况下，误操作写数据依然会成功。但有些平台，比如Hibernate，可能会在提交时抛出异常。所以，我们不能依赖它来防止写操作，而应把它当作一种性能和规范上的最佳实践。”**

****总结（一句话收尾）：****  
**“所以，在我的项目中，我们会强制要求所有纯查询方法都加上**`**@Transactional(readOnly = true)**`**，这既是为了性能，也是为了代码的清晰和规范。”**

#### 设置事务的异常回滚规则
**核心机制：**  
在Spring框架的`@Transactional`注解中，事务回滚的默认行为是：

+ **默认回滚**：遇到**运行时异常**（`RuntimeException`及其子类）和**错误**（`Error`及其子类）时，事务会自动回滚。
+ **默认不回滚**：遇到**受检异常**（Checked Exception，即编译时异常），事务默认不会回滚。

**1. 设置特定异常触发回滚**

您可以通过`rollbackFor`属性来覆盖默认规则，指定哪些异常（包括原本默认不回滚的受检异常）发生时也触发回滚。

```java
// 示例1：任何异常（包括所有运行时异常和受检异常）发生都回滚
@Transactional(rollbackFor = Exception.class)

// 示例2：发生IOException（受检异常）或任何运行时异常时，都触发回滚
@Transactional(rollbackFor = IOException.class)
```

**2. 设置特定异常不触发回滚**

您可以通过`noRollbackFor`属性来指定即使发生了某些默认会回滚的异常（如运行时异常），事务也不回滚。

```java
// 示例：发生NullPointerException（运行时异常）时不回滚，但发生其他运行时异常或已配置的受检异常时仍会回滚。
@Transactional(noRollbackFor = NullPointerException.class)
```

**关键提醒：**

+ `rollbackFor` 用于 **扩展** 回滚的异常范围。
+ `noRollbackFor` 用于 **缩小** 回滚的异常范围。

### **事务的全注解式开发**

编写一个类来代替配置文件，代码如下：

```java
package com.jkweilai.bank.config;

import com.alibaba.druid.pool.DruidDataSource;
import org.mybatis.spring.SqlSessionFactoryBean;
import org.mybatis.spring.mapper.MapperScannerConfigurer;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.InputStreamResource;
import org.springframework.jdbc.datasource.DataSourceTransactionManager;
import org.springframework.transaction.TransactionManager;
import org.springframework.transaction.annotation.EnableTransactionManagement;

import javax.sql.DataSource;
import java.util.ResourceBundle;

// 这个类是代替 spring.xml 文件。
@Configuration
@ComponentScan("com.jkweilai.bank")
@MapperScan("com.jkweilai.bank.mapper")
@EnableTransactionManagement
public class SpringConfig {

    @Bean
    public DataSource getDataSource(){
        ResourceBundle bundle = ResourceBundle.getBundle("jdbc");
        String driver = bundle.getString("jdbc.driver");
        String url = bundle.getString("jdbc.url");
        String username = bundle.getString("jdbc.username");
        String password = bundle.getString("jdbc.password");
        DruidDataSource dataSource = new DruidDataSource();
        dataSource.setDriverClassName(driver);
        dataSource.setUrl(url);
        dataSource.setUsername(username);
        dataSource.setPassword(password);
        return dataSource;
    }

    @Bean
    public SqlSessionFactoryBean getSqlSessionFactoryBean(DataSource dataSource){ // 这个 DataSource 参数会被自动注入。
        SqlSessionFactoryBean sqlSessionFactoryBean = new SqlSessionFactoryBean();
        InputStreamResource isr = new InputStreamResource(Thread.currentThread()
                .getContextClassLoader().getResourceAsStream("mybatis-config.xml"));
        sqlSessionFactoryBean.setConfigLocation(isr);
        sqlSessionFactoryBean.setDataSource(dataSource);
        sqlSessionFactoryBean.setTypeAliasesPackage("com.jkweilai.bank.entity");
        return sqlSessionFactoryBean;
    }

    @Bean
    public TransactionManager getTransactionManager(DataSource dataSource){
        DataSourceTransactionManager dataSourceTransactionManager = new DataSourceTransactionManager();
        dataSourceTransactionManager.setDataSource(dataSource);
        return dataSourceTransactionManager;
    }
}

```

测试程序如下：

```java
@Test
public void testNoXml(){
    ApplicationContext applicationContext = new AnnotationConfigApplicationContext(SpringConfig.class);
    AccountService accountService = applicationContext.getBean("accountService", AccountService.class);
    try {
        accountService.transfer("act-001", "act-002", 10000);
        System.out.println("转账成功");
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763901697717-7b9ec7b7-cc65-4195-ae11-8435e38e8311.png)

数据库表中数据：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1666511460275-5ede53ce-9ad1-4bce-935a-32436a46c83a.png)

****
