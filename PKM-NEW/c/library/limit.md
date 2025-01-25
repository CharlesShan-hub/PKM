# limits.h

## Content

整数值的最大值和最小值非常有用，或者简单地说，任何整数类型的极限在编程中都起着重要作用。无需记住这些值，可以使用不同的宏。**\<climits>(limits.h)**定义整数类型的大小。\[2]

* 此头定义了用于特定系统和编译器实现的基本整数类型的限制常量。
* 基本浮点类型的限制在 \<cfloat> (\<float.h>) 中定义。&#x20;
* 宽度特定的整数类型和其他 typedef 类型的限制在 \<cstdint> (\<stdint.h>) 中定义。

<table><thead><tr><th width="187">name[1]</th><th>expresses</th><th>possible value*</th></tr></thead><tbody><tr><td>CHAR_BIT</td><td>Number of bits in a <code>char</code> object (byte)</td><td><code>8</code> or greater*</td></tr><tr><td>SCHAR_MIN</td><td>Minimum value for an object of type <code>signed char</code></td><td><code>-127</code> (<code>-27+1</code>) or less*</td></tr><tr><td>SCHAR_MAX</td><td>Maximum value for an object of type <code>signed char</code></td><td><code>127</code> (<code>27-1</code>) or greater*</td></tr><tr><td>UCHAR_MAX</td><td>Maximum value for an object of type <code>unsigned char</code></td><td><code>255</code> (<code>28-1</code>) or greater*</td></tr><tr><td>CHAR_MIN</td><td>Minimum value for an object of type <code>char</code></td><td>either SCHAR_MIN or <code>0</code></td></tr><tr><td>CHAR_MAX</td><td>Maximum value for an object of type <code>char</code></td><td>either SCHAR_MAX or UCHAR_MAX</td></tr><tr><td>MB_LEN_MAX</td><td>Maximum number of bytes in a multibyte character, for any locale</td><td><code>1</code> or greater*</td></tr><tr><td>SHRT_MIN</td><td>Minimum value for an object of type <code>short int</code></td><td><code>-32767</code> (<code>-215+1</code>) or less*</td></tr><tr><td>SHRT_MAX</td><td>Maximum value for an object of type <code>short int</code></td><td><code>32767</code> (<code>215-1</code>) or greater*</td></tr><tr><td>USHRT_MAX</td><td>Maximum value for an object of type <code>unsigned short int</code></td><td><code>65535</code> (<code>216-1</code>) or greater*</td></tr><tr><td>INT_MIN</td><td>Minimum value for an object of type <code>int</code></td><td><code>-32767</code> (<code>-215+1</code>) or less*</td></tr><tr><td>INT_MAX</td><td>Maximum value for an object of type <code>int</code></td><td><code>32767</code> (<code>215-1</code>) or greater*</td></tr><tr><td>UINT_MAX</td><td>Maximum value for an object of type <code>unsigned int</code></td><td><code>65535</code> (<code>216-1</code>) or greater*</td></tr><tr><td>LONG_MIN</td><td>Minimum value for an object of type <code>long int</code></td><td><code>-2147483647</code> (<code>-231+1</code>) or less*</td></tr><tr><td>LONG_MAX</td><td>Maximum value for an object of type <code>long int</code></td><td><code>2147483647</code> (<code>231-1</code>) or greater*</td></tr><tr><td>ULONG_MAX</td><td>Maximum value for an object of type <code>unsigned long int</code></td><td><code>4294967295</code> (<code>232-1</code>) or greater*</td></tr><tr><td>LLONG_MIN</td><td>Minimum value for an object of type <code>long long int</code></td><td><code>-9223372036854775807</code> (<code>-263+1</code>) or less*</td></tr><tr><td>LLONG_MAX</td><td>Maximum value for an object of type <code>long long int</code></td><td><code>9223372036854775807</code> (<code>263-1</code>) or greater*</td></tr><tr><td>ULLONG_MAX</td><td>Maximum value for an object of type <code>unsigned long long int</code></td><td><code>18446744073709551615</code> (<code>264-1</code>) or greater*</td></tr></tbody></table>


## Demo


```c
#include <stdio.h>
#include <limits.h>

int main() {
   printf("The value of CHAR_BIT: %d\n", CHAR_BIT);
   printf("The value of SCHAR_MIN: %d\n", SCHAR_MIN);
   printf("The value of SCHAR_MAX: %d\n", SCHAR_MAX);
   printf("The value of UCHAR_MAX: %u\n", UCHAR_MAX);
   printf("The value of CHAR_MIN: %d\n", CHAR_MIN);
   printf("The value of CHAR_MAX: %d\n", CHAR_MAX);
   printf("The value of MB_LEN_MAX: %d\n", MB_LEN_MAX);
   printf("The value of SHRT_MIN: %d\n", SHRT_MIN);
   printf("The value of SHRT_MAX: %d\n", SHRT_MAX);
   printf("The value of USHRT_MAX: %u\n", USHRT_MAX);
   printf("The value of INT_MIN: %d\n", INT_MIN);
   printf("The value of INT_MAX: %d\n", INT_MAX);
   printf("The value of UINT_MAX: %u\n", UINT_MAX);
   printf("The value of LONG_MIN: %ld\n", LONG_MIN);
   printf("The value of LONG_MAX: %ld\n", LONG_MAX);
   printf("The value of ULONG_MAX: %lu\n", ULONG_MAX);
   return 0;
}
```


```cpp
// limits.cpp -- some integer limits
#include <iostream>
#include <climits> // use limits.h for older systems
int main()
{
    using namespace std;
    int n_int = INT_MAX;      // initialize n_int to max int value
    short n_short = SHRT_MAX; // symbols defined in climits file
    long n_long = LONG_MAX;
    long long n_llong = LLONG_MAX;

    // sizeof operator yields size of type or of variable
    cout << "int is " << sizeof(int) << " bytes." << endl;
    cout << "short is " << sizeof n_short << " bytes." << endl;
    cout << "long is " << sizeof n_long << " bytes." << endl;
    cout << "long long is " << sizeof n_llong << " bytes." << endl;
    cout << endl;

    cout << "Maximum values:" << endl;
    cout << "int: " << n_int << endl;
    cout << "short: " << n_short << endl;
    cout << "long: " << n_long << endl;
    cout << "long long: " << n_llong << endl
         << endl;

    cout << "Minimum int value = " << INT_MIN << endl;
    cout << "Bits per byte = " << CHAR_BIT << endl;
    // cin.get();
    return 0;
}

// (base) kimshan@MacBook-Pro output % ./"limits"
// int is 4 bytes.
// short is 2 bytes.
// long is 8 bytes.
// long long is 8 bytes.

// Maximum values:
// int: 2147483647
// short: 32767
// long: 9223372036854775807
// long long: 9223372036854775807

// Minimum int value = -2147483648
// Bits per byte = 8
```


## Resources

\[1] [https://cplusplus.com/reference/climits/](https://cplusplus.com/reference/climits/)

\[2] [https://www.geeksforgeeks.org/climits-limits-h-cc/](https://www.geeksforgeeks.org/climits-limits-h-cc/)
