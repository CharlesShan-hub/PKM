# Servlet Advance

* [servlet-lifecycle](notes/servlet-lifecycle.md)：servlet不推荐写构造，推荐放到init，因为有参构造器会让无餐构造器消失。tomcat 被 url 请求时，tomcat 会 new 出来 servlet 对象，然后调用 init。这里可以写数据库连接池等初始化的操作。接着每次调用都会调用 service 函数。最后销毁时调用 destroy。
* [generic-servlet](notes/generic-servlet.md)：GenericServlet是实现了Servlet与ServletConfig的抽象类。
* [servlet-config](notes/servlet-config.md)
* [servlet-context](notes/servlet-context.md)
* [http-servlet](notes/http-servlet.md)
* [department-management](notes/department-management.md)
* [forward-and-redirect](notes/forward-and-redirect.md)
* [listener](notes/listener.md)
* [filter](notes/filter.md)