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
* 案例：[escape-character-example](../../details/escape-character-example.md)


## 常见问题与注意事项
1. `\r\n` 与 `\n\r`
- **`\r\n`**：Windows系统的行结束符（回车+换行）
- **`\n\r`**：较少使用，先换行再回车
- **`\n`**：Unix/Linux/Mac系统的行结束符

2. 八进制和十六进制转义
- **八进制**：`\ddd`（d为0-7的数字），如`\101`表示'A'
- **十六进制**：`\xhh`或`\uhhhh`，如`\u0041`表示'A'

3. 文件路径问题：
   - Windows路径：`"C:\\Users\\Name\\file.txt"`
   - 错误写法：`"C:\Users\Name\file.txt"`（缺少转义）

4. JSON字符串中的引号：
   ```java
   String json = "{\"name\":\"张三\",\"age\":25}";
   ```

5. 正则表达式中的转义：
   - 正则中的`.`需要转义为`\\.`
   - Java中需要写为`"\\."`


## 参考资料
1. [Java里\r和\n的区别](https://blog.csdn.net/ShiMengRan107/article/details/76923090)
2. [解析java中的\r、\n、\r\n、\n\r的区别](https://blog.51cto.com/u_14233037/5824468)
3. [Java概述——Java转义字符](https://blog.csdn.net/weixin_43763859/article/details/118080288)
4. [Oracle官方文档 - 转义序列](https://docs.oracle.com/javase/specs/jls/se17/html/jls-3.html#jls-3.10.6)
