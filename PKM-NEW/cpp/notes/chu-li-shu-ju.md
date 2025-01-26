
# 处理数据

第3章处理数据:C++提供了内置类型来存储两种数据:整数(没有小数的数字)和浮点数(带小数的数字)。为满足程序员的各种需求，C++为每一种数据都提供了几个类型。本章将要讨论这些类型，包括创建变量和编写各种类型的常量。另外，还将讨论C++是 如何处理不同类型之间的隐式和显式转换的。

### 3.1 简单变量

#### 3.1.1 变量名

* 在名称中只能使用字母字符、数字和下划线 ( \_ )；
* 名称的第一个字符不能是数字；
* 区分大写字符与小写字符；
* 不能将C++关键字用作名称；
* <mark style="color:orange;">以</mark>_<mark style="color:orange;">两个下划线</mark>_ <mark style="color:orange;"></mark><mark style="color:orange;">或</mark> <mark style="color:orange;"></mark>_<mark style="color:orange;">下划线+大写字母</mark>_ <mark style="color:orange;"></mark><mark style="color:orange;">打头的名称被保留给实现（编译器及其使用的资源）使用</mark>；
* <mark style="color:orange;">以</mark> <mark style="color:orange;"></mark>_<mark style="color:orange;">一个下划线</mark>_ <mark style="color:orange;"></mark><mark style="color:orange;">开头的名称被保留给实现，用作全局标识符</mark>；
* C++对于名称的长度没有限制，名称中所有的字符都有意义，但有些平台有长度限制。

{% hint style="info" %}
倒数第二三点与前面几点有些不同，因为使用像 <mark style="color:orange;">\_\_time\_stop</mark> 或 <mark style="color:orange;">\_Donut</mark> 这样的名称不会导致编译器错误，而会导致行为的不确定性。换句话说，不知道结果将是什么。不出现编译器错误的原因是，这样的名称不 是非法的，但要留给实现使用。
{% endhint %}

{% hint style="warning" %}
TODO

命名风格
{% endhint %}

#### 3.1.2 整型

整数无限大，每一种 C++的整形只是数学上的整数的一部分。

#### 3.1.3 short、int、long、long long

1. 用 [climits.md](library/climits.md "mention") 来确定各种整形的最大最小值
2. 赋值竟然可以这样：`int a = {}; // 这个就是 0`，`int b = {100}; // 就是 100`

#### 3.1.4 无符号类型

why：比如人口等，不需要负数，无符号类型可以扩展数的范围

<details>

<summary>无符号类型的越界</summary>

```cpp
// exceed.cpp -- exceeding some integer limits
#include <iostream>
#define ZERO 0     // makes ZERO symbol for 0 value
#include <climits> // defines INT_MAX as largest int value
int main()
{
    using namespace std;
    short sam = SHRT_MAX;     // initialize a variable to max value
    unsigned short sue = sam; // okay if variable sam already defined

    cout << "Sam has " << sam << " dollars and Sue has " << sue;
    cout << " dollars deposited." << endl
         << "Add $1 to each account." << endl
         << "Now ";
    sam = sam + 1;
    sue = sue + 1;
    cout << "Sam has " << sam << " dollars and Sue has " << sue;
    cout << " dollars deposited.\nPoor Sam!" << endl;
    sam = ZERO;
    sue = ZERO;
    cout << "Sam has " << sam << " dollars and Sue has " << sue;
    cout << " dollars deposited." << endl;
    cout << "Take $1 from each account." << endl
         << "Now ";
    sam = sam - 1;
    sue = sue - 1;
    cout << "Sam has " << sam << " dollars and Sue has " << sue;
    cout << " dollars deposited." << endl
         << "Lucky Sue!" << endl;
    // cin.get();
    return 0;
}
```

```bash
(base) kimshan@MacBook-Pro output % ./"exceed"
Sam has 32767 dollars and Sue has 32767 dollars deposited.
Add $1 to each account.
Now Sam has -32768 dollars and Sue has 32768 dollars deposited.
Poor Sam!
Sam has 0 dollars and Sue has 0 dollars deposited.
Take $1 from each account.
Now Sam has -1 dollars and Sue has 65535 dollars deposited.
Lucky Sue!
```

</details>

#### 3.1.5 如何选择具体的整型

原则：能省则省

#### 3.1.6 整形字面量

<details>

<summary> 不同进制的字面量</summary>

<pre class="language-cpp"><code class="lang-cpp">// hexoct1.cpp -- shows hex and octal literals
#include &#x3C;iostream>
int main()
{
    using namespace std;
<strong>    int chest = 42;   // decimal integer literal
</strong><strong>    int waist = 0x42; // hexadecimal integer literal
</strong><strong>    int inseam = 042; // octal integer literal
</strong>
    cout &#x3C;&#x3C; "Monsieur cuts a striking figure!\n";
    cout &#x3C;&#x3C; "chest = " &#x3C;&#x3C; chest &#x3C;&#x3C; " (42 in decimal)\n";
    cout &#x3C;&#x3C; "waist = " &#x3C;&#x3C; waist &#x3C;&#x3C; " (0x42 in hex)\n";
    cout &#x3C;&#x3C; "inseam = " &#x3C;&#x3C; inseam &#x3C;&#x3C; " (042 in octal)\n";
    // cin.get();
    return 0;
}
</code></pre>

```
(base) kimshan@MacBook-Pro output % ./"hexoct1"
Monsieur cuts a striking figure!
chest = 42 (42 in decimal)
waist = 66 (0x42 in hex)
inseam = 34 (042 in octal)
```

</details>

<details>

<summary>print成不同进制：std::hex，std::oct</summary>

<pre class="language-cpp"><code class="lang-cpp">// hexoct2.cpp -- display values in hex and octal
#include &#x3C;iostream>
using namespace std;
int main()
{
    using namespace std;
    int chest = 42;
    int waist = 42; 
    int inseam = 42;

    cout &#x3C;&#x3C; "Monsieur cuts a striking figure!"  &#x3C;&#x3C; endl;
    cout &#x3C;&#x3C; "chest = " &#x3C;&#x3C; chest &#x3C;&#x3C; " (decimal for 42)" &#x3C;&#x3C; endl;
<strong>    cout &#x3C;&#x3C; hex;      // manipulator for changing number base
</strong>    cout &#x3C;&#x3C; "waist = " &#x3C;&#x3C; waist &#x3C;&#x3C; " (hexadecimal for 42)" &#x3C;&#x3C; endl;
<strong>    cout &#x3C;&#x3C; oct;      // manipulator for changing number base
</strong>    cout &#x3C;&#x3C; "inseam = " &#x3C;&#x3C; inseam &#x3C;&#x3C; " (octal for 42)" &#x3C;&#x3C; endl;
    // cin.get();
    return 0; 
}
</code></pre>

```
(base) kimshan@MacBook-Pro output % ./"hexoct2"
Monsieur cuts a striking figure!
chest = 42 (decimal for 42)
waist = 2a (hexadecimal for 42)
inseam = 52 (octal for 42)
```

</details>

#### 3.1.7 常量

<table><thead><tr><th width="81">进制</th><th width="106">int</th><th>long</th><th>long long</th></tr></thead><tbody><tr><td>十</td><td>1234</td><td>1234L 或 1234l</td><td>1234LL 或 1234ll</td></tr><tr><td>八</td><td>01234</td><td>01234L 或 01234l</td><td>01234LL 或 01234ll</td></tr><tr><td>十六</td><td>0x1234</td><td>0x1234L 或 0x1234l</td><td>0x1234LL 或 0x1234ll</td></tr></tbody></table>

#### 3.1.8 字符：ASCII（大小位 1 个字节）

<details>

<summary>1. cin 来输入一个字符</summary>

<pre class="language-cpp"><code class="lang-cpp">// chartype.cpp -- the char type
#include &#x3C;iostream>
int main()
{
    using namespace std;
    char ch; // declare a char variable

    cout &#x3C;&#x3C; "Enter a character: " &#x3C;&#x3C; endl;
<strong>    cin >> ch;
</strong>    cout &#x3C;&#x3C; "Hola! ";
    cout &#x3C;&#x3C; "Thank you for the " &#x3C;&#x3C; ch &#x3C;&#x3C; " character." &#x3C;&#x3C; endl;
    // cin.get();
    // cin.get();
    return 0;
}
</code></pre>

```
(base) kimshan@MacBook-Pro output % ./"chartype"
Enter a character: 
M
Hola! Thank you for the M character.
```

</details>

<details>

<summary>2. char and int</summary>

```cpp
// morechar.cpp -- the char type and int type contrasted
#include <iostream>
int main()
{
    using namespace std;
    char ch = 'M'; // assign ASCII code for M to ch
    int i = ch;    // store same code in an int
    cout << "The ASCII code for " << ch << " is " << i << endl;

    cout << "Add one to the character code:" << endl;
    ch = ch + 1; // change character code in ch
    i = ch;      // save new character code in i
    cout << "The ASCII code for " << ch << " is " << i << endl;

    // using the cout.put() member function to display a char
    cout << "Displaying char ch using cout.put(ch): ";
    cout.put(ch);

    // using cout.put() to display a char constant
    cout.put('!');

    cout << endl
         << "Done" << endl;
    // cin.get();
    return 0;
}
```

```
(base) kimshan@MacBook-Pro output % ./"morechar"
The ASCII code for M is 77
Add one to the character code:
The ASCII code for N is 78
Displaying char ch using cout.put(ch): N!
Done
```

</details>

<details>

<summary>3. 既生“&#x3C;&#x3C;”何生".put()" ：历史原因</summary>

答案与历史有关。在 C++的 Release 2.0 之前，cout 将字符变量显示为字符，而将字符常量(如 ‘M’和‘N’)显示为数字。问题是，C++的早期版本与 C 一样，也将把字符常量存储为 int 类型。也就是 说，‘M’的编码 77 将被存储在一个 16 位或 32 位的单元中。而 char 变量一般占 8 位。

遗憾的是，这意味着对 cout 来说，‘M’和 ch 看上去有天壤之别，虽然它们存储的值相同。因此，下 面的语句将打印$字符的 ASCII 码，而不是字符$：

```
cout << '$';
```

在Release 2.0之后，C++将字符常量存储为char类型，而不是int类型。这意味着cout现在可以正确 处理字符常量了。

</details>

4. 转义字符

| 字符名称         | ASCII符号 | C++代码 | 十进制ASCII码 | 十六进制ASCII码 |
| ------------ | ------- | ----- | --------- | ---------- |
| 换行符（NL (LF)） | NL(LF)  | `\n`  | 10        | 0xA        |
| 水平制表符（HT）    | HT      | `\t`  | 9         | 0x9        |
| 垂直制表符（VT）    | VT      | `\v`  | 11        | 0xB        |
| 退格（BS）       | BS      | `\b`  | 8         | 0x8        |
| 回车（CR）       | CR      | `\r`  | 13        | 0xD        |
| 振铃（BEL）      | BEL     | `\a`  | 7         | 0x7        |
| 反斜杠（\）       | \\      | `\\`  | 92        | 0x5C       |
| 问号（?）        | ?       | `\?`  | 63        | 0x3F       |
| 单引号（'）       | '       | `\'`  | 39        | 0x27       |
| 双引号（"）       | "       | `\"`  | 34        | 0x22       |

5. signed char 和 unsigned char

与 int 不同的是，char 在默认情况下既不是没有符号，也不是有符号。是否有符号由 C++实现决定， 这样编译器开发人员可以最大限度地将这种类型与硬件属性匹配起来。如果 char 有某种特定的行为对您来 说非常重要，则可以显式地将类型设置为 signed char 或 unsigned char

```cpp
char a; // 可能是有符号，也有可能无符号
unsigned char b; // 一定丝滑无符号
signed char c; // 一定是无符号
```

6. wcha\_t（宽字符类型）：用来表示比如日语，汉语这种 ASCII 表示不了的字符。

```cpp
wchar_t bob = L'P';
wcout << L"tall" << endl;
```

#### 3.1.7 bool

* true：true，非 0 的整数比如-1, 10
* false：false，整数 0

***

### 3.2 const 限定符

通用模板如下

```cpp
const 类型 名字 = value;
```

const 比 define 好：可以限制类型，可以更精确的控制作用域

***

### 3.3 浮点数

#### 3.3.1 书写浮点数

1. 直接写小数点：12.34，8.0
2. 科学计数法（E 和 e 都可以）：2.52e+8，8.33E-3，3.3e2

#### 3.3.2 浮点类型

<details>

<summary>Demo</summary>

```cpp
// floatnum.cpp -- floating-point types
#include <iostream>
int main()
{
    using namespace std; 
    cout.setf(ios_base::fixed, ios_base::floatfield); // fixed-point
    float tub = 10.0 / 3.0;     // good to about 6 places
    double mint = 10.0 / 3.0;   // good to about 15 places
    const float million = 1.0e6;

    cout << "tub = " << tub;
    cout << ", a million tubs = " << million * tub;
    cout << ",\nand ten million tubs = ";
    cout << 10 * million * tub << endl;

    cout << "mint = " << mint << " and a million mints = ";
    cout << million * mint << endl;
    // cin.get();
    return 0;
}
```

```
(base) kimshan@MacBook-Pro output % ./"floatnum"
tub = 3.333333, a million tubs = 3333333.250000,
and ten million tubs = 33333332.000000
mint = 3.333333 and a million mints = 3333333.333333
```

</details>

1. `cout.setf()`：用来重新定义输出的小数位数。floatfield 是 6，就是说保留六位小数。
2. 这个例子可以看出 float 和 double 的有效位的区别，float 只有 32-9=24bits 表示位数，也就是24/4=6 位有效数字。

{% hint style="info" %}
弹幕大神：因为尾数：2^23是8388608个数字，也就是没有触及边界的情况下，7位精确，但是触及边界就6位精确
{% endhint %}

#### 3.3.3 浮点常量

```cpp
1.234f   // float const
2.45E20F // float const
2.345E28 // double const
2.2L     // long double const
```

#### 3.3.4 浮点数的优缺点

<details>

<summary> 浮点数损失精度</summary>

```cpp
// fltadd.cpp -- precision problems with float
#include <iostream>
int main()
{
    using namespace std;
    float a = 2.34E+22f;
    float b = a + 1.0f;

    cout << "a = " << a << endl;
    cout << "b - a = " << b - a << endl;
    // cin.get();
    return 0;
}
```

```
(base) kimshan@MacBook-Pro output % ./"fltadd"
a = 2.34e+22
b - a = 0
```

</details>

***

### 3.4 C++算术运算符

#### 3.4.1 运算符优先级和结合性

```
+,-,*,/,%
```

取余数只能整数和整数运算

#### 3.4.2 除法分支

<details>

<summary>Demo</summary>

```cpp
// divide.cpp -- integer and floating-point division
// 如果两个操作数都是整数，则 C++将执行整数除法。
// 这意味着结果的小数部分将被丢弃，使得最后的结果是一个整数。
// 如果其中有一个(或两个)操作数是浮点值，则小数部分将保留，结果为浮点数
#include <iostream>
int main()
{
    using namespace std;
    cout.setf(ios_base::fixed, ios_base::floatfield);
    cout << "Integer division: 9/5 = " << 9 / 5  << endl;
    cout << "Floating-point division: 9.0/5.0 = ";
    cout << 9.0 / 5.0 << endl;
    cout << "Mixed division: 9.0/5 = " << 9.0 / 5  << endl;
    cout << "double constants: 1e7/9.0 = ";
    cout << 1.e7 / 9.0 <<  endl;
    cout << "float constants: 1e7f/9.0f = ";
    cout << 1.e7f / 9.0f <<  endl;
    // cin.get();
    return 0;
}
```

```
(base) kimshan@MacBook-Pro output % ./"divide"
Integer division: 9/5 = 1
Floating-point division: 9.0/5.0 = 1.800000
Mixed division: 9.0/5 = 1.800000
double constants: 1e7/9.0 = 1111111.111111
float constants: 1e7f/9.0f = 1111111.125000
```

</details>

#### 3.4.3 求模运算符

<details>

<summary>Demo</summary>

```cpp
// modulus.cpp -- uses % operator to convert lbs to stone
#include <iostream>
int main()
{
    using namespace std;
    const int Lbs_per_stn = 14;
    int lbs;

    cout << "Enter your weight in pounds: ";
    cin >> lbs;
    int stone = lbs / Lbs_per_stn;      // whole stone
    int pounds = lbs % Lbs_per_stn;     // remainder in pounds
    cout << lbs << " pounds are " << stone
         << " stone, " << pounds << " pound(s).\n";
    // cin.get();
    // cin.get();
    return 0; 
}

```

```
(base) kimshan@MacBook-Pro output % ./"modulus"
Enter your weight in pounds: 100
100 pounds are 7 stone, 2 pound(s).
```

</details>

#### 3.4.4 类型转换

情况：赋值，表达式求值，函数传参

<details>

<summary>Demo</summary>

```cpp
// assign.cpp -- type changes on assignment
#include <iostream>
int main()
{
    using namespace std;
    cout.setf(ios_base::fixed, ios_base::floatfield);
    float tree = 3;     // int converted to float
    int guess = 3.9832; // float converted to int
    int debt = 7.2E12;  // result not defined in C++
    cout << "tree = " << tree << endl;
    cout << "guess = " << guess << endl;
    cout << "debt = " << debt << endl;
    // cin.get();
    return 0;
}

```

```
(base) kimshan@MacBook-Pro output % ./"assign"
tree = 3.000000
guess = 3
debt = 4098
```

</details>

<details>

<summary>{}的初始化，不允许类型转换</summary>

```cpp
const int code = 66; // √
int x = 66; // √
char c1 {31325}; // √
char c2 = {66}; // √
char c3 {code}; // √
char c4 = {x}; // x  {}里边不能是变量
char c5 = x; // √
```

</details>

<details>

<summary>强制类型转换</summary>

```cpp
// typecast.cpp -- forcing type changes
#include <iostream>
int main()
{
    using namespace std;
    int auks, bats, coots;

    // the following statement adds the values as double,
    // then converts the result to int
    auks = 19.99 + 11.99;

    // these statements add values as int
    bats = (int) 19.99 + (int) 11.99;   // old C syntax
    coots = int (19.99) + int (11.99);  // new C++ syntax
    cout << "auks = " << auks << ", bats = " << bats;
    cout << ", coots = " << coots << endl;

    char ch = 'Z';
    cout << "The code for " << ch << " is ";    // print as char
    cout << int(ch) << endl;                    // print as int
    cout << "Yes, the code is ";
    cout << static_cast<int>(ch) << endl;       // using static_cast
   // cin.get();
    return 0; 
}

```

```
(base) kimshan@MacBook-Pro output % ./"typecast"
auks = 31, bats = 30, coots = 30
The code for Z is 90
Yes, the code is 90
```

</details>

#### 3.4.5 C++11 中的 auto 声明

使用关键字auto，而不指定变量的类型，编译器将把变量的类型设置成 与初始值相同（推断完就固定了，不能改了）

```cpp
auto a = 1.0;
auto b = 3;
```

其实 auto 更适合 STL，标准模块库

```cpp
std::vector<double> scores;
// std::vector<double>::iterator pv = scoress.begin();
auto pv = scoress.begin();
```





