# Bean的作用域

---

## singleton

默认情况下，Spring的IoC容器创建的Bean对象是单例的。来测试一下：

```java
public class SpringBean {
}

```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="sb" class="com.jkweilai.spring.beans.SpringBean" />
    
</beans>
```

```java
@Test
public void testScope(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-scope.xml");

    SpringBean sb1 = applicationContext.getBean("sb", SpringBean.class);
    System.out.println(sb1);

    SpringBean sb2 = applicationContext.getBean("sb", SpringBean.class);
    System.out.println(sb2);
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763718986453-86ca83e3-8bbf-4c45-8699-e2ae7bbcc988.png)

通过测试得知：Spring的IoC容器中，默认情况下，Bean对象是单例的。

这个对象在什么时候创建的呢？可以为SpringBean提供一个无参数构造方法，测试一下，如下：

```java
public class SpringBean {
    public SpringBean() {
        System.out.println("SpringBean的无参数构造方法执行。");
    }
}

```

将测试程序中getBean()所在行代码注释掉：

```java
@Test
public void testScope(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-scope.xml");
}
```

执行测试程序：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763719064958-d248764f-59d7-4d41-b509-1d18b2e5191b.png)

通过测试得知，默认情况下，Bean对象的创建是在初始化Spring上下文的时候就完成的。

---

## prototype

如果想让Spring的Bean对象以多例的形式存在，可以在bean标签中指定scope属性的值为：****prototype****，这样Spring会在每一次执行getBean()方法的时候创建Bean对象，调用几次则创建几次。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="sb" class="com.jkweilai.spring.beans.SpringBean" scope="prototype" />

</beans>
```

```java
@Test
public void testScope(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-scope.xml");

    SpringBean sb1 = applicationContext.getBean("sb", SpringBean.class);
    System.out.println(sb1);

    SpringBean sb2 = applicationContext.getBean("sb", SpringBean.class);
    System.out.println(sb2);
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763719105263-11ce286c-1d5b-492c-8e36-fd21400b3b17.png)

我们可以把测试代码中的getBean()方法所在行代码注释掉：

```java
@Test
public void testScope(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-scope.xml");
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763719118424-ee74b420-f5a9-40af-86b6-e095da0924e6.png)

可以看到这一次在初始化Spring上下文的时候，并没有创建Bean对象。

那你可能会问：scope如果没有配置，它的默认值是什么呢？默认值是singleton，单例的。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="sb" class="com.jkweilai.spring.beans.SpringBean" />

</beans>
```

```java
@Test
public void testScope(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring-scope.xml");

    SpringBean sb1 = applicationContext.getBean("sb", SpringBean.class);
    System.out.println(sb1);

    SpringBean sb2 = applicationContext.getBean("sb", SpringBean.class);
    System.out.println(sb2);
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763719172933-83153245-ab36-4656-8fd4-4168e85edbd0.png)

通过测试得知，没有指定scope属性时，默认是singleton单例的。

---

## 其它scope

**scope属性的值不止两个，它一共包括8个选项：**

+ singleton：默认的，单例。
+ prototype：原型。每调用一次getBean()方法则获取一个新的Bean对象。或每次注入的时候都是新对象。
+ request：一个请求对应一个Bean。****仅限于在WEB应用中使用****。
+ session：一个会话对应一个Bean。****仅限于在WEB应用中使用****。
+ application：一个应用对应一个Bean。****仅限于在WEB应用中使用。****
+ websocket：一个websocket生命周期对应一个Bean。****仅限于在WEB应用中使用。****
+ 自定义scope：几乎用不上，感兴趣的可以研究。
