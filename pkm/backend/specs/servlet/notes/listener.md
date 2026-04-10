# 监听器 Listener

Servlet 监听器是 Servlet 规范中的一部分，主要用于监听 Web 应用中的特定事件，当这些事件发生时执行预定义的操作。监听器提供了一种事件驱动的编程模型，允许开发者在应用生命周期的关键点插入自定义逻辑。

---

## 主要监听器类型

Servlet 规范定义了以下几种监听器接口：

1. **ServletContext 监听器**
    - `ServletContextListener`：监听 Web 应用的启动和关闭
    - `ServletContextAttributeListener`：监听应用范围内属性的添加、移除和替换
2. **HttpSession 监听器**
    - `HttpSessionListener`：监听会话的创建和销毁
    - `HttpSessionAttributeListener`：监听会话范围内属性的添加、移除和替换
    - `HttpSessionActivationListener`：监听会话的激活和钝化(集群环境)
    - `HttpSessionBindingListener`：监听对象绑定到会话或从会话解绑
3. **ServletRequest 监听器**
    - `ServletRequestListener`：监听请求的初始化和销毁
    - `ServletRequestAttributeListener`：监听请求范围内属性的添加、移除和替换

---

## 典型应用场景

1. **应用初始化**：在应用启动时加载资源(数据库连接池、缓存数据等)
2. **资源清理**：在应用关闭时释放资源
3. **会话管理**：统计在线用户、会话超时处理
4. **请求监控**：记录请求日志、性能监控
5. **属性变更跟踪**：跟踪应用、会话或请求范围内属性的变化

---

## 配置方式

监听器可以通过以下两种方式配置：

1. **注解方式**：在监听器类上使用 `@WebListener` 注解

```java
@WebListener
public class MyListener implements ServletContextListener {...}
```

2. **web.xml 配置**：

```xml
<listener>
    <listener-class>com.example.MyListener</listener-class>
</listener>
```

---

## 以 ServletContextListener 为例

该监听器中提供了两个方法：

+ contextInitialized：服务器启动的时候这个方法自动调用。
+ contextDestroyed：服务器关闭的时候这个方法自动调用。

编写类实现 `ServletContextListener`接口：

```java
package com.jkweilai.listener;

import jakarta.servlet.ServletContextEvent;
import jakarta.servlet.ServletContextListener;
import jakarta.servlet.annotation.WebListener;

@WebListener
public class MyServletContextListener implements ServletContextListener {
    @Override
    public void contextInitialized(ServletContextEvent sce) {
        System.out.println("=====contextInitialized=====");
    }

    @Override
    public void contextDestroyed(ServletContextEvent sce) {
        System.out.println("=====contextDestroyed=====");
    }
}
```

`web.xml` 文件中配置监听器，或者使用 `@WebListener注解` 标注 。这里选择使用注解，更加方便一些。

启动和关闭服务器，观察控制台输出结果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749198649363-2c3d4952-dc36-4095-b5c7-a44987fc0a60.png)
