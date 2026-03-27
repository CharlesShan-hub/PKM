# Auto Configuration Import Filters

org.springframework.boot.autoconfigure.AutoConfigurationImportFilter=\
org.springframework.boot.autoconfigure.condition.OnBeanCondition,\
org.springframework.boot.autoconfigure.condition.OnClassCondition,\
org.springframework.boot.autoconfigure.condition.OnWebApplicationCondition

```

**三个过滤器对应的条件注解：**

| **过滤器** | **对应的条件注解** | **作用** |
| --- | --- | --- |
| `**OnClassCondition**` | `**@ConditionalOnClass**``**@ConditionalOnMissingClass**` | **根据类路径是否存在某个类来过滤** |
| `**OnBeanCondition**` | `**@ConditionalOnBean**``**@ConditionalOnMissingBean**` | **根据容器中是否存在某个Bean来过滤** |
| `**OnWebApplicationCondition**` | `**@ConditionalOnWebApplication**``**@ConditionalOnNotWebApplication**` | **根据是否是Web应用来过滤** |

---

## **条件过滤源码分析**

我们需要分析这个最核心的步骤，重新回到：`AutoConfigurationImportSelector`类的`getAutoConfigurationEntry`方法。

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
    // 这个就是最核心的步骤：根据条件注解进行过滤，底层3个过滤器都会起作用。
    configurations = getConfigurationClassFilter().filter(configurations);
    fireAutoConfigurationImportEvents(configurations, exclusions);
    return new AutoConfigurationEntry(configurations, exclusions);
}

```

进入 `filter`方法：

```java

List<String> filter(List<String> configurations) {
    long startTime = System.nanoTime();
    String[] candidates = StringUtils.toStringArray(configurations);
    boolean skipped = false;
    for (AutoConfigurationImportFilter filter : this.filters) {
        boolean[] match = filter.match(candidates, this.autoConfigurationMetadata);
        for (int i = 0; i < match.length; i++) {
            if (!match[i]) {
                candidates[i] = null;
                skipped = true;
            }
        }
    }
    if (!skipped) {
        return configurations;
    }
    List<String> result = new ArrayList<>(candidates.length);
    for (String candidate : candidates) {
        if (candidate != null) {
            result.add(candidate);
        }
    }
    if (logger.isTraceEnabled()) {
        int numberFiltered = configurations.size() - result.size();
        logger.trace("Filtered " + numberFiltered + " auto configuration class in "
                + TimeUnit.NANOSECONDS.toMillis(System.nanoTime() - startTime) + " ms");
    }
    return result;
}

```

以上方法中最核心的代码就是：

```java

for (AutoConfigurationImportFilter filter : this.filters) {
    boolean[] match = filter.match(candidates, this.autoConfigurationMetadata);
    for (int i = 0; i < match.length; i++) {
        if (!match[i]) {
            candidates[i] = null;
            skipped = true;
        }
    }
}

```

这个最外层循环会循环 3 次，因为 SpringBoot 内置了 3 个过滤器。

外层循环每循环一次，内层循环 156 次。

**以上代码中最核心的代码是：**

```java

// 第一个参数：156个自动配置类
// 第二个参数：自动配置元数据（914个条件）
boolean[] match = filter.match(candidates, this.autoConfigurationMetadata);

```

`**914**`**个条件是写在配置文件中的，在 **`**spring-boot-autoconfigure-3.5.8.jar**`**的 **`**META-INF/spring-autoconfigure-metadata.properties**`**文件中。该文件一共 914 行，每一行都是一个条件，这些条件是用来约束那 156 个自动配置类的。**思考：**为什么要把 914 个条件放到一个属性文件中？这些条件不应该都在自动配置类上吗？直接通过反射读取 156 个配置类动态获取配置类上的条件不行吗？答案是：不行，原因是效率太低。**

