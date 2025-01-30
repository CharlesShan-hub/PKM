# Arguments

---

## Overview

![[../assets/argument-drawing|1000]]

---

## Operater

![[../assets/operater-drawing|1000]]

### 基本运算符

* 赋值：`=`
  * 可以三重赋值：`int a,b,c; a = b = c = 1;`
  * 赋值的顺序是从右向左
* 加法：`+`
* 减法：`-`
* 符号：`-`与`+`（就是正负号，C90 才可以用）
* 乘法：`*`
* 除法：`/`
  * 如果是整数除法会截断，浮点数除法得到浮点数
* 取模：`%`
  * 不能用于浮点数
  * 负数怎么办
* 递增运算符：`++`
  * 前缀模式，后缀模式
  * 优先级：括号 > 递增递减 > 其他
* 递减运算符：`--`
* 比较：`==`，`>=`，`<=`，`<`，`>`

### 逻辑运算符

* 与或非：`&&`，`||`，`！`
* [[../library/iso646|👉 iso646]]

### 其他运算符

* `sizeof` 函数返回 `size_t` 类型的值，这是个无符号整型。
* C99 可以用 `%zd` 对应 `size_t` 类型的值，如果编译器支持也可以用 `%u` 或 `%lu`。

### 运算符优先级

| 运算符（优先级从高至低）     | 结合律      |
| ---------------- | -------- |
| ()               | 从左往右     |
| - + ++ -- sizeof | 从右往左     |
| \* / %           | 从左往右     |
| + -              | 从左往右     |
| < > <= >=        | 从左往右     |
| == !=            | 从左往右     |
| && \|\|          | **从右向左** |
| =                | 从右往左     |

### 不要自作聪明

`ans = num/2 + 5*(1 + num++);`

编译器会自己选择先运算`num/2`还是`5*(1 + num++)`

所以不要写这样的代码！

***

## Expression and Argument

C语言的六种语句
* 标号语句
* 复合语句
* 表达式语句
* 选择语句
* 迭代语句
* 跳转语句

* 表达式（expression）
  * <mark style="color:red;">每个表达式都有一个值</mark>。
  * 表达式是常量、变量或二者的组合。
* 语句（argument）
  * 语句是一条完整的计算机指令，以分号结尾（大多数）。
  * 单独一个分号叫做空语句。
  * `int a = 1;`这个语句去掉分号并不是表达式。
* 副作用（side effect）
  * c 语言的角度，它的目的是对表达式进行求值。如果改变了某个内存的数据，这个就是副作用。
  * 比如：`a = 5;`，求“5”本身是目的，把 5 存在了 a 是副作用。
  * （这么看有一种万物归一的感觉，表达式求值与改变内存进行了统一）
* 序列点（sequence point）
  * 程序执行的点：一个分号就是一个序列点，一个完整表达式的结束也算是一个序列点。
* 完整表达式（full expression）
  * 某个表达式并不是一个更大表达式的一部分
  * 比如：`while(i++ < 10) printf("%d \n", i);`，其中`i++ < 10`就是一个完整表达式。
  * 比如：，`y = (4+x++) + (6+x++)`，其中`4+x++`就不是一个完整表达式。因为程序无法保证x 在`4+x++`之后不再变化。

***

## Loop

### while

```c
while (expression)
    statement
```

* [[../details/while-example1|👉 while + scanf，循环输入]]
* [[../details/while-examples2|👉 while + getchar，输入一个字符串]]

### do while

```c
do
    statement
while(expression);
```

### for

```c
for(init; condition; update)
    statement
```

等价于

```c
init
for(;condition;)
{
    statement
    update
}
```

可以省略init，condition，update，statement任意位置

另外可以用逗号插入多个内容在一个语句里：`for(int i=1,j=2; i+j<100; i++,j++)`

***

## Branch

### if, else

```c
if(condition)
    statement1
else
    statement2
```

* [[../details/if-example|👉 example]]

### ?:（条件运算符）

```c
condition ? statement1 : statement2
```

注意， Rust 里边的 if else 是表达式，但是C 里边 if else 并不是表达式

```c
#include <stdio.h>

int main()
{
    int a = 100;
    int b = a == 100 ? a + 1 : a + 2;
    int c = (if (a == 100) a + 1 else a + 2); // wrong!
    return 0;
}
```


### break, continue

break和 continue 都是针对本轮循环

### switch

* 本质就是 if else
* switch的内容必须是整数或字符常量表达式，而不能是浮点数、字符串或其他数据类型
* [[../details/switch-example1|👉 switch简单案例]]
* 如果没有 break 就会进入下一个代码块，可以利用这个特性，制作多重标签：[[../details/switch-example2|👉案例]]

***

## Jump

### goto

唯一的 goto 使用场景：跳出多重循环（[[../details/goto-example|👉案例]]）