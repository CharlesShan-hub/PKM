# 标识符

## 可以标识以下内容
1. 变量（Variable）
2. 方法（Method）
3. 类（Class）
4. 接口（Interface）
5. 枚举（Enum）
6. 注解（Annotation）
7. 包（Package）
8. 类型参数（Type Parameter）
9. 类型名称（Type Name）
10. 常量（Constant）


## 标识符命名规则
1. 标识符可以由**字母**、**数字**、**下划线**（`_`）和**美元符号**（`$`）组成，不能含有其他符号。（Java 支持全球所有语言，所以这里的字母指的是任何一个国家的语言都可以）
2. 标识符不能以数字开头。
3. 标识符不能是 Java 中的关键字，如 public、class、void 等。
4. 标识符是区分大小写的，即 Foo 和 foo 是两个不同的标识符。
5. 标识符的长度没有限制，但是 Java 建议使用有意义的、简短的标识符。

例如，以下是合法的标识符：`_name`、`$name`、 `中文`

而以下是不合法的标识符：

1. `123name`（以数字开头）
2. `public`（关键字）
3. `my-name`（中间包含横线）
4. `MyClassName!`（包含非法字符）


## 标识符命名规范
1. 见名知意
2. 类名、接口名、枚举、注解：大驼峰。（`StudentService`，`UserService`）
3. 变量名和方法名：小驼峰。（`doSome`，`doOther`）
4. 常量名：全部大写，每个单词用下划线连接。（`LOGIN_SUCCESS`，`SYSTEM_ERROR`）
5. 包名：全部小写
6. 代码规范：👉[Google规范](http://doc.vrd.net.cn/codingstyle/google-java-styleguide-zh.pdf)，👉[JLS](https://docs.oracle.com/javase/specs/jls/se21/html/)
