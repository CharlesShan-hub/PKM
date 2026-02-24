# Java键盘输入

![java-basic-sacnner.excalidraw|1000](../../assets/java-basic-sacnner.excalidraw.md)

---

## 快速入门

### 基础示例
```java
import java.util.Scanner;

public class KeyboardInputDemo {
    public static void main(String[] args) {
        // 1. 创建Scanner对象
        Scanner scanner = new Scanner(System.in);
        
        // 2. 接收各种类型输入
        System.out.print("请输入名字: ");
        String name = scanner.next();
        
        System.out.print("请输入性别: ");
        char gender = scanner.next().charAt(0);
        
        System.out.print("请输入年龄: ");
        int age = scanner.nextInt();
        
        System.out.print("请输入薪水: ");
        double salary = scanner.nextDouble();
        
        // 3. 输出结果
        System.out.println("名字: " + name);
        System.out.println("性别: " + gender);
        System.out.println("年龄: " + age);
        System.out.println("薪水: " + salary);
        
        // 4. 关闭Scanner
        scanner.close();
    }
}
```

### 参考资料
- [Java Scanner 类（菜鸟教程）](https://www.runoob.com/java/java-scanner-class.html)
- [Java 11 Scanner API文档](https://www.runoob.com/manual/jdk11api/java.base/java/util/Scanner.html)

---

## Scanner类详解

### 什么是Scanner？
Scanner是Java中用于解析基本类型和字符串的文本扫描器，位于`java.util`包中。

### 主要特点
- **基于正则表达式**进行文本解析
- **支持多种数据类型**：整数、浮点数、字符串、布尔值等
- **多种输入源**：键盘、字符串、文件等
- **线程不安全**：不适合多线程环境共享使用

---

## 创建Scanner对象

### 从不同输入源创建
```java
// 1. 从标准输入（键盘）
Scanner keyboardScanner = new Scanner(System.in);

// 2. 从字符串
Scanner stringScanner = new Scanner("Hello World 123");

// 3. 从文件
try {
    Scanner fileScanner = new Scanner(new File("input.txt"));
} catch (FileNotFoundException e) {
    e.printStackTrace();
}

// 4. 从输入流
Scanner streamScanner = new Scanner(System.in);
```

---

## 常用输入方法

### 基本数据类型输入
- **`next()`**：读取下一个字符串（以空格为分隔符）
- **`nextLine()`**：读取整行文本（包括空格）
- **`nextInt()`**：读取下一个整数
- **`nextDouble()`**：读取下一个双精度浮点数
- **`nextFloat()`**：读取下一个单精度浮点数
- **`nextLong()`**：读取下一个长整数
- **`nextShort()`**：读取下一个短整数
- **`nextByte()`**：读取下一个字节
- **`nextBoolean()`**：读取下一个布尔值

### 检查方法
- **`hasNext()`**：检查是否还有输入
- **`hasNextInt()`**：检查下一个输入是否是整数
- **`hasNextDouble()`**：检查下一个输入是否是双精度数
- **`hasNextLine()`**：检查是否还有下一行

### 综合示例
```java
import java.util.Scanner;

public class ComprehensiveExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // 字符串输入
        System.out.print("请输入姓名: ");
        String name = scanner.nextLine();
        
        // 整数输入
        System.out.print("请输入年龄: ");
        int age = scanner.nextInt();
        
        // 浮点数输入
        System.out.print("请输入身高(米): ");
        double height = scanner.nextDouble();
        
        // 布尔值输入
        System.out.print("是否已婚(true/false): ");
        boolean isMarried = scanner.nextBoolean();
        
        // 清理缓冲区（重要！）
        scanner.nextLine();
        
        // 再次读取字符串
        System.out.print("请输入地址: ");
        String address = scanner.nextLine();
        
        // 输出结果
        System.out.println("\n=== 用户信息 ===");
        System.out.println("姓名: " + name);
        System.out.println("年龄: " + age);
        System.out.println("身高: " + height + "米");
        System.out.println("婚姻状况: " + (isMarried ? "已婚" : "未婚"));
        System.out.println("地址: " + address);
        
        scanner.close();
    }
}
```

---

## 重要特性与技巧

### 1. next() vs nextLine() 的区别
```java
Scanner scanner = new Scanner(System.in);

System.out.print("输入测试: ");
String word = scanner.next();      // 只读取到空格前
System.out.println("next(): " + word);

scanner.nextLine(); // 清理缓冲区

System.out.print("再输入测试: ");
String line = scanner.nextLine();  // 读取整行
System.out.println("nextLine(): " + line);
```

**示例输入输出**：
```
输入测试: Hello World
next(): Hello
再输入测试: Hello World
nextLine(): Hello World
```


### 2. 处理混合输入问题
```java
// 常见问题：nextInt()后接nextLine()会跳过
Scanner scanner = new Scanner(System.in);

System.out.print("请输入年龄: ");
int age = scanner.nextInt();  // 读取数字，但留下换行符

// 解决方案1：添加额外的nextLine()清理缓冲区
scanner.nextLine();

System.out.print("请输入姓名: ");
String name = scanner.nextLine();  // 现在可以正常读取

System.out.println("年龄: " + age + ", 姓名: " + name);
```

### 3. 自定义分隔符
```java
// 默认使用空白字符分隔，可以自定义
String data = "苹果,香蕉,橙子,葡萄";
Scanner scanner = new Scanner(data);
scanner.useDelimiter(",");  // 设置逗号为分隔符

while (scanner.hasNext()) {
    System.out.println(scanner.next());
}
// 输出：苹果 香蕉 橙子 葡萄
```

### 4. 区域设置（Locale）
```java
Scanner scanner = new Scanner("123,45");
scanner.useLocale(Locale.FRENCH);  // 法国使用逗号作为小数点
double number = scanner.nextDouble();  // 123.45
System.out.println(number);
```

### 5. 使用正则表达式
```java
Scanner scanner = new Scanner("abc123def456ghi789");

// 查找匹配模式的内容
while (scanner.hasNext()) {
    if (scanner.hasNextInt()) {
        int num = scanner.nextInt();
        System.out.println("找到数字: " + num);
    } else {
        scanner.next(); // 跳过非数字
    }
}
```

---

## 常见问题与解决方案

### 问题1：InputMismatchException
**现象**：输入类型与期望类型不匹配
```java
Scanner scanner = new Scanner(System.in);
System.out.print("请输入数字: ");
try {
    int num = scanner.nextInt();
} catch (InputMismatchException e) {
    System.out.println("输入的不是有效数字！");
    scanner.next(); // 清除错误的输入
}
```

### 问题2：NoSuchElementException
**现象**：没有更多输入时调用next方法
```java
Scanner scanner = new Scanner("");
if (scanner.hasNext()) {
    String text = scanner.next();  // 安全调用
}
```

### 问题3：资源未关闭
**解决方案**：使用try-with-resources自动关闭
```java
try (Scanner scanner = new Scanner(System.in)) {
    System.out.print("请输入: ");
    String input = scanner.nextLine();
    System.out.println("输入的是: " + input);
} // 自动关闭，无需显式调用close()
```

### 问题4：System.in被关闭
**注意**：关闭Scanner也会关闭关联的System.in
```java
Scanner scanner1 = new Scanner(System.in);
scanner1.close();

// 错误：System.in已被关闭
// Scanner scanner2 = new Scanner(System.in);
```

---

## 实际应用示例

### 示例1：用户注册系统
```java
import java.util.Scanner;

public class UserRegistration {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("=== 用户注册 ===");
            
            System.out.print("用户名: ");
            String username = scanner.nextLine();
            
            System.out.print("密码: ");
            String password = scanner.nextLine();
            
            System.out.print("邮箱: ");
            String email = scanner.nextLine();
            
            System.out.print("年龄: ");
            int age = scanner.nextInt();
            scanner.nextLine(); // 清理缓冲区
            
            System.out.print("手机号: ");
            String phone = scanner.nextLine();
            
            System.out.println("\n注册成功！");
            System.out.println("用户名: " + username);
            System.out.println("邮箱: " + email);
            System.out.println("年龄: " + age);
            System.out.println("手机号: " + phone);
        }
    }
}
```

### 示例2：计算器程序
```java
import java.util.Scanner;

public class SimpleCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== 简单计算器 ===");
        System.out.print("请输入第一个数字: ");
        double num1 = scanner.nextDouble();
        
        System.out.print("请输入运算符(+, -, *, /): ");
        char operator = scanner.next().charAt(0);
        
        System.out.print("请输入第二个数字: ");
        double num2 = scanner.nextDouble();
        
        double result = 0;
        boolean valid = true;
        
        switch (operator) {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                if (num2 != 0) {
                    result = num1 / num2;
                } else {
                    System.out.println("错误：除数不能为0！");
                    valid = false;
                }
                break;
            default:
                System.out.println("错误：无效的运算符！");
                valid = false;
        }
        
        if (valid) {
            System.out.printf("%.2f %c %.2f = %.2f\n", num1, operator, num2, result);
        }
        
        scanner.close();
    }
}
```

### 示例3：文件内容读取
```java
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class FileReaderExample {
    public static void main(String[] args) {
        try (Scanner fileScanner = new Scanner(new File("data.txt"))) {
            int lineNumber = 1;
            
            while (fileScanner.hasNextLine()) {
                String line = fileScanner.nextLine();
                System.out.printf("第%d行: %s\n", lineNumber++, line);
            }
            
            System.out.println("文件读取完成，共" + (lineNumber - 1) + "行");
            
        } catch (FileNotFoundException e) {
            System.out.println("文件未找到: " + e.getMessage());
        }
    }
}
```

### 示例4：CSV数据解析
```java
import java.util.Scanner;

public class CSVParser {
    public static void main(String[] args) {
        String csvData = "张三,25,北京,工程师\n李四,30,上海,经理\n王五,28,广州,设计师";
        Scanner scanner = new Scanner(csvData);
        
        System.out.println("=== CSV数据解析 ===");
        System.out.println("姓名\t年龄\t城市\t职位");
        System.out.println("----------------------------");
        
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            Scanner lineScanner = new Scanner(line);
            lineScanner.useDelimiter(",");
            
            while (lineScanner.hasNext()) {
                System.out.print(lineScanner.next() + "\t");
            }
            System.out.println();
            
            lineScanner.close();
        }
        
        scanner.close();
    }
}
```

---

## 最佳实践指南

### 1. 输入验证
```java
public static int getValidInt(Scanner scanner, String prompt) {
    while (true) {
        System.out.print(prompt);
        if (scanner.hasNextInt()) {
            int value = scanner.nextInt();
            scanner.nextLine(); // 清理缓冲区
            return value;
        } else {
            System.out.println("输入无效，请重新输入数字！");
            scanner.next(); // 清除无效输入
        }
    }
}
```

### 2. 安全关闭资源
```java
// 推荐：使用try-with-resources
try (Scanner scanner = new Scanner(System.in)) {
    // 使用scanner
    String input = scanner.nextLine();
    System.out.println("输入: " + input);
} // 自动关闭

// 或者：在finally块中关闭
Scanner scanner = null;
try {
    scanner = new Scanner(System.in);
    // 使用scanner
} finally {
    if (scanner != null) {
        scanner.close();
    }
}
```

### 3. 性能优化建议
- 对于大量数据读取，考虑使用`BufferedReader`
- 避免频繁创建和销毁Scanner对象
- 对于文件读取，使用合适的缓冲区大小

### 4. 错误处理模板
```java
public class SafeInput {
    public static String getStringInput(Scanner scanner, String prompt) {
        System.out.print(prompt);
        try {
            return scanner.nextLine();
        } catch (Exception e) {
            System.out.println("输入错误: " + e.getMessage());
            return "";
        }
    }
    
    public static int getIntInput(Scanner scanner, String prompt) {
        while (true) {
            System.out.print(prompt);
            try {
                int value = Integer.parseInt(scanner.nextLine());
                return value;
            } catch (NumberFormatException e) {
                System.out.println("请输入有效的整数！");
            }
        }
    }
}
```

---

## 总结要点

### 核心知识点
1. **创建Scanner**：`new Scanner(System.in)` 用于键盘输入
2. **读取方法**：
   - `next()`：读取单词（空格分隔）
   - `nextLine()`：读取整行
   - `nextInt()`、`nextDouble()`等：读取特定类型
3. **缓冲区问题**：混合输入时注意清理缓冲区
4. **资源管理**：使用后关闭Scanner，推荐try-with-resources

### 常见陷阱
1. `nextInt()`后接`nextLine()`会跳过输入
2. 输入类型不匹配会导致`InputMismatchException`
3. 关闭Scanner也会关闭关联的输入流

### 实用技巧
1. 使用`hasNextXxx()`方法进行输入验证
2. 自定义分隔符处理特定格式数据
3. 结合正则表达式进行复杂文本解析

通过掌握Scanner类的使用，可以轻松处理各种用户输入场景，构建交互性强的Java应用程序。