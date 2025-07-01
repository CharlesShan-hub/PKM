# Springboot Introduction

## 资料

Spring Boot是一个基于Spring的套件，它帮我们预组装了Spring的一系列组件，以便以尽可能少的代码和配置来开发基于Spring的Java应用程序。

* 官网: https://spring.io/projects/spring-boot
* 廖雪峰: https://liaoxuefeng.com/books/java/springboot/index.html
* 网课(黑马):  https://www.bilibili.com/video/BV14z4y1N7pg

---
## ​Spring 项目​概要​

* spring 所有的项目: https://spring.io/projects

1. 核心项目
	1. ​**​Spring Framework​**​
	    - 核心功能：依赖注入、事务管理、Web应用、数据访问、消息传递等。
	    - 特点：模块化设计，按需使用。
	2. ​**​Spring Boot​**​
	    - 快速启动Spring应用，提供默认配置（约定优于配置）。
	3. ​**​Spring Data​**​
	    - 统一数据访问支持（关系型/非关系型数据库、Map-Reduce等）。
	4. ​**​Spring Security​**​
	    - 全面的身份验证和授权支持，保护应用程序安全。
	5. ​**​Spring Session​**​
	    - 管理用户会话信息的API和实现。
2. ​​分布式系统与微服务​​
	1. ​**​Spring Cloud​**​
	    - 分布式系统工具包（如服务发现、配置管理）。
	    - 微服务部署支持。
	2. ​**​Spring Cloud Data Flow​**​
	    - 数据微服务应用的编排服务。
	3. ​**​Spring for GraphQL​**​
	    - 基于GraphQL Java的Spring应用支持。
3. 集成与API开发​​
	1. ​**​Spring Integration​**​
	    - 企业集成模式（轻量级消息传递和声明式适配器）。
	2. ​**​Spring HATEOAS​**​
	    - 遵循HATEOAS原则的RESTful资源表示。
	3. ​**​Spring REST Docs​**​
	    - 结合手写文档与自动化测试片段生成RESTful服务文档。
	4. ​**​Spring Shell​**​
	    - CLI工具简化RESTful应用的开发和测试。
4. 新兴领域支持​​
	1. ​**​Spring AI​**​
	    - AI工程框架，连接企业数据/API与AI模型。
	2. ​**​Spring Batch​**​
	    - 高容量批处理操作优化。
	3. ​**​Spring AMQP​**​
	    - 基于AMQP的消息解决方案。
	4. ​**​Spring Statemachine​**​
	    - 状态机概念在Spring应用中的实现。
	5. ​**​Spring Web Flow​**​
	    - 控制导航的Web应用（如多步骤表单）。
5. 其他工具​
	- ​**​Spring Modulith​**​：模块化Spring Boot应用开发。
	- ​**​Spring LDAP​**​：简化LDAP应用开发的模板工具。
	- ​**​Spring Flo​**​：可视化管道构建器（HTML5/JavaScript）。

📌 ​**​总结​**​：​**​Spring Boot 是绝对核心​**​，其他项目围绕它扩展。企业开发中 90% 会用到 Boot + Data + Security。

