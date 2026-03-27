# 外部化配置

---

## 什么是外部化配置

外部化配置是指：将`配置信息`存储在`应用程序代码`之外的地方。这样`配置信息`可以独立于代码进行管理。这样方便了配置的修改，并且修改后不需要重新编译代码，也不需要重新部署项目。

### 外部化配置的方式

SpringBoot支持多种外部化配置方式，包括但不限于：

+ properties文件
+ YAML文件
+ 系统环境变量
+ 命令行参数
+ ......

### 外部化配置的优势

1. **灵活性**：配置文件可以独立于应用程序部署，这使得可以根据运行环境的不同来调整配置，而无需修改代码。
2. **易于维护**：配置变更不需要重新构建和部署应用程序，降低了维护成本。
3. **安全性**：敏感信息如数据库密码、API密钥等可以存储在外部，并且可以限制谁有权限访问这些配置信息。
4. **共享性**：多实例或多服务可以共享相同的配置信息，减少重复配置的工作量。
5. **版本控制**：配置文件可以存放在版本控制系统中，便于跟踪历史版本和回滚配置。

总之，外部化配置使得配置更加灵活、安全、易于管理和共享，是现代云原生应用中非常推荐的做法

### 外部化配置对比传统配置

在传统的SSM三大框架中，如果修改XML的配置后，需要对应用重新打包，重新部署。

使用SpringBoot框架的`外部化配置`后，修改配置后，不需要对应用重新打包，也不需要重新部署，**最多重启一下服务即可**。

---

## application.properties

`application.properties`配置文件是SpringBoot框架默认的配置文件。

`application.properties`不是必须的，SpringBoot对于应用程序来说，都提供了一套默认配置（就是我们所说的自动配置）。

如果你要改变这些默认的行为，可以在`application.properties`文件中进行配置。

`application.properties`可以放在类路径当中，也可以放在项目之外。因此称为外部化配置。

Spring Boot 框架在启动时会尝试从以下位置加载 `application.properties` 配置文件：

1. `**file:./config/**`：首先在Spring Boot 当前工作目录下的 `config` 文件夹中查找。
    1. **注意：如果没有找到**`**application.properties**`**会继续找**`**application.yml**`**，如果这两个都没有找到，才会进入以下位置查找，以此类推。**
2. `**file:./**`：如果在当前工作目录下`config`目录中找不到时，再从当前工作目录中查找。
3. `**classpath:/config/**`： 如果从工作目录中找不到，会从类路径中找，先从类路径的 `/config/` 目录下寻找配置文件。
4. `**classpath:/**`：如果在 `/config/` 下没有找到，它会在类路径的根目录下查找。

**覆盖规则**：**

+ **优先级从高到低**（1 最高，4 最低）。**
+ **高优先级配置文件中的属性会覆盖低优先级中的同名属性**。**
+ **所有配置会合并**，不冲突的属性会同时生效。**

如果你想要指定其他的配置文件位置或者改变默认的行为，可以通过 `--spring.config.location=` 后跟路径的方式来指定配置文件的具体位置。例如 ：

```plain
java -jar sb3-01-first-web-1.0-SNAPSHOT.jar --spring.config.location=file:///E:\a\b\application.properties
```

这样，Spring Boot 将会首先从 `E:\a\b\` 这个路径加载配置文件。注意，这种方式可以用来覆盖默认的配置文件位置，**它的优先级是最高的**。

注意：以上的`--spring.config.location=file:///E:\a\b\application.properties`就属于命令行参数，它将来会被传递到**main方法的(String[] args)**参数上。

---

## 使用@Value注解

**知识点列表：**

1. `**@Value("${key}")**`**可以取配置文件中的配置信息。**
2. `**@Value("${key}")**`**如果指定的 key 不存在，会报错。**
3. `**@Value("${key: defalut}")**`**语法可以指定默认值。**
4. `**@Value("${APP_KEY}")**`**语法也可以取操作系统的环境变量值。这是一个比较重要的注解，在 Spring 中我们已经用过了，在这里再回顾一下。然后再补充一点内容。**

@Value注解可以将`application.properties`/`application.yml`文件中的配置信息注入/绑定到java对象的属性上。

**语法格式：@Value("${key}")**

使用脚手架创建SpringBoot项目，不添加任何启动器：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729589121331-13dc38dc-a34f-413f-963d-d1833df9686d.png" width="243" title="" crop="0,0,1,1" id="u042ae6c1" class="ne-image">

在`resources/application.properties`文件中进行如下配置：

```properties
myapp.username=jack
myapp.email=jack@123.com
myapp.age=30
```

编写service类：

```java
@Service("userService")
public class UserService {
    
    @Value("${myapp.username}")
    private String username;
    
    @Value("${myapp.email}")
    private String email;
    
    @Value("${myapp.age}")
    private Integer age;
    
    public void printInfo(){
        String str = String.join(",", username, email, String.valueOf(age));
        System.out.println(str);
    }
}
```

编写单元测试：

```java
@SpringBootTest
class Sb307ExternalConfigApplicationTests {
    @Autowired
    private UserService userService;
    @Test
    void test01() {
        userService.printInfo();
    }
}
```

运行结果：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729648496732-56988017-05c1-4d2c-9d72-6b88bca91656.png" width="257" title="" crop="0,0,1,1" id="u25a180e1" class="ne-image">

使用@Value注解时也可以指定默认值，当指定默认值时，如果配置文件中没有指定配置值，则采用默认值。

**语法格式：@Value("${key:defalut}")**

```java
@Service("userService")
public class UserService {

    @Value("${myapp.username}")
    private String username;

    @Value("${myapp.email}")
    private String email;

    @Value("${myapp.age}")
    private Integer age;
    
    @Value("${myapp.password:123456}")
    private String password;

    public void printInfo(){
        String str = String.join(",", username, email, String.valueOf(age), password);
        System.out.println(str);
    }
}
```

执行结果：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729648777588-90155042-3924-4126-b610-3e201ced970a.png" width="288" title="" crop="0,0,1,1" id="u352c8f1b" class="ne-image">

当然，如果配置文件进行了相关的配置，则不会采用默认值，修改配置文件`application.properties`：

```properties
myapp.username=jack
myapp.email=jack@123.com
myapp.age=30
myapp.password=888888
```

执行结果：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729648891492-48293951-3910-4180-8ace-c2741dc0b378.png" width="289" title="" crop="0,0,1,1" id="ue78d94f6" class="ne-image">

**另外，使用**`**@Value**`**注解也可以读取系统的环境变量，例如 windows 系统有一个环境变量**`**APP_KEY**`**，那么使用**`**@Value("${APP_KEY}")**`**是可以读取到的。但配置文件**`**APP_KEY**`**之后，一定要重启 windows 系统才行。**

---

## YAML

### YAML概述

SpringBoot采用集中式配置管理，所有的配置都编写到一个配置文件中：`application.properties`

如果配置非常多，层级不够分明，因此SpringBoot为了提高配置文件可读性，也支持YAML格式的配置文件：`application.yml`

YAML（YAML Ain't Markup Language）是一种人类可读的数据序列化格式，它通常用于配置文件，在各种编程语言中作为一种存储或传输数据的方式。YAML的设计目标是易于阅读和编写，同时保持足够的表达能力来表示复杂的数据结构。

**YAML文件的扩展名可以是**`**.yaml**`**或**`**.yml**`**。**

### 常见的数据存储和交换格式

`properties`、`XML`、`JSON`、`YAML`这几种格式确实是用来存储和交换数据的常见方式，但它们各有特点和适用场景：

**Properties**

+ 这种格式主要用于Java应用程序中的配置文件。它是键值对的形式，每一行是一个键值对，使用等号或冒号分隔键和值。
+ 特点是简单易懂，但在处理复杂结构的数据时显得力不从心。

**XML (eXtensible Markup Language)**

+ XML是一种标记语言，用来描述数据的格式。它支持复杂的数据结构，包括嵌套和属性。
+ XML文档具有良好的结构化特性，适合传输和存储结构化的数据。但是，XML文档通常体积较大，解析起来也比较耗资源。

**JSON (JavaScript Object Notation)**

+ JSON是一种轻量级的数据交换格式，易于人阅读和编写，同时也易于机器解析和生成。它基于JavaScript的一个子集，支持多种数据类型，如数字、字符串、布尔值、数组和对象。
+ JSON因为简洁和高效而广泛应用于Web应用程序之间进行数据交换。

**YAML (YAML Ain't Markup Language)**

+ YAML设计的目标之一就是让人类更容易阅读。它支持类似JSON的数据序列化，但提供了更多的灵活性，例如缩进来表示数据结构。
+ YAML非常适合用来编写配置文件，因为它允许以一种自然的方式组织数据，并且可以包含注释和其他人类可读的元素。

总结来说，这四种格式都可以用来存储和交换数据，但它们的设计初衷和最佳使用场景有所不同。选择哪种格式取决于具体的应用需求、数据复杂度、性能要求等因素。

### YAML的语法规则

YAML的语法规则如下：

1. 数据结构：YAML支持多种数据类型，包括：
    1. 字符串、数字、布尔值
    2. 数组、list集合
    3. map键值对   等。
2. YAML使用`一个冒号和一个空格`来分隔`属性名`和`属性值`，例如：
    1. `properties`文件中这样的配置：`name=jack`
    2. `yaml`文件中需要这样配置：`name: jack`
3. YAML用`换行+空格`来表示层级关系。注意不能使用tab，必须是空格，空格数量无要求，大部分建议2个或4个空格。例如：
    1. `properties`文件中这样的配置：`myapp.name=mall`
    2. `yaml`文件中就需要这样配置：

```yaml
myapp:
  name: mall
```

4. 同级元素左对齐。例如：
    1. `properties`文件中有这样的配置：

```properties
myapp.name=mall
myapp.count=10
```

    2. `yaml`文件中就应该这样配置：

```yaml
myapp:
  name: mall
  count: 10
```

5. 键必须是唯一的：在一个映射中，键必须是唯一的。
6. 注释：使用`#`进行注释。
7. 区分大小写。

### YAML的使用小细节

**第一：**普通文本也可以使用单引号或双引号括起来：（当然普通文本也可以不使用单引号和双引号括起来。）

+ 单引号括起来：单引号内所有的内容都被当做普通文本，不转义（例如字符串中有\n，则\n被当做普通的字符串）
+ 双引号括起来：双引号中有 \n 则会被转义为换行符
+ 单引号和双引号都不加，和添加单引号的效果一样。

**第二：**保留文本格式

+ `|`      将文本写到这个符号的下层，会自动保留格式。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764911738962-23784ede-1206-4272-aa19-93950ba84bdb.png" width="315.2" title="" crop="0,0,1,1" id="uf250886d" class="ne-image">

**第三：**换行变空格

+ `>`     将文本写到这个符号的下层，内容中换行会自动变成空格。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764911715905-473c2f95-77ee-4c93-8871-d7a951af446f.png" width="134.4" title="" crop="0,0,1,1" id="iQrra" class="ne-image">

**第四：**文档切割

+ --- 这个符号下面的配置可以认为是一个独立的yaml文件。便于庞大文件的阅读。

**### application.yml
Spring Boot框架同时支持`properties`和`yaml`。**强调：在同一个目录下同时存在**`**application.properties**`**和**`**application.yml**`**时，SpringBoot优先解析**`**application.properties**`**文件。**在`resources/config`目录下新建`application.yml`文件，进行如下配置：

```yaml
myapp:
  username: jim
  email: jim@123.com
  age: 40
  password: jim123
```

一定要把`resources/config`目录下`application.properties`名字修改为`application2.properties`，这样Spring Boot才会解析`resources/config/application.yml`。

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729654743068-a014695d-b7ea-42fe-91f8-0ea230bcb7d3.png" width="286" title="" crop="0,0,1,1" id="ud9c6ceee" class="ne-image">

运行测试程序：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729654822036-0c4b5c28-1c39-41c7-9321-03225aa3ec7a.png" width="295" title="" crop="0,0,1,1" id="uacb464b5" class="ne-image">

---

## 配置文件合并

一个项目中所有的配置全部编写到`application.properties`文件中，会导致配置臃肿，不易维护，有时我们会将配置编写到不同的文件中，例如：`application-mysql.properties`专门配置mysql的信息，`application-redis.properties`专门配置redis的信息，最终将两个配置文件合并到一个配置文件中。

### properties文件

`application-mysql.properties`

```properties
spring.datasource.username=root
spring.datasource.password=123456
```

`application-redis.properties`

```properties
spring.data.redis.host=localhost
spring.data.redis.port=6379
```

`application.properties`

```properties
spring.config.import=classpath:application-mysql.properties,classpath:application-redis.properties
```

编写service测试，看看能否拿到配置信息：

```java
package com.jkweilai.sb307externalconfig.service;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service("userServiceMulti")
public class UserServiceMulti {
    @Value("${spring.datasource.username}")
    private String username;
    @Value("${spring.datasource.password}")
    private String password;
    @Value("${spring.data.redis.host}")
    private String host;
    @Value("${spring.data.redis.port}")
    private String port;
    
    public void printInfo(){
        String str = String.join(",", username, password, host, port);
        System.out.println(str);
    }
}
```

运行测试：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729662602259-3ebb69e9-600a-4b5e-9536-30814ce5d19d.png" width="297" title="" crop="0,0,1,1" id="u2aafb6be" class="ne-image">

### yaml文件

`application-mysql.yml`

```yaml
spring:
  datasource:
    username: root
    password: 789789
```

`application-redis.yml`

```yaml
spring:
  data:
    redis:
      host: localhost
      port: 6379
```

`application.yml`

```yaml
spring:
  config:
    import:
      - classpath:application-mysql.yml
      - classpath:application-redis.yml
```

运行测试：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729663359961-e28ba636-6675-4e87-86a3-375859017754.png" width="279" title="" crop="0,0,1,1" id="uf3dbb91a" class="ne-image">

---

## 多环境切换**知识点列表：**1. **springboot 支持多配置文件切换**

2. **例如有 3 个配置文件：**`**application-x.properties**`**、**`**application-y.properties**`**、**`**application-z.properties**`
3. **在 **`**application.properties**`**中配置 **`**spring.profiles.active=x**`**则自动启用**`**application-x.properties**`**配置。**
4. **也可以通过命令行参数来指定启动哪个：--spring.profiles.active=x**

在Spring Boot中，多环境切换是指在一个应用程序中支持多种运行环境配置的能力。这通常用于区分开发（development）、测试（testing）、预生产（staging）和生产（production）等不同阶段的环境。

这种功能使得开发者能够在不同的环境中使用不同的配置，比如数据库连接信息、服务器端口、环境变量等，而不需要更改代码。这对于维护一个可移植且易于管理的应用程序非常重要。

1. 开发环境的配置文件名一般叫做：`application-dev.properties`

```properties
spring.datasource.username=dev
spring.datasource.password=dev123
spring.datasource.url=jdbc:mysql://localhost:3306/dev
```

2. 测试环境的配置文件名一般叫做：`application-test.properties`

```properties
spring.datasource.username=test
spring.datasource.password=test123
spring.datasource.url=jdbc:mysql://localhost:3306/test
```

3. 预生产环境的配置文件名一般叫做：`application-preprod.properties`

```properties
spring.datasource.username=preprod
spring.datasource.password=preprod123
spring.datasource.url=jdbc:mysql://localhost:3306/preprod
```

4. 生产环境的配置文件名一般叫做：`application-prod.properties`

```properties
spring.datasource.username=prod
spring.datasource.password=prod123
spring.datasource.url=jdbc:mysql://localhost:3306/prod
```

如果你希望该项目使用生产环境的配置，你可以这样做：

+ 第一种方式：在`application.properties`文件中添加这个配置：**spring.profiles.active=prod**
+ 第二种方式：在命令行参数上添加：**--spring.profiles.active=prod

---

## 将配置绑定到bean

### 绑定简单bean

**知识点列表：**

1. **使用 **`**@Component**`**+**`**@ConfigurationProperties(prefix = "app")**`**可以将配置文件中的配置一次性绑定到 Bean 上。**
2. **如果没有前缀，**`**prefix**`**可以省略。**
3. **绑定时，配置文件中的 key 需要和 Bean 的属性名对应上，并且给属性提供 setter 方法。**
4. **bean 的属性需要是非静态的。**

SpringBoot配置文件中的信息除了可以使用`@Value注解`读取之外，也可以将配置信息一次性赋值给Bean对象的属性。

例如有这样的配置：

`application.yml`

```yaml
app:
  name: jack
  age: 30
  email: jack@123.com
```

Bean需要这样定义：

```java
package com.jkweilai.sb307externalconfig.bean;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

@Component
@ConfigurationProperties(prefix = "app")
public class AppBean {
    private String name;
    private Integer age;
    private String email;

    @Override
    public String toString() {
        return "AppBean{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", email='" + email + '\'' +
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

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}
```

说明：

1. 被绑定的bean，需要使用`@ConfigurationProperties(prefix = "app")`注解进行标注，prefix用来指定前缀，哪个是前缀，如下图所示：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729667789270-8c85788b-8b00-4d17-bbab-5f87b9a68103.png" width="302" title="" crop="0,0,1,1" id="u391dc507" class="ne-image">

配置文件中的`name`、`age`、`email`要和bean对象的属性名`name`、`age`、`email`对应上。（属性名相同）

并且bean中的所有属性都提供了`setter`方法。因为底层是通过`setter`方法给bean属性赋值的。

2. 注意：前缀 prefix 不是必须的，如果没有添加前缀，则从开始查找。
3. 这样的bean需要使用`@Component`注解进行标注，纳入IoC容器的管理。`@Component`注解负责创建Bean对象，`@ConfigurationProperties(prefix = "app")`注解负责给bean对象的属性赋值。
4. bean的属性需要是`非static`的属性。

编写测试程序，将bean对象输出，结果如下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729668174305-f203b7f0-9ed2-435a-8c89-0f385cc6f50b.png" width="551" title="" crop="0,0,1,1" id="u7d23a56d" class="ne-image">

### @Configuration注解

**知识点列表：**

1. **如果是一个配置类的话，建议使用 **`**@Configuration**`**注解代替 **`**@Component**`**，语义更加明确。**
2. **使用 **`**@Configuration**`**注解后，输出对象的地址是一个代理对象地址（使用@Component 不会生成代理对象），生成代理对象效率较低，可以添加 **`**proxyBeanMethods = false**`**属性不生成代理对象。**
3. `**proxyBeanMethods = false**`**和 **`**proxyBeanMethods = true**`**的区别：true：生成代理，虽然效率低，可以保证 bean 是单例。false：不生成代理，虽然效率高，不保证单例。**

```java
@Configuration(proxyBeanMethods = false)
public class MyConfig {
    @Bean
    A a() { return new A(); }

    @Bean
    B b() {
        A a1 = a();  // 第1次调用
        A a2 = a();  // 第2次调用
        System.out.println(a1 == a2);
        return new B();
    }
}
class A {}
class B {}
```

以上操作中使用了`@Component注解`进行了标注，来纳入IoC容器的管理。也可以使用另外一个注解`@Configuration`，用这个注解将Bean标注为配置类。多数情况下我们会选择使用这个注解，因为该Bean对象的属性对应的就是配置文件中的配置信息，因此这个Bean我们也可以将其看做是一个配置类。

```java
@Configuration
@ConfigurationProperties(prefix = "app")
public class AppBean {
    private String name;
    private Integer age;
    private String email;
    //setter and getter
}
```

运行测试程序：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729671038234-ecf76053-a6d2-4100-8942-cf246e71397c.png" width="539" title="" crop="0,0,1,1" id="ub90abe6a" class="ne-image">

我们把这个Bean对象的类名打印一下看看：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764859292118-89926acf-071e-4220-9193-463bf5c1567a.png" width="504.8" title="" crop="0,0,1,1" id="u82b66397" class="ne-image">

可以发现底层实际上创建了`AppBean`的代理对象`AppBean$$SpringCGLIB`。

生成代理对象会影响效率，这里我们不需要使用代理功能，可以通过以下配置来取消代理机制：

```java
@Configuration(proxyBeanMethods = false)
@ConfigurationProperties(prefix = "app")
public class AppBean {
    private String name;
    private Integer age;
    private String email;
    //setter and getter
}
```

执行结果如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764859318989-b191024f-a0ba-45ef-98bd-6456a84bf8a9.png" width="355.2" title="" crop="0,0,1,1" id="u93e8ac9c" class="ne-image">

### 绑定嵌套bean

**知识点列表：**

1. **Bean 中嵌套一个 Bean，也可以绑定配置信息。比如 User 对象中有 Address 属性。**

当一个Bean中嵌套了一个Bean，这种情况下可以将配置信息绑定到该Bean上吗？当然可以。

有这样的一个配置：

```yaml
app:
  name: jack
  age: 30
  email: jack@123.com
  address: 
    city: BJ
    street: ChaoYang
    zipcode: 123456
```

需要编写这样的两个Bean：

```java
package com.jkweilai.sb307externalconfig.bean;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;

@Configuration(proxyBeanMethods = false)
@ConfigurationProperties(prefix = "app")
public class AppBean {
    private String name;
    private Integer age;
    private String email;
    private Address address;

    @Override
    public String toString() {
        return "AppBean{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", email='" + email + '\'' +
                ", address=" + address +
                '}';
    }

    public Address getAddress() {
        return address;
    }

    public void setAddress(Address address) {
        this.address = address;
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

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}

```

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

执行测试程序，结果如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764859348029-b1a2b1e9-a275-45fa-bb84-9fe4b1684dc1.png" width="908" title="" crop="0,0,1,1" id="uc1372835" class="ne-image">

### **@EnableConfigurationProperties与@ConfigurationPropertiesScan知识点列表：**

1. **之前的代码是这样写的：`**@Component**`**+**`**@ConfigurationProperties(prefix = "app")**`
2. **或者是这样写的： **`**@Configuration**`**+**`**@ConfigurationProperties(prefix = "app")**`
3. **有了以下这两个注解（任意一个都行，要求写到主入口类上），**`**@Component**`**和 **`**@Configuration**`**可以省略了：**
    1. **@EnableConfigurationProperties(Bean.class)**
    2. **@**ConfigurationPropertiesScan(basePackages="")**将`AppBean`纳入IoC容器的管理，之前我们说了两种方式：第一种是使用`@Component`，第二种是使用`@Configuration`。SpringBoot其实还提供了另外两种方式：

+ 第一种：@EnableConfigurationProperties
+ 第二种：@**ConfigurationPropertiesScan这两个注解都是标注在SpringBoot主入口程序上的：**

```java
@EnableConfigurationProperties(AppBean.class)
@SpringBootApplication
public class Sb307ExternalConfigApplication {
    public static void main(String[] args) {
        SpringApplication.run(Sb307ExternalConfigApplication.class, args);
    }
}
```

或者

```java
@ConfigurationPropertiesScan(basePackages = "com.jkweilai.sb307externalconfig.bean")
@SpringBootApplication
public class Sb307ExternalConfigApplication {
    public static void main(String[] args) {
        SpringApplication.run(Sb307ExternalConfigApplication.class, args);
    }
}
```

运行测试程序，执行结果如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764859369700-e1ff53bb-cca8-4613-b8ac-50cf12bab692.png" width="892.8" title="" crop="0,0,1,1" id="ucf259988" class="ne-image">

### 将配置赋值到Bean的Map/List/Array属性上**知识点列表：

1. **关键在于 **`**application.yml**`**中如何配置 Map/List/Array**

```yaml
