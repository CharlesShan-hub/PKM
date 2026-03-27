# list（写法和数组一样）

customer-list:
  - customer-name: joke
    age: 30
  - customer-name: susan
    age: 40

```

代码如下：

```java

package com.jkweilai.sb307externalconfig.bean;

import org.springframework.boot.context.properties.ConfigurationProperties;

import java.util.Arrays;
import java.util.List;
import java.util.Map;

@ConfigurationProperties
public class CollectionConfig {
    private String[] names;
    private List<Product> products;
    private Map<String, Vip> vips;

    @Override
    public String toString() {
        return "CollectionConfig{" +
                "names=" + Arrays.toString(names) +
                ", products=" + products +
                ", vips=" + vips +
                '}';
    }

    public String[] getNames() {
        return names;
    }

    public void setNames(String[] names) {
        this.names = names;
    }

    public List<Product> getProducts() {
        return products;
    }

    public void setProducts(List<Product> products) {
        this.products = products;
    }

    public Map<String, Vip> getVips() {
        return vips;
    }

    public void setVips(Map<String, Vip> vips) {
        this.vips = vips;
    }
}

class Product {
    private String name;
    private Double price;

    @Override
    public String toString() {
        return "Product{" +
                "name='" + name + '\'' +
                ", price=" + price +
                '}';
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Double getPrice() {
        return price;
    }

    public void setPrice(Double price) {
        this.price = price;
    }
}

class Vip {
    private String name;
    private Integer age;

    @Override
    public String toString() {
        return "Vip{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }
}

```

配置信息如下：`application.yml`

```yaml

#数组
names:
  - jackson
  - lucy
  - lili

#List集合
products: 
  - name: 西瓜
    price: 3.0
  - name: 苹果
    price: 2.0

#Map集合
vips:
  vip1:
    name: 张三
    age: 20
  vip2:
    name: 李四
    age: 22

```

提醒：记得入口程序使用**@ConfigurationPropertiesScan(basePackages = "com.jkweilai.sb307externalconfig.bean")进行标注。编写测试程序，执行结果如下：**

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729680626317-8b45a7b3-9117-47da-ac28-f153ac4d3d49.png" width="1554" title="" crop="0,0,1,1" id="u627f6edf" class="ne-image">

### 将配置绑定到第三方对象

**知识点列表：**

1. **如果 Bean 的源码我们接触不到，无法编辑源码，如何将配置文件的信息绑定到这个对象上？**
2. **使用 **`**@Bean**`**+**`**@ConfigurationProperties**`**可以实现。你只需要这么做，其他注解都不需要：**

```java

@Bean
@ConfigurationProperties
public SpringBean springBean() {
    return new SpringBean();
}

```

将配置文件中的信息绑定到某个Bean对象上，如果这个Bean对象没有源码，是第三方库提供的，怎么办？

此时可以单独编写一个方法，在方法上使用以下两个注解进行标注：

+ **@Bean**
+ **@ConfigurationProperties**

假设我们有这样一个类`Address`，代码如下：

```java

package com.jkweilai.sb307externalconfig.bean;

public class Address {
    private String city;
    private String street;
    private String zipcode;

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }

    public String getZipcode() {
        return zipcode;
    }

    public void setZipcode(String zipcode) {
        this.zipcode = zipcode;
    }

    @Override
    public String toString() {
        return "Address{" +
                "city='" + city + '\'' +
                ", street='" + street + '\'' +
                ", zipcode='" + zipcode + '\'' +
                '}';
    }
}

```

当然，我们是看不到这个源码的，只知道有这样一个字节码`Address.class`。大家也可以看到这个`Address`类上没有添加任何注解。假设我们要将以下配置绑定到这个Bean上应该怎么做？

```yaml

address:
  city: TJ
  street: XiangYangLu
  zipcode: 11111111

```

实现代码如下：

```java

@Configuration
public class ApplicationConfig {
    @Bean
    @ConfigurationProperties(prefix = "address")
    public Address getAddress(){
        return new Address();
    }
}

```

运行结果如下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729674936611-e86b3cad-c910-4f00-bb9f-8d5f976f8d94.png" width="615" title="" crop="0,0,1,1" id="ubdf95c9b" class="ne-image">

### 指定数据来源

**知识点列表：**

1. **如果需要加载的配置不是 **`**application.properties**`**中的，可以使用 **`**@PropertySource**`**来指定数据的来源。**
2. **@PropertySource("classpath:a/b/group-info.properties")**

之前所讲的内容是将Spring Boot框架默认的配置文件`application.properties`或`application.yml`作为数据的来源绑定到Bean上。如果配置信息没有在默认的配置文件中呢？可以使用@PropertySource注解指定配置文件的位置，这个配置文件可以是`.properties`，也可以是`.xml`。这里重点掌握`.properties`即可。

在`resources`目录下新建`a`目录，在`a`目录下新建`b`目录，`b`目录中新建`group-info.properties`文件，进行如下的配置：

```properties

group.name=IT
group.leader=LaoDu
group.count=20

```

定义Java类`Group`，然后进行注解标注：

```java

package com.jkweilai.sb307externalconfig.bean;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration
@ConfigurationProperties(prefix = "group")
@PropertySource("classpath:a/b/group-info.properties")
public class Group {
    private String name;
    private String leader;
    private Integer count;

    @Override
    public String toString() {
        return "Group{" +
                "name='" + name + '\'' +
                ", leader='" + leader + '\'' +
                ", count=" + count +
                '}';
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getLeader() {
        return leader;
    }

    public void setLeader(String leader) {
        this.leader = leader;
    }

    public Integer getCount() {
        return count;
    }

    public void setCount(Integer count) {
        this.count = count;
    }
}

```

以下三个注解分别起到什么作用：

+ @Configuration：指定该类为配置类，纳入Spring容器的管理
+ @ConfigurationProperties(prefix = "group")：将配置文件中的值赋值给Bean对象的属性
+ @PropertySource("classpath:a/b/group-info.properties")：指定额外的配置文件

编写测试程序，测试结果如下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729681829431-7e25af75-4618-410a-a5c7-d377c53683d9.png" width="449" title="" crop="0,0,1,1" id="ub262939b" class="ne-image">

---

## @ImportResource注解

**知识点列表：**

1. **如果 Bean 的配置编写在 **`**XML**`**文件中，如果在SpringBoot框架中应该怎么实现呢？在入口类上使用@ImportResource注解实现**
2. **@ImportResource("classpath:applicationContext.xml")**

定义一个普通的Java类：Person

```java

package com.jkweilai.sb307externalconfig.bean;

public class Person {
    private String name;
    private String age;

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age='" + age + '\'' +
                '}';
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }
}

```

在`resources`目录下新建`applicationContext.xml`配置文件：

```xml

<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="person" class="com.jkweilai.sb307externalconfig.bean.Person">
        <property name="name" value="jackson"/>
        <property name="age" value="20"/>
    </bean>
</beans>

```

在SpringBoot主入口类上添加@ImportResource进行资源导入，这样`applicationContext.xml`文件中的Bean将会纳入IoC容器的管理：

```java

@ImportResource("classpath:applicationContext.xml")
public class Sb307ExternalConfigApplication {}

```

编写测试程序，看看是否可以获取到`person`这个bean对象：

```java

@SpringBootTest
class Sb307ExternalConfigApplicationTests {
    @Autowired
    private Person person;
    @Test
    void test09(){
        System.out.println(person);
    }
}

```

执行结果如下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729683600179-80efe94a-9aca-4959-a6ee-af938bb4fc61.png" width="358" title="" crop="0,0,1,1" id="uf286517c" class="ne-image">

因此，项目中如果有类似于Spring的这种xml配置文件，要想纳入IoC容器管理，需要在入口类上使用`@ImportResource("classpath:applicationContext.xml")`注解即可。

---

## Environment

**知识点列表：**

1. `**Environment**`**是 SpringBoot 框架提供的环境对象。**
2. `**Environment**`**封装了什么信息？**
3. **在程序可以直接注入**`**Environment**`**对象，然后调用相关方法来获取各种配置信息。SpringBoot框架在启动的时候会将系统配置，环境信息全部封装到**`**Environment**`**对象中，如果要获取这些环境信息，可以调用**`**Environment**`**接口的方法。**

在Spring Boot中，`Environment`接口提供了访问应用程序环境信息的方法，比如活动配置文件、系统环境变量、命令行参数等。`Environment`接口由Spring框架提供，Spring Boot应用程序通常会使用Spring提供的实现类`AbstractEnvironment`及其子类来实现具体的环境功能。

`Environment`对象封装的主要数据包括：

1. **Active Profiles**: 当前激活的配置文件列表。Spring Boot允许应用程序定义不同的环境配置文件（如开发环境、测试环境和生产环境），通过激活不同的配置文件来改变应用程序的行为。
2. **System Properties**: 系统属性，通常是操作系统级别的属性，比如操作系统名称、Java版本等。
3. **System Environment Variables**: 系统环境变量，这些变量通常是由操作系统提供的，可以在启动应用程序时设置特定的值。
4. **Command Line Arguments**: 应用程序启动时传递给主方法的命令行参数。
5. **Property Sources**: `Environment`还包含了一个`PropertySource`列表，这个列表包含了从不同来源加载的所有属性。

在Spring Boot中，可以通过注入`Environment`来获取上述信息。例如：

```java

package com.jkweilai.springboot.bean;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.stereotype.Component;

@Component
public class SomeBean {

    @Autowired
    private Environment environment;

    public void doSome(){
        // 直接使用这个环境对象，来获取环境信息，配置信息等。
        String[] activeProfiles = environment.getActiveProfiles();
        for (String activeProfile : activeProfiles) {
            System.out.println(activeProfile);
        }

        // 获取配置信息
        String street = environment.getProperty("app.xyz.addr.street");
        System.out.println(street);
    }
}

```

通过这种方式，你可以根据环境的不同灵活地配置你的应用程序。`Environment`是一个非常有用的工具，它可以帮助你管理各种类型的配置信息，并根据不同的运行时条件做出相应的调整。

