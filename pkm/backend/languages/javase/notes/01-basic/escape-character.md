# Java转义字符

---

## 什么是转义字符

转义字符是以反斜杠`\`开头的特殊字符序列，用于表示一些无法直接输入的字符或具有特殊含义的字符。

## 常用转义字符表

| 转义字符 | 名称  | 说明        | 示例                        |
| ---- | --- | --------- | ------------------------- |
| `\t` | 制表符 | 水平制表，用于对齐 | `"北京\t天津\t上海"`            |
| `\n` | 换行符 | 换到下一行开头   | `"第一行\n第二行"`              |
| `\\` | 反斜杠 | 表示一个反斜杠字符 | `"C:\\Windows\\System32"` |
| `\"` | 双引号 | 表示双引号字符   | `"他说：\"你好！\""`            |
| `\'` | 单引号 | 表示单引号字符   | `'字符：\'A\''`              |
| `\r` | 回车符 | 回到行首（覆盖）  | `"abc\rde"` → `"dec"`     |
| `\b` | 退格符 | 后退一格      | `"ab\bc"` → `"ac"`        |
| `\f` | 换页符 | 换到下一页开头   | 用于打印机控制                   |

## 详细说明与示例

### 1. 制表符 `\t`
- **功能**：在输出中插入一个制表位，实现对齐效果
- **示例**：
  ```java
  System.out.println("姓名\t年龄\t城市");
  System.out.println("张三\t25\t北京");
  System.out.println("李四\t30\t上海");
  ```
  **输出**：
  ```
  姓名    年龄    城市
  张三    25      北京
  李四    30      上海
  ```

### 2. 换行符 `\n`
- **功能**：在当前位置换行
- **示例**：
  ```java
  System.out.println("第一行\n第二行\n第三行");
  ```
  **输出**：
  ```
  第一行
  第二行
  第三行
  ```

### 3. 反斜杠 `\\`
- **功能**：表示文件路径中的反斜杠
- **示例**：
  ```java
  System.out.println("文件路径：C:\\Program Files\\Java");
  ```
  **输出**：
  ```
  文件路径：C:\Program Files\Java
  ```

### 4. 引号 `\"` 和 `\'`
- **功能**：在字符串中插入引号字符
- **示例**：
  ```java
  System.out.println("他说：\"Java很有趣！\"");
  System.out.println("字符：\'A\'");
  ```
  **输出**：
  ```
  他说："Java很有趣！"
  字符：'A'
  ```

### 5. 回车符 `\r`（重点理解）
- **功能**：将光标移动到当前行的开头，后续内容会覆盖前面的内容
- **示例**：
  ```java
  System.out.println("abc\rde");
  System.out.println("123456\rxx");
  ```
  **输出**：
  ```
  dec
  xx3456
  ```
- **解释**：
  - `"abc\rde"`：先输出`abc`，回车到行首，输出`de`覆盖`ab`，结果为`dec`
  - `"123456\rxx"`：先输出`123456`，回车到行首，输出`xx`覆盖`12`，结果为`xx3456`

### 6. 退格符 `\b`
- **功能**：将光标后退一个字符位置
- **示例**：
  ```java
  System.out.println("ab\bc");
  System.out.println("hello\b\bworld");
  ```
  **输出**：
  ```
  ac
  helworld
  ```

## 综合示例

```java
// EscapeCharacters.java
public class EscapeCharacters {
    public static void main(String[] args) {
        // 制表符示例
        System.out.println("商品\t价格\t数量");
        System.out.println("苹果\t5.0\t10");
        System.out.println("香蕉\t3.0\t20");
        
        // 换行符示例
        System.out.println("\n--- 用户信息 ---");
        System.out.println("姓名：张三\n年龄：25\n城市：北京");
        
        // 路径示例
        System.out.println("\n--- 系统路径 ---");
        System.out.println("Java安装目录：C:\\Program Files\\Java\\jdk1.8");
        
        // 引号示例
        System.out.println("\n--- 对话 ---");
        System.out.println("老师说：\"同学们好！\"");
        System.out.println("学生说：\'老师好！\'");
        
        // 回车符演示
        System.out.println("\n--- 回车符演示 ---");
        System.out.print("加载中");
        for (int i = 0; i < 3; i++) {
            try {
                Thread.sleep(500); // 暂停500毫秒
                System.out.print(".");
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println("\r加载完成！");
        
        // 退格符示例
        System.out.println("\n--- 退格符演示 ---");
        System.out.println("密码：123\b\b***");
    }
}
```

## 特殊组合

### 1. `\r\n` 与 `\n\r`
- **`\r\n`**：Windows系统的行结束符（回车+换行）
- **`\n\r`**：较少使用，先换行再回车
- **`\n`**：Unix/Linux/Mac系统的行结束符

### 2. 八进制和十六进制转义
- **八进制**：`\ddd`（d为0-7的数字），如`\101`表示'A'
- **十六进制**：`\xhh`或`\uhhhh`，如`\u0041`表示'A'

## 常见问题与注意事项

1. **文件路径问题**：
   - Windows路径：`"C:\\Users\\Name\\file.txt"`
   - 错误写法：`"C:\Users\Name\file.txt"`（缺少转义）

2. **JSON字符串中的引号**：
   ```java
   String json = "{\"name\":\"张三\",\"age\":25}";
   ```

3. **正则表达式中的转义**：
   - 正则中的`.`需要转义为`\\.`
   - Java中需要写为`"\\."`

4. **`\r`和`\n`的区别**：
   - `\r`：回车，光标回到行首
   - `\n`：换行，光标移动到下一行
   - Windows：`\r\n`组合使用
   - Unix/Linux：`\n`单独使用

## 参考资料

1. [Java里\r和\n的区别](https://blog.csdn.net/ShiMengRan107/article/details/76923090)
2. [解析java中的\r、\n、\r\n、\n\r的区别](https://blog.51cto.com/u_14233037/5824468)
3. [Java概述——Java转义字符](https://blog.csdn.net/weixin_43763859/article/details/118080288)
4. [Oracle官方文档 - 转义序列](https://docs.oracle.com/javase/specs/jls/se17/html/jls-3.html#jls-3.10.6)
