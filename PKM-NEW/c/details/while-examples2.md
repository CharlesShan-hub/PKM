读取输入字符，将字母字符转换为其后续字符，并保留非字母字符不变，直到遇到文件结束符（EOF）。

```c
// cypher2.c -- alters input, preserving non-letters
#include <stdio.h>
#include <ctype.h>            // for isalpha()
int main(void)
{
    char ch;
    
    //while ((ch = getchar()) != '\n')
    while ((ch = getchar()) != EOF)
    {
        if (isalpha(ch))      // if a letter,
            putchar(ch + 1);  // display next letter
        else                  // otherwise,
            putchar(ch);      // display as is
    }
    putchar(ch);              // display the newline
    
    return 0;
}

```

```
(base) kimshan@MacBook-Pro output % ./"cypher2"
ABCDabcd
BCDEbcde
```
