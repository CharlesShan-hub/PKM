# JSP

- 我的第一个JSP程序：
  
  - 在WEB-INF目录之外创建一个index.jsp文件，然后这个文件中没有任何内容。
  
- 将上面的项目部署之后，启动服务器，打开浏览器，访问以下地址：
  - http://localhost:8080/jsp/index.jsp 展现在大家面前的是一个空白。
  - 实际上访问以上的这个：index.jsp，底层执行的是：index_jsp.class 这个java程序。
  - 这个index.jsp会被tomcat翻译生成index_jsp.java文件，然后tomcat服务器又会将index_jsp.java编译生成index_jsp.class文件
  - 访问index.jsp，实际上执行的是index_jsp.class中的方法。
  
- JSP实际上就是一个Servlet。
  - index.jsp访问的时候，会自动翻译生成index_jsp.java，会自动编译生成index_jsp.class，那么index_jsp 这就是一个类。
  - index_jsp 类继承 HttpJspBase，而HttpJspBase类继承的是HttpServlet。所以index_jsp类就是一个Servlet类。
  - jsp的生命周期和Servlet的生命周期完全相同。完全就是一个东西。没有任何区别。
  - jsp和servlet一样，都是单例的。（假单例。）
  
- jsp文件第一次访问的时候是比较慢的，为什么？
  - 为什么大部分的运维人员在给客户演示项目的时候，为什么提前先把所有的jsp文件先访问一遍。
  - 第一次比较麻烦：
    - 要把jsp文件翻译生成java源文件
    - java源文件要编译生成class字节码文件
    - 然后通过class去创建servlet对象
    - 然后调用servlet对象的init方法
    - 最后调用servlet对象的service方法。
  - 第二次就比较快了，为什么？
    - 因为第二次直接调用单例servlet对象的service方法即可。
  
- JSP是什么？
  - JSP是java程序。（JSP本质还是一个Servlet）
  - JSP是：JavaServer Pages的缩写。（基于Java语言实现的服务器端的页面。）
  - Servlet是JavaEE的13个子规范之一，那么JSP也是JavaEE的13个子规范之一。
  - JSP是一套规范。所有的web容器/web服务器都是遵循这套规范的，都是按照这套规范进行的“翻译”
  - 每一个web容器/web服务器都会内置一个JSP翻译引擎。
  
- 对JSP进行错误调试的时候，还是要直接打开JSP文件对应的java文件，检查java代码。

- 开发JSP的最高境界：
  
  - 眼前是JSP代码，但是脑袋中呈现的是java代码。
  
- JSP既然本质上是一个Servlet，那么JSP和Servlet到底有什么区别呢？
  - 职责不同：
    - Servlet的职责是什么：收集数据。（Servlet的强项是逻辑处理，业务处理，然后链接数据库，获取/收集数据。）
    - JSP的职责是什么：展示数据。（JSP的强项是做数据的展示）
  
- JSP的基础语法
  - 在jsp文件中直接编写文字，都会自动被翻译到哪里？
    - 翻译到servlet类的service方法的out.write("翻译到这里")，直接翻译到双引号里，被java程序当做普通字符串打印输出到浏览器。
    - 在JSP中编写的HTML CSS JS代码，这些代码对于JSP来说只是一个普通的字符串。但是JSP把这个普通的字符串一旦输出到浏览器，浏览器就会对HTML CSS JS进行解释执行。展现一个效果。
  - JSP的page指令（这个指令后面再详细说，这里先解决一下中文乱码问题），解决响应时的中文乱码问题：
    - 通过page指令来设置响应的内容类型，在内容类型的最后面添加：charset=UTF-8
      - <%@page contentType="text/html;charset=UTF-8"%>，表示响应的内容类型是text/html，采用的字符集UTF-8
      - <%@page import="java.util.List,java.util.ArrayList"%>
  - 怎么在JSP中编写Java程序：
    - <% java语句; %>
      - 在这个符号当中编写的被视为java程序，被翻译到Servlet类的service方法内部。
      - 这里你要细心点，你要思考，在<% %>这个符号里面写java代码的时候，你要时时刻刻的记住你正在“方法体”当中写代码，方法体中可以写什么，不可以写什么，你心里是否明白呢？
      - 在service方法当中编写的代码是有顺序的，方法体当中的代码要遵循自上而下的顺序依次逐行执行。
      - service方法当中不能写静态代码块，不能写方法，不能定义成员变量。。。。。。
      - 在同一个JSP当中 <%%> 这个符号可以出现多个。
    - <%! %>
      - 在这个符号当中编写的java程序会自动翻译到service方法之外。
      - 这个语法很少用，为什么？不建议使用，因为在service方法外面写静态变量和实例变量，都会存在线程安全问题，因为JSP就是servlet，servlet是单例的，多线程并发的环境下，这个静态变量和实例变量一旦有修改操作，必然会存在线程安全问题。
    - JSP的输出语句
      - 怎么向浏览器上输出一个java变量。
      - <% String name = “jack”;  out.write("name = " + name); %>
      - 注意：以上代码中的out是JSP的九大内置对象之一。可以直接拿来用。当然，必须只能在service方法内部使用。
      - 如果向浏览器上输出的内容中没有“java代码”，例如输出的字符串是一个固定的字符串，可以直接在jsp中编写，不需要写到<%%> 这里。
      - 如果输出的内容中含有“java代码”，这个时候可以使用以下语法格式：
        - <%= %> 注意：在=的后面编写要输出的内容。
        - <%= %> 这个符号会被翻译到哪里？最终翻译成什么？ 
          - 翻译成了这个java代码：   out.print();
          - 翻译到service方法当中了。
        - 什么时候使用<%=%> 输出呢？输出的内容中含有java的变量，输出的内容是一个动态的内容，不是一个死的字符串。如果输出的是一个固定的字符串，直接在JSP文件中编写即可。
  - 在JSP中如何编写JSP的专业注释
    - <%--JSP的专业注释，不会被翻译到java源代码当中。--%>
    - <!--这种注释属于HTML的注释，这个注释信息仍然会被翻译到java源代码当中，不建议。-->
  - JSP基础语法总结：
    - JSP中直接编写普通字符串
      - 翻译到service方法的out.write("这里")
    - <%%>
      - 翻译到service方法体内部，里面是一条一条的java语句。
    - <%! %>
      - 翻译到service方法之外。
    - <%= %>
      - 翻译到service方法体内部，翻译为：out.print();
    - <%@page  contentType="text/html;charset=UTF-8"%>
      - page指令，通过contentType属性用来设置响应的内容类型。
  - 使用Servlet + JSP完成oa项目的改造。
    - 使用Servlet处理业务，收集数据。 使用JSP展示数据。

    - 将之前原型中的html文件，全部修改为jsp，然后在jsp文件头部添加page指令（指定contentType防止中文乱码），将所有的JSP直接拷贝到web目录下。

    - 完成所有页面的正常流转。（页面仍然能够正常的跳转。修改超链接的请求路径。）
      
      - <%=request.getContextPath() %>  在JSP中动态的获取应用的根路径。
      
    - Servlet中连接数据库，查询所有的部门，遍历结果集。
      - 遍历结果集的过程中，取出部门编号、部门名、位置等信息，封装成java对象。
      - 将java对象存放到List集合中。
      - 将List集合存储到request域当中。
      - 转发forward到jsp。
      
    - 在JSP中：
      - 从request域当中取出List集合。
      - 遍历List集合，取出每个部门对象。动态生成tr。
      
    - 思考一个问题：如果我只用JSP这一个技术，能不能开发web应用？

      - 当然可以使用JSP来完成所有的功能。因为JSP就是Servlet，在JSP的<%%>里面写的代码就是在service方法当中的，所以在<%%>当中完全可以编写JDBC代码，连接数据库，查询数据，也可以在这个方法当中编写业务逻辑代码，处理业务，都是可以的，所以使用单独的JSP开发web应用完全没问题。
      - 虽然JSP一个技术就可以完成web应用，但是不建议，还是建议采用servlet + jsp的方式进行开发。这样都能将各自的优点发挥出来。JSP就是做数据展示。Servlet就是做数据的收集。（JSP中编写的Java代码越少越好。）一定要职责分明。

    - JSP文件的扩展名必须是xxx.jsp吗？

      - jsp文件的扩展名是可以配置的。不是固定的。

      - 在CATALINA_HOME/conf/web.xml，在这个文件当中配置jsp文件的扩展名。

      - ```xml
        <servlet-mapping>
            <servlet-name>jsp</servlet-name>
            <url-pattern>*.jsp</url-pattern>
            <url-pattern>*.jspx</url-pattern>
        </servlet-mapping>
        ```

      - xxx.jsp文件对于小猫咪来说，只是一个普通的文本文件，web容器会将xxx.jsp文件最终生成java程序，最终调用的是java对象相关的方法，真正执行的时候，和jsp文件就没有关系了。

      - 小窍门：JSP如果看不懂，建议把jsp翻译成java代码，就能看懂了。

    - 同学问：包名bean是什么意思？

      - javabean（java的logo是一杯冒着热气的咖啡。javabean被翻译为：咖啡豆）
      - java是一杯咖啡，咖啡又是由一粒一粒的咖啡豆研磨而成。
      - 整个java程序中有很多bean的存在。由很多bean组成。
      - 什么是javabean？实际上javabean你可以理解为符合某种规范的java类，比如：
        - 有无参数构造方法
        - 属性私有化
        - 对外提供公开的set和get方法
        - 实现java.io.Serializable接口
        - 重写toString
        - 重写hashCode+equals
        - ....
      - javabean其实就是java中的实体类。负责数据的封装。
      - 由于javabean符合javabean规范，具有更强的通用性。

    - 完成剩下所有功能的改造。
  
- 当前的oa应用存在的问题：

  - 任何一个用户都可以访问这个系统，都可以对这个系统当中的数据进行增删改这些危险的操作。我只想让合法的用户去使用这个系统，不合法的用户不能访问这个系统，怎么办？
    - 加一个登录功能。登录成功的可以访问该系统，登录失败不能访问。
  - 实现登录功能：
    - 步骤1：数据库当中添加一个用户表：t_user
      - t_user表当中存储的是用户的登录信息，最基本的也包括：登录的用户名和登录的密码。
      - 密码一般在数据库表当中存储的是密文。一般不以明文的形式存储。（这里先使用明文方式。）
      - 向t_user表中插入数据。
    - 步骤2：再实现一个登录页面。
      - 登录页面上应该有一个登录的表单。有用户名和密码输入的框。
      - 用户点击登录，提交表单，提交用户名和密码。form是post方式提交。
    - 步骤3：后台要有一个对应的Servlet来处理登录的请求。
      - 登录成功：跳转到部门列表页面。
      - 登录失败：跳转到失败的页面。
    - 步骤4：再提供一个登录失败的页面。

- 登录功能实现了，目前存在的最大的问题：

  - 这个登录功能目前只是一个摆设，没有任何作用。只要用户知道后端的请求路径，照样可以在不登录的情况下访问。
  - 这个登录没有真正起到拦截的作用。怎么解决？
  
- JSP的指令

  - 指令的作用：指导JSP的翻译引擎如何工作（指导当前的JSP翻译引擎如何翻译JSP文件。）

  - 指令包括哪些呢？

    - include指令：包含指令，在JSP中完成静态包含，很少用了。（这里不讲）
    - taglib指令：引入标签库的指令。这个到JJSTL标签库的时候再学习。现在先不管。
    - page指令：目前重点学习一个page指令。

  - 指令的使用语法是什么？

    - <%@指令名  属性名=属性值  属性名=属性值  属性名=属性值....%>

  - 关于page指令当中都有哪些常用的属性呢？

    - ```
      <%@page session="true|false" %>
      true表示启用JSP的内置对象session，表示一定启动session对象。没有session对象会创建。
      如果没有设置，默认值就是session="true"
      session="false" 表示不启动内置对象session。当前JSP页面中无法使用内置对象session。
      ```

    - ```
      <%@page contentType="text/json" %>
      contentType属性用来设置响应的内容类型
      但同时也可以设置字符集。
      <%@page contentType="text/json;charset=UTF-8" %>
      ```

    - ```
      <%@page pageEncoding="UTF-8" %>
      pageEncoding="UTF-8" 表示设置响应时采用的字符集。
      ```

    - ```
      <%@page import="java.util.List, java.util.Date, java.util.ArrayList" %>
      <%@page import="java.util.*" %>
      import语句，导包。
      ```

    - ```
      <%@page errorPage="/error.jsp" %>
      当前页面出现异常之后，跳转到error.jsp页面。
      errorPage属性用来指定出错之后的跳转位置。
      ```

    - ```
      <%@page isErrorPage="true" %>
      表示启用JSP九大内置对象之一：exception
      默认值是false。
      ```

- JSP的九大内置对象

  - jakarta.servlet.jsp.PageContext pageContext       页面作用域
  - jakarta.servlet.http.HttpServletRequest request 请求作用域
  - jakarta.servlet.http.HttpSession session  会话作用域
  - jakarta.servlet.ServletContext application 应用作用域
    - pageContext < request < session < application
    - 以上四个作用域都有：setAttribute、getAttribute、removeAttribute方法。
    - 以上作用域的使用原则：尽可能使用小的域。

  - java.lang.Throwable exception   

  - jakarta.servlet.ServletConfig config

  - java.lang.Object page  （其实是this，当前的servlet对象）

  - jakarta.servlet.jsp.JspWriter out  （负责输出）
  - jakarta.servlet.http.HttpServletResponse response （负责响应）

# EL表达式

- EL表达式是干什么用的？
  - Expression Language（表达式语言）
  - EL表达式可以代替JSP中的java代码，让JSP文件中的程序看起来更加整洁，美观。
  - JSP中夹杂着各种java代码，例如<% java代码 %>、<%=%>等，导致JSP文件很混乱，不好看，不好维护。所以才有了后期的EL表达式。
  - EL表达式可以算是JSP语法的一部分。EL表达式归属于JSP。
  
- EL表达式出现在JSP中主要是：
  - 从某个作用域中取数据，然后将其转换成字符串，然后将其输出到浏览器。这就是EL表达式的功效。三大功效：
    - 第一功效：从某个域中取数据。
      - 四个域：
        - pageContext
        - request
        - session
        - application
    - 第二功效：将取出的数据转成字符串。
      - 如果是一个java对象，也会自动调用java对象的toString方法将其转换成字符串。
    - 第三功效：将字符串输出到浏览器。
      - 和这个一样：<%= %>，将其输出到浏览器。
  
- EL表达式很好用，基本的语法格式：
  - ${表达式}
  
- EL表达式的使用：

  - ```jsp
    <%
    	// 创建User对象
    	User user = new User();
    	user.setUsername("jackson");
    	user.setPassword("1234");
    	user.setAge(50);
    
    	// 将User对象存储到某个域当中。一定要存，因为EL表达式只能从某个范围中取数据。
    	// 数据是必须存储到四大范围之一的。
    	request.setAttribute("userObj", user);
    %>
    
    <%--使用EL表达式取--%>
    ${这个位置写什么？？？？这里写的一定是存储到域对象当中时的name}
    要这样写：
    ${userObj}
    等同于java代码：<%=request.getAttribute("userObj")%>
    你不要这样写：${"userObj"}
    
    面试题：
    	${abc} 和 ${"abc"}的区别是什么？
    		${abc}表示从某个域中取出数据，并且被取的这个数据的name是"abc"，之前一定有这样的代码: 域.setAttribute("abc", 对象);
    		${"abc"} 表示直接将"abc"当做普通字符串输出到浏览器。不会从某个域中取数据了。
    
    ${userObj} 底层是怎么做的？从域中取数据，取出user对象，然后调用user对象的toString方法，转换成字符串，输出到浏览器。
    
    <%--如果想输出对象的属性值，怎么办？--%>
    ${userObj.username} 使用这个语法的前提是：User对象有getUsername()方法。
    ${userObj.password} 使用这个语法的前提是：User对象有getPassword()方法。
    ${userObj.age} 使用这个语法的前提是：User对象有getAge()方法。
    ${userObj.email} 使用这个语法的前提是：User对象有getEmail()方法。
    EL表达式中的. 这个语法，实际上调用了底层的getXxx()方法。
    注意：如果没有对应的get方法，则出现异常。报500错误。
    
    ${userObj.addr222.zipcode}
    以上EL表达式对应的java代码：
    user.getAddr222().getZipcode()
    ```

  - EL表达式优先从小范围中读取数据。

    - pageContext < request < session < application

  - EL表达式中有四个隐含的隐式的范围：

    - pageScope 对应的是 pageContext范围。
    - requestScope 对应的是 request范围。
    - sessionScope 对应的是 session范围。
    - applicationScope 对应的是 application范围。

  - EL表达式对null进行了预处理。如果是null，则向浏览器输出一个空字符串。

  - EL表达式取数据的时候有两种形式：

    - 第一种：.  （大部分使用这种方式）
    - 第二种：[ ] （如果存储到域的时候，这个name中含有特殊字符，可以使用 [ ]）
      - request.setAttribute("abc.def", "zhangsan");
      - ${requestScope.abc.def} 这样是无法取值的。
      - 应该这样：${requestScope["abc.def"]}

  - 掌握使用EL表达式，怎么从Map集合中取数据：

    - ${map.key}

  - 掌握使用EL表达式，怎么从数组和List集合中取数据：

    - ${数组[0]}
    - ${数组[1]}
    - ${list[0]}

  - page指令当中，有一个属性，可以忽略EL表达式

    - ```
      <%@page contentType="text/html;charset=UTF-8" isELIgnored="true" %>
      isELIgnored="true" 表示忽略EL表达式
      isELIgnored="false" 表示不忽略EL表达式。（这是默认值）
      
      isELIgnored="true" 这个是全局的控制。
      
      可以使用反斜杠进行局部控制：\${username} 这样也可以忽略EL表达式。
      ```

  - 通过EL表达式获取应用的根：

    - ${pageContext.request.contextPath}

  - EL表达式中其他的隐式对象：

    - pageContext
    - param
    - paramValues
    - initParam
  
  - EL表达式的运算符
  
    - 算术运算符
      - +、-、*、/、%
    - 关系运算符
      - [ ] == eq != > >= < <= 
    - 逻辑运算符
      - [ ] !  && ||  not and or
    - 条件运算符
      - [ ] ? : 
    - 取值运算符
      - [ ]和.
    - empty运算符
      - [ ] empty运算符的结果是boolean类型
      - [ ] ${empty param.username}
      - [ ] ${not empty param.username}
      - [ ] ${!empty param.password}

# JSTL标签库

- 什么是JSTL标签库？

  - Java Standard Tag Lib（Java标准的标签库）
  - JSTL标签库通常结合EL表达式一起使用。目的是让JSP中的java代码消失。
  - 标签是写在JSP当中的，但实际上最终还是要执行对应的java程序。（java程序在jar包当中。）

- 使用JSTL标签库的步骤：

  - 第一步：引入JSTL标签库对应的jar包。

    - tomcat10之后引入的jar包是：
      - jakarta.servlet.jsp.jstl-2.0.0.jar
      - jakarta.servlet.jsp.jstl-api-2.0.0.jar
    - 在IDEA当中怎么引入？
      - 在WEB-INF下新建lib目录，然后将jar包拷贝到lib当中。然后将其“Add Lib...”
      - 一定是要和mysql的数据库驱动一样，都是放在WEB-INF/lib目录下的。
      - 什么时候需要将jar包放到WEB-INF/lib目录下？如果这个jar是tomcat服务器没有的。
    
  - 第二步：在JSP中引入要使用标签库。（使用taglib指令引入标签库。）
  
    - JSTL提供了很多种标签，你要引入哪个标签？？？？重点掌握核心标签库。
  
    - ```
      <%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
      这个就是核心标签库。
      prefix="这里随便起一个名字就行了，核心标签库，大家默认的叫做c，你随意。"
      ```
  
  - 第三步：在需要使用标签的位置使用即可。表面使用的是标签，底层实际上还是java程序。
  
- JSTL标签的原理

  - ```
    <%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
    以上uri后面的路径实际上指向了一个xxx.tld文件。
    tld文件实际上是一个xml配置文件。
    在tld文件中描述了“标签”和“java类”之间的关系。
    以上核心标签库对应的tld文件是：c.tld文件。它在哪里。
    在jakarta.servlet.jsp.jstl-2.0.0.jar里面META-INF目录下，有一个c.tld文件。
    ```

  - 源码解析：配置文件tld解析

    - ```
      <tag>
          <description>对该标签的描述</description>
          <name>catch</name> 标签的名字
          <tag-class>org.apache.taglibs.standard.tag.common.core.CatchTag</tag-class> 标签对应的java类。
          <body-content>JSP</body-content> 标签体当中可以出现的内容，如果是JSP，就表示标签体中可以出现符合JSP所有语法的代码。例如EL表达式。
          <attribute>
              <description>
              	对这个属性的描述
              </description>
              <name>var</name> 属性名
              <required>false</required> false表示该属性不是必须的。true表示该属性是必须的。
              <rtexprvalue>false</rtexprvalue> 这个描述说明了该属性是否支持EL表达式。false表示不支持。true表示支持EL表达式。
          </attribute>
        </tag>
      
      <c:catch var="">
      	JSP....
      </c:catch>
      ```
    
  - jstl中的核心标签库core当中有哪些常用的标签呢？
  
    - c:if
  
      - <c:if test="boolean类型，支持EL表达式"></c: if>
  
    - c:forEach
  
      - <c:forEach items="集合，支持EL表达式" var="集合中的元素" varStatus="元素状态对象"> ${元素状态对象.count} </c: forEach>
      - <c:forEach var="i" begin="1" end="10" step="2"> ${i} </c: forEach>
  
    - c:choose c:when c:otherwise
  
      - ```
        <c:choose>
            <c:when test="${param.age < 18}">
                青少年
            </c:when>
            <c:when test="${param.age < 35}">
                青年
            </c:when>
            <c:when test="${param.age < 55}">
                中年
            </c:when>
            <c:otherwise>
                老年
            </c:otherwise>
        </c:choose>
        ```

## 改造OA

- 使用什么技术改造呢？

  - Servlet + JSP + EL表达式 + JSTL标签。进行改造。

- 在前端HTML代码中，有一个标签，叫做base标签，这个标签可以设置整个网页的基础路径。

  - 这是Java的语法，也不是JSP的语法。是HTML中的一个语法。HTML中的一个标签。通常出现在head标签中。

  - < base href="http://localhost:8080/oa/">

  - 在当前页面中，凡是路径没有以“/”开始的，都会自动将base中的路径添加到这些路径之前。

    - < a href="ab/def"></ a>
    - 等同于：< a href="http://localhost:8080/oa/ab/def"></ a>

  - 需要注意：在JS代码中的路径，保险起见，最好不要依赖base标签。JS代码中的路径最好写上全路径。

  - ```
    <base href="${pageContext.request.scheme}://${pageContext.request.serverName}:${pageContext.request.serverPort}${pageContext.request.contextPath}/">
    ```

# Filter过滤器

- 当前的OA项目存在什么缺陷？
  - DeptServlet、EmpServlet、OrderServlet。每一个Servlet都是处理自己相关的业务。在这些Servlet执行之前都是需要判断用户是否登录了。如果用户登录了，可以继续操作，如果没有登录，需要用户登录。这段判断用户是否登录的代码是固定的，并且在每一个Servlet类当中都需要编写，显然代码没有得到重复利用。包括每一个Servlet都要解决中文乱码问题，也有公共的代码。这些代码目前都是重复编写，并没有达到复用。怎么解决这个问题?
    - 可以使用Servlet规范中的Filter过滤器来解决这个问题。
  
- Filter是什么，有什么用，执行原理是什么？
  - Filter是过滤器。
  - Filter可以在Servlet这个目标程序执行之前添加代码。也可以在目标Servlet执行之后添加代码。之前之后都可以添加过滤规则。
  - 一般情况下，都是在过滤器当中编写公共代码。
  
- 一个过滤器怎么写呢？

  - 第一步：编写一个Java类实现一个接口：jarkata.servlet.Filter。并且实现这个接口当中所有的方法。

    - init方法：在Filter对象第一次被创建之后调用，并且只调用一次。
    - doFilter方法：只要用户发送一次请求，则执行一次。发送N次请求，则执行N次。在这个方法中编写过滤规则。
    - destroy方法：在Filter对象被释放/销毁之前调用，并且只调用一次。

  - 第二步：在web.xml文件中对Filter进行配置。这个配置和Servlet很像。

    - ```
      <filter>
          <filter-name>filter2</filter-name>
          <filter-class>com.bjpowernode.javaweb.servlet.Filter2</filter-class>
      </filter>
      <filter-mapping>
          <filter-name>filter2</filter-name>
          <url-pattern>*.do</url-pattern>
      </filter-mapping>
      ```

    - 或者使用注解：@WebFilter({"*.do"})

- 注意：

  - Servlet对象默认情况下，在服务器启动的时候是不会新建对象的。
  - Filter对象默认情况下，在服务器启动的时候会新建对象。
  - Servlet是单例的。Filter也是单例的。（单实例。）

- 目标Servlet是否执行，取决于两个条件：

  - 第一：在过滤器当中是否编写了：chain.doFilter(request, response); 代码。
  - 第二：用户发送的请求路径是否和Servlet的请求路径一致。

- chain.doFilter(request, response); 这行代码的作用：

  - 执行下一个过滤器，如果下面没有过滤器了，执行最终的Servlet。

- 注意：Filter的优先级，天生的就比Servlet优先级高。

  - /a.do 对应一个Filter，也对应一个Servlet。那么一定是先执行Filter，然后再执行Servlet。

- 关于Filter的配置路径：

  - /a.do、/b.do、/dept/save。这些配置方式都是精确匹配。
  - /* 匹配所有路径。
  - *.do 后缀匹配。不要以 / 开始
  - /dept/*  前缀匹配。

- 在web.xml文件中进行配置的时候，Filter的执行顺序是什么？

  - 依靠filter-mapping标签的配置位置，越靠上优先级越高。

- 过滤器的调用顺序，遵循栈数据结构。

- 使用@WebFilter的时候，Filter的执行顺序是怎样的呢？

  - 执行顺序是：比较Filter这个类名。
  - 比如：FilterA和FilterB，则先执行FilterA。
  - 比如：Filter1和Filter2，则先执行Filter1.

- Filter的生命周期？

  - 和Servlet对象生命周期一致。
  - 唯一的区别：Filter默认情况下，在服务器启动阶段就实例化。Servlet不会。

- Filter过滤器这里有一个设计模式：

  - 责任链设计模式。
  - 过滤器最大的优点：
    - 在程序编译阶段不会确定调用顺序。因为Filter的调用顺序是配置到web.xml文件中的，只要修改web.xml配置文件中filter-mapping的顺序就可以调整Filter的执行顺序。显然Filter的执行顺序是在程序运行阶段动态组合的。那么这种设计模式被称为责任链设计模式。
  - 责任链设计模式最大的核心思想：
    - 在程序运行阶段，动态的组合程序的调用顺序。
  
- 使用过滤器改造OA项目。

# Listener监听器

- 什么是监听器？

  - 监听器是Servlet规范中的一员。就像Filter一样。Filter也是Servlet规范中的一员。
  - 在Servlet中，所有的监听器接口都是以“Listener”结尾。

- 监听器有什么用？

  - 监听器实际上是Servlet规范留给我们javaweb程序员的特殊时机。
  - 特殊的时刻如果想执行这段代码，你需要想到使用对应的监听器。

- Servlet规范中提供了哪些监听器？

  - jakarta.servlet包下：
    - ServletContextListener
    - ServletContextAttributeListener
    - ServletRequestListener
    - ServletRequestAttributeListener
  - jakarta.servlet.http包下：
    - HttpSessionListener
    - HttpSessionAttributeListener
      - 该监听器需要使用@WebListener注解进行标注。
      - 该监听器监听的是什么？是session域中数据的变化。只要数据变化，则执行相应的方法。主要监测点在session域对象上。
    - HttpSessionBindingListener
      - 该监听器不需要使用@WebListener进行标注。
      - 假设User类实现了该监听器，那么User对象在被放入session的时候触发bind事件，User对象从session中删除的时候，触发unbind事件。
      - 假设Customer类没有实现该监听器，那么Customer对象放入session或者从session删除的时候，不会触发bind和unbind事件。
    - HttpSessionIdListener
      - session的id发生改变的时候，监听器中的唯一一个方法就会被调用。
    - HttpSessionActivationListener
      - 监听session对象的钝化和活化的。
      - 钝化：session对象从内存存储到硬盘文件。
      - 活化：从硬盘文件把session恢复到内存。

- 实现一个监听器的步骤：以ServletContextListener为例。

  - 第一步：编写一个类实现ServletContextListener接口。并且实现里面的方法。

    - ```
      void contextInitialized(ServletContextEvent event)
      void contextDestroyed(ServletContextEvent event)
      ```

  - 第二步：在web.xml文件中对ServletContextListener进行配置，如下：

    - ```
      <listener>
          <listener-class>com.bjpowernode.javaweb.listener.MyServletContextListener</listener-class>
      </listener>
      ```

    - 当然，第二步也可以不使用配置文件，也可以用注解，例如：@WebListener
  
- 注意：所有监听器中的方法都是不需要javaweb程序员调用的，由服务器来负责调用？什么时候被调用呢？

  - 当某个特殊的事件发生（特殊的事件发生其实就是某个时机到了。）之后，被web服务器自动调用。
  
- 思考一个业务场景：

  - 请编写一个功能，记录该网站实时的在线用户的个数。
  - 我们可以通过服务器端有没有分配session对象，因为一个session代表了一个用户。有一个session就代表有一个用户。如果你采用这种逻辑去实现的话，session有多少个，在线用户就有多少个。这种方式的话：HttpSessionListener够用了。session对象只要新建，则count++，然后将count存储到ServletContext域当中，在页面展示在线人数即可。
  - 业务发生改变了，只统计登录的用户的在线数量，这个该怎么办？
    - session.setAttribute("user", userObj); 
    - 用户登录的标志是什么？session中曾经存储过User类型的对象。那么这个时候可以让User类型的对象实现HttpSessionBindingListener监听器，只要User类型对象存储到session域中，则count++，然后将count++存储到ServletContext对象中。页面展示在线人数即可。

- 实现oa项目中当前登录在线的人数。

  - 什么代表着用户登录了？
    - session.setAttribute("user", userObj); User类型的对象只要往session中存储过，表示有新用户登录。
  - 什么代表着用户退出了？
    - session.removeAttribute("user"); User类型的对象从session域中移除了。
    - 或者有可能是session销毁了。（session超时）
