# 基本算术运算符
- **加法**：`+`
- **减法**：`-`
- **乘法**：`*`
- **除法**：`/`
- **取余**：`%`
- **自增**：`++`
- **自减**：`--`

## 加号的妙用
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

👉 更多案例：[operator-plus](operator-plus.md)

## 除法运算细节
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


## 取余运算
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


## 自增/自减运算符
```java
int i = 1;
i = i++;  // 结果：i = 1

int j = 1;
j = ++j;  // 结果：j = 2
```

两个原料：

- **`i = 100`的执行步骤**：(原料1：赋值)
    1. `temp = 100;`
    2. `i = temp;`

- **`++`的执行步骤**：（原料2：自增自减）
    1. `i = i + 1;`

把原料拼在一起：

- **`i = i++` 的执行步骤**：
    1. `temp = i;`      // temp = 1
    2. `i = i + 1;`     // i = 2
    3. `i = temp;`      // i = 1

- **`j = ++j` 的执行步骤**：
    1. `j = j + 1;`     // j = 2
    2. `temp = j;`      // temp = 2
    3. `j = temp;`      // j = 2

**参考资料**：[自增运算符详细讲解](https://www.bilibili.com/video/BV1a5411y77c?p=52)
