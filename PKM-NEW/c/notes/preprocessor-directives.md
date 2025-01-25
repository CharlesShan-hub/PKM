
# Preprocessor Directives

## 预处理器指令

<details>

<summary>所有的预处理器指令（GPT）</summary>



C语言的预处理器（Preprocessor）是一段特殊的代码处理程序，它负责在编译器实际编译源代码之前对源代码进行处理。预处理器指令以井号 `#` 开头，并且它们不是C语言语句的一部分，而是被编译器识别并执行的指令。以下是一些常用的C语言预处理器指令：

1. **`#include`**：文件包含指令，用于将一个文件的内容包含到另一个文件中。
2. `#include_next`：与 `#include` 类似，但优先级较低，只在没有 `#include` 指令时才会被处理。
3. `#include_alias`：为 `#include` 指令提供一个别名。
4. `#include_guard`：使用 `#ifndef` 和 `#define` 宏来保护头文件，防止重复包含。
5. **`#define`**：宏定义指令，用于定义一个宏，它会在编译时被替换。
6. **`#undef`**：取消宏定义，用于删除之前用 `#define` 定义的宏。
7. **`#if`**：条件编译指令，如果指定的条件为真，则编译随后的代码。
8. **`#elif`**：条件编译指令，如果之前的 `#if` 条件为假，且该 `#elif` 条件为真，则编译随后的代码。
9. **`#else`**：条件编译指令，与 `#if` 或 `#elif` 结合使用，当 `#if` 或 `#elif` 的条件都不为真时编译随后的代码。
10. **`#endif`**：结束条件编译指令，用于标记 `#if`、`#elif` 或 `#else` 块的结束。
11. **`#ifdef`**：条件编译指令，如果指定的宏已经被定义，则编译随后的代码。
12. **`#ifndef`**：条件编译指令，如果指定的宏没有被定义，则编译随后的代码。
13. **`#if defined`**：条件编译指令，如果指定的宏被定义，则编译随后的代码。
14. **`#if !defined`**：条件编译指令，如果指定的宏没有被定义，则编译随后的代码。
15. **`#elif defined`**：条件编译指令，如果之前的 `#if` 或 `#elif` 条件为假，且该 `#elif defined` 条件为真，则编译随后的代码。
16. **`#elif !defined`**：条件编译指令，如果之前的 `#if` 或 `#elif` 条件为假，且该 `#elif !defined` 条件为真，则编译随后的代码。
17. `#ifdef` 和 `#ifndef` 的别名：
    1. `#if defined` 和 `#if !defined` 的别名分别为 `#ifdef` 和 `#ifndef`。
    2. `#elif defined` 和 `#elif !defined` 的别名分别为 `#elif` 和 `#else`。
18. `#pragma`：指令，用于指定编译器的行为，如内存模型、浮点环境等。
19. `#line`：指令，用于改变编译器的行号，通常用于调试和生成错误消息。
20. `#error`：指令，用于在编译时生成一个错误信息。
21. `#warning`：指令，用于在编译时生成一个警告信息。
22. `#message`：指令，用于在编译时生成一个消息，通常用于调试。
23. `#assert`：指令，用于在编译时检查一个表达式是否为真，如果为假，则生成一个错误信息。

</details>

## #define

<details>

<summary>#define</summary>

<pre class="language-c"><code class="lang-c">/* preproc.c -- simple preprocessor examples */
#include &#x3C;stdio.h>
<strong>#define TWO 2        /* you can use comments if you like   */
</strong><strong>#define OW "Consistency is the last refuge of the unimagina\
</strong><strong>tive. - Oscar Wilde" /* a backslash continues a definition */
</strong>/* to the next line                   */
<strong>#define FOUR  TWO*TWO
</strong><strong>#define PX printf("X is %d.\n", x)
</strong><strong>#define FMT  "X is %d.\n"
</strong>
int main(void)
{
    int x = TWO;
    
    PX;
    x = FOUR;
    printf(FMT, x);
    printf("%s\n", OW);
    printf("TWO: OW\n");
    
    return 0;
}

// X is 2.
// X is 4.
// Consistency is the last refuge of the unimaginative. - Oscar Wilde
// TWO: OW
</code></pre>

</details>

<details>

<summary>#define(注意)</summary>

注意长段的空格或者注释会编译成一个空格

```c
#define SIX 2*3
#define SIX 2 * 3 // 这两样是不一样的！
```

</details>

<details>

<summary>#define(函数)</summary>



```c
/* mac_arg.c -- macros with arguments */
#include <stdio.h>
#define SQUARE(X) X *X
#define PR(X) printf("The result is %d.\n", X)
int main(void)
{
    int x = 5;
    int z;

    printf("x = %d\n", x);
    z = SQUARE(x);
    printf("Evaluating SQUARE(x): ");
    PR(z);
    z = SQUARE(2);
    printf("Evaluating SQUARE(2): ");
    PR(z);
    printf("Evaluating SQUARE(x+2): ");
    PR(SQUARE(x + 2));
    printf("Evaluating 100/SQUARE(2): ");
    PR(100 / SQUARE(2));
    printf("x is %d.\n", x);
    printf("Evaluating SQUARE(++x): ");
    PR(SQUARE(++x));
    printf("After incrementing, x is %x.\n", x);

    return 0;
}
// (base) kimshan@MacBook-Pro output % ./"mac_arg"
// x = 5
// Evaluating SQUARE(x): The result is 25.
// Evaluating SQUARE(2): The result is 4.
// Evaluating SQUARE(x+2): The result is 17.
// Evaluating 100/SQUARE(2): The result is 100.
// x is 5.
// Evaluating SQUARE(++x): The result is 42.
// After incrementing, x is 7.
```

</details>

<details>

<summary>#define(井号)</summary>



```c
/* subst.c -- substitute in string */
#include <stdio.h>
#define PSQR(x) printf("The square of " #x " is %d.\n", ((x) * (x)))

int main(void)
{
    int y = 5;

    PSQR(y);
    PSQR(2 + 4);

    return 0;
}

// (base) kimshan@MacBook-Pro output % ./"subst"
// The square of y is 25.
// The square of 2 + 4 is 36.
```

</details>

<details>

<summary>#dehine(x2, x3, x4, ....)</summary>



```c
// glue.c -- use the ## operator
#include <stdio.h>
#define XNAME(n) x ## n
#define PRINT_XN(n) printf("x" #n " = %d\n", x ## n);

int main(void)
{
    int XNAME(1) = 14;  // becomes int x1 = 14;
    int XNAME(2) = 20;  // becomes int x2 = 20;
    int x3 = 30;
    PRINT_XN(1);        // becomes printf("x1 = %d\n", x1);
    PRINT_XN(2);        // becomes printf("x2 = %d\n", x2);
    PRINT_XN(3);        // becomes printf("x3 = %d\n", x3);
    return 0;
}

```

</details>

<details>

<summary>变参宏</summary>

```c
// variadic.c -- variadic macros
#include <stdio.h>
#include <math.h>
#define PR(X, ...) printf("Message " #X ": " __VA_ARGS__)

int main(void)
{
    double x = 48;
    double y;

    y = sqrt(x);
    PR(1, "x = %g\n", x);
    PR(2, "x = %.2f, y = %.4f\n", x, y);

    return 0;
}

// Message 1: x = 48
// Message 2: x = 48.00, y = 6.9282
```

</details>



## #include

<details>

<summary>Demo</summary>

```c
#include <stdio.h> // 标准库
#include "utils.h" // 本地
#include "/usr/biff/p.h" // 绝对路径
```

</details>



## #undef、#ifdef、#ifndef、#else、#endif

<details>

<summary> 取消定义</summary>

```c
#define LIMIT 400
#undef LIMIT
```

</details>

<details>

<summary> 条件编译</summary>



<pre class="language-c"><code class="lang-c">/* ifdef.c -- uses conditional compilation */
#include &#x3C;stdio.h>
#define JUST_CHECKING
#define LIMIT 4

int main(void)
{
    int i;
    int total = 0;

    for (i = 1; i &#x3C;= LIMIT; i++)
    {
        total += 2*i*i + 1;
<strong>#ifdef JUST_CHECKING
</strong>        printf("i=%d, running total = %d\n", i, total);
#endif
    }
    printf("Grand total = %d\n", total);
    
    return 0;
}

// (base) kimshan@MacBook-Pro output % ./"ifdef"
// i=1, running total = 3
// i=2, running total = 12
// i=3, running total = 31
// i=4, running total = 64
// Grand total = 64
</code></pre>

</details>

<details>

<summary>ifndef</summary>



<pre class="language-cpp"><code class="lang-cpp">// names.h --revised with include protection

<strong>#ifndef NAMES_H_
</strong><strong>#define NAMES_H_
</strong>
// constants
#define SLEN 32

// structure declarations
struct names_st
{
    char first[SLEN];
    char last[SLEN];
};

// typedefs
typedef struct names_st names;

// function prototypes
void get_names(names *);
void show_names(const names *);
char * s_gets(char * st, int n);

#endif

</code></pre>

</details>

## #if, #elif, #else

<details>

<summary>demo</summary>

```c
#if SYS == 1
    #include "ibm.h"
#elif SYS == 2
    #include "vax.h"
#elif SYS == 3
    #include "mac.h"
#else
    #include "general.h"
#endif
```

```c
#if defined (IBMPC)
    #include "ibmpc.h"
#elif defined (VAX)
    #include "vax.h"
#elif defined (MAX)
    #inclue "mac.h"
#else
    #include "general.h"
```

</details>

## 预定宏

<table><thead><tr><th width="179">宏</th><th>含义</th></tr></thead><tbody><tr><td><strong>DATE</strong></td><td>预处理的日期（"Mmm dd yyyy"形式的字符串常量，如Nov 23 2013）</td></tr><tr><td><strong>FILE</strong></td><td>表示当前源代码文件名的字符串字面量</td></tr><tr><td><strong>LINE</strong></td><td>表示当前源代码文件中行号的整型常量</td></tr><tr><td><strong>STDC</strong></td><td>设置为1时，表明实现遵循C标准</td></tr><tr><td><strong>STDC_HOSTED</strong></td><td>本机环境设置为1；否则设置为0</td></tr><tr><td><strong>STDC_VERSION</strong></td><td>支持C99标准，设置为199901L；支持C11标准，设置为201112L</td></tr><tr><td><strong>TIME</strong></td><td>翻译代码的时间，格式为“hh:mm:ss”</td></tr></tbody></table>

<details>

<summary>Demo</summary>



```c
// predef.c -- predefined identifiers
#include <stdio.h>
void why_me();

int main()
{
    printf("The file is %s.\n", __FILE__);
    printf("The date is %s.\n", __DATE__);
    printf("The time is %s.\n", __TIME__);
    printf("The version is %ld.\n", __STDC_VERSION__);
    printf("This is line %d.\n", __LINE__);
    printf("This function is %s\n", __func__);
    why_me();

    return 0;
}

void why_me()
{
    printf("This function is %s\n", __func__);
    printf("This is line %d.\n", __LINE__);
}

// (base) kimshan@MacBook-Pro output % ./"predef"
// The file is /Volumes/Charles/books/C/C Primer Plus配套资料/Ch16/predef.c.
// The date is Sep  6 2024.
// The time is 14:51:47.
// The version is 201710.
// This is line 11.
// This function is main
// This function is why_me
// This is line 21.
// (base) kimshan@Mac
```

</details>

## #line、#error

\#line可以重置行号和文件名

\#error，这个需要 C11

## #pragma

<details>

<summary>#pragma 有什么用(GPT)</summary>

\#pragma 是一个指令，用于给编译器一些指示。它不是ISO C的一部分，不过大多数C/C++编译器都支持它，只是支持的pragma不同。 下面是一些常见的用法：

1. **打包结构**：`#pragma pack(push, 1)` 和 `#pragma pack(pop)` 可以用来改变结构的内存对齐方式，强制编译器按照指定的方式进行内存对齐。
2. **优化开关**：`#pragma optimize("on")` 和 `#pragma optimize("off")` 用于控制编译器的优化选项。
3. **警告抑制**：某些编译器允许通过#pragma来禁用特定的警告信息。
4. **指定段或函数属性**：在Windows平台上，可以使用#pragma来指定DLL导出的函数和数据。
5. **消息输出**：`#pragma message("`string`")` 可以让编译器输出自定义的消息到屏幕上。 不同的编译器可能支持不同的#pragma指令，因此在使用时需要参考具体的编译器文档。

</details>

## 泛型（C11）

<details>

<summary>Demo</summary>



```c
//  mytype.c

#include <stdio.h>

#define MYTYPE(X) _Generic((X),\
int: "int",\
float : "float",\
double: "double",\
default: "other"\
)

int main(void)
{
    int d = 5;
    
    printf("%s\n", MYTYPE(d));     // d is type int
    printf("%s\n", MYTYPE(2.0*d)); // 2.0* d is type double
    printf("%s\n", MYTYPE(3L));    // 3L is type long
    printf("%s\n", MYTYPE(&d));    // &d is type int *
    return 0;
}

// (base) kimshan@MacBook-Pro output % ./"mytype"
// int
// double
// other
// other
```

</details>

## 内联函数（C99）

普通函数通过堆栈调用。内联函数会把调用的地方替换成函数内容

<details>

<summary>Demo</summary>

在C语言中，`inline` 关键字用于告诉编译器将一个函数定义为内联函数。内联函数在调用时不会产生函数调用开销，因为它会在调用点直接展开成函数体代码。这通常用于函数体较小的函数，以减少函数调用的开销。 以下是一个简单的 C 语言内联函数的例子：

<pre class="language-c"><code class="lang-c">#include &#x3C;stdio.h>
// 定义一个内联函数，用于计算两个数的和
<strong>inline int add(int a, int b) {
</strong>    return a + b;
}
int main() {
    int x = 5;
    int y = 3;
    int sum = add(x, y); // 调用内联函数
    printf("The sum is: %d\n", sum);
    return 0;
}
</code></pre>

在这个例子中，`add` 函数被声明为 `inline`，这意味着编译器会在每次调用 `add` 函数时，直接将 `add` 函数的代码插入到调用点，而不是生成一个函数调用。这通常会提高程序的运行效率，特别是当函数体较小时。

</details>

## 问题集锦

1. define 和 const 的区别：`#define`会在编译的时候替换，`const`不会。
