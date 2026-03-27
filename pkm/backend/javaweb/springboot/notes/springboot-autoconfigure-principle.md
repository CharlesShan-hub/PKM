# 自动配置实现原理

---

## 自动配置类的三个来源

1. 以前配置是写在 XML 文件中的，现在的配置都是配置类。一个配置类对应一套配置。springboot 通过加载配置类来加载该配置。
2. 一个 springboot 项目的配置类在哪？来源有三个
3. **SpringBoot 官方提供的自动配置类**
    1. 位置： spring-boot-autoconfigure.jar 的META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports 配置中。
    2. 内容： Spring Boot 团队维护的所有官方自动配置
    3. 数量：约 150-200 个（不同版本略有差异）
4. **第三方启动器提供的自动配置类**
    1. 位置：在各自的 jar 包中，路径也是：META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports
5. **自己项目中自己写的自动配置类**
    1. 位置：在自己的项目中，路径也是：META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports
6. **不管来源是哪个，位置都是一样的**，这是一种约定，都是从 jar 包的 `META-INF/spring`目录下的 `org.springframework.boot.autoconfigure.AutoConfiguration.imports`文件中加载自动配置类。

---

## 加载机制：合并所有来源

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764984821891-fe81ca97-fdc3-49e6-8478-20635b149524.png" width="804.4000244140625" title="" crop="0,0,1,1" id="ua9efc3e6" class="ne-image">

---

## SpringBoot 官方提供了 150 多个自动配置类

1. 当我们导入`spring-boot-starter-web`【web启动器】
2. 会关联导入了`spring-boot-starter`【任何一个 springboot 项目都需要这个启动器】
3. 核心启动器导入之后，关联导入了一个jar包：`spring-boot-autoconfigure`
    1. 注意：这个jar包中存放的是springboot框架**官方支持的自动配置类**。如下图：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1731120167649-5b43660e-d911-4af1-b609-7ba357483cbb.png" width="523" title="" crop="0,0,1,1" id="FY7Mq" class="ne-image">

    2. 官方支持的自动配置类有多少个呢，可以通过下图位置查看：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1731120316690-38e92299-860c-4f52-8e90-93773af32190.png" width="534" title="" crop="0,0,1,1" id="u73900a9f" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1731120338604-18c536ab-a98f-4ba7-adf3-10f47f02056d.png" width="675" title="" crop="0,0,1,1" id="u769be9ac" class="ne-image">

得知`springboot3.3.5`这个版本共`152`个自动配置类。自动配置类的命名规则是`XxxxAutoConfiguration`。

**提示：哪个自动配置类生效，就代表哪个配置文件生效，那么对应的技术就完成了整合，就可以进行对应技术的开发。**

---

## 自动配置实现原理

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1764985417738-3e5a53b6-eaec-4801-8fbc-37f2d95f40de.png" width="564.4000244140625" title="" crop="0,0,1,1" id="uce68e9b0" class="ne-image">

---

## 加载 150 多个自动配置类的源码分析

### 重要的注解

主入口类上的注解是：@SpringBootApplication

@SpringBootApplication 上面有一个@EnableAutoConfiguration，用来启用自动配置

@EnableAutoConfiguration 上面有一个@Import(AutoConfigurationImportSelector.class)，导入自动配置选择器

AutoConfigurationImportSelector.class 这个选择器负责导入符合条件的自动配置类

### 从哪个文件中导入 150 多个类名

`AutoConfigurationImportSelector`类中的核心方法 `getAutoConfigurationEntry`：该方法完成了自动配置类的筛选。

```java
protected AutoConfigurationEntry getAutoConfigurationEntry(AnnotationMetadata annotationMetadata) {
    if (!isEnabled(annotationMetadata)) {
        return EMPTY_ENTRY;
    }
    AnnotationAttributes attributes = getAttributes(annotationMetadata);
    // 这一行代码读取了150多个自动配置类的类名（从这一行代码进入，可以看到读取的是哪个配置文件）
    List<String> configurations = getCandidateConfigurations(annotationMetadata, attributes);
    configurations = removeDuplicates(configurations);
    Set<String> exclusions = getExclusions(annotationMetadata, attributes);
    checkExcludedClasses(configurations, exclusions);
    configurations.removeAll(exclusions);
    configurations = getConfigurationClassFilter().filter(configurations);
    fireAutoConfigurationImportEvents(configurations, exclusions);
    return new AutoConfigurationEntry(configurations, exclusions);
}
```

继续进入当前类的另一个方法：`getCandidateConfigurations`

```java
protected List<String> getCandidateConfigurations(AnnotationMetadata metadata, AnnotationAttributes attributes) {
    // 这个load方法就是用来加载配置文件中的150多个自动配置类的类名的。
    ImportCandidates importCandidates = ImportCandidates.load(this.autoConfigurationAnnotation,
            getBeanClassLoader());
    List<String> configurations = importCandidates.getCandidates();
    Assert.state(!CollectionUtils.isEmpty(configurations),
            "No auto configuration classes found in " + "META-INF/spring/"
                    + this.autoConfigurationAnnotation.getName() + ".imports. If you "
                    + "are using a custom packaging, make sure that file is correct.");
    return configurations;
}
```

继续进入 `ImportCandidates`类 `load`方法：

```java
public static ImportCandidates load(Class<?> annotation, ClassLoader classLoader) {
    Assert.notNull(annotation, "'annotation' must not be null");
    ClassLoader classLoaderToUse = decideClassloader(classLoader);
    // 从location变量可以捕捉到是从 META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports 文件中加载的。
    String location = String.format(LOCATION, annotation.getName());
    Enumeration<URL> urls = findUrlsInClasspath(classLoaderToUse, location);
    List<String> importCandidates = new ArrayList<>();
    while (urls.hasMoreElements()) {
        URL url = urls.nextElement();
        importCandidates.addAll(readCandidateConfigurations(url));
    }
    return new ImportCandidates(importCandidates);
}
```

通过上面源码的跟踪，可以得出，150 多个自动配置类是从 `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports`配置文件中加载的。

---

## 核心方法的主要流程分析

`AutoConfigurationImportSelector`类中的核心方法 `getAutoConfigurationEntry`：该方法完成了自动配置类的筛选。

```java
protected AutoConfigurationEntry getAutoConfigurationEntry(AnnotationMetadata annotationMetadata) {
    if (!isEnabled(annotationMetadata)) {
        return EMPTY_ENTRY;
    }
    AnnotationAttributes attributes = getAttributes(annotationMetadata);
    List<String> configurations = getCandidateConfigurations(annotationMetadata, attributes);
    configurations = removeDuplicates(configurations);
    Set<String> exclusions = getExclusions(annotationMetadata, attributes);
    checkExcludedClasses(configurations, exclusions);
    configurations.removeAll(exclusions);
    configurations = getConfigurationClassFilter().filter(configurations);
    fireAutoConfigurationImportEvents(configurations, exclusions);
    return new AutoConfigurationEntry(configurations, exclusions);
}
```

### 获取注解属性

```java
AnnotationAttributes attributes = getAttributes(annotationMetadata);
```

**作用**：解析**`**@EnableAutoConfiguration**`**注解的属性。**

```java
// 假设入口类上写了这样一个注解：通过这种方式用户可以显示的告诉springboot需要排除掉哪些自动配置类。
@EnableAutoConfiguration(
    exclude = DataSourceAutoConfiguration.class,
    excludeName = "org.springframework.boot.autoconfigure.security.SecurityAutoConfiguration"
)

// 上面代码执行后会解析得到：
attributes = {
    "exclude": [DataSourceAutoConfiguration.class],
    "excludeName": ["org.springframework.boot.autoconfigure.security.SecurityAutoConfiguration"]
}
```

### 获取候选配置

```java
List<String> configurations = getCandidateConfigurations(annotationMetadata, attributes);
```

**作用**：从**`**META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports**`**文件加载所有自动配置类。**

### **去重**

```java
configurations = removeDuplicates(configurations);
```

**作用**：确保配置类不重复。理论上不会重复，但多个 jar 包就不一定了。**

### **获取排除项**

```java
Set<String> exclusions = getExclusions(annotationMetadata, attributes);
```

**作用**：收集所有要排除的配置类。（这里的排除只是排除掉程序员在编码阶段指定的要排除的类，并不是通过条件注解进行过滤。）**

### **检查排除项**

```java
checkExcludedClasses(configurations, exclusions);
```

**作用**：验证用户排除的类确实是自动配置类（防止排除错误）。**

### **排除**

```java
configurations.removeAll(exclusions);
```

**作用**：从候选列表中移除被排除的配置类。（仍然是排除程序员指定要排除的配置类。并不是经过条件注解进行过滤。）**

### **条件过滤（最核心的一步）**

```java
configurations = getConfigurationClassFilter().filter(configurations);
```

**作用**：使用**`**@Conditional**`**系列注解进行智能过滤。**

### **触发事件（这个对于我们来说不重要）**

```java
fireAutoConfigurationImportEvents(configurations, exclusions);
```

**作用**：触发**自动配置导入**事件，让监听器可以处理。触发监听后，主要做了三件事：**

1. **生成条件评估报告**- 记录哪些配置类被匹配/排除**
2. **存储在ConditionEvaluationReport中**- 供后续使用**
3. **当开启debug时输出到控制台**- 显示详细的自动配置决策信息**

---

## **条件过滤器**

SpringBoot 内置了三个过滤器：spring-boot-autoconfigure-3.5.8.jar 的 META-INF/spring.factories 配置文件中存在三个过滤器

```java
