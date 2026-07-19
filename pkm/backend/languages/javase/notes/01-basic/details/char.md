# 字符型变量

## 字符编码
* **ASCII表**：[在线查看](https://www.runoob.com/w3cnote/ascii.html)
* **Unicode转换**：[在线工具](https://tool.chinaz.com/Tools/Unicode.aspx)


## 字符表示方式
```java
// 字符字面量
char a = 'a';

// ASCII码值
char b = 97;  // 等价于 'a'

// 验证相等性
System.out.println(a == b);  // true

// 获取字符的ASCII码
System.out.println((int) a);  // 97

// 输出字符
System.out.println(b);  // a
```


## 转义字符
允许使用转义字符：

```java
char newline = '\n';
char tab = '\t';
char backslash = '\\';
char quote = '\"';
```


## 字符运算
```java
// 字符参与数值运算
System.out.println('a' + 10);  // 97 + 10 = 107

// 数值转字符
System.out.println((char) 21333);  // 输出：单

// 数值转字符
int radix1 = 10;  // 十进制
int value_int1 = 6;  // 6变成'6'
char value_char1 = Character.forDigit(value_int1 , radix1); 
System.out.println(value_char1);

int radix2 = 16;  // 十六进制  
int value_int2 = 12;  // 12变成'c'  
char value_char2 = Character.forDigit(value_int2 , radix2);  
System.out.println(value_char2);
```


## 存储原理
字符在计算机内部的存储过程：

1. **存储**：`'a'` → 97 → 二进制 `01100001`
2. **读取**：二进制 `01100001` → 97 → `'a'`
