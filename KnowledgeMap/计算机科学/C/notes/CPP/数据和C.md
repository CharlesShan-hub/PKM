# 数据和C
2022.06.30
[TOC]

关键字

| 最初       | C90    | C99        |
| -------- | ------ | ---------- |
| int      | signed | _Bool      |
| long     | void   | _Complex   |
| short    |        | _Imaginary |
| unsigned |        |            |
| char     |        |            |
| float    |        |            |
| double   |        |            |





布尔类型

```c
#include <stdio.h>
#include <stdbool.h>
int main(){
	bool a=true;
	_Bool b=true;
	printf("%d,%d,%d,%d\n",int(sizeof(a)),int(sizeof(b)),a==b,a==1);
	// output: 1,1,1,1
	return 0;
}
```

