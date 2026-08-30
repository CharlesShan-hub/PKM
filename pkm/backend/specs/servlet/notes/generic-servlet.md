# GenericServlet

---

## 适配器设计模式

**在GoF（Gang of Four）提出的23种经典设计模式中，******适配器模式(Adapter Pattern)******是******结构型模式******的一种。**

### **模式定义**

**适配器模式将一个类的接口转换成客户期望的另一个接口，使得原本由于接口不兼容而不能一起工作的类可以一起工作。**

### **经典案例**

日志框架适配器

```java
// 目标接口
interface MyLogger {
    void log(String message);
}

// 被适配者1
class Log4jLogger {
    public void logMessage(String msg) {
        System.out.println("Log4j: " + msg);
    }
}

// 被适配者2
class Slf4jLogger {
    public void log(String content) {
        System.out.println("SLF4J: " + content);
    }
}

// 适配器1
class Log4jAdapter implements MyLogger {
    private Log4jLogger log4j;
    
    public Log4jAdapter(Log4jLogger log4j) {
        this.log4j = log4j;
    }
    
    @Override
    public void log(String message) {
        log4j.logMessage(message);
    }
}

// 适配器2
class Slf4jAdapter implements MyLogger {
    private Slf4jLogger slf4j;
    
    public Slf4jAdapter(Slf4jLogger slf4j) {
        this.slf4j = slf4j;
    }
    
    @Override
    public void log(String message) {
        slf4j.log(message);
    }
}

// 客户端可以统一使用MyLogger接口
public class Client {
    public static void main(String[] args) {
        MyLogger logger1 = new Log4jAdapter(new Log4jLogger());
        MyLogger logger2 = new Slf4jAdapter(new Slf4jLogger());
        
        logger1.log("使用Log4j记录日志");
        logger2.log("使用SLF4J记录日志");
    }
}
```

**这个案例展示了适配器模式如何在不修改原有代码的情况下，使不兼容的接口能够协同工作。**

---

## 缺省适配器设计模式

缺省适配器模式（Default Adapter Pattern），也称为默认适配器模式，是适配器模式的一种特殊形式。它主要用于为接口提供默认实现，使得子类只需关注自己感兴趣的方法，而不必实现接口中的所有方法。

### 模式定义

缺省适配器模式通过创建一个抽象类（适配器）实现目标接口，并为所有方法提供空实现或默认实现。具体子类可以继承这个适配器类，只覆盖它们感兴趣的方法。

### 模式结构

+ **目标接口(Target Interface)**：定义了大量方法的接口
+ **缺省适配器(Default Adapter)**：实现了目标接口，为所有方法提供默认实现
+ **具体实现类(Concrete Class)**：继承缺省适配器，只实现感兴趣的方法

### 示例代码

```java
// 目标接口 - 定义了很多方法
interface ServiceInterface {
    void operation1();
    void operation2();
    void operation3();
    // ...可能还有很多方法
}

// 缺省适配器 - 提供所有方法的默认实现
abstract class DefaultAdapter implements ServiceInterface {
    public void operation1() {} // 空实现
    public void operation2() {} // 空实现
    public void operation3() {} // 空实现
    // ...其他方法的空实现
}

// 具体类 - 只实现感兴趣的方法
class ConcreteService extends DefaultAdapter {
    @Override
    public void operation2() {
        System.out.println("只实现了operation2方法");
    }
}
```

### 与普通适配器模式的区别

1. **目的不同**：普通适配器模式用于接口转换，缺省适配器用于提供默认实现
2. **结构不同**：普通适配器包含被适配对象，缺省适配器直接实现目标接口
3. **使用场景不同**：普通适配器解决接口不兼容问题，缺省适配器解决接口方法过多问题

缺省适配器模式是一种非常实用的设计模式，特别适用于处理包含大量方法的接口，它能显著简化客户端代码的编写。

---

## GenericServlet 是缺省适配器

`GenericServlet` 是一个典型的 **缺省适配器模式**。**为什么是缺省适配器模式？**

1. **背景：Servlet 接口的复杂性**  
`Servlet` 接口定义了多个方法（如 `init()`, `service()`, `destroy()`, `getServletConfig()`, `getServletInfo()`），但实际开发中，我们通常只关心 `service()` 方法（处理请求的核心逻辑）。如果直接实现 `Servlet` 接口，必须实现所有方法，即使某些方法不需要。
2. **GenericServlet 的作用**  
`GenericServlet` 是一个抽象类，它实现了 `Servlet` 接口，并为所有方法提供了 **默认的空实现**（比如 `init()` 和 `destroy()` 是空方法）。这样，用户只需继承 `GenericServlet` 并重写自己关心的方法（通常是 `service()`），而不必强制实现所有接口方法。
3. **简化子类实现**  
子类可以只关注核心逻辑（如 `service()`），而无需处理其他不必要的方法。例如：

```java
public class MyServlet extends GenericServlet {
    @Override
    public void service(ServletRequest req, ServletResponse res) {
        // 只需实现业务逻辑
    }
}
```

`GenericServlet` 是缺省适配器模式的典型应用，它通过默认空实现简化了 `Servlet` 接口的使用，****让开发者能够专注于核心逻辑****。

---

## GenericServlet 源码剖析

GenericServlet 源码如下：

```java
package jakarta.servlet;

import java.io.IOException;
import java.util.Enumeration;

public abstract class GenericServlet implements Servlet, ServletConfig, java.io.Serializable {

    // 在 init(ServletConfig) 方法被调用时，该属性被赋值。
    private transient ServletConfig config;

    /**
     * 什么都不做。所有的 Servlet 初始化工作都由某个 init 方法完成。
     */
    public GenericServlet() {}

    /**
     * 由 Servlet 容器调用，用于通知 Servlet 它即将被投入服务。 
     */
    @Override
    public void init(ServletConfig config) throws ServletException {
        this.config = config;
        this.init();
    }

    /**
     * 由Servlet容器调用，以允许Servlet对请求作出响应。
     */
    @Override
    public abstract void service(ServletRequest req, ServletResponse res) throws ServletException, IOException;

    /**
     * 由 Servlet 容器调用，用于通知 Servlet 它即将被停止服务。
     */
    @Override
    public void destroy() {}

    /**
     * 获取ServletConfig对象。
     */ 
    @Override
    public ServletConfig getServletConfig() {
        return config;
    }

    /**
     * 返回有关该 Servlet 的信息，例如作者、版本和版权信息。
     * 默认情况下，此方法返回空字符串。如需返回有意义的值，请重写此方法。
     */
    @Override
    public String getServletInfo() {
        return "";
    }

    // ================================================以下方法都是为了开发方便额外扩展的方法====================================================

    /**
     * 如果要重写init方法，建议重写这个无参数的init方法，如果你重写有参数的 init(ServletConfig) 方法，config 属性将无法赋值。
     */
    public void init() throws ServletException {}

    // 额外扩展的方法
    @Override
    public String getInitParameter(String name) {
        return getServletConfig().getInitParameter(name);
    }

    // 额外扩展的方法
    @Override
    public Enumeration<String> getInitParameterNames() {
        return getServletConfig().getInitParameterNames();
    }

    // 额外扩展的方法
    @Override
    public ServletContext getServletContext() {
        return getServletConfig().getServletContext();
    }

    // 额外扩展的方法：获取当前servlet实例的名字。也就是<servlet-name>的配置。
    @Override
    public String getServletName() {
        return config.getServletName();
    }

    // 额外扩展的方法
    public void log(String message) {
        getServletContext().log(getServletName() + ": " + message);
    }

    // 额外扩展的方法
    public void log(String message, Throwable t) {
        getServletContext().log(getServletName() + ": " + message, t);
    }
}

```

---

## GenericServlet 的使用

有了 `GenericServlet`，编写 `Servlet`类时可以不再直接实现 `Servlet`接口。

编写 `WelcomServlet`继承 `GenericServlet`这个****抽象类****，如果你只需要处理用户的请求，则只需要重写 `service`方法即可。代码如下：

```java
package com.jkweilai.servlet;

import jakarta.servlet.GenericServlet;
import jakarta.servlet.ServletException;
import jakarta.servlet.ServletRequest;
import jakarta.servlet.ServletResponse;

import java.io.IOException;

public class WelcomeServlet extends GenericServlet {
    @Override
    public void service(ServletRequest request, ServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        response.getWriter().print("<h1>欢迎学习 GenericServlet</h1>");
    }
}

```

编写 `web.xml`配置：

```xml
<servlet>
    <servlet-name>welServlet</servlet-name>
    <servlet-class>com.jkweilai.servlet.WelcomeServlet</servlet-class>
</servlet>
<servlet-mapping>
    <servlet-name>welServlet</servlet-name>
    <url-pattern>/wel</url-pattern>
</servlet-mapping>
```

启动服务器，打开浏览器，输入 URL：http://localhost:8080/web01/wel

![1748937624855-09f37e67-5dc8-4227-8d77-872897bd0019.png](../assets/1748937624855-09f37e67-5dc8-4227-8d77-872897bd0019.png)

可以看到，编写 Servlet 类更加的方便了。只需要继承 `GenericServlet`，重写 `service`方法即可。
