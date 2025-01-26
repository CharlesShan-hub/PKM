
# Pointer

## 指针

1. 指针是什么：指针是一个值，为内存地址的变量。
2. 声明指针（`int *pi, *pi2;`）：类型 \* 变量名 \* 变量名
3. &：取地址（`ptr = &pooh;`），把 pooh 的地址给 ptr。
4. \*：解引用（`val = *ptr;`），把 ptr 所指向的数据赋值给 val。
5. 运算优先级：\*与++相同，顺序从右往左

优先级

**“顺序从右到左”我的理解是，都在指针左边比如`*++p2`就先++再\*，但如果是`*p1++`那就还是先\*再++**

```c
/* order.c -- precedence in pointer operations */
#include <stdio.h>
int data[2] = {100, 200};
int moredata[2] = {300, 400};
int main(void)
{
    int * p1, * p2, * p3;
    
    p1 = p2 = data;
    p3 = moredata;
    printf("  *p1 = %d,   *p2 = %d,     *p3 = %d\n",
           *p1     ,   *p2     ,     *p3);
    printf("*p1++ = %d, *++p2 = %d, (*p3)++ = %d\n",
           *p1++     , *++p2     , (*p3)++);
    printf("  *p1 = %d,   *p2 = %d,     *p3 = %d\n",
           *p1     ,   *p2     ,     *p3);
    
    return 0;
}

//   *p1 = 100,   *p2 = 100,     *p3 = 300
// *p1++ = 100, *++p2 = 200, (*p3)++ = 300
//   *p1 = 200,   *p2 = 200,     *p3 = 301
```


6. pintf 指针：%p
7. 指向下一个内容：++
8. 严重错误：解引用未初始化的指针，相当于在不知道什么地方改变了数据

解引用未初始化的指针

```c
#include <stdio.h>
#include <stdlib.h>
int main()
{
    // wrong
    int *a = 1;

    // wrong
    int *b;
    *b = 100;

    // right
    int *c = malloc(sizeof(int));
    *c = 200;
    return 0;
}
```


## 指针与数组

* p代表指针，eg `int *p;`
* array代表数组 eg `int array[32];`
* 已经把指针指向数组：`p = array[0];`

指针指向数组；通过指针访问数组

```c
#include <stdio.h>

int main()
{
    int array[8] = {0, 1, 2, 3, 4, 5, 6, 7};
    int *p1 = array;
    int *p2 = &array[0];

    for (int i = 0; i < 8; i++)
    {
        printf("%d ", *(p1 + i)); // 0 1 2 3 4 5 6 7
        printf("%d ", *(p2 + i)); // 0 1 2 3 4 5 6 7
    }

    return 0;

```

指针与二维数组：精髓在于，指针是“一层一层”指下去的

```c
/* zippo1.c --  zippo info */
#include <stdio.h>
int main(void)
{
       int zippo[4][2] = {{2, 4}, {6, 8}, {1, 3}, {5, 7}};

       printf("   zippo = %p,    zippo + 1 = %p\n",
              zippo, zippo + 1);
       printf("zippo[0] = %p, zippo[0] + 1 = %p\n",
              zippo[0], zippo[0] + 1);
       printf("  *zippo = %p,   *zippo + 1 = %p\n",
              *zippo, *zippo + 1);
       printf("zippo[0][0] = %d\n", zippo[0][0]);
       printf("  *zippo[0] = %d\n", *zippo[0]);
       printf("    **zippo = %d\n", **zippo);
       printf("      zippo[2][1] = %d\n", zippo[2][1]);
       printf("*(*(zippo+2) + 1) = %d\n", *(*(zippo + 2) + 1));

       return 0;
}
//    zippo = 0x7ff7b301c7f0,    zippo + 1 = 0x7ff7b301c7f8
// zippo[0] = 0x7ff7b301c7f0, zippo[0] + 1 = 0x7ff7b301c7f4
//   *zippo = 0x7ff7b301c7f0,   *zippo + 1 = 0x7ff7b301c7f4
// zippo[0][0] = 2
//   *zippo[0] = 2
//     **zippo = 2
//       zippo[2][1] = 3
// *(*(zippo+2) + 1) = 3
```

指针与二维数组，注意，[]优先级高于*！

```c
/* zippo2.c --  zippo info via a pointer variable */
#include <stdio.h>
int main(void)
{
    int zippo[4][2] = { {2,4}, {6,8}, {1,3}, {5, 7} };
    int (*pz)[2]; // pz 指向一个内部含有两个 int 的数组
    pz = zippo;
    
    printf("   pz = %p,    pz + 1 = %p\n",
           pz,         pz + 1);
    printf("pz[0] = %p, pz[0] + 1 = %p\n",
           pz[0],      pz[0] + 1);
    printf("  *pz = %p,   *pz + 1 = %p\n",
           *pz,        *pz + 1);
    printf("pz[0][0] = %d\n", pz[0][0]);
    printf("  *pz[0] = %d\n", *pz[0]);
    printf("    **pz = %d\n", **pz);
    printf("      pz[2][1] = %d\n", pz[2][1]);
    printf("*(*(pz+2) + 1) = %d\n", *(*(pz+2) + 1));
    
    return 0;
}
// (base) kimshan@MacBook-Pro output % ./"zippo2"
//    pz = 0x7ff7bc6da800,    pz + 1 = 0x7ff7bc6da808
// pz[0] = 0x7ff7bc6da800, pz[0] + 1 = 0x7ff7bc6da804
//   *pz = 0x7ff7bc6da800,   *pz + 1 = 0x7ff7bc6da804
// pz[0][0] = 2
//   *pz[0] = 2
//     **pz = 2
//       pz[2][1] = 3
// *(*(pz+2) + 1) = 3
```



符合字面量：比如`(int [2]){10,20}`

```c
// flc.c -- funny-looking constants
#include <stdio.h>
#define COLS 4
int sum2d(const int ar[][COLS], int rows);
int sum(const int ar[], int n);
int main(void)
{
    int total1, total2, total3;
    int * pt1;
    int (*pt2)[COLS];
    
    pt1 = (int [2]) {10, 20};
    pt2 = (int [2][COLS]) { {1,2,3,-9}, {4,5,6,-8} };
    
    total1 = sum(pt1, 2);
    total2 = sum2d(pt2, 2);
    total3 = sum((int []){4,4,4,5,5,5}, 6);
    printf("total1 = %d\n", total1);
    printf("total2 = %d\n", total2);
    printf("total3 = %d\n", total3);
    
    return 0;
}

int sum(const int ar[], int n)
{
    int i;
    int total = 0;
    
    for( i = 0; i < n; i++)
        total += ar[i];
    
    return total;
}

int sum2d(const int ar[][COLS], int rows)
{
    int r;
    int c;
    int tot = 0;
    
    for (r = 0; r < rows; r++)
        for (c = 0; c < COLS; c++)
            tot += ar[r][c];
    
    return tot;
}
```

```bash
(base) kimshan@MacBook-Pro output % ./"flc"
total1 = 30
total2 = 4
total3 = 2
```

## 指针与函数

通过 `int array\[]` 和 `int *array`，作为形参是一样的

```c
#include <stdio.h>
#include <stdlib.h>

void merge(int *array1, int array2[], int res[], int len1, int len2)
{
    for (int i = 0; i < len1 + len2; i++)
        *(res + i) = *(array1 + i);
    for (int i = 0; i < +len2; i++)
        res[i + len1] = array2[i];
}

int main()
{
    const int LEN1 = 4;
    const int LEN2 = 2;
    int array1[LEN1] = {0, 1, 2, 3};
    int array2[LEN2] = {4, 5};
    int *array3 = malloc(sizeof(int) * (LEN1 + LEN2));
    merge(array1, array2, array3, LEN1, LEN2);

    for (int i = 0; i < LEN1 + LEN2; i++)
        printf("%d ", *(array3 + i));
    return 0;
}
```

悬空指针：指针指向一个地方，但是那个地方作用域已经结束（修改一行上边的代码）

```c
#include <stdio.h>
#include <stdlib.h>

int *merge(int *array1, int array2[], int len1, int len2)
{
    int res[len1 + len2];
    for (int i = 0; i < len1 + len2; i++)
        *(res + i) = *(array1 + i);
    for (int i = 0; i < +len2; i++)
        res[i + len1] = array2[i];
    return res; // wrong!但是编译器能通过
}

int main()
{
    const int LEN1 = 4;
    const int LEN2 = 2;
    int array1[LEN1] = {0, 1, 2, 3};
    int array2[LEN2] = {4, 5};
    int *array3 = malloc(sizeof(int) * (LEN1 + LEN2));
    array3 = merge(array1, array2, LEN1, LEN2);

    for (int i = 0; i < LEN1 + LEN2; i++)
        printf("%d ", *(array3 + i));
    return 0;
}
```

形参对原地址的变量的保护，形参+const，这样如果不小心写了<code>array[i]++</code>，编译器就会捕获这个错误

```c
int sum(const int *array, int n)
{
    int total = 0;
    for(int i=0; i<n; i++)
        total += array[i];
    return total;
}
```

* 多重指针/多维数组，在函数里边怎么传参数
  * 不能这样声明：`int sum2(int ar[][], int rows);`，两个都是\[]不行
  * 需要这样：`int sum2(int ar[][COL], int rows);`，COL 放在数组中，rows 单独传入
  * 只能忽略最左边的：`int sum4d(int ar[][2][3][4], int rows);`因为C 规定数组的维数必须是固定的。

有很多等价写法

```c
// array2d.c -- functions for 2d arrays
#include <stdio.h>
#define ROWS 3
#define COLS 4
void sum_rows(int ar[][COLS], int rows);
void sum_cols(int[][COLS], int);      // ok to omit names
int sum2d(int (*ar)[COLS], int rows); // another syntax
int main(void)
{
    int junk[ROWS][COLS] = {
        {2, 4, 6, 8},
        {3, 5, 7, 9},
        {12, 10, 8, 6}};

    sum_rows(junk, ROWS);
    sum_cols(junk, ROWS);
    printf("Sum of all elements = %d\n", sum2d(junk, ROWS));

    return 0;
}

void sum_rows(int ar[][COLS], int rows)
{
    int r;
    int c;
    int tot;

    for (r = 0; r < rows; r++)
    {
        tot = 0;
        for (c = 0; c < COLS; c++)
            tot += ar[r][c];
        printf("row %d: sum = %d\n", r, tot);
    }
}

void sum_cols(int ar[][COLS], int rows)
{
    int r;
    int c;
    int tot;

    for (c = 0; c < COLS; c++)
    {
        tot = 0;
        for (r = 0; r < rows; r++)
            tot += ar[r][c];
        printf("col %d: sum = %d\n", c, tot);
    }
}

int sum2d(int ar[][COLS], int rows)
{
    int r;
    int c;
    int tot = 0;

    for (r = 0; r < rows; r++)
        for (c = 0; c < COLS; c++)
            tot += ar[r][c];

    return tot;
}

// (base) kimshan@MacBook-Pro output % ./"array2d"
// row 0: sum = 20
// row 1: sum = 24
// row 2: sum = 36
// col 0: sum = 17
// col 1: sum = 19
// col 2: sum = 21
// col 3: sum = 23
// Sum of all elements = 8
```

以上的写法很不方便，所以 C11 引入了 VLA 变长数组

```c
//vararr2d.c -- functions using VLAs
#include <stdio.h>
#define ROWS 3
#define COLS 4
int sum2d(int rows, int cols, int ar[rows][cols]);
int main(void)
{
    int i, j;
    int rs = 3;
    int cs = 10;
    int junk[ROWS][COLS] = {
        {2,4,6,8},
        {3,5,7,9},
        {12,10,8,6}
    };
    
    int morejunk[ROWS-1][COLS+2] = {
        {20,30,40,50,60,70},
        {5,6,7,8,9,10}
    };
    
    int varr[rs][cs];  // VLA
    
    for (i = 0; i < rs; i++)
        for (j = 0; j < cs; j++)
            varr[i][j] = i * j + j;
    
    printf("3x5 array\n");
    printf("Sum of all elements = %d\n",
           sum2d(ROWS, COLS, junk));
    
    printf("2x6 array\n");
    printf("Sum of all elements = %d\n",
           sum2d(ROWS-1, COLS+2, morejunk));
    
    printf("3x10 VLA\n");
    printf("Sum of all elements = %d\n",
           sum2d(rs, cs, varr));
    
    return 0;
}

// function with a VLA parameter
int sum2d(int rows, int cols, int ar[rows][cols])
{
    int r;
    int c;
    int tot = 0;
    
    for (r = 0; r < rows; r++)
        for (c = 0; c < cols; c++)
            tot += ar[r][c];
    
    return tot;
}

// (base) kimshan@MacBook-Pro output % ./"vararr2d"
// 3x5 array
// Sum of all elements = 80
// 2x6 array
// Sum of all elements = 315
// 3x10 VLA
// Sum of all elements = 270
```