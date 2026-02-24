# Java运算符

![java-basic-operator.excalidraw|1000](../../assets/java-basic-operator.excalidraw.md)

---

## 运算符分类概览

- **算术运算符**（数学运算）：`+ - * / % ++ --`
- **关系运算符**（比较运算）：`== != < > <= >= instanceof`
- **逻辑运算符**（布尔运算）：`& | ^ ! && ||`
- **位运算符**（二进制运算）：`& | ^ ~ << >> >>>`
- **赋值运算符**（赋值运算）：`= += -= *= /= %= &= |= ^= <<= >>= >>>=`
- **三元运算符**（条件运算）：`? :`

### 基本算术运算符
- **加法**：`+`
- **减法**：`-`
- **乘法**：`*`
- **除法**：`/`
- **取余**：`%`
- **自增**：`++`
- **自减**：`--`

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

### 除法运算细节

除法取整
```java
// 整数除法：结果取整
double n1 = 10 / 3;      // 3.0（整数除法，结果取整）

// 浮点数除法：保留小数
double n2 = 10.0 / 3;    // 3.3333333333333335
double n3 = 10 / 3.0;    // 3.3333333333333335
double n4 = (double)10 / 3; // 3.3333333333333335
```

除0的情况，当浮点数除以 0 的时候，结果为 Infinity 或者 NaN。当整数除以 0 的时候（`10 / 0`），会抛出异常。
```java
System.out.println(10.0 / 0.0); // Infinity 
System.out.println(0.0 / 0.0); // NaN
```

### 取余运算
```java
System.out.println(10 % 3);    // 1
System.out.println(-10 % 3);   // -1
System.out.println(10 % -3);   // 1
System.out.println(-10 % -3);  // -1
System.out.println(-10.5 % 3); // -1.5
```

**取余运算原理**：Java中取余的本质公式：a % b = a - a / b * b

**记忆技巧**：
1. `n % (±m)` 结果相同
2. `(±n) % m` 等价于 `±(n % m)`
3. 浮点数取余不会强制转换为整数

### 自增/自减运算符
```java
int i = 1;
i = i++;  // 结果：i = 1

int j = 1;
j = ++j;  // 结果：j = 2
```

两个原料：
* **`i = 100`的执行步骤**：(原料1：赋值)
	1. `temp = 100;`
	2. `i = temp;`
* **`++`的执行步骤**：（原料2：自增自减）
	1. `i = i + 1;`

把原料拼在一起：
* **`i = i++` 的执行步骤**：
	1. `temp = i;`      // temp = 1
	2. `i = i + 1;`     // i = 2
	3. `i = temp;`      // i = 1

* **`j = ++j` 的执行步骤**：
	1. `j = j + 1;`     // j = 2
	2. `temp = j;`      // temp = 2
	3. `j = temp;`      // j = 2

**参考资料**：[自增运算符详细讲解](https://www.bilibili.com/video/BV1a5411y77c?p=52)

---

## 关系运算符

### 基本关系运算符
- **等于**：`==`
- **不等于**：`!=`
- **小于**：`<`
- **大于**：`>`
- **小于等于**：`<=`
- **大于等于**：`>=`

### 类型检查运算符
- **类型判断**：`instanceof`
```java
String str = "Hello";
System.out.println(str instanceof String);  // true
System.out.println(str instanceof Object);  // true
```

---

## 逻辑运算符

### 逻辑运算符分类

> `&&`和`||`和C语言一样，就会短路。`$`和`|`就不会短路。

- **逻辑与** `&`：非短路，两边都计算
- **逻辑或** `|`：非短路，两边都计算  
- **逻辑异或** `^`：相同为false，不同为true
- **逻辑非** `!`：取反
- **短路与** `&&`：左边为false则短路
- **短路或** `||`：左边为true则短路

### 短路 vs 非短路
```java
public class LogicDemo {
    public static boolean condition1() {
        System.out.println("condition1执行");
        return true;
    }
    
    public static boolean condition2() {
        System.out.println("condition2执行");
        return false;
    }
    
    public static void main(String[] args) {
        System.out.println("=== 非短路与 & ===");
        if (condition1() & condition2()) {
            // 两个条件都会执行
        }
        
        System.out.println("\n=== 短路与 && ===");
        if (condition1() && condition2()) {
            // condition2可能不会执行
        }
    }
}
```

### 逻辑运算练习
```java
// 练习1：非短路与
int x = 5, y = 5;
if (x++ == 6 & ++y == 6) {  // x=5(比较),x=6; y=6(比较)
    x = 11;
}
System.out.println("x=" + x + ", y=" + y);  // x=6, y=6

// 练习2：短路与
int x = 5, y = 5;
if (x++ == 6 && ++y == 6) {  // x=5(比较),x=6; y不变（短路）
    x = 11;
}
System.out.println("x=" + x + ", y=" + y);  // x=6, y=5

// 练习3：非短路或
int x = 5, y = 5;
if (x++ == 5 | ++y == 5) {  // x=5(比较),x=6; y=6(比较)
    x = 11;
}
System.out.println("x=" + x + ", y=" + y);  // x=11, y=6

// 练习4：短路或
int x = 5, y = 5;
if (x++ == 5 || ++y == 5) {  // x=5(比较),x=6; y不变（短路）
    x = 11;
}
System.out.println("x=" + x + ", y=" + y);  // x=11, y=5

// 练习5：综合练习
boolean x = true;
boolean y = false;
short z = 46;
if ((z++ == 46) && (y = true)) z++;  // z=47, y=true, z=48
if ((x = false) || (++z == 49)) z++;  // x=false, z=49, z=50
System.out.println("z=" + z);  // z=50
```

### 异或运算
```java
// 异或：相同为false，不同为true
System.out.println(true ^ true);    // false
System.out.println(true ^ false);   // true
System.out.println(false ^ true);   // true
System.out.println(false ^ false);  // false
```

---

## 赋值运算符

### 基本赋值运算符
- **简单赋值**：`=`
- **复合赋值**：`+= -= *= /= %= &= |= ^= <<= >>= >>>=`

### 复合赋值特性
```java
byte a = 2;

// 正确：复合赋值包含隐式类型转换
a += 2;  // 等价于 a = (byte)(a + 2)

// 错误：需要显式类型转换
// a = a + 2;

// 正确：显式类型转换
a = (byte)(a + 2);
```

### 三元运算符（条件运算符）

条件表达式 ? 表达式1 : 表达式2

### 优先级示例
```java
int result = 5 + 3 * 2;        // 11（乘法优先）
boolean flag = 5 > 3 && 2 < 4; // true（比较优先于逻辑与）
int value = a > b ? a : b + 1; // 相当于 a > b ? a : (b + 1)
```

**参考资料**：[Java运算符优先级详解](https://www.cnblogs.com/lvlp/p/16783709.html)

---

## 总结与最佳实践

### 1. 运算符选择建议
- **算术运算**：注意整数除法和浮点数除法的区别
- **逻辑运算**：优先使用短路运算符`&&`和`||`提高效率
- **位运算**：适用于标志位操作、简单加密等场景
- **三元运算符**：简化简单的if-else语句，但注意类型转换

### 2. 常见陷阱
- **自增/自减**：注意前自增和后自增的区别
- **浮点数比较**：避免直接使用`==`比较浮点数
- **类型转换**：复合赋值包含隐式转换，普通赋值需要显式转换
- **三元运算符**：可能发生意外的类型提升

### 3. 调试技巧
```java
// 使用括号明确优先级
int result = (a + b) * c;  // 明确表达意图

// 分步计算复杂表达式
int temp1 = a * b;
int temp2 = c / d;
int finalResult = temp1 + temp2;

// 使用System.out.println调试
System.out.println("a=" + a + ", b=" + b);
System.out.println("中间结果: " + (a + b));
```

### 4. 性能考虑
- 短路运算符`&&`和`||`可以提高性能
- 位运算通常比算术运算更快
- 避免在循环条件中使用复杂表达式

通过掌握这些运算符的特性和优先级，可以编写出更高效、更清晰的Java代码。