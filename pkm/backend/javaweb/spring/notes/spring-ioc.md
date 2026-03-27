# Spring对IoC的实现

---

## IoC 控制反转

+ 控制反转是一种思想。
+ 控制反转是为了降低程序耦合度，提高程序扩展力，达到OCP原则，达到DIP原则。
+ 控制反转，反转的是什么？
    - 将对象的创建权利交出去，交给第三方容器负责。
    - 将对象和对象之间关系的维护权交出去，交给第三方容器负责。
+ 控制反转这种思想如何实现呢？
    - DI（Dependency Injection）：依赖注入

---

## 依赖注入

依赖注入实现了控制反转的思想。

****Spring通过依赖注入的方式来完成Bean管理的。****

****Bean管理说的是：Bean对象的创建，以及Bean对象中属性的赋值（或者叫做Bean对象之间关系的维护）。****

依赖注入：

+ 依赖指的是对象和对象之间的关联关系。
+ 注入指的是一种数据传递行为，通过注入行为来让对象和对象产生关系。

依赖注入常见的实现方式包括两种：

+ 第一种：set注入
+ 第二种：构造注入

新建模块：spring-002-dependency-injection

### set注入

set注入，基于set方法实现的，底层会通过反射机制调用属性对应的set方法然后给属性赋值。这种方式要求属性必须对外提供set方法。

```java
package com.jkweilai.spring.dao;

public class UserDao {

    public void insert(){
        System.out.println("正在保存用户数据。");
    }
}

```

```java
package com.jkweilai.spring.service;

import com.jkweilai.spring.dao.UserDao;

public class UserService {

    private UserDao userDao;

    // 使用set方式注入，必须提供set方法。
    // 反射机制要调用这个方法给属性赋值的。
    public void setUserDao(UserDao userDao) {
        this.userDao = userDao;
    }

    public void save(){
        userDao.insert();
    }
}

```

像这样去配置他们的关系：

```xml
<bean id="userDaoBean" class="com.jkweilai.spring.dao.UserDao"/>

<bean id="userServiceBean" class="com.jkweilai.spring.service.UserService">
    <property name="userDao" ref="userDaoBean"/>
</bean>
```

```java
public class DITest {

    @Test
    public void testSetDI(){
        ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring.xml");
        UserService userService = applicationContext.getBean("userServiceBean", UserService.class);
        userService.save();
    }
}
```

运行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763703270197-41c911da-b886-43e5-9412-e31e91cdbb2b.png)

重点内容是，什么原理：

```xml
<bean id="userDaoBean" class="com.jkweilai.spring.dao.UserDao"/>

<bean id="userServiceBean" class="com.jkweilai.spring.service.UserService">
  <property name="userDao" ref="userDaoBean"/>
</bean>
```

实现原理：

+ 通过property标签获取到属性名：userDao
+ 通过属性名推断出set方法名：setUserDao
+ 通过反射机制调用setUserDao()方法给属性赋值
+ property标签的name是属性名。
+ property标签的ref是要注入的bean对象的id。****(通过ref属性来完成bean的装配，这是bean最简单的一种装配方式。装配指的是：创建系统组件之间关联的动作)****

**可以把set方法注释掉，再测试一下**：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763718228299-478ab23d-ebde-4f03-867e-fe4a91bf8d3c.png)

通过测试得知，底层实际上调用了setUserDao()方法。所以需要确保这个方法的存在。

我们现在把属性名修改一下，但方法名还是setUserDao()，我们来测试一下：

```java
public class UserService {

    private UserDao aaa;

    // 使用set方式注入，必须提供set方法。
    // 反射机制要调用这个方法给属性赋值的。
    public void setUserDao(UserDao userDao) {
        this.aaa = userDao;
    }

    public void save(){
        aaa.insert();
    }
}

```

运行测试程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763703431816-e00a0a7f-80e6-41c6-851a-484a6e0fc93a.png)

通过测试看到程序仍然可以正常执行，说明property标签的name是：setUserDao()方法名演变得到的。演变的规律是：

+ setUsername() 演变为 username
+ setPassword() 演变为 password
+ setUserDao() 演变为 userDao
+ setUserService() 演变为 userService

另外，对于property标签来说，ref属性也可以采用标签的方式，但使用ref属性是多数的：

```xml
<bean id="userServiceBean" class="com.jkweilai.spring.service.UserService">
  <property name="userDao">
    <ref bean="userDaoBean"/>
  </property>
</bean>
```

****总结：set注入的核心实现原理：通过反射机制调用set方法来给属性赋值，让两个对象之间产生关系。****

****

### 构造注入

核心原理：通过调用构造方法来给属性赋值。

```java
public class OrderDao {
    public void deleteById(){
        System.out.println("正在删除订单。。。");
    }
}
```

```java
public class OrderService {
    private OrderDao orderDao;

    // 通过反射机制调用构造方法给属性赋值
    public OrderService(OrderDao orderDao) {
        this.orderDao = orderDao;
    }

    public void delete(){
        orderDao.deleteById();
    }
}
```

```xml
<bean id="orderDaoBean" class="com.jkweilai.spring.dao.OrderDao"/>
<bean id="orderServiceBean" class="com.jkweilai.spring.service.OrderService">
  <!--index="0"表示构造方法的第一个参数，将orderDaoBean对象传递给构造方法的第一个参数。-->
  <constructor-arg index="0" ref="orderDaoBean"/>
</bean>
```

```java
@Test
public void testConstructorDI(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring.xml");
    OrderService orderServiceBean = applicationContext.getBean("orderServiceBean", OrderService.class);
    orderServiceBean.delete();
}
```

运行结果如下：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763703541233-f144603f-0a7c-4efc-be49-7e4cb31ee9f0.png)

****

****如果构造方法有两个参数：****

```java
public class OrderService {
    private OrderDao orderDao;
    private UserDao userDao;

    // 通过反射机制调用构造方法给属性赋值
    public OrderService(OrderDao orderDao, UserDao userDao) {
        this.orderDao = orderDao;
        this.userDao = userDao;
    }

    public void delete(){
        orderDao.deleteById();
        userDao.insert();
    }
}

```

spring配置文件：

```xml
<bean id="orderDaoBean" class="com.jkweilai.spring.dao.OrderDao"/>

<bean id="orderServiceBean" class="com.jkweilai.spring.service.OrderService">
  <!--第一个参数下标是0-->
  <constructor-arg index="0" ref="orderDaoBean"/>
  <!--第二个参数下标是1-->
  <constructor-arg index="1" ref="userDaoBean"/>
</bean>

<bean id="userDaoBean" class="com.jkweilai.spring.dao.UserDao"/>
```

执行测试程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763703565658-98132ed3-4e4c-4524-9633-89ecbb517c76.png)

****

****不使用参数下标，使用参数的名字可以吗？****

```xml
<bean id="orderDaoBean" class="com.jkweilai.spring.dao.OrderDao"/>

<bean id="orderServiceBean" class="com.jkweilai.spring.service.OrderService">
  <!--这里使用了构造方法上参数的名字-->
  <constructor-arg name="orderDao" ref="orderDaoBean"/>
  <constructor-arg name="userDao" ref="userDaoBean"/>
</bean>

<bean id="userDaoBean" class="com.jkweilai.spring.dao.UserDao"/>
```

执行测试程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763703580933-9558d7db-975e-4289-969b-d910c1b3d3ee.png)

****不指定参数下标，不指定参数名字，可以吗？****

```xml
<bean id="orderDaoBean" class="com.jkweilai.spring.dao.OrderDao"/>
<bean id="orderServiceBean" class="com.jkweilai.spring.service.OrderService">
  <!--没有指定下标，也没有指定参数名字-->
  <constructor-arg ref="orderDaoBean"/>
  <constructor-arg ref="userDaoBean"/>
</bean>

<bean id="userDaoBean" class="com.jkweilai.spring.dao.UserDao"/>
```

执行测试程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763703580933-9558d7db-975e-4289-969b-d910c1b3d3ee.png)

****

****配置文件中构造方法参数的类型顺序和构造方法参数的类型顺序不一致呢？****

```xml
<bean id="orderDaoBean" class="com.jkweilai.spring.dao.OrderDao"/>

<bean id="orderServiceBean" class="com.jkweilai.spring.service.OrderService">
  <!--顺序已经和构造方法的参数顺序不同了-->
  <constructor-arg ref="userDaoBean"/>
  <constructor-arg ref="orderDaoBean"/>
</bean>

<bean id="userDaoBean" class="com.jkweilai.spring.dao.UserDao"/>
```

执行测试程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763703580933-9558d7db-975e-4289-969b-d910c1b3d3ee.png)

通过测试得知，通过构造方法注入的时候：

+ 可以通过下标
+ 可以通过参数名
+ 也可以不指定下标和参数名，可以类型自动推断。

Spring在装配方面做的还是比较健壮的。

---

## set注入专题

### 注入外部Bean

在之前4.2.1中使用的案例就是注入外部Bean的方式。

```xml
<bean id="userDaoBean" class="com.jkweilai.spring.dao.UserDao"/>

<bean id="userServiceBean" class="com.jkweilai.spring.service.UserService">
    <property name="userDao" ref="userDaoBean"/>
</bean>
```

外部Bean的特点：bean定义到外面，在property标签中使用ref属性进行注入。通常这种方式是常用的。

### 注入内部Bean

内部Bean的方式：在bean标签中嵌套bean标签。

```xml
<bean id="userServiceBean" class="com.jkweilai.spring.service.UserService">
    <property name="userDao">
        <bean class="com.jkweilai.spring.dao.UserDao"/>
    </property>
</bean>
```

```java
@Test
public void testInnerBean(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-inner-bean.xml");
    UserService userService = applicationContext.getBean("userServiceBean", UserService.class);
    userService.save();
}
```

执行测试程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763703724923-3d6fe488-4cc4-464a-9fb4-46737d190786.png)

这种方式作为了解。

### 注入简单类型

我们之前在进行注入的时候，对象的属性是另一个对象。

```java
public class UserService{
    
    private UserDao userDao;
    
    public void setUserDao(UserDao userDao){
        this.userDao = userDao;
    }
    
}
```

那如果对象的属性是int类型呢？

```java
public class User{
    
    private int age;
    
    public void setAge(int age){
        this.age = age;
    }
    
}
```

可以通过set注入的方式给该属性赋值吗？

+ 当然可以。因为只要能够调用set方法就可以给属性赋值。

**编写程序给一个User对象的age属性赋值20：**

第一步：定义User类，提供age属性，提供age属性的setter方法。

```java
public class User {
    private int age;

    public void setAge(int age) {
        this.age = age;
    }
    
    @Override
    public String toString() {
        return "User{" +
                "age=" + age +
                '}';
    }
}

```

第二步：编写spring配置文件：spring-simple-type.xml

```xml
<bean id="userBean" class="com.jkweilai.spring.beans.User">
    <!--如果像这种int类型的属性，我们称为简单类型，这种简单类型在注入的时候要使用value属性，不能使用ref-->
    <!--<property name="age" value="20"/>-->
    <property name="age">
        <value>20</value>
    </property>
</bean>
```

第三步：编写测试程序

```java
@Test
public void testSimpleType(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-simple-type.xml");
    User user = applicationContext.getBean("userBean", User.class);
    System.out.println(user);
}
```

第四步：运行测试程序

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763703886349-7e587def-2b4f-4abf-aff0-6c0f41011328.png)

****

****需要特别注意：如果给简单类型赋值，使用value属性或value标签。而不是ref。****

简单类型包括哪些呢？可以通过Spring的源码来分析一下：BeanUtils类、ClassUtils类：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1726729479656-34799374-2f4a-4d05-a2ce-89defea2ad21.png)

简单类型包括：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1726729370217-81b396a1-bf0b-4459-9b15-2c1e77c37093.png)

**经典案例：给数据源的属性注入值：**

假设我们现在要自己手写一个数据源，我们都知道所有的数据源都要实现javax.sql.DataSource接口，并且数据源中应该有连接数据库的信息，例如：driver、url、username、password等。

```java
public class MyDataSource implements DataSource {
    private String driver;
    private String url;
    private String username;
    private String password;

    public void setDriver(String driver) {
        this.driver = driver;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    
    @Override
    public String toString() {
        return "MyDataSource{" +
                "driver='" + driver + '\'' +
                ", url='" + url + '\'' +
                ", username='" + username + '\'' +
                ", password='" + password + '\'' +
                '}';
    }

    @Override
    public Connection getConnection() throws SQLException {
        return null;
    }

    @Override
    public Connection getConnection(String username, String password) throws SQLException {
        return null;
    }

    @Override
    public PrintWriter getLogWriter() throws SQLException {
        return null;
    }

    @Override
    public void setLogWriter(PrintWriter out) throws SQLException {

    }

    @Override
    public void setLoginTimeout(int seconds) throws SQLException {

    }

    @Override
    public int getLoginTimeout() throws SQLException {
        return 0;
    }

    @Override
    public Logger getParentLogger() throws SQLFeatureNotSupportedException {
        return null;
    }

    @Override
    public <T> T unwrap(Class<T> iface) throws SQLException {
        return null;
    }

    @Override
    public boolean isWrapperFor(Class<?> iface) throws SQLException {
        return false;
    }
}

```

我们给driver、url、username、password四个属性分别提供了setter方法，我们可以使用spring的依赖注入完成数据源对象的创建和属性的赋值吗？看配置文件

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
  
    <bean id="dataSource" class="com.jkweilai.spring.beans.MyDataSource">
        <property name="driver" value="com.mysql.cj.jdbc.Driver"/>
        <property name="url" value="jdbc:mysql://localhost:3306/spring"/>
        <property name="username" value="root"/>
        <property name="password" value="123456"/>
    </bean>
  
</beans>
```

测试程序：

```java
@Test
public void testDataSource(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-datasource.xml");
    MyDataSource dataSource = applicationContext.getBean("dataSource", MyDataSource.class);
    System.out.println(dataSource);
}
```

执行测试程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763703988968-74f61c13-64c3-4af9-aa3f-0124482b808d.png)

你学会了吗？

****

### 级联属性赋值（了解）

```java
public class Clazz {
    private String name;

    public Clazz() {
    }

    public Clazz(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Clazz{" +
                "name='" + name + '\'' +
                '}';
    }
}

```

```java
public class Student {
    private String name;
    private Clazz clazz;

    public Student() {
    }

    public Student(String name, Clazz clazz) {
        this.name = name;
        this.clazz = clazz;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setClazz(Clazz clazz) {
        this.clazz = clazz;
    }

    public Clazz getClazz() {
        return clazz;
    }

    @Override
    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                ", clazz=" + clazz +
                '}';
    }
}

```

```xml
<bean id="clazzBean" class="com.jkweilai.spring.beans.Clazz"/>

<bean id="student" class="com.jkweilai.spring.beans.Student">
    <property name="name" value="张三"/>

    <!--要点1：以下两行配置的顺序不能颠倒-->
    <property name="clazz" ref="clazzBean"/>
    <!--要点2：clazz属性必须有getter方法-->
    <property name="clazz.name" value="高三一班"/>
</bean>
```

```java
@Test
public void testCascade(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-cascade.xml");
    Student student = applicationContext.getBean("student", Student.class);
    System.out.println(student);
}
```

运行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763704075496-763dcaba-4244-4d90-8b1b-a2b6c8148730.png)

****要点：****

+ ****在spring配置文件中，如上，注意顺序。****
+ ****在spring配置文件中，clazz属性必须提供getter方法。****

****

### 注入数组

**当数组中的元素是简单类型**：

```java
package com.jkweilai.spring.beans;

import java.util.Arrays;

public class Person {
    private String[] favoriteFoods;

    public void setFavoriteFoods(String[] favoriteFoods) {
        this.favoriteFoods = favoriteFoods;
    }

    @Override
    public String toString() {
        return "Person{" +
                "favoriteFoods=" + Arrays.toString(favoriteFoods) +
                '}';
    }
}

```

```xml
<bean id="person" class="com.jkweilai.spring.beans.Person">
    <property name="favoriteFoods">
        <array>
            <value>鸡排</value>
            <value>汉堡</value>
            <value>鹅肝</value>
        </array>
    </property>
</bean>
```

```java
@Test
public void testArraySimple(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-array-simple.xml");
    Person person = applicationContext.getBean("person", Person.class);
    System.out.println(person);
}
```

**当数组中的元素是非简单类型：一个订单中包含多个商品。**

```java
public class Goods {
    private String name;

    public Goods() {
    }

    public Goods(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Goods{" +
                "name='" + name + '\'' +
                '}';
    }
}

```

```java
public class Order {
    // 一个订单中有多个商品
    private Goods[] goods;

    public Order() {
    }

    public Order(Goods[] goods) {
        this.goods = goods;
    }

    public void setGoods(Goods[] goods) {
        this.goods = goods;
    }

    @Override
    public String toString() {
        return "Order{" +
                "goods=" + Arrays.toString(goods) +
                '}';
    }
}

```

```xml
<bean id="goods1" class="com.jkweilai.spring.beans.Goods">
    <property name="name" value="西瓜"/>
</bean>

<bean id="goods2" class="com.jkweilai.spring.beans.Goods">
    <property name="name" value="苹果"/>
</bean>

<bean id="order" class="com.jkweilai.spring.beans.Order">
    <property name="goods">
        <array>
            <!--这里使用ref标签即可-->
            <ref bean="goods1"/>
            <ref bean="goods2"/>
        </array>
    </property>
</bean>
```

测试程序：

```java
@Test
public void testArray(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-array.xml");
    Order order = applicationContext.getBean("order", Order.class);
    System.out.println(order);
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763717431738-ef375752-075c-43bd-bf25-d62f957e52f2.png)

****要点：****

+ ****如果数组中是简单类型，使用value标签。****
+ ****如果数组中是非简单类型，使用ref标签。****

****

### 注入List集合

List集合：有序可重复

```java
public class People {
    // 一个人有多个名字
    private List<String> names;

    public void setNames(List<String> names) {
        this.names = names;
    }

    @Override
    public String toString() {
        return "People{" +
                "names=" + names +
                '}';
    }
}

```

```xml
<bean id="peopleBean" class="com.jkweilai.spring.beans.People">
    <property name="names">
        <list>
            <value>铁锤</value>
            <value>张三</value>
            <value>张三</value>
            <value>张三</value>
            <value>狼</value>
        </list>
    </property>
</bean>
```

```java
@Test
public void testCollection(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-collection.xml");
    People peopleBean = applicationContext.getBean("peopleBean", People.class);
    System.out.println(peopleBean);
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763717474219-f00a5de9-fe99-401d-8540-0dfb59671bb2.png)

****注意：注入List集合的时候使用list标签，如果List集合中是简单类型使用value标签，反之使用ref标签。****

****

### 注入Set集合

Set集合：无序不可重复

```java
public class People {
    // 一个人有多个电话
    private Set<String> phones;

    public void setPhones(Set<String> phones) {
        this.phones = phones;
    }
    
    //......
    
    @Override
    public String toString() {
        return "People{" +
                "phones=" + phones +
                ", names=" + names +
                '}';
    }
}

```

```xml
<bean id="peopleBean" class="com.jkweilai.spring.beans.People">
    <property name="phones">
        <set>
            <!--非简单类型可以使用ref，简单类型使用value-->
            <value>110</value>
            <value>110</value>
            <value>120</value>
            <value>120</value>
            <value>119</value>
            <value>119</value>
        </set>
    </property>
</bean>
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763717525860-5898bf62-8e74-438d-afee-979fb446ff0f.png)

****要点：****

+ ****使用<set>标签****
+ ****set集合中元素是简单类型的使用value标签，反之使用ref标签。****

****

### 注入Map集合

```java
public class People {
    // 一个人有多个住址
    private Map<Integer, String> addrs;

    public void setAddrs(Map<Integer, String> addrs) {
        this.addrs = addrs;
    }
    
    //......
    
    @Override
    public String toString() {
        return "People{" +
                "addrs=" + addrs +
                ", phones=" + phones +
                ", names=" + names +
                '}';
    }

}

```

```xml
<bean id="peopleBean" class="com.jkweilai.spring.beans.People">
    <property name="addrs">
        <map>
            <!--如果key不是简单类型，使用 key-ref 属性-->
            <!--如果value不是简单类型，使用 value-ref 属性-->
            <entry key="1" value="北京海淀"/>
            <entry key="2" value="上海浦东"/>
            <entry key="3" value="天津南开"/>
        </map>
    </property>
</bean>
```

****要点：****

+ ****使用<map>标签****
+ ****如果key是简单类型，使用 key 属性，反之使用 key-ref 属性。****
+ ****如果value是简单类型，使用 value 属性，反之使用 value-ref 属性。****

****

### 注入Properties

java.util.Properties继承java.util.Hashtable，所以Properties也是一个Map集合。

```java
public class People {

    private Properties properties;

    public void setProperties(Properties properties) {
        this.properties = properties;
    }
    
    //......

    @Override
    public String toString() {
        return "People{" +
                "properties=" + properties +
                ", addrs=" + addrs +
                ", phones=" + phones +
                ", names=" + names +
                '}';
    }
}

```

```xml
<bean id="peopleBean" class="com.jkweilai.spring.beans.People">
    <property name="properties">
        <props>
            <prop key="driver">com.mysql.cj.jdbc.Driver</prop>
            <prop key="url">jdbc:mysql://localhost:3306/spring</prop>
            <prop key="username">root</prop>
            <prop key="password">123456</prop>
        </props>
    </property>
</bean>
```

执行测试程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763717687274-17ec7c70-16b4-4a1a-b67b-d252ccfef797.png)

****要点：****

+ ****使用<props>标签嵌套<prop>标签完成。****

****

### 注入null和空字符串

注入空字符串使用：<value/> 或者 value=""

注入null使用：<null/> 或者 不为该属性赋值

+ 我们先来看一下，怎么注入空字符串。

```java
public class Vip {
    private String email;

    public void setEmail(String email) {
        this.email = email;
    }

    @Override
    public String toString() {
        return "Vip{" +
                "email='" + email + '\'' +
                '}';
    }
}

```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="vipBean" class="com.jkweilai.spring.beans.Vip">
        <!--空串的第一种方式-->
        <!--<property name="email" value=""/>-->
        <!--空串的第二种方式-->
        <property name="email">
            <value/>
        </property>
    </bean>

</beans>
```

```java
@Test
public void testNull(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-null.xml");
    Vip vipBean = applicationContext.getBean("vipBean", Vip.class);
    System.out.println(vipBean);
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763717731445-35c6fea4-2f21-4450-b29c-2111f2ce1d7a.png)

+ 怎么注入null呢？

第一种方式：不给属性赋值

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="vipBean" class="com.jkweilai.spring.beans.Vip" />

</beans>
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763717749034-ffa72b1d-fb17-4b6d-8f2c-d6b88208bae1.png)

第二种方式：使用<null/>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="vipBean" class="com.jkweilai.spring.beans.Vip">
        <property name="email">
            <null/>
        </property>
    </bean>

</beans>
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763717759124-7724e7c6-92ba-4ae8-b3e1-d9cd847c712e.png)

### 注入的值中含有特殊符号

XML中有5个特殊字符，分别是：`<``>``'``"``&`

以上5个特殊符号在XML中会被特殊对待，会被当做XML语法的一部分进行解析，如果这些特殊符号直接出现在注入的字符串当中，会报错。

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763718169577-c2150391-6ada-4ba4-8d78-ed66ce8db5f4.png)

解决方案包括两种：

+ 第一种：特殊符号使用转义字符代替。
+ 第二种：将含有特殊符号的字符串放到：<![CDATA[]]> 当中。因为放在CDATA区中的数据不会被XML文件解析器解析。

5个特殊字符对应的转义字符分别是：

| **特殊字符** | **转义字符** |
| --- | --- |
| > | &gt; |
| < | &lt; |
| ' | &apos; |
| " | &quot; |
| & | &amp; |

先使用转义字符来代替：

```java
public class Math {
    private String result;

    public void setResult(String result) {
        this.result = result;
    }

    @Override
    public String toString() {
        return "Math{" +
                "result='" + result + '\'' +
                '}';
    }
}

```

```xml
<bean id="mathBean" class="com.jkweilai.spring.beans.Math">
    <property name="result" value="2 &lt; 3"/>
</bean>
```

```java
@Test
public void testSpecial(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-special.xml");
    Math mathBean = applicationContext.getBean("mathBean", Math.class);
    System.out.println(mathBean);
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763717850747-fe3fa73b-806c-4ae2-ab0f-06e5359075e6.png)

我们再来使用CDATA方式：

```xml
<bean id="mathBean" class="com.jkweilai.spring.beans.Math">
    <property name="result">
        <!--只能使用value标签-->
        <value><![CDATA[2 < 3]]></value>
    </property>
</bean>
```

****注意：使用CDATA时，不能使用value属性，只能使用value标签。****

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763717882333-4ff84443-b20b-499b-bf88-bc489e189fe1.png)

---

## p命名空间注入

目的：简化配置。

使用p命名空间注入的前提条件包括两个：

+ 第一：在XML头部信息中添加p命名空间的配置信息：xmlns:p="[http://www.springframework.org/schema/p"](http://www.springframework.org/schema/p")
+ 第二：p命名空间注入是基于setter方法的，所以需要对应的属性提供setter方法。

```java
public class Customer {
    private String name;
    private int age;

    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "Customer{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}

```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:p="http://www.springframework.org/schema/p"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="customerBean" class="com.jkweilai.spring.beans.Customer" p:name="zhangsan" p:age="20"/>

</beans>
```

```java
@Test
public void testP(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-p.xml");
    Customer customerBean = applicationContext.getBean("customerBean", Customer.class);
    System.out.println(customerBean);
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763718009839-ade48dfb-1431-4f10-a994-4ab8374ef367.png)

把setter方法去掉：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763718119042-3c78856d-6f8b-4b23-8559-51d174a399f9.png)

所以p命名空间实际上是对set注入的简化。

---

## c命名空间注入

c命名空间是简化构造方法注入的。

使用c命名空间的两个前提条件：

第一：需要在xml配置文件头部添加信息：**xmlns:****c****="http://www.springframework.org/schema/c"**

第二：需要提供构造方法。

```java
public class MyTime {
    private int year;
    private int month;
    private int day;

    public MyTime(int year, int month, int day) {
        this.year = year;
        this.month = month;
        this.day = day;
    }

    @Override
    public String toString() {
        return "MyTime{" +
                "year=" + year +
                ", month=" + month +
                ", day=" + day +
                '}';
    }
}

```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:c="http://www.springframework.org/schema/c"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
  
    <bean id="myTimeBean" class="com.jkweilai.spring.beans.MyTime" c:_0="2008" c:_1="8" c:_2="8"/>

</beans>
```

```java
@Test
public void testC(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-c.xml");
    MyTime myTimeBean = applicationContext.getBean("myTimeBean", MyTime.class);
    System.out.println(myTimeBean);
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763718096636-e9af0497-bb5a-4341-bf38-eabde32ba060.png)

把构造方法注释掉：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763718138114-98841768-357f-4408-aef7-7c57107cdb3e.png)

所以，c命名空间是依靠构造方法的。

****注意：不管是p命名空间还是c命名空间，注入的时候都可以注入简单类型以及非简单类型。****

****

---

## util命名空间

使用util命名空间可以让****配置复用****。

使用util命名空间的前提是：在spring配置文件头部添加配置信息。如下：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1665218059794-30411b76-a22c-4339-ab60-acad8f02ab28.png)

```java
public class MyDataSource1 {
    private Properties properties;

    public void setProperties(Properties properties) {
        this.properties = properties;
    }

    @Override
    public String toString() {
        return "MyDataSource1{" +
                "properties=" + properties +
                '}';
    }
}

```

```java
public class MyDataSource2 {
    private Properties properties;

    public void setProperties(Properties properties) {
        this.properties = properties;
    }

    @Override
    public String toString() {
        return "MyDataSource2{" +
                "properties=" + properties +
                '}';
    }
}

```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:util="http://www.springframework.org/schema/util"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
                           http://www.springframework.org/schema/util http://www.springframework.org/schema/util/spring-util.xsd">

    <util:properties id="prop">
        <prop key="driver">com.mysql.cj.jdbc.Driver</prop>
        <prop key="url">jdbc:mysql://localhost:3306/spring</prop>
        <prop key="username">root</prop>
        <prop key="password">123456</prop>
    </util:properties>

    <bean id="dataSource1" class="com.jkweilai.spring.beans.MyDataSource1">
        <property name="properties" ref="prop"/>
    </bean>

    <bean id="dataSource2" class="com.jkweilai.spring.beans.MyDataSource2">
        <property name="properties" ref="prop"/>
    </bean>
</beans>
```

```java
@Test
public void testUtil(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-util.xml");

    MyDataSource1 dataSource1 = applicationContext.getBean("dataSource1", MyDataSource1.class);
    System.out.println(dataSource1);

    MyDataSource2 dataSource2 = applicationContext.getBean("dataSource2", MyDataSource2.class);
    System.out.println(dataSource2);
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763718455643-7d9355ac-8556-47fe-ab67-1e2349d580e2.png)

---

## 基于XML的自动装配

Spring还可以完成自动化的注入，自动化注入又被称为自动装配。它可以根据****名字****进行自动装配，也可以根据****类型****进行自动装配。

### 根据名称自动装配

```java
public class UserDao {

    public void insert(){
        System.out.println("正在保存用户数据。");
    }
}

```

```java
public class UserService {

    private UserDao aaa;

    // 这个set方法非常关键
    public void setAaa(UserDao aaa) {
        this.aaa = aaa;
    }

    public void save(){
        aaa.insert();
    }
}

```

Spring的配置文件这样配置：

```xml
<bean id="userService" class="com.jkweilai.spring.service.UserService" autowire="byName"/>

<bean id="aaa" class="com.jkweilai.spring.dao.UserDao"/>
```

这个配置起到关键作用：

+ UserService Bean中需要添加autowire="byName"，表示通过名称进行装配。
+ UserService类中有一个UserDao属性，而UserDao属性的名字是aaa，****对应的set方法是setAaa()****，正好和UserDao Bean的id是一样的。这就是根据名称自动装配。

```java
@Test
public void testAutowireByName(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-autowire.xml");
    UserService userService = applicationContext.getBean("userService", UserService.class);
    userService.save();
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763718549628-c1b58d51-d746-4d9e-aeb0-c8c5ee1f0a59.png)

我们来测试一下，byName装配是和属性名有关还是和set方法名有关系：

```java
public class UserService {
    // 这里没修改
    private UserDao aaa;

    /*public void setAaa(UserDao aaa) {
        this.aaa = aaa;
    }*/

    // set方法名变化了
    public void setDao(UserDao aaa){
        this.aaa = aaa;
    }

    public void save(){
        aaa.insert();
    }
}

```

在执行测试程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763718582395-53105c38-4844-412e-bcba-cc52e90013ab.png)

通过测试得知，aaa属性并没有赋值成功。也就是并没有装配成功。

我们将spring配置文件修改以下：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
  
  <bean id="userService" class="com.jkweilai.spring.service.UserService" autowire="byName"/>
  <!--这个id修改了-->
  <bean id="dao" class="com.jkweilai.spring.dao.UserDao"/>
  
</beans>
```

执行测试程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763718621703-01a7eaa0-f0cb-44c1-80f6-d113eb52eb86.png)

这说明，如果根据名称装配(byName)，底层会调用set方法进行注入。

例如：setAge() 对应的名字是age，setPassword()对应的名字是password，setEmail()对应的名字是email。

### 根据类型自动装配

```java
public class AccountDao {
    public void insert(){
        System.out.println("正在保存账户信息");
    }
}

```

```java
public class AccountService {
    private AccountDao accountDao;

    public void setAccountDao(AccountDao accountDao) {
        this.accountDao = accountDao;
    }

    public void save(){
        accountDao.insert();
    }
}

```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <!--byType表示根据类型自动装配-->
    <bean id="accountService" class="com.jkweilai.spring.service.AccountService" autowire="byType"/>

    <bean class="com.jkweilai.spring.dao.AccountDao"/>

</beans>
```

```java
@Test
public void testAutowireByType(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-autowire.xml");
    AccountService accountService = applicationContext.getBean("accountService", AccountService.class);
    accountService.save();
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763718680599-8c83ff07-8541-4638-9607-6b2a2585c4c3.png)

我们把UserService中的set方法注释掉，再执行：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763718687238-6eb11940-af46-4b9f-81cd-7715d0605040.png)

可以看到无论是byName还是byType，在装配的时候都是基于set方法的。所以set方法是必须要提供的。提供构造方法是不行的，大家可以测试一下。这里就不再赘述。

如果byType，根据类型装配时，如果配置文件中有两个类型一样的bean会出现什么问题呢？

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="accountService" class="com.jkweilai.spring.service.AccountService" autowire="byType"/>

    <bean id="x" class="com.jkweilai.spring.dao.AccountDao"/>
    <bean id="y" class="com.jkweilai.spring.dao.AccountDao"/>

</beans>
```

执行测试程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763718715528-42fe5699-776e-4cd1-b4d2-6bc55d8590be.png)

测试结果说明了，当byType进行自动装配的时候，配置文件中某种类型的Bean必须是唯一的，不能出现多个。

---

## Spring引入外部属性配置文件

我们都知道编写数据源的时候是需要连接数据库的信息的，例如：driver url username password等信息。这些信息可以单独写到一个属性配置文件中吗，这样用户修改起来会更加的方便。当然可以。

第一步：写一个数据源类，提供相关属性。

```java
public class MyDataSource implements DataSource {
    @Override
    public String toString() {
        return "MyDataSource{" +
                "driver='" + driver + '\'' +
                ", url='" + url + '\'' +
                ", username='" + username + '\'' +
                ", password='" + password + '\'' +
                '}';
    }

    private String driver;
    private String url;
    private String username;
    private String password;

    public void setDriver(String driver) {
        this.driver = driver;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    //......
}

```

第二步：在类路径下新建jdbc.properties文件，并配置信息。

```properties
driver=com.mysql.cj.jdbc.Driver
url=jdbc:mysql://localhost:3306/spring
username=root
password=root123
```

第三步：在spring配置文件中引入context命名空间。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
                           http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">

</beans>
```

第四步：在spring中配置使用jdbc.properties文件。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
                           http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">

    <context:property-placeholder location="jdbc.properties"/>
    
    <bean id="dataSource" class="com.jkweilai.spring.beans.MyDataSource">
        <property name="driver" value="${driver}"/>
        <property name="url" value="${url}"/>
        <property name="username" value="${username}"/>
        <property name="password" value="${password}"/>
    </bean>
</beans>
```

测试程序：

```java
@Test
public void testProperties(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-properties.xml");
    MyDataSource dataSource = applicationContext.getBean("dataSource", MyDataSource.class);
    System.out.println(dataSource);
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763718790927-1686291f-2da2-4f2b-a8b5-e22901e90044.png)

****这里有一个坑。******配置文件中用户名是**`**root**`**，但是取出来的是**`**Adminitrator**`**。什么原因？**

**这个问题很常见，是因为系统环境变量的优先级导致的。Spring在解析**`**${}**`**占位符时，会按照以下顺序查找：**

1. ****系统环境变量******（如**`**USERNAME**`**）**
2. ****JVM 系统属性******（**`**System.getProperties()**`**）**
3. ****属性文件******中定义的值**

**在Windows系统中，**`**USERNAME**`**是一个默认的环境变量，存储了当前登录用户的用户名，所以Spring会优先使用这个值而不是你属性文件中的值。**

****解决这个问题很简单：****

```properties
jdbc.driver=com.mysql.cj.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:3306/spring
jdbc.username=root
jdbc.password=root123
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
                           http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">

    <context:property-placeholder location="jdbc.properties"/>
    
    <bean id="dataSource" class="com.jkweilai.spring.beans.MyDataSource">
        <property name="driver" value="${jdbc.driver}"/>
        <property name="url" value="${jdbc.url}"/>
        <property name="username" value="${jdbc.username}"/>
        <property name="password" value="${jdbc.password}"/>
    </bean>
</beans>
```
