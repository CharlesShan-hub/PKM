# 国际化（了解）

在Spring Boot中实现国际化（i18n）是一个常见的需求，它允许应用程序根据用户的语言和地区偏好显示不同的文本。

---

## 实现国际化

### 第一步：创建资源文件

创建包含不同语言版本的消息文件。这些文件通常放在`src/main/resources`目录下，并且以`.properties`为扩展名。例如：

+ `messages.properties` (默认语言，如中文)
+ `messages_en.properties` (英文)
+ `messages_fr.properties` (法语)

每个文件都应包含相同的消息键，但值应对应于相应的语言。例如：

**messages.properties**:

```properties
welcome.message=欢迎来到我们的应用！
```

**messages_en.properties**:

```properties
welcome.message=Welcome to our application!
```

**messages_fr.properties**:

```properties
welcome.message=Bienvenue dans notre application !
```

### 第二步：在模板文件中取出消息

语法格式为：#{welcome.message}

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1 th:text="#{welcome.message}"></h1>
</body>
</html>
```

**测试1：浏览器默认的语言环境是中文时**

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1731511421500-651602c6-6dac-418c-9d1e-77c7ae40f463.png" width="373" title="" crop="0,0,1,1" id="u77fa5895" class="ne-image">

**测试2：将浏览器默认语言环境修改为法文**

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1731512808484-d61096e2-4d1d-446c-a26f-33c1505d76e4.png" width="696" title="" crop="0,0,1,1" id="u441ef955" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1731512824927-f649b549-0add-4450-9dc3-9e2a4331c025.png" width="608" title="" crop="0,0,1,1" id="u593fd8ed" class="ne-image">

---

## 国际化实现原理

做国际化的自动配置类是：`MessageSourceAutoConfiguration`

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1731513242246-ac4e59e3-a1e9-45c3-a346-41ae1b41f658.png" width="791" title="" crop="0,0,1,1" id="u89d8877d" class="ne-image">

通过以上源码得知，国际化对应的配置前缀是：`spring.message`

例如在`application.properties`中进行如下配置：

```properties
