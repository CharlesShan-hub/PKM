
这段 C 语言代码演示了不同进制（二进制、八进制、十进制、十六进制）的整数字面量在内存中具有相同的值。它们只是数字的不同表示形式，而非不同的数据类型。

```c
#include <stdio.h>
int main()
{
    // 定义各种数据类型变量
    int binary_number = 0b1010011010;
    int octal_number = 01232;
    int decimal_number = 666;
    int hexadecimal_number = 0x29a;

    // 查看他们是否相等
    printf("%d", (int)(binary_number == octal_number));        // 1
    printf("%d", (int)(octal_number == decimal_number));       // 1
    printf("%d", (int)(decimal_number == hexadecimal_number)); // 1
    return 0;
}

```
