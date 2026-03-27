# Spring中的八大模式

---

## 简单工厂模式

获取 bean 的时候可以通过简单工厂模式（静态工厂模式）来获取；

---

## 工厂方法模式

FactoryBean是典型的工厂方法模式。在配置文件中通过factory-method属性来指定工厂方法，该方法是一个实例方法。

---

## 单例模式

Spring用的是双重判断加锁的单例模式。请看下面代码，我们之前讲解Bean的循环依赖的时候见过：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1666663352271-4ba8d737-1e32-4f0e-b01a-aa305ad3abea.png)

---

## 代理模式

Spring的AOP就是使用了动态代理实现的。

---

## 装饰器模式

JavaSE中的IO流是非常典型的装饰器模式。

**IoC 容器中的 Bean 包装：**

```java
// Bean 的装饰器模式应用
BeanWrapper wrapper = new BeanWrapperImpl(targetObject);
```

**Spring 使用装饰器来增强 Bean 的功能，如属性访问、类型转换等。**

****Spring中类名中带有：Decorator和Wrapper单词的类，都是装饰器模式。****

****

---

## 观察者模式

### Spring 容器生命周期管理

在 `AbstractApplicationContext` 的 `refresh()` 方法中：

```java
// Spring 容器启动时的观察者模式
public void refresh() {
    // 1. 准备刷新 - 发布 ContextRefreshedEvent
    initApplicationEventMulticaster();
    
    // 2. 通知所有监听器容器正在启动
    publishEvent(new ContextRefreshedEvent(this));
    
    // 3. 容器关闭时发布 ContextClosedEvent
    publishEvent(new ContextClosedEvent(this));
}
```

Spring 容器自己就是个"大主播"，在**启动、刷新、关闭**这些关键节点时，会发布事件通知所有"粉丝"（内置监听器），让它们执行相应的处理逻辑。

---

## 策略模式

**Resource 资源加载策略**

```java
// 策略接口
org.springframework.core.io.ResourceLoader

// 具体策略实现
ClassPathResourceLoader     // 类路径加载
FileSystemResourceLoader    // 文件系统加载  
UrlResourceLoader          // 网络资源加载
ServletContextResourceLoader // Web应用加载
```

Spring 根据资源路径的前缀（`classpath:`、`file:`、`http:`）自动选择不同的加载策略。

**事务管理策略**

```java
// 策略接口
org.springframework.transaction.PlatformTransactionManager

// 具体策略
DataSourceTransactionManager    // JDBC事务
JpaTransactionManager          // JPA事务
HibernateTransactionManager    // Hibernate事务
JtaTransactionManager          // 分布式事务
```

根据不同的数据访问技术，选择对应的事务管理实现。

**特点：**

+ 都有统一的策略接口
+ 多个具体实现类
+ 根据运行时条件动态选择策略

---

## 模板方法模式

Spring中的JdbcTemplate类就是一个模板类。它就是一个模板方法设计模式的体现。在模板类的模板方法execute中编写核心算法，具体的实现步骤在子类中完成。
