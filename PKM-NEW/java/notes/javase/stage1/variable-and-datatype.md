# 变量与数据类型

---

## 变量基础

### 变量概念
- **三要素**：类型、名称、值
- **变量声明**：定义变量的类型和名称
- **变量赋值**：为变量赋予具体的值

### 作用域规则
- 变量在一个作用域内不能重名
- Java不支持变量遮蔽（与C语言不同）

```java
public class Main {
    public static void main(String[] args) {
        int a = 1;
        {
            // 错误：不能像C语言一样遮蔽变量
            // double a = 1; 
        }
    }
}
```

---

## 数据类型分类

### 基本数据类型（8种）
| 类别 | 类型 | 大小 | 说明 |
|------|------|------|------|
| 整型 | `byte` | 1字节 | -128 ~ 127 |
| 整型 | `short` | 2字节 | -32,768 ~ 32,767 |
| 整型 | `int` | 4字节 | -2³¹ ~ 2³¹-1 |
| 整型 | `long` | 8字节 | -2⁶³ ~ 2⁶³-1 |
| 浮点型 | `float` | 4字节 | 约±3.403E38，7位小数精度 |
| 浮点型 | `double` | 8字节 | 约±1.798E308，16位小数精度 |
| 字符型 | `char` | 2字节 | Unicode字符 |
| 布尔型 | `boolean` | 1字节 | `true` 或 `false` |

**注意**：Java变量所占空间固定，与操作系统无关！

### 引用数据类型
- **类**（如 `String`）
- **接口**
- **数组**

### 字符类型比较
- **Java**：`char` 2字节（Unicode）
- **C语言**：`char` 1字节（ASCII）
- **Rust**：`char` 4字节（Unicode标量值）

---

## 运算符特性

### 加号的妙用
- **两边都是数值**：执行加法运算
  ```java
  System.out.println(1 + 2); // 输出：3
  ```

- **char参与运算**：char本质是数值
  ```java
  System.out.println('a' + 10); // 97 + 10 = 107
  ```

- **包含字符串**：执行字符串拼接
  ```java
  System.out.println("Hello" + 3); // 输出：Hello3
  ```

- **运算顺序**：从左到右
  ```java
  System.out.println(1 + 2 + "Hello"); // 输出：3Hello
  System.out.println("Hello" + 1 + 2);  // 输出：Hello12
  ```

---

## 整型变量

### 类型范围表
| 类型 | 空间 | 范围 | 数学表示 |
|------|------|------|----------|
| `byte` | 1B | -128 ~ 127 | -2⁷ ~ 2⁷-1 |
| `short` | 2B | -32,768 ~ 32,767 | -2¹⁵ ~ 2¹⁵-1 |
| `int` | 4B | -2,147,483,648 ~ 2,147,483,647 | -2³¹ ~ 2³¹-1 |
| `long` | 8B | -9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807 | -2⁶³ ~ 2⁶³-1 |

### 字面量规则
1. **默认类型**：整数字面量默认为 `int`
2. **long字面量**：需要在结尾加 `L` 或 `l`

```java
// 错误：long字面量不能直接赋值给int
// java: incompatible types: possible lossy conversion from long to int
int a = 100L;

// 正确：明确指定long类型
long b = 200L;

// 错误：超出int范围，但字面量默认为int
long c = 2147493648;  // 编译错误

// 正确：添加L后缀
long d = 2147493648L; // 编译通过
```

---

## 浮点型变量

### 类型对比
| 类型 | 空间 | 范围 | 后缀 |
|------|------|------|------|
| `float` | 4B | ±3.403E38 | `F` 或 `f` |
| `double` | 8B | ±1.798E308 | `D` 或 `d`（可省略） |

### 使用要点
1. **精度问题**：浮点数采用IEEE 754标准，尾数部分可能丢失精度
2. **默认类型**：建议使用 `double`，它是默认的浮点类型
3. **float必须加后缀**：`float` 类型字面量必须添加 `F` 或 `f`

```java
// 错误：1.1默认为double，不能直接赋值给float
float a = 1.1;

// 正确：明确指定float类型
float b = 1.2F;

// 正确：double类型（D可省略）
double c = 10.5;
double d = 10.5d;
```

### 表示形式
```java
double a = 5.12;      // 标准表示
float b = 512.0F;     // float类型
double c = .512;      // 等价于0.512（省略前导0）
double d = 5.12e2;    // 科学计数法：5.12 × 10² = 512.0
double e = 5.12e-2;   // 科学计数法：5.12 × 10⁻² = 0.0512
```

### 精度对比
```java
double a = 2.123456789;   // 保持精度：2.123456789
float b = 2.123456789F;   // 精度损失：2.1234567
```

### 浮点数陷阱
由于二进制表示的限制，某些十进制小数无法精确表示：

```java
double a = 2.7;
double b = 8.1 / 3;  // 理论值：2.7，实际值：2.6999999999999997

// 错误：直接比较浮点数
System.out.println(a == b);  // false

// 正确：使用容差比较
if (Math.abs(a - b) < 0.00001) {
    System.out.println("差值小到可以忽略");
}

// 注意：直接赋值的相同值可以相等
double c = 2.7;
System.out.println(a == c);  // true
```

double 同样不适合用于精确的数值，比如说金额，可以使用[BigInteger和BigDecimal](../stage2/BigIntegerBigDecimal.md)

在实际开发中，如果不是特别大的金额（精确到 0.01 元，也就是一分钱），一般建议乘以 100 转成整型进行处理。

---

## 字符型变量

### 字符编码
- **ASCII表**：[在线查看](https://www.runoob.com/w3cnote/ascii.html)
- **Unicode转换**：[在线工具](https://tool.chinaz.com/Tools/Unicode.aspx)

### 字符表示方式
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

### 转义字符
允许使用转义字符：
```java
char newline = '\n';
char tab = '\t';
char backslash = '\\';
char quote = '\"';
```

### 字符运算
```java
// 字符参与数值运算
System.out.println('a' + 10);  // 97 + 10 = 107

// 数值转字符
System.out.println((char) 21333);  // 输出：单
```

### 存储原理
字符在计算机内部的存储过程：
1. **存储**：`'a'` → 97 → 二进制 `01100001`
2. **读取**：二进制 `01100001` → 97 → `'a'`

---

## 布尔类型

### 基本特性
- **大小**：占用1字节
- **取值**：只能是 `true` 或 `false`
- **与C的区别**：不能用0或非零整数代替 `boolean`

```java
boolean isReady = true;
boolean isFinished = false;

// 错误：Java不支持数值到boolean的转换
// int flag = 1;
// boolean b = flag;
```

---

## 类型转换

### 自动类型转换
#### 转换方向（从小到大）

byte → short → int → long → float → double
↑
char


#### 转换规则
1. **默认转成最宽泛的类型**
   ```java
   int a = 1;
   // 错误：1.1默认为double
   float n1 = a + 1.1;
   
   // 正确：明确指定float
   float n2 = a + 1.1F;
   
   // 正确：使用double接收
   double n3 = a + 1.1;
   ```

2. **char与byte/short的特殊关系**
   ```java
   // 正确：常量在范围内可自动转换
   byte a = 97;
   
   // 错误：超出范围
   // byte b = 123456;
   
   // 正确：强制转换
   byte c = (byte) 97;
   
   // 错误：变量无法判断范围
   int temp = 97;
   // byte d = temp;
   
   // 正确：强制转换
   byte e = (byte) temp;
   
   // 正确：char可以直接保存整数常量
   char f = 97;
   
   // 错误：byte不能自动转成char
   // char g = a;
   
   // 正确：强制转换
   char h = (char) a;
   ```

3. **char与byte/short运算**
   ```java
   byte age = 20;
   byte age2 = 30;
   // age + age2 的结果是int类型
   int sum = age + age2;
   ```

4. **boolean不参与转换**
   ```java
   boolean flag = true;
   // 错误：boolean不能转换为其他类型
   // int num = flag;
   ```

### 强制类型转换
通过类型转换运算符 `(类型)`：
```java
double d = 3.14;
int i = (int) d;  // i = 3（截断小数部分）
```

### 基本类型与String的转换

#### 基本类型 → String
```java
int num = 123;
String s = num + "";  // "123"
```

#### String → 基本类型
使用[WrapperClass](../stage2/WrapperClass.md)的解析方法：
```java
String s = "123";

int n1 = Integer.parseInt(s);
double n2 = Double.parseDouble(s);
float n3 = Float.parseFloat(s);
long n4 = Long.parseLong(s);
byte n5 = Byte.parseByte(s);
boolean n6 = Boolean.parseBoolean("true");
short n7 = Short.parseShort(s);
```

#### char → 基本类型
使用`Character`类（也是包装类）的方法：
```java
int a = Character.getNumericValue('1');
int b = Character.digit('1', 10);
```

#### 字符串操作
```java
// 提取字符串中的字符
String s = "123";
char c = s.charAt(0);  // '1'

// 字符串相等比较（推荐方式）
String name = "林黛玉";
System.out.println("林黛玉".equals(name));  // 更好：避免空指针
System.out.println(name.equals("林黛玉"));   // 可能引发空指针异常
```

---

## 总结要点

1. **变量命名**：作用域内不能重名，Java不支持变量遮蔽
2. **类型选择**：
   - 整数默认用 `int`，大数用 `long`
   - 浮点数默认用 `double`，`float` 必须加 `F` 后缀
3. **类型转换**：
   - 小范围类型可自动转大范围类型
   - 大范围转小范围需要强制转换
   - `boolean` 不参与类型转换
4. **浮点数陷阱**：避免直接比较，使用容差法
5. **字符串操作**：使用 `equals()` 比较字符串，注意空指针问题
6. **字符特性**：`char` 可参与数值运算，本质是Unicode编码