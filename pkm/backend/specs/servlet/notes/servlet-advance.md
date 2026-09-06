# Servlet Advance

![servlet-draw.excalidraw|1000](../assets/servlet-draw.excalidraw.md)

* [servlet-lifecycle](notes/servlet-lifecycle.md)：servlet不推荐写构造，推荐放到init，因为有参构造器会让无餐构造器消失。tomcat 被 url 请求时，tomcat 会 new 出来 servlet 对象，然后调用 init。这里可以写数据库连接池等初始化的操作。接着每次调用都会调用 service 函数。最后销毁时调用 destroy。
* [generic-servlet](notes/generic-servlet.md)：GenericServlet是实现了Servlet与ServletConfig的抽象类。
* [servlet-config](notes/servlet-config.md)：配置信息写到xml里面，程序可以通过GenericServlet或者ServletConfig对象获取配置信息。
* [servlet-context](notes/servlet-context.md)：ServletContent用来保存应用级别的数据。
    * `getInitParameterNames`获取配置文件中单Servlet的`<init-param>`与全局的`<context-param>`
    * `setAttribute`（或者get/remove）在程序中操控全局共享的缓存。
    * `getContextPath`获取根目录，`getRealPath`获取到某一文件夹的绝对路径。
* [http-servlet](notes/http-servlet.md)：HttpServlet是GenericServlet的利用模板方法设计模式的子类。子类只需要重写`doGet`或者`doPost`这种方法就好了。其中405错误是get或者post等没实现，但是访问了导致的。
* [department-management](notes/department-management.md)：项目实践
* [forward-and-redirect](notes/forward-and-redirect.md)
* [listener](notes/listener.md)
* [filter](notes/filter.md)