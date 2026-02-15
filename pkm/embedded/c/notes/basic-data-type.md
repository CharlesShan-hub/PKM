# Basic Data Type
---
## Overview

![[../assets/datatype-drawing|1000]]
***

## 1. Integer

### 1.1. int, long, short, unsigned

1. 类型与大小

	|  |  短   | 中 |  长   |  长   |
	| :---: | :---: |:---: | :---: | :---: |
	|  有符号   | `short`,<br>`short int` | `int` | `long`,<br>`long int` | `long long`,<br>`long long int`  |
	|  无符号   | `unsigned short`,<br>`unsigned short int` | `unsigned`,<br>`unsigned int` | `unsigned long`,<br>`unsigned long int` | `unsigned long long`,<br>`unsigned long long int`  |

	👉 [查看自己电脑不同类型整数所占字节数](../details/integer-space.md)

2. 字面量与前缀：一个具体写在程序中的数字叫做字面量，加前缀用来表示不同的进制

	| 进制 | 案例 | 简介|
	| :---:|:---:|---|
	| 十进制（Decimal）|`65`|不加前缀，默认就是十进制|
	|二进制（Binary）|`0b1000001`|`0b`，`0B`|
	|八进制（Octal）|`0101`|`0`,（数字 0️⃣，不是字母 O）|
	| 十六进制（Hexadecimal）|`0x41`|`0x`，`0X`|

	 👉 [C语言进制案例与细节](../details/carry-system.md)

3. 打印与后缀：为字面量加入后缀，来代表它是不同的整数类型
	
	| type | printf | hexadecimal | octal | decimal |
	|:---:|:---:|:---:|:---:|:---:|
	|`char`|`%c`|`'\0x41'`|`'\0101'`||
	|`int`|`%d`|`0x41`|`0101`|`65`|
	|`unsigned int`|`%u`|`0x41u`|`0101u`|`65u`|
	|`long`|`%ld`|`0x41L`|`0101L`|`65L`|
	|`unsigned long`|`%lu`|`0x41UL`|`0101UL`|`65UL`|
	|`long long`|`%lld`|`0x41LL`|`0101LL`|`65LL`|
	|`unsigned long long`|`%llu`|`0x41ULL`|`0101ULL`|`65ULL`|

	👉 [使用整数来表示字符](../details/integer-represent-char.md)

4. 辅助工具

	* 各种整型的声明： 👉 [stdint](../library/stdint.md)
	* 各种整型的 printf：👉 [inttypes](../library/inttypes.md)
	* 各种整型的最值：👉 [limit](../library/limit.md)

### 1.2. char

1. 字符与字符串
	1. `char` 代表字符，采用 ASCII 码，占用内存 8 bits。
		* ✅：`char a = 'T';`
		* ❌：`char b = "T";`
	2. `char[]` 代表字符数组/字符串。
		* ✅：`char s[] = "T";`

2. 转义字符：特殊含义的字符

	|  转义序列  | 含义                                    |
	| :----: | ------------------------------------- |
	|  `\a`  | 警报（ANSI C）                            |
	|  `\b`  | 退格                                    |
	|  `\f`  | 换页                                    |
	|  `\n`  | 换行                                    |
	|  `\r`  | 回车                                    |
	|  `\t`  | 水平制表符                                 |
	|  `\v`  | 垂直制表符                                 |
	|  `\\`  | 反斜杠（\）                                |
	|  `\'`  | 单引号                                   |
	|  `\"`  | 双引号                                   |
	|  `\?`  | 问号                                    |
	| `\0oo` | 八进制值（oo必须是有效的八进制数，即每个o可表示0\~7中的一个数）   |
	| `\xhh` | 十六进制值（hh必须是有效的十六进制数，即每个h可表示0\~f中的一个数） |
### 1.3. \_Bool

* C99添加了布尔类型，占用 1bit。 我们可以直接就使用`_Bool`
* 也可以通过引入`stdbool.h`来使用`bool`，`true`代表1，`false`代表0
* 👉 [stdbool](../library/stdbool.md)

---
## 2. Decimal

### 2.1. float, double, long double

1. 占用字节数与表示范围

	| 类型          | 范围                      | 大小       |
	| ----------- | ----------------------- | -------- |
	| float       | 大约 -3.4e38 到 3.4e38     | 通常 4 字节  |
	| double      | 大约 -1.8e308 到 1.8e308   | 通常 8 字节  |
	| long double | 大约 -1.2e4932 到 1.2e4932 | 通常 16 字节 |

2. 浮点型常量
	1. 省略：可以省略整数部分或小数部分，但不能都省略
		```c
		double a = .0; // 正确，只省略整数
		float b = 2. // 正确，只省略小数
		float c = . // 错误，不能都省略
		```
	2. 科学计数法
		```c
		float d = .8E-5; // 正确，可以用e
		float e = .8e-5; // 正确，可以用E
		float f = .8 e-5; // 错误，不能有空格
		```
	3. 后缀
		```c
		float g = 4.0f; // 正确，可以用f，表示float
		float h = 9.11E9F; // 正确，可以用F，表示float
		double i = 4.0; // 正确，4.0默认就是double
		double j = 4.0l; // 正确，可以用l，表示double
		double k = 4.0L; // 正确，可以用L，表示double
		double l = 4.0 * 2.0; // 正确
		float m = 4.0 * 2.0; // 正确，但是double会被截断成float
		```
	4. （C99）16进制
		```c
		double n = 0xa.1fp10; // 0x代表16进制，p或P代表2的幂
		```

3. 不同格式的 printf, 前提`double num = 12345.6789;`（如果`num`是`long double`那么对应的都要加`L`, 比如`%Le`）

	| 类型       | 占位符 | Code Demo | Output |
	| :--------: | :---: | :---: | :---: |
	| 普通       | %f  | `printf("%f\n", num);` | `12345.678900` |
	| 10进制科学计数法（e） | %e  | `printf("%e\n", num);`| `1.234568e+04`|
	| 10进制科学计数法（E） | %E  |`printf("%E\n", num);`| `1.234568E+04`|
	| 16进制科学计数法（a） | %a  | `printf("%a\n", num);`| `0x1.81cd6e631f8a1p+13`|
	| 16进制科学计数法（A） | %A  |`printf("%A\n", num);`| `0X1.81CD6E631F8A1P+13`|
	| 自动选择     | %g  |`printf("%g\n", num);`| `12345.7`|


4. 浮点数会产生舍入误差（因为 float 可以表示的精度有限）

	```c
	#include <stdio.h>
	
	int main() {
	
	  printf("%f\n",2.0e20); // 200000000000000000000.000000
	
	  float a = 2.0e20;
	  printf("%f\n",a); // 200000004008175468544.000000
	
	  float b = a + 1;
	  printf("%f\n",b); // 200000004008175468544.000000
	
	  a = b - 2.0e20;
	  printf("%f\n",a); // 4008175468544.000000
	
	  return 0;
	}
	```

### 2.2. Complex, Imaginary

* C99
  * 复数：`float _Complex`, `double _Complex`, `long double _Complex`
  * 虚数：`float _Imaginary`, `double _Imaginary`, `long double _Imaginary`
* [complex.h](../library/complex.md)
  * 复数：`float complex`, `double complex`, `long double complex`
  * 虚数：`I`, `float imaginary`, `double imaginary`, `long double imaginary`

---

## 3. Type Casting

### 3.1. Auto Type Casting

1. **升级**（promotion），即从较小类型转换为较大类型。在不同类型的数进行运算时，会遵循将较小的类型转换到更大的类型的原则。
	![[../assets/auto-type-casting-drawing|1000]]
2. **降级**（demotion），即从较大类型转换为较小类型，通常发生在赋值语句中，有可能会发生阶段比如，浮点数到整数会丢掉小数部分，大的整数到小的整数会直接取模。

### 3.2. Forced Type Casting

1. 强制类型转换运算符（cast operator）：`(type)`
2. 案例

	```c
	#include <stdio.h> 
	int main() { 
		printf("Float to int: %d\n", (int)(123.456f)); 
		printf("Double to float: %f\n", (float)(123456789.123456789)); 
		printf("Int to char: %d\n", (char)(256)); 
		return 0; 
	}
	```
	
	```bash
	Float to int: 123
	Double to float: 123456792.000000
	Int to char: 0
	```
