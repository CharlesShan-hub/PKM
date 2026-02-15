
# IO

缓冲区

字符先输入到缓冲区，然后再由程序读取。

* 完全缓冲：缓冲区满
* 行缓冲：读到\n

## 结束键盘输入

文件、流和键盘输入：[[../library/stdio|👉 stdio]]

文件结尾

1. `while ((ch = getchar()) != EOF)`
2. EOF是什么：`#define EOF -1`，因为 char 是 0～127，-1 不会用到

## 重定向和文件

1. 重定向输入：大于号或小于号从文件指向可执行文件
2. 重定向输出：大于号或小于号从可执行文件指向文件

<details>

<summary>Demo</summary>

* file1 和 file2 是文件名
* prog 是程序名
* 把输出重定向到文件：`prog >file1`
* 把输入重定向到文件：`prog <file1`
* 组合重定向：`prog <file2 >file1`，`prog >file1 <file2`

```c
// file_eof.c --open a file and display it
#include <stdio.h>
#include <stdlib.h>  // for exit()
int main()
{
    int ch;
    FILE * fp;
    char fname[50];         // to hold the file name
    
    printf("Enter the name of the file: ");
    scanf("%s", fname);
    fp = fopen(fname, "r"); // open file for reading
    if (fp == NULL)         // attempt failed
    {
	    printf("Failed to open file. Bye\n");
	    exit(1);            // quit program
    }
    // getc(fp) gets a character from the open file
    while ((ch = getc(fp)) != EOF)
        putchar(ch);
    fclose(fp);             // close the file
    
    return 0;
}

```

</details>

## TIPs

<details>

<summary>输入一个字符，后边的\n会也保存成一个字符</summary>

```c
/* guess.c -- an inefficient and faulty number-guesser */
#include <stdio.h>
int main(void)
{
    int guess = 1;
    
    printf("Pick an integer from 1 to 100. I will try to guess ");
    printf("it.\nRespond with a y if my guess is right and with");
    printf("\nan n if it is wrong.\n");
    printf("Uh...is your number %d?\n", guess);
    while (getchar() != 'y')      /* get response, compare to y */
        printf("Well, then, is it %d?\n", ++guess);
    printf("I knew I could do it!\n");
    
    return 0;
}
```

```c
(base) kimshan@MacBook-Pro output % ./"guess"
Pick an integer from 1 to 100. I will try to guess it.
Respond with a y if my guess is right and with
an n if it is wrong.
Uh...is your number 1?
n
Well, then, is it 2?
Well, then, is it 3?
nn
Well, then, is it 4?
Well, then, is it 5?
Well, then, is it 6?
y
I knew I could do it!
```

Improved：

<pre class="language-c"><code class="lang-c">/* guess.c -- an inefficient and faulty number-guesser */
#include &#x3C;stdio.h>
int main(void)
{
    int guess = 1;

    printf("Pick an integer from 1 to 100. I will try to guess ");
    printf("it.\nRespond with a y if my guess is right and with");
    printf("\nan n if it is wrong.\n");
    printf("Uh...is your number %d?\n", guess);

<strong>    char responce;
</strong><strong>    while ((responce = getchar()) != 'y')
</strong>    {
        if (responce == 'n')
            printf("Well, then, is it %d?\n", ++guess);
        else
            printf("Sorry, I understand only y or n.\n");
<strong>        while (getchar() != '\n')
</strong><strong>            continue;
</strong>    }

    printf("I knew I could do it!\n");

    return 0;
}

</code></pre>

```bash
(base) kimshan@MacBook-Pro output % ./"a"
Pick an integer from 1 to 100. I will try to guess it.
Respond with a y if my guess is right and with
an n if it is wrong.
Uh...is your number 1?
n
Well, then, is it 2?
nnn
Well, then, is it 3?
y
I knew I could do it!
```



</details>

<details>

<summary> 既要输入字符，又要输入数字</summary>

错误案例

```c
/* showchar1.c -- program with a BIG I/O problem */
#include <stdio.h>
void display(char cr, int lines, int width);
int main(void)
{
    int ch;             /* character to be printed    */
    int rows, cols;     /* number of rows and columns */
    printf("Enter a character and two integers:\n");
    while ((ch = getchar()) != '\n')
    {
        scanf("%d %d", &rows, &cols);
        display(ch, rows, cols);
        printf("Enter another character and two integers;\n");
        printf("Enter a newline to quit.\n");
    }
    printf("Bye.\n");
    
    return 0;
}

void display(char cr, int lines, int width)
{
    int row, col;
    
    for (row = 1; row <= lines; row++)
    {
        for (col = 1; col <= width; col++)
            putchar(cr);
        putchar('\n');  /* end line and start a new one */
    }
}

```

&#x20;会发现，执行了一轮，程序自动退出了。

```bash
(base) kimshan@MacBook-Pro output % ./"showchar1"
Enter a character and two integers:
* 2 3
***
***
Enter another character and two integers;
Enter a newline to quit.
Bye.
```

进行下面的修改：在 scanf后边，把\n收走

<pre class="language-c"><code class="lang-c">/* showchar2.c -- prints characters in rows and columns */
#include &#x3C;stdio.h>
void display(char cr, int lines, int width);
int main(void)
{
    int ch;             /* character to be printed      */
    int rows, cols;     /* number of rows and columns   */
    
    printf("Enter a character and two integers:\n");
    while ((ch = getchar()) != '\n')
    {
        if (scanf("%d %d",&#x26;rows, &#x26;cols) != 2)
            break;
        display(ch, rows, cols);
<strong>        while (getchar() !=  '\n')
</strong><strong>            continue;
</strong>        printf("Enter another character and two integers;\n");
        printf("Enter a newline to quit.\n");
    }
    printf("Bye.\n");
    
    return 0;
}

void display(char cr, int lines, int width)
{
    int row, col;
    
    for (row = 1; row &#x3C;= lines; row++)
    {
        for (col = 1; col &#x3C;= width; col++)
            putchar(cr);
        putchar('\n');  /* end line and start a new one */
    }
}

</code></pre>



</details>

<details>

<summary> 对输入进行检查</summary>



<pre class="language-c"><code class="lang-c">// checking.c -- validating input
#include &#x3C;stdio.h>
#include &#x3C;stdbool.h>
// validate that input is an integer
long get_long(void);
// validate that range limits are valid
bool bad_limits(long begin, long end,
                long low, long high);
// calculate the sum of the squares of the integers
// a through b
double sum_squares(long a, long b);
int main(void)
{
    const long MIN = -10000000L;  // lower limit to range
    const long MAX = +10000000L;  // upper limit to range
    long start;                   // start of range
    long stop;                    // end of range
    double answer;
    
    printf("This program computes the sum of the squares of "
           "integers in a range.\nThe lower bound should not "
           "be less than -10000000 and\nthe upper bound "
           "should not be more than +10000000.\nEnter the "
           "limits (enter 0 for both limits to quit):\n"
           "lower limit: ");
<strong>    start = get_long();
</strong>    printf("upper limit: ");
<strong>    stop = get_long();
</strong>    while (start !=0 || stop != 0)
    {
<strong>        if (bad_limits(start, stop, MIN, MAX))
</strong>            printf("Please try again.\n");
        else
        {
            answer = sum_squares(start, stop);
            printf("The sum of the squares of the integers ");
            printf("from %ld to %ld is %g\n",
                    start, stop, answer);
        }
        printf("Enter the limits (enter 0 for both "
               "limits to quit):\n");
        printf("lower limit: ");
<strong>        start = get_long();
</strong>        printf("upper limit: ");
<strong>        stop = get_long();
</strong>    }
    printf("Done.\n");
    
    return 0;
}

long get_long(void)
{
    long input;
    char ch;
    
    while (scanf("%ld", &#x26;input) != 1)
    {
        while ((ch = getchar()) != '\n')
            putchar(ch);  // dispose of bad input
        printf(" is not an integer.\nPlease enter an ");
        printf("integer value, such as 25, -178, or 3: ");
    }
    
    return input;
}

double sum_squares(long a, long b)
{
    double total = 0;
    long i;
    
    for (i = a; i &#x3C;= b; i++)
        total += (double)i * (double)i;
    
    return total;
}

bool bad_limits(long begin, long end,
                long low, long high)
{
    bool not_good = false;
    
    if (begin > end)
    {
        printf("%ld isn't smaller than %ld.\n", begin, end);
        not_good = true;
    }
    if (begin &#x3C; low || end &#x3C; low)
    {
        printf("Values must be %ld or greater.\n", low);
        not_good = true;
    }
    if (begin > high || end > high)
    {
        printf("Values must be %ld or less.\n", high);
        not_good = true;
    }
    
    return not_good;
}

</code></pre>

</details>
