# 软件架构模式

---

## 三层架构模式

三层架构是一种常见的软件架构模式。它将应用程序划分为三个逻辑层次，每层有明确的职责：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749727730298-3fbf26a7-40a4-4ee2-bd8b-6ed01adec552.png)

### 表示层(Presentation Layer)

+ **职责**：处理用户界面和用户交互
+ **在Servlet中的实现**：Servlet本身（处理HTTP请求和响应）、Thymeleaf 页面（视图展示）
+ **主要任务**：接收用户请求、调用业务逻辑层处理、返回适当的响应（HTML、JSON等）

### 业务层(Business Logic Layer)

+ **职责**：包含应用程序的核心业务规则和逻辑
+ **在Servlet中的实现**：独立的Java类（通常称为Service）
+ **主要任务**：处理业务规则、验证数据、协调数据访问层操作、事务管理

### 持久层/数据访问层(Data Access Layer)

+ **职责**：与数据源交互（数据库、文件等）
+ **在Servlet中的实现**：DAO(Data Access Object)类、可能使用JDBC或ORM框架
+ **主要任务**：执行CRUD操作、封装数据访问细节、提供数据持久化功能

### 三层架构优点

1. **解耦**：各层职责明确，修改一层不影响其他层
2. **可维护性**：代码组织清晰，易于维护
3. **可测试性**：各层可以独立测试
4. **可扩展性**：可以单独扩展某一层

### 三层架构包名规范

#### 使用三层架构后建议的包名
以 `dept`项目为例，使用三层架构后建议的包名结构如下：

```plain
com.jkweilai.dept
├── common/                                                            （基础层）
│   ├── util/           # 工具类
│   ├── constant/       # 常量类
│   └── exception/      # 异常类
├── controller/         # Servlet控制器 （表示层）
├── service/            # 业务接口      （业务层）
├── service/impl/       # 业务实现
├── dao/                # 数据访问接口  （持久层）
├── dao/impl/           # JDBC实现
├── entity/             # 数据库实体（等同PO）（数据模型）
├── dto/                # 数据传输对象       （数据模型）
└── vo/                 # 视图对象           （数据模型）
```

#### POJO/JavaBean/PO/Entity/DTO/VO/DAO
1. **POJO (Plain Old Java Object)**  
普通的Java对象，不依赖任何框架，只有属性和getter/setter。  
2. **JavaBean**  
符合特定规范的POJO（可序列化实现 Serializable 接口、有无参构造、以及 setter/getter方法）。  
3. **PO (Persistent Object)**  
与数据库表严格对应的对象，仅用于数据存储，无业务逻辑。  
4. **Entity (领域实体)**  
代表业务领域的对象，可能包含业务逻辑，通常与数据库表映射。  
5. **DTO (Data Transfer Object)**  
用于跨层/跨系统数据传输的对象，仅承载数据，无行为。  例如前端传入的参数对象。
6. **VO (View Object)**  
为前端展示定制的对象，可能组合多个实体的数据（如格式化日期）。  
7. **DAO (Data Access Object)**  
抽象数据库操作接口（如`UserDao.save()`），隔离业务层与持久层。

****

**口诀**：  

+ **POJO/JavaBean**是基础  
+ **PO/Entity**管存储（PO纯数据，Entity可带逻辑）  
+ **DTO/VO**管传输（DTO跨层，VO对前端）  
+ **DAO**管数据库

---

## 银行账户转账功能实现

1. 使用三层架构实现 JavaWeb 项目。
2. 后端技术采用：Servlett + JDBC + Thymeleaf。
3. 需要保证转账时事务的安全（同时成功或同时失败）。
4. 这个项目中涉及到开发中日志代码的编写。
5. 这个项目中涉及到全局异常的处理。

### 数据库表和数据的准备

```sql
drop table if exists t_act;

create table t_act(
  id int primary key auto_increment,
  act_no varchar(255),
  balance decimal(10,1)
);

insert into t_act(act_no,balance) values('6222021234567890123', 50000.0);
insert into t_act(act_no,balance) values('6222021234567890124', 0.0);

drop table if exists t_tran;

CREATE TABLE t_tran (
  id INT PRIMARY KEY AUTO_INCREMENT,
  from_act_no VARCHAR(255) NOT NULL COMMENT '转出账号',
  to_act_no VARCHAR(255) NOT NULL COMMENT '转入账号',
  amount DECIMAL(10,1) NOT NULL COMMENT '转账金额',
  tran_time DATETIME NOT NULL COMMENT '交易时间',
  tran_no VARCHAR(32) NOT NULL COMMENT '交易号',
  INDEX idx_from_act_no (from_act_no),
  INDEX idx_to_act_no (to_act_no),
  INDEX idx_transaction_time (tran_time),
  INDEX idx_transaction_no (tran_no)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='交易记录表';

INSERT INTO t_tran(from_act_no, to_act_no, amount, tran_time, tran_no) VALUES ('6222021234567890123', '6222021234567890124', 1000.0, '2023-11-15 14:30:25', '20231115143025876543');

commit;
select * from t_act;
select * from t_tran;
```

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749784541016-ede604cb-55e0-4f99-91e5-32348f433dbb.png)

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749784579080-9a5840d0-832b-4e40-acb1-0f76ccea624b.png)

### DeepSeek 生成前端页面

#### 转账页面

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>银行账户转账</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f5f7fa;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 500px;
            padding: 30px;
        }

        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
            font-size: 24px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            color: #34495e;
            font-weight: 600;
        }

        input {
            width: 100%;
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 16px;
            transition: border-color 0.3s;
        }

        input:focus {
            border-color: #3498db;
            outline: none;
            box-shadow: 0 0 0 2px rgba(52, 152, 219, 0.2);
        }

        button {
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 14px;
            width: 100%;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: background-color 0.3s;
            margin-top: 10px;
        }

        button:hover {
            background-color: #2980b9;
        }

        .result {
            margin-top: 20px;
            padding: 15px;
            border-radius: 6px;
            display: none;
        }

        .success {
            background-color: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }

        .error {
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }

        .hint {
            font-size: 12px;
            color: #7f8c8d;
            margin-top: 5px;
        }
    </style>
</head>
<body>
<div class="container">
    <h1>银行账户转账</h1>

    <form id="transferForm" method="post">
        <div class="form-group">
            <label for="fromAccount">转出账户</label>
            <input type="text" id="fromAccount" placeholder="请输入转出账户号码" required>
            <div class="hint">例如：6222021234567890123</div>
        </div>

        <div class="form-group">
            <label for="toAccount">转入账户</label>
            <input type="text" id="toAccount" placeholder="请输入转入账户号码" required>
            <div class="hint">例如：6228481234567890123</div>
        </div>

        <div class="form-group">
            <label for="amount">转账金额 (元)</label>
            <input type="number" id="amount" min="0.01" step="0.01" placeholder="请输入转账金额" required>
        </div>

        <button id="transferBtn">确认转账</button>
    </form>

    <div id="resultMessage" class="result"></div>
</div>

<script>
    document.getElementById('transferBtn').addEventListener('click', function(e) {
        e.preventDefault();
        const fromAccount = document.getElementById('fromAccount').value.trim();
        const toAccount = document.getElementById('toAccount').value.trim();
        const amount = parseFloat(document.getElementById('amount').value);

        // 简单验证
        if (!fromAccount || !toAccount || isNaN(amount) || amount <= 0) {
            showResult('请填写完整的转账信息，且金额必须大于0', false);
            return;
        }

        // 验证账户格式（简单验证是否为数字）
        if (!/^\d+$/.test(fromAccount) || !/^\d+$/.test(toAccount)) {
            showResult('账户号码必须为数字', false);
            return;
        }

        // 账户长度验证（通常银行账号16-19位）
        if (fromAccount.length < 16 || fromAccount.length > 19 ||
            toAccount.length < 16 || toAccount.length > 19) {
            showResult('账户号码长度应在16-19位之间', false);
            return;
        }

        if (fromAccount === toAccount) {
            showResult('转出账户和转入账户不能相同', false);
            return;
        }

        // 提交表单
        document.getElementById("transferForm").submit();
    });

    function showResult(message, isSuccess) {
        const resultMessage = document.getElementById('resultMessage');
        resultMessage.textContent = message;
        resultMessage.className = 'result ' + (isSuccess ? 'success' : 'error');
        resultMessage.style.display = 'block';
        // 5秒后自动隐藏消息
        setTimeout(() => {
            resultMessage.style.display = 'none';
        }, 5000);
    }
</script>
</body>
</html>
```

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749783989569-ad3bf2f5-40df-464e-83d9-d586d28d6872.png)

#### 转账成功页面

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>转账结果</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Arial', sans-serif;
        }
        
        body {
            background-color: #f5f7fa;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 500px;
            padding: 30px;
            text-align: center;
        }
        
        h1 {
            color: #2c3e50;
            margin-bottom: 30px;
            font-size: 24px;
        }
        
        .status-icon {
            font-size: 60px;
            margin-bottom: 20px;
            color: #2ecc71;
        }
        
        .detail-card {
            background-color: #f8f9fa;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 15px;
            text-align: left;
        }
        
        .detail-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 12px;
            padding-bottom: 12px;
            border-bottom: 1px solid #eee;
        }
        
        .detail-row:last-child {
            border-bottom: none;
            margin-bottom: 0;
            padding-bottom: 0;
        }
        
        .detail-label {
            color: #7f8c8d;
            font-weight: 500;
        }
        
        .detail-value {
            color: #2c3e50;
            font-weight: 600;
        }
        
        .amount {
            font-size: 24px;
            color: #e74c3c;
            font-weight: 700;
        }
        
        .transaction-number {
            color: #7f8c8d;
            font-size: 14px;
            margin-bottom: 25px;
        }
        
        .continue-btn {
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 12px 25px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            width: 100%;
            transition: background-color 0.3s;
        }
        
        .continue-btn:hover {
            background-color: #2980b9;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="status-icon">✓</div>
        <h1>转账成功</h1>
        
        <div class="detail-card">
            <div class="detail-row">
                <span class="detail-label">转出账户</span>
                <span class="detail-value">****9012</span>
            </div>
            <div class="detail-row">
                <span class="detail-label">转入账户</span>
                <span class="detail-value">****2333</span>
            </div>
            <div class="detail-row">
                <span class="detail-label">转账金额</span>
                <span class="detail-value amount">￥1,500.00</span>
            </div>
            <div class="detail-row">
                <span class="detail-label">转账时间</span>
                <span class="detail-value">2030-11-15 14:30:25</span>
            </div>
        </div>
        
        <div class="transaction-number">交易流水号：20231115143025876543</div>
        <button class="continue-btn">继续转账</button>
    </div>
</body>
</html>
```

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749784155028-338b8c19-eb43-44e3-92bb-d191969038ee.png)

#### 转账失败页面

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>转账失败</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Arial', sans-serif;
        }
        
        body {
            background-color: #f5f7fa;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 500px;
            padding: 40px;
            text-align: center;
        }
        
        h1 {
            color: #e74c3c;
            margin-bottom: 30px;
            font-size: 28px;
        }
        
        .status-icon {
            font-size: 60px;
            margin-bottom: 25px;
            color: #e74c3c;
        }
        
        .error-message {
            color: #e74c3c;
            font-size: 18px;
            font-weight: 500;
            margin-bottom: 30px;
        }
        
        .continue-btn {
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 14px;
            width: 100%;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        
        .continue-btn:hover {
            background-color: #2980b9;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="status-icon">✕</div>
        <h1>转账失败</h1>
        <div class="error-message">转账失败原因：账户余额不足</div>
        <button class="continue-btn" onclick="window.location.href='transfer.html'">继续转账</button>
    </div>
</body>
</html>
```

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749784033465-30698f73-5f79-4f1c-b10a-a73eddd95401.png)

### 项目搭建及准备工作

1. IDEA 中创建一个 java 模块：bank
2. 创建 `web`目录 对 java 模块添加 web 支持
3. 添加 mysql 驱动 jar 包到 WEB-INF/lib
4. 添加 servlet-api.jar 到 classpath
5. 添加 thymeleaf 相关 jar 包
6. 添加日志框架 logback 的 jar 包和日志配置文件 logback.xml
7. 将slf4j-api-2.0.16.jar 和 thymeleaf-3.1.3.RELEASE.jar 加入到 classpath 中
8. 添加 DbUtils 工具类，将`jdbc.properties`添加到类的根路径下
9. 添加监听器完成 thymeleaf 模板引擎的初始化
10. 在 WEB-INF 目录下新建 templates 目录，用来存储 thymeleaf 的模板文件
11. 将 `index.html`、`success.html`、`error.html`拷贝到 templates 目录下
12. 拷贝之前的 `ThymeleafViewServlet`。
13. 拷贝之前的 `IndexServlet`，但 `IndexServlet`中的代码需要修改为如下：

```java
package com.jkweilai.bank.controller;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
s
@WebServlet("/index")
public class IndexServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setAttribute("template", "index");
        request.getRequestDispatcher("/view").forward(request, response);
    }
}

```

14. 配置欢迎页，达到的效果是访问 `http://localhost:8080/bank`时，显示转账页面。

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749885780415-e9e517b9-c41d-4b2c-a9fd-3f59aeff30e1.png)

### 添加全局异常处理及日志记录

#### 日志记录
日志记录统一面向 `slf4j`日志门面进行日志记录，`slf4j`日志的实现框架采用 `logback`。

修改 `logback.xml`配置文件，代码如下：

```xml
<configuration>
    <!-- 控制台输出格式简化 -->
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{HH:mm:ss} [%thread] %-5level - %msg%n</pattern>
        </encoder>
    </appender>

    <!-- 错误日志单独文件输出:滚动记录，最多保留7天的日志。 -->
    <appender name="ERROR_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>logs/error.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>logs/error.%d{yyyy-MM-dd}.log</fileNamePattern>
            <maxHistory>7</maxHistory>
        </rollingPolicy>
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>

    <!-- Thymeleaf相关日志设置 -->
    <logger name="org.thymeleaf" level="ERROR"/>
    <logger name="org.thymeleaf.TemplateEngine" level="INFO"/>

    <!-- JDBC日志设置：默认Hikari打印日志太多，设置为WARN，只打印重要日志 -->
    <logger name="java.sql" level="WARN"/>
    <logger name="com.zaxxer.hikari" level="WARN"/>

    <!-- 应用包路径日志设置，可以看到自己写的业务逻辑、控制器、服务类的运行情况 -->
    <logger name="com.jkweilai" level="INFO"/>

    <!-- 全局日志级别为：全局日志级别设为 WARN，所有日志同时输出到控制台和错误日志文件 -->
    <root level="WARN">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="ERROR_FILE"/>
    </root>
</configuration>
```

日志级别从低到高：TRACE < DEBUG < INFO < WARN < ERROR（越低，信息越详细）

在需要记录日志的类中获取日志记录器对象，通过它可以记录日志：

```java
private static final Logger logger = LoggerFactory.getLogger(当前类的类名.class);
```

#### 自定义数据库访问异常

```java
package com.jkweilai.bank.common.exception;

/**
 * 数据访问层异常（所有数据库相关异常的父类）
 */
public class DataAccessException extends RuntimeException {
    
    private String errorCode;

    public DataAccessException(String message, Throwable cause) {
        super(message, cause);
    }

    public DataAccessException(String errorCode, String message) {
        super(message);
        this.errorCode = errorCode;
    }

    public DataAccessException(String errorCode, String message, Throwable cause) {
        super(message, cause);
        this.errorCode = errorCode;
    }

    public String getErrorCode() {
        return errorCode;
    }
}
```

#### 自定义业务异常

```java
package com.jkweilai.bank.common.exception;

/**
 * 业务异常
 */
public class BusinessException extends RuntimeException {
    private String errorCode;

    public BusinessException(String errorCode, String message) {
        super(message);
        this.errorCode = errorCode;
    }

    public String getErrorCode() {
        return errorCode;
    }
}
```

#### 编写全局异常处理器
web 容器的异常处理流程

**异常发生时的容器行为：当应用程序中发生未捕获的异常时，Web 容器（如 Tomcat、Jetty）会：**

```java
// 伪代码展示容器的大致处理逻辑
try {
    // 容器调用你的 Servlet
    servlet.service(request, response);
} catch (Throwable t) {
    // 1. 记录错误日志
    containerLogger.error("Servlet执行异常", t);
    
    // 2. 检查web.xml中的error-page配置
    String errorLocation = findErrorPage(t); // servlet/filter
    
    if (errorLocation != null) {
        // 3. 设置错误属性到request中
        request.setAttribute(RequestDispatcher.ERROR_EXCEPTION, t);
        request.setAttribute(RequestDispatcher.ERROR_STATUS_CODE, 500);
        request.setAttribute(RequestDispatcher.ERROR_MESSAGE, t.getMessage());
        
        // 4. 转发到错误处理页面
        request.getRequestDispatcher(errorLocation).forward(request, response);
    } else {
        // 没有配置错误页面，返回默认错误响应
        response.sendError(500, "Internal Server Error");
    }
}
```

因此我们可以编写这样一个全局的异常处理器：

```java
package com.jkweilai.bank.controller;

import com.jkweilai.bank.common.exception.BusinessException;
import com.jkweilai.bank.common.exception.DataAccessException;
import jakarta.servlet.RequestDispatcher;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;

@WebServlet("/error-handler")
public class GlobalExceptionHandler extends HttpServlet {

    private static final Logger logger = LoggerFactory.getLogger(GlobalExceptionHandler.class);

    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        Throwable throwable = (Throwable) request.getAttribute(RequestDispatcher.ERROR_EXCEPTION);
        Integer statusCode = (Integer) request.getAttribute(RequestDispatcher.ERROR_STATUS_CODE);

        if (throwable instanceof BusinessException e) {
            // 业务异常
            logger.warn("转账业务异常: {}", e.getMessage(), e);
            request.setAttribute("errorCode", e.getErrorCode());
            request.setAttribute("errorMessage", e.getMessage());
        } else if (throwable instanceof DataAccessException e) {
            // 数据库访问异常
            logger.error("数据库访问异常", e);
            request.setAttribute("errorCode", "DATABASE_ERROR");
            request.setAttribute("errorMessage", "系统繁忙，请稍后再试");
        } else {
            // 根据状态码定制错误信息
            if (statusCode != null && statusCode == 404) {
                logger.warn("404错误: {}", request.getAttribute(RequestDispatcher.ERROR_REQUEST_URI));
                request.setAttribute("errorCode", "NOT_FOUND");
                request.setAttribute("errorMessage", "请求的资源不存在");
            } else {
                logger.error("系统未知异常", throwable);
                request.setAttribute("errorCode", "SYSTEM_ERROR");
                request.setAttribute("errorMessage", "系统异常，请联系管理员");
            }
        }
        request.setAttribute("template", "error");
        request.getRequestDispatcher("/view").forward(request, response);
    }
}

```

#### 配置全局异常处理器 web.xml

```xml
<error-page>
    <exception-type>java.lang.Throwable</exception-type>
    <location>/error-handler</location>
</error-page>
<error-page>
    <error-code>404</error-code>
    <location>/error-handler</location>
</error-page>
<error-page>
    <error-code>500</error-code>
    <location>/error-handler</location>
</error-page>
```

#### 项目异常处理的最佳实践
在Servlet + Thymeleaf + JDBC的JavaWeb项目中，异常处理的最佳实践可归纳如下：

1. **异常分类与设计**
+ **业务异常**（`BusinessException`）：继承`RuntimeException`，用于处理业务规则违规（如余额不足、数据校验失败）
+ **数据访问异常**（`DataAccessException`）：封装JDBC/SQL异常，隐藏底层数据库细节
+ **系统异常**：非预期的运行时异常（如`NullPointerException`），需记录完整堆栈
2. **分层处理原则**
+ **DAO层**：捕获所有`SQLException`，转换为自定义`DataAccessException`
+ **Service层**：抛出业务异常，避免处理UI相关逻辑
+ **Controller/Servlet层**：捕获异常并转换为用户友好的错误消息
3. **全局异常处理**
+ 配置`web.xml`的`<error-page>`，统一处理HTTP错误码（404/500等）
+ 实现全局异常过滤器（`Filter`）或Servlet，集中处理未捕获异常
+ 通过`request.setAttribute()`传递错误信息到Thymeleaf页面
4. **事务管理**
+ 在Service层开启事务，确保异常时回滚（`Connection#setAutoCommit(false)`）
+ 避免在`catch`块中吞没异常，需抛出或回滚
+ 使用`try-with-resources`确保JDBC资源释放
5. **日志记录规范**
+ **用户/运维需要知道的 →**`**INFO**`
+ **开发排查问题需要的 →**`**DEBUG**`
+ **有问题但还能继续运行的 →**`**WARN**`
+ **无法继续运行的错误 →**`**ERROR**`

### 编写 DTO

根据表单项提取 DTO：AccountDTO

属性包括：转出账户 fromActNo、转入账户 toActNo、转账金额 amount

```java
package com.jkweilai.bank.dto;

import java.math.BigDecimal;

public class AccountDTO {
    private String fromActNo;
    private String toActNo;
    private BigDecimal amount;

    public AccountDTO() {
    }

    public AccountDTO(String fromActNo, String toActNo, BigDecimal amount) {
        this.fromActNo = fromActNo;
        this.toActNo = toActNo;
        this.amount = amount;
    }

    public String getFromActNo() {
        return fromActNo;
    }

    public void setFromActNo(String fromActNo) {
        this.fromActNo = fromActNo;
    }

    public String getToActNo() {
        return toActNo;
    }

    public void setToActNo(String toActNo) {
        this.toActNo = toActNo;
    }

    public BigDecimal getAmount() {
        return amount;
    }

    public void setAmount(BigDecimal amount) {
        this.amount = amount;
    }
}
```

### 编写 VO

根据页面的展示来编写 VO：AccountVO

属性包括：转出账户，转入账户，转账金额，转账时间，交易流水号

```java
package com.jkweilai.bank.vo;

import java.math.BigDecimal;
import java.time.LocalDateTime;

public class AccountVO {
    private String fromActNo;
    private String toActNo;
    private BigDecimal amount;
    private LocalDateTime tranTime;
    private String tranNo;

    public AccountVO() {
    }

    public AccountVO(String fromActNo, String toActNo, BigDecimal amount, LocalDateTime tranTime, String tranNo) {
        this.fromActNo = fromActNo;
        this.toActNo = toActNo;
        this.amount = amount;
        this.tranTime = tranTime;
        this.tranNo = tranNo;
    }

    public String getFromActNo() {
        return fromActNo;
    }

    public void setFromActNo(String fromActNo) {
        this.fromActNo = fromActNo;
    }

    public String getToActNo() {
        return toActNo;
    }

    public void setToActNo(String toActNo) {
        this.toActNo = toActNo;
    }

    public BigDecimal getAmount() {
        return amount;
    }

    public void setAmount(BigDecimal amount) {
        this.amount = amount;
    }

    public LocalDateTime getTranTime() {
        return tranTime;
    }

    public void setTranTime(LocalDateTime tranTime) {
        this.tranTime = tranTime;
    }

    public String getTranNo() {
        return tranNo;
    }

    public void setTranNo(String tranNo) {
        this.tranNo = tranNo;
    }
}
```

### 编写 Entity

实体类和数据库表对应即可，两个实体类：Account、Tran

```java
package com.jkweilai.bank.entity;

import java.math.BigDecimal;

public class Account {
    private Integer id;
    private String actNo;
    private BigDecimal balance;

    public Account() {
    }

    public Account(Integer id, String actNo, BigDecimal balance) {
        this.id = id;
        this.actNo = actNo;
        this.balance = balance;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getActNo() {
        return actNo;
    }

    public void setActNo(String actNo) {
        this.actNo = actNo;
    }

    public BigDecimal getBalance() {
        return balance;
    }

    public void setBalance(BigDecimal balance) {
        this.balance = balance;
    }
}

```

```java
package com.jkweilai.bank.entity;

import java.math.BigDecimal;
import java.time.LocalDateTime;

public class Tran {
    private Integer id;
    private String fromActNo;
    private String toActNo;
    private BigDecimal amount;
    private LocalDateTime tranTime;
    private String tranNo;

    public Tran() {
    }

    public Tran(Integer id, String fromActNo, String toActNo, BigDecimal amount, LocalDateTime tranTime, String tranNo) {
        this.id = id;
        this.fromActNo = fromActNo;
        this.toActNo = toActNo;
        this.amount = amount;
        this.tranTime = tranTime;
        this.tranNo = tranNo;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getFromActNo() {
        return fromActNo;
    }

    public void setFromActNo(String fromActNo) {
        this.fromActNo = fromActNo;
    }

    public String getToActNo() {
        return toActNo;
    }

    public void setToActNo(String toActNo) {
        this.toActNo = toActNo;
    }

    public BigDecimal getAmount() {
        return amount;
    }

    public void setAmount(BigDecimal amount) {
        this.amount = amount;
    }

    public LocalDateTime getTranTime() {
        return tranTime;
    }

    public void setTranTime(LocalDateTime tranTime) {
        this.tranTime = tranTime;
    }

    public String getTranNo() {
        return tranNo;
    }

    public void setTranNo(String tranNo) {
        this.tranNo = tranNo;
    }
}

```

### 编写 DAO

DAO 在编写的时候，一般一个 DAO 接口对应一张表。

DAO 接口中的方法名在起名的时候一般带有：select、insert、delete、update 单词。

#### 编写 AccountDao 接口
转账的过程中需要：

1. 根据账号查询账户，因为要看余额是否充足。
2. 转账时需要修改账户余额，因此要更新账户信息。

```java
package com.jkweilai.bank.dao;

import com.jkweilai.bank.entity.Account;

public interface AccountDao {
    Account selectByActNo(String actNo);
    int updateByActNo(Account account);
}

```

#### 编写 AccountDao 接口的实现类

```java
package com.jkweilai.bank.dao.impl;

import com.jkweilai.bank.common.exception.BusinessException;
import com.jkweilai.bank.common.exception.DataAccessException;
import com.jkweilai.bank.common.util.DbUtils;
import com.jkweilai.bank.dao.AccountDao;
import com.jkweilai.bank.entity.Account;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class AccountDaoImpl implements AccountDao {
    @Override
    public Account selectByActNo(String actNo) {
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        Account account = null;
        try {
            conn = DbUtils.getConnection();
            String sql = "select * from t_act where act_no = ?";
            ps = conn.prepareStatement(sql);
            ps.setString(1, actNo);
            rs = ps.executeQuery();
            if (rs.next()) {
                account = new Account();
                account.setId(rs.getInt("id"));
                account.setActNo(rs.getString("act_no"));
                account.setBalance(rs.getBigDecimal("balance"));
            }else {
                throw new BusinessException("ACCOUNT_NOT_FOUND", actNo + " not found");
            }
        } catch (SQLException e) {
            throw new DataAccessException("数据库访问失败", e);
        } finally {
            DbUtils.close(conn, ps, rs);
        }
        return account;
    }

    @Override
    public int updateByActNo(Account account) {
        Connection conn = null;
        PreparedStatement ps = null;
        int count = 0;
        try {
            conn = DbUtils.getConnection();
            String sql = "update t_act set balance = ? where act_no = ?";
            ps = conn.prepareStatement(sql);
            ps.setBigDecimal(1, account.getBalance());
            ps.setString(2, account.getActNo());
            count = ps.executeUpdate();
            if (count != 1) {
                throw new BusinessException("ACCOUNT_UPDATE_FAIL", account.getActNo() + " update failed");
            }
        } catch (SQLException e) {
            throw new DataAccessException("数据库访问失败", e);
        } finally {
            DbUtils.close(conn, ps, null);
        }
        return count;
    }
}
```

#### 编写 TranDao 接口
转账时要生成一条交易记录，因此需要向交易表中插入一条记录：

```java
package com.jkweilai.bank.dao;

import com.jkweilai.bank.entity.Tran;

public interface TranDao {
    int insert(Tran tran);
}

```

#### 编写 TranDao 接口的实现类

```java
package com.jkweilai.bank.dao.impl;

import com.jkweilai.bank.common.exception.BusinessException;
import com.jkweilai.bank.common.exception.DataAccessException;
import com.jkweilai.bank.common.util.DbUtils;
import com.jkweilai.bank.dao.TranDao;
import com.jkweilai.bank.entity.Tran;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.Timestamp;

public class TranDaoImpl implements TranDao {
    @Override
    public int insert(Tran tran) {
        Connection conn = null;
        PreparedStatement ps = null;
        int count = 0;
        try {
            conn = DbUtils.getConnection();
            String sql = "insert into t_tran(from_act_no,to_act_no,amount,tran_time,tran_no) values(?,?,?,?,?)";
            ps = conn.prepareStatement(sql);
            ps.setString(1, tran.getFromActNo());
            ps.setString(2, tran.getToActNo());
            ps.setBigDecimal(3, tran.getAmount());
            ps.setTimestamp(4, Timestamp.valueOf(tran.getTranTime()));
            ps.setString(5, tran.getTranNo());
            count = ps.executeUpdate();
            if (count != 1) {
                throw new BusinessException("SAVE_TRAN_FAIL", "保存交易记录失败");
            }
        } catch (SQLException e) {
            throw new DataAccessException("SAVE_TRAN_FAIL", "保存交易记录失败");
        } finally {
            DbUtils.close(conn, ps, null);
        }
        return count;
    }
}
```

### 编写 Service

#### 交易号生成工具

```java
package com.jkweilai.bank.common.util;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.atomic.AtomicLong;

public class TranNoGenerator {
    
    private static final AtomicLong counter = new AtomicLong(0);

    public static synchronized String generate() {
        SimpleDateFormat sdf = new SimpleDateFormat("yyyyMMddHHmmssSSS");
        String timePart = sdf.format(new Date());
        long count = counter.incrementAndGet() % 10000;
        return timePart + String.format("%04d", count);
    }
}
```

#### 编写 AccountService 接口
业务接口中的方法名应该带有业务色彩，例如转账：transfer

```java
package com.jkweilai.bank.service;

import com.jkweilai.bank.dto.AccountDTO;
import com.jkweilai.bank.entity.Tran;

public interface AccountService {
    Tran transfer(AccountDTO accountDTO);
}
```

#### 编写 AccountService 接口的实现类
****提示：一定要在 service 的转账业务方法中控制事务！！！！（控制事务都在业务层完成，因为一个事务对应一个完整的业务！！！）****

```java
package com.jkweilai.bank.service.impl;

import com.jkweilai.bank.common.exception.BusinessException;
import com.jkweilai.bank.common.exception.DataAccessException;
import com.jkweilai.bank.common.util.DbUtils;
import com.jkweilai.bank.common.util.TranNoGenerator;
import com.jkweilai.bank.dao.AccountDao;
import com.jkweilai.bank.dao.TranDao;
import com.jkweilai.bank.dao.impl.AccountDaoImpl;
import com.jkweilai.bank.dao.impl.TranDaoImpl;
import com.jkweilai.bank.dto.AccountDTO;
import com.jkweilai.bank.entity.Account;
import com.jkweilai.bank.entity.Tran;
import com.jkweilai.bank.service.AccountService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.sql.Connection;
import java.sql.SQLException;
import java.time.LocalDateTime;

public class AccountServiceImpl implements AccountService {

    private static final Logger logger = LoggerFactory.getLogger(AccountServiceImpl.class);

    private AccountDao accountDao = new AccountDaoImpl();
    private TranDao tranDao = new TranDaoImpl();

    @Override
    public Tran transfer(AccountDTO accountDTO) {
        // 添加日志记录转账开始
        logger.info("开始处理转账业务，转出账户: {}, 转入账户: {}, 金额: {}", accountDTO.getFromActNo(), accountDTO.getToActNo(), accountDTO.getAmount());

        Tran tran = null;
        Connection conn = null;
        try {
            conn = DbUtils.getConnection();
            // 开启事务
            conn.setAutoCommit(false);

            // 1. 查询转出账户
            Account fromAct = accountDao.selectByActNo(accountDTO.getFromActNo());
            logger.debug("转出账户查询结果: {}", fromAct);

            // 2. 检查余额是否充足
            if (fromAct.getBalance().compareTo(accountDTO.getAmount()) < 0) {
                logger.warn("账户余额不足，转出账户: {}, 当前余额: {}, 转账金额: {}", accountDTO.getFromActNo(), fromAct.getBalance(), accountDTO.getAmount());
                throw new BusinessException("BALANCE_NOT_ENOUGH", "余额不足");
            }

            // 3. 查询转入账户
            Account toAct = accountDao.selectByActNo(accountDTO.getToActNo());
            logger.debug("转入账户查询结果: {}", toAct);

            // 4. 更新账户余额
            fromAct.setBalance(fromAct.getBalance().subtract(accountDTO.getAmount()));
            toAct.setBalance(toAct.getBalance().add(accountDTO.getAmount()));

            // 5. 更新数据库
            int count = accountDao.updateByActNo(fromAct);
            count += accountDao.updateByActNo(toAct);

            // 6. 插入交易记录
            tran = new Tran(null, accountDTO.getFromActNo(), accountDTO.getToActNo(), accountDTO.getAmount(), LocalDateTime.now(), TranNoGenerator.generate());
            count += tranDao.insert(tran);
            logger.debug("交易记录生成: {}", tran);

            if (count != 3) {
                logger.error("数据库操作数量异常，预期3条，实际{}条", count);
                throw new BusinessException("TRANSACTION_FAILED", "数据库操作异常");
            }

            // 提交事务
            conn.commit();
            logger.info("转账业务处理成功，交易单号: {}", tran.getTranNo());
        } catch (BusinessException e) {
            // 业务异常直接抛出，不需要回滚（因为已经由调用方处理）
            logger.warn("转账业务异常: {}", e.getMessage());
            throw e;
        } catch (DataAccessException e) {
            // 数据库异常回滚并包装
            logger.error("数据库操作异常", e);
            try {
                if (conn != null) {
                    conn.rollback();
                }
            } catch (SQLException ex) {
                logger.error("事务回滚失败", ex);
                throw new DataAccessException("ROLLBACK_FAILED", "事务回滚失败", ex);
            }
            throw e;
        } catch (Exception e) {
            // 其他未知异常
            logger.error("转账处理发生未知异常", e);
            try {
                if (conn != null) {
                    conn.rollback();
                }
            } catch (SQLException ex) {
                logger.error("事务回滚失败", ex);
                throw new DataAccessException("ROLLBACK_FAILED", "事务回滚失败", ex);
            }
            throw new BusinessException("TRANSFER_FAILED", "转账处理失败");
        } finally {
            DbUtils.close(conn, null, null);
        }
        return tran;
    }
}
```

### 编写 Controller

编写 `AccountController`，它是 Servlet，需要继承 `HttpServlet`，重写 `doPost`方法：

```java
package com.jkweilai.bank.controller;

import com.jkweilai.bank.dto.AccountDTO;
import com.jkweilai.bank.entity.Tran;
import com.jkweilai.bank.service.AccountService;
import com.jkweilai.bank.service.impl.AccountServiceImpl;
import com.jkweilai.bank.vo.AccountVO;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.math.BigDecimal;

@WebServlet("/transfer")
public class AccountController extends HttpServlet {
    private static final Logger logger = LoggerFactory.getLogger(AccountController.class);
    private AccountService accountService = new AccountServiceImpl();

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 记录请求开始
        logger.info("接收到转账请求: fromActNo={}, toActNo={}, amount={}", request.getParameter("fromActNo"), request.getParameter("toActNo"), request.getParameter("amount"));

        // 1. 获取并验证参数
        String fromActNo = request.getParameter("fromActNo");
        String toActNo = request.getParameter("toActNo");
        BigDecimal amount = new BigDecimal(request.getParameter("amount"));

        // 2. 封装DTO
        AccountDTO accountDTO = new AccountDTO(fromActNo, toActNo, amount);

        // 3. 调用服务层进行转账
        Tran tran = accountService.transfer(accountDTO);
        logger.info("转账成功，交易单号: {}", tran.getTranNo());

        // 4. 封装VO对象
        AccountVO accountVO = new AccountVO("****" + fromActNo.substring(fromActNo.length() - 4), "****" + toActNo.substring(toActNo.length() - 4), amount, tran.getTranTime(), tran.getTranNo());

        // 5. 设置请求属性
        request.setAttribute("account", accountVO);
        request.setAttribute("template", "success");

        // 转发请求
        request.getRequestDispatcher("/view").forward(request, response);
    }
}
```

### 修改页面代码

所有页面添加：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749862638029-eadc2ab5-486f-4494-9c71-f6d21c84b873.png)

#### index.html
![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749862710376-fce5be45-58a5-4add-80c8-03b46b40525c.png)

提醒：表单提交方式为 post 方式。

#### success.html
![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749864719488-37300995-d632-40ec-9510-b1282d2d0e5f.png)

#### error.html
![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749883647968-f34a7f78-715e-43e6-9aa9-39df94b335b3.png)

### 测试

到此为止，已经实现了基本的转账逻辑。

---

## 事务问题

1. 在更新转出账户和转入账户之间模拟异常，你会发现数据库中的钱丢了。

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749883851146-f69089c0-c49a-49ae-aff3-e701ab3cfc40.png)

2. 什么原因导致钱丢了？
    1. 在 service 中多次使用 dao，而目前 dao 中任意一个方法只要执行一次就会开启一个新的连接对象，开启一个新的事务。导致 service 方法从开始执行到最终结束，是多个事务，而不是一个事务。
    2. JDBC 默认情况下，如果没有关闭自动提交机制的话，只要执行一条 DML 语句就会自动提交一次。
3. 怎么解决事务问题？
    1. 必须保证在同一个线程中 service 和 dao 中的 Connection 对象是同一个。

---

## ThreadLocal 解决事务问题

要保证在同一个线程中 service 和 dao 中的 Connection 对象是同一个，可以使用 JDK 提供的 `java.lang.ThreadLocal`。

`ThreadLocal`的作用是：在同一个线程中共享同一个 Java 对象。常用方法三个：

```java
// 向当前线程绑定数据data
void set(Object data);

// 获取当前线程中绑定的数据data
Object get();

// 删除当前线程中绑定的数据data
void remove();
```

因此我们需要修改 `DbUtils`工具类，修改获取连接对象的逻辑。代码如下：

```java
package com.jkweilai.bank.common.util;

import java.sql.*;
import java.util.ResourceBundle;

public class DbUtils {
    private static String url;
    private static String user;
    private static String password;
    private static ThreadLocal<Connection> local = new ThreadLocal<>();

    static {
        // 读取属性资源文件
        ResourceBundle bundle = ResourceBundle.getBundle("jdbc");
        String driver = bundle.getString("driver");
        url = bundle.getString("url");
        user = bundle.getString("user");
        password = bundle.getString("password");
        // 注册驱动
        try {
            Class.forName(driver);
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
    }

    public static Connection getConnection() throws SQLException {
        Connection conn = local.get();
        if (conn == null) {
            conn = DriverManager.getConnection(url, user, password);
            local.set(conn);
        }
        return conn;
    }

    public static void close(Connection conn, Statement stmt, ResultSet rs) {
        if (rs != null) {
            try {
                rs.close();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
        if (stmt != null) {
            try {
                stmt.close();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
        if (conn != null) {
            try {
                conn.close();
                // 关闭连接对象移除绑定
                local.remove();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
    }
}
```

所有 DAO 中的方法结束时，不能关闭 Connection 对象：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749866466555-a6ab166c-7ef5-41b1-8c8e-746839a22dc8.png)

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1749866476191-24d4d8f3-11c7-4607-b3a9-839adeb2d038.png)

再次进行测试，你会发现，发生异常之后，数据安全了，事务得到了控制，如果不发生异常，则可以正常完成转账。

---

## MVC架构模式（Java后端视角）

### MVC是什么

MVC（Model-View-Controller）是一种软件架构模式，它将应用程序分为三个核心组件：

1. **Model（模型）**：只收集数据和业务逻辑处理，不关心数据如何展示
    - 在Java Web应用中，通常包含POJO（Plain Old Java Object）、Service层、DAO层等
2. **View（视图）**：只负责数据展示，不负责数据的收集与业务逻辑处理
    - 在Servlet+Thymeleaf中，Thymeleaf模板就是View层
3. **Controller（控制器）**：接收用户请求并协调Model和View
    - Servlet就是Controller的一种实现
    - 处理HTTP请求，调用适当的业务逻辑，决定返回哪个视图

### MVC的工作流程

1. 用户发起HTTP请求 → Web服务器接收请求
2. 根据URL映射到对应的Servlet（Controller）
3. Controller 处理请求：Controller解析参数，调用Service层（Model）处理业务逻辑，将结果数据绑定到域对象
4. Controller 调用Thymeleaf模板（View）,Thymeleaf引擎渲染模板，生成HTML响应，服务器返回HTML给客户端

### MVC的好处

1. **关注点分离**：各组件职责单一，便于维护
    - 修改界面不影响业务逻辑
    - 修改业务逻辑不影响界面
2. **提高可维护性**：代码结构清晰，易于理解和修改
3. **便于团队协作**：
    - 前端开发者专注于View
    - 后端开发者专注于Model和Controller
4. **可重用性**：
    - 同一个Model可以被多个View使用
    - 业务逻辑可以复用
5. **易于测试**：各组件可以独立测试

### MVC与三层架构的区别

| **维度** | **MVC** | **三层架构** |
| --- | --- | --- |
| 关注点 | 关注的是表现层的架构 | 关注的是整个应用的层次划分 |
| 适用范围 | 属于前端的软件设计模式 | 用于整个应用程序的架构模式 |
| 层次关系 | 存在于三层架构的表示层中 | 三层架构包含 MVC |

### MVC 与三层架构的联系

1. MVC通常实现于三层架构的**表示层**中：
    - Controller和View属于表示层
    - Model可能包含业务逻辑层和数据访问层
2. 在实际Java Web应用中，通常结合使用：

```plain
三层架构
├── 表示层 (MVC)
│   ├── Controller (Servlet)
│   ├── View (Thymeleaf)
│   └── Model (DTO/VO)
├── 业务逻辑层 (Service)
└── 数据访问层 (DAO/Repository)
```

3. MVC的Model在三层架构中可能对应业务逻辑层+数据访问层
