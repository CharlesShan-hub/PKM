不同的 int 在不同电脑中占用字节数不同，这也就代表了不同电脑的某种 int 可以表示的范围不同。

```c
#include <stdio.h>

int main(){
  // short
  short a;
  short int b;
  unsigned short c;
  unsigned short int d;

  printf("sizeof short = %luB\n", sizeof(a));
  printf("sizeof short int = %luB\n", sizeof(b));
  printf("sizeof unsigned short = %luB\n", sizeof(c));
  printf("sizeof unsigned short int = %luB\n\n", sizeof(d));

  // int
  int e;
  unsigned f;
  unsigned int g;
  
  printf("sizeof int = %luB\n", sizeof(e));
  printf("sizeof unsigned = %luB\n", sizeof(f));
  printf("sizeof unsigned int = %luB\n\n", sizeof(g));

  // long
  long h;
  long int i;
  unsigned long j;
  unsigned long int k;

  printf("sizeof long = %luB\n", sizeof(h));
  printf("sizeof long int = %luB\n", sizeof(i));
  printf("sizeof unsigned long = %luB\n", sizeof(j));
  printf("sizeof unsigned long int = %luB\n\n", sizeof(k));

  // long long
  long long l;
  long long int m;
  unsigned long long n;
  unsigned long long int o;

  printf("sizeof long long = %luB\n", sizeof(l));
  printf("sizeof long long int = %luB\n", sizeof(m));
  printf("sizeof unsigned long long = %luB\n", sizeof(n));
  printf("sizeof unsigned long long int = %luB\n", sizeof(o));

}
```

```bash
sizeof short = 2B
sizeof short int = 2B
sizeof unsigned short = 2B
sizeof unsigned short int = 2B

sizeof int = 4B
sizeof unsigned = 4B
sizeof unsigned int = 4B

sizeof long = 8B
sizeof long int = 8B
sizeof unsigned long = 8B
sizeof unsigned long int = 8B

sizeof long long = 8B
sizeof long long int = 8B
sizeof unsigned long long = 8B
sizeof unsigned long long int = 8B
```
