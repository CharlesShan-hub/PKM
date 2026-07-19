# 整型变量

## 类型范围表
| 类型 | 空间 | 范围 | 数学表示 |
|------|------|------|----------|
| `byte` | 1B | -128 ~ 127 | -2⁷ ~ 2⁷-1 |
| `short` | 2B | -32,768 ~ 32,767 | -2¹⁵ ~ 2¹⁵-1 |
| `int` | 4B | -2,147,483,648 ~ 2,147,483,647 | -2³¹ ~ 2³¹-1 |
| `long` | 8B | -9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807 | -2⁶³ ~ 2⁶³-1 |


## 字面量规则
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


## 面试题：Integer.MAX_VALUE + 1
Integer是包装类（[WrapperClass](../04-utils/WrapperClass.md)），里边包含了一些常量和方法，`Integer.MAX_VALUE`是int最大值，+1会溢出，变成`Integer.MIN_VALUE`。

```java
int maxValue = Integer.MAX_VALUE;
System.out.println("Integer.MAX_VALUE = " + maxValue); 
// Integer.MAX_VALUE = 2147483647
System.out.println("Integer.MAX_VALUE + 1 = " + (maxValue + 1)); 
// Integer.MAX_VALUE + 1 = -2147483648

// ⽤⼆进制来表示最⼤值和最⼩值

System.out.println("Integer.MAX_VALUE in binary: " + Integer.toBinaryString(maxValue));
// Integer.MAX_VALUE in binary: 1111111111111111111111111111111

System.out.println("Integer.MIN_VALUE in binary: " +
Integer.toBinaryString(Integer.MIN_VALUE)); 
// Integer.MIN_VALUE in binary: 10000000000000000000000000000000
```
