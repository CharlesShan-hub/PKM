# Yaml Syntax

## Syntax

**键值对**：并不像 json 需要括号，yaml 想 python 一样，仅用缩进就可以了，所以说 yaml 是一种适合人类阅读的标记语言

```yaml
app: user-authentication
port: 9000
version: 1.7
```

**字符串**：我们可以用单引号，双括号或者不加引号。但是如果有转义符号，还是要加引号

```yaml
str1: "string"
str2: 'string'
str3: string
str4: "Hello World\n"
long_string: |
    this is a single line string, thaat should be all one one line.
    some othher stuff.
```

**注释**：yaml 也是支持注释的，json 不支持

```yaml
# 这是注释
```

**对象**：下面的microservice就是对象，app等等都是它的属性

```yaml
microservice:
    app: user-authentication
    port: 9000
    version: 1.7
```

**列表**：加入横线，并列的就在一个列表里了。或者用\[]也可以

<pre class="language-yaml"><code class="lang-yaml">microservice:
<strong>  - app: user-authentication
</strong>    port: 9000
    version: 1.7
  - app: shopping-cart
    port: 9002
    versions: [1.0, 2.0, 2.1]
</code></pre>

**布尔**：true 或 false，yes 或 no，on 或 off

<pre class="language-yaml"><code class="lang-yaml">microservice:
  - app: user-authentication
    port: 9000
    version: 1.7
<strong>    deployed: true # false
</strong><strong>    # deployed: yes / no
</strong><strong>    # deployed: on / off
</strong></code></pre>

**系统变量**：$

```yaml
command:
    - /bin/sh
    - -ec
    - >-
        mysql -h 127.0.0.1 -u root -p$MYSQL_ROT_PASSWORD$ -e 'SELECT 1'
```

**占位符**：\{{\}}，保留一个位置，让其他语言来进一步添加

```yaml
app:
  name: My Application
  version: 1.0.0
  environment: {{ environment }}
  database:
    host: {{ db_host }}
    port: {{ db_port }}
    username: {{ db_username }}
    password: {{ db_password }}

api:
  base_url: {{ api_base_url }}
  timeout: {{ api_timeout }}
```

用 python 的 jinja2 动态地替换这些占位符：

```python
from jinja2 import Template

# 读取 YAML 文件
with open("config.yaml", "r") as file:
    template_content = file.read()

# 创建模板
template = Template(template_content)

# 定义替换占位符的值
values = {
    "environment": "production",
    "db_host": "localhost",
    "db_port": "5432",
    "db_username": "admin",
    "db_password": "password123",
    "api_base_url": "https://api.example.com",
    "api_timeout": 30
}

# 渲染模板
rendered_content = template.render(values)

# 输出渲染后的内容
print(rendered_content)

```

```yaml
app:
  name: My Application
  version: 1.0.0
  environment: production
  database:
    host: localhost
    port: 5432
    username: admin
    password: password123

api:
  base_url: https://api.example.com
  timeout: 30
```

文件分离（---）：比如 log 文件

```yaml
---
Time: 2001-11-23 15:01:42 -5
User: ed
Warning:
  This is an error message
  for the log file
---
Time: 2001-11-23 15:02:31 -5
User: ed
Warning:
  A slightly different error
  message.
---
Date: 2001-11-23 15:03:17 -5
User: ed
Fatal:
  Unknown variable "bar"
Stack:
- file: TopClass.py
  line: 23
  code: |
    x = MoreObject("345\n")
- file: MoreClass.py
  line: 58
  code: |-
    foo = bar
```



## Reference

\[1] [Yaml Tutorial | Learn YAML in 18 mins](https://www.youtube.com/watch?v=1uFVr15xDGg)
