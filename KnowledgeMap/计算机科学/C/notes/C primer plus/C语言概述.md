# C语言概述
2022.06.30
[TOC]

## 简单示例与细节

```C
#include <stdio.h>
int main(void){
  int num;
  num = 1;
  
  printf("I am a simple computer.\n");
  printf("My favoriate number is %d.\n",num);
  
  return 0;
}
```

1. `int main(void)`是标准形式，如果写`main()`或者`void main()`
2. C99和C11允许使用更长的标识符名，但是编译器只识别前63个字符。对于外部标识符（参阅第12章），只允许使用31个字符。
3. 