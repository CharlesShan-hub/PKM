# Tomcat 简介

---

## Web 服务器 & 应用服务器

> 一句话：webserver只实现了Jakarta规范的Servlet+JSP，应用服务器实现了全部规范。所以很多应用服务器内嵌tomcat。

### Web Server

**Web 服务器**是专门用于处理 HTTP 请求的软件，主要功能是存储、处理和传递网页给客户端（通常是浏览器）。

**主要特点**：

- 处理 HTTP/HTTPS 协议请求
- 返回静态内容（HTML、CSS、JS、图片等）
- 轻量级，性能高

**Java Web 服务器代表**：

1. **Apache Tomcat**​ - 最流行的 Java Web 服务器和 Servlet 容器
2. **Jetty**​ - 轻量级、嵌入式的 Web 服务器
3. **Undertow**​ - JBoss 提供的轻量高性能 Web 服务器

### Application Server

**应用服务器**是为应用程序提供业务逻辑的中间件平台，功能比 Web 服务器更全面。

**主要特点**：

- 包含 Web 服务器的所有功能
- 支持 EJB、JMS、JTA 等企业级特性
- 提供事务管理、连接池、集群等高级功能
- 支持分布式计算和复杂业务逻辑

**Java 应用服务器代表**：

1. **WildFly**​ (原 JBoss AS) - Red Hat 开发的开源应用服务器
2. **WebLogic**​ - Oracle 提供的商业应用服务器
3. **WebSphere Application Server**​ - IBM 的商业应用服务器
4. **GlassFish**​ - Oracle 提供的开源参考实现

### 总结

* **Web 服务器**​ = 只实现了 Jakarta EE 中的 Servlet + JSP 规范。
* **应用服务器**​ = 实现了完整的 Jakarta EE 规范。
* **现代趋势**：随着微服务架构的流行，轻量级的 **Web 服务器**（如 Tomcat）**结合 Spring Boot** 等框架的使用越来越普遍，传统重量级应用服务器的使用在减少。

---

## Tomcat 简介

### 开发与维护

- **创始人**：Tomcat 最初由 Sun Microsystems 的工程师 **James Duncan Davidson**​ 开发（1999 年），后捐赠给 Apache 软件基金会。
- **当前维护**：由 **Apache 软件基金会**​ 下的开源社区维护，是 Apache Jakarta 项目的一部分。

### 名字和 logo

**Tomcat**​ 的名字源自开发者 James Duncan Davidson 养的公猫（Tom）。象征敏捷（轻量级）和独立（自己可以照顾自己）。

![tomcat](../assets/tomcat.png)

### 核心功能

- **Servlet/JSP 容器**：实现 Java EE（现 Jakarta EE）的 Servlet、JSP 规范，支持动态 Web 应用。
- **轻量级**：相比完整应用服务器，Tomcat 更专注于 Servlet 容器功能。
- **嵌入式支持**：可嵌入 Spring Boot 等框架作为内嵌服务器。

### 核心组件

- **Catalina**：Servlet 容器。（**它是最核心的组件，相当于 Tomcat 的大脑**）**Santa Catalina Island**​ 是美国加州附近的一座风景优美的岛屿，延续了 Apache 软件基金会的“地理风”命名风格。
- **Coyote**：HTTP 连接器（支持 HTTP/1.1、HTTP/2）。
- **Jasper**：JSP 引擎。
- **Cluster**：高可用性模块。

### 版本历史

| **Tomcat 版本**​   | **发布日期**​         | **Servlet/JSP 规范**​       | **Java EE/Jakarta EE 版本**​ | **JDK 要求**​   | **状态**​           | **备注**​                                             |
| ---------------- | ----------------- | ------------------------- | -------------------------- | ------------- | ----------------- | --------------------------------------------------- |
| Tomcat 11​       | 2023 年            | Servlet 6.0, JSP 3.1      | Jakarta EE 10              | JDK 11+       | 过渡版本​             |                                                     |
| **Tomcat 10.1**​ | **2022 年（持续更新）**​ | **Servlet 6.0, JSP 3.1**​ | **Jakarta EE 10**​         | **JDK 11+**​  | **长期支持（LTS）**​    | **包名改为`jakarta.`（不兼容旧版）**  <br>**当前企业主流版本，呈上升趋势。**​ |
| Tomcat 10.0​     | 2021 年            | Servlet 5.0, JSP 3.0      | Jakarta EE 9               | JDK 8+        | 过渡版本              | 首个 Jakarta EE 兼容版本                                  |
| Tomcat 9.0​      | 2018 年（持续更新）​     | Servlet 4.0, JSP 2.3​     | Java EE 8​                 | JDK 8+        | 长期支持（LTS）​        | 当前企业使用呈减少趋势。​                                       |
| Tomcat 8.5​      | 2016 年​           | Servlet 3.1, JSP 2.3​     | Java EE 7​                 | JDK 7+（推荐 8+） | 2024 年 3 月终止支持​   | 支持 HTTP/2、TLS 1.2 等​                                |
| Tomcat 7.0​      | 2011 年​           | Servlet 3.0, JSP 2.2​     | Java EE 6​                 | JDK 6+​       | 已终止（2021 年 3 月）​  | 需升级到更高版本​                                           |
| Tomcat 6.0​      | 2007 年​           | Servlet 2.5, JSP 2.1​     | Java EE 5​                 | JDK 5+​       | 已终止（2016 年 12 月）​ | 仅适合遗留系统​                                            |
| Tomcat 5.5​      | 2004 年​           | Servlet 2.4, JSP 2.0​     | J2EE 1.4​                  | JDK 1.4+      | 已终止（2012 年）       | 需要 JDK 1.4 或更高版本​                                   |
| Tomcat 4.x​      | 2002 年​           | Servlet 2.3, JSP 1.2​     | J2EE 1.3​                  | JDK 1.3+      | 已终止​              | 首个 Apache 主导版本​                                     |
| Tomcat 3.x​      | 1999 年​           | Servlet 2.2, JSP 1.1​     | -​                         | JDK 1.1+      | 已终止​              | 原始版本（Sun 捐赠代码）​                                     |

**Jakarta EE、Java SE（JDK）、Servlet、Tomcat，它们的关系是什么？**

- Jakarta EE 是 Java 企业级开发规范。
- Jakarta EE 是建立在 Java SE 基础上的（JDK 是最基本的）。
- Jakarta EE 中的子规范很多，Servlet 是其中的一个子规范。
- Tomcat 是实现了 Servlet 规范的 Web 服务器/Web 容器。
