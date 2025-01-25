
# stdarg.h

## API

### Library Variables

Following is the variable type defined in the header stdarg.h −

<table><thead><tr><th width="71">No.</th><th>Variable &#x26; Description</th></tr></thead><tbody><tr><td>1</td><td><p>va_list</p><p>This is a type suitable for holding information needed by the three macros va_start(), va_arg() and va_end().</p></td></tr></tbody></table>

### Library Macros

Following are the macros defined in the header stdarg.h −

<table><thead><tr><th width="79">No.</th><th>Macro &#x26; Description</th></tr></thead><tbody><tr><td>1</td><td><p><a href="https://www.tutorialspoint.com/c_standard_library/c_macro_va_start.htm">void va_start(va_list ap, parmN)</a></p><p>This macro enables access to variadic function arguments.</p></td></tr><tr><td>2</td><td><p><a href="https://www.tutorialspoint.com/c_standard_library/c_macro_va_arg.htm">type va_arg(va_list ap, type)</a></p><p>This macro retrieves the next argument in the parameter list of the function with type type.</p></td></tr><tr><td>3</td><td><p><a href="https://www.tutorialspoint.com/c_standard_library/c_macro_va_end.htm">void va_end(va_list ap)</a></p><p>This macro allows to end traversal of the variadic function arguments.</p></td></tr><tr><td>4</td><td><p><a href="https://www.tutorialspoint.com/c_standard_library/c_macro_va_copy.htm">void va_copy( va_list dest, va_list src )</a></p><p>This macro makes a copy of the variadic function arguments.</p></td></tr></tbody></table>

## Demo

```c
#include <stdarg.h>
#include <stdio.h>

// 这是一个可变参数函数，它接受任意数量的整数参数
void print_numbers(int count, ...)
{
    va_list ap;
    va_start(ap, count); // 初始化va_list，设置参数列表的第一个参数

    // 使用va_arg宏遍历可变参数列表
    for (int i = 0; i < count; i++)
    {
        int number = va_arg(ap, int); // 获取下一个整数参数
        printf("Number %d: %d\n", i + 1, number);
    }

    va_end(ap); // 清理va_list，释放资源
}

int main()
{
    // 调用print_numbers函数，传递一个整数参数列表
    print_numbers(5, 1, 2, 3, 4, 5);

    return 0;
}

```
