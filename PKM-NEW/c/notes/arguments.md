# Arguments

## Operater

### 基本运算符

* 赋值：`=`
  * 可以三重赋值：`int a,b,c; a = b = c = 1;`
  * 赋值的顺序是从右向左
* 加法：`+`
* 减法：`-`
* 符号：`-`与`+`（就是正负号，C90 才可以用）
* 乘法：`*`
* 除法：`/`
  * 如果是整数除法会截断，浮点数除法得到浮点数
* 取模：`%`
  * 不能用于浮点数
  * 负数怎么办
* 递增运算符：`++`
  * 前缀模式，后缀模式
  * 优先级：括号 > 递增递减 > 其他
* 递减运算符：`--`
* 比较：`==`，`>=`，`<=`，`<`，`>`

### 逻辑运算符

* 与或非：`&&`，`||`，`！`
* [[../library/iso646|👉 iso646]]

### 其他运算符

* `sizeof` 函数返回 `size_t` 类型的值，这是个无符号整型。
* C99 可以用 `%zd` 对应 `size_t` 类型的值，如果编译器支持也可以用 `%u` 或 `%lu`。

### 运算符优先级

| 运算符（优先级从高至低）     | 结合律      |
| ---------------- | -------- |
| ()               | 从左往右     |
| - + ++ -- sizeof | 从右往左     |
| \* / %           | 从左往右     |
| + -              | 从左往右     |
| < > <= >=        | 从左往右     |
| == !=            | 从左往右     |
| && \|\|          | **从右向左** |
| =                | 从右往左     |

### 不要自作聪明

`ans = num/2 + 5*(1 + num++);`

编译器会自己选择先运算`num/2`还是`5*(1 + num++)`

所以不要写这样的代码！

***

## Expression and Argument

* 表达式（expression）
  * <mark style="color:red;">每个表达式都有一个值</mark>。
  * 表达式是常量、变量或二者的组合。
* 语句（argument）
  * 语句是一条完整的计算机指令，以分号结尾（大多数）。
  * 单独一个分号叫做空语句。
  * `int a = 1;`这个语句去掉分号并不是表达式。
* 副作用（side effect）
  * c 语言的角度，它的目的是对表达式进行求值。如果改变了某个内存的数据，这个就是副作用。
  * 比如：`a = 5;`，求“5”本身是目的，把 5 存在了 a 是副作用。
  * （这么看有一种万物归一的感觉，表达式求值与改变内存进行了统一）
* 序列点（sequence point）
  * 程序执行的点：一个分号就是一个序列点，一个完整表达式的结束也算是一个序列点。
* 完整表达式（full expression）
  * 某个表达式并不是一个更大表达式的一部分
  * 比如：`while(i++ < 10) printf("%d \n", i);`，其中`i++ < 10`就是一个完整表达式。
  * 比如：，`y = (4+x++) + (6+x++)`，其中`4+x++`就不是一个完整表达式。因为程序无法保证x 在`4+x++`之后不再变化。

***

## Loop

### while

```c
while (expression)
    statement
```

while + scanf，循环输入

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


while + scanf，输入一个字符串
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

</details>

### do while

```c
do
    statement
while(expression);
```

### for

```c
for(init; condition; update)
    statement
```

等价于

```c
init
for(;condition;)
{
    statement
    update
}
```

可以省略init，condition，update，statement任意位置

另外可以用逗号插入多个内容在一个语句里：`for(int i=1,j=2; i+j<100; i++,j++)`

***

## Branch

### if, else

```c
// electric.c -- calculates electric bill 
#include <stdio.h>
#define RATE1   0.13230       // rate for first 360 kwh      
#define RATE2   0.15040       // rate for next 108 kwh  
#define RATE3   0.30025       // rate for next 252 kwh
#define RATE4   0.34025       // rate for over 720 kwh       
#define BREAK1  360.0         // first breakpoint for rates  
#define BREAK2  468.0         // second breakpoint for rates 
#define BREAK3  720.0         // third breakpoint for rates
#define BASE1   (RATE1 * BREAK1)
// cost for 360 kwh            
#define BASE2  (BASE1 + (RATE2 * (BREAK2 - BREAK1)))
// cost for 468 kwh
#define BASE3   (BASE1 + BASE2 + (RATE3 *(BREAK3 - BREAK2)))
//cost for 720 kwh
int main(void)
{
    double kwh;               // kilowatt-hours used         
    double bill;              // charges                     
    
    printf("Please enter the kwh used.\n");
    scanf("%lf", &kwh);       // %lf for type double         
    if (kwh <= BREAK1)
        bill = RATE1 * kwh;
    else if (kwh <= BREAK2)   // kwh between 360 and 468     
        bill = BASE1 + (RATE2 * (kwh - BREAK1));
    else if (kwh <= BREAK3)   // kwh betweent 468 and 720
        bill = BASE2 + (RATE3 * (kwh - BREAK2));
    else                      // kwh above 680               
        bill = BASE3 + (RATE4 * (kwh - BREAK3));
    printf("The charge for %.1f kwh is $%1.2f.\n", kwh, bill);
    
    return 0;
}

```


### ?:（条件运算符）

```c
if(condition)
    statement1
else
    statement2
```

等价于

```c
condition ? statement1 : statement2
```

注意， Rust 里边的 if else 是表达式，但是C 里边 if else 并不是表达式

```c
#include <stdio.h>

int main()
{
    int a = 100;
    int b = a == 100 ? a + 1 : a + 2;
    int c = (if (a == 100) a + 1 else a + 2); // wrong!
    return 0;
}
```


### break, continue

break和 continue 都是针对本轮循环

### switch

本质就是 if else

```c
/* animals.c -- uses a switch statement */
#include <stdio.h>
#include <ctype.h>
int main(void)
{
    char ch;
    
    printf("Give me a letter of the alphabet, and I will give ");
    printf("an animal name\nbeginning with that letter.\n");
    printf("Please type in a letter; type # to end my act.\n");
    while ((ch = getchar()) != '#')
    {
        if('\n' == ch)
            continue;
        if (islower(ch))     /* lowercase only          */
            switch (ch)
        {
            case 'a' :
                printf("argali, a wild sheep of Asia\n");
                break;
            case 'b' :
                printf("babirusa, a wild pig of Malay\n");
                break;
            case 'c' :
                printf("coati, racoonlike mammal\n");
                break;
            case 'd' :
                printf("desman, aquatic, molelike critter\n");
                break;
            case 'e' :
                printf("echidna, the spiny anteater\n");
                break;
            case 'f' :
                printf("fisher, brownish marten\n");
                break;
            default :
                printf("That's a stumper!\n");
        }                /* end of switch           */
        else
            printf("I recognize only lowercase letters.\n");
        while (getchar() != '\n')
            continue;      /* skip rest of input line */
        printf("Please type another letter or a #.\n");
    }                        /* while loop end          */
    printf("Bye!\n");
    
    return 0;
}

```



如果没有 break 就会进入下一个代码块，可以利用这个特性，制作多重标签

```c
// vowels.c -- uses multiple labels
#include <stdio.h>
int main(void)
{
    char ch;
    int a_ct, e_ct, i_ct, o_ct, u_ct;

    a_ct = e_ct = i_ct = o_ct = u_ct = 0;

    printf("Enter some text; enter # to quit.\n");
    while ((ch = getchar()) != '#')
    {
        switch (ch)
        {
        case 'a':
        case 'A':
            a_ct++;
            break;
        case 'e':
        case 'E':
            e_ct++;
            break;
        case 'i':
        case 'I':
            i_ct++;
            break;
        case 'o':
        case 'O':
            o_ct++;
            break;
        case 'u':
        case 'U':
            u_ct++;
            break;
        default:
            break;
        } // end of switch
    } // while loop end
    printf("number of vowels:   A    E    I    O    U\n");
    printf("                 %4d %4d %4d %4d %4d\n",
           a_ct, e_ct, i_ct, o_ct, u_ct);

    return 0;
}

// (base) kimshan@MacBook-Pro output % ./"vowels"
// Enter some text; enter # to quit.
// A
// a
// #
// number of vowels:   A    E    I    O    U
//                     2    0    0
```

***

## Jump

### goto

唯一的 goto 使用场景：跳出多重循环

```c
#include <stdio.h>

int main()
{

    for (int i = 0; i < 3; ++i)
    {
        for (int j = 0; j < 3; ++j)
        {
            for (int k = 0; k < 3; ++k)
            {
                printf("i: %d, j: %d, k: %d\n", i, j, k);
                // 假设当 i == 1, j == 2, k == 2 时，我们需要跳出所有循环
                if (i == 1 && j == 2 && k == 2)
                {
                    goto end_of_loops;
                }
            }
        }
    }

end_of_loops:
    printf("跳出所有循环。\n");
test:
    printf("不调用也会 print\n");

    return 0;
}
// (base) kimshan@MacBook-Pro output % ./"a"
// i: 0, j: 0, k: 0
// i: 0, j: 0, k: 1
// i: 0, j: 0, k: 2
// i: 0, j: 1, k: 0
// i: 0, j: 1, k: 1
// i: 0, j: 1, k: 2
// i: 0, j: 2, k: 0
// i: 0, j: 2, k: 1
// i: 0, j: 2, k: 2
// i: 1, j: 0, k: 0
// i: 1, j: 0, k: 1
// i: 1, j: 0, k: 2
// i: 1, j: 1, k: 0
// i: 1, j: 1, k: 1
// i: 1, j: 1, k: 2
// i: 1, j: 2, k: 0
// i: 1, j: 2, k: 1
// i: 1, j: 2, k: 2
// 跳出所有循环。
// 不调用也会 print
```
