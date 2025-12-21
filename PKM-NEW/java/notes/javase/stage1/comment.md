# Java注释

---

## 注释的作用

注释是程序员在代码中添加的说明性文字，不会被编译器执行，主要用于：
1. **代码说明**：解释代码的功能和逻辑
2. **文档生成**：通过Javadoc生成API文档
3. **调试辅助**：临时禁用代码段
4. **团队协作**：帮助其他开发者理解代码

## 注释的类型

### 1. 单行注释
- **语法**：`// 注释内容`
- **特点**：从`//`开始到行尾的内容都是注释
- **用途**：简短说明、行尾注释

```java
// 这是单行注释
int age = 25;  // 定义年龄变量
// System.out.println("这行代码被注释了");
```

### 2. 多行注释
- **语法**：`/* 注释内容 */`
- **特点**：可以跨越多行
- **用途**：较长的说明、临时屏蔽代码块

```java
/*
 * 这是多行注释
 * 可以包含多行内容
 * 常用于方法或类的说明
 */

/*
 也可以不使用星号前缀
 直接写多行内容
*/

/* 临时注释掉的代码段
System.out.println("第一行");
System.out.println("第二行");
System.out.println("第三行");
*/
```

### 3. 文档注释（Javadoc）
- **语法**：`/** 文档注释 */`
- **特点**：特殊的注释格式，用于生成HTML格式的API文档
- **用途**：类、接口、方法、字段的正式文档

```java
/**
 * 这是一个学生类
 * 用于表示学生的基本信息
 * 
 * @author 张三
 * @version 1.0
 * @since 2024
 */
public class Student {
    /**
     * 学生姓名
     */
    private String name;
    
    /**
     * 学生年龄
     */
    private int age;
    
    /**
     * 构造方法
     * @param name 学生姓名
     * @param age 学生年龄
     */
    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    /**
     * 获取学生姓名
     * @return 学生姓名
     */
    public String getName() {
        return name;
    }
    
    /**
     * 设置学生姓名
     * @param name 新的姓名
     */
    public void setName(String name) {
        this.name = name;
    }
}
```

## Javadoc标签

### 常用标签
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

### 标签使用示例
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

## 生成API文档

### 使用Javadoc工具
```bash
# 基本语法
javadoc [选项] [包名] [源文件]

# 常用选项
-d <directory>      # 指定输出目录
-author             # 包含@author信息
-version            # 包含@version信息
-encoding <编码>    # 指定源文件编码
-windowtitle <文本> # 浏览器窗口标题
-doctitle <HTML>    # 文档标题

# 示例：为单个文件生成文档
javadoc -d ./doc -author -version Student.java

# 示例：为包生成文档
javadoc -d ./doc -author -version com.example.util

# 示例：指定编码（处理中文）
javadoc -d ./doc -author -version -encoding UTF-8 Student.java
```

### 生成文档示例
```bash
# 创建文档目录
mkdir doc

# 生成文档
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

## 注释的最佳实践

### 1. 该注释什么
- **公共API**：所有public类、接口、方法、字段
- **复杂算法**：难以理解的逻辑
- **业务规则**：特定的业务需求
- **TODO/FIXME**：待完成或需要修复的代码
- **重要假设**：代码基于的假设条件

### 2. 注释风格建议
```java
// 好的注释示例
public class Calculator {
    /**
     * 计算圆的面积
     * 使用公式：π * r²
     * 
     * @param radius 圆的半径（必须大于0）
     * @return 圆的面积
     * @throws IllegalArgumentException 如果半径小于等于0
     */
    public double calculateCircleArea(double radius) {
        if (radius <= 0) {
            throw new IllegalArgumentException("半径必须大于0");
        }
        return Math.PI * radius * radius;
    }
    
    // TODO: 添加计算矩形面积的方法
    // FIXME: 这里需要处理浮点数精度问题
    
    /**
     * 假设：用户ID从1000开始递增
     * 如果系统迁移，可能需要修改这个逻辑
     */
    private static final int START_USER_ID = 1000;
}

// 不好的注释示例
public class BadExample {
    // 设置x为10（废话注释）
    int x = 10;
    
    // 增加计数器（没有说明为什么）
    counter++;
    
    /* 这个方法做了一些事情 */
    public void doSomething() {
        // 这里有很多代码
    }
}
```

### 3. 注释的"不要"
- ❌ 不要写显而易见的注释
- ❌ 不要写与代码不一致的注释
- ❌ 不要保留无用的注释代码
- ❌ 不要用注释代替清晰的代码
- ❌ 不要写过于冗长的注释

## 特殊注释标记

### 1. TODO
- 标识需要完成的工作
```java
// TODO: 实现用户验证逻辑
// TODO: 添加缓存机制
```

### 2. FIXME
- 标识需要修复的问题
```java
// FIXME: 这里存在内存泄漏风险
// FIXME: 时区处理有问题
```

### 3. XXX
- 标识有问题或需要改进的代码
```java
// XXX: 这个实现效率较低，需要优化
// XXX: 临时解决方案，需要重构
```

### 4. HACK
- 标识临时解决方案或取巧的代码
```java
// HACK: 临时绕过权限检查
// HACK: 由于第三方库的限制，这里需要这样写
```

## IDE中的注释功能

### 1. 快速注释/取消注释
- **快捷键**：
  - Windows/Linux: `Ctrl + /`（单行），`Ctrl + Shift + /`（块）
  - Mac: `Cmd + /`（单行），`Cmd + Shift + /`（块）

### 2. 生成Javadoc
- 在方法或类上方输入`/**`然后按回车
- IDE会自动生成文档注释模板

### 3. 查看Javadoc
- 鼠标悬停在方法或类上查看文档
- 使用`Ctrl + Q`（Windows）或`F1`（Mac）查看

## 参考资料

1. [Java文档注释 - 菜鸟教程](https://www.runoob.com/java/java-documentation.html)
2. [Oracle官方Javadoc指南](https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html)
3. [如何编写好的代码注释](https://stackoverflow.com/questions/209015/what-is-self-documenting-code-and-can-it-replace-well-documented-code)