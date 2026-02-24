# Web基础知识

## HTTP协议

1. 不需要手动去解析HTTP协议，SpringBoot已经帮我们解析好了
2. HttpServletRequest类可以获取请求信息，包括请求方式、请求路径、请求协议、请求参数、请求头等，内容。

```java
package com.charles.server;  
  
import jakarta.servlet.http.HttpServletRequest;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.bind.annotation.RestController;  
  
@RestController  
public class RequestController {  
    @RequestMapping("/request")  
    public String request(HttpServletRequest request) {  
        // 1. 获取请求方式  
        System.out.println("请求方式: "+request.getMethod());  
  
        // 2. 获取请求路径  
        System.out.println("URL: "+request.getRequestURL());  
        System.out.println("URI: "+request.getRequestURI());  
  
        // 3. 获取请求协议  
        System.out.println("协议: "+request.getProtocol());  
  
        // 4. 获取请求参数  
        System.out.println("请求参数name: "+request.getParameter("name"));  
        System.out.println("请求参数age: "+request.getParameter("age"));  
  
        // 5. 获取请求头  
        System.out.println("请求头Accept: "+request.getHeader("Accept"));  
  
        return "OK";  
  
        // http://localhost:8081/request?name=charles&age=18  
  
        // 请求方式: GET  
        // URL: http://localhost:8081/request        
        // URI: /request        
        // 协议: HTTP/1.1  
        // 请求参数name: charles  
        // 请求参数age: 18  
        // 请求头Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7  
    }  
}
```

状态码举例

1. 1xx：信息性状态码，表示请求已被接受，需要继续处理
2. 2xx：成功状态码，表示请求已成功被服务器接收、理解、并接受
   1. 200 OK：请求成功
3. 3xx：重定向状态码，表示需要进行附加操作以完成请求
   1. 307：临时重定向，请求的资源临时从不同的URI响应请求（比如http://www.baidu.com会被重定向到https://www.baidu.com）
4. 4xx：客户端错误状态码，表示请求包含语法错误或无法实现
5. 5xx：服务器错误状态码，表示服务器在处理请求的过程中发生了错误

HttpServletResponse类可以设置响应信息，包括响应状态码、响应头、响应体等内容。


## SpringBoot Web案例

## 分层解耦

我们的需求是服务器本地保存了用户的信息，现在客户端发送一个用户id，我们返回对应的名字

(/Users/kimshan/Public/project/webasic/demo01/src/main/resources/user.txt)
```txt
1,Tom,111  
2,Jerry,222
```

并创建用户信息的类

* lombok 是一个工具库，可以帮助我们简化Java代码，提高开发效率。
* @Data 注解会为类的所有属性自动生成 getter、setter、equals、hashCode 和 toString 方法，以简化JavaBean的编写。
* @NoArgsConstructor 注解会生成一个无参构造函数，以方便在反序列化时使用。
* @AllArgsConstructor 注解会生成一个包含所有属性的构造函数，以方便在创建对象时使用。

```java
// /Users/kimshan/Public/project/webasic/demo01/src/main/java/com/charles/demo01/entity/User.java
package com.charles.demo01.entity;  
  
import lombok.AllArgsConstructor;  
import lombok.Data;  
import lombok.NoArgsConstructor;  
  
@Data  
@NoArgsConstructor  
@AllArgsConstructor  
public class User {  
    private Integer id;  
    private String name;  
    private String password;  
}
```

我们可以创造一个Controller来实现。我们使用了 hutool 进行文件的读取，简化了流程。

```java
// /Users/kimshan/Public/project/webasic/demo01/src/main/java/com/charles/demo01/controller/UserController.java
package com.charles.demo01.controller;  
  
import cn.hutool.core.io.IoUtil;  
import com.charles.demo01.entity.User;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.bind.annotation.RestController;  
  
import java.io.InputStream;  
import java.util.ArrayList;  
import java.util.List;  
  
@RestController  
public class UserController {  
    @RequestMapping("/user")  
    public String user(Integer user_id) {  
        // 读取文件  
        InputStream inputStream = getClass().getResourceAsStream("/user.txt");  
        ArrayList<String> lines = IoUtil.readLines(inputStream, "utf-8", new ArrayList<>());  
        // for (int i = 0; i < lines.size(); i++) {  
        //     System.out.println(lines.get(i));        
        // }        
        // 1,Tom,111        
        // 2,Jerry,222  
        
        // 解析文件  
        List<User> users = lines.stream().map(line -> {  
            String[] strings = line.split(",");  
            Integer id = Integer.parseInt(strings[0]);  
            String name = strings[1];  
            String password = strings[2];  
            return new User(id, name, password);  
        }).toList(); // >= JDK 16  
        // for (int i = 0; i < users.size(); i++) {        
        //      System.out.println(users.get(i));        
        // }        
        // User(id=1, name=Tom, password=111)        
        // User(id=2, name=Jerry, password=222)  
        
        // 返回指定信息  
        for (User user : users) {  
            if (user.getId().equals(user_id)) {  
                return user.getName();  
            }        }  
        return "";  
    }}
```

可以发现这样的写法各种功能部分混在了一起，这就要引出「分层解耦」了。

* Controller：处理请求和响应
* Service：处理业务逻辑
* Repository：处理数据访问

我们将UserController中的「功能部分」拆分到UserService中。

```java
// /Users/kimshan/Public/project/webasic/demo01/src/main/java/com/charles/demo01/service/UserService.java
package com.charles.demo01.service;

import com.charles.demo01.entity.User;
import java.util.List;

public interface UserService {
    public List<User> getAllUsers();
}

```

```java
// /Users/kimshan/Public/project/webasic/demo01/src/main/java/com/charles/demo01/service/impl/UserServiceImpl.java

package com.charles.demo01.service.impl;
import com.charles.demo01.dao.UserDao;
import com.charles.demo01.dao.impl.UserDaoImpl;
import com.charles.demo01.entity.User;
import com.charles.demo01.service.UserService;

import java.util.List;

public class UserServiceImpl implements UserService{

    private final UserDaoImpl userDaoImpl = new UserDaoImpl();
    public List<User> getAllUsers()
    {
        List<String> lines = userDaoImpl.getAllUsers();
        List<User> users = lines.stream().map(line -> {
            String[] strings = line.split(",");
            Integer id = Integer.parseInt(strings[0]);
            String name = strings[1];
            String password = strings[2];
            return new User(id, name, password);
        }).toList(); // >= JDK 16
        return users;
    }
}

```

把数据访问相关内容放到dao层中。

```java
// /Users/kimshan/Public/project/webasic/demo01/src/main/java/com/charles/demo01/dao/UserDao.java
package com.charles.demo01.dao;  
  
import java.util.List;  
  
public interface UserDao {  
    public List<String> getAllUsers();  
}
```

```java
// /Users/kimshan/Public/project/webasic/demo01/src/main/java/com/charles/demo01/dao/impl/UserDaoImpl.java
package com.charles.demo01.dao.impl;  
import cn.hutool.core.io.IoUtil;  
import com.charles.demo01.dao.UserDao;  
  
import java.util.ArrayList;  
import java.util.List;  
import java.io.InputStream;  
  
public class UserDaoImpl implements UserDao {  
    public List<String> getAllUsers()  
    {        InputStream inputStream = getClass().getResourceAsStream("/user.txt");  
        return IoUtil.readLines(inputStream, "utf-8", new ArrayList<>());  
    }
}
```

Controller只剩下下面内容

```java
package com.charles.demo01.controller;  
  
import com.charles.demo01.service.impl.UserServiceImpl;  
import com.charles.demo01.entity.User;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.bind.annotation.RestController;  
  
import java.util.List;  
  
@RestController  
public class UserController {  
    @RequestMapping("/getAllUsers")  
    public List<User> getAllUsers(Integer user_id) {  
        return new UserServiceImpl().getAllUsers();  
    }
}
```

我们可以发现，这样的写法，Controller和Service之间的耦合度降低了，Controller只负责处理请求和响应，Service只负责处理业务逻辑。

访问 http://localhost:8080/getAllUsers 得到

```json
[
  {
    "id": 1,
    "name": "Tom",
    "password": "111"
  },
  {
    "id": 2,
    "name": "Jerry",
    "password": "222"
  }
]
```

## IOC与DI

* 耦合：指程序模块之间的依赖关系
* 内聚：指模块内部的功能是否单一
* IOC：Inversion of Control，控制反转，是一种设计思想，它的核心是将对象的创建和管理交给框架来完成，而不是由应用程序来创建和管理。
* DI：Dependency Injection，依赖注入，是一种设计模式，它的核心是将对象的依赖关系交给框架来完成，而不是由应用程序来创建和管理。
* Bean对象：是一个Java对象，它可以被Spring容器管理。
* `@Component` 注解：是一个Spring注解，它可以将一个类声明为一个Bean对象。
* `@Autowired` 注解：是一个Spring注解，它可以将一个Bean对象注入到另一个Bean对象中。


下边增加上IOC和DI

```java
// UserDaoImpl.java
package com.charles.demo01.dao.impl;  
import cn.hutool.core.io.IoUtil;  
import com.charles.demo01.dao.UserDao;  
import org.springframework.stereotype.Component;  
  
import java.util.ArrayList;  
import java.util.List;  
import java.io.InputStream;  
  
@Component  
public class UserDaoImpl implements UserDao {  
    public List<String> getAllUsers()  
    {        
	    InputStream inputStream = getClass().getResourceAsStream("/user.txt");  
        return IoUtil.readLines(inputStream, "utf-8", new ArrayList<>());  
    }
}
```

```java
// UserServiceImpl.java
package com.charles.demo01.service.impl;  
import com.charles.demo01.dao.UserDao;  
import com.charles.demo01.entity.User;  
import com.charles.demo01.service.UserService;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.stereotype.Component;  
  
import java.util.List;  
  
@Component  
public class UserServiceImpl implements UserService{  
  
    @Autowired  
    private UserDao userDao;  
    @Override  
    public List<User> getAllUsers()  
    {  
        List<String> lines = userDao.getAllUsers();  
        List<User> users = lines.stream().map(line -> {  
            String[] strings = line.split(",");  
            Integer id = Integer.parseInt(strings[0]);  
            String name = strings[1];  
            String password = strings[2];  
            return new User(id, name, password);  
        }).toList(); // >= JDK 16  
        return users;  
    }
}
```

```java
// UserController.java
package com.charles.demo01.controller;  
  
import com.charles.demo01.service.UserService;  
import com.charles.demo01.entity.User;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.bind.annotation.RestController;  
  
import java.util.List;  
  
@RestController  
public class UserController {  
    @Autowired  
    private UserService userService;  
    @RequestMapping("/getAllUsers")  
    public List<User> getAllUsers(Integer user_id) {  
        return userService.getAllUsers();  
    }
}
```

### IOC 详解

* `@Component` 注解：是一个Spring注解，它可以将一个类声明为一个Bean对象。
* `@Controller` 注解：是一个`@Component`注解的子类，主要用于控制层。
* `@Service` 注解：是一个`@Component`注解的子类，主要用于业务层。
* `@Repository` 注解：是一个`@Component`注解的子类，主要用于数据访问层。(由于和MyBatics等框架的整合，一般不使用该注解)

```java
// Controller
package com.charles.demo01.controller;  
  
import com.charles.demo01.entity.User;  
import com.charles.demo01.service.UserService;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.web.bind.annotation.RequestMapping;  
import org.springframework.web.bind.annotation.RestController;  
  
import java.util.List;  
  
@RestController  
public class UserController {  
    @Autowired  
    private UserService userService;  
    @RequestMapping("/getAllUsers")  
    public List<User> getAllUsers(Integer user_id) {  
        return userService.getAllUsers();  
    }
}
```

```java
// Service
package com.charles.demo01.service.impl;  
import com.charles.demo01.dao.UserDao;  
import com.charles.demo01.entity.User;  
import com.charles.demo01.service.UserService;  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.stereotype.Service;  
  
import java.util.List;  
  
@Service  
public class UserServiceImpl implements UserService{  
  
    @Autowired  
    private UserDao userDao;  
    @Override  
    public List<User> getAllUsers()  
    {  
        List<String> lines = userDao.getAllUsers();  
        List<User> users = lines.stream().map(line -> {  
            String[] strings = line.split(",");  
            Integer id = Integer.parseInt(strings[0]);  
            String name = strings[1];  
            String password = strings[2];  
            return new User(id, name, password);  
        }).toList(); // >= JDK 16  
        return users;  
    }
}
```

```java
// Repository
package com.charles.demo01.dao.impl;  
import cn.hutool.core.io.IoUtil;  
import com.charles.demo01.dao.UserDao;  
import org.springframework.stereotype.Repository;  
  
import java.util.ArrayList;  
import java.util.List;  
import java.io.InputStream;  
  
@Repository  
public class UserDaoImpl implements UserDao {  
    public List<String> getAllUsers()  
    {        InputStream inputStream = getClass().getResourceAsStream("/user.txt");  
        return IoUtil.readLines(inputStream, "utf-8", new ArrayList<>());  
    }
}
```

`ComponentScan` 注解：是一个Spring注解，它可以指定一个包下的所有类声明为Bean对象。默认是扫描`@SpringBootApplication`所在包及其子包下的所有类。

## DI 详解

`@Autowired` 属性注入：是一个Spring注解，它可以将一个Bean对象注入到另一个Bean对象中。

```java
public class UserController {
    @Autowired
    private UserService userService;
    // ...
}
```

`@Autowired` 构造器注入：是一个Spring注解，它可以将一个Bean对象注入到另一个Bean对象的构造器中。
```java
public class UserController {
    private final UserService userService; // 必须是final的
    @Autowired
    public UserController(UserService userService) {
        this.userService = userService;
    }
    //...
}
```

`@Autowired` setter注入：是一个Spring注解，它可以将一个Bean对象注入到另一个Bean对象的setter方法中。
```java
public class UserController {
    private UserService userService;
    @Autowired
    public void setUserService(UserService userService) {
        this.userService = userService;
    }
    //...
}   
```

如果一个类只有一个构造器，那么可以省略`@Autowired`注解。

如果一个类有两个实现类，有三种方法：

1. 使用`@Qualifier`注解指定实现类的名称。
2. 使用`@Primary`注解指定默认实现类。
3. 使用`@Resource`注解指定实现类的名称。

