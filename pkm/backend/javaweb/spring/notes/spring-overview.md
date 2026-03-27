# Spring概述

---

## Spring简介

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1663722326376-02a67b9e-f80f-4717-ac33-1253723135f3.png)

来自百度百科

> **Spring是一个由Rod Johnson创建的开源框架，其核心目标是简化复杂的企业级应用开发。通过提供******简单性、可测试性与松耦合性******这三大特性，它能让任何Java应用的开发都变得更加高效和优雅。**
>
> ****Spring是一个轻量级的控制反转(IoC)和面向切面(AOP)的容器框架。****
>
> ****Spring最初的出现是为了解决EJB臃肿的设计，以及难以测试等问题。****
>
> ****Spring为简化开发而生，让程序员只需关注核心业务的实现，尽可能的不再关注非业务逻辑代码（事务控制，安全日志等）。****
>

****

---

## Spring 的 7 个模块

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763643561157-765b31eb-9766-4a14-948b-315a09fec552.png)

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763643650645-a4daae43-075d-4bc7-87dd-1e12c8edf581.png)

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763643697234-10890100-6dd7-4c70-9d40-4132b2d641ed.png)

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763643800797-f4c8ef1b-3f81-448c-a403-0ee8f07b6e45.png)

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763643838115-953e83de-1182-4e92-ad81-04d15a4b65cd.png)

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763643872341-82bca2fa-e2df-49a1-b2f8-8875bf1a9c3f.png)

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763643893472-6532f10a-d928-4d4b-a72e-95fca870596d.png)

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1763643919695-920d67f8-1824-46ed-a266-a72a78f933af.png)

---

## web 同步与 web 异步的区别

Spring Web MVC 是同步方案。Spring WebFlux 是异步方案。它们的区别是：

****

**想象一个异步文件下载：**

**1. 传统同步方式 (MVC):**

```java
// 线程会停在这里等待，直到文件下载完成
byte[] data = downloadFileFromNetwork("http://example.com/file");
// 下载完成后，才继续执行这里
return data;
```

**2. WebFlux方式 (基于回调):**

```java
// 立即返回，不等待
downloadFileFromNetwork("http://example.com/file", new Callback() {
    // 这是一个回调函数
    @Override 
    public void onDataReceived(byte[] data) {
        // 当数据真正到达时，这个函数会被自动调用
        sendResponse(data);
    }
    
    @Override
    public void onError(Throwable error) {
        // 出错时的回调
        sendError(error);
    }
});
// 注意：代码执行到这里时，文件可能还没开始下载！
```

**核心要点：**

+ **"你先去忙，好了call我"**：主线程不等待，立即返回
+ **回调函数是"联系方式"**：告诉系统"数据到了之后，请调用我这个函数"
+ **事件驱动**：当网络数据到达、数据库查询完成等事件发生时，自动触发相应的回调函数

---

## Spring特点

1. ****控制反转/依赖注入******：对象不用自己找依赖，Spring容器自动"送货上门"，实现松耦合。**
2. ****面向切面编程******：像切洋葱一样把通用功能（日志、事务）横向抽取，让核心业务更纯净。**
3. ****数据访问支持******：用统一的方式操作各种数据库，告别繁琐的JDBC代码和不同数据库的兼容问题。**
4. ****声明式事务管理******：只需一个**`**@Transactional**`**注解，复杂的事务管理就像"开关"一样简单可控。**
5. ****高度模块化设计******：像乐高积木，需要什么拿什么，不必引入整个框架。**
6. ****强大测试支持******：专为测试而生，轻松模拟完整Spring环境进行单元和集成测试。**
