# Spring IoC注解式开发

---

## 声明Bean的注解

负责声明Bean的注解，常见的包括四个：

+ @Component
+ @Controller
+ @Service
+ @Repository

源码如下：

```java
@Target(value = {ElementType.TYPE})
@Retention(value = RetentionPolicy.RUNTIME)
public @interface Component {
    String value();
}

```

```java
@Target({ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Component
public @interface Controller {
    @AliasFor(
        annotation = Component.class
    )
    String value() default "";
}

```

```java
@Target({ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Component
public @interface Service {
    @AliasFor(
        annotation = Component.class
    )
    String value() default "";
}

```

```java
@Target({ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Component
public @interface Repository {
    @AliasFor(
        annotation = Component.class
    )
    String value() default "";
}

```

通过源码可以看到，@Controller、@Service、@Repository这三个注解都是@Component注解的别名。

也就是说：这四个注解的功能都一样。用哪个都可以。

只是为了增强程序的可读性，建议：

+ 控制器类上使用：Controller
+ service类上使用：Service
+ dao类上使用：Repository

他们都是只有一个value属性。value属性用来指定bean的id，也就是bean的名字。

---

## Spring注解的使用

如何使用以上的注解呢？

+ 第一步：加入aop的依赖
+ 第二步：在配置文件中添加context命名空间
+ 第三步：在配置文件中指定扫描的包
+ 第四步：在Bean类上使用注解

**第一步：加入aop的依赖**

当加入spring-context依赖之后，会关联加入aop的依赖。所以这一步不用做。

**第二步：在配置文件中添加context命名空间**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
                           http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">

</beans>
```

**第三步：在配置文件中指定要扫描的包**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
                           http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">
    <context:component-scan base-package="com.jkweilai.spring.bean"/>
</beans>
```

**第四步：在Bean类上使用注解**

```java
package com.jkweilai.spring.bean;

import org.springframework.stereotype.Component;

@Component(value = "userBean")
public class User {
}

```

编写测试程序：

```java
public class AnnotationTest {
    @Test
    public void testBean(){
        ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring.xml");
        User userBean = applicationContext.getBean("userBean", User.class);
        System.out.println(userBean);
    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763804203105-01de403b-0c38-49b2-b97a-539b080ff2ce.png)

****如果注解的属性名是value，那么value是可以省略的。****

```java
@Component("vipBean")
public class Vip {
}

```

```java
public class AnnotationTest {
    @Test
    public void testBean(){
        ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring.xml");
        Vip vipBean = applicationContext.getBean("vipBean", Vip.class);
        System.out.println(vipBean);
    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763804235969-ee73d66b-b32a-45e1-bd5a-14be1d80c299.png)

****如果把value属性彻底去掉，spring会为 Bean自动取名吗？会的。并且默认名字的规律是：Bean类名首字母小写。****

```java
@Component
public class BankDao {
}
```

也就是说，这个BankDao的bean的名字为：bankDao

测试一下

```java
public class AnnotationTest {
    @Test
    public void testBean(){
        ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring.xml");
        BankDao bankDao = applicationContext.getBean("bankDao", BankDao.class);
        System.out.println(bankDao);
    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763804278652-8433e88b-d875-44b4-b035-8088bc3849a3.png)

我们将Component注解换成其它三个注解，看看是否可以用：

```java
@Controller
public class BankDao {
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763804296741-fd026e58-9034-448f-8c7f-29d26316ba8d.png)

剩下的两个注解大家可以测试一下。

****如果是多个包怎么办？有两种解决方案：****

+ ****第一种：在配置文件中指定多个包，用逗号隔开。****
+ ****第二种：指定多个包的共同父包。****

先来测试一下逗号（英文）的方式：

创建一个新的包：bean2，定义一个Bean类。

```java
@Service
public class Order {
}

```

配置文件修改：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
                           http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">
    <context:component-scan base-package="com.jkweilai.spring.bean,com.jkweilai.spring.bean2"/>
</beans>
```

测试程序：

```java
public class AnnotationTest {
    @Test
    public void testBean(){
        ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring.xml");
        BankDao bankDao = applicationContext.getBean("bankDao", BankDao.class);
        System.out.println(bankDao);
        Order order = applicationContext.getBean("order", Order.class);
        System.out.println(order);
    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763804341646-5c51361e-bd26-4f3b-b86e-af784a6051f5.png)

我们再来看看，指定共同的父包行不行：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
                           http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">
    <context:component-scan base-package="com.jkweilai.spring"/>
</beans>
```

执行测试程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763804354597-61388add-ec5c-4121-88b2-273cfafd7a12.png)

---

## 选择性实例化Bean

假设在某个包下有很多Bean，有的Bean上标注了Component，有的标注了Controller，有的标注了Service，有的标注了Repository，现在由于某种特殊业务的需要，只允许其中所有的Controller参与Bean管理，其他的都不实例化。这应该怎么办呢？

```java
@Component
public class A {
    public A() {
        System.out.println("A的无参数构造方法执行");
    }
}

@Controller
class B {
    public B() {
        System.out.println("B的无参数构造方法执行");
    }
}

@Service
class C {
    public C() {
        System.out.println("C的无参数构造方法执行");
    }
}

@Repository
class D {
    public D() {
        System.out.println("D的无参数构造方法执行");
    }
}

@Controller
class E {
    public E() {
        System.out.println("E的无参数构造方法执行");
    }
}

@Controller
class F {
    public F() {
        System.out.println("F的无参数构造方法执行");
    }
}

```

我只想实例化bean3包下的Controller。配置文件这样写：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
                           http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">

    <context:component-scan base-package="com.jkweilai.spring.bean3" use-default-filters="false">
        <context:include-filter type="annotation" expression="org.springframework.stereotype.Controller"/>
    </context:component-scan>
    
</beans>
```

use-default-filters="true" 表示：使用spring默认的规则，只要有Component、Controller、Service、Repository中的任意一个注解标注，则进行实例化。

****use-default-filters="false"**** 表示：不再spring默认实例化规则，即使有Component、Controller、Service、Repository这些注解标注，也不再实例化。

<context:include-filter type="annotation" expression="org.springframework.stereotype.Controller"/> 表示只有Controller进行实例化。

```java
@Test
public void testChoose(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-choose.xml");
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763804449496-e4d1f7c3-436d-4f66-baff-b698715d56bf.png)

也可以将use-default-filters设置为true（不写就是true），并且采用exclude-filter方式排出哪些注解标注的Bean不参与实例化：

```xml
<context:component-scan base-package="com.jkweilai.spring.bean3">
  <context:exclude-filter type="annotation" expression="org.springframework.stereotype.Repository"/>
  <context:exclude-filter type="annotation" expression="org.springframework.stereotype.Service"/>
  <context:exclude-filter type="annotation" expression="org.springframework.stereotype.Controller"/>
</context:component-scan>
```

执行测试程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763804479326-d90316fa-ca13-4a1e-b50d-f69afe8bd63e.png)

---

## 负责注入的注解

@Component @Controller @Service @Repository 这四个注解是用来声明Bean的，声明后这些Bean将被实例化。接下来我们看一下，如何给Bean的属性赋值。给Bean属性赋值需要用到这些注解：

+ @Value
+ @Autowired
+ @Qualifier
+ @Resource

### @Value

当属性的类型是简单类型时，可以使用@Value注解进行注入。

```java
@Component
public class User {
    @Value(value = "zhangsan")
    private String name;
    @Value("20")
    private int age;

    @Override
    public String toString() {
        return "User{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}

```

开启包扫描：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
                           http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">
    <context:component-scan base-package="com.jkweilai.spring.bean4"/>
</beans>
```

```java
@Test
public void testValue(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-injection.xml");
    Object user = applicationContext.getBean("user");
    System.out.println(user);
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763804917630-cc7f0031-f604-4fc9-aab3-80642ab35aa9.png)

通过以上代码可以发现，我们并没有给属性提供setter方法，但仍然可以完成属性赋值。

如果提供setter方法，并且在setter方法上添加@Value注解，可以完成注入吗？尝试一下：

```java
@Component
public class User {
    
    private String name;

    private int age;

    @Value("李四")
    public void setName(String name) {
        this.name = name;
    }

    @Value("30")
    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "User{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763804943343-e101a0a8-fbce-4e33-be2f-05a95c64f7a6.png)

通过测试可以得知，@Value注解可以直接使用在属性上，也可以使用在setter方法上。都是可以的。都可以完成属性的赋值。

为了简化代码，以后我们一般不提供setter方法，直接在属性上使用@Value注解完成属性赋值。

出于好奇，我们再来测试一下，是否能够通过构造方法完成注入：

```java
@Component
public class User {

    private String name;

    private int age;

    public User(@Value("隔壁老王") String name, @Value("33") int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return "User{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763804995156-d949008f-37c3-4c67-8e6c-691963c4dca5.png)

通过测试得知：@Value注解可以出现在属性上、setter方法上、以及构造方法的形参上。可见Spring给我们提供了多样化的注入。太灵活了。

### @Autowired与@Qualifier

@Autowired注解可以用来注入****非简单类型****。被翻译为：自动连线的，或者自动装配。

单独使用@Autowired注解，****默认根据类型装配****。【默认是byType】

看一下它的源码：

```java
@Target({ElementType.CONSTRUCTOR, ElementType.METHOD, ElementType.PARAMETER, ElementType.FIELD, ElementType.ANNOTATION_TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface Autowired {
    boolean required() default true;
}
```

源码中有两处需要注意：

+ 第一处：该注解可以标注在哪里？
    - 构造方法上
    - 方法上
    - 形参上
    - 属性上
    - 注解上
+ 第二处：该注解有一个required属性，默认值是true，表示在注入的时候要求被注入的Bean必须是存在的，如果不存在则报错。如果required属性设置为false，表示注入的Bean存在或者不存在都没关系，存在的话就注入，不存在的话，也不报错。

****我们先在属性上使用@Autowired注解：****

```java
public interface UserDao {
    void insert();
}

```

```java
@Repository //纳入bean管理
public class UserDaoForMySQL implements UserDao{
    @Override
    public void insert() {
        System.out.println("正在向mysql数据库插入User数据");
    }
}

```

```java
package com.jkweilai.spring.service;

import com.jkweilai.spring.dao.UserDao;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service // 纳入bean管理
public class UserService {

    @Autowired // 在属性上注入
    private UserDao userDao;
    
    // 没有提供构造方法和setter方法。

    public void save(){
        userDao.insert();
    }
}
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
                           http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">
    <context:component-scan base-package="com.jkweilai.spring.dao,com.jkweilai.spring.service"/>
</beans>
```

```java
@Test
public void testAutowired(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-injection.xml");
    UserService userService = applicationContext.getBean("userService", UserService.class);
    userService.save();
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763805114065-6361a6f4-61c9-474b-9ae9-ef0ed63f6865.png)

以上构造方法和setter方法都没有提供，经过测试，仍然可以注入成功。

****接下来，再来测试一下@Autowired注解出现在setter方法上：****

```java
@Service
public class UserService {

    private UserDao userDao;

    @Autowired
    public void setUserDao(UserDao userDao) {
        this.userDao = userDao;
    }

    public void save(){
        userDao.insert();
    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763805143555-f1d1626f-416f-4812-87b2-c347277c2399.png)

****我们再来看看能不能出现在构造方法上：****

```java
@Service
public class UserService {

    private UserDao userDao;

    @Autowired
    public UserService(UserDao userDao) {
        this.userDao = userDao;
    }

    public void save(){
        userDao.insert();
    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763805158158-1864aedd-717b-4cbc-a174-1b8cf56b0907.png)

****再来看看，这个注解能不能只标注在构造方法的形参上：****

```java
@Service
public class UserService {

    private UserDao userDao;

    public UserService(@Autowired UserDao userDao) {
        this.userDao = userDao;
    }

    public void save(){
        userDao.insert();
    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763805183577-c0a54642-14c1-45aa-98a7-2353dc7c0dc9.png)

****还有更劲爆的，当有参数的构造方法只有一个时，@Autowired注解可以省略。****

```java
@Service
public class UserService {

    private UserDao userDao;

    public UserService(UserDao userDao) {
        this.userDao = userDao;
    }

    public void save(){
        userDao.insert();
    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763805219740-0dd5b10c-b852-4a76-9d3d-72913af93ffc.png)

****当然，如果有多个构造方法，@Autowired肯定是不能省略的。****

```java
@Service
public class UserService {

    private UserDao userDao;

    public UserService(UserDao userDao) {
        this.userDao = userDao;
    }
    
    public UserService(){
        
    }

    public void save(){
        userDao.insert();
    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763805250282-dae28d2e-04b3-450c-bfb9-c3cd14458593.png)

到此为止，我们已经清楚@Autowired注解可以出现在哪些位置了。

@Autowired注解默认是byType进行注入的，也就是说根据类型注入的，如果以上程序中，UserDao接口还有另外一个实现类，会出现问题吗？

```java
@Repository //纳入bean管理
public class UserDaoForOracle implements UserDao{
    @Override
    public void insert() {
        System.out.println("正在向Oracle数据库插入User数据");
    }
}

```

当你写完这个新的实现类之后，此时IDEA工具已经提示错误信息了：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763805295378-ca25b98c-bab2-4d28-b7bb-190ea894aa40.png)

错误信息中说：不能装配，UserDao这个Bean的数量大于1.

怎么解决这个问题呢？****当然要byName，根据名称进行装配了。****

@Autowired注解和@Qualifier注解联合起来才可以根据名称进行装配，在@Qualifier注解中指定Bean名称。

```java
@Repository // 这里没有给bean起名，默认名字是：userDaoForOracle
public class UserDaoForOracle implements UserDao{
    @Override
    public void insert() {
        System.out.println("正在向Oracle数据库插入User数据");
    }
}

```

```java
@Service
public class UserService {

    private UserDao userDao;

    @Autowired
    @Qualifier("userDaoForOracle") // 这个是bean的名字。
    public void setUserDao(UserDao userDao) {
        this.userDao = userDao;
    }

    public void save(){
        userDao.insert();
    }
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763805339010-607a6347-00c3-40f2-8e95-826b07e2641f.png)

总结：

+ @Autowired注解可以出现在：属性上、构造方法上、构造方法的参数上、setter方法上。
+ 当带参数的构造方法只有一个，@Autowired注解可以省略。
+ @Autowired注解默认根据类型注入。如果要根据名称注入的话，需要配合@Qualifier注解一起使用。

### @Resource

@Resource注解也可以完成非简单类型注入。那它和@Autowired注解有什么区别？

+ @Resource注解是JDK扩展包中的，也就是说属于JDK的一部分。所以该注解是标准注解，更加具有通用性。(JSR-250标准中制定的注解类型。JSR是Java规范提案。)
+ @Autowired注解是Spring框架自己的。
+ ****@Resource注解默认根据名称装配byName，未指定name时，使用属性名作为name。通过name找不到的话会自动启动通过类型byType装配。****
+ ****@Autowired注解默认根据类型装配byType，如果想根据名称装配，需要配合@Qualifier注解一起用。****
+ @Resource注解用在属性上、setter方法上。
+ @Autowired注解用在属性上、setter方法上、构造方法上、构造方法参数上。

@Resource注解属于JDK扩展包，所以不在JDK当中，需要额外引入以下依赖：【****如果是JDK8的话不需要额外引入依赖。高于JDK11或低于JDK8需要引入以下依赖。****】

```xml
<dependency>
  <groupId>jakarta.annotation</groupId>
  <artifactId>jakarta.annotation-api</artifactId>
  <version>2.1.1</version>
</dependency>
```

一定要注意：****如果你用Spring6+，要知道它不再支持JavaEE，它支持的是JakartaEE9。****

@Resource注解的源码如下：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1665565515435-2ad5614a-8572-4c6f-80c1-efa236dbe35f.png)

测试一下：

```java
@Repository("xyz")
public class UserDaoForOracle implements UserDao{
    @Override
    public void insert() {
        System.out.println("正在向Oracle数据库插入User数据");
    }
}
```

```java
@Service
public class UserService {

    @Resource(name = "xyz")
    private UserDao userDao;

    public void save(){
        userDao.insert();
    }
}
```

执行测试程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763805703043-58f861ec-79ca-409e-bc92-b731277c6dd3.png)

**我们把UserDaoForOracle的名字xyz修改为userDao，让这个Bean的名字和UserService类中的UserDao属性名一致：**

```java
@Repository("userDao")
public class UserDaoForOracle implements UserDao{
    @Override
    public void insert() {
        System.out.println("正在向Oracle数据库插入User数据");
    }
}

```

```java
@Service
public class UserService {

    @Resource
    private UserDao userDao;

    public void save(){
        userDao.insert();
    }
}

```

执行测试程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763805728365-2326f7c4-ecf6-440e-a6f7-e6dd40eb914b.png)

通过测试得知，当@Resource注解使用时没有指定name的时候，还是根据name进行查找，这个name是属性名。

接下来把UserService类中的属性名修改一下：

```java
@Service
public class UserService {

    @Resource
    private UserDao userDao2;

    public void save(){
        userDao2.insert();
    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763805768831-da788b4d-49b5-4dd0-a444-e2b0bed95b37.png)

根据异常信息得知：显然当通过name找不到的时候，自然会启动byType进行注入。以上的错误是因为UserDao接口下有两个实现类导致的。所以根据类型注入就会报错。

我们再来看@Resource注解使用在setter方法上可以吗？

```java
@Service
public class UserService {

    private UserDao userDao;

    @Resource
    public void setUserDao(UserDao userDao) {
        this.userDao = userDao;
    }

    public void save(){
        userDao.insert();
    }
}

```

注意这个setter方法的方法名，setUserDao去掉set之后，将首字母变小写userDao，userDao就是name

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763805795181-a8d504f6-ae7f-4ed0-af53-d42600cc3a52.png)

当然，也可以指定name：

```java
@Service
public class UserService {

    private UserDao userDao;

    @Resource(name = "userDaoForMySQL")
    public void setUserDao(UserDao userDao) {
        this.userDao = userDao;
    }

    public void save(){
        userDao.insert();
    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763805810622-0e5e2cb0-7aa9-45b6-bf56-f35c991e7ed4.png)

一句话总结@Resource注解：默认byName注入，没有指定name时把属性名当做name，根据name找不到时，才会byType注入。byType注入时，某种类型的Bean只能有一个。

---

## 全注解式开发

所谓的全注解开发就是不再使用spring配置文件了。写一个配置类来代替配置文件。

```java
package com.jkweilai.spring;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan({"com.jkweilai.spring.dao", "com.jkweilai.spring.service"})
public class SpringConfiguration {

    // 将自己new的对象纳入IoC容器的管理
    @Bean("myUserService")
    public UserService getUserService() {
        // 虽然是自己 new 的对象。如果对象中属性需要注入，Spring IoC容器会自动注入。不需要担心null。
        return new UserService();
    }
}

```

编写测试程序：不再new ClassPathXmlApplicationContext()对象了。

```java
@Test
public void testNoXml(){
    ApplicationContext applicationContext = new AnnotationConfigApplicationContext(SpringConfiguration.class);
    UserService userService = applicationContext.getBean("userService", UserService.class);
    userService.save();
    UserService myUserService = applicationContext.getBean("myUserService", UserService.class);
    myUserService.save();
}
```

以上内容主要掌握的注解有三个：

1. `@Configuration`
2. `@ComponentScan`
3. `@Bean`
