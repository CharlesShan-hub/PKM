# Java注释

![Java-basic-comment.excalidraw|1000](../../assets/java-basic-comment.excalidraw.md)

* 极简案例：[comment-detail](../../details/comment-detail.md)

---

## 普通注释

1. Java注释是代码中的非执行性文本，用于向开发者说明代码逻辑、功能或临时屏蔽代码段。它分为单行注释（`//`）、多行注释（`/* ... */`）和文档注释（`/** ... */`）。前两者通常用于代码内部的简短说明、调试或临时注释代码块，而文档注释则专用于API文档的生成。
2. 多行注释的两种写法
    ```java
    /*
     这是一个
     多行注释
    */
    
    /*
     * 这是多行注释
     * 这样写更好看
     */
    ```

### 文档注释（Javadoc）

* **语法**：`/** 文档注释 */`
* **特点**：特殊的注释格式，用于生成HTML格式的API文档
* **用途**：类、接口、方法、字段的正式文档

常用标签

| 标签 | 说明 | 示例 |
|------|------|------|
| `@author` | 作者信息 | `@author 张三` |
| `@version` | 版本号 | `@version 1.0` |
| `@since` | 起始版本 | `@since 1.8` |
| `@param` | 方法参数说明 | `@param name 用户名` |
| `@return` | 返回值说明 | `@return 计算结果` |
| `@throws` | 抛出的异常 | `@throws IOException 输入输出异常` |
| `@see` | 参考链接 | `@see java.lang.String` |
| `@deprecated` | 已过时 | `@deprecated 使用新方法代替` |
标签使用示例

```java
/**
 * 计算两个数的和
 * 
 * @param a 第一个加数
 * @param b 第二个加数
 * @return 两个数的和
 * @throws IllegalArgumentException 如果参数为负数
 * @see Math#addExact(int, int)
 * @since 1.0
 * @author 开发团队
 */
public int add(int a, int b) throws IllegalArgumentException {
    if (a < 0 || b < 0) {
        throw new IllegalArgumentException("参数不能为负数");
    }
    return a + b;
}

/**
 * 已过时的方法，请使用{@link #newMethod()}代替
 * 
 * @deprecated 从版本2.0开始不再推荐使用
 */
@Deprecated
public void oldMethod() {
    // 旧方法实现
}
```

## Javadoc工具

基本语法

```bash
javadoc [选项] [包名] [源文件]
```

常用选项

```bash
-d <directory>      # 指定输出目录
-author             # 包含@author信息
-version            # 包含@version信息
-encoding <编码>    # 指定源文件编码
-windowtitle <文本> # 浏览器窗口标题
-doctitle <HTML>    # 文档标题
```

案例演示

```bash
# 创建文档目录
mkdir doc

# 示例：为单个文件生成文档
javadoc -d ./doc -author -version Student.java

# 示例：为包生成文档
javadoc -d ./doc -author -version com.example.util

# 示例：指定编码（处理中文）
javadoc -d ./doc -author -version -encoding UTF-8 Student.java

# 示例：生成文档
javadoc -d ./doc \
        -author \
        -version \
        -windowtitle "学生管理系统API" \
        -doctitle "<h1>学生管理系统</h1>" \
        Student.java Course.java Teacher.java

# 查看文档
open ./doc/index.html  # Mac
# 或
start ./doc/index.html # Windows
```

## 特殊注释标记

### 1. TODO

* 标识需要完成的工作

```java
// TODO: 实现用户验证逻辑
// TODO: 添加缓存机制
```

### 2. FIXME

* 标识需要修复的问题

```java
// FIXME: 这里存在内存泄漏风险
// FIXME: 时区处理有问题
```

### 3. XXX

* 标识有问题或需要改进的代码

```java
// XXX: 这个实现效率较低，需要优化
// XXX: 临时解决方案，需要重构
```

### 4. HACK

* 标识临时解决方案或取巧的代码

```java
// HACK: 临时绕过权限检查
// HACK: 由于第三方库的限制，这里需要这样写
```

## IDE中的注释功能

### 1. 快速注释/取消注释

* **快捷键**：
  * Windows/Linux: `Ctrl + /`（单行），`Ctrl + Shift + /`（块）
  * Mac: `Cmd + /`（单行），`Cmd + Shift + /`（块）

### 2. 生成Javadoc

* 在方法或类上方输入`/**`然后按回车
* IDE会自动生成文档注释模板

### 3. 查看Javadoc

* 鼠标悬停在方法或类上查看文档
* 使用`Ctrl + Q`（Windows）或`F1`（Mac）查看

## 参考资料

1. [Java文档注释 - 菜鸟教程](https://www.runoob.com/java/java-documentation.html)
2. [Oracle官方Javadoc指南](https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html)
3. [如何编写好的代码注释](https://stackoverflow.com/questions/209015/what-is-self-documenting-code-and-can-it-replace-well-documented-code)
