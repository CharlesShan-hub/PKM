# JavaEE 概述

JavaEE（Java Platform, Enterprise Edition）是Sun Microsystems（后被Oracle收购）推出的企业级Java平台，现演变为**Jakarta EE**。以下是详细解答：

---

## 什么是JavaEE

+ **定义**：JavaEE是一套基于Java SE（标准版）的企业级开发规范集合，用于构建分布式、可扩展、可靠的多层应用（如Web应用、微服务等）。
+ **特点**：提供标准化的组件和API（如Servlet、JPA等），简化企业开发中的复杂性（如事务、安全、并发等）。

---

## JavaEE的核心规范（常用）

JavaEE包含以下关键规范（不同版本略有增减）：

|  **分类**   | **规范**                                               | **用途**                          |
| :-------: | ---------------------------------------------------- | ------------------------------- |
| **Web层**  | **Servlet**（要会）                                      | 处理HTTP请求/响应                     |
|           | JSP (JavaServer Pages)                               | 动态页面生成（现多被模板引擎替代）               |
|           | JSF (JavaServer Faces)                               | 组件化Web框架                        |
|  **业务层**  | EJB (Enterprise JavaBeans)                           | 分布式业务逻辑（如事务管理）                  |
|           | CDI (Contexts and Dependency Injection)              | 依赖注入和上下文管理                      |
|  **数据层**  | **JPA** (Java Persistence API)（要会）                   | 对象关系映射（ORM）                     |
|           | JTA (Java Transaction API)                           | 分布式事务管理                         |
| **消息/集成** | **JMS** (Java Message Service)（要会）                   | 异步消息队列（如ActiveMQ、RabbitMQ集成）    |
|  **安全**   | JAAS (Java Authentication and Authorization Service) | 认证和授权                           |
|  **其他**   | JAX-RS (Java API for RESTful Services)               | RESTful Web服务（如Jersey、RESTEasy） |
|           | JAX-WS (Java API for XML Web Services)               | SOAP Web服务                      |
因此：Servlet 属于 JavaEE 规范。

---

## Jakarta EE是什么

+ **背景**：2017年Oracle将JavaEE移交给**Eclipse基金会**（开源组织），因商标问题，JavaEE更名为**Jakarta EE**。
+ **关系**：
    - Jakarta EE是JavaEE的延续，目前最新版本为**Jakarta EE 10**（2022年发布）。
    - 规范名称中的`javax.*`包逐步改为`jakarta.*`（如`javax.servlet` → `jakarta.servlet`）。

| **对比项** | **JavaEE**         | **Jakarta EE**       |
| ------- | ------------------ | -------------------- |
| 维护方     | Oracle             | Eclipse基金会           |
| 版本      | 最终版本JavaEE 8（2017） | 持续更新（如Jakarta EE 10） |
| 包名      | `javax.*`          | `jakarta.*`          |
| 新特性     | 停止更新               | **新增云原生支持**          |

---

## Jakarta EE 10 API 帮助文档

主站点：<https://jakarta.ee/>
