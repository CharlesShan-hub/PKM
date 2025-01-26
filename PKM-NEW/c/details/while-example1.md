这个程序允许用户输入一个基数和一个指数，然后计算并显示这个基数乘以自身指数次的结果。如果用户输入了非数值字符（例如 ‘q’），程序将停止接收输入并退出。

```c
// power.c -- raises numbers to integer powers
#include <stdio.h>
double power(double n, int p); // ANSI prototype
int main(void)
{
    double x, xpow;
    int exp;
    
    printf("Enter a number and the positive integer power");
    printf(" to which\nthe number will be raised. Enter q");
    printf(" to quit.\n");
    while (scanf("%lf%d", &x, &exp) == 2)
    {
        xpow = power(x,exp);   // function call
        printf("%.3g to the power %d is %.5g\n", x, exp, xpow);
        printf("Enter next pair of numbers or q to quit.\n");
    }
    printf("Hope you enjoyed this power trip -- bye!\n");
    
    return 0;
}

double power(double n, int p)  // function definition
{
    double pow = 1;
    int i;
    
    for (i = 1; i <= p; i++)
        pow *= n;
    
    return pow;                // return the value of pow
}

```

```
(base) kimshan@MacBook-Pro output % ./"power"
Enter a number and the positive integer power to which
the number will be raised. Enter q to quit.
1 2
1 to the power 2 is 1
Enter next pair of numbers or q to quit.
1.1 2
1.1 to the power 2 is 1.21
Enter next pair of numbers or q to quit.
100 2    
100 to the power 2 is 10000
Enter next pair of numbers or q to quit.
100.1 2
100 to the power 2 is 10020
Enter next pair of numbers or q to quit.
100 11.1
100 to the power 11 is 1e+22
Enter next pair of numbers or q to quit.
q
Hope you enjoyed this power trip -- bye!
```
