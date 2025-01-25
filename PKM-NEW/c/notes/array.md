
# Array

## 一维数组

未初始化

```c
#define SIZE 4
int array[SIZE];
```

如果 size 是 4，只赋值了两个，那就是默认给前两个赋值了

```c
int array[SIZE] = {100,200}; // [100,200,0,0]
```

也可以指定给某个位置赋值（需要 C99）

```c
int array[SIZE] = {[0]=100, [3]=200}; // [100, 0, 0, 200]
```

可以不指定长度

```c
int array[] = {100,200}; // [100, 200]
```

可以用变量指定数组长度（需要 C99）

```c
int array[n];
```

下面这样的时候不可以的！不能用一个数组给另一个数组赋值

```c
int array2[] = array; // wrong! 
```

下面这个也不行，不能声明完了再用大括号赋值

```c
int array2[SIZE];
array2 = {100, 200}; // wrong!
```

## 多维数组

就像数学中的矩阵一样。比如三行四列的矩阵就是a\[3]\[4]

<details>

<summary>Demo</summary>



```c
/* rain.c  -- finds yearly totals, yearly average, and monthly
 average for several years of rainfall data */
#include <stdio.h>
#define MONTHS 12    // number of months in a year
#define YEARS   5    // number of years of data
int main(void)
{
    // initializing rainfall data for 2010 - 2014
    const float rain[YEARS][MONTHS] =
    {
        {4.3,4.3,4.3,3.0,2.0,1.2,0.2,0.2,0.4,2.4,3.5,6.6},
        {8.5,8.2,1.2,1.6,2.4,0.0,5.2,0.9,0.3,0.9,1.4,7.3},
        {9.1,8.5,6.7,4.3,2.1,0.8,0.2,0.2,1.1,2.3,6.1,8.4},
        {7.2,9.9,8.4,3.3,1.2,0.8,0.4,0.0,0.6,1.7,4.3,6.2},
        {7.6,5.6,3.8,2.8,3.8,0.2,0.0,0.0,0.0,1.3,2.6,5.2}
    };
    int year, month;
    float subtot, total;
    
    printf(" YEAR    RAINFALL  (inches)\n");
    for (year = 0, total = 0; year < YEARS; year++)
    {             // for each year, sum rainfall for each month
        for (month = 0, subtot = 0; month < MONTHS; month++)
            subtot += rain[year][month];
        printf("%5d %15.1f\n", 2010 + year, subtot);
        total += subtot; // total for all years
    }
    printf("\nThe yearly average is %.1f inches.\n\n",
           total/YEARS);
    printf("MONTHLY AVERAGES:\n\n");
    printf(" Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct ");
    printf(" Nov  Dec\n");
    
    for (month = 0; month < MONTHS; month++)
    {             // for each month, sum rainfall over years
        for (year = 0, subtot =0; year < YEARS; year++)
            subtot += rain[year][month];
        printf("%4.1f ", subtot/YEARS);
    }
    printf("\n");
    
    return 0;
}

// (base) kimshan@MacBook-Pro output % ./"rain"
//  YEAR    RAINFALL  (inches)
//  2010            32.4
//  2011            37.9
//  2012            49.8111
//  2013            44.0
//  2014            32.9
// 
// The yearly average is 39.4 inches.
// 
// MONTHLY AVERAGES:
// 
//  Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec
//  7.3  7.3  4.9  3.0  2.3  0.6  1.2  0.3  0.5  1.7  3.6  6.7 
```

</details>







