# Lombok库

---

## 了解 Lombok

**知识点列表：**

1. **Lombok 是一个 Java 库。自动帮我们生成构造方法，setter 和 getter，equals 和 hashCode，toString 等。**
2. **Lombok 只在编译阶段起作用，因此不影响程序的执行效率。**
3. **可以通过查看字节码，看看 Lombok 都帮我们生成了什么。**

Lombok 是一个 Java 库，它可以通过注解的方式减少 Java 代码中的样板代码。Lombok 自动为你生成构造函数、getter、setter、equals、hashCode、toString 方法等，从而避免了手动编写这些重复性的代码。这不仅减少了出错的机会，还让代码看起来更加简洁。

**Lombok只是一个编译阶段的库，能够帮我们自动补充代码，在Java程序运行阶段并不起作用。（因此Lombok库并不会影响Java程序的执行效率）**

例如我们有这样一个java源文件`User.java`，代码如下：

```java
@Data
public class User{
    private String name;
}
```

以上代码在程序的编译阶段，Lombok库会将`User.java`文件编译生成这样的`User.class`字节码文件：

```java
public class com.jkweilai.lomboktest.entity.User {
  public com.jkweilai.lomboktest.entity.User();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: return

  public java.lang.String getName();
    Code:
       0: aload_0
       1: getfield      #7                  // Field name:Ljava/lang/String;
       4: areturn

  public void setName(java.lang.String);
    Code:
       0: aload_0
       1: aload_1
       2: putfield      #7                  // Field name:Ljava/lang/String;
       5: return

  public boolean equals(java.lang.Object);
    Code:
       0: aload_1
       1: aload_0
       2: if_acmpne     7
       5: iconst_1
       6: ireturn
       7: aload_1
       8: instanceof    #8                  // class com/jkweilai/lomboktest/entity/User
      11: ifne          16
      14: iconst_0
      15: ireturn
      16: aload_1
      17: checkcast     #8                  // class com/jkweilai/lomboktest/entity/User
      20: astore_2
      21: aload_2
      22: aload_0
      23: invokevirtual #13                 // Method canEqual:(Ljava/lang/Object;)Z
      26: ifne          31
      29: iconst_0
      30: ireturn
      31: aload_0
      32: invokevirtual #17                 // Method getName:()Ljava/lang/String;
      35: astore_3
      36: aload_2
      37: invokevirtual #17                 // Method getName:()Ljava/lang/String;
      40: astore        4
      42: aload_3
      43: ifnonnull     54
      46: aload         4
      48: ifnull        65
      51: goto          63
      54: aload_3
      55: aload         4
      57: invokevirtual #21                 // Method java/lang/Object.equals:(Ljava/lang/Object;)Z
      60: ifne          65
      63: iconst_0
      64: ireturn
      65: iconst_1
      66: ireturn

  protected boolean canEqual(java.lang.Object);
    Code:
       0: aload_1
       1: instanceof    #8                  // class com/jkweilai/lomboktest/entity/User
       4: ireturn

  public int hashCode();
    Code:
       0: bipush        59
       2: istore_1
       3: iconst_1
       4: istore_2
       5: aload_0
       6: invokevirtual #17                 // Method getName:()Ljava/lang/String;
       9: astore_3
      10: iload_2
      11: bipush        59
      13: imul
      14: aload_3
      15: ifnonnull     23
      18: bipush        43
      20: goto          27
      23: aload_3
      24: invokevirtual #24                 // Method java/lang/Object.hashCode:()I
      27: iadd
      28: istore_2
      29: iload_2
      30: ireturn

  public java.lang.String toString();
    Code:
       0: aload_0
       1: invokevirtual #17                 // Method getName:()Ljava/lang/String;
       4: invokedynamic #28,  0             // InvokeDynamic #0:makeConcatWithConstants:(Ljava/lang/String;)Ljava/lang/String;
       9: areturn
}
```

通过字节码可以看到Lombok库的`@Data`注解可以帮助我们生成`无参构造器`、`setter`、`getter`、`toString`、`hashCode`、`equals`。

---

## Lombok 的主要注解

**@Data**：

+ 等价于 `@ToString`, `@EqualsAndHashCode`, `@Getter`，`@Setter`, `@RequiredArgsConstructor`.
+ 用于生成：必要参数的构造方法、getter、setter、toString、equals 和 hashcode 方法。

**@Getter** / **@Setter**：

+ 分别用于生成所有的 getter 和 setter 方法。
+ 可以作用于整个类，也可以作用于特定的字段。

**@NoArgsConstructor**：

+ 生成一个无参构造方法。

**@AllArgsConstructor**：

+ 生成一个包含所有实例变量的构造器。

**@RequiredArgsConstructor**：

+ 生成包含所有被 `final` 修饰符修饰的实例变量的构造方法。
+ **如果没有**`**final**`**的实例变量，则自动生成无参数构造方法。@ToString** / **@EqualsAndHashCode**：

+ 用于生成 toString 和 equals/hashCode 方法。
+ **这两个注解都有**`**exclude**`**属性，通过这个属性可以定制toString、hashCode、equals方法。## 使用 Lombok

### 添加依赖

在 Maven 的 `pom.xml` 文件中添加 Lombok 依赖：

```xml
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
</dependency>
```

### 使用 Lombok 注解

在 Java 类中使用 Lombok 提供的注解。

```java
import lombok.Data;

@Data
public class User {
    private String name;
}
```

编写测试程序：

```java
package com.jkweilai.lomboktest;

import com.jkweilai.lomboktest.entity.User;

public class Test {
    public static void main(String[] args) {
        User user = new User();
        user.setName("jackson");
        System.out.println(user.getName());
        System.out.println(user.toString());
        System.out.println(user.hashCode());
        User user2 = new User();
        user2.setName("jackson");
        System.out.println(user.equals(user2));
    }
}

```

测试结果：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729148006400-a32df299-5efe-49b7-82e4-34a7a23b4b88.png" width="218" title="" crop="0,0,1,1" id="ufe74f98a" class="ne-image">

**以下的注解可以自行测试：**

+ **@Getter**
+ **@Setter**
+ **@ToString【exclude属性】**
+ **@EqualsAndHashCode【exclude属性】**
+ **@NoArgsConstructor**
+ **@AllArgsConstructor**
+ **@RequiredArgsConstructor注：Lombok只能帮助我们生成无参数构造方法和全参数构造方法，其他定制参数的构造方法无法生成。

---

## Lombok的其他常用注解

@Value

@Builder

@Singular

@Slf4j

### @Value

该注解会给所有属性添加`final`，给所有属性提供`getter`方法，自动生成`toString`、`hashCode`、`equals`

**通过这个注解可以创建不可变对象。**

```java
package com.jkweilai.lomboktest.entity;

import lombok.Value;

@Value
public class Customer {
    Long id;
    String name;
    String password;
}
```

测试程序：

```java
package com.jkweilai.lomboktest;

import com.jkweilai.lomboktest.entity.Customer;

public class CustomerTest {
    public static void main(String[] args) {
        Customer c1 = new Customer(1L, "jackson", "123");
        System.out.println(c1);
        System.out.println(c1.getId());
        System.out.println(c1.getName());
        System.out.println(c1.getPassword());
        System.out.println(c1.hashCode());
        Customer c2 = new Customer(1L, "jackson", "123");
        System.out.println(c1.equals(c2));
    }
}

```

运行结果：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1729219457643-9a89e6b4-bc3c-4a3a-b456-462574324d7d.png" width="465" title="" crop="0,0,1,1" id="u9cdaa773" class="ne-image">

可以查看一下字节码，你会发现，@Value注解的作用只会生成：全参数构造方法、getter方法、hashCode、equals、toString方法。（没有setter方法。）

### 建造者模式

建造模式（Builder Pattern）属于创建型设计模式。GoF23种设计模式之一。

**用于解决对象创建时参数过多的问题。它可以让对象的构造过程可以逐步完成，而不是一次性提供所有参数。建造模式的主要目的是让对象的创建过程更加清晰、灵活和可控。**

简而言之，建造模式用于：

1. **简化构造过程**：通过逐步构造对象，避免构造函数参数过多。
2. **提高可读性和可维护性**：让构造过程更加清晰和有序。
3. **增强灵活性**：允许按需配置对象的不同部分。

**建造模式的代码**

建造模式代码如下：

```java
package com.jkweilai.demo.entity;

// 建造者模式
public class Person {
    private String name;
    private Integer age;
    private String email;

    // 私有的全参数构造方法
    private Person(String name, Integer age, String email){
        this.name = name;
        this.age = age;
        this.email = email;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", email='" + email + '\'' +
                '}';
    }

    // 获取建造者对象
    public static PersonBuilder builder(){
        return new PersonBuilder();
    }

    // 一般会提供一个静态的内部类：建造者类
    public static class PersonBuilder {
        private String name;
        private Integer age;
        private String email;
        public PersonBuilder name(String name){
            this.name = name;
            return this;
        }
        public PersonBuilder age(Integer age){
            this.age = age;
            return this;
        }
        public PersonBuilder email(String email){
            this.email = email;
            return this;
        }
        // 核心代码：建造方法
        public Person build(){
            return new Person(name, age, email);
        }
    }

    public static void main(String[] args) {
        Person person = Person.builder()
                .name("zhangsan")
                .age(100)
                .email("zhangsan@123.com")
                .build();
        System.out.println(person);
    }
}

```

执行结果如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764939369776-ceb92250-25a2-4511-b955-7dc78218af2d.png" width="543.2" title="" crop="0,0,1,1" id="u9102e10b" class="ne-image">

### @Builder

`@Builder`注解可以帮我们生成建造者模式的代码。

```java
package com.jkweilai.demo.entity;

import lombok.Builder;

// 建造者模式
@Builder
public class Person {
    private String name;
    private Integer age;
    private String email;

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", email='" + email + '\'' +
                '}';
    }

    public static void main(String[] args) {
        Person person = Person.builder()
                .name("zhangsan")
                .age(100)
                .email("zhangsan@123.com")
                .build();
        System.out.println(person);
    }
}

```

执行结果：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764939437424-40cb14ff-af28-459d-8674-bef1b04ac985.png" width="484" title="" crop="0,0,1,1" id="uc4eacf67" class="ne-image">

### @Singular

@Singular注解是辅助@Builder注解的。

当被建造的对象的属性是一个集合，这个集合属性使用@Singular注解进行标注的话，可以连续调用集合属性对应的方法完成多个元素的添加。如果没有这个注解，则无法连续调用方法完成多个元素的添加。代码如下：

```java
package com.jkweilai.demo.entity;

import lombok.Builder;
import lombok.Singular;
import lombok.ToString;

import java.util.List;

// 建造者模式
@Builder
@ToString
public class Person {
    private String name;
    private Integer age;
    private String email;
    @Singular("addPhone")
    private List<String> phones;

    public static void main(String[] args) {
        Person person = Person.builder()
                .name("zhangsan")
                .age(100)
                .email("zhangsan@123.com")
                .addPhone("18799878786")
                .addPhone("18977667675")
                .build();
        System.out.println(person);
    }
}

```

执行结果如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764939641595-91256ba4-3e6c-44b2-bbfd-329c66c58785.png" width="722.4" title="" crop="0,0,1,1" id="u2f9023b0" class="ne-image">

### @Slf4j

`@Slf4j`注解可以帮助我们在类中生成一个专门记录日志的常量：`log`。我们直接用就行，很方便。

`@Slf4j`底层使用的是日志门面中的方法，具体底层使用的是哪个日志框架，取决于你引入的具体日志框架的依赖。

SpringBoot 默认采用 `logback-classic`，如果在 SpringBoot 项目中使用 `Lombok`，则底层使用的是 `logback`。

```java
package com.jkweilai.demo;

import lombok.extern.slf4j.Slf4j;

import java.math.BigDecimal;

@Slf4j
public class LombokLog {

    // 使用 @Slf4j 底层会自动生成这样一个常量。（常量在字节码中看不到）
    //private static final org.slf4j.Logger log = org.slf4j.LoggerFactory.getLogger(LombokLog.class);

    public static void transfer(String from, String to, BigDecimal amount) {
        log.info("from:{}, to:{}, amount:{}", from, to, amount);
    }

    public static void main(String[] args) {
        transfer("act-001", "act-002", new BigDecimal(100));
    }
}

```

