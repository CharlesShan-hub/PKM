# Background

1. Servlet 是 Spring MVC 的核心。
2. Servlet 是 Server Applet 的简称，可以认为是服务器端的小java程序。
3. 模板技术：早期使用 JSP（目前基本已被弃用），现多采用 Thymeleaf 作为替代。
4. Servlet 是 [BS架构](../details/bs-cs-architecture.md)（浏览器/服务器）的技术。
5. 从浏览器访问URL到服务器响应并最终渲染页面的完整[通信流程](../details/bs-communication-principle.md)（B/S通信原理），包括：URL结构、DNS解析、HTTP请求/响应、浏览器渲染等关键环节。
6. Servlet就是[JavaEE](../details/javaee-overview.md)的13种规范之一。
7. 应用服务器实现了完整的 JavaEE 的规范，很庞大，现在用的更多的是 Web 服务器，只实现 JavaEE 的 Servlet 和 JSP，Java Web 服务器有很多，比如：[tomcat](../details/tomcat-server.md)、Jetty、Undertow。
8. Servlet是一个接口，web项目中javaweb服务器实现接口，后端开发人员使用接口，从而实现了解耦合。可以参考一个简单模拟：[servlet-deep-dive](servlet-deep-dive.md)。
9. [http-protocol](http-protocol.md)