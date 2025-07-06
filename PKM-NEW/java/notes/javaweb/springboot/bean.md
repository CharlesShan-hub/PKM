# Springboot —— bean 扫描

---
## 基本介绍

默认的 bean 扫描已经包含在注解`@SpringBootApplication`中，如果要增加其他的包需要手动增加`@ComponentScan`

```Java
package com.charlesshan.helloworld;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class HelloWorldApplication {
    public static void main(String[] args) {
        SpringApplication.run(HelloWorldApplication.class, args);
    }
}
```

相当于

```java
package com.charlesshan.helloworld;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
@SpringBootConfigration
@EnableAutoConfigration
@ComponentScan
public class HelloWorldApplication {
    public static void main(String[] args) {
        SpringApplication.run(HelloWorldApplication.class, args);
    }
}
```

相当于

```java
package com.charlesshan.helloworld;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
@SpringBootConfigration
@EnableAutoConfigration
@ComponentScan(basePackages = "com.charlesshan")
public class HelloWorldApplication {
    public static void main(String[] args) {
        SpringApplication.run(HelloWorldApplication.class, args);
    }
}
```

---
## 主要参数

`@ComponentScan` 有几个重要的参数可以配置：

1. ​**​basePackages / value​**​: 指定要扫描的基础包
    
    ```
    @ComponentScan(basePackages = "com.example")
    @ComponentScan({"com.example", "com.other"}) // value 的简写
    ```
    
2. ​**​basePackageClasses​**​: 通过类来指定扫描的基础包
    
    ```
    @ComponentScan(basePackageClasses = {SomeClass.class, AnotherClass.class})
    ```
    
3. ​**​includeFilters​**​: 包含特定的组件类型
    
    ```
    @ComponentScan(includeFilters = @Filter(type = FilterType.ANNOTATION, classes = CustomAnnotation.class))
    ```
    
4. ​**​excludeFilters​**​: 排除特定的组件类型
    
    ```
    @ComponentScan(excludeFilters = @Filter(type = FilterType.ANNOTATION, classes = Controller.class))
    ```
    
5. ​**​useDefaultFilters​**​: 是否使用默认过滤器（默认为 true）
    
    ```
    @ComponentScan(useDefaultFilters = false)
    ```
    
---
## 使用场景示例

### 1. 扫描多个包

```
@SpringBootApplication
@ComponentScan(basePackages = {"com.example.main", "com.example.utils"})
public class MyApplication {
    // ...
}
```

### 2. 排除特定组件

```
@SpringBootApplication
@ComponentScan(excludeFilters = @Filter(type = FilterType.ANNOTATION, classes = {Service.class}))
public class MyApplication {
    // ...
}
```

### 3. 自定义过滤器

```
@SpringBootApplication
@ComponentScan(
    includeFilters = @Filter(type = FilterType.CUSTOM, classes = MyTypeFilter.class),
    useDefaultFilters = false
)
public class MyApplication {
    // ...
}
```

