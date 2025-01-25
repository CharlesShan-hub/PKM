
# stdlib.h

## Overview



## Function

### qsort

```c
#include <stdio.h>
#include <stdlib.h>

// 定义一个包含五个整数的数组
int values[] = { 88, 56, 100, 2, 25 };

// 比较函数，用于比较两个整数
int cmpfunc (const void * a, const void * b)
{
   return ( *(int*)a - *(int*)b );
}

int main()
{
   int n;

   // 输出排序之前的数组内容
   printf("排序之前的列表：\n");
   for( n = 0 ; n < 5; n++ ) {
      printf("%d ", values[n]);
   }

   // 使用 qsort 函数对数组进行排序
   qsort(values, 5, sizeof(int), cmpfunc);

   // 输出排序之后的数组内容
   printf("\n排序之后的列表：\n");
   for( n = 0 ; n < 5; n++ ) {
      printf("%d ", values[n]);
   }
  
   return 0;
}
```


### atoi

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
   int val;
   char str[20];
   
   strcpy(str, "98993489");
   val = atoi(str);
   printf("字符串值 = %s, 整型值 = %d\n", str, val);

   strcpy(str, "runoob.com");
   val = atoi(str);
   printf("字符串值 = %s, 整型值 = %d\n", str, val);

   return(0);
}
```



## Reference

\[1] [https://www.runoob.com/cprogramming/c-standard-library-stdlib-h.html](https://www.runoob.com/cprogramming/c-standard-library-stdlib-h.html)
