# 本章内容概要

- 标识符（掌握）
- 关键字（理解）
- 字面量（理解）
- 变量（掌握）
- 二进制（掌握）
- 八进制与十六进制（了解）f
- 原码反码补码（掌握）
- 数据类型（掌握）
- 运算符（掌握）
- 控制语句（掌握）
- 方法、方法重载、方法递归（掌握）
- package 和 import（掌握）



# 本章内容详解



<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="QJn8S" class="ne-image">

## 二进制（掌握）

计算机底层只能识别二进制。计算机底层只识别二进制是因为计算机内部的电子元件只能识别两种状态，即开和关，或者高电平和低电平。二进制正好可以用两种状态来表示数字和字符，因此成为了计算机最基本的表示方法。在计算机内部，所有的数据都被转化为二进制形式进行处理和存储。虽然计算机可以通过不同的编程语言和程序来处理不同的数据类型和格式，但最终都需要将其转化为二进制形式才能被计算机底层识别和处理。

### 什么是二进制

十进制：满十进一。

二进制：满二进一。

| 十进制 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 二进制 | 1 | 10 | 11 | 100 | 101 | 110 | 111 | 1000 | 1001 | 1010 |
| | 2 的零次方 | 2 的一次方 | | 2 的二次方 | | | | 2 的三次方 | | |

### 二进制和十进制的转换

#### 十进制转换为二进制

要将一个十进制数转换为二进制数，可以使用以下步骤：

1. 将十进制数除以 2，得到商和余数。
2. 将余数记录下来，然后将商作为新的十进制数，重复步骤 1，直到商为 0 为止。
3. 将记录的余数从下往上排列，得到的就是对应的二进制数。

例如，将十进制数 27 转换为二进制数：

27 ÷ 2 = 13 ... 1  
13 ÷ 2 = 6 ... 1  
6 ÷ 2 = 3 ... 0  
3 ÷ 2 = 1 ... 1  
1 ÷ 2 = 0 ... 1

所以 27 的二进制数为 11011。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="TOUaO" class="ne-image">

#### 二进制转换为十进制

将二进制数每一位权值找出来，然后每个权值与对应二进制位相乘，最后将它们相加，即可得到十进制数。

什么是权值？

在二进制中，**权值指的是每个位所代表的数值大小**，即二进制中每个位的位置所代表的数值大小。例如，在二进制数 1101 中，最高位的权值为 8，次高位的权值为 4，第三位的权值为 2，最低位的权值为 1。

例如，二进制数 1101 转换为十进制数的计算过程如下：

1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 8 + 4 + 0 + 1 = 13

因此，二进制数 1101 转换为十进制数为 13。

#### 练习一下

将以下十进制的数字转换为二进制：

- 243：11110011
- 165
- 89

将以下二进制的数字转换为十进制：

- 101010
- 111100
- 011001

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="AtBaK" class="ne-image">

## 八进制与十六进制（了解）

### 什么是八进制

八进制：满八进一。

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1684908204559-91d1813e-e0f3-4338-b649-20b8e8b7d34a.png" width="1259" title="" crop="0,0,1,1" id="u1cfb14bd" class="ne-image">

### 八进制与十进制的转换

#### 十进制转换为八进制

将十进制数除以 8，直到商为 0，然后将每次的余数从下往上排列即为该十进制数的八进制表示。

例如，将十进制数 27 转换为八进制：

27 ÷ 8 = 3 … 3  
3 ÷ 8 = 0 … 3

所以 27 的八进制表示为 33。

#### 八进制转换为十进制

八进制转换为十进制的方法如下：

1. 将八进制数的每一位按权展开，权值分别为 8 的 0 次方、8 的 1 次方、8 的 2 次方，以此类推。
2. 将每一位的值乘以对应的权值，然后将所有结果相加。

例如，将八进制数 346 转换为十进制数：

3×8^2 + 4×8^1 + 6×8^0 = 3×64 + 4×8 + 6×1 = 230

因此，八进制数 346 转换为十进制数为 230。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="sDiBQ" class="ne-image">

### 什么是十六进制

满十六进一。

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1684908662850-c5f95463-a51b-4c8e-842a-0e9365501b41.png" width="1261" title="" crop="0,0,1,1" id="u58161d01" class="ne-image">

### 十六进制与十进制的转换

#### 十进制转换为十六进制

1. 首先将十进制数除以 16，得到商和余数。
2. 将余数转换为对应的十六进制数，如果余数小于 10，则直接写下来，否则用 A、B、C、D、E、F 表示 10、11、12、13、14、15。
3. 将商作为新的十进制数，重复步骤 1 和 2，直到商为 0 为止。
4. 将每一步得到的十六进制数倒序排列，即为最终的十六进制数。

例如，将十进制数 255 转换为十六进制数：

1. 255 ÷ 16 = 15 余 15
2. 余数 15 对应的十六进制数为 F，所以最后一位为 F。
3. 15 ÷ 16 = 0 余 15
4. 余数 15 对应的十六进制数为 F，所以第二位为 F。
5. 最终的十六进制数为 FF。

#### 十六进制转换为十进制

将十六进制转换为十进制的方法是将每一位的十六进制数值乘以对应的权值，再将各位的结果相加。

例如，将十六进制数 ABCD 转换为十进制数：

1. 将 A、B、C、D 分别转换为对应的十进制数值，即 10、11、12、13。
2. 根据十六进制的权值规则，从右往左依次乘以 16 的 0 次方、1 次方、2 次方、3 次方，即 1、16、256、4096。
3. 将各位的乘积相加，即：13×1 + 12×16 + 11×256 + 10×4096 = 43981。
4. 所以，十六进制数 ABCD 转换为十进制数为 43981。

另一种简便的方法是，将十六进制数中的每一位转换为 4 位的二进制数，再将这些二进制数转换为十进制数，最后将各位的结果相加。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="XGEoO" class="ne-image">

### 二进制与十六进制的转换

#### 二进制转换为十六进制

二进制转换为十六进制的方法如下：

1. 将二进制数从右往左每四位一组，不足四位则在左侧补 0，得到若干个四位二进制数。
2. 将每个四位二进制数转换为对应的十六进制数，可以使用下表进行转换：

| 二进制数 | 十六进制数 |
| --- | --- |
| 0000 | 0 |
| 0001 | 1 |
| 0010 | 2 |
| 0011 | 3 |
| 0100 | 4 |
| 0101 | 5 |
| 0110 | 6 |
| 0111 | 7 |
| 1000 | 8 |
| 1001 | 9 |
| 1010 | A |
| 1011 | B |
| 1100 | C |
| 1101 | D |
| 1110 | E |
| 1111 | F |

3. 将每个四位二进制数对应的十六进制数按照从左往右的顺序排列，得到最终的十六进制数。

例如，将二进制数 1101011010111011 转换为十六进制数：

1. 从右往左每四位一组，得到 1101 0110 1011 1011。
2. 将每个四位二进制数转换为对应的十六进制数，得到 D 6 B B。
3. 将每个四位二进制数对应的十六进制数按照从左往右的顺序排列，得到最终的十六进制数：D6BB。

#### 十六进制转换为二进制

将每个十六进制数位转换为四位二进制数即可。

例如：将十六进制数 AF 转换为二进制数。

A 对应的二进制数为 1010，F 对应的二进制数为 1111，因此 AF 对应的二进制数为 10101111。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="Gg080" class="ne-image">

## 原码反码补码（掌握）

### byte 与 bit

byte（字节）是计算机存储和处理数据的基本单位，通常由 8 个比特（bit）组成。每个比特（bit）是计算机中最小的表示单位，只能存储 0 或 1 两个状态。因此，一个字节（byte）可以存储 8 个比特（bit）的数据。

两者之间的关系是，1 byte = 8 bit，即 8 个比特（bit）组成一个字节（byte）。

在计算机中，数据通常以字节（byte）为单位进行存储和传输，而比特（bit）则是用来表示数据的最小单位。

1KB = 1024byte  
1MB = 1024KB  
1GB = 1024MB  
1TB = 1024GB

### 原码反码补码

原码、反码和补码都是计算机二进制的表示方式。

**<font style="color:#DF2A3F;">计算机在底层是采用补码形式表示数据的。（为什么采用补码？感兴趣的可以研究一下。其实研究这个没啥用，记住就行了，够程序员用就行了）</font>**

在二进制当中，最高位表示符号位，0 表示正数，1 表示负数。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="tvltT" class="ne-image">

#### 正数的原码反码补码

正数的原码、反码和补码都是相同的。

例如，一个十进制数 `+5` 的二进制原码为 00000101，反码为 00000101，补码为 00000101。

原码：将正数的二进制表示直接写下来，最高位为 0。

反码：正数的反码就是其原码本身。

补码：正数的补码也就是其原码本身。

#### 127 的原码反码补码

127 的原码为 01111111，其反码和补码均与原码相同。

#### 负数的原码反码补码

**<font style="color:#000000;">负数的原码运算规则：</font>** **<font style="color:#DF2A3F;">将绝对值转换为二进制后，最高位改为 1。</font>**

-5 的原码：10000101  
-5 的反码：11111010（原则是：以原码作为参考，符号位不变，其他位取反。）  
-5 的补码：11111011（原则是：以反码作为参考，符号位不变，加 1）

#### -128 的原码反码补码

-128 的原码为 10000000，其反码为 11111111，补码为 10000000。注意，对于 -128 这个特殊的数，它的补码和原码相同。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="vk7U4" class="ne-image">

### 已知负数的补码怎么得到原码

虽然计算机底层是采用补码的形式存储的，但最终显示给人类的时候是以原码的形式显示的。所以大家需要具备这个能力！！！

将负数的补码形式**<font style="color:#DF2A3F;">除符号位外的所有位按位取反，再加 1</font>**即可得到原码。

已知补码：10000001  
它的原码是：11111111  
结果是：-127

通过这个可以得出，对于一个字节来说，最大值 127，最小值 -128。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="QkXMI" class="ne-image">

## 数据类型（掌握）

数据类型：决定了变量在内存中的空间大小。不同的数据类型，在内存中占用空间大小不同。

为什么需要学习数据类型？为了定义变量。

---

### Java 数据类型概述

Java 语言包括两种数据类型：

- 基本数据类型
  - 整数类型：包括 **<font style="color:#DF2A3F;">byte</font>**、**<font style="color:#DF2A3F;">short</font>**、**<font style="color:#DF2A3F;">int</font>** 和 **<font style="color:#DF2A3F;">long</font>** 四种类型，用于表示整数。
  - 浮点类型：包括 **<font style="color:#DF2A3F;">float</font>** 和 **<font style="color:#DF2A3F;">double</font>** 两种类型，用于表示带小数点的数值。
  - 布尔类型：**<font style="color:#DF2A3F;">boolean</font>** 类型，只有 true 和 false 两个值，用于表示逻辑值。
  - 字符类型：**<font style="color:#DF2A3F;">char</font>** 类型，用于表示单个字符，它是基于 Unicode 编码的。
- 引用数据类型
  - 类、接口、数组、枚举等。（或者你也可以这样记：除了 8 种基本数据类型之外，其他都是引用数据类型，**<font style="color:#DF2A3F;">包括 String</font>**。）

<u>现阶段重点研究基本数据类型，以后再说引用数据类型。</u>

下面详细介绍一下每种类型的特点和使用方法：

1. 整数类型：
   - byte 类型：占用 1 个字节，范围是 -128 到 127，常用于存储小整数。<font style="color:#DF2A3F;">（byte 类型的 1：00000001）</font>
   - short 类型：占用 2 个字节，范围是 -32768 到 32767，常用于存储中等大小的整数。<font style="color:#DF2A3F;">（short 类型的 1：00000000 00000001）</font>
   - int 类型：占用 4 个字节，范围是 -2147483648 到 2147483647，是 Java 中最常用的整数类型。
   - long 类型：占用 8 个字节，范围是 -9223372036854775808 到 9223372036854775807，用于存储极大或极小的整数。

**<font style="color:#117CEE;">为什么设计出这么多整数？目的是合适的数据选择合适的类型，可以节省空间，但实际开发中不必斤斤计较，大部分采用 int。另外，如果数据过大，超过了 long，可以使用 BigInteger，它就不是基本数据类型了，属于引用数据类型。后面再说。</font>**

2. 浮点类型：
   - float 类型：占用 4 个字节，范围是 1.4E-45 到 3.4028235E38，精度为 7 位小数，常用于科学计算和工程计算。
   - double 类型：占用 8 个字节，范围是 4.9E-324 到 1.7976931348623157E308，精度为 15 位小数，是 Java 中最常用的浮点类型。

（**<font style="color:#2F4BDA;">如果超出了 double，可以使用 BigDecimal，同样它也是一种引用数据类型。</font>**）

3. 布尔类型：
   - boolean 类型：只有两个值，true 和 false，用于表示逻辑值，例如判断语句、循环语句等。

4. 字符类型：
   - char 类型：占用 2 个字节，用于表示单个字符，例如 'A'、'B'、'C' 等，也可以表示 Unicode 编码中的任意字符。

这是一个直观的列表：

| **数据类型** | **占用字节数** | **取值范围** | **具体取值范围** | **默认值** |
| --- | --- | --- | --- | --- |
| byte | 1 | -2<sup>7</sup> ~ 2<sup>7</sup>-1 | -128 ~ 127 | 0 |
| short | 2 | -2<sup>15</sup> ~ 2<sup>15</sup>-1 | -32768 ~ 32767 | 0 |
| int | 4 | -2<sup>31</sup> ~ 2<sup>31</sup>-1 | -2147483648 ~ 2147483647 | 0 |
| long | 8 | -2<sup>63</sup> ~ 2<sup>63</sup>-1 | -9223372036854775808 ~ 9223372036854775807 | 0L |
| float | 4 | 1.4E-45 ~ 3.4028235E38 | 1.4E-45 ~ 3.4028235E38 | 0.0f |
| double | 8 | 4.9E-324 ~ 1.7976931348623157E308 | 4.9E-324 ~ 1.7976931348623157E308 | 0.0d |
| boolean | 1 | true / false | true / false | false |
| char | 2 | 0 ~ 2<sup>16</sup>-1 | 0 ~ 65535 | '\u0000' |

关于默认值：Java 语言中变量必须先声明，再赋值，才能使用。对于局部变量来说必须手动赋值，而对于成员变量来说，如果没有手动赋值，系统会自动赋默认值。例如：

```java
public class DefaultValue {
    // 成员变量有系统默认值
    static int i;

    public static void main(String[] args){
        System.out.println(i); // 0

        // 成员变量没有系统默认值
        int k;
        System.out.println(k); // 编译报错
    }
}
```

注意：对于引用数据类型来说，默认值 null，例如：

```java
public class DefaultValue {
    static String name;

    public static void main(String[] args){
        // String 是引用数据类型。
        System.out.println(name); // null
    }
}
```

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="kDlPb" class="ne-image">

### 整数型详解

#### 整数型字面量的四种表示形式

Java 中整数型字面量有以下四种表示形式：

1. 十进制表示法：以数字 0-9 组成的常数，默认为十进制表示法。
   例如：int a = 10;
2. 二进制表示法：以 0b 或 0B 开头的常数，由 0 和 1 组合而成。
   例如：int b = 0b101;
3. 八进制表示法：以 0 开头的常数，由数字 0-7 组成。
   例如：int c = 012;
4. 十六进制表示法：以 0x 或 0X 开头的常数，由 0-9 和 A-F（大小写均可）组成。
   例如：int d = 0x1F;

#### 整数型字面量默认当做 int 处理

Java 中整数型字面量默认被当做 int 类型来处理，**<font style="color:#DF2A3F;">如果要表示 long 类型的整数，需要在字面量后面加上 'L' 或 'l' 标记</font>**。例如，下面是表示 int 和 long 类型整数的字面量的示例：

```java
int x = 10;   // 10 是一个 int 类型的字面量
long y = 10L; // 10L 是一个 long 类型的字面量
```

需要注意的是，大小写字母 'L' 和 'l' 的使用没有区别，但是容易被误解为数字 1，因此建议使用大写字母。

请看以下代码有什么问题吗？

```java
long z = 2147483648;
```

编译报错，原因是 2147483648 被当做 int 类型处理，而该数字本身已经超出了 int 最大值，如何修改？

```java
long z = 2147483648L;
```

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="aLeT5" class="ne-image">

#### 自动类型转换

<img src="https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1685069585779-fa67f45b-7462-4a35-a91f-ae398e79f432.jpeg" width="536" title="" crop="0,0,1,1" id="u2896ab28" class="ne-image">

在 Java 中，对于基本数据类型来说，小容量是可以直接赋值给大容量的，这被称为自动类型转换。对于数字类型来说大小关系为：byte < short < int < long < float < double。

下面是一些自动类型转换的示例：

```java
double a = 10;     // 将 int 类型自动转换为 double 类型
int b = 100;
float c = b;       // 将 int 类型自动转换为 float 类型
long d = b;        // 将 int 类型自动转换为 long 类型
byte e = 10;
short f = e;       // 将 byte 类型自动转换为 short 类型
```

需要注意的是，自动类型转换只适用于基本数据类型之间的转换。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="QSYuB" class="ne-image">

#### 强制类型转换

强制类型转换：Java 中大容量是无法直接转换成小容量的。因为这种操作**<font style="color:#DF2A3F;">可能</font>**会导致精度损失，所以这种行为交给了程序员来决定，当然这种后果自然是程序员自己去承担。因此在代码中需要程序员自己亲手加上强制类型转换符，程序才能编译通过。

以下程序编译器就会报错：

```java
int num = 10L;
```

解决方案两个：要么把 L 去掉，要么使用强制类型转换符，例如：

```java
int num = (int)10L;
```

这样编译器就能编译通过了。

强制类型转换时，底层二进制是如何变化的？**<font style="color:#DF2A3F;">原则：砍掉左侧多余的二进制</font>**。例如以上程序的二进制变化是这样的：

long 类型的 10 对应的二进制：00000000 00000000 00000000 00000000 00000000 00000000 00000000 00001010

强制转换为 int 类型的 10 是这样的：00000000 00000000 00000000 00001010

因此，强制类型转换时，精度可能会损失，也可能不会损失，这要看具体的数据是否真正的超出了强转后的类型的取值范围。如下图：水可能溢出，也可能不会溢出，这要看真实存放的水有多少！！！

<img src="https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1685070043987-1dc39f31-20a2-4ccd-98d5-a162fcb3f02f.jpeg" width="676" title="" crop="0,0,1,1" id="udaab356a" class="ne-image">

如果你理解了强制类型转换，那么下面这个程序的执行结果可以推算出来吗？

```java
byte b = (byte)150;
```

int 类型的 150 的补码（150 是正数：原码反码补码一样）：00000000 00000000 00000000 10010110

强转砍掉前三个多出的字节，结果是：10010110（这个是最终存储在计算机中的，注意：存储在计算机中的是补码）

将以上补码 10010110 推算出原码：11101010（结果是：-106）

因此 int 类型的 150 强转为 byte 类型之后，结果是 -106

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="fU9hE" class="ne-image">

#### 当整数字面量没有超出 byte 的范围

在 Java 中有这样一个规定，当整数型字面量没有超出 byte 的范围：可以直接赋值给 byte 类型的变量。

```java
byte b = 127; // 这是允许的
```

很显然，这是一种编译优化。同时也是为了方便程序员写代码。

如果超出了范围，例如：

```java
byte b = 128; // 编译报错
```

这样就会报错，需要做强制类型转换，例如：

```java
byte b = (byte)128;
```

它的执行结果你知道吗？可以尝试推算一下，最终结果是：-128

**<font style="color:#DF2A3F;">在整数类型中，除了 byte 有这个待遇之外，short 同样也是支持的。也就是说：如果整数型字面量没有超出 short 取值范围时，也是支持直接赋值的。</font>**

#### 两个 int 类型做运算

两个 int 类型的数据做运算，最终的结果还是 int 类型：

```java
int a = 10;
int b = 3;
int c = a / b;
System.out.println(c); // 3
```

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="JyIME" class="ne-image">

#### 多种数据类型混合运算

在 Java 中，多种数据类型混合运算时，各自先转换成容量最大的类型，再做运算。

```java
byte a = 100;
int b = 200;
long c = 300L;
long d = a + b + c;
```

你可以测试一下，如果 d 变量是 int 类型则编译器会报错。

#### 编译器的小心思

以下程序编译通过：

```java
byte x = 10 / 3;
```

为什么编译通过？这种情况下都是字面量的时候，编译器可以在编译阶段得出结果是 3，而 3 没有超出 byte 取值范围。可以直接赋值。

以下程序编译报错：

```java
int a = 10;
int b = 3;
byte x = a / b;
```

为什么编译失败？这种 a 和 b 都是变量的情况下，编译器是无法在编译阶段得出结果的，编译器只能检测到结果是 int 类型。int 类型不能直接赋值给 byte 类型变量。

怎么解决？要么把 x 变量声明为 int 类型，要么强制类型转换，例如：

```java
int a = 10;
int b = 3;
byte x = (byte)(a / b);
```

这里需要注意的是：注意小括号的添加，如果不添加小括号，例如：

```java
int a = 10;
int b = 3;
byte x = (byte)a / b;
```

这样还是编译报错，因为只是将 a 强转为 byte 了，b 还是 int。byte 和 int 混合运算，结果还是 int 类型。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="e3FCI" class="ne-image">

### 浮点型详解

浮点型类型包括：

- 单精度（float）：4 字节（32 位）
- 双精度（double）：8 字节（64 位），精度较高，实际开发中 double 用的多。

#### 浮点型字面量默认被当做 double

Java 中，浮点型字面量默认被当做 double 类型，如果要当做 float 类型，需要在数字后面添加 F 或 f。

```java
float f = 3.0; // 编译报错
```

报错原因是：3.0 默认被当做 double 类型，大容量无法直接赋值给小容量。如何修改：

```java
float f = 3.0F;
```

另外，可以通过以下程序的输出结果看到，double 精度高于 float：

```java
double d = 1.5656856894;
System.out.println(d);

float f = 1.5656856894F;
System.out.println(f);
```

#### 浮点型数据两种表示形式

第一种形式：十进制

```java
double x = 1.23;
double y = 0.23;
double z = .23;
```

第二种形式：科学计数法

```java
double x = 0.123E2;   // 0.123 * 10 的平方
double y = 123.34E-2; // 123.34 / 10 的平方
```

#### 浮点型数据存储原理

以单精度 float 为例：

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1685082090577-59e58430-81f7-4ab9-bfa4-10f89e18639c.png" width="975" title="" crop="0,0,1,1" id="u31eea96c" class="ne-image">

符号位：0 表示整数。1 表示负数。

指数位：比如小数 0.123E30，其中 30 就是指数。表示 0.123 * 10 的 30 次幂。所以也有把指数位叫做偏移量的。最大偏移量 127。

尾数位：浮点数的小数部分的有效数字。例如：0.00123，那么尾数位存储 123 对应的二进制。

**<font style="color:#DF2A3F;">从浮点型数据存储原理上可以看到，二进制中的指数位决定了数字呈指数级增大。因此 float 虽然是 4 个字节，但却可以表示比 long 更大的数值。因此 float 容量比 long 的容量大。</font>**

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="n7XpD" class="ne-image">

#### 使用浮点数的注意事项

计算机的二进制位有限，现实世界中有无限循环的数字，例如 3.333333333333333333……，因此计算机这种有限资源去存储无限数据是不可能的，所以浮点型数据在底层真实存储的时候都是采用近似值的方式存储的。尾数位越多精度越高。

实际上包括 0.1 这样简单的数字，浮点型数据也是无法精确存储的。（想了解更多，请查看相关文献）

这样就会有一个问题，请看以下程序：

```java
double x = 6.9;
double y = 3.0;
double z = x / y;
System.out.println(z);
```

它的执行结果是：2.3000000000000003 并不是 2.3

因此一旦有浮点型数据参与运算得出的结果，一定不要使用“==”与其它数字进行“相等比较”。例如，以下代码就存在问题：

```java
double x = 6.9;
double y = 3.0;
double z = x / y;
if(z == 2.3){
    System.out.println("相等");
}
```

执行发现并没有输出：相等。原因是判断条件有问题。

如果确实需要进行比较，可以将代码修改为如下：

```java
double x = 6.9;
double y = 3.0;
double z = x / y;
if(z - 2.3 < 0.000001){
    System.out.println("相等");
}
```

也就是说，如果这两个数字之间的差小于 0.000001，我就认为是相等的。

因此：如果有浮点型数据参与运算得出了结果，不要拿着这个结果和另一个数据进行“==”相等比较。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="zRLvf" class="ne-image">

### 字符型详解

char：字符型，占用 2 个字节。取值范围 0~65535。和 short（-32768~32767）所表示的个数相同。但 char 可以表示更大的整数。

字符型字面量采用单引号括起来，例如：'a'、'A'、'0'、'国' 等。

字符型字面量只能是单个字符，不能是多个字符。

Java 中 char 类型可以存储一个汉字。

```java
char c1 = 'A';
char c2 = 'a';
char c3 = '0';
char c4 = '国';
char c5 = '¥';

// 编译报错
// char c6 = 'ab';
```

再看下面程序：

```java
char x = '';
```

编译报错。由于单引号中没有任何字符，因此无法给 c 赋值，所以会导致编译报错，提示无效的字符字面量。

如果要赋给 c 一个空的字符，可以使用转义字符 '\u0000' 来表示。如下所示：

```java
char c = '\u0000'; // 赋给 c 一个空字符
```

**<font style="color:#DF2A3F;">注意：空字符与空格字符完全是两码事。</font>**

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="yROH0" class="ne-image">

#### 转义字符

Java 中的转义字符是一些在字符串中具有特殊含义的字符序列，它们以反斜线（\）开始。以下是 Java 中的一些常用转义字符：

- \t：表示制表符，相当于按下 Tab 键
- \n：表示换行符
- \"：表示双引号（"）
- \'：表示单引号（'）
- \\：表示反斜线（\）本身

这些转义序列可以用于不同的 Java 数据类型，如字符串、字符等。在 Java 编程中，转义字符可以帮助我们在字符串中表示一些特殊的字符，例如制表符、换行符、引号等。例如，下面的代码演示了如何使用转义字符来创建包含制表符和换行符的字符串：

```java
String str = "Hello\tworld\nHow are you?";
System.out.println(str);
```

这个例子中，\t 和 \n 分别表示字符串中的制表符和换行符。输出结果是：

```plain
Hello   world
How are you?
```

#### 字符编码的理解

字符编码（Character encoding）是计算机系统中使用的一种将字符集中的字符转换为二进制数据的方式，从而方便计算机的存储和传输。在计算机内部，所有的信息都是以二进制形式存储和处理的，因此字符编码是将字符和二进制数据之间的转换方式。每一个字符在计算机中都有其对应的二进制代码。不同的字符编码可以采用不同的编码方式将字符映射到二进制代码，最终这些二进制代码被存储在计算机内部。

在早期计算机系统中，字符编码主要采用的是 ASCII 编码，采用 1 个字节编码。最多可以表示 256 个字符。（实际上 ASCII 码表只用了 128 个。）

以下是 ASCII 码表：

| **十进制** | **字符** | **十进制** | **字符** | **十进制** | **字符** | **十进制** | **字符** |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | NUL | 32 | SPACE | 64 | @ | 96 | ` |
| 1 | SOH | 33 | ! | **<font style="color:#DF2A3F;">65</font>** | **<font style="color:#DF2A3F;">A</font>** | **<font style="color:#DF2A3F;">97</font>** | **<font style="color:#DF2A3F;">a</font>** |
| 2 | STX | 34 | " | 66 | B | 98 | b |
| 3 | ETX | 35 | # | 67 | C | 99 | c |
| 4 | EOT | 36 | $ | 68 | D | 100 | d |
| 5 | ENQ | 37 | % | 69 | E | 101 | e |
| 6 | ACK | 38 | & | 70 | F | 102 | f |
| 7 | BEL | 39 | ' | 71 | G | 103 | g |
| 8 | BS | 40 | ( | 72 | H | 104 | h |
| 9 | HT | 41 | ) | 73 | I | 105 | i |
| 10 | LF | 42 | * | 74 | J | 106 | j |
| 11 | VT | 43 | + | 75 | K | 107 | k |
| 12 | FF | 44 | , | 76 | L | 108 | l |
| 13 | CR | 45 | - | 77 | M | 109 | m |
| 14 | SO | 46 | . | 78 | N | 110 | n |
| 15 | SI | 47 | / | 79 | O | 111 | o |
| 16 | DLE | **<font style="color:#DF2A3F;">48</font>** | **<font style="color:#DF2A3F;">0</font>** | 80 | P | 112 | p |
| 17 | DC1 | 49 | 1 | 81 | Q | 113 | q |
| 18 | DC2 | 50 | 2 | 82 | R | 114 | r |
| 19 | DC3 | 51 | 3 | 83 | S | 115 | s |
| 20 | DC4 | 52 | 4 | 84 | T | 116 | t |
| 21 | NAK | 53 | 5 | 85 | U | 117 | u |
| 22 | SYN | 54 | 6 | 86 | V | 118 | v |
| 23 | ETB | 55 | 7 | 87 | W | 119 | w |
| 24 | CAN | 56 | 8 | 88 | X | 120 | x |
| 25 | EM | 57 | 9 | 89 | Y | 121 | y |
| 26 | SUB | 58 | : | 90 | Z | 122 | z |
| 27 | ESC | 59 | ; | 91 | [ | 123 | { |
| 28 | FS | 60 | < | 92 | \ | 124 | | |
| 29 | GS | 61 | = | 93 | ] | 125 | } |
| 30 | RS | 62 | > | 94 | ^ | 126 | ~ |
| 31 | US | 63 | ? | 95 | _ | 127 | DEL |

作为程序员，我们应当记住以下几个常用字符的 ASCII 码：

- a 对应 ASCII 码 97（b 是 98，以此类推）
- A 对应 ASCII 码 65（B 是 66，以此类推）
- 0 对应 ASCII 码 48（1 是 49，以此类推）

---

**什么是解码？什么是编码？乱码是如何产生的？**

在计算机系统中，解码（Decoding）和编码（Encoding）是两个常用的概念，分别表示将二进制数据转换为字符和将字符转换为二进制数据。

编码是将字符转换为二进制数据的过程。解码是将二进制数据转换为字符的过程。例如：

- 'a' ---------按照 ASCII 码表 **<font style="color:#DF2A3F;">编码</font>** -----------> 01100001
- 01100001 --------按照 ASCII 码表 **<font style="color:#DF2A3F;">解码</font>** ------------> 'a'

乱码是指在字符编码和解码的过程中，由于编码和解码所采用的字符集不一致，或者编码和解码所采用的字符集不支持某些字符，导致最终显示的字符与原始字符不一致。为了避免乱码的问题，我们需要统一使用一个字符集，并且在进行字符编码和解码时要保持一致。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="aWc2L" class="ne-image">

#### 常见的字符编码

常见的字符编码方式如下：

1. ASCII 编码（American Standard Code for Information Interchange：美国信息交换标准编码）：采用 1 个字节编码，包括字母、数字、符号和控制字符等。
2. Latin-1 编码（ISO 8859-1），采用 1 个字节编码。该编码方式是为了表示欧洲语言（如荷兰语、西班牙语、法语、德语等）中的字符而设计的，共支持 256 个字符。
3. Unicode 字符集：容纳了全球所有国家的文字，每一个文字都对应一个编号。Unicode 字符集当中包含多种字符编码方式。（**<font style="color:rgb(15, 17, 21);">字符集</font>** <font style="color:rgb(15, 17, 21);">是给每个字符分配一个唯一编号（码点）的集合；</font> **<font style="color:rgb(15, 17, 21);">字符编码方式</font>** <font style="color:rgb(15, 17, 21);">是把这个编号转换成计算机实际存储的二进制字节的具体规则</font>）
4. UTF-8 编码（Unicode Transformation Format，8-bit）：基于 Unicode 字符集的**可变长度字符编码**，能够支持多语言和国际化的需求，使用 1~4 个字节来表示一个字符，是目前 Web 开发中最常用的字符编码方式。（一个英文字母 1 个字节，一个汉字 3 个字节。）
5. UTF-16 编码：基于 Unicode 字符集的可变长度字符编码，使用 2 或 4 个字节来表示一个字符，Java 中采用的就是这个字符编码方式。（一个英文字母 2 个字节。一个普通汉字占 2 个字节。一个不常见的汉字占 4 个字节，例如 `𠀀`。）
6. UTF-32 编码：基于 Unicode 字符集的固定长度字符编码，其特点是每个字符占用 4 个字节。
7. GB2312 编码（小）：是中国国家标准的简体中文字符集，使用 2 个字节来表示一个汉字，是 GBK 编码的前身。
8. GBK 编码（Guo Biao Ku）（中）：是针对中文设计的一个汉字编码方式，使用 2 个字节来表示一个汉字，能够表示中国内地的所有汉字。
9. GB18030 编码（大）：是中国国家标准 GB 18030-2005《信息技术 中文编码字符集》中规定的字符集编码方案，用于取代 GB2312 和 GBK 编码。
10. Big5 编码（大五码）：是台湾地区的繁体中文字符集，使用 2 个字节来表示一个汉字，适用于使用繁体中文的应用场景。
11. ANSI：不是一种具体的编码方式，而是编码方式的一个别名，具体的编码方式是什么取决操作系统，假设操作系统是简体中文的，那么 ANSI 代表的编码方式就是 GBK。

**注意：** <font style="color:rgb(15, 17, 21);">Java 的字符和字符串在</font> **<font style="color:rgb(15, 17, 21);">字符集层面</font>** <font style="color:rgb(15, 17, 21);">都使用 Unicode，在</font> **<font style="color:rgb(15, 17, 21);">内部存储编码</font>** <font style="color:rgb(15, 17, 21);">上主要使用 UTF-16（可能带优化）。</font>

#### Unicode 码表

Unicode 码表的一部分：

| **十六进制码** | **字符** | **名称** | **符号** |
| --- | --- | --- | --- |
| U+0020 | | 空格 | (space) |
| U+0021 | ! | 感叹号 | (exclamation mark) |
| U+0022 | " | 双引号 | (quotation mark) |
| U+0023 | # | 井号 | (number sign) |
| U+0024 | $ | 美元 | (dollar sign) |
| U+0025 | % | 百分号 | (percent sign) |
| U+0026 | & | 和号 | (ampersand) |
| U+0027 | ' | 单引号 | (apostrophe) |
| U+0028 | ( | 左括号 | (left parenthesis) |
| U+0029 | ) | 右括号 | (right parenthesis) |
| U+002A | * | 星号 | (asterisk) |
| U+002B | + | 加号 | (plus sign) |
| U+002C | , | 逗号 | (comma) |
| U+002D | - | 减号 | (hyphen, -minus sign) |
| U+002E | . | 句点 | (full stop, period) |
| U+002F | / | 斜杠 | (slash, forward slash) |
| U+0030 | 0 | 零 | (digit zero) |
| U+0031 | 1 | 一 | (digit one) |
| U+0032 | 2 | 二 | (digit two) |
| U+0033 | 3 | 三 | (digit three) |
| U+0034 | 4 | 四 | (digit four) |
| U+0035 | 5 | 五 | (digit five) |
| U+0036 | 6 | 六 | (digit six) |
| U+0037 | 7 | 七 | (digit seven) |
| U+0038 | 8 | 八 | (digit eight) |
| U+0039 | 9 | 九 | (digit nine) |
| U+003A | : | 冒号 | (colon) |
| U+003B | ; | 分号 | (semicolon) |
| U+003C | < | 小于号 | (less than sign) |
| U+003D | = | 等于号 | (equals sign) |
| U+003E | > | 大于号 | (greater than sign) |
| U+003F | ? | 问号 | (question mark) |
| U+0040 | @ | 艾特符号 | (commercial at) |
| U+0041 | A | 拉丁大写字母 A | (Latin capital letter A) |
| U+0042 | B | 拉丁大写字母 B | (Latin capital letter B) |
| U+0043 | C | 拉丁大写字母 C | (Latin capital letter C) |
| U+0044 | D | 拉丁大写字母 D | (Latin capital letter D) |
| U+0045 | E | 拉丁大写字母 E | (Latin capital letter E) |
| U+0046 | F | 拉丁大写字母 F | (Latin capital letter F) |
| U+0047 | G | 拉丁大写字母 G | (Latin capital letter G) |

在 Java 程序中也可以使用 Unicode 码来指定 char 变量的值：

```java
char c = '\u0041';
```

输出结果是：A

网络上也有很多在线转码工具，例如：[http://www.jsons.cn/unicode/](http://www.jsons.cn/unicode/)

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="L8TdH" class="ne-image">

#### char 参与的运算

Java 中允许将一个整数赋值给 char 类型变量，但这个整数会被当做 ASCII 码值来处理，例如：

```java
char c = 97;
System.out.println(c);
```

会将 97 当做 ASCII 码值，该码值转换 char 类型是字符 'a'，所以输出结果是：a

但需要特别注意的是，这个码值有要求，不能超出 char 的取值范围。如果是这样的，编译会报错：

```java
// 编译报错
char c = 65536;
```

所以结合之间的 byte 和 short，可以有这样一个结论（记住）：只要没有超出 byte short char 的取值范围，是可以直接赋值给 byte short char 类型变量的。例如：

```java
byte b = 1;
short s = 1;
char c = 1;
```

再看以下程序输出结果：

```java
System.out.println('a' + 1);
```

输出结果是：98。这是因为 1 是 int 类型，所以 'a' 会被转换为 int 类型。

再看以下程序输出结果：

```java
char c = 'a' + 1;
System.out.println(c);
```

输出结果是：b。这是因为 c 的类型是 char 类型。

再看以下程序输出结果：

```java
byte b = 1;
short s = 1;
char c = 1;
short num = b + s + c;
```

编译报错：第 4 行的等号右边是 int 类型，int 类型无法赋值给 short 类型的变量。

这里有一个结论需要记住：byte short char 混合运算时，各自会先转换成 int 再做运算。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="xbncD" class="ne-image">

### 布尔型详解

#### 关于布尔型的值

Java 中的布尔型，关键字：boolean

只有两个值：true、false。没有 1 和 0 这一说。

true 表示真，false 表示假。

#### 布尔值通常使用在哪

Java 中的布尔值（boolean）通常用于表示一些逻辑上的真假值，并在程序中进行逻辑控制。以下是布尔值在 Java 中常用的场景：

1. 条件语句，if 和 while 等语句中需要进行条件判断时，通常使用布尔类型的变量作为条件表达式，根据条件的真假情况执行不同的代码逻辑。
2. 逻辑运算，布尔值是逻辑运算的基础，Java 中的逻辑运算符有：与（&&）、或（||）、非（!）等，常用于对布尔值的运算和操作。
3. 方法返回值，可以将布尔值作为方法的返回值，表示某种条件是否满足。
4. 开关标记，布尔变量在程序中常用于开关标记的判断和设置，例如，当某个功能开启或关闭时，我们可以用布尔类型的变量来表示。

综上所述，Java 中的布尔值在程序中有很多用途，可以在很多场景下提供非常便利的逻辑控制和判断能力。

下面是一个使用布尔值的简单案例：

```java
boolean gender = true;
if(gender){
    System.out.println("男");
}else{
    System.out.println("女");
}
```

### 基本数据类型转换规则总结

1. 八种基本数据类型，除布尔型之外，其它类型都可以互相转换。
2. 小容量转换为大容量，叫做自动类型转换，容量从小到大的排序为：
   3. byte < short(char) < int < long < float < double
   4. 注意 char 比 short 可以表示更大的整数
5. 大容量转换为小容量，叫做强制类型转换，需要加强制类型转换符才能编译通过，运行时可能损失精度，也可能不会损失。
6. 整数字面量如果没有超出 byte short char 的取值范围，可以直接赋值给 byte short char 类型的变量。
7. byte short char 混合运算，各自先转换为 int 再做运算。
8. 多种类型混合运算，各自先转换成容量最大的类型，再做运算。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="j554m" class="ne-image">

### 变量和数据类型的作业题

1. 请定义合理的变量用来存储个人信息（姓名、年龄、性别、联系电话），并编写程序定义这些变量，给变量赋值，并打印输出。输出效果如下：

   姓名 年龄 性别 联系电话
   张三 20 男 12545457585
   李四 30 女 15622525855

2. 有两个变量 a 和 b，a 变量中存储的数据 100，b 变量中存储的数据 200，请编写程序交换两个变量中的数据。让 a 变量存储 200，让 b 变量存储 100。并且计算两个 int 类型数据的和，要求最终输出 200+100=300 的效果。

3. 请分析以下程序中哪些是可以编译通过的，哪些是报错的

```java
short s = 100;
s = s - 99;

byte b = 100;
b = b + 1;

char c = 'a';
int i = 20;
float f = .3F;
double d = c + i + f;

byte b1 = 11;
short s1 = 22;
short x = b1 + s1;
```

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="U5CEY" class="ne-image">

## 运算符（掌握）

### 运算符总览及优先级

下面是完整的 Java 运算符列表：

| **运算符类型** | **运算符** | **说明** |
| --- | --- | --- |
| 算术运算符 | + | 加法 |
| | - | 减法 |
| | * | 乘法 |
| | / | 除法 |
| | % | 取模 |
| | ++ | 自增 |
| | -- | 自减 |
| 关系运算符 | == | 相等 |
| | != | 不等于 |
| | > | 大于 |
| | < | 小于 |
| | >= | 大于等于 |
| | <= | 小于等于 |
| 逻辑运算符 | & | 逻辑与 |
| | | | 逻辑或 |
| | ! | 逻辑非 |
| | && | 短路与 |
| | || | 短路或 |
| 按位运算符 | & | 按位与 |
| | | | 按位或 |
| | ^ | 按位异或 |
| | ~ | 取反 |
| | << | 左移 |
| | >> | 右移 |
| | >>> | 无符号右移 |
| 赋值运算符 | = | 赋值 |
| | += | 加等于 |
| | -= | 减等于 |
| | *= | 乘等于 |
| | /= | 除等于 |
| | %= | 取模等于 |
| | &= | 按位与等于 |
| | |= | 按位或等于 |
| | ^= | 按位异或等于 |
| | <<= | 左移等于 |
| | >>= | 右移等于 |
| | >>>= | 无符号右移等于 |
| 条件运算符 | ? : | 如果条件为真，则返回第一个值，否则返回第二个值 |
| instanceof 运算符 | instanceof | 测试对象是否为特定类的实例 |
| new 运算符 | new | 通过创建一个对象或数组来分配新的内存 |
| . 运算符 | . | 对象成员访问，使用“对象.属性”或“对象.方法（参数）” |

以上列出了在 Java 中可用的所有运算符。需要根据操作数来选择适当的运算符。并且运算符是有优先级的，优先级如下：由高到低：

| 运算符类型 | 运算符 | 优先级 |
| --- | --- | --- |
| 后缀运算符 | ++ -- | 高 |
| 一元运算符 | + - ~ ! | |
| 乘性运算符 | * / % | |
| 加性运算符 | + - | |
| 移位运算符 | << >> >>> | |
| 关系运算符 | < <= > >= instanceof | |
| 相等运算符 | == != | |
| 按位与运算符 | & | |
| 按位异或运算符 | ^ | |
| 按位或运算符 | | | |
| 逻辑与运算符 | && | |
| 逻辑或运算符 | || | |
| 三目运算符 | ? : | |
| 赋值运算符 | = += -= *= /= %= &= |= ^= <<= >>= >>>= | 低 |

注意，优先级高的运算符会比优先级低的先执行，如果有多个操作符在同一个表达式中，则按照优先级解析。**<font style="color:#DF2A3F;">在表达式中使用圆括号可以明确调整优先级</font>**。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="slT1K" class="ne-image">

### 算术运算符

#### 算术运算符用法

+（加法、正数、字符串拼接）、-（减法、负数）、*（乘法）、/（除法）、%（取模）、++（自增 1）、--（自减 1）

```java
// +
int num1 = +10;
int num2 = 3;
System.out.println(num1 + "+" + num2 + "=" + (num1 + num2));

// -
int num3 = 10;
int num4 = -3;
System.out.println(num3 - num4);

// *
int num5 = 10;
int num6 = 3;
System.out.println(num5 * num6);

// /
System.out.println(num5 / num6);

double num7 = 10.0;
int num8 = 3;
System.out.println(num7 / num8);

int num9 = 10;
int num10 = 3;
double num11 = num9 / num10;
System.out.println(num11);

// %
System.out.println(num5 % num6);

int x = 10;
int y = 3;
// 取模的运算公式： x - x / y * y
System.out.println(x % y); // 1

x = -10;
System.out.println(x % y); // -1

x = 10;
y = -3;
System.out.println(x % y); // 1
```

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="hSpXY" class="ne-image">

#### 自增/自减

以自增为例讲解，自减自行研究。

++ 可以出现在变量前，也可以出现在变量后。**<font style="color:#DF2A3F;">单独使用</font>**时，都会让变量自加 1。

```java
int i = 10;
i++;
System.out.println(i); // 11

int k = 10;
++k;
System.out.println(k); // 11
```

无论是 ++i 还是 i++，都等同于：i = i + 1;

如果出现在表达式当中，出现在变量前和变量后是不同的：

变量前：先自加 1，后赋值。

```java
int i = 10;
int k = ++i; // i = i + 1; k = i;
System.out.println("i = " + i); // 11
System.out.println("k = " + k); // 11
```

变量后：先赋值，后自加 1。

```java
int i = 10;
int k = i++; // k = i; i = i + 1;
System.out.println("i = " + i); // 11
System.out.println("k = " + k); // 10
```

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="dB9QE" class="ne-image">

#### 接收用户键盘输入

System.out.println() 可以完成输出，怎么在控制台接收用户键盘输入呢？以下代码先照抄，后期学完面向对象就明白了：

```java
public class KeyInput {
    public static void main(String[] args){
        java.util.Scanner s = new java.util.Scanner(System.in);

        // 接收一个整数
        int num1 = s.nextInt();
        System.out.println("您输入的整数是：" + num1);

        // 接收一个浮点数
        double num2 = s.nextDouble();
        System.out.println("您输入的浮点数是：" + num2);

        // 接收一个字符串
        String str = s.next();
        System.out.println("您输入的字符串是：" + str);
    }
}
```

#### 解读字节码指令

```java
public class ReadClass{
    public static void main(String[] args){
        int i = 10;
    }
}
```

编译生成：ReadClass.class

如何查看字节码？javap -c ReadClass.class，以上程序字节码如下：

```java
public class ReadClass {
    public ReadClass();
    Code:
        0: aload_0
        1: invokespecial #1 // Method java/lang/Object."<init>":()V
        4: return

    public static void main(java.lang.String[]);
    Code:
        0: bipush 10
        2: istore_1
        3: return
}
```

重点研究 main 方法中的字节码含义：

bipush 指令：将字面量压入操作数栈。

istore_1 指令：将操作数栈中顶部数据弹出，然后将该数据存放到局部变量表的第 1 个位置。

什么是局部变量表？什么是操作数栈？

每个方法在被调用时都会分配一个独立的空间，该空间中又包括局部变量表和操作数栈两个部分。

局部变量表用来存储方法中定义的局部变量、方法参数等等，它是在编译时确定大小的，具体的大小可以在字节码中看到。

操作数栈用来存储方法执行中的操作数据，操作数栈是一个后进先出（LIFO）的数据结构，Java 虚拟机在执行指令时会将数据压入操作数栈中，然后再从栈中取出数据进行计算。

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1685760980390-3ab8a654-05b8-465e-9c3b-90f3c0135765.png" width="978" title="" crop="0,0,1,1" id="u28c0867a" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1685761033069-82771e65-bc70-410d-95cb-575e167239ce.png" width="1098" title="" crop="0,0,1,1" id="u241d6585" class="ne-image">

```java
public class ReadClass{
    public static void main(String[] args){
        int i = 10;
        int j = i;
    }
}
```

编译生成：ReadClass.class

javap -c ReadClass.class，以上程序字节码如下：

```java
public class ReadClass {
    public ReadClass();
    Code:
        0: aload_0
        1: invokespecial #1 // Method java/lang/Object."<init>":()V
        4: return

    public static void main(java.lang.String[]);
    Code:
        0: bipush 10
        2: istore_1
        3: iload_1
        4: istore_2
        5: return
}
```

iload_1 指令：将局部变量表中第 1 个位置存储的数据复制一份，放到操作数栈当中。

istore_2 指令：将操作数栈顶部数据弹出，将其存放到局部变量表的第 2 个位置上。

```java
public class ReadClass{
    public static void main(String[] args){
        int i = 10;
        i++;
    }
}
```

编译生成：ReadClass.class

javap -c ReadClass.class，以上程序字节码如下：

```java
public class ReadClass {
    public ReadClass();
    Code:
        0: aload_0
        1: invokespecial #1 // Method java/lang/Object."<init>":()V
        4: return

    public static void main(java.lang.String[]);
    Code:
        0: bipush 10
        2: istore_1
        3: iinc 1, 1
        6: return
}
```

iinc 指令：将局部变量表中第 1 个位置数据加 1

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="ScKMB" class="ne-image">

#### 算术运算符相关作业题

题目 1：采用字节码解读的方式分析以下代码的区别

```java
int i = 10;
int k = i++;
```

```java
int i = 10;
int k = ++i;
```

题目 2：以下程序输出结果是？

```java
int a = 5;
int b = a++;
b = a++;
System.out.println("a = " + a);
System.out.println("b = " + b);

int c = 10;
int d = --c;
System.out.println("c = " + c);
System.out.println("d = " + d);
```

题目 3：以下程序输出结果是？

```java
int i = 10;
int k = i++ + ++i;
System.out.println(k);

int f = 10;
int m = f++ + f;
System.out.println(m);
System.out.println(f);
```

题目 4：以下程序输出结果是？经典面试题

```java
int i = 10;
i = i++;
System.out.println(i);

int i = 10;
i = ++i;
System.out.println(i);
```

题目 5：从键盘上接收一个整数三位数，请分别输出它的个位、十位、百位。

题目 6：681 分钟是多少个小时 + 多少分钟。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="w8iAS" class="ne-image">

### 关系运算符

关系运算符又叫做比较运算符。包括：>、>=、<、<=、==、!=

所有关系运算符的运算结果都是布尔类型，不是 true，就是 false。

```java
int a = 10;
int b = 10;
System.out.println(a > b);  // false
System.out.println(a >= b); // true
System.out.println(a < b);  // false
System.out.println(a <= b); // true
System.out.println(a == b); // true
System.out.println(a != b); // false
```

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="rF1cA" class="ne-image">

### 逻辑运算符

逻辑运算符：&（逻辑与）、|（逻辑或）、!（逻辑非）、^（逻辑异或）、&&（短路与）、||（短路或）

逻辑运算符特点：逻辑运算符两边的操作数要求必须是布尔类型，并且最终运算结果也一定是布尔类型。

逻辑与 &：两边操作数都是 true，结果才是 true。可以翻译为“并且”。

逻辑或 |：两边操作数只要有一个是 true，结果就是 true。可以翻译为“或者”。

逻辑非 !：!false 就是 true，!true 就是 false。

逻辑异或 ^：咱俩不一样，结果就是 true。

短路与 &&：和逻辑与 & 的运算结果相同。只是存在一种短路现象。（左边操作数为 false 时，右边操作数不执行）

短路或 ||：和逻辑或 | 的运算结果相同。只是存在一种短路现象。（左边操作数为 true 时，右边操作数不执行）

虽然短路与 && 效率高于逻辑与 &，但逻辑与 & 也有用武之地，具体看需求是怎样的。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="I7AXm" class="ne-image">

### 按位运算符

#### 按位运算符概述

按位运算符用于在**<font style="color:#DF2A3F;">二进制位级别上处理整数数据</font>**。主要包括：

- 按位与 &
- 按位或 |
- 按位异或 ^
- 按位取反 ~
- 左移 <<
- 右移 >>
- 无符号右移 >>>

注意：**<font style="color:#DF2A3F;">按位运算符的操作数要求必须是整数</font>**。否则会出现编译错误。

**<font style="color:#DF2A3F;">另外需要注意的是：在 Java 中所有的按位运算符都是针对二进制的补码进行运算的。</font>**

#### 按位与 &

将两个整数的二进制表示按位进行与运算，只有当相应的二进制位都为 1 时，结果才为 1，否则结果为 0

```java
int a = 32;
int b = 25;
System.out.println(a & b); // 0
```

a 的二进制：00100000  
b 的二进制：00011001  
按位与之后：00000000

**<font style="color:#DF2A3F;">应用一下</font>**：请使用按位与运算符判断某个数字是否为奇数？思路：拿着这个数字和 1 进行按位与，如果结果是 1，则表示该数字为奇数。

#### 按位或 |

将两个整数的二进制表示按位进行或运算，只有当相应的二进制位都为 0 时，结果才为 0，否则结果为 1

```java
int a = 32;
int b = 25;
System.out.println(a | b); // 57
```

a 的二进制：00100000  
b 的二进制：00011001  
按位或之后：00111001

**<font style="color:#DF2A3F;">应用一下</font>**：请将 0 这个数字中第 2、4、6 位的二进制**<font style="color:#DF2A3F;">位设置</font>**为 1（这属于标志位设置的具体应用）

```java
int flag = 0;
flag = flag | (1 << 1);
System.out.println(flag);

flag = flag | (1 << 3);
System.out.println(flag);

flag = flag | (1 << 5);
System.out.println(flag);
```

#### 按位异或 ^

将两个整数的二进制表示按位进行异或运算，只有当相应的二进制位不同，结果才为 1，否则结果为 0

```java
int a = 100;
int b = 200;
System.out.println(a ^ b); // 172
```

a 的二进制：01100100  
b 的二进制：11001000  
按位异或之后：10101100

按位异或运算符具有**自反性**，所谓的自反性是指：数字 A 连续对数字 B 进行两次按位异或运算之后，可以得到原始的数字 A。因为按位异或运算符具有这样的特征，所以在密码学方面应用广泛。通常使用它可以完成加密和解密操作。

**<font style="color:#DF2A3F;">应用一下</font>**：按位异或可以实现简单的加密和解密。

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1685686526533-b7d12ade-e4fb-4f37-a725-09a164ac1176.png" width="287" title="" crop="0,0,1,1" id="uba7622db" class="ne-image">

#### 按位取反 ~

将整数的二进制表示按位进行取反运算，即 0 变为 1，1 变为 0

```java
System.out.println(~100); // -101
```

100 的二进制：01100100  
取反后：10011011（这是一个补码哦）  
将补码转为原码：11100101（-101）

**<font style="color:#DF2A3F;">应用一下</font>**：**<font style="color:#DF2A3F;">位清除</font>**操作（将某个二进制位中指定位清除为 0），例如有这样一个二进制：0b01101101，将第 4 个低位清除为 0

```java
// 待清除数据
int value = 0b01101101;
// 需要清除第 4 个低位
int flag = 1 << 3; // 00001000 (它取反：11110111)
// 使用以下方式运算进行位清除
int result = value & (~flag);
System.out.println(result);
```

#### 左移 <<

它能够将一个二进制数的所有位向左移动指定的位数。左移运算符的运算规则如下：

1. 将二进制数左移 n 位，相当于将数值乘以 2 的 n 次方。  
   例如，将二进制数 0b1011 左移 2 位，即为 0b101100，相当于将 11 乘以 2 的 2 次方（即 4），得到 44。
2. 左移运算符**<font style="color:#DF2A3F;">可能会</font>**改变符号位。
3. 左移运算符会对溢出进行截断，右补 0

**<font style="color:#DF2A3F;">应用一下</font>**：如何将 2 快速变成 8？

```java
System.out.println(2 << 2);
```

#### 右移 >>

它能够将一个二进制数的所有位向右移动指定的位数。右移运算符的运算规则如下：

1. 将二进制数右移 n 位，相当于将数值除以 2 的 n 次方。  
   例如，将二进制数 0b101100 右移 2 位，即为 0b1011，相当于将 44 除以 2 的 2 次方（即 4），得到 11。
2. 右移运算符对正数、负数和零的处理方式不同。
   - 对于正数，符号位不变，右移时左补 0
   - 对于负数，符号位不变，右移时左补 1。
   - 对于零，右移运算符操作后结果仍为零。
3. 右移运算符会对溢出进行截断。

#### 无符号右移 >>>

它能够将一个二进制数的所有位向右移动指定的位数，而不考虑符号位。无符号右移运算符的运算规则如下：

1. 将二进制数右移 n 位，相当于将数值除以 2 的 n 次方，并将最高位填充为 0。
2. 任意一个数字经过无符号右移之后，最终结果一定是非负数（0 或正整数）
3. 无符号右移运算符对溢出进行截断。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="qQevm" class="ne-image">

### 赋值运算符

赋值运算符包括：

- 基本赋值运算符
  - =
- 扩展赋值运算符
  - +=、-=、*=、/=、%=、&=、|=、^=、>>=、<<=、>>>=

#### 基本赋值运算符 =

等号右边先执行，将直接结果赋值给左边的变量。

```java
int a = 10;
int b = 20;
int c = a + b;
```

#### 扩展赋值运算符

+=、-=、*=、/=、%=、&=、|=、^=、>>=、<<=、>>>=

以 += 为例。i += 3; 表示 i = i + 3; += 就是先 + 后 =，也就是先求和，然后将求和的结果重新赋值。

对于扩展赋值运算符来说，有一个非常重要的运算规则需要注意：扩展赋值运算符不会改变运算结果的类型。（即使精度损失了，也不会改变运算结果类型。）

```java
byte b = 100;
b += 1000; // 运算完之后，虽然精度损失了，可是 b 类型仍然是 byte 类型
```

### 条件运算符

Java 语言中的条件运算符由 ? 和 : 组成，也被称为三元运算符。它的语法格式为：

```plain
布尔表达式 ? 表达式1 : 表达式2
```

当布尔表达式的值为 true 时，条件运算符的结果为表达式 1 的值，否则为表达式 2 的值。这种运算符常用于简化 if-else 语句的代码量。

使用条件运算符的主要步骤为：

1. 编写带有条件判断的布尔表达式。
2. 编写布尔表达式为 true 时执行的代码，即为表达式 1。
3. 编写布尔表达式为 false 时执行的代码，即为表达式 2。

下面是一个条件运算符的简单示例：

```java
int a = 5, b = 7;
int max = (a > b) ? a : b;
System.out.println("最大值为：" + max);
```

在上述代码中，首先定义了两个变量 a 和 b，然后使用条件运算符比较这两个变量的大小，取其中较大值作为变量 max 的值，最后输出结果。

当 a > b 的结果为 false 时，条件运算符的结果为表达式 2，即 b 的值为变量 max 的值。当 a > b 的结果为 true 时，条件运算符的结果为表达式 1，即 a 的值为变量 max 的值。

总的来说，条件运算符在 Java 中的使用相对简单，能够减少代码重复和代码量，常用于简单的条件处理和表达式值的判断。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="Lq9fA" class="ne-image">

### 运算符作业题

1. 编写 Java 代码，输入一个半径值，计算圆的面积和周长，并输出结果。注意：圆的面积公式为 pi * r * r，周长公式为 pi * 2 * r，其中 pi 取 3.14。

```java
public class Circle {
    public static void main(String[] args) {
        java.util.Scanner input = new java.util.Scanner(System.in); // 创建 Scanner 对象
        double pi = 3.14; // 定义圆周率为 3.14
        System.out.print("请输入圆的半径值：");
        double r = input.nextDouble(); // 输入半径值
        double S = pi * r * r; // 计算圆的面积
        double C = pi * 2 * r; // 计算圆的周长
        System.out.println("半径为" + r + "的圆的面积为：" + S);
        System.out.println("半径为" + r + "的圆的周长为：" + C);
    }
}
```

2. 假设变量 a、b、c 分别为 6、9、10，请编写 Java 代码输出它们的最大值。

```java
public class MaxValue {
    public static void main(String[] args) {
        int a = 6, b = 9, c = 10;
        int max = (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c);
        System.out.println("三个数中的最大值是：" + max);
    }
}
```

3. 假设变量 n 为整数，请编写 Java 代码判断它是不是一个偶数。

```java
public class IsEven {
    public static void main(String[] args) {
        java.util.Scanner input = new java.util.Scanner(System.in); // 创建 Scanner 对象
        System.out.print("请输入一个整数：");
        int n = input.nextInt(); // 输入整数 n
        String result = (n % 2 == 0) ? "是一个偶数" : "是一个奇数";
        System.out.println(n + " " + result);
    }
}
```

4. 编写 Java 代码，输入三个整数，分别判断第一个数是否大于 0，第二个数是否小于 10，第三个数是否是偶数。如果都满足条件，则输出“三个条件都满足”，否则输出“不满足所有条件”。

```java
public class CheckConditions {
    public static void main(String[] args) {
        java.util.Scanner input = new java.util.Scanner(System.in); // 创建 Scanner 对象
        System.out.print("请输入三个整数，以空格或回车分隔：");
        int a = input.nextInt();
        int b = input.nextInt();
        int c = input.nextInt();
        String result = (a > 0 && b < 10 && c % 2 == 0) ? "三个条件都满足" : "不满足所有条件";
        System.out.println(result);
    }
}
```

5. 编写 Java 代码，输入一个年份，判断它是否是闰年。若该年份能被 4 整除且不能被 100 整除，或者能被 400 整除，则该年份为闰年。输出结果为“该年是闰年”或“该年不是闰年”。

```java
public class LeapYear {
    public static void main(String[] args) {
        java.util.Scanner input = new java.util.Scanner(System.in); // 创建 Scanner 对象
        System.out.print("请输入一个年份：");
        int year = input.nextInt();

        if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
            System.out.println("该年是闰年");
        } else {
            System.out.println("该年不是闰年");
        }
    }
}
```

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="hJsMV" class="ne-image">

## 控制语句（掌握）

Java 中的控制语句用于控制程序的执行流程，改变程序执行的次序。分为三大类：

1. 分支语句：分支语句用于根据某个条件的成立情况来改变程序的执行路径。
   2. if
   3. switch
4. 循环语句：循环语句用于重复执行某一段代码，具体执行次数可以在开始前指定，也可以通过某个变量值或者条件来确定执行的次数。
   5. for
   6. while
   7. do while
8. 跳转语句：跳转语句用于改变代码的执行顺序，可以直接跳转到代码的某个位置。
   9. break
   10. continue
   11. return

控制语句在 Java 中具有非常重要的作用，可以根据执行条件来控制执行流程，提高代码的灵活性和可扩展性。通过使用控制语句，可以编写出更加高效、优雅和易于维护的代码。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="rOJoV" class="ne-image">

### 分支语句

分支语句包括：

- if 语句
- switch 语句

#### if 语句

if 语句又叫做**<font style="color:#DF2A3F;">条件控制语句</font>**。有以下四种写法：

1. if 语句

语法格式：

```java
if (布尔表达式) {
    // 如果布尔表达式为真，则执行下面的代码
}
```

说明：if 语句只有一个条件，当条件为真时，执行下面的代码块。

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686123487086-4fe63396-533a-4c3e-8b16-70f88b630d8e.png" width="230" title="" crop="0,0,1,1" id="n0e6z" class="ne-image">

**练一练：**

编写一个程序，输入一个人的年龄 age，如果他的年龄大于等于 18 岁，则输出"你已经成年了"，否则不输出任何东西。

编写一个程序，输入一个学生的分数 score（百分制），如果学生的分数大于等于 60，则输出"你已经及格了"，否则不输出任何东西。

编写一个程序，输入一个学生的分数 score（百分制），如果学生的分数大于等于 60，则输出"你已经及格了"，如果学生的分数小于 60，则输出"很抱歉，你不及格"。

2. if-else 语句

语法格式：

```java
if (布尔表达式) {
    // 如果布尔表达式为真，则执行下面的代码
} else {
    // 如果布尔表达式为假，则执行下面的代码
}
```

说明：if-else 语句有两个条件，当第一个条件为真时，执行 if 的代码块，否则执行 else 的代码块。

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686123813957-cd0dc709-840c-4d27-9710-0537b11630a8.png" width="355" title="" crop="0,0,1,1" id="u53588e86" class="ne-image">

**练一练：**

第一题：编写一个程序，输入一个学生的分数 score（百分制），如果学生的分数大于等于 60，则输出"你已经及格了"，如果学生的分数小于 60，则输出"很抱歉，你不及格"。

第二题：编写一个程序，输入一个数字 num，判断它是否为 7 的倍数。如果是，则输出"num 是 7 的倍数"，否则输出"num 不是 7 的倍数"。

第三题：编写一个程序，输入一个数字 num，判断它是否同时为 3 的倍数和 5 的倍数。如果是，则输出"num 既是 3 的倍数又是 5 的倍数"，否则输出"num 不同时是 3 的倍数和 5 的倍数"。

3. if-else if-else if 语句

语法格式：

```java
if (布尔表达式 1) {
    // 如果布尔表达式 1 为真，则执行下面的代码块 1
} else if (布尔表达式 2) {
    // 如果布尔表达式 1 为假，且布尔表达式 2 为真，则执行下面的代码块 2
} else if (布尔表达式 3) {
    // 如果布尔表达式 1 和 2 都为假，且布尔表达式 3 为真，则执行下面的代码块 3
}
```

说明：if-else if-else if 语句有多个条件，依次判断每一个条件，当某个条件为真时，执行相应的代码块。如果所有条件都为假，则不执行任何分支。

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686124880204-9b0c0e40-e74d-4339-83a2-70633ef4e9fa.png" width="542" title="" crop="0,0,1,1" id="ubb91fd37" class="ne-image">

1. if-else if-else if-else 语句

语法格式：

```java
if (布尔表达式 1) {
    // 如果布尔表达式 1 为真，则执行下面的代码块 1
} else if (布尔表达式 2) {
    // 如果布尔表达式 1 为假，且布尔表达式 2 为真，则执行下面的代码块 2
} else if (布尔表达式 3) {
    // 如果布尔表达式 1 和 2 都为假，且布尔表达式 3 为真，则执行下面的代码块 3
} else {
    // 如果布尔表达式 1 2 3 都为假，则执行这个代码块
}
```

说明：if-else if-else if-else 语句有多个条件，依次判断每一个条件，当某个条件为真时，执行相应的代码块。如果所有条件都为假，则执行 else 代码块。

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686125114083-1e94085c-e3d7-4796-804b-f4a76f4febb7.png" width="669" title="" crop="0,0,1,1" id="ub5fe4dd8" class="ne-image">

**练一练：**

第一题：编写一个程序，输入一个数字 num，判断它是否为正数、负数或零，并输出对应的信息。例如，如果 num 是正数，则输出"num 是正数"，如果 num 是负数，则输出"num 是负数"，如果 num 等于 0，则输出"num 等于 0"。

第二题：编写一个程序，输入一个学生的分数 score（百分制），根据成绩的不同输出不同的评价。如果学生的分数大于等于 90 分，则输出"你的成绩是优秀"；如果分数大于等于 80 分但小于 90 分，则输出"你的成绩是良好"；如果分数大于等于 70 分但小于 80 分，则输出"你的成绩是中等"；如果分数大于等于 60 分但小于 70 分，则输出"你的成绩是及格"；否则输出"你的成绩不及格"。

第三题：编写一个程序，输入一个年份 year 和一个月份 month，判断这个月份有多少天。判断方法如下：

1) 如果 month 为 1、3、5、7、8、10、12 中的一个，输出"month 有 31 天"；
2) 如果 month 为 4、6、9、11 中的一个，输出"month 有 30 天"；
3) 如果 month 为 2 并且 year 为闰年，输出"month 有 29 天"；（如果一个年份能够被 4 整除但不能被 100 整除，或者能够被 400 整除，那么它就是闰年）
4) 如果 month 为 2 并且 year 不是闰年，输出"month 有 28 天"。

对于 if 语句，我们需要注意的：

- 对于任何一个 if 语句来说，最多只能有一个分支执行。
- 分支中如果只有一条 Java 语句，大括号可以省略。
- 对于以上第 2 种和第 4 种，这两种写法是可以保证一定会有一个分支执行的。因为这两种写法都有 else 分支。
- 对于以上第 1 种和第 3 种，这两种写法可能会没有分支执行。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="TcnEa" class="ne-image">

#### switch 语句

switch 语句又叫做：**<font style="color:#DF2A3F;">选择语句</font>**。

完整的语法格式：

```java
switch(expression) {
    case value1:
        // 当 expression 的值等于 value1 时，执行这里的代码
        break;
    case value2:
        // 当 expression 的值等于 value2 时，执行这里的代码
        break;
    case value3:
        // 当 expression 的值等于 value3 时，执行这里的代码
        break;
    //...
    default:
        // 当 expression 的值与所有的 case 语句都不匹配时，执行这里的代码
}
```

其中，expression 表示要判断的表达式，value1、value2 等表示每个 case 语句要匹配的值。当 expression 的值与某个 case 语句中的值匹配时，程序就会执行对应的代码块。如果 expression 的值与所有的 case 语句都不匹配，则执行 default 语句块中的代码。

switch 语句执行原理如下：

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686203407310-7f9ba1b9-cebc-42c3-9545-7b8030abc44c.png" width="750" title="" crop="0,0,1,1" id="u8715a159" class="ne-image">

**在使用 switch 语句时需要注意以下几点：**

1. switch 语句只适用于对某一个变量进行多分支判断的情况，不适用于复杂的判断逻辑。
2. JDK7 之前，switch 只支持 int 类型、枚举类型，在 JDK7 之后，增加了对字符串类型的支持。
3. case 语句中的值必须是字面量，不能是变量。
4. case 语句中的值必须和 switch 后面的值是同一类型，或者能够相互转换。
5. case 可以合并。
6. 在每个 case 分支中要加上 break 语句，以避免 case 穿透现象。
7. 在 switch 语句中，一般都应该有一个 default 分支，用于处理一些特殊情况，以避免程序出错。（当然，default 语句不写，也不会编译报错。）
8. switch 语句中的 default 分支可以放在 switch 块的任意位置，但是通常建议将 default 分支放在所有 case 分支的最后面。（可读性好）

**if 语句和 switch 语句都是分支语句，他们有什么区别？switch 语句和 if 语句分别用于不同的编程场景和需求。**

if 语句用于根据一个或多个条件来控制程序的执行流程，例如：

```java
if (condition1) {
    // 处理语句 1
} else if (condition2) {
    // 处理语句 2
} else {
    // 处理语句 3
}
```

if 语句适用于针对多个条件进行判断和控制程序流程的情况。

switch 语句则用于根据不同的值来执行不同的代码块，例如：

```java
switch (value) {
    case value1:
        // 处理语句 1
        break;
    case value2:
        // 处理语句 2
        break;
    default:
        // 处理默认语句
}
```

switch 语句适用于对一个变量的多个可能取值进行判断和控制程序流程的情况。

switch 语句的优点是结构简洁，易于阅读，执行效率高，适合多个值的判断和处理。if 语句的优点是灵活性更强，可以根据多个条件来进行程序流程的判断和处理。

**练一练：**

1. 编写一个程序，根据输入的月份，输出该月份所属的季节。
2. 编写一个程序，根据输入的运算符符号，输出两个数的运算结果。例如输入符号为"+"，则输出两个数的和；输入符号为"-"，则输出两个数的差，以此类推。
3. 编写一个程序，根据输入的图形名称，输出对应图形的边数。例如输入"三角形"，则输出"三角形有 3 条边"，以此类推。
4. 编写一个程序，根据输入的成绩，输出对应的等级。例如输入成绩为 90~100，则输出"优秀"；输入成绩为 70~89，则输出"良好"，以此类推。

**Java12 之后，switch 语句又引入了新特性，让编码变的更加简洁：**

```java
int x = 1;
switch(x){
    case 1 -> System.out.println(1);
    case 2 -> System.out.println(2);
    default -> System.out.println("default");
}
```

```java
int x = 1;
switch(x){
    case 1, 2, 3 -> System.out.println("123");
    default -> System.out.println("default");
}
```

分支语句中如果有多条 Java 语句，可以使用代码块：

```java
int x = 1;
switch(x){
    case 1 -> {
        System.out.println(1);
        System.out.println(1);
    }
    case 2 -> System.out.println(2);
    default -> System.out.println("default");
}
```

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="G3Tvn" class="ne-image">

### 循环语句

当某代码片段需要频繁多次执行时，可以采用循环语句。循环语句包括：for、while、do-while

例如以下代码：

```java
System.out.println(1);
System.out.println(2);
System.out.println(3);
System.out.println(4);
System.out.println(5);
System.out.println(6);
System.out.println(7);
System.out.println(8);
System.out.println(9);
System.out.println(10);
```

可以使用循环简化代码：

```java
for(int i = 1; i <= 10; i++){
    System.out.println(i);
}
```

#### for 循环

语法格式：

```java
for(初始化表达式; 布尔表达式; 更新表达式){
    // 循环体
}
```

执行原理：

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686214924062-0c412879-ba9f-40c2-ac84-1f3e9fb27be7.png" width="767" title="" crop="0,0,1,1" id="uedb3074b" class="ne-image">

说明：

1. 初始化表达式：最先执行，并且只执行一次。
2. 布尔表达式：结果是 true 或者 false，用来决定循环是否继续。
3. 循环体：需要反复执行的代码片段。
4. 更新表达式：通常用来更新某个变量的值，让布尔表达式结果为 false，从而终止循环。
5. 初始化表达式，布尔表达式，更新表达式，都不是必须的，如果缺少布尔表达式，则默认为 true。
6. 初始化表达式中声明的变量只在循环中有效，循环结束后，变量不可访问。

**练一练：**

1. 输出 1~10
2. 输出 1~100 中所有的偶数
3. 输出 100, 97, 94, 91, ......, 1
4. 计算 1~100 所有奇数的和。
5. 计算 n 的阶乘。

for 循环嵌套

for 循环嵌套指的是在一个 for 循环的循环体中再嵌套另一个 for 循环。通过嵌套 for 循环，可以在外层循环的每次迭代中执行内层循环若干次。

例如，以下代码使用 for 循环嵌套打印九九乘法表：

```java
for (int i = 1; i <= 9; i++) {
    for (int j = 1; j <= i; j++) {
        System.out.print(j + " x " + i + " = " + i * j + "\t");
    }
    System.out.println();
}
```

这段代码中，外层循环的循环变量为 i，它的取值范围是 1 到 9，每次迭代时执行内层循环。内层循环的循环变量为 j，它的取值范围是 1 到 i，这样可以确保每行只打印到当前行数的结果。在内层循环中，打印出 j 和 i 的积，用 tab 键隔开，使结果排列整齐。

嵌套 for 循环可以用于处理多维数组、多重循环控制变量等场景，但如果嵌套层数过多，会导致代码难以理解和维护，影响代码可读性和可维护性，因此需要合理使用 for 循环嵌套，尽可能避免嵌套层数过多。

**练一练：**

1. 输出以下图形：

```plain
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
```

以下是其中一种实现方式：

```java
class DiamondPattern {
    public static void main(String[] args) {
        int n = 5; // 上半部分的行数（包括中间行）

        // 打印上半部分（包括中间行）
        for (int i = 0; i < n; i++) {
            // 打印前导空格
            for (int j = 0; j < i; j++) {
                System.out.print(" ");
            }
            // 打印星号
            for (int k = 0; k < 2 * (n - i) - 1; k++) {
                System.out.print("*");
            }
            System.out.println();
        }

        // 打印下半部分
        for (int i = n - 2; i >= 0; i--) {
            // 打印前导空格
            for (int j = 0; j < i; j++) {
                System.out.print(" ");
            }
            // 打印星号
            for (int k = 0; k < 2 * (n - i) - 1; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
```

2. 输出以下图形：

```plain
    1
   121
  12321
 1234321
123454321
```

以下是其中一种实现方式：

```java
class NumberPyramid {
    public static void main(String[] args) {
        int n = 5; // 金字塔的高度

        for (int i = 1; i <= n; i++) {
            // 打印前导空格
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            // 打印递增数字 (1 到 i)
            for (int k = 1; k <= i; k++) {
                System.out.print(k);
            }
            // 打印递减数字 (i-1 到 1)
            for (int k = i - 1; k >= 1; k--) {
                System.out.print(k);
            }
            System.out.println();
        }
    }
}
```

3. 找出 1~100 的所有质数（只能被 1 和自身整除的数叫做质数，1 除外，1 不是质数）。
4. 求 100 到 999 之间的水仙花数。水仙花数的每个位上的数字的 3 次幂之和等于它本身（例如：1^3 + 5^3 + 3^3 = 153）
5. 找出 1~1000 的所有质数，输出时每 8 个换一行。
6. 找 1~100 之间的质数，并输出两两相邻的质数差值等于 2 的质数对，例如（3，5），（5，7），（11，13），（17，19）等等。找出孪生质数/素数。

以下代码实现可作为参考：

```java
class TwinPrimes {
    public static void main(String[] args) {
        int pre = 2;
        for(int num = 2; num < 100; num++){
            boolean isPrime = true;
            for(int i = 2; i <= num / 2; i++){
                if(num % i == 0){
                    // 不是质数
                    isPrime = false;
                    // 终止循环
                    break;
                }
            }
            if(isPrime){
                if(num - pre == 2){
                    System.out.println("(" + pre + ", " + num + ")");
                }
                pre = num;
            }
        }
    }
}
```

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="sV2Hq" class="ne-image">

#### while 循环

语法格式：

```java
while(布尔表达式){
    // 循环体
}
```

执行原理：

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686282826740-78ebb78c-4497-42fb-8988-320c6be51c73.png" width="452" title="" crop="0,0,1,1" id="u2baa6fb7" class="ne-image">

循环体执行次数：0 ~ N 次。

使用 while 循环输出 1~10

```java
int i = 1;
while(i <= 10){
    System.out.println(i);
    i++;
}
```

以上程序当然也可以使用 for 循环完成

```java
for(int i = 1; i <= 10; i++){
    System.out.println(i);
}
```

while 和 for 如何选择？

如果循环次数已知，建议使用 for 循环。如果循环次数未知，需要通过不断的判断循环条件来决定是否继续下一次循环，建议使用 while 循环。

**练一练：**

1. 计算阶乘：要求用户输入一个正整数 n，使用 while 循环计算 n 的阶乘并输出。例如，输入 5，输出：120。
2. 猜数字小游戏：程序生成 1~100 之间的一个随机数，要求用户猜这个数是多少，程序做出相应的提示，如果猜中了则输出恭喜信息，并记录猜的次数，如果猜错了可以提示用户再猜一次。使用 while 循环实现游戏的主体流程。
3. 简单计算器：要求用户输入两个数字和一个运算符（加、减、乘、除），使用 while 循环计算并输出结果。如果用户输入的运算符不合法，可以提示用户重新输入。例如，输入 5 + 3，输出 8。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="MGP4L" class="ne-image">

#### do while 循环

语法格式：

```java
do {
    // 循环体
} while(布尔表达式);
```

执行原理：

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686286341115-5682821d-568a-4289-99e6-dfc09a6f9a67.png" width="462" title="" crop="0,0,1,1" id="ub10c30fe" class="ne-image">

循环体执行次数：1~N 次。（和 while 循环的区别就在这里。）

do while 循环比较适合的场景是：先执行一次，后判断的场景。

**练一练：**

1. 求平均数：要求用户输入一组数字，用 -1 表示输入结束，使用 do-while 循环计算这些数字的平均数并输出。要使用一个计数器来记录输入的数字个数，遇到 -1 则终止输入并计算平均数。
2. 翻转数字：要求用户输入一个正整数并使用 do-while 循环从最低位开始逐个输出每一位数字，实现数字的翻转。例如输入数字 123，则输出 321。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="yC1l7" class="ne-image">

### 跳转语句

跳转语句包括三个：

- break; 终止循环（也可以终止 switch 语句）。
- continue; 终止当前本次循环，直接进入下一次循环继续执行。
- return; 终止方法。

#### break

终止循环：

```java
public static void main(String[] args){
    for(int i = 0; i < 10; i++){
        if(i == 5){
            break;
        }
        System.out.println("i = " + i);
    }
    System.out.println("Hello World!");
}
```

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686287599466-93fe898e-c740-49e4-a0c2-5010088511ef.png" width="184" title="" crop="0,0,1,1" id="u1d69b3a1" class="ne-image">

如果循环嵌套，它默认终止的是哪个循环？

```java
public static void main(String[] args){
    for(int k = 0; k < 2; k++){
        for(int i = 0; i < 10; i++){
            if(i == 5){
                break;
            }
            System.out.println("i = " + i);
        }
    }
    System.out.println("Hello World!");
}
```

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686287712449-846caff9-3551-4ce4-9541-1716fae8cafd.png" width="224" title="" crop="0,0,1,1" id="u1c96895d" class="ne-image">

通过测试得知：break 语句默认终止的是离它最近的循环。（也就是说，默认终止的是当前循环）

可以指定终止某个循环吗？**<font style="color:#DF2A3F;">可以通过给循环打标签的方式来实现终止指定循环</font>**。

```java
public static void main(String[] args){
    for1:for(int k = 0; k < 2; k++){
        for2:for(int i = 0; i < 10; i++){
            if(i == 5){
                break for1;
            }
            System.out.println("i = " + i);
        }
    }
    System.out.println("Hello World!");
}
```

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686287842474-3d41633c-6758-451f-9b31-dcd030bf80f2.png" width="195" title="" crop="0,0,1,1" id="u304d37eb" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="vSMjX" class="ne-image">

#### continue

可以通过 continue 和 break 的对比来学习 continue 语句。看以下两个程序：

```java
public static void main(String[] args){
    for(int i = 0; i < 10; i++){
        if(i == 5){
            break;
        }
        System.out.println("i = " + i);
    }
    System.out.println("Hello World!");
}
```

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686287599466-93fe898e-c740-49e4-a0c2-5010088511ef.png" width="184" title="" crop="0,0,1,1" id="Q84Aq" class="ne-image">

```java
public static void main(String[] args){
    for(int i = 0; i < 10; i++){
        if(i == 5){
            continue;
        }
        System.out.println("i = " + i);
    }
    System.out.println("Hello World!");
}
```

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686288024801-95977cea-240d-48ae-8a20-0ec465eaaf6a.png" width="178" title="" crop="0,0,1,1" id="ud3212f45" class="ne-image">

通过测试得知：continue 语句只是终止当前本次循环，直接进入下一次循环继续执行。

continue 语句也支持打标签的方式，例如：continue for1; 这里不再赘述，可以自行测试。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="RoY6L" class="ne-image">

#### return

return 也可以通过与 break 语句的对比来进行学习。请看以下两段代码：

```java
public static void main(String[] args){
    for(int i = 0; i < 10; i++){
        if(i == 5){
            break;
        }
        System.out.println("i = " + i);
    }
    System.out.println("Hello World!");
}
```

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686287599466-93fe898e-c740-49e4-a0c2-5010088511ef.png" width="184" title="" crop="0,0,1,1" id="EmwGu" class="ne-image">

```java
public static void main(String[] args){
    for(int i = 0; i < 10; i++){
        if(i == 5){
            return;
        }
        System.out.println("i = " + i);
    }
    System.out.println("Hello World!");
}
```

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686288481951-4805bcff-3c9e-43ee-bfda-fcec80076cc2.png" width="155" title="" crop="0,0,1,1" id="u28c06c0d" class="ne-image">

可以清楚的看到，break 与 return 根本不是一个级别的。return 终止的是方法。

**练一练：**

1. 请编写一个程序，打印 1~100 所有的奇数，但是跳过所有以数字 3 结尾的数字。
2. 请设计一个程序，不断的从键盘上接收一个正整数或者负整数，要求计算所有正整数的和，如果接收到 0，则程序退出。
3. 韩信点兵，三人一组余两人，五人一组余三人，七人一组余四人，请问最少需要多少士兵

先自己写，然后再参考以下代码：

```java
public class HanxinPointSoldiersSimple {
    public static void main(String[] args) {
        int x = 1;
        while (true) {
            if (x % 3 == 2 && x % 5 == 3 && x % 7 == 4) {
                System.out.println("最少需要士兵数: " + x);
                break;
            }
            x++;
        }
    }
}
```

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="AMkZM" class="ne-image">

## 方法（掌握）

### 方法的作用

需求：编写程序，判断 103 和 107 是否为质数。如果不用方法，程序需要这样写：

```java
public static void main(String[] args){
    int num1 = 103;
    boolean f1 = true;
    for(int i = 2; i <= num1 / 2; i++){
        if(num1 % i == 0){
            f1 = false;
            break;
        }
    }
    System.out.println(f1 ? num1 + "是质数" : num1 + "不是质数");

    int num2 = 107;
    boolean f2 = true;
    for(int i = 2; i <= num2 / 2; i++){
        if(num2 % i == 0){
            f2 = false;
            break;
        }
    }
    System.out.println(f2 ? num2 + "是质数" : num2 + "不是质数");
}
```

可以看到，103 的判断逻辑和 107 的判断逻辑完全是一样的，导致相同的代码写了两次，显然代码没有得到重复使用（复用）。怎么办？使用 Java 中的方法可以解决：

```java
public static void main(String[] args){
    // 想用这个功能，直接调用就行了。
    judgingPrime(103);
    // 想用这个功能，直接调用就行了。
    judgingPrime(107);
}

// 专门判断某个整数数字是否为质数的方法。
public static void judgingPrime(int num){
    boolean flag = true;
    for(int i = 2; i <= num / 2; i++){
        if(num % i == 0){
            flag = false;
            break;
        }
    }
    System.out.println(flag ? num + "是质数" : num + "不是质数");
}
```

方法是什么，有什么用？

Java 中的方法（method）是：可以完成某个特定的功能，并且还可以被重复使用的代码片段。方法是一种封装代码逻辑的重要方式。在 C 语言中叫做函数。

Java 中的方法具有以下作用：

1. 代码重用：方法是一种模块化编程的方式，可以用来封装具有独立功能的代码块，避免重复编写相同的代码，提高代码的重用性。
2. 简化代码：通过将一组具有相似功能的代码封装到同一个方法中，可以简化程序的代码量，提高代码的可读性和可维护性。
3. 隐藏实现细节：方法允许封装具体逻辑，对外隐藏实现细节，只暴露方法的名字和参数，可以保护代码的安全性和完整性。
4. 提高程序的可扩展性：通过定义方法，程序开发人员可以很容易地扩展程序的功能，只需要在需要的地方添加相应的方法调用即可。
5. 分解复杂问题：当我们面对某一复杂问题时，将其分解为若干个较小的部分并用方法来实现，可以提高算法的实现效率，同时也方便了程序的调试和测试。
6. 提高程序的可读性：方法用来封装一定的功能，并起名为符合规范的逻辑名字，使程序代码更加清晰，易读，易懂。
7. 便于程序的测试和维护：通过将程序分解为多个方法，可以在程序中精准地调试，也能够更好地维护程序的代码。

总之，方法是 Java 程序中非常重要的组成部分，它们可以提高程序代码的可读性、可维护性、可扩展性和重用性，从而帮助我们更好地实现自己的代码逻辑。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="VecLr" class="ne-image">

### 方法的定义和调用

语法格式：

```java
[修饰符列表] 返回值类型 方法名(形式参数列表){
    方法体;
}
```

说明：

1. 修饰符列表：可选项。目前固定写法 public static，后面课程中再做介绍。
2. 返回值类型：用来指定方法返回值的数据类型（方法执行结束后的结果类型）。



好的，从“4. 循环语句：循环语句用于重复执行某一段代码，具体执行次数可以在开始前指定，”这里继续排版整理。

---

4. 循环语句：循环语句用于重复执行某一段代码，具体执行次数可以在开始前指定，也可以通过某个变量值或者条件来确定执行的次数。
   5. for
   6. while
   7. do while
8. 跳转语句：跳转语句用于改变代码的执行顺序，可以直接跳转到代码的某个位置。
   9. break
   10. continue
   11. return

控制语句在 Java 中具有非常重要的作用，可以根据执行条件来控制执行流程，提高代码的灵活性和可扩展性。通过使用控制语句，可以编写出更加高效、优雅和易于维护的代码。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="rOJoV" class="ne-image">

### 分支语句

分支语句包括：

- if 语句
- switch 语句

#### if 语句

if 语句又叫做**<font style="color:#DF2A3F;">条件控制语句</font>**。有以下四种写法：

1. if 语句

语法格式：

```java
if (布尔表达式) {
    // 如果布尔表达式为真，则执行下面的代码
}
```

说明：if 语句只有一个条件，当条件为真时，执行下面的代码块。

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686123487086-4fe63396-533a-4c3e-8b16-70f88b630d8e.png" width="230" title="" crop="0,0,1,1" id="n0e6z" class="ne-image">

**练一练：**

编写一个程序，输入一个人的年龄 age，如果他的年龄大于等于 18 岁，则输出"你已经成年了"，否则不输出任何东西。

编写一个程序，输入一个学生的分数 score（百分制），如果学生的分数大于等于 60，则输出"你已经及格了"，否则不输出任何东西。

编写一个程序，输入一个学生的分数 score（百分制），如果学生的分数大于等于 60，则输出"你已经及格了"，如果学生的分数小于 60，则输出"很抱歉，你不及格"。

2. if-else 语句

语法格式：

```java
if (布尔表达式) {
    // 如果布尔表达式为真，则执行下面的代码
} else {
    // 如果布尔表达式为假，则执行下面的代码
}
```

说明：if-else 语句有两个条件，当第一个条件为真时，执行 if 的代码块，否则执行 else 的代码块。

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686123813957-cd0dc709-840c-4d27-9710-0537b11630a8.png" width="355" title="" crop="0,0,1,1" id="u53588e86" class="ne-image">

**练一练：**

第一题：编写一个程序，输入一个学生的分数 score（百分制），如果学生的分数大于等于 60，则输出"你已经及格了"，如果学生的分数小于 60，则输出"很抱歉，你不及格"。

第二题：编写一个程序，输入一个数字 num，判断它是否为 7 的倍数。如果是，则输出"num 是 7 的倍数"，否则输出"num 不是 7 的倍数"。

第三题：编写一个程序，输入一个数字 num，判断它是否同时为 3 的倍数和 5 的倍数。如果是，则输出"num 既是 3 的倍数又是 5 的倍数"，否则输出"num 不同时是 3 的倍数和 5 的倍数"。

3. if-else if-else if 语句

语法格式：

```java
if (布尔表达式 1) {
    // 如果布尔表达式 1 为真，则执行下面的代码块 1
} else if (布尔表达式 2) {
    // 如果布尔表达式 1 为假，且布尔表达式 2 为真，则执行下面的代码块 2
} else if (布尔表达式 3) {
    // 如果布尔表达式 1 和 2 都为假，且布尔表达式 3 为真，则执行下面的代码块 3
}
```

说明：if-else if-else if 语句有多个条件，依次判断每一个条件，当某个条件为真时，执行相应的代码块。如果所有条件都为假，则不执行任何分支。

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686124880204-9b0c0e40-e74d-4339-83a2-70633ef4e9fa.png" width="542" title="" crop="0,0,1,1" id="ubb91fd37" class="ne-image">

4. if-else if-else if-else 语句

语法格式：

```java
if (布尔表达式 1) {
    // 如果布尔表达式 1 为真，则执行下面的代码块 1
} else if (布尔表达式 2) {
    // 如果布尔表达式 1 为假，且布尔表达式 2 为真，则执行下面的代码块 2
} else if (布尔表达式 3) {
    // 如果布尔表达式 1 和 2 都为假，且布尔表达式 3 为真，则执行下面的代码块 3
} else {
    // 如果布尔表达式 1 2 3 都为假，则执行这个代码块
}
```

说明：if-else if-else if-else 语句有多个条件，依次判断每一个条件，当某个条件为真时，执行相应的代码块。如果所有条件都为假，则执行 else 代码块。

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686125114083-1e94085c-e3d7-4796-804b-f4a76f4febb7.png" width="669" title="" crop="0,0,1,1" id="ub5fe4dd8" class="ne-image">

**练一练：**

第一题：编写一个程序，输入一个数字 num，判断它是否为正数、负数或零，并输出对应的信息。例如，如果 num 是正数，则输出"num 是正数"，如果 num 是负数，则输出"num 是负数"，如果 num 等于 0，则输出"num 等于 0"。

第二题：编写一个程序，输入一个学生的分数 score（百分制），根据成绩的不同输出不同的评价。如果学生的分数大于等于 90 分，则输出"你的成绩是优秀"；如果分数大于等于 80 分但小于 90 分，则输出"你的成绩是良好"；如果分数大于等于 70 分但小于 80 分，则输出"你的成绩是中等"；如果分数大于等于 60 分但小于 70 分，则输出"你的成绩是及格"；否则输出"你的成绩不及格"。

第三题：编写一个程序，输入一个年份 year 和一个月份 month，判断这个月份有多少天。判断方法如下：

1) 如果 month 为 1、3、5、7、8、10、12 中的一个，输出"month 有 31 天"；
2) 如果 month 为 4、6、9、11 中的一个，输出"month 有 30 天"；
3) 如果 month 为 2 并且 year 为闰年，输出"month 有 29 天"；（如果一个年份能够被 4 整除但不能被 100 整除，或者能够被 400 整除，那么它就是闰年）
4) 如果 month 为 2 并且 year 不是闰年，输出"month 有 28 天"。

对于 if 语句，我们需要注意的：

- 对于任何一个 if 语句来说，最多只能有一个分支执行。
- 分支中如果只有一条 Java 语句，大括号可以省略。
- 对于以上第 2 种和第 4 种，这两种写法是可以保证一定会有一个分支执行的。因为这两种写法都有 else 分支。
- 对于以上第 1 种和第 3 种，这两种写法可能会没有分支执行。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="TcnEa" class="ne-image">

#### switch 语句

switch 语句又叫做：**<font style="color:#DF2A3F;">选择语句</font>**。

完整的语法格式：

```java
switch(expression) {
    case value1:
        // 当 expression 的值等于 value1 时，执行这里的代码
        break;
    case value2:
        // 当 expression 的值等于 value2 时，执行这里的代码
        break;
    case value3:
        // 当 expression 的值等于 value3 时，执行这里的代码
        break;
    //...
    default:
        // 当 expression 的值与所有的 case 语句都不匹配时，执行这里的代码
}
```

其中，expression 表示要判断的表达式，value1、value2 等表示每个 case 语句要匹配的值。当 expression 的值与某个 case 语句中的值匹配时，程序就会执行对应的代码块。如果 expression 的值与所有的 case 语句都不匹配，则执行 default 语句块中的代码。

switch 语句执行原理如下：

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686203407310-7f9ba1b9-cebc-42c3-9545-7b8030abc44c.png" width="750" title="" crop="0,0,1,1" id="u8715a159" class="ne-image">

**在使用 switch 语句时需要注意以下几点：**

1. switch 语句只适用于对某一个变量进行多分支判断的情况，不适用于复杂的判断逻辑。
2. JDK7 之前，switch 只支持 int 类型、枚举类型，在 JDK7 之后，增加了对字符串类型的支持。
3. case 语句中的值必须是字面量，不能是变量。
4. case 语句中的值必须和 switch 后面的值是同一类型，或者能够相互转换。
5. case 可以合并。
6. 在每个 case 分支中要加上 break 语句，以避免 case 穿透现象。
7. 在 switch 语句中，一般都应该有一个 default 分支，用于处理一些特殊情况，以避免程序出错。（当然，default 语句不写，也不会编译报错。）
8. switch 语句中的 default 分支可以放在 switch 块的任意位置，但是通常建议将 default 分支放在所有 case 分支的最后面。（可读性好）

**if 语句和 switch 语句都是分支语句，他们有什么区别？switch 语句和 if 语句分别用于不同的编程场景和需求。**

if 语句用于根据一个或多个条件来控制程序的执行流程，例如：

```java
if (condition1) {
    // 处理语句 1
} else if (condition2) {
    // 处理语句 2
} else {
    // 处理语句 3
}
```

if 语句适用于针对多个条件进行判断和控制程序流程的情况。

switch 语句则用于根据不同的值来执行不同的代码块，例如：

```java
switch (value) {
    case value1:
        // 处理语句 1
        break;
    case value2:
        // 处理语句 2
        break;
    default:
        // 处理默认语句
}
```

switch 语句适用于对一个变量的多个可能取值进行判断和控制程序流程的情况。

switch 语句的优点是结构简洁，易于阅读，执行效率高，适合多个值的判断和处理。if 语句的优点是灵活性更强，可以根据多个条件来进行程序流程的判断和处理。

**练一练：**

1. 编写一个程序，根据输入的月份，输出该月份所属的季节。
2. 编写一个程序，根据输入的运算符符号，输出两个数的运算结果。例如输入符号为"+"，则输出两个数的和；输入符号为"-"，则输出两个数的差，以此类推。
3. 编写一个程序，根据输入的图形名称，输出对应图形的边数。例如输入"三角形"，则输出"三角形有 3 条边"，以此类推。
4. 编写一个程序，根据输入的成绩，输出对应的等级。例如输入成绩为 90~100，则输出"优秀"；输入成绩为 70~89，则输出"良好"，以此类推。

**Java12 之后，switch 语句又引入了新特性，让编码变的更加简洁：**

```java
int x = 1;
switch(x){
    case 1 -> System.out.println(1);
    case 2 -> System.out.println(2);
    default -> System.out.println("default");
}
```

```java
int x = 1;
switch(x){
    case 1, 2, 3 -> System.out.println("123");
    default -> System.out.println("default");
}
```

分支语句中如果有多条 Java 语句，可以使用代码块：

```java
int x = 1;
switch(x){
    case 1 -> {
        System.out.println(1);
        System.out.println(1);
    }
    case 2 -> System.out.println(2);
    default -> System.out.println("default");
}
```

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="G3Tvn" class="ne-image">

### 循环语句

当某代码片段需要频繁多次执行时，可以采用循环语句。循环语句包括：for、while、do-while

例如以下代码：

```java
System.out.println(1);
System.out.println(2);
System.out.println(3);
System.out.println(4);
System.out.println(5);
System.out.println(6);
System.out.println(7);
System.out.println(8);
System.out.println(9);
System.out.println(10);
```

可以使用循环简化代码：

```java
for(int i = 1; i <= 10; i++){
    System.out.println(i);
}
```

#### for 循环

语法格式：

```java
for(初始化表达式; 布尔表达式; 更新表达式){
    // 循环体
}
```

执行原理：

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686214924062-0c412879-ba9f-40c2-ac84-1f3e9fb27be7.png" width="767" title="" crop="0,0,1,1" id="uedb3074b" class="ne-image">

说明：

1. 初始化表达式：最先执行，并且只执行一次。
2. 布尔表达式：结果是 true 或者 false，用来决定循环是否继续。
3. 循环体：需要反复执行的代码片段。
4. 更新表达式：通常用来更新某个变量的值，让布尔表达式结果为 false，从而终止循环。
5. 初始化表达式，布尔表达式，更新表达式，都不是必须的，如果缺少布尔表达式，则默认为 true。
6. 初始化表达式中声明的变量只在循环中有效，循环结束后，变量不可访问。

**练一练：**

1. 输出 1~10
2. 输出 1~100 中所有的偶数
3. 输出 100, 97, 94, 91, ......, 1
4. 计算 1~100 所有奇数的和。
5. 计算 n 的阶乘。

for 循环嵌套

for 循环嵌套指的是在一个 for 循环的循环体中再嵌套另一个 for 循环。通过嵌套 for 循环，可以在外层循环的每次迭代中执行内层循环若干次。

例如，以下代码使用 for 循环嵌套打印九九乘法表：

```java
for (int i = 1; i <= 9; i++) {
    for (int j = 1; j <= i; j++) {
        System.out.print(j + " x " + i + " = " + i * j + "\t");
    }
    System.out.println();
}
```

这段代码中，外层循环的循环变量为 i，它的取值范围是 1 到 9，每次迭代时执行内层循环。内层循环的循环变量为 j，它的取值范围是 1 到 i，这样可以确保每行只打印到当前行数的结果。在内层循环中，打印出 j 和 i 的积，用 tab 键隔开，使结果排列整齐。

嵌套 for 循环可以用于处理多维数组、多重循环控制变量等场景，但如果嵌套层数过多，会导致代码难以理解和维护，影响代码可读性和可维护性，因此需要合理使用 for 循环嵌套，尽可能避免嵌套层数过多。

**练一练：**

1. 输出以下图形：

```plain
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
```

以下是其中一种实现方式：

```java
class DiamondPattern {
    public static void main(String[] args) {
        int n = 5; // 上半部分的行数（包括中间行）

        // 打印上半部分（包括中间行）
        for (int i = 0; i < n; i++) {
            // 打印前导空格
            for (int j = 0; j < i; j++) {
                System.out.print(" ");
            }
            // 打印星号
            for (int k = 0; k < 2 * (n - i) - 1; k++) {
                System.out.print("*");
            }
            System.out.println();
        }

        // 打印下半部分
        for (int i = n - 2; i >= 0; i--) {
            // 打印前导空格
            for (int j = 0; j < i; j++) {
                System.out.print(" ");
            }
            // 打印星号
            for (int k = 0; k < 2 * (n - i) - 1; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
```

2. 输出以下图形：

```plain
    1
   121
  12321
 1234321
123454321
```

以下是其中一种实现方式：

```java
class NumberPyramid {
    public static void main(String[] args) {
        int n = 5; // 金字塔的高度

        for (int i = 1; i <= n; i++) {
            // 打印前导空格
            for (int j = 1; j <= n - i; j++) {
                System.out.print(" ");
            }
            // 打印递增数字 (1 到 i)
            for (int k = 1; k <= i; k++) {
                System.out.print(k);
            }
            // 打印递减数字 (i-1 到 1)
            for (int k = i - 1; k >= 1; k--) {
                System.out.print(k);
            }
            System.out.println();
        }
    }
}
```

3. 找出 1~100 的所有质数（只能被 1 和自身整除的数叫做质数，1 除外，1 不是质数）。
4. 求 100 到 999 之间的水仙花数。水仙花数的每个位上的数字的 3 次幂之和等于它本身（例如：1^3 + 5^3 + 3^3 = 153）
5. 找出 1~1000 的所有质数，输出时每 8 个换一行。
6. 找 1~100 之间的质数，并输出两两相邻的质数差值等于 2 的质数对，例如（3，5），（5，7），（11，13），（17，19）等等。找出孪生质数/素数。

以下代码实现可作为参考：

```java
class TwinPrimes {
    public static void main(String[] args) {
        int pre = 2;
        for(int num = 2; num < 100; num++){
            boolean isPrime = true;
            for(int i = 2; i <= num / 2; i++){
                if(num % i == 0){
                    // 不是质数
                    isPrime = false;
                    // 终止循环
                    break;
                }
            }
            if(isPrime){
                if(num - pre == 2){
                    System.out.println("(" + pre + ", " + num + ")");
                }
                pre = num;
            }
        }
    }
}
```

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="sV2Hq" class="ne-image">

#### while 循环

语法格式：

```java
while(布尔表达式){
    // 循环体
}
```

执行原理：

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686282826740-78ebb78c-4497-42fb-8988-320c6be51c73.png" width="452" title="" crop="0,0,1,1" id="u2baa6fb7" class="ne-image">

循环体执行次数：0 ~ N 次。

使用 while 循环输出 1~10

```java
int i = 1;
while(i <= 10){
    System.out.println(i);
    i++;
}
```

以上程序当然也可以使用 for 循环完成

```java
for(int i = 1; i <= 10; i++){
    System.out.println(i);
}
```

while 和 for 如何选择？

如果循环次数已知，建议使用 for 循环。如果循环次数未知，需要通过不断的判断循环条件来决定是否继续下一次循环，建议使用 while 循环。

**练一练：**

1. 计算阶乘：要求用户输入一个正整数 n，使用 while 循环计算 n 的阶乘并输出。例如，输入 5，输出：120。
2. 猜数字小游戏：程序生成 1~100 之间的一个随机数，要求用户猜这个数是多少，程序做出相应的提示，如果猜中了则输出恭喜信息，并记录猜的次数，如果猜错了可以提示用户再猜一次。使用 while 循环实现游戏的主体流程。
3. 简单计算器：要求用户输入两个数字和一个运算符（加、减、乘、除），使用 while 循环计算并输出结果。如果用户输入的运算符不合法，可以提示用户重新输入。例如，输入 5 + 3，输出 8。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="MGP4L" class="ne-image">

#### do while 循环

语法格式：

```java
do {
    // 循环体
} while(布尔表达式);
```

执行原理：

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686286341115-5682821d-568a-4289-99e6-dfc09a6f9a67.png" width="462" title="" crop="0,0,1,1" id="ub10c30fe" class="ne-image">

循环体执行次数：1~N 次。（和 while 循环的区别就在这里。）

do while 循环比较适合的场景是：先执行一次，后判断的场景。

**练一练：**

1. 求平均数：要求用户输入一组数字，用 -1 表示输入结束，使用 do-while 循环计算这些数字的平均数并输出。要使用一个计数器来记录输入的数字个数，遇到 -1 则终止输入并计算平均数。
2. 翻转数字：要求用户输入一个正整数并使用 do-while 循环从最低位开始逐个输出每一位数字，实现数字的翻转。例如输入数字 123，则输出 321。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="yC1l7" class="ne-image">

### 跳转语句

跳转语句包括三个：

- break; 终止循环（也可以终止 switch 语句）。
- continue; 终止当前本次循环，直接进入下一次循环继续执行。
- return; 终止方法。

#### break

终止循环：

```java
public static void main(String[] args){
    for(int i = 0; i < 10; i++){
        if(i == 5){
            break;
        }
        System.out.println("i = " + i);
    }
    System.out.println("Hello World!");
}
```

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686287599466-93fe898e-c740-49e4-a0c2-5010088511ef.png" width="184" title="" crop="0,0,1,1" id="u1d69b3a1" class="ne-image">

如果循环嵌套，它默认终止的是哪个循环？

```java
public static void main(String[] args){
    for(int k = 0; k < 2; k++){
        for(int i = 0; i < 10; i++){
            if(i == 5){
                break;
            }
            System.out.println("i = " + i);
        }
    }
    System.out.println("Hello World!");
}
```

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686287712449-846caff9-3551-4ce4-9541-1716fae8cafd.png" width="224" title="" crop="0,0,1,1" id="u1c96895d" class="ne-image">

通过测试得知：break 语句默认终止的是离它最近的循环。（也就是说，默认终止的是当前循环）

可以指定终止某个循环吗？**<font style="color:#DF2A3F;">可以通过给循环打标签的方式来实现终止指定循环</font>**。

```java
public static void main(String[] args){
    for1:for(int k = 0; k < 2; k++){
        for2:for(int i = 0; i < 10; i++){
            if(i == 5){
                break for1;
            }
            System.out.println("i = " + i);
        }
    }
    System.out.println("Hello World!");
}
```

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686287842474-3d41633c-6758-451f-9b31-dcd030bf80f2.png" width="195" title="" crop="0,0,1,1" id="u304d37eb" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="vSMjX" class="ne-image">

#### continue

可以通过 continue 和 break 的对比来学习 continue 语句。看以下两个程序：

```java
public static void main(String[] args){
    for(int i = 0; i < 10; i++){
        if(i == 5){
            break;
        }
        System.out.println("i = " + i);
    }
    System.out.println("Hello World!");
}
```

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686287599466-93fe898e-c740-49e4-a0c2-5010088511ef.png" width="184" title="" crop="0,0,1,1" id="Q84Aq" class="ne-image">

```java
public static void main(String[] args){
    for(int i = 0; i < 10; i++){
        if(i == 5){
            continue;
        }
        System.out.println("i = " + i);
    }
    System.out.println("Hello World!");
}
```

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686288024801-95977cea-240d-48ae-8a20-0ec465eaaf6a.png" width="178" title="" crop="0,0,1,1" id="ud3212f45" class="ne-image">

通过测试得知：continue 语句只是终止当前本次循环，直接进入下一次循环继续执行。

continue 语句也支持打标签的方式，例如：continue for1; 这里不再赘述，可以自行测试。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="RoY6L" class="ne-image">

#### return

return 也可以通过与 break 语句的对比来进行学习。请看以下两段代码：

```java
public static void main(String[] args){
    for(int i = 0; i < 10; i++){
        if(i == 5){
            break;
        }
        System.out.println("i = " + i);
    }
    System.out.println("Hello World!");
}
```

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686287599466-93fe898e-c740-49e4-a0c2-5010088511ef.png" width="184" title="" crop="0,0,1,1" id="EmwGu" class="ne-image">

```java
public static void main(String[] args){
    for(int i = 0; i < 10; i++){
        if(i == 5){
            return;
        }
        System.out.println("i = " + i);
    }
    System.out.println("Hello World!");
}
```

<img src="https://cdn.nlark.com/yuque/0/2023/png/21376908/1686288481951-4805bcff-3c9e-43ee-bfda-fcec80076cc2.png" width="155" title="" crop="0,0,1,1" id="u28c06c0d" class="ne-image">

可以清楚的看到，break 与 return 根本不是一个级别的。return 终止的是方法。

**练一练：**

1. 请编写一个程序，打印 1~100 所有的奇数，但是跳过所有以数字 3 结尾的数字。
2. 请设计一个程序，不断的从键盘上接收一个正整数或者负整数，要求计算所有正整数的和，如果接收到 0，则程序退出。
3. 韩信点兵，三人一组余两人，五人一组余三人，七人一组余四人，请问最少需要多少士兵

先自己写，然后再参考以下代码：

```java
public class HanxinPointSoldiersSimple {
    public static void main(String[] args) {
        int x = 1;
        while (true) {
            if (x % 3 == 2 && x % 5 == 3 && x % 7 == 4) {
                System.out.println("最少需要士兵数: " + x);
                break;
            }
            x++;
        }
    }
}
```

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="AMkZM" class="ne-image">

## 方法（掌握）

### 方法的作用

需求：编写程序，判断 103 和 107 是否为质数。如果不用方法，程序需要这样写：

```java
public static void main(String[] args){
    int num1 = 103;
    boolean f1 = true;
    for(int i = 2; i <= num1 / 2; i++){
        if(num1 % i == 0){
            f1 = false;
            break;
        }
    }
    System.out.println(f1 ? num1 + "是质数" : num1 + "不是质数");

    int num2 = 107;
    boolean f2 = true;
    for(int i = 2; i <= num2 / 2; i++){
        if(num2 % i == 0){
            f2 = false;
            break;
        }
    }
    System.out.println(f2 ? num2 + "是质数" : num2 + "不是质数");
}
```

可以看到，103 的判断逻辑和 107 的判断逻辑完全是一样的，导致相同的代码写了两次，显然代码没有得到重复使用（复用）。怎么办？使用 Java 中的方法可以解决：

```java
public static void main(String[] args){
    // 想用这个功能，直接调用就行了。
    judgingPrime(103);
    // 想用这个功能，直接调用就行了。
    judgingPrime(107);
}

// 专门判断某个整数数字是否为质数的方法。
public static void judgingPrime(int num){
    boolean flag = true;
    for(int i = 2; i <= num / 2; i++){
        if(num % i == 0){
            flag = false;
            break;
        }
    }
    System.out.println(flag ? num + "是质数" : num + "不是质数");
}
```

方法是什么，有什么用？

Java 中的方法（method）是：可以完成某个特定的功能，并且还可以被重复使用的代码片段。方法是一种封装代码逻辑的重要方式。在 C 语言中叫做函数。

Java 中的方法具有以下作用：

1. 代码重用：方法是一种模块化编程的方式，可以用来封装具有独立功能的代码块，避免重复编写相同的代码，提高代码的重用性。
2. 简化代码：通过将一组具有相似功能的代码封装到同一个方法中，可以简化程序的代码量，提高代码的可读性和可维护性。
3. 隐藏实现细节：方法允许封装具体逻辑，对外隐藏实现细节，只暴露方法的名字和参数，可以保护代码的安全性和完整性。
4. 提高程序的可扩展性：通过定义方法，程序开发人员可以很容易地扩展程序的功能，只需要在需要的地方添加相应的方法调用即可。
5. 分解复杂问题：当我们面对某一复杂问题时，将其分解为若干个较小的部分并用方法来实现，可以提高算法的实现效率，同时也方便了程序的调试和测试。
6. 提高程序的可读性：方法用来封装一定的功能，并起名为符合规范的逻辑名字，使程序代码更加清晰，易读，易懂。
7. 便于程序的测试和维护：通过将程序分解为多个方法，可以在程序中精准地调试，也能够更好地维护程序的代码。

总之，方法是 Java 程序中非常重要的组成部分，它们可以提高程序代码的可读性、可维护性、可扩展性和重用性，从而帮助我们更好地实现自己的代码逻辑。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="VecLr" class="ne-image">

### 方法的定义和调用

语法格式：

```java
[修饰符列表] 返回值类型 方法名(形式参数列表){
    方法体;
}
```

说明：

1. 修饰符列表：可选项。目前固定写法 public static，后面课程中再做介绍。
2. 返回值类型：用来指定方法返回值的数据类型（方法执行结束后的结果类型）。只要是 Java 合法的数据类型，都可以，例如：byte, short, int, long, float, double, boolean, char, String...。如果方法执行结束时没有返回任何数据，返回值类型也不能空着，需要写 void 关键字。
3. 方法名：只要是合法的标识符即可。但最好见名知意。方法通常反应行为，所以方法名一般为动词。
4. 形式参数列表：简称形参。用来接收数据。参数个数 0~N 个。如果有多个，使用逗号隔开。例如（int a, double b, long c）。每一个形式参数都可以看做局部变量。
5. 每个方法都有方法体，方法体是一对大括号。在大括号中编写 Java 语句。
6. 方法的调用：如果修饰符列表中 static 关键字，采用“类名.方法名(实际参数列表);”调用方法。
   7. 调用者和被调用者在同一个类中，“类名.”可以省略。
   8. 实际参数列表：简称实参，实参和形参要一一对应，个数对应，数据类型对应。
9. 调用方法，如果方法执行结束后有返回值，可以采用变量接收该返回值。当然，也可以选择不接收。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="TUlar" class="ne-image">

### 方法执行时的内存变化

方法只定义不调用是不会分配内存的，只是方法的字节码指令存储在元空间中。

方法调用时会给该方法在 JVM 的栈内存中分配空间，此时发生压栈动作，这个方法的空间被称为栈帧。

栈帧中主要包括：局部变量表，操作数栈等。

方法执行结束时，该栈帧弹栈，方法内存空间释放。

**Java8 的 JVM 内存结构：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1758597438123-1cd291e4-7734-498f-b3ca-df42ce161d26.png" width="1910" title="" crop="0,0,1,1" id="uf8dd0421" class="ne-image">

代码如下：

```java
public class MethodTest08{
    public static void main(String[] args){
        System.out.println("main begin");
        int x = 10;
        add(x);
        System.out.println("main==>" + x);
        System.out.println("main end");
    }

    public static void add(int y){
        System.out.println("add begin");
        y++;
        minus(y);
        System.out.println("add ===> " + y);
        System.out.println("add end");
    }

    public static void minus(int z){
        System.out.println("minus begin");
        z--;
        System.out.println("minus ==> " + z);
        System.out.println("minus end");
    }
}
```

**方法执行时的内存变化：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1758598689082-0c83f0ff-5a12-4270-b55a-cd6128a0c175.png" width="466" title="" crop="0,0,1,1" id="u9d1b68a3" class="ne-image">

**比较经典的面试题：**

```java
public class MethodTest09{
    public static void main(String[] args){
        int x = 10;
        // 调用方法传递 x 的时候，实际上是把 x 变量中保存的 10 复制一份，传递过去了。
        add(x);
        System.out.println("main's x = " + x); // 10
    }

    public static void add(int x){
        x++;
        System.out.println("add's x = " + x); // 11
    }
}
```

### 方法重载

方法重载（overload）：编译阶段的一种机制（静态多态）

1. 什么情况下构成方法重载？
   2. 在同一个类中
   3. 方法名相同
   4. 参数列表不同
      1. 类型不同算不同
      2. 顺序不同算不同
      3. 个数不同算不同
5. 什么时候我们考虑使用方法重载？
   6. 在同一个类中，如果功能相似，建议使用方法重载。
7. 方法重载好处？
   8. 简化代码调用。
   9. 更易维护。
   10. 代码美观。

### 方法递归

1. 什么是方法的递归调用？
   2. 代码层面的形式就是方法自己调用自己。
3. 递归时，内存是如何变化的？要求能够画出递归时的内存变化。
4. 递归使用注意事项？
   5. 递归必须要有结束条件。
   6. 递归和循环都能完成的话，优先选择循环。（递归更耗费栈内存。）
7. 递归有结束条件，就一定不会栈内存溢出吗？
   8. 有时也会栈内存溢出，有时即使有结束条件，但递归的太深，栈内存不够的话，也会导致栈内存溢出错误的发生。
9. 实际开发中，使用递归时，发生栈内存溢出，你该怎么办？
   10. 先看看递归的结束条件是否合法。
   11. 如果确认递归结束条件正常，可以尝试通过配置扩大 JVM 的栈内存大小。

递归的代码：

```java
/*
方法的递归调用
1. 方法自己调用自己，就是方法的递归调用。
2. 递归调用很容易发生栈内存溢出错误：java.lang.StackOverflowError
3. 怎么避免栈内存溢出错误？递归必须要有结束条件。
4. 如果循环和递归都可以完成某个功能，建议优先选择循环。因为递归比较耗费内存。
5. 当递归有结束条件的时候，就一定不会发生栈内存溢出错误吗？
   不一定。有可能这个结束条件是正确的，但是递归的太深，仍然会出现栈内存溢出错误。
6. 在实际开发中我们如果遇到了栈内存溢出错误应该怎么办？
   第一步：先扩大栈内存。如果扩大之后没有用。怎么办？
   第二步：再次检查程序，看看递归的结束条件有没有问题。
   第三步：还是不行，就得换方案，不能用递归了。
*/
public class RecursionTest01{
    public static void main(String[] args){
        doSome();
        System.out.println("main over!");
    }

    public static void doSome(){
        System.out.println("doSome begin");
        doSome();
        System.out.println("doSome end");
    }
}
```

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1758608511810-e0006d0e-c4b5-4732-a8b7-c338a81bdbc8.png" width="565" title="" crop="0,0,1,1" id="ue07a214c" class="ne-image">

使用递归计算 1-n 的求和：

```java
public class RecursionTest02{
    public static void main(String[] args){
        int n = 5;
        int retValue = sum(n);
        System.out.println("1-" + n + "的和：" + retValue);
    }

    public static int sum(int n){
        if(n == 1){
            return 1;
        }
        return n + sum(n - 1);
    }
}
```

以上代码的内存图：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1758609397186-2ae64dcf-a170-48d9-ab6f-63b71beda123.png" width="695.2" title="" crop="0,0,1,1" id="u71faeace" class="ne-image">

**练一练：**

1. 使用递归计算 1~n 的求和。
2. 使用递归计算 n 的阶乘。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="YqRtg" class="ne-image">

## package 和 import

### package

1. 包机制作用：便于代码管理。
2. 怎么定义包：在 Java 源码第一行编写 package 语句。
   3. package 语句只能出现在 Java 代码第一行。
4. 包名命名规范
   5. 要求是全部小写。
   6. 公司域名倒序 + 项目名 + 模块名 + 功能名。例如：com.jkweilai.oa.emp.service
7. 带包编译：javac -d 编译后的存放目录 Java 源文件路径
8. 有了包机制后，完整类名是包含包名的，例如类名是：com.jkweilai.javase.chapter02.PackageTest

### import

1. import 语句用来引入其他类。
2. A 类中使用 B 类，A 类和 B 类不在同一个包下时，就需要在 A 类中使用 import 引入 B 类。
3. java.lang 包下的不需要手动引入。
4. import 语句只能出现在 package 语句之下，class 定义之前。
5. import 语句可以编写多个。
6. import 语句可以模糊导入：java.util.*;
7. import 静态导入：import static java.lang.System.*;

# 作业题

1. 猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又吃了一个，第二天早上又将剩下的桃子吃了一半，又多吃了一个，以后每天早上都是吃了前一天剩下的一半零一个，到第 10 天早上再吃的时候，发现只剩下一个桃子了，问一共多少个桃子。

先自己写，再参考以下代码：

```java
public class PeachCount {
    public static void main(String[] args) {
        int days = 10;
        int remaining = 1; // 第 10 天早上剩下的桃子数

        // 从第 9 天开始倒推，直到第 1 天
        for (int day = days - 1; day >= 1; day--) {
            remaining = (remaining + 1) * 2;
        }

        System.out.println("第一天摘的桃子总数为: " + remaining);
    }
}
```

2. 100 个和尚吃了 100 个馒头，100 和尚有大和尚和小和尚，一个大和尚能吃 3 馒头，三个小和尚吃 1 个馒头，问大和尚和小和尚有多少个？

先自己写，再参考以下代码：

```java
public class MonkProblem {
    public static void main(String[] args) {
        int totalMonks = 100;
        int totalBuns = 100;

        for (int bigMonks = 0; bigMonks <= totalMonks; bigMonks++) {
            int smallMonks = totalMonks - bigMonks;
            // 检查：9 * bigMonks + smallMonks == 300
            if (9 * bigMonks + smallMonks == 3 * totalBuns) {
                System.out.println("大和尚人数: " + bigMonks);
                System.out.println("小和尚人数: " + smallMonks);
                break;
            }
        }
    }
}
```

3. 已知一只公鸡 5 块钱，母鸡 3 块钱，小鸡 1 块钱 3 只，问 100 元买 100 只鸡有哪些方案？提示：如果拿 100 元买公鸡，最多买 20 个。如果拿 100 元买母鸡，最多买 33 个。如果拿 100 元买小鸡，最多买 300 只。

先自己写，再参考以下代码：

```java
public class ChickenProblemOptimized {
    public static void main(String[] args) {
        for (int i = 0; i <= 20; i++) {     // 公鸡数量
            for (int j = 0; j <= 33; j++) { // 母鸡数量
                int k = 100 - i - j;        // 小鸡数量
                if (k % 3 == 0 && i * 5 + j * 3 + k / 3 == 100) {
                    System.out.print("公鸡数量：" + i);
                    System.out.print("母鸡数量：" + j);
                    System.out.println("小鸡数量：" + k);
                }
            }
        }
    }
}
```
