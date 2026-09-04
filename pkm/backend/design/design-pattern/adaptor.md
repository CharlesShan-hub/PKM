# 适配器模式

## 适配器设计模式

在GoF（Gang of Four）提出的23种经典设计模式中，**适配器模式(Adapter Pattern)** 是**结构型模式**的一种。

### 模式定义

适配器模式将一个类的接口转换成客户期望的另一个接口，使得原本由于接口不兼容而不能一起工作的类可以一起工作。

### 经典案例

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

这个案例展示了适配器模式如何在不修改原有代码的情况下，使不兼容的接口能够协同工作。

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
