# 第一个Java程序
---

## Hello World实战
1. 基本步骤
    1. **编码** - 创建`Hello.java`文件。
    2. **编译** - 使用`javac`命令：`javac ./Hello.java`，生成`Hello.class`字节码文件。
    3. **运行** - 使用`java`命令：`java Hello`。注意：运行时不带`.class`扩展名。
2. 编码注意事项
    1. windows中文默认使用GBK编码，所以代码.java文件也需要保存为GBK编码
    2. 也可以把windows终端和代码一起改成utf-8，总之就是终端和程序要统一
    3. 具体编码介绍：[编码](../../05-io/coding.md)
3. 示例代码
    ```java
    // Hello.java
    public class Hello {
        public static void main(String[] args) {
            System.out.println("Hello World");
        }
    }
    ```
* `javac`命令具体参数：👉[command-javac](command-javac.md)
* `java`命令具体参数：👉[command-java](command-java.md)

---


## Java源文件结构
1. 类声明规则
    1. 一个java文件中可以有**0或1个**`public`类
    2. 一个java文件中可以有**0到n个**非`public`类
    3. 源文件名必须与`public`类名完全一致
    4. 编译后，每个类都会生成对应的`.class`文件

    ```java
    // Hello.java（文件名必须与 public 类名一致）
    public class Hello {
        public static void main(String[] args) {
            System.out.println("Hello World");
        }
    }
    
    // 可以包含多个非public类
    class Another {
    }
    ```

2. `main`方法的位置
    1. `public static void main(String[] args)`可以不在`public`类中
    2. 运行时需要指定包含`main`方法的类名

    ```java
    // Hello.java
    // 编译：javac Hello.java
    // 运行：java Another
    public class Hello {
        // 这个类没有main方法
    }
    
    class Another {
        public static void main(String[] args) {
            System.out.println("Another World");
        }
    }
    ```


## 注释
1. Java注释是代码中的非执行性文本，用于向开发者说明代码逻辑、功能或临时屏蔽代码段。它分为单行注释（`//`）、多行注释（`/* ... */`）和文档注释（`/** ... */`）。前两者通常用于代码内部的简短说明、调试或临时注释代码块，而文档注释则专用于API文档的生成。
2. 注释在换行的地方也可以写：[comment-example](../../../details/comment-example.md)
3. 多行注释的两种写法
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
