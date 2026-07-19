# 浮点型变量

## 表示形式
| 类型 | 空间 | 范围 | 后缀 |
|------|------|------|------|
| `float` | 4B | ±3.403E38 | `F` 或 `f` |
| `double` | 8B | ±1.798E308 | `D` 或 `d`（可省略） |

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

```java
double a = 5.12;      // 标准表示
float b = 512.0F;     // float类型
double c = .512;      // 等价于0.512（省略前导0）
double d = 5.12e2;    // 科学计数法：5.12 × 10² = 512.0
double e = 5.12e-2;   // 科学计数法：5.12 × 10⁻² = 0.0512
```

```java
double a = 2.123456789;   // 保持精度：2.123456789
float b = 2.123456789F;   // 精度损失：2.1234567
```


## IEEE754标准
```java
public class Ieee754Demo {
    public static void main(String[] args) {
        float a = 0.1f;
        float b = 0.2f;
        float c = a + b;
        
        System.out.println("a = " + a);
        System.out.println("b = " + b);
        System.out.println("c = a + b = " + c);
        
        double x = 1.0 / 0.0;
        double y = -1.0 / 0.0;
        double z = 0.0 / 0.0;
        
        System.out.println("x = 1.0 / 0.0 = " + x);
        System.out.println("y = -1.0 / 0.0 = " + y);
        System.out.println("z = 0.0 / 0.0 = " + z);
    }
}
```

```java
a = 0.1
b = 0.2
c = a + b = 0.3
x = 1.0 / 0.0 = Infinity
y = -1.0 / 0.0 = -Infinity
z = 0.0 / 0.0 = NaN
```


## 浮点数陷阱
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

double 同样不适合用于精确的数值，比如说金额，可以使用[BigInteger和BigDecimal](../04-utils/BigIntegerBigDecimal.md)

在实际开发中，如果不是特别大的金额（精确到 0.01 元，也就是一分钱），一般建议乘以 100 转成整型进行处理。


## 面试题：float 怎么表示⼩数
是通过 IEEE 754 标准的单精度浮点数格式来表示
$$V = (-1)^S\cdot M \cdot 2^E$$

* S：符号位，0 代表正数，1 代表负数；
* M：尾数部分，⽤于表示数值的精度；⽐如说 ${1.25 * 2^2}$；1.25 就是尾数；
* R：基数，⼗进制中的基数是 10，⼆进制中的基数是 2；
* E：指数部分，例如 $10^{-1}$ 中的 -1 就是指数。

1. 符号位（Sign bit）：1 位
2. 指数部分（Exponent）：10 位
3. 尾数部分（Mantissa，或 Fraction）：21 位

比如25.125(D) = 11001.001(B) = 1.1001001 * 2^4(B)

* 符号位就是 0
* 指数部分：0000000100
* 尾数部分：000000000000001001001
