
# Java 对象和 XML 互转

JAXB(Java Architecture for XML Binding)是最常用的XML绑定技术。使用 JAXB 需要引入以下 jar 包：

1. Java 8：**Java 8 内置了 JAXB**，无需额外引入依赖。直接在代码中导入 `javax.xml.bind.*`包即可。

    ```java
    import javax.xml.bind.*;
    // Java 8 可以直接使用
    ```

2. Java 9 - Java 11：**JAXB 从 Java 标准库中移除**，需要**手动引入依赖**。在 `pom.xml`中添加：

    ```xml
    <dependency>
        <groupId>javax.xml.bind</groupId>
        <artifactId>jaxb-api</artifactId>
        <version>2.3.1</version>
    </dependency>
    
    <dependency>
        <groupId>com.sun.xml.bind</groupId>
        <artifactId>jaxb-core</artifactId>
        <version>2.3.0.1</version>
    </dependency>
    
    <dependency>
        <groupId>com.sun.xml.bind</groupId>
        <artifactId>jaxb-impl</artifactId>
        <version>2.3.3</version>
    </dependency>
    ```

    **或者使用更简洁的 Jakarta EE 9+ 版本**（推荐，面向未来）

    ```xml
    <dependency>
        <groupId>jakarta.xml.bind</groupId>
        <artifactId>jakarta.xml.bind-api</artifactId>
        <version>4.0.0</version>
    </dependency>
    
    <dependency>
        <groupId>com.sun.xml.bind</groupId>
        <artifactId>jaxb-impl</artifactId>
        <version>4.0.0</version>
        <scope>runtime</scope>
    </dependency>
    ```

3. Java 11+（现代项目推荐）：**强烈推荐使用 Jakarta EE 命名空间**，这是 JAXB 的新标准。在 `pom.xml`中添加：

    ```xml
    <!-- Jakarta XML Binding API (JAXB) -->
    <dependency>
        <groupId>jakarta.xml.bind</groupId>
        <artifactId>jakarta.xml.bind-api</artifactId>
        <version>4.0.0</version>
    </dependency>
    
    <!-- 实现（选择其中一个即可） -->
    
    <!-- 方案1：GlassFish 参考实现 -->
    <dependency>
        <groupId>org.glassfish.jaxb</groupId>
        <artifactId>jaxb-runtime</artifactId>
        <version>4.0.0</version>
        <scope>runtime</scope>
    </dependency>
    
    <!-- 方案2：Eclipse Implementation（推荐） -->
    <dependency>
        <groupId>org.eclipse.persistence</groupId>
        <artifactId>org.eclipse.persistence.moxy</artifactId>
        <version>4.0.0</version>
        <scope>runtime</scope>
    </dependency>
    ```

    **注意**：代码中的导入包名也要相应改变：

    ```java
    // Java 8
    import javax.xml.bind.*;
    
    // Jakarta EE 9+
    import jakarta.xml.bind.*;
    ```

4. Spring Boot 项目：在 Spring Boot 项目中，可以简化配置：

    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
        <!-- 如果使用 Jakarta EE -->
        <exclusions>
            <exclusion>
                <groupId>javax.xml.bind</groupId>
                <artifactId>jaxb-api</artifactId>
            </exclusion>
        </exclusions>
    </dependency>
    
    <!-- 添加 Jakarta JAXB -->
    <dependency>
        <groupId>jakarta.xml.bind</groupId>
        <artifactId>jakarta.xml.bind-api</artifactId>
    </dependency>
    
    <dependency>
        <groupId>org.glassfish.jaxb</groupId>
        <artifactId>jaxb-runtime</artifactId>
    </dependency>
    ```

---

## 快速选择建议

|你的项目|推荐方案|示例坐标|
|---|---|---|
|**Java 8 老项目**​|无需添加依赖，使用内置|（无需添加）|
|**Java 9-11 升级项目**​|Jakarta EE 版本|上述方案3|
|**Java 11+ 新项目**​|Jakarta EE 版本|上述方案3|
|**Spring Boot 2.7+/3.0+**​|Jakarta EE 版本|上述方案4|
|**需要向前兼容**​|旧版 javax|上述方案2|

**最通用方案**（2026年推荐）：

```xml
<dependency>
    <groupId>jakarta.xml.bind</groupId>
    <artifactId>jakarta.xml.bind-api</artifactId>
    <version>4.0.0</version>
</dependency>
<dependency>
    <groupId>org.glassfish.jaxb</groupId>
    <artifactId>jaxb-runtime</artifactId>
    <version>4.0.0</version>
    <scope>runtime</scope>
</dependency>
```

导入包时使用：`import jakarta.xml.bind.*;`

---

## Java 对象转换为 XML

```java
import jakarta.xml.bind.JAXBContext;
import jakarta.xml.bind.Marshaller;
import jakarta.xml.bind.annotation.XmlRootElement;

import java.io.StringWriter;

public class JavaObjectToXML {
    public static void main(String[] args) throws Exception {
        User user = new User("admin", 30);
        
        // 创建JAXBContext上下文环境，指定要序列化的类
        // JAXBContext是JAXB API的入口点，负责管理XML绑定的元数据
        JAXBContext context = JAXBContext.newInstance(User.class);

        // 通过JAXBContext创建Marshaller对象
        // Marshaller负责将Java对象转换为XML数据(序列化器)
        Marshaller marshaller = context.createMarshaller();
        
        // 设置Marshaller的属性，使输出的XML格式美观（有缩进和换行）
        // 如果不设置此属性，XML将会是单行显示，没有格式
        marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);
        
        StringWriter writer = new StringWriter();
        
        // 执行对象到XML的转换（序列化）
        // 将user对象转换为XML并写入到writer中
        marshaller.marshal(user, writer);
        
        String xmlString = writer.toString();
        System.out.println(xmlString);
    }
}

@XmlRootElement
class User{
    private String name;
    private int age;

    public User() {
    }

    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
```

---

## XML 转换为 Java 对象

```java
import jakarta.xml.bind.JAXBContext;
import jakarta.xml.bind.Unmarshaller;

import java.io.StringReader;

public class XMLToJavaObject {
    public static void main(String[] args) throws Exception {
        String xmlString = """
                <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
                <user>
                    <age>30</age>
                    <name>admin</name>
                </user>
                """;
        
        // 创建JAXBContext上下文环境，指定要处理的类(User.class)
        // JAXBContext是JAXB操作的入口点，它包含了对象与XML映射的元数据信息
        JAXBContext context = JAXBContext.newInstance(User.class);

        // 通过JAXBContext创建Unmarshaller对象
        // Unmarshaller负责将XML数据转换回Java对象（反序列化）
        Unmarshaller unmarshaller = context.createUnmarshaller();

        // 执行XML到对象的转换（反序列化）
        // 将XML字符串通过StringReader读取，然后转换为User对象
        // unmarshal()方法返回的是Object类型，需要强制转换为User类型
        User user = (User) unmarshaller.unmarshal(new StringReader(xmlString));
        System.out.println(user);
    }
}
```

当然，Java 对象和 XML 互转，不仅仅有 JAXB 技术，还有其它的，例如：XStream、Jackson XML 等，感兴趣的可以自行研究。
