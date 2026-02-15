可以使用八进制或十六进制的数字来表示字符

```c
#include <stdio.h>

int main() {
    // \0x41 是十六进制转义序列，代表 ASCII 码中的 'A'
    char hexEscape = '\0x41';
    
    // \0101 是八进制转义序列，同样代表 ASCII 码中的 'A'
    // 在八进制中，101 转换为十进制是 65，这是 'A' 的 ASCII 值
    char octalEscape = '\0101';
    
    // 打印这两个字符
    printf("字符 '\\0x41' 的 ASCII 值是: %c\n", hexEscape);
    printf("字符 '\\0101' 的 ASCII 值是: %c\n", octalEscape);
    
    return 0;
}

```

```bash
字符 '\0x41' 的 ASCII 值是: 1
字符 '\0101' 的 ASCII 值是: 1
```