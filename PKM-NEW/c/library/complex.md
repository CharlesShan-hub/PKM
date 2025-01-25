# complex.h


|  Macro Name   |  Expands To  |
| :---:| :---: |
|`complex`|`_Complex`|
|`imaginary`|`_Imaginary`|
|`_Complex_I`|(`const float _Complex`) `i`|
|`_Imaginary_I`|(`const float _Imaginary`) `i`|
|`I`|`_Imaginary_I`(`_Complex_I` if `_Imaginary_I` is absent)|

```c
#include <stdio.h>
#include <complex.h> // 包含对 _Complex 类型支持的函数和宏

int main()
{
    // 声明两个 _Complex 类型的变量
    double complex z1 = 3.0 + 2.0 * I; // 使用 I 宏表示虚数单位
    double complex z2 = 1.0 - 2.0 * I;

    // 打印原始复数
    printf("z1 = %f + %fi\n", creal(z1), cimag(z1));
    printf("z2 = %f + %fi\n", creal(z2), cimag(z2));

    // 复数加法
    _Complex double sum = z1 + z2;
    printf("Sum: %f + %fi\n", creal(sum), cimag(sum));

    // 复数减法
    _Complex double diff = z1 - z2;
    printf("Difference: %f + %fi\n", creal(diff), cimag(diff));

    // 复数乘法
    _Complex double product = z1 * z2;
    printf("Product: %f + %fi\n", creal(product), cimag(product));

    // 复数除法
    _Complex double quotient = z1 / z2;
    printf("Quotient: %f + %fi\n", creal(quotient), cimag(quotient));

    // 复数的模（绝对值）
    double magnitude = cabs(z1);
    printf("Magnitude of z1: %f\n", magnitude);

    return 0;
}
```