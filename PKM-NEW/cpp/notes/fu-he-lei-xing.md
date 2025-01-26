# 复合类型

第4章 复合类型:C++让程序员能够使用基本的内置类型来创建更复杂的类型。最高级的形式是类（9～13章）。本章主要包括数组(存储多个同类型的值)、结构(存储多个不同类型的值)、指针(标识内存位置)。您还将学习如何创建和存储文本字符串及如何使用C风格字符数组和C++ string类来处理文本输入输出。最后，还将学习C++处理内存分配的方法，包括用于显式地管理内存的new和delete运算符。

### 4.1 数组

<details>

<summary>Demo</summary>

```cpp
// arrayone.cpp -- small arrays of integers
#include <iostream>
int main()
{
    using namespace std;
    int yams[3];    // creates array with three elements
    yams[0] = 7;    // assign value to first element
    yams[1] = 8;
    yams[2] = 6;

    int yamcosts[3] = {20, 30, 5}; // create, initialize array
    // int yamcosts[3]; // not allowed
    // yamcosts = {20, 30, 5}; // not allowed

    // NOTE: If your C++ compiler or translator can't initialize
    // this array, use static int yamcosts[3] instead of
    // int yamcosts[3]

    cout << "Total yams = ";
    cout << yams[0] + yams[1] + yams[2] << endl;
    cout << "The package with " << yams[1] << " yams costs ";
    cout << yamcosts[1] << " cents per yam.\n";
    int total = yams[0] * yamcosts[0] + yams[1] * yamcosts[1];
    total = total + yams[2] * yamcosts[2];
    cout << "The total yam expense is " << total << " cents.\n";

    cout << "\nSize of yams array = " << sizeof yams;
    cout << " bytes.\n";
    cout << "Size of one element = " << sizeof yams[0];
    cout << " bytes.\n";

    // cin.get();
    return 0; 
}

```

```
(base) kimshan@MacBook-Pro output % ./"arrayone"
Total yams = 21
The package with 8 yams costs 30 cents per yam.
The total yam expense is 410 cents.

Size of yams array = 12 bytes.
Size of one element = 4 bytes.
```

</details>

<details>

<summary>初始化</summary>

```cpp
// 赋值
int a[3] = {1,2,3};
// [1,2,3]
int b[3] = {1,2};
// [1,2,0]
int c[3] = {0};
// [0,0,0]

// 可以省略= （C++11）
int d[3] {1,2,3};
// [1,2,3]
int e[3] {0};
// [0,0,0]
```

</details>

***

### 4.2 字符串

参考：[cstring.md](library/cstring.md "mention")

<details>

<summary>cin，遇到空白 （空格、制表符和换行符）代表输入结束</summary>

```cpp
// strings.cpp -- storing strings in an array
#include <iostream>
#include <cstring>  // for the strlen() function
int main()
{
    using namespace std;
    const int Size = 15;
    char name1[Size];               // empty array
    char name2[Size] = "C++owboy";  // initialized array
    // NOTE: some implementations may require the static keyword
    // to initialize the array name2

    cout << "Howdy! I'm " << name2;
    cout << "! What's your name?\n";
    cin >> name1;
    cout << "Well, " << name1 << ", your name has ";
    cout << strlen(name1) << " letters and is stored\n";
    cout << "in an array of " << sizeof(name1) << " bytes.\n";
    cout << "Your initial is " << name1[0] << ".\n";
    name2[3] = '\0';                // set to null character
    cout << "Here are the first 3 characters of my name: ";
    cout << name2 << endl;
    // cin.get();
    // cin.get();
    return 0;
}

```

```
Howdy! I'm C++owboy! What's your name?
Charles
Well, Charles, your name has 7 letters and is stored
in an array of 15 bytes.
Your initial is C.
Here are the first 3 characters of my name: C++
```

</details>

<details>

<summary>cin.getline，遇到换行符代表输入结束，换行符可以被自动删掉</summary>

{% code title="错误的输入案例" %}
```cpp
// instr1.cpp -- reading more than one string
#include <iostream>
int main()
{
    using namespace std;
    const int ArSize = 20;
    char name[ArSize];
    char dessert[ArSize];

    cout << "Enter your name:\n";
    cin >> name;
    cout << "Enter your favorite dessert:\n";
    cin >> dessert;
    cout << "I have some delicious " << dessert;
    cout << " for you, " << name << ".\n";
    // cin.get();
	// cin.get();
    return 0; 
}
```
{% endcode %}

```
(base) kimshan@MacBook-Pro output % ./"instr1"
Enter your name:
Jassica Windy
Enter your favorite dessert:
I have some delicious Windy for you, Jassica.
```

{% code title="正确的" %}
```cpp
// instr2.cpp -- reading more than one word with getline
#include <iostream>
int main()
{
    using namespace std;
    const int ArSize = 20;
    char name[ArSize];
    char dessert[ArSize];

    cout << "Enter your name:\n";
    cin.getline(name, ArSize);  // reads through newline
    cout << "Enter your favorite dessert:\n";
    cin.getline(dessert, ArSize);
    cout << "I have some delicious " << dessert;
    cout << " for you, " << name << ".\n";
    // cin.get();
    return 0; 
}

```
{% endcode %}

```
(base) kimshan@MacBook-Pro output % ./"instr2"
Enter your name:
Jassica Windy
Enter your favorite dessert:
Cookie
I have some delicious Cookie for you, Jassica Windy.
```

</details>

<details>

<summary>cin.get，遇到换行符代表输入结束，换行符可以不被删掉，要再 get 一下</summary>

```cpp
// instr3.cpp -- reading more than one word with get() & get()
#include <iostream>
int main()
{
    using namespace std;
    const int ArSize = 20;
    char name[ArSize];
    char dessert[ArSize];

    cout << "Enter your name:\n";
    cin.get(name, ArSize).get();    // read string, newline
    cout << "Enter your favorite dessert:\n";
    cin.get(dessert, ArSize).get();
    cout << "I have some delicious " << dessert;
    cout << " for you, " << name << ".\n";
    // cin.get();
    return 0; 
}

```

```
(base) kimshan@MacBook-Pro output % ./"instr3"
Enter your name:
Tony's Fu
Enter your favorite dessert:
Soup
I have some delicious Soup for you, Tony's Fu.
```

</details>

<details>

<summary>输入混合的字符串和数字（cin 会留一个回车在缓冲区）</summary>

<pre class="language-cpp"><code class="lang-cpp">// numstr.cpp -- following number input with line input
#include &#x3C;iostream>
int main()
{
    using namespace std;
    cout &#x3C;&#x3C; "What year was your house built?\n";
    int year;
<strong>    (cin >> year).get();
</strong><strong>    // cin.get();
</strong>    cout &#x3C;&#x3C; "What is its street address?\n";
    char address[80];
    cin.getline(address, 80);
    cout &#x3C;&#x3C; "Year built: " &#x3C;&#x3C; year &#x3C;&#x3C; endl;
    cout &#x3C;&#x3C; "Address: " &#x3C;&#x3C; address &#x3C;&#x3C; endl;
    cout &#x3C;&#x3C; "Done!\n";
    // cin.get();
    return 0;
}

</code></pre>

```
(base) kimshan@MacBook-Pro output % ./"numstr"
What year was your house built?
2022
What is its street address?
No1
Year built: 2022
Address: No1
Done!
```

</details>

***

### 4.3 string类简介

C++98 加入了 std::string。string 可以自动调整大小，char\[]不可以。

<details>

<summary>char[] vs string</summary>

```cpp
// Init
char array1[20]; // √
char array2[20] = "Hello"; // √
char array3[] = "Hello"; // √
char array4[20] = {"Hello"}; // √
char array5[] = {"Hello"}; // √

string str1 = "Hello"; √
string str2 = {"Hello"}; √

// Assign
array1 = array2;// x
str1 = str2; // √

// 拼接
str1 += str2; // √
```

```cpp
// strtype2.cpp - assigning, adding, and appending
#include <iostream>
#include <string>               // make string class available
int main()
{
    using namespace std;
    string s1 = "penguin";
    string s2, s3;

    cout << "You can assign one string object to another: s2 = s1\n";
    s2 = s1;
    cout << "s1: " << s1 << ", s2: " << s2 << endl;
    cout << "You can assign a C-style string to a string object.\n";
    cout << "s2 = \"buzzard\"\n";
    s2 = "buzzard";
    cout << "s2: " << s2 << endl;
    cout << "You can concatenate strings: s3 = s1 + s2\n";
    s3 = s1 + s2;
    cout << "s3: " << s3 << endl;
    cout << "You can append strings.\n";
    s1 += s2;
    cout <<"s1 += s2 yields s1 = " << s1 << endl;
    s2 += " for a day";
    cout <<"s2 += \" for a day\" yields s2 = " << s2 << endl;

    //cin.get();
    return 0; 
}
```

```
(base) kimshan@MacBook-Pro output % ./"strtype2"
You can assign one string object to another: s2 = s1
s1: penguin, s2: penguin
You can assign a C-style string to a string object.
s2 = "buzzard"
s2: buzzard
You can concatenate strings: s3 = s1 + s2
s3: penguinbuzzard
You can append strings.
s1 += s2 yields s1 = penguinbuzzard
s2 += " for a day" yields s2 = buzzard for a day
```

</details>

<details>

<summary>string的其他操作，比如.size（class vs cstring）</summary>

```cpp
// strtype3.cpp -- more string class features
#include <iostream>
#include <string>               // make string class available
#include <cstring>              // C-style string library
int main()
{
    using namespace std;
    char charr1[20]; 
    char charr2[20] = "jaguar"; 
    string str1;  
    string str2 = "panther";

    // assignment for string objects and character arrays
    str1 = str2;                // copy str2 to str1
    strcpy(charr1, charr2);     // copy charr2 to charr1
 
    // appending for string objects and character arrays
    str1 += " paste";           // add paste to end of str1
    strcat(charr1, " juice");   // add juice to end of charr1

    // finding the length of a string object and a C-style string
    int len1 = str1.size();     // obtain length of str1
    int len2 = strlen(charr1);  // obtain length of charr1
 
    cout << "The string " << str1 << " contains "
         << len1 << " characters.\n";
    cout << "The string " << charr1 << " contains "
         << len2 << " characters.\n";
    // cin.get();

    return 0; 
}

```

```
(base) kimshan@MacBook-Pro output % ./"strtype3"
The string panther paste contains 13 characters.
The string jaguar juice contains 12 characters.
```

</details>

<details>

<summary>cin.getline(charr, 20); vs getline(cin, str);</summary>

```cpp
// strtype4.cpp -- line input
#include <iostream>
#include <string>               // make string class available
#include <cstring>              // C-style string library
int main()
{
    using namespace std;
    char charr[20]; 
    string str;

    cout << "Length of string in charr before input: " 
         << strlen(charr) << endl;
    cout << "Length of string in str before input: "
         << str.size() << endl;
    cout << "Enter a line of text:\n";
    cin.getline(charr, 20);     // indicate maximum length
    cout << "You entered: " << charr << endl;
    cout << "Enter another line of text:\n";
    getline(cin, str);          // cin now an argument; no length specifier
    cout << "You entered: " << str << endl;
    cout << "Length of string in charr after input: " 
         << strlen(charr) << endl;
    cout << "Length of string in str after input: "
         << str.size() << endl;
    // cin.get();

    return 0; 
}

```

```
(base) kimshan@MacBook-Pro output % ./"strtype4"
Length of string in charr before input: 0 
Length of string in str before input: 0
Enter a line of text:
qwertyuio
You entered: qwertyuio
Enter another line of text:
asdfghjkl
You entered: asdfghjkl
Length of string in charr after input: 9
Length of string in str after input: 9
```

</details>

***

### 4.4 结构简介

数组要求类型相同，结构可以是不同类型

<details>

<summary>Demo</summary>

<pre class="language-cpp"><code class="lang-cpp">// structur.cpp -- a simple structure
#include &#x3C;iostream>
struct inflatable   // structure declaration
{
    char name[20];
    float volume;
    double price;
};

int main()
{
    using namespace std;
    inflatable guest =
    {
        "Glorious Gloria",  // name value
        1.88,               // volume value
        29.99               // price value
    };  // guest is a structure variable of type inflatable
// It's initialized to the indicated values
<strong>    inflatable pal = // C++里边可以不写成 struct inflatable pal
</strong>    {
        "Audacious Arthur",
        3.12,
        32.99
    };  // pal is a second variable of type inflatable
// NOTE: some implementations require using
// static inflatable guest =

    cout &#x3C;&#x3C; "Expand your guest list with " &#x3C;&#x3C; guest.name;
    cout &#x3C;&#x3C; " and " &#x3C;&#x3C; pal.name &#x3C;&#x3C; "!\n";
// pal.name is the name member of the pal variable
    cout &#x3C;&#x3C; "You can have both for $";
    cout &#x3C;&#x3C; guest.price + pal.price &#x3C;&#x3C; "!\n";
    // cin.get();
    return 0; 
}

</code></pre>

```
(base) kimshan@MacBook-Pro output % ./"structur"
Expand your guest list with Glorious Gloria and Audacious Arthur!
You can have both for $62.98!
```

</details>

<details>

<summary>C++的结构体可以直接赋值！</summary>

<pre class="language-cpp"><code class="lang-cpp">// assgn_st.cpp -- assigning structures
#include &#x3C;iostream>
struct inflatable
{
    char name[20];
    float volume;
    double price;
};
int main()
{
    using namespace std;
    inflatable bouquet =
    {
        "sunflowers",
        0.20,
        12.49
    };
    inflatable choice;
    cout &#x3C;&#x3C; "bouquet: " &#x3C;&#x3C; bouquet.name &#x3C;&#x3C; " for $";
    cout &#x3C;&#x3C; bouquet.price &#x3C;&#x3C; endl;

<strong>    choice = bouquet;  // assign one structure to another
</strong>    cout &#x3C;&#x3C; "choice: " &#x3C;&#x3C; choice.name &#x3C;&#x3C; " for $";
    cout &#x3C;&#x3C; choice.price &#x3C;&#x3C; endl;
    // cin.get();
    return 0; 
}

</code></pre>

```
(base) kimshan@MacBook-Pro output % ./"assgn_st"
bouquet: sunflowers for $12.49
choice: sunflowers for $12.49
```

</details>

<details>

<summary>结构体数组</summary>

```cpp
// arrstruc.cpp -- an array of structures
#include <iostream>
struct inflatable
{
    char name[20];
    float volume;
    double price;
};
int main()
{
    using namespace std;
    inflatable guests[2] =          // initializing an array of structs
    {
        {"Bambi", 0.5, 21.99},      // first structure in array
        {"Godzilla", 2000, 565.99}  // next structure in array
    };

    cout << "The guests " << guests[0].name << " and " << guests[1].name
         << "\nhave a combined volume of "
         << guests[0].volume + guests[1].volume << " cubic feet.\n";
    // cin.get();
    return 0; 
}

```

```
(base) kimshan@MacBook-Pro output % ./"arrstruct"
The guests Bambi and Godzilla
have a combined volume of 2000.5 cubic feet.
```

</details>

***

### 4.5 共用体

只能存一个元素的结构体，用 union 关键字

***

### 4.6 枚举

<details>

<summary>Demo</summary>

```cpp
#include <iostream>
#include <climits>
#include <stdio.h>

enum spectrum
{
    red,
    orange,
    yellow,
    green,
    blue,
    violet,
    indigo,
    ultraviolt
};

int main()
{
    using namespace std;

    spectrum band;
    // 赋值给枚举
    band = blue; // √
    // band = 2; // x
    band = spectrum(2); // √

    // 枚举赋值给别人
    int num = band;
    cout << "num = " << num << ", band = " << band << endl; // num = 2, band = 2

    // enum spectrum1
    // {
    //     red,
    //     orange,
    //     yellow,
    //     green,
    //     blue,
    //     violet
    // };
    // 0,1,2,3,4,5
    // enum spectrum2
    // {
    //     red,
    //     orange,
    //     yellow = 10,
    //     green,
    //     blue,
    //     violet
    // };
    // 0,1,10,11,12,13

    spectrum r = red;
    spectrum b = blue;
    int c = r + b;           // √
    int d = spectrum(r + b); // √
    spectrum e = spectrum(r + b); // √

    return 0;
}
```

</details>

***

### 4.7 指针和自由存储空间

<details>

<summary>&#x26;取地址</summary>

<pre class="language-cpp"><code class="lang-cpp">// address.cpp -- using the &#x26; operator to find addresses
#include &#x3C;iostream>
int main()
{
    using namespace std;
    int donuts = 6;
    double cups = 4.5;

    cout &#x3C;&#x3C; "donuts value = " &#x3C;&#x3C; donuts;
<strong>    cout &#x3C;&#x3C; " and donuts address = " &#x3C;&#x3C; &#x26;donuts &#x3C;&#x3C; endl;
</strong>// NOTE: you may need to use unsigned (&#x26;donuts)
// and unsigned (&#x26;cups)
    cout &#x3C;&#x3C; "cups value = " &#x3C;&#x3C; cups;
<strong>    cout &#x3C;&#x3C; " and cups address = " &#x3C;&#x3C; &#x26;cups &#x3C;&#x3C; endl;
</strong>    // cin.get();
    return 0; 
}

</code></pre>

```
(base) kimshan@MacBook-Pro output % ./"address"
donuts value = 6 and donuts address = 0x7ff7b597c7f8
cups value = 4.5 and cups address = 0x7ff7b597c7f0
```

</details>

<details>

<summary>*解引用</summary>

```cpp
// pointer.cpp -- our first pointer variable
#include <iostream>
int main()
{
    using namespace std;
    int updates = 6;        // declare a variable
    int * p_updates;        // declare pointer to an int

    p_updates = &updates;   // assign address of int to pointer

// express values two ways
    cout << "Values: updates = " << updates;
    cout << ", *p_updates = " << *p_updates << endl;

// express address two ways
    cout << "Addresses: &updates = " << &updates;
    cout << ", p_updates = " << p_updates << endl;

// use pointer to change value
    *p_updates = *p_updates + 1;
    cout << "Now updates = " << updates << endl;
    // cin.get();
    return 0; 
}

```

```
(base) kimshan@MacBook-Pro output % ./"pointer"
Values: updates = 6, *p_updates = 6
Addresses: &updates = 0x7ff7b51f67f8, p_updates = 0x7ff7b51f67f8
Now updates = 7
```

</details>

<details>

<summary>指针初始化，C++中 int* 本身是一种复合类型</summary>

<pre class="language-cpp"><code class="lang-cpp">// init_ptr.cpp -- initialize a pointer
#include &#x3C;iostream>
int main()
{
    using namespace std;
    int higgens = 5;
<strong>    int * pt = &#x26;higgens;
</strong>
    cout &#x3C;&#x3C; "Value of higgens = " &#x3C;&#x3C; higgens
         &#x3C;&#x3C; "; Address of higgens = " &#x3C;&#x3C; &#x26;higgens &#x3C;&#x3C; endl;
    cout &#x3C;&#x3C; "Value of *pt = " &#x3C;&#x3C; *pt
         &#x3C;&#x3C; "; Value of pt = " &#x3C;&#x3C; pt &#x3C;&#x3C; endl;
    // cin.get();
    return 0; 
}

</code></pre>

```
(base) kimshan@MacBook-Pro output % ./"init_ptr"
Value of higgens = 5; Address of higgens = 0x7ff7b875b7f8
Value of *pt = 5; Value of pt = 0x7ff7b875b7f8
```

</details>

<details>

<summary>指针的危险</summary>

```cpp
// 不要这样
long *p;
*p = 2333333; // 这样就会把不知道什么地方的值改成了2333333
```

</details>

<details>

<summary>new（C 里边的malloc，C++用 new）</summary>

<pre class="language-cpp"><code class="lang-cpp">// use_new.cpp -- using the new operator
#include &#x3C;iostream>
int main()
{
    using namespace std;
    int nights = 1001;
<strong>    int * pt = new int;         // allocate space for an int
</strong>    *pt = 1001;                 // store a value there

    cout &#x3C;&#x3C; "nights value = ";
    cout &#x3C;&#x3C; nights &#x3C;&#x3C; ": location " &#x3C;&#x3C; &#x26;nights &#x3C;&#x3C; endl;
    cout &#x3C;&#x3C; "int ";
    cout &#x3C;&#x3C; "value = " &#x3C;&#x3C; *pt &#x3C;&#x3C; ": location = " &#x3C;&#x3C; pt &#x3C;&#x3C; endl;

<strong>    double * pd = new double;   // allocate space for a double
</strong>    *pd = 10000001.0;           // store a double there

    cout &#x3C;&#x3C; "double ";
    cout &#x3C;&#x3C; "value = " &#x3C;&#x3C; *pd &#x3C;&#x3C; ": location = " &#x3C;&#x3C; pd &#x3C;&#x3C; endl;
    cout &#x3C;&#x3C; "location of pointer pd: " &#x3C;&#x3C; &#x26;pd &#x3C;&#x3C; endl;
    cout &#x3C;&#x3C; "size of pt = " &#x3C;&#x3C; sizeof(pt);
    cout &#x3C;&#x3C; ": size of *pt = " &#x3C;&#x3C; sizeof(*pt) &#x3C;&#x3C; endl;
    cout &#x3C;&#x3C; "size of pd = " &#x3C;&#x3C; sizeof pd;
    cout &#x3C;&#x3C; ": size of *pd = " &#x3C;&#x3C; sizeof(*pd) &#x3C;&#x3C; endl;
    // cin.get();
    return 0;
}

</code></pre>

```
(base) kimshan@MacBook-Pro output % ./"use_new"
nights value = 1001: location 0x7ff7bf9de7f8
int value = 1001: location = 0x7fcef4f06030
double value = 1e+07: location = 0x7fcef4f06040
location of pointer pd: 0x7ff7bf9de7e8
size of pt = 8: size of *pt = 4
size of pd = 8: size of *pd = 8
```

</details>

<details>

<summary>数组的 new 和 delete</summary>

<pre class="language-cpp"><code class="lang-cpp">// arraynew.cpp -- using the new operator for arrays
#include &#x3C;iostream>
int main()
{
    using namespace std;
<strong>    double * p3 = new double [3]; // space for 3 doubles
</strong>    p3[0] = 0.2;                  // treat p3 like an array name
    p3[1] = 0.5;
    p3[2] = 0.8;
    cout &#x3C;&#x3C; "p3[1] is " &#x3C;&#x3C; p3[1] &#x3C;&#x3C; ".\n";
    p3 = p3 + 1;                  // increment the pointer
    cout &#x3C;&#x3C; "Now p3[0] is " &#x3C;&#x3C; p3[0] &#x3C;&#x3C; " and ";
    cout &#x3C;&#x3C; "p3[1] is " &#x3C;&#x3C; p3[1] &#x3C;&#x3C; ".\n";
    p3 = p3 - 1;                  // point back to beginning
<strong>    delete [] p3;                 // free the memory
</strong>    // cin.get();
    return 0; 
}

</code></pre>

```
(base) kimshan@MacBook-Pro output % ./"arraynew"
p3[1] is 0.5.
Now p3[0] is 0.5 and p3[1] is 0.8.
```

</details>

***

### 4.8 指针、数组和指针算数

<details>

<summary>Demo</summary>

1. `pw = pw + 1;`如果pw 指向 double，+1一下地址+8，如果 pw 指向 short，+1 一下地址+2
2. 数组和指针的区别来了！数组是常量，指针可以+1！

```cpp
// addpntrs.cpp -- pointer addition
#include <iostream>
int main()
{
    using namespace std;
    double wages[3] = {10000.0, 20000.0, 30000.0};
    short stacks[3] = {3, 2, 1};

// Here are two ways to get the address of an array
    double * pw = wages;     // name of an array = address
    short * ps = &stacks[0]; // or use address operator
// with array element
    cout << "pw = " << pw << ", *pw = " << *pw << endl;
    pw = pw + 1;
    cout << "add 1 to the pw pointer:\n";
    cout << "pw = " << pw << ", *pw = " << *pw << "\n\n";

    cout << "ps = " << ps << ", *ps = " << *ps << endl;
    ps = ps + 1;
    cout << "add 1 to the ps pointer:\n";
    cout << "ps = " << ps << ", *ps = " << *ps << "\n\n";

    cout << "access two elements with array notation\n";
    cout << "stacks[0] = " << stacks[0] 
         << ", stacks[1] = " << stacks[1] << endl;
    cout << "access two elements with pointer notation\n";

    cout << "*stacks = " << *stacks
         << ", *(stacks + 1) =  " << *(stacks + 1) << endl;

    cout << sizeof(wages) << " = size of wages array\n";
    cout << sizeof(pw) << " = size of pw pointer\n";
    // cin.get();
    return 0; 
}

```

```
(base) kimshan@MacBook-Pro output % ./"addpntrs"
pw = 0x7ff7b86cd7e0, *pw = 10000
add 1 to the pw pointer:
pw = 0x7ff7b86cd7e8, *pw = 20000

ps = 0x7ff7b86cd7d6, *ps = 3
add 1 to the ps pointer:
ps = 0x7ff7b86cd7d8, *ps = 2

access two elements with array notation
stacks[0] = 3, stacks[1] = 2
access two elements with pointer notation
*stacks = 3, *(stacks + 1) =  2
24 = size of wages array
8 = size of pw pointer
```

</details>

<details>

<summary>输入字符串（静态）</summary>

```cpp
// ptrstr.cpp -- using pointers to strings
#include <iostream>
#include <cstring>              // declare strlen(), strcpy()
int main()
{
    using namespace std;
    char animal[20] = "bear";   // animal holds bear
    const char * bird = "wren"; // bird holds address of string
    char * ps;                  // uninitialized

    cout << animal << " and ";  // display bear
    cout << bird << "\n";       // display wren
    // cout << ps << "\n";      //may display garbage, may cause a crash

    cout << "Enter a kind of animal: ";
    cin >> animal;              // ok if input < 20 chars
    // cin >> ps; Too horrible a blunder to try; ps doesn't
    //            point to allocated space

    ps = animal;                // set ps to point to string
    cout << ps << "!\n";       // ok, same as using animal
    cout << "Before using strcpy():\n";
    cout << animal << " at " << (int *) animal << endl;
    cout << ps << " at " << (int *) ps << endl;

    ps = new char[strlen(animal) + 1];  // get new storage
    strcpy(ps, animal);         // copy string to new storage
    cout << "After using strcpy():\n";
    cout << animal << " at " << (int *) animal << endl;
    cout << ps << " at " << (int *) ps << " " << &ps << endl;
    delete [] ps;
    return 0; 
}

```

```
(base) kimshan@MacBook-Pro output % ./"ptrstr"
bear and wren
Enter a kind of animal: snake
snake!
Before using strcpy():
snake at 0x7ff7b2c327e0
snake at 0x7ff7b2c327e0
After using strcpy():
snake at 0x7ff7b2c327e0
snake at 0x7faa28804080 0x7ff7b2c327c8
```

</details>

<details>

<summary>输入字符串（动态）</summary>

```cpp
// newstrct.cpp -- using new with a structure
#include <iostream>
struct inflatable   // structure definition
{
    char name[20];
    float volume;
    double price;
};
int main()
{
    using namespace std;
    inflatable * ps = new inflatable; // allot memory for structure
    cout << "Enter name of inflatable item: ";
    cin.get(ps->name, 20);            // method 1 for member access
    cout << "Enter volume in cubic feet: ";
    cin >> (*ps).volume;              // method 2 for member access
    cout << "Enter price: $";
    cin >> ps->price;
    cout << "Name: " << (*ps).name << endl;              // method 2
    cout << "Volume: " << ps->volume << " cubic feet\n"; // method 1
    cout << "Price: $" << ps->price << endl;             // method 1
    delete ps;                        // free memory used by structure
    // cin.get();
    // cin.get();
    return 0; 
}

```

```
(base) kimshan@MacBook-Pro output % ./"newstrct"
Enter name of inflatable item: Cookie  
Enter volume in cubic feet: 20
Enter price: $100
Name: Cookie
Volume: 20 cubic feet
Price: $100
```

</details>

<details>

<summary>delete来释放内存，然后重新输入</summary>

```cpp
// delete.cpp -- using the delete operator
#include <iostream>
#include <cstring>      // or string.h
using namespace std;
char * getname(void);   // function prototype
int main()
{
    char * name;        // create pointer but no storage
    name = getname();   // assign address of string to name

    cout << name << " at " << (int *) name << "\n";
    delete [] name;     // memory freed

    name = getname();   // reuse freed memory
    cout << name << " at " << (int *) name << "\n";
    delete [] name;     // memory freed again
    // cin.get();
    // cin.get();
    return 0;
}

char * getname()        // return pointer to new string
{
    char temp[80];      // temporary storage
    cout << "Enter last name: ";
    cin >> temp;
    char * pn = new char[strlen(temp) + 1];
    strcpy(pn, temp);   // copy string into smaller space

    return pn;          // temp lost when function ends
}

```

```
(base) kimshan@MacBook-Pro output % ./"delete"
Enter last name: Charles 
Charles at 0x7fcb09804080
Enter last name: Shan
Shan at 0x7fcb08f06030
```

</details>

***

### 4.9 类型组合

<details>

<summary>其实就是把上边的综合这些一个Demo</summary>

```cpp
// mixtypes.cpp --some type combinations
#include <iostream>

struct antarctica_years_end
{
    int year;
 /* some really interesting data, etc. */
};

int main()
{
    antarctica_years_end s01, s02, s03; 
    s01.year = 1998;
    antarctica_years_end * pa = &s02;
    pa->year = 1999;
    antarctica_years_end trio[3]; // array of 3 structures
    trio[0].year = 2003;
    std::cout << trio->year << std::endl;
    const antarctica_years_end * arp[3] = {&s01, &s02, &s03};
    std::cout << arp[1]->year << std::endl;
    const antarctica_years_end ** ppa = arp; 
    auto ppb = arp; // C++0x automatic type deduction
// or else use const antarctica_years_end ** ppb = arp; 
    std::cout << (*ppa)->year << std::endl;
    std::cout << (*(ppb+1))->year << std::endl;
    // std::cin.get();
    return 0;
}
```

```
(base) kimshan@MacBook-Pro output % ./"mixtypes"
2003
1999
1998
1999
```

</details>

***

### 4.10 数组的替代品

<details>

<summary>vector</summary>

```cpp
#include <iostream>
#include <vector>

int main()
{
    using namespace std;
    // 创建一个空的 vector 来存储整数
    vector<int> numbers;

    // 向 vector 添加一些元素
    numbers.push_back(10);
    numbers.push_back(20);
    numbers.push_back(30);
    numbers.push_back(40);
    numbers.push_back(50);

    // 输出 vector 中的元素
    cout << "Vector contains:" << endl;
    for (int i = 0; i < numbers.size(); ++i)
    {
        cout << "Element at index " << i << ": " << numbers[i] << endl;
    }

    // 使用迭代器来访问 vector 中的元素
    cout << "Accessing elements using iterators:" << endl;
    for (vector<int>::iterator it = numbers.begin(); it != numbers.end(); ++it)
    {
        cout << *it << " ";
    }
    cout << endl;

    // 修改 vector 中的元素
    numbers[2] = 300; // 将索引为 2 的元素修改为 300

    // 再次输出 vector 中的元素，查看修改结果
    cout << "After modification, vector contains:" << endl;
    for (int number : numbers)
    {
        cout << number << " ";
    }
    cout << endl;

    // 删除 vector 中的最后一个元素
    numbers.pop_back();

    // 输出 vector 中的元素数量
    cout << "The vector now contains " << numbers.size() << " elements." << endl;

    return 0;
}

```

```
(base) kimshan@MacBook-Pro output % ./"test1"
Vector contains:
Element at index 0: 10
Element at index 1: 20
Element at index 2: 30
Element at index 3: 40
Element at index 4: 50
Accessing elements using iterators:
10 20 30 40 50 
After modification, vector contains:
10 20 300 40 50 
The vector now contains 4 elements.
```

</details>

<details>

<summary>array</summary>

```cpp
// choices.cpp -- array variations
#include <iostream>
#include <vector>   // STL C++98
#include <array>    // C++0x
int main()
{
    using namespace std;
// C, original C++
    double a1[4] = {1.2, 2.4, 3.6, 4.8};
// C++98 STL
    vector<double> a2(4);   // create vector with 4 elements
// no simple way to initialize in C98
    a2[0] = 1.0/3.0;
    a2[1] = 1.0/5.0;
    a2[2] = 1.0/7.0;
    a2[3] = 1.0/9.0;
// C++0x -- create and initialize array object
    array<double, 4> a3 = {3.14, 2.72, 1.62, 1.41};  
    array<double, 4> a4;
    a4 = a3;     // valid for array objects of same size
// use array notation
    cout << "a1[2]: " << a1[2] << " at " << &a1[2] << endl;
    cout << "a2[2]: " << a2[2] << " at " << &a2[2] << endl;
    cout << "a3[2]: " << a3[2] << " at " << &a3[2] << endl;
    cout << "a4[2]: " << a4[2] << " at " << &a4[2] << endl;
// misdeed
    a1[-2] = 20.2;
    cout << "a1[-2]: " << a1[-2] <<" at " << &a1[-2] << endl;
    cout << "a3[2]: " << a3[2] << " at " << &a3[2] << endl;
    cout << "a4[2]: " << a4[2] << " at " << &a4[2] << endl;
    //  cin.get();
    return 0;
}
```

```
(base) kimshan@MacBook-Pro output % ./"choices"
a1[2]: 3.6 at 0x7ff7b52d77e0
a2[2]: 0.142857 at 0x7f8f71004090
a3[2]: 1.62 at 0x7ff7b52d77a0
a4[2]: 1.62 at 0x7ff7b52d7780
a1[-2]: 20.2 at 0x7ff7b52d77c0
a3[2]: 1.62 at 0x7ff7b52d77a0
a4[2]: 1.62 at 0x7ff7b52d7780
```

</details>
