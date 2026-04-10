# request 常用方法总结

---

## ServletRequest 接口

以下是 ServletRequest 接口中的方法：

```java
// 将指定名称的属性绑定到请求对象中
void setAttributes(String name, Object o);
// 返回请求对象中指定名称的属性值
Object getAttribute(String name);
// 移除请求对象中指定名称的属性
void removeAttribute(String name);

// 设置请求体的字符编码格式
void setCharacterEncoding(String env);

// 返回请求中指定名称的参数值（单值）
String getParameter(String name);
// 返回请求中指定名称的所有参数值（多值，如复选框）
String[] getParameterValues(String name);
// 返回包含所有请求参数的键值对映射
Map<String,String[]> getParameterMap();
// 返回请求中所有参数名称的枚举
Enumeration<String> getParameterNames();

// 返回客户端IP地址
String getRemoteAddr();
// 返回指定路径的请求分派器，用于服务器端转发
RequestDispatcher getRequestDispatcher(String path);

// 判断请求是否通过安全协议（如HTTPS）发送
boolean isSecure();
```

---

## HttpServletRequest 接口

以下是关于 `HttpServletRequest`接口增加的方法，HttpServletRequest 接口继承了 ServletRequest 接口：

```java
// 返回当前Web应用的上下文路径
String getContextPath();
// 返回客户端发送的所有Cookie数组
Cookie[] getCookies();
// 返回指定请求头的值
String getHeader(String name);
// 返回HTTP请求方法（如GET、POST等）
String getMethod();
// 返回请求的URI（不包含协议、主机和查询参数）
String getRequestURI();
// 返回完整的请求URL（不包括查询参数）
StringBuffer getRequestURL();
// 返回请求URL中调用Servlet的部分
String getServletPath();
// 返回当前会话，若无则创建新会话
HttpSession getSession();
```
