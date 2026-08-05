
## Jackson 解析 JSON

Jackson 库解析 JSON 需要引入以下 jar 包：

```xml
<!-- Jackson 核心：必须的 -->
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-core</artifactId>
    <version>2.16.1</version>
</dependency>

<!-- Jackson 数据绑定：将 JSON 与对象互转 -->
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.16.1</version>
</dependency>

<!-- Jackson 注解支持 -->
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-annotations</artifactId>
    <version>2.16.1</version>
</dependency>
```

**简化写法**：`jackson-databind`会自动引入 `jackson-core`和 `jackson-annotations`，所以通常只需要：

```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.16.1</version>
</dependency>
```

### 实体类的定义

```java
package com.laodu.jackson;

import java.util.List;

public class Person {
    private String name;
    private int age;
    private String email;
    private Address address;
    private List<String> hobbies;

    // 必须有无参构造函数
    public Person() {}

    // setter and getter
}

```

```java
package com.laodu.jackson;

public class Address {
    private String street;
    private String city;

    public Address() {}

    // setter and getter
}
```

### Java 对象转换为 JSON

```java
package com.laodu.jackson;

import com.fasterxml.jackson.databind.ObjectMapper;

import java.util.List;

public class JavaToJsonExample {
    public static void main(String[] args) throws Exception {
        // 1. 创建 Person 对象
        Address address = new Address();
        address.setStreet("123 Main St");
        address.setCity("New York");

        Person person = new Person();
        person.setName("Alice");
        person.setAge(30);
        person.setEmail("alice@example.com");
        person.setAddress(address);
        person.setHobbies(List.of("Reading", "Hiking"));

        // 2. 使用 Jackson 转换为 JSON 字符串
        ObjectMapper mapper = new ObjectMapper();
        String jsonString = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(person);

        // 3. 打印结果
        System.out.println("JSON 字符串：\n" + jsonString);
    }
}

```

### JSON 转换为 Java 对象

```java
package com.laodu.jackson;

import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonToJavaExample {
    public static void main(String[] args) throws Exception {
        // 1. 模拟 JSON 字符串
        String jsonString = """
                {
                  "name" : "Bob",
                  "age" : 25,
                  "email" : "bob@example.com",
                  "address" : {
                    "street" : "456 Oak Ave",
                    "city" : "Los Angeles"
                  },
                  "hobbies" : [ "Gaming", "Swimming" ]
                }
                """;

        // 2. 使用 Jackson 解析为 Java 对象
        ObjectMapper mapper = new ObjectMapper();
        // 这里需要注意的是：Person 需要保证存在无参数构造方法。
        Person person = mapper.readValue(jsonString, Person.class);

        // 3. 验证结果
        System.out.println("Person 对象：");
        System.out.println("Name: " + person.getName());
        System.out.println("Age: " + person.getAge());
        System.out.println("Address: " + person.getAddress().getStreet() + ", " + person.getAddress().getCity());
        System.out.println("Hobbies: " + person.getHobbies());
    }
}
```
