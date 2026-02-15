
# Storage

## 存储类别

### 作用域

1. 块作用域：其实就是花括号（在 C99 之前确实就是这样）
2. for 循环，while 循环，do while 循环，if 语句所用值得代码，及时没有花括号，也算作用域的一部分

```c
#include<stdio.h>
int main()
{
    for(int i=0; i<1;i++)
        printf("%d",i);
}
```

3. 只有在变长数组中，形参名才有用：`void use_a_VLA(int n, int m, ar[n][m]);`
4. 在 main 外边的变量，作用域是这个文件

### 链接

<pre class="language-c"><code class="lang-c">#include &#x3C;stdio.h>

<strong>int giants = 5;         // 文件作用域，外部链接
</strong><strong>static int dodgers = 3; // 文件作用域，内部链接
</strong>
int main()
{
    return 0;
}
</code></pre>

### 存储期

* 静态存储期：程序执行是一直存在——文件作用域
* 线程存储期：以\_\_Thread\_local声明一个独享，每个线程都获得改变量的私有备份
* 自动存储期：块作用域
* 动态分配存储期：malloc

| 存储类别   | 存储期 | 作用域 | 链接 | 声明方式                |
| ------ | --- | --- | -- | ------------------- |
| 自动     | 自动  | 块   | 无  | 块内                  |
| 寄存器    | 自动  | 块   | 无  | 块内, 使用关键字 register  |
| 静态外部链接 | 静态  | 文件  | 外部 | 所有函数外               |
| 静态内部链接 | 静态  | 文件  | 内部 | 所有函数外, 使用关键字 static |
| 静态无链接  | 静态  | 块   | 无  | 块内, 使用关键字 static    |

### 自动变量

可以显示的写：**auto**。（最好不要用 auto，因为和 C++不统一）。

我们可以实现 rust 中的“遮蔽”，C 里边叫“隐藏”

<details>

<summary>Demo</summary>

```
(base) kimshan@MacBook-Pro output % ./"hiding"
x in outer block: 30 at 0x7ff7bb130828
x in inner block: 77 at 0x7ff7bb130824
x in outer block: 30 at 0x7ff7bb130828
x in while loop: 101 at 0x7ff7bb130820
x in while loop: 101 at 0x7ff7bb130820
x in while loop: 101 at 0x7ff7bb130820
(这个最难理解，因为每次 while，里边的 x 都会重新声明，所以一直都是 101)
x in outer block: 34 at 0x7ff7bb130828
```

```c
// hiding.c -- variables in blocks
#include <stdio.h>
int main()
{
    int x = 30;      // original x
    
    printf("x in outer block: %d at %p\n", x, &x);
    {
        int x = 77;  // new x, hides first x
        printf("x in inner block: %d at %p\n", x, &x);
    }
    printf("x in outer block: %d at %p\n", x, &x);
    while (x++ < 33) // original x
    {
        int x = 100; // new x, hides first x 
        x++;
        printf("x in while loop: %d at %p\n", x, &x);
    }
    printf("x in outer block: %d at %p\n", x, &x);

    return 0;
}
```

</details>

### 寄存器变量

可以显示的写：**register**。（程序会尝试把内容存在寄存器，但不保证一定能存到，可能会被降级成普通）

`register int quick;`

### 块作用域的静态变量

可以显示的写：**static**。（证明了本文件可访问的全局变量）而且只被初始化一次。

<details>

<summary>Demo</summary>

```c
/* loc_stat.c -- using a local static variable */
#include <stdio.h>
void trystat(void);

int main(void)
{
    int count;

    for (count = 1; count <= 3; count++)
    {
        printf("Here comes iteration %d:\n", count);
        trystat();
    }

    return 0;
}

void trystat(void)
{
    int fade = 1;
    static int stay = 1;

    printf("fade = %d and stay = %d\n", fade++, stay++);
}

// (base) kimshan@MacBook-Pro output % ./"loc_stat"
// Here comes iteration 1:
// fade = 1 and stay = 1
// Here comes iteration 2:
// fade = 1 and stay = 2
// Here comes iteration 3:
// fade = 1 and stay = 3
```

</details>

### 外部链接的静态变量

使用外部的变量：extern。

* 如果用本文件内的全局变量，可以选择的写 extern
* 如果用别的文件的全局变量，必须要写 extern
* 不要用 extern 来创建新的变量，他是用来引用别的变量的

<details>

<summary>Demo</summary>

```c
int Erupt;            /* 外部定义的变量 */
double Up[100];       /* 外部定义的数组 */
extern char Coal;     /* 如果Coal被定义在另一个文件,则必须这样声明*/
void next(void);      
int main(void)
{
    extern int Erupt;  /* 可选的声明*/
    extern double Up[];/* 可选的声明*/
    ...
}
void next(void)
{
    ...
}
```

</details>

注意，初始化不可以用变量

```c
#include<stdio.h>
int x = 10; // 可以
int x2 = 2*x; // 不可以
int x3 = 2*10; // 可以
int main(){return 0;}
```

### 内部链接的静态变量

略

### 多文件

略

### 存储类别说明符

总结一下以上内容，一共六个关键字：

* &#x20;auto
* register
* static
* extern
* \_Thread\_local
* typedef

只有 \_Thread\_local可以和 static 火化 extern 一起使用，其他的都只能单独使用。

### 存储类别和函数

函数也有存储类别

```c
double gamma(double);
// 外部函数：本文件可调用，别的文件不能调用它
static double beta(int, int);
// 内部函数：本文件可以调用，别的文件不能调用它
extern double delta(double, int);
// 调用别的文件的函数，要这样先声明一下
```

### 存储类别的选择

外部存储类别方便但不安全，请不要什么都用外部存储类别。

***

## 随机数函数和静态变量

种子“next”是具有内部链接的静态变量，rand0 函数是具有外部链接的函数，可以被别的文件调用

```c
/* rand0.c –– produces random numbers            */
/*               uses ANSI C portable algorithm  */
static unsigned long int next = 1;  /* the seed  */

unsigned int rand0(void)
{
    /* magic formula to generate pseudorandom number */
    next = next * 1103515245 + 12345;
    return (unsigned int) (next/65536) % 32768;
}
```

```c
/* r_drive0.c -- test the rand0() function */
/* compile with rand0.c                    */
#include <stdio.h>
extern unsigned int rand0(void);

int main(void)
{
    int count;

    for (count = 0; count < 5; count++)
        printf("%d\n", rand0());

    return 0;
}

// (base) kimshan@MacBook-Pro Ch12 % gcc rand0.c r_drive0.c -o a
// (base) kimshan@MacBook-Pro Ch12 % ./a
// 16838
// 5758
// 10113
// 17515
// 31051
```

我们可以发现，种子是固定的，每次都是从16838这里开始，我们进一步写一个更新 seed 的函数

```c
/* s_and_r.c -- file for rand1() and srand1()    */
/*                uses ANSI C portable algorithm */
static unsigned long int next = 1;  /* the seed  */

int rand1(void)
{
    /* magic formula to generate pseudorandom number */
    next = next * 1103515245 + 12345;
    return (unsigned int) (next/65536) % 32768;
}

void srand1(unsigned int seed)
{
    next = seed;
}

```

````c
/* r_drive1.c -- test rand1() and srand1() */
/* compile with s_and_r.c                  */
#include <stdio.h>
#include <stdlib.h>
extern void srand1(unsigned int x);
extern int rand1(void);

int main(void)
{
    int count;
    unsigned seed;
    
    printf("Please enter your choice for seed.\n");
    while (scanf("%u", &seed) == 1)
    {
        srand1(seed);    /* reset seed */
        for (count = 0; count < 5; count++)
            printf("%d\n", rand1());
        printf("Please enter next seed (q to quit):\n");
    }
    printf("Done\n");
    
    return 0;
}

// (base) kimshan@MacBook-Pro Ch12 % gcc s_and_r.c r_drive1.c -o b
// (base) kimshan@MacBook-Pro Ch12 % ./b
// Please enter your choice for seed.
// 100
// 12662
// 23392
// 22561
// 20718
// 6314
// Please enter next seed (q to quit):
// 200
// 25325
// 25316
// 2367
// 19320
// 9131
// Please enter next seed (q to quit):
// q
// Done
```
````

***

## malloc 和 free

```c
double *p = (double *)malloc(30*sizeof(double));
```

注意是 double \*，它要指向 double，而不是指向 30 个大小的 double！

```c
if(p==NULL)
{
    puts("Memory out!");
    exit(EXIT_FAILURE);
}
```

记得要 free

```c
free(p);
```

也可以用 calloc

```c
double *q = (double *)malloc(30, sizeof(double)); // 就一点区别
```

***

## ANSI C 类型限定符

### const

1. 幂等性

```c
const const const int n=6;
```

等同于

```c
const int n=6;
```

所以我们可以这么写

```c
typedef const int zip;
const zip q=8;
```

2. 指针与 const

```c
#include <stdio.h>

int main()
{
    { // const 在 * 左边
        double d1 = 100.0;
        double d2 = 100.0;
        const double *p1 = &d1; // 限定的是double 是 const
        // double const *p1 = &d1; // 一样
        p1 = &d2; // 可以，指针可变
        // *p1 = d2;            // 不行, 值不能变
    }
    { // const 在 * 右边
        double d1 = 100.0;
        double d2 = 100.0;
        double *const p1 = &d1; // 限定的是double 是 const
        // p1 = &d2;            // 不行，指针不能变
        *p1 = d2; // 可以, 值可以变
    }

    return 0;
}
```

全局变量很危险，所以使用 const 限制它会很好！

### volatile

volatile 和 const 语法一样，volatile 用于给编译器优化用。比如一个地址存的是当前的时钟时间，需要不停的改变。

<details>

<summary>GPT</summary>

`volatile` 关键字在以下几种情况下是必须的：

1.  **硬件寄存器映射**：当变量被映射到硬件寄存器时，这些寄存器的值可能会在没有显式软件操作的情况下改变（例如，由硬件事件触发）。在这种情况下，声明为 `volatile` 可以防止编译器优化掉对这些变量的读取和写入操作。

    ```c
    volatile uint32_t * hardwareRegister = (uint32_t *)0x12345678; // 假设地址是硬件寄存器的地址
    ```
2.  **多线程共享变量**：在多线程程序中，如果多个线程共享一个变量，并且至少有一个线程可能会在任何时候修改它，那么这个变量应该被声明为 `volatile`，以防止编译器假设它在没有显式同步的情况下保持不变。

    ```c
    volatile int sharedFlag = 0; // 在多个线程中共享的标志
    ```
3.  **中断服务例程（ISR）**：在中断服务例程中使用的变量，或者在主程序中被中断服务例程修改的变量，应该声明为 `volatile`，因为中断可以在程序的任何地方发生，从而改变这些变量的值。

    ```c
    volatile int interruptCounter = 0; // 在中断服务例程中递增的计数器
    ```
4.  **非原子操作**：在某些情况下，对变量的读写操作不是原子的，特别是在32位或更大数据类型的变量在32位处理器上。如果变量可能被不同的线程或中断以非原子方式修改，那么它应该被声明为 `volatile`。

    ```c
    volatile long nonAtomicValue; // 在多线程环境中可能被非原子方式修改的值
    ```
5. **操作系统特定的同步机制**：在某些操作系统中，特定的同步机制（如信号量、事件等）可能要求相关的变量声明为 `volatile`，以确保编译器不会对它们的访问进行优化。 在所有这些情况下，使用 `volatile` 关键字可以确保编译器生成的代码能够正确地反映变量可能的变化，从而避免由于编译器优化而导致的潜在错误。然而，需要注意的是，`volatile` 并不提供任何线程同步机制，它只是告诉编译器不要对变量进行不必要的优化。对于多线程同步，仍然需要使用互斥锁（mutexes）、信号量（semaphores）或其他同步机制。

</details>

### restrict (C99)

<details>

<summary>GPT</summary>

\
`restrict` 是 C99 标准引入的一个关键字，用于限定指针的属性。当一个指针被指定为 `restrict` 时，它表示该指针指向的对象在当前作用域内是唯一的，即不会有其他指针同时指向该对象。这样可以允许编译器进行更多的优化，尤其是在涉及到内存操作的场合。

具体来说，当你使用 `restrict` 关键字来修饰一个指针参数时，你是在告诉编译器，除了通过这个指针以外，没有其他途径可以访问到这个对象。这意味着编译器可以安全地进行一些假设，例如它可以放心地将数据缓存到寄存器中，而不必担心会有其他的指针导致缓存失效。

举个例子，考虑下面的函数原型：

c复制

```
void my_function(restrict int *ptr);
```

在这个例子中，`my_function` 函数接受一个类型为 `int` 的指针作为参数，并且这个指针被标记为 `restrict`。这就意味着在 `my_function` 内部，只有通过 `ptr` 指针才能访问到它所指向的数据，没有任何其他指针可以同时指向这块内存区域。

请注意，`restrict` 关键字的用法有一定的限制。首先，它只能用于限定指向对象的指针，而不能用于标量类型。其次，`restrict` 只能用来修饰指针本身，不能直接作用于指针所指的对象的类型上。最后，`restrict` 关键字的使用还需要依赖于具体的编译器和平台支持。

总结一下，`restrict` 关键字的主要目的是为了帮助编译器进行更好的优化，尤其是对于那些涉及大量内存操作的代码。通过明确指出某块内存的唯一访问路径，开发者可以帮助编译器减少不必要的内存屏障和缓存刷新，从而提高程序的执行效率。

</details>

<details>

<summary>Demo</summary>

```c
#include <stdio.h>

void copy_memory(const int *restrict src, int *restrict dst, size_t n)
{
    for (size_t i = 0; i < n; ++i)
    {
        dst[i] = src[i]; // 编译器可以假设src和dst不会重叠
    }
}

int main()
{
    size_t n = 10;
    int src_array[n];
    int dst_array[n];

    // 初始化源数组
    for (size_t i = 0; i < n; ++i)
    {
        src_array[i] = i;
    }

    // 调用函数，使用restrict关键字
    copy_memory(src_array, dst_array, n);

    // 打印目标数组来验证拷贝是否成功
    printf("Copied array:\n");
    for (size_t i = 0; i < n; ++i)
    {
        printf("%d ", dst_array[i]);
    }
    printf("\n");

    return 0;
}

```

</details>

### \_Atomic (C11)

并发中的原子性。一个进程访问他时，别的进程不能访问。
