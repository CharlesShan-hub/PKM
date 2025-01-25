
# string.h

## Overview

![[../assets/string-drawing|1000]]

1. 字符串 = 真正的字符串内容+'\0'，'\0'用来代表字符串结束。
2. scanf 和printf用 %s 占位字符串

## Functions

<table><thead><tr><th width="72">I</th><th>函数 &#x26; 描述</th></tr></thead><tbody><tr><td>1</td><td><a href="https://www.runoob.com/cprogramming/c-function-memchr.html">void *memchr(const void *str, int c, size_t n)</a><br>在参数 <em>str</em> 所指向的字符串的前 n 个字节中搜索第一次出现字符 c（一个无符号字符）的位置。</td></tr><tr><td>2</td><td><a href="https://www.runoob.com/cprogramming/c-function-memcmp.html">int memcmp(const void *str1, const void *str2, size_t n)</a><br>把 <em>str1</em> 和 <em>str2</em> 的前 n 个字节进行比较。</td></tr><tr><td>3</td><td><a href="https://www.runoob.com/cprogramming/c-function-memcpy.html">void *memcpy(void *dest, const void *src, size_t n)</a><br>从 src 复制 n 个字符到 <em>dest</em>。</td></tr><tr><td>4</td><td><a href="https://www.runoob.com/cprogramming/c-function-memmove.html">void *memmove(void *dest, const void *src, size_t n)</a><br>另一个用于从 <em>src</em> 复制 n 个字符到 <em>dest</em> 的函数。</td></tr><tr><td>5</td><td><a href="https://www.runoob.com/cprogramming/c-function-memset.html">void *memset(void *str, int c, size_t n)</a><br>将指定的值 c 复制到 str 所指向的内存区域的前 n 个字节中。</td></tr><tr><td>6</td><td><a href="https://www.runoob.com/cprogramming/c-function-strcat.html">char *strcat(char *dest, const char *src)</a><br>把 <em>src</em> 所指向的字符串追加到 <em>dest</em> 所指向的字符串的结尾。</td></tr><tr><td>7</td><td><a href="https://www.runoob.com/cprogramming/c-function-strncat.html">char *strncat(char *dest, const char *src, size_t n)</a><br>把 <em>src</em> 所指向的字符串追加到 <em>dest</em> 所指向的字符串的结尾，直到 n 字符长度为止。</td></tr><tr><td>8</td><td><a href="https://www.runoob.com/cprogramming/c-function-strchr.html">char *strchr(const char *str, int c)</a><br>在参数 <em>str</em> 所指向的字符串中搜索第一次出现字符 c（一个无符号字符）的位置。</td></tr><tr><td>9</td><td><a href="https://www.runoob.com/cprogramming/c-function-strcmp.html">int strcmp(const char *str1, const char *str2)</a><br>把 <em>str1</em> 所指向的字符串和 <em>str2</em> 所指向的字符串进行比较。</td></tr><tr><td>10</td><td><a href="https://www.runoob.com/cprogramming/c-function-strncmp.html">int strncmp(const char *str1, const char *str2, size_t n)</a><br>把 <em>str1</em> 和 <em>str2</em> 进行比较，最多比较前 n 个字节。</td></tr><tr><td>11</td><td><a href="https://www.runoob.com/cprogramming/c-function-strcoll.html">int strcoll(const char *str1, const char *str2)</a><br>把 <em>str1</em> 和 <em>str2</em> 进行比较，结果取决于 LC_COLLATE 的位置设置。</td></tr><tr><td>12</td><td><a href="https://www.runoob.com/cprogramming/c-function-strcpy.html">char *strcpy(char *dest, const char *src)</a><br>【不检查空间】把 <em>src</em> 所指向的字符串复制到 <em>dest</em>。</td></tr><tr><td>13</td><td><a href="https://www.runoob.com/cprogramming/c-function-strncpy.html">char *strncpy(char *dest, const char *src, size_t n)</a><br>【会限制空间】把 <em>src</em> 所指向的字符串复制到 <em>dest</em>，最多复制 n 个字符。</td></tr><tr><td>14</td><td><a href="https://www.runoob.com/cprogramming/c-function-strcspn.html">size_t strcspn(const char *str1, const char *str2)</a><br>检索字符串 str1 开头连续有几个字符都不含字符串 str2 中的字符。</td></tr><tr><td>15</td><td><a href="https://www.runoob.com/cprogramming/c-function-strerror.html">char *strerror(int errnum)</a><br>从内部数组中搜索错误号 errnum，并返回一个指向错误消息字符串的指针。</td></tr><tr><td>16</td><td><a href="https://www.runoob.com/cprogramming/c-function-strlen.html">size_t strlen(const char *str)</a><br>计算字符串 str 的长度，直到空结束字符，但不包括空结束字符。</td></tr><tr><td>17</td><td><a href="https://www.runoob.com/cprogramming/c-function-strpbrk.html">char *strpbrk(const char *str1, const char *str2)</a><br>检索字符串 <em>str1</em> 中第一个匹配字符串 <em>str2</em> 中字符的字符，不包含空结束字符。也就是说，依次检验字符串 str1 中的字符，当被检验字符在字符串 str2 中也包含时，则停止检验，并返回该字符位置。</td></tr><tr><td>18</td><td><a href="https://www.runoob.com/cprogramming/c-function-strrchr.html">char *strrchr(const char *str, int c)</a><br>在参数 <em>str</em> 所指向的字符串中搜索最后一次出现字符 c（一个无符号字符）的位置。</td></tr><tr><td>19</td><td><a href="https://www.runoob.com/cprogramming/c-function-strspn.html">size_t strspn(const char *str1, const char *str2)</a><br>检索字符串 <em>str1</em> 中第一个不在字符串 <em>str2</em> 中出现的字符下标。</td></tr><tr><td>20</td><td><a href="https://www.runoob.com/cprogramming/c-function-strstr.html">char *strstr(const char *haystack, const char *needle)</a><br>在字符串 <em>haystack</em> 中查找第一次出现字符串 <em>needle</em>（不包含空结束字符）的位置。</td></tr><tr><td>21</td><td><a href="https://www.runoob.com/cprogramming/c-function-strtok.html">char *strtok(char *str, const char *delim)</a><br>分解字符串 <em>str</em> 为一组字符串，<em>delim</em> 为分隔符。</td></tr><tr><td>22</td><td><a href="https://www.runoob.com/cprogramming/c-function-strxfrm.html">size_t strxfrm(char *dest, const char *src, size_t n)</a><br>根据程序当前的区域选项中的 LC_COLLATE 来转换字符串 src 的前 n 个字符，并把它们放置在字符串 dest 中。</td></tr></tbody></table>

<details>

<summary>strlen</summary>

strlen 通过检查'\0'判断长度

可以把字符串中的某一位变成'\0'来提前截断字符串

```c
/* test_fit.c -- try the string-shrinking function */
#include <stdio.h>
#include <string.h> /* contains string function prototypes */
void fit(char *, unsigned int);

int main(void)
{
    char mesg[] = "Things should be as simple as possible,"
                  " but not simpler.";

    puts(mesg);
    fit(mesg, 38);
    puts(mesg);
    puts("Let's look at some more of the string.");
    puts(mesg + 39);

    return 0;
}

void fit(char *string, unsigned int size)
{
    if (strlen(string) > size)
        string[size] = '\0';
}

// (base) kimshan@MacBook-Pro output % ./"test_fit"
// Things should be as simple as possible, but not simpler.
// Things should be as simple as possible
// Let's look at some more of the string.
//  but not simpler.
```

</details>

<details>

<summary>strcat</summary>

把第二个拼在第一个后边

```c
/* str_cat.c -- joins two strings */
#include <stdio.h>
#include <string.h> /* declares the strcat() function */
#define SIZE 80
char *s_gets(char *st, int n);
int main(void)
{
    char flower[SIZE];
    char addon[] = "s smell like old shoes.";

    puts("What is your favorite flower?");
    if (s_gets(flower, SIZE))
    {
        strcat(flower, addon);
        puts(flower);
        puts(addon);
    }
    else
        puts("End of file encountered!");
    puts("bye");

    return 0;
}

char *s_gets(char *st, int n)
{
    char *ret_val;
    int i = 0;

    ret_val = fgets(st, n, stdin);
    if (ret_val)
    {
        while (st[i] != '\n' && st[i] != '\0')
            i++;
        if (st[i] == '\n')
            st[i] = '\0';
        else // must have words[i] == '\0'
            while (getchar() != '\n')
                continue;
    }
    return ret_val;
}

// (base) kimshan@MacBook-Pro output % ./"str_cat"
// What is your favorite flower?
// sunflower
// sunflowers smell like old shoes.
// s smell like old shoes.
// bye
```

</details>

<details>

<summary>strncat</summary>

strcat 无法检查第一个数组是否能容纳第二个数组，如果数组 1 不够大，就会溢出影响旁边存储的内容！

```c
/* join_chk.c -- joins two strings, check size first */
#include <stdio.h>
#include <string.h>
#define SIZE 30
#define BUGSIZE 13
char *s_gets(char *st, int n);
int main(void)
{
    char flower[SIZE];
    char addon[] = "s smell like old shoes.";
    char bug[BUGSIZE];
    int available;

    puts("What is your favorite flower?");
    s_gets(flower, SIZE);
    if ((strlen(addon) + strlen(flower) + 1) <= SIZE)
        strcat(flower, addon);
    puts(flower);
    puts("What is your favorite bug?");
    s_gets(bug, BUGSIZE);
    available = BUGSIZE - strlen(bug) - 1;
    strncat(bug, addon, available);
    puts(bug);

    return 0;
}
char *s_gets(char *st, int n)
{
    char *ret_val;
    int i = 0;

    ret_val = fgets(st, n, stdin);
    if (ret_val)
    {
        while (st[i] != '\n' && st[i] != '\0')
            i++;
        if (st[i] == '\n')
            st[i] = '\0';
        else // must have words[i] == '\0'
            while (getchar() != '\n')
                continue;
    }
    return ret_val;
}

// (base) kimshan@MacBook-Pro output % ./"join_chk"
// What is your favorite flower?
// 1123456789098765432134567890
// 1123456789098765432134567890
// What is your favorite bug?
// qwertyuiokjhgfdscvvbnm
// qwertyuiokjh
// (base) kimshan@MacBook-Pro output % ./"join_chk"
// What is your favorite flower?
// sunflower
// sunflower
// What is your favorite bug?
// overflow
// overflows sm
// (base) kimshan@MacBook-Pro output % ./"join_chk"
// What is your favorite flower?
// 1
// 1s smell like old shoes.
// What is your favorite bug?
// 2
// 2s smell lik
```

</details>

<details>

<summary>strcmp</summary>

进行字符串比较

```c
/* compback.c -- strcmp returns */
#include <stdio.h>
#include <string.h>
int main(void)
{
    
    printf("strcmp(\"A\", \"A\") is ");
    printf("%d\n", strcmp("A", "A"));
    
    printf("strcmp(\"A\", \"B\") is ");
    printf("%d\n", strcmp("A", "B"));
    
    printf("strcmp(\"B\", \"A\") is ");
    printf("%d\n", strcmp("B", "A"));
    
    printf("strcmp(\"C\", \"A\") is ");
    printf("%d\n", strcmp("C", "A"));
    
    printf("strcmp(\"Z\", \"a\") is ");
    printf("%d\n", strcmp("Z", "a"));
    
    printf("strcmp(\"apples\", \"apple\") is ");
    printf("%d\n", strcmp("apples", "apple"));
    
    return 0;
}

// (base) kimshan@MacBook-Pro output % ./"compback"
// strcmp("A", "A") is 0
// strcmp("A", "B") is -1
// strcmp("B", "A") is 1
// strcmp("C", "A") is 1
// strcmp("Z", "a") is -1
// strcmp("apples", "apple") is 1
```

</details>

<details>

<summary>strncmp</summary>

限定找前n 个字符

```c
/* starsrch.c -- use strncmp() */
#include <stdio.h>
#include <string.h>
#define LISTSIZE 6
int main()
{
    const char *list[LISTSIZE] = {
        "astronomy",
        "astounding",
        "astrophysics",
        "ostracize",
        "asterism",
        "astrophobia",
    };
    int count = 0;
    int i;

    for (i = 0; i < LISTSIZE; i++)
        if (strncmp(list[i], "astro", 5) == 0)
        {
            printf("Found: %s\n", list[i]);
            count++;
        }
    printf("The list contained %d words beginning"
           " with astro.\n",
           count);

    return 0;
}

// (base) kimshan@MacBook-Pro output % ./"starsrch"
// Found: astronomy
// Found: astrophysics
// Found: astrophobia
// The list contained 3 words beginning with astro.

```

</details>

<details>

<summary>strcpy</summary>

字符串拷贝

```c
/* copy1.c -- strcpy() demo */
#include <stdio.h>
#include <string.h> // declares strcpy()
#define SIZE 40
#define LIM 5
char *s_gets(char *st, int n);

int main(void)
{
    char qwords[LIM][SIZE];
    char temp[SIZE];
    int i = 0;

    printf("Enter %d words beginning with q:\n", LIM);
    while (i < LIM && s_gets(temp, SIZE))
    {
        if (temp[0] != 'q')
            printf("%s doesn't begin with q!\n", temp);
        else
        {
            strcpy(qwords[i], temp);
            i++;
        }
    }
    puts("Here are the words accepted:");
    for (i = 0; i < LIM; i++)
        puts(qwords[i]);

    return 0;
}

char *s_gets(char *st, int n)
{
    char *ret_val;
    int i = 0;

    ret_val = fgets(st, n, stdin);
    if (ret_val)
    {
        while (st[i] != '\n' && st[i] != '\0')
            i++;
        if (st[i] == '\n')
            st[i] = '\0';
        else // must have words[i] == '\0'
            while (getchar() != '\n')
                continue;
    }
    return ret_val;
}

// (base) kimshan@MacBook-Pro output % ./"copy1"
// Enter 5 words beginning with q:
// qwert
// qazwsx
// qwererty
// qqq
// q
// Here are the words accepted:
// qwert
// qazwsx
// qwererty
// qqq
// q
```

</details>

<details>

<summary>strcpy</summary>

因为第一个参数是指针，所以我们可以从某个位置开始加入新字符。

<pre class="language-c"><code class="lang-c">/* copy2.c -- strcpy() demo */
#include &#x3C;stdio.h>
#include &#x3C;string.h> // declares strcpy()
#define WORDS "beast"
#define SIZE 40

int main(void)
{
    const char *orig = WORDS;
    char copy[SIZE] = "Be the best that you can be.";
    char *ps;

    puts(orig);
    puts(copy);
<strong>    ps = strcpy(copy + 7, orig);
</strong>    puts(copy);
    puts(ps);

    return 0;
}

// (base) kimshan@MacBook-Pro output % ./"copy2"
// beast
// Be the best that you can be.
// Be the beast
// beast
</code></pre>

</details>

<details>

<summary>strncpy</summary>

```c
/* copy3.c -- strncpy() demo */
#include <stdio.h>
#include <string.h> /* declares strncpy() */
#define SIZE 40
#define TARGSIZE 7
#define LIM 5
char *s_gets(char *st, int n);

int main(void)
{
    char qwords[LIM][TARGSIZE];
    char temp[SIZE];
    int i = 0;

    printf("Enter %d words beginning with q:\n", LIM);
    while (i < LIM && s_gets(temp, SIZE))
    {
        if (temp[0] != 'q')
            printf("%s doesn't begin with q!\n", temp);
        else
        {
            strncpy(qwords[i], temp, TARGSIZE - 1);
            qwords[i][TARGSIZE - 1] = '\0';
            i++;
        }
    }
    puts("Here are the words accepted:");
    for (i = 0; i < LIM; i++)
        puts(qwords[i]);

    return 0;
}

char *s_gets(char *st, int n)
{
    char *ret_val;
    int i = 0;

    ret_val = fgets(st, n, stdin);
    if (ret_val)
    {
        while (st[i] != '\n' && st[i] != '\0')
            i++;
        if (st[i] == '\n')
            st[i] = '\0';
        else // must have words[i] == '\0'
            while (getchar() != '\n')
                continue;
    }
    return ret_val;
}

// (base) kimshan@MacBook-Pro output % ./"copy3"
// Enter 5 words beginning with q:
// q1
// q12
// q12345
// q1234567
// q1234567890
// Here are the words accepted:
// q1
// q12
// q12345
// q12345
// q12345
```

</details>

## Content in Table

has C++ demo links\[2]

<table><thead><tr><th width="298">Copying - function</th><th>Description</th></tr></thead><tbody><tr><td><a href="https://cplusplus.com/reference/cstring/memcpy/"><strong>memcpy</strong></a></td><td>Copy block of memory (function)</td></tr><tr><td><a href="https://cplusplus.com/reference/cstring/memmove/"><strong>memmove</strong></a></td><td>Move block of memory (function)</td></tr><tr><td><a href="https://cplusplus.com/reference/cstring/strcpy/"><strong>strcpy</strong></a></td><td>Copy string (function)</td></tr><tr><td><a href="https://cplusplus.com/reference/cstring/strncpy/"><strong>strncpy</strong></a></td><td>Copy characters from string (function)</td></tr></tbody></table>

<table><thead><tr><th width="298">Concatenation - function</th><th>Description</th></tr></thead><tbody><tr><td><a href="https://cplusplus.com/reference/cstring/strcat/"><strong>strcat</strong></a></td><td>Concatenate strings (function)</td></tr><tr><td><a href="https://cplusplus.com/reference/cstring/strncat/"><strong>strncat</strong></a></td><td>Append characters from string (function)</td></tr></tbody></table>

<table><thead><tr><th width="298">Comparison</th><th>Description</th></tr></thead><tbody><tr><td><a href="https://cplusplus.com/reference/cstring/memcmp/"><strong>memcmp</strong></a></td><td>Compare two blocks of memory (function)</td></tr><tr><td><a href="https://cplusplus.com/reference/cstring/strcmp/"><strong>strcmp</strong></a></td><td>Compare two strings (function)</td></tr><tr><td><a href="https://cplusplus.com/reference/cstring/strcoll/"><strong>strcoll</strong></a></td><td>Compare two strings using locale (function)</td></tr><tr><td><a href="https://cplusplus.com/reference/cstring/strncmp/"><strong>strncmp</strong></a></td><td>Compare characters of two strings (function)</td></tr><tr><td><a href="https://cplusplus.com/reference/cstring/strxfrm/"><strong>strxfrm</strong></a></td><td>Transform string using locale (function)</td></tr></tbody></table>

<table><thead><tr><th width="298">Concatenation - function</th><th>Description</th></tr></thead><tbody><tr><td><a href="https://cplusplus.com/reference/cstring/strcat/"><strong>strcat</strong></a></td><td>Concatenate strings (function)</td></tr><tr><td><a href="https://cplusplus.com/reference/cstring/strncat/"><strong>strncat</strong></a></td><td>Append characters from string (function)</td></tr></tbody></table>

<table><thead><tr><th width="298">Searching - function</th><th>Description</th></tr></thead><tbody><tr><td><a href="https://cplusplus.com/reference/cstring/memchr/"><strong>memchr</strong></a></td><td>Locate character in block of memory (function)</td></tr><tr><td><a href="https://cplusplus.com/reference/cstring/strchr/"><strong>strchr</strong></a></td><td>Locate first occurrence of character in string (function)</td></tr><tr><td><a href="https://cplusplus.com/reference/cstring/strcspn/"><strong>strcspn</strong></a></td><td>Get span until character in string (function)</td></tr><tr><td><a href="https://cplusplus.com/reference/cstring/strpbrk/"><strong>strpbrk</strong></a></td><td>Locate characters in string (function)</td></tr><tr><td><a href="https://cplusplus.com/reference/cstring/strrchr/"><strong>strrchr</strong></a></td><td>Locate last occurrence of character in string (function)</td></tr><tr><td><a href="https://cplusplus.com/reference/cstring/strspn/"><strong>strspn</strong></a></td><td>Get span of character set in string (function)</td></tr><tr><td><a href="https://cplusplus.com/reference/cstring/strstr/"><strong>strstr</strong></a></td><td>Locate substring (function)</td></tr><tr><td><a href="https://cplusplus.com/reference/cstring/strtok/"><strong>strtok</strong></a></td><td>Split string into tokens (function)</td></tr></tbody></table>

<table><thead><tr><th width="298">Others - function</th><th>Description</th></tr></thead><tbody><tr><td><a href="https://cplusplus.com/reference/cstring/memset/"><strong>memset</strong></a></td><td>Fill block of memory (function)</td></tr><tr><td><a href="https://cplusplus.com/reference/cstring/strerror/"><strong>strerror</strong></a></td><td>Get pointer to error message string (function)</td></tr><tr><td><a href="https://cplusplus.com/reference/cstring/strlen/"><strong>strlen</strong></a></td><td>Get string length (function)</td></tr></tbody></table>

<table><thead><tr><th width="298">Macros</th><th>Description</th></tr></thead><tbody><tr><td><a href="https://cplusplus.com/reference/cstring/NULL/"><strong>NULL</strong></a></td><td>Null pointer (macro)</td></tr></tbody></table>

<table><thead><tr><th width="298">Types</th><th>Description</th></tr></thead><tbody><tr><td><a href="https://cplusplus.com/reference/cstring/size_t/"><strong>size_t</strong></a></td><td>Unsigned integral type (type)</td></tr></tbody></table>

## Reference

\[1] [https://www.runoob.com/cprogramming/c-standard-library-string-h.html](https://www.runoob.com/cprogramming/c-standard-library-string-h.html)

\[2] [https://cplusplus.com/reference/cstring/](https://cplusplus.com/reference/cstring/)
