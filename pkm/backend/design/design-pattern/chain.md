# 责任链设计模式

责任链模式（Chain of Responsibility Pattern）是 GoF 23 种设计模式中的一种**行为型模式**，其主要目的是**将请求的发送者和接收者解耦**，让多个对象都有机会处理请求，从而避免请求发送者与接收者之间的强耦合关系。

### 核心思想

将多个处理请求的对象连成一条链，请求沿着这条链传递，直到有一个对象处理它为止。每个处理者都包含对下一个处理者的引用，形成链式结构。

### 关键角色

1. **抽象处理者（Handler）**  
    - 定义处理请求的接口（通常包含一个处理请求的方法和一个设置下一个处理者的方法）。
    - 可以包含对下一个处理者的引用（即“链”的实现）。
2. **具体处理者（Concrete Handler）**  
    - 实现抽象处理者的方法，判断是否能处理当前请求。
    - 如果能处理则处理，否则将请求转发给下一个处理者。
3. **客户端（Client）**  
    - 组装责任链（设置链中处理者的顺序关系）。
    - 向链的头部发起请求。

### 工作流程

1. 客户端发起请求到责任链的第一个处理者。
2. 每个处理者判断自己是否能处理该请求：
    - 能处理 → 处理并结束流程。
    - 不能处理 → 将请求传递给下一个处理者。
3. 如果链中所有处理者都无法处理，请求可能被忽略或由默认逻辑处理。

### 该模式的优点

+ **解耦**：请求发送者无需知道具体由哪个对象处理，只需向链头发送请求。
+ **动态组合**：可以灵活调整链中处理者的顺序或增减处理者。
+ **符合开闭原则**：新增处理者无需修改现有代码。

### 经典应用场景

1. 多级审批流程（如请假审批：组长 → 经理 → CEO）。
2. 异常处理（如 Java 中的 `try-catch` 块，按顺序匹配异常类型）。
3. 过滤器链（如 Web 框架中的中间件处理 HTTP 请求）。

### 简单代码示例

```java
// 抽象处理者
abstract class Handler {
    protected Handler next;
    public void setNext(Handler next) { this.next = next; }
    public abstract void handleRequest(String request);
}

// 具体处理者A
class ConcreteHandlerA extends Handler {
    public void handleRequest(String request) {
        if (request.equals("A")) {
            System.out.println("Handler A 处理请求");
        } else if (next != null) {
            next.handleRequest(request); // 传递给下一个处理者
        }
    }
}

// 具体处理者B
class ConcreteHandlerB extends Handler {
    public void handleRequest(String request) {
        if (request.equals("B")) {
            System.out.println("Handler B 处理请求");
        } else if (next != null) {
            next.handleRequest(request);
        }
    }
}

// 客户端
public class Client {
    public static void main(String[] args) {
        Handler handlerA = new ConcreteHandlerA();
        Handler handlerB = new ConcreteHandlerB();
        handlerA.setNext(handlerB); // 组装责任链
        
        handlerA.handleRequest("B"); // 输出：Handler B 处理请求
    }
}
```

### **Filter 是责任链模式的典型应用**

1. ****角色对应******：**
    - ****抽象处理者******→**`****Filter****`**接口（定义**`****doFilter****`**方法）。**
    - ****具体处理者******→ 用户实现的 Filter（如日志、鉴权 Filter）。**
    - ****链式传递******→ 通过**`****FilterChain.doFilter()****`**将请求传递给下一个节点。**
2. ****工作流程******：**
    - **请求依次经过多个 Filter，每个 Filter 可前置处理（如权限校验），再通过**`****chain.doFilter()****`**传递请求，最后还可能执行后置处理（如日志记录）。**
    - **链的组装通过**`****web.xml****`**或注解配置顺序。**
3. ****对比经典责任链******：**
    - ****强制传递******：必须调用**`****chain.doFilter()****`**确保请求到达 Servlet，而经典模式可能中途终止。**
    - ****双向处理******：支持请求前/后的拦截（经典模式通常单向）。**
