# 循环语句

第5章 循环和关系表达式:程序经常需要执行重复性操作，为此 C++提供了3种循环结构:for循环、while循环和do while循环。这些循环必须知道何时终止，C++的关系运算符使程序员能够创建测试 来引导循环。本章还将介绍如何创建逐字符地读取和处理输入的循 环。最后，您将学习如何创建二维数组以及如何使用嵌套循环来处 理它们。

## 5.1 for循环

{% hint style="success" %}
推荐跳过
{% endhint %}

<details>

<summary>Basic Demo</summary>

没有大括号，默认后边的一行

```cpp
for (initialization; test-expression; update-expression)
    body;
```

有大括号

```cpp
for (initialization; test-expression; update-expression) {
    body;
}
```

&#x20;Demo

```cpp
// forloop.cpp -- introducing the for loop
#include <iostream>
int main()
{
    using namespace std;
    int i;  // create a counter
//   initialize; test ; update
    for (i = 0; i < 5; i++)
        cout << "C++ knows loops.\n";
    cout << "C++ knows when to stop.\n";
    // cin.get();
    return 0;
}

```

</details>

<details>

<summary>Update counter</summary>

* 可以++，--，注意理论上++i 比 i++速度快
* 可以倒序

```cpp
for (int i = word.size() - 1; i >= 0; i--)
        cout << word[i];
```

* 可以递增递减指针

```cpp
int main()
{
    using namespace std;
    
    double arr[5] = {2,4,6,8,10};
    double *p = arr;
    cout << *p++ << *p++ << *p++; // 2 4 6
    double * = arr;
    cout << *++q << *++q << *++q; // 4 6 8
    return 0;
}
```

```cpp
// 指针递增，然后取值
*++p;
// 取值然后指针递增
*p++;
// 指针指得地方++
++*p;
// 指针指得地方++
(*p)++;
```

</details>

<details>

<summary>more expression in one block</summary>

逗号运算符

<pre class="language-cpp"><code class="lang-cpp">// forstr2.cpp -- reversing an array
#include &#x3C;iostream>
#include &#x3C;string>
int main()
{
    using namespace std;
    cout &#x3C;&#x3C; "Enter a word: ";
    string word;
    cin >> word;

    // physically modify string object
    char temp;
    int i, j;
<strong>    for (j = 0, i = word.size() - 1; j &#x3C; i; --i, ++j)
</strong>    {                       // start block
        temp = word[i];
        word[i] = word[j];
        word[j] = temp;
    }                       // end block
    cout &#x3C;&#x3C; word &#x3C;&#x3C; "\nDone\n";
    // cin.get();
    // cin.get();
    return 0; 
}
</code></pre>

</details>

***

## 5.2 while 循环

{% hint style="success" %}
推荐跳过
{% endhint %}

<details>

<summary>Basic Demo</summary>

```cpp
while (test-condition)
    body
    
while (test-condition) {
    body
}
```

```cpp
// while.cpp -- introducing the while loop
#include <iostream>
const int ArSize = 20;
int main()
{
    using namespace std;
    char name[ArSize];

    cout << "Your first name, please: ";
    cin >> name;
    cout << "Here is your name, verticalized and ASCIIized:\n";
    int i = 0;                  // start at beginning of string
    while (name[i] != '\0')     // process to end of string
    {
        cout << name[i] << ": " << int(name[i]) << endl;
        i++;                    // don't forget this step
    }
    // cin.get();
    // cin.get();
    return 0; 
}

```

</details>

<details>

<summary>waiting Demo (with ctime)</summary>



<pre class="language-cpp"><code class="lang-cpp">// waiting.cpp -- using clock() in a time-delay loop
#include &#x3C;iostream>
#include &#x3C;ctime> // describes clock() function, clock_t type
int main()
{
    using namespace std;
    cout &#x3C;&#x3C; "Enter the delay time, in seconds: ";
    float secs;
    cin >> secs;
    clock_t delay = secs * <a data-footnote-ref href="#user-content-fn-1">CLOCKS_PER_SEC</a>;  // convert to clock ticks
    cout &#x3C;&#x3C; "starting\a\n";
    clock_t start = clock();
    while (clock() - start &#x3C; delay )        // wait until time elapses
        ;                                   // note the semicolon
    cout &#x3C;&#x3C; "done \a\n";
    // cin.get();
    // cin.get();
    return 0; 
}

</code></pre>

```
(base) kimshan@MacBook-Pro output % ./"waiting"
Enter the delay time, in seconds: 10
starting
done 
```

</details>

***

## 5.3 do while 循环

{% hint style="success" %}
推荐跳过
{% endhint %}

<details>

<summary>Basic Demo</summary>

```cpp
do {
    body
} while (test-condition);
```

</details>

***

## 5.4 基于范围的 for 循环

{% hint style="info" %}
C++11新特性
{% endhint %}

<details>

<summary>Basic Demo</summary>

遍历数字所有元素，就算没有初始化那也遍历

```cpp
#include <iostream>
#include <ctime>

int main()
{
    using namespace std;

    int array1[] = {100, 200, 300};
    for (int x : array1)
        cout << x << " \n";

    int array2[4] = {140, 250, 360};
    for (int x : array2)
        cout << x << " \n";

    return 0;
}

```

```
(base) kimshan@MacBook-Pro output % ./"test1"
100 
200 
300 
140 
250 
360 
0 
```

</details>

***

## 5.5 循环和文本输入

{% hint style="success" %}
用的时候看一看就好
{% endhint %}

<details>

<summary> 最终完善的代码（利用 EOF）</summary>

Mac的 EOF 是 command+D

Windows 的 EOF是 control+Z+enter

<pre class="language-cpp"><code class="lang-cpp">// textin4.cpp -- reading chars with cin.get()
#include &#x3C;iostream>
int main(void)
{
    using namespace std;
    int ch;                         // should be int, not char
    int count = 0;

<strong>    while ((ch = cin.get()) != EOF) // test for end-of-file
</strong>    {
        cout.put(char(ch));
        ++count;
    }
    cout &#x3C;&#x3C; endl &#x3C;&#x3C; count &#x3C;&#x3C; " characters read\n";
	return 0; 
}

</code></pre>

```
(base) kimshan@MacBook-Pro output % ./"textin4"
Hello World
Hello World
A B CCC ddddd ###jhrfijiwj
A B CCC ddddd ###jhrfijiwj
^D
39 characters read
```

</details>



[^1]: in ctime
