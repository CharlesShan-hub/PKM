
# 转移字符案例
## 单个案例

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


## 综合案例
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