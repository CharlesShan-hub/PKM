# 使用日志组，这是改组的日志级别

logging.level.mybusiness=DEBUG

```

### SpringBoot 内置的日志组

| **日志组名称** | **包含的日志记录器 (Loggers)** |
| --- | --- |
| `**web**` | `**org.springframework.core.codec**`<br/>**,**`**org.springframework.http**`<br/>**,**`**org.springframework.web**`<br/>**,**`**org.springframework.boot.actuate.endpoint.web**`<br/>**,**`**org.springframework.boot.web.servlet.ServletContextInitializerBeans**` |
| `**sql**` | `**org.springframework.jdbc.core**`<br/>**,**`**org.hibernate.SQL**`<br/>**,**`**org.hibernate.type.descriptor.sql.BasicBinder**` |

`**sql**`**日志组**：**统一配置**JDBC Template**和**Hibernate**这类与数据库交互的底层框架的日志，**它与 MyBatis 完全无关**

`**web**`**日志组：**记录了**Spring MVC/WebFlux 框架处理 HTTP 请求、响应及内部组件的全链路调试信息**，是排查 Web 层问题的核心工具。通过组名可以统一配置日志行为：**

```yaml

logging:
  level:
    sql: TRACE    # 同时输出SQL和参数
    web: TRACE    # 输出Web处理全链路

```

### 日志的查找优先级

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1765190559645-fb05639a-972a-45be-9041-a83502619933.png" width="600.4000244140625" title="" crop="0,0,1,1" id="u967a3449" class="ne-image">

---

## 日志输出到文件

```properties

logging.file.name=./log/my.log

```

日志文件将被生成到当前工作目录下的 `log`目录，并且在该目录下生成 `my.log`文件

---

## 滚动日志

滚动日志是一种日志管理机制，用于防止日志文件无限增长，通过将日志文件分割成多个文件，每个文件只包含一定时间段或大小的日志记录。滚动日志可以帮助你更好地管理和维护日志文件，避免单个日志文件过大导致难以处理。

```properties
