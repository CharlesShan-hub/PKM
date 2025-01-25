# Advanced Data Type

---

![[../assets/advanced-data-type-drawing|1000]]

--- 

## struct

record in pascal

```pascal
program PrintBirthday;

type
    birthday = record
        year : integer;
        month : integer;
        day : integer;
    end;

var
    b : birthday;

begin
    b := (year: 2000; month: 1; day: 1); // 创建并初始化生日记录

    // 打印生日
    writeln('Birthday: ', b.day, '/', b.month, '/', b.year);
end.
```

struct in C

```c
//* book.c -- one-book inventory */
#include &#x3C;stdio.h>
#include &#x3C;string.h>
char * s_gets(char * st, int n);
#define MAXTITL  41      /* maximum length of title + 1         */
#define MAXAUTL  31      /* maximum length of author's name + 1 */

struct book {            /* structure template: tag is book     */
    char title[MAXTITL];
    char author[MAXAUTL];
    float value;
};                       /* end of structure template           */

int main(void)
{
<strong>    struct book library; /* declare library as a book variable  */
</strong>    
    printf("Please enter the book title.\n");
    s_gets(library.title, MAXTITL); /* access to the title portion         */
    printf("Now enter the author.\n");
    s_gets(library.author, MAXAUTL);
    printf("Now enter the value.\n");
    scanf("%f", &#x26;library.value);
    printf("%s by %s: $%.2f\n",library.title,
           library.author, library.value);
    printf("%s: \"%s\" ($%.2f)\n", library.author,
           library.title, library.value);
    printf("Done.\n");
    
    return 0;
}

char * s_gets(char * st, int n)
{
    char * ret_val;
    char * find;
    
    ret_val = fgets(st, n, stdin);
    if (ret_val)
    {
        find = strchr(st, '\n');   // look for newline
        if (find)                  // if the address is not NULL,
            *find = '\0';          // place a null character there
        else
            while (getchar() != '\n')
                continue;          // dispose of rest of line
    }
    return ret_val;
}
```

```shell
(base) kimshan@MacBook-Pro output % ./"book"
Please enter the book title.
Hello
Now enter the author.
Charles
Now enter the value.
10
Hello by Charles: $10.00
Charles: "Hello" ($10.00)
Done.
```

struct 基础

声明

```c
// 1
struct book {            /* structure template: tag is book     */
    char title[MAXTITL];
    char author[MAXAUTL];
    float value;
};                       /* end of structure template           */
struct book library, *p_lib;

// 2 简化
struct book { 
    char title[MAXTITL];
    char author[MAXAUTL];
    float value;
} library, *p_lib;

// 3. 数组
struct book library[MAXBOOKS];

// 4. 嵌套
struct book {
    char title[MAXTITL];
    char author[MAXAUTL];
    float value;
    struct book[MAXRELATE] res;
} library[MAXBOOKS];

// 5 typedef
typedef struct BiTNode
{
    int data;
    struct BiTNode *lchild;
    struct BiTNode *rchild;
    //struct BiTNode *parent; // 变成了 三叉链表
}BiTNode,*BiTree;
```

初始化

```c
// 1. 按顺序
struct book library = 
{
    "The Pious Pirate and te Devious Damsel",
    "Rennee Vivotte",
    1.95
};

// 2. 按成员
struct book gift = 
{
    .value = 25.99;
    .author = "Me";
    .title = "You";
}
```

访问

```c
scanf("%f", &library.value);
s_gets(library.author, MAXAUTL);

scanf("%f", &p_lib->value);
s_gets(p_lib->author, MAXAUTL);
```









<details>

<summary>struct + malloc</summary>

struct 中声明字符串然后 scanf 进来会导致错误（可能把字符串保存在任意位置）

<pre class="language-c"><code class="lang-c">#include &#x3C;stdio.h>

#define LEN 20

struct names {
    char first[LEN];
    char last[LEN];
};

int main() {
    struct names veep = {"Talia", "Summers"};
    struct pnames treas = {"Brad", "Fallingjaw"};
    
    printf("%s and %s\n", veep.first, treas.first);
    
<strong>    struct names accountant;
</strong><strong>    struct names attorney;
</strong>
    printf("Enter the last name of your accountant: ");
<strong>    scanf("%s", accountant.last);
</strong>
    printf("Enter the last name of your attorney: ");
<strong>    scanf("%s", attorney.last); /* 这里有一个潜在的危险 */
</strong>    
    return 0;
}
</code></pre>

现在更好的办法是，struct 里边不要字符串，而是改成指针，每次去 malloc

<pre class="language-c"><code class="lang-c">// names3.c -- use pointers and malloc()
#include &#x3C;stdio.h>
#include &#x3C;string.h>   // for strcpy(), strlen()
#include &#x3C;stdlib.h>   // for malloc(), free()
#define SLEN 81
struct namect {
<strong>    char * fname;  // using pointers
</strong><strong>    char * lname;
</strong>    int letters;
};

void getinfo(struct namect *);        // allocates memory
void makeinfo(struct namect *);
void showinfo(const struct namect *);
void cleanup(struct namect *);        // free memory when done
char * s_gets(char * st, int n);

int main(void)
{
    struct namect person;
    
    getinfo(&#x26;person);
    makeinfo(&#x26;person);
    showinfo(&#x26;person);
    cleanup(&#x26;person);
    
    return 0;
}

void getinfo (struct namect * pst)
{
    char temp[SLEN];
    printf("Please enter your first name.\n");
    s_gets(temp, SLEN);
    // allocate memory to hold name
<strong>    pst->fname = (char *) malloc(strlen(temp) + 1);
</strong>    // copy name to allocated memory
    strcpy(pst->fname, temp);
    printf("Please enter your last name.\n");
    s_gets(temp, SLEN);
<strong>    pst->lname = (char *) malloc(strlen(temp) + 1);
</strong>    strcpy(pst->lname, temp);
}

void makeinfo (struct namect * pst)
{
    pst->letters = strlen(pst->fname) +
    strlen(pst->lname);
}

void showinfo (const struct namect * pst)
{
    printf("%s %s, your name contains %d letters.\n",
           pst->fname, pst->lname, pst->letters);
}

void cleanup(struct namect * pst)
{
    free(pst->fname);
    free(pst->lname);
}

char * s_gets(char * st, int n)
{
    char * ret_val;
    char * find;
    
    ret_val = fgets(st, n, stdin);
    if (ret_val)
    {
        find = strchr(st, '\n');   // look for newline
        if (find)                  // if the address is not NULL,
            *find = '\0';          // place a null character there
        else
            while (getchar() != '\n')
                continue;          // dispose of rest of line
    }
    return ret_val;
}


</code></pre>

</details>

<details>

<summary>struct 复合字面量（C99）</summary>

<pre class="language-c"><code class="lang-c">/* complit.c -- compound literals */
#include &#x3C;stdio.h>
#define MAXTITL  41
#define MAXAUTL  31

struct book {          // structure template: tag is book
    char title[MAXTITL];
    char author[MAXAUTL];
    float value;
};

int main(void)
{
    struct book readfirst;
    int score;
    
    printf("Enter test score: ");
    scanf("%d",&#x26;score);
    
    if(score >= 84)
<strong>        readfirst = (struct book) {"Crime and Punishment",
</strong><strong>            "Fyodor Dostoyevsky",
</strong><strong>            11.25};
</strong>    else
<strong>        readfirst = (struct book) {"Mr. Bouncy's Nice Hat",
</strong><strong>            "Fred Winsome",
</strong><strong>            5.99};
</strong>    printf("Your assigned reading:\n");
    printf("%s by %s: $%.2f\n",readfirst.title,
           readfirst.author, readfirst.value);
    
    return 0;
}
</code></pre>

</details>

<details>

<summary>伸缩型成员变量（C99）</summary>

结构体里边的数组不写 MAX，只写 方括号，这样后边的 malloc 就要去计算大小了

<pre class="language-c"><code class="lang-c">// flexmemb.c -- flexible array member (C99 feature)
#include &#x3C;stdio.h>
#include &#x3C;stdlib.h>

struct flex
{
    size_t count;
    double average;
<strong>    double scores[];   // flexible array member
</strong>};

void showFlex(const struct flex * p);

int main(void)
{
<strong>    struct flex * pf1, *pf2;
</strong>    int n = 5;
    int i;
    int tot = 0;
    
    // allocate space for structure plus array
<strong>    pf1 = malloc(sizeof(struct flex) + n * sizeof(double));
</strong>    pf1->count = n;
    for (i = 0; i &#x3C; n; i++)
    {
        pf1->scores[i] = 20.0 - i;
        tot += pf1->scores[i];
    }
    pf1->average = tot / n;
    showFlex(pf1);
    
    n = 9;
    tot = 0;
<strong>    pf2 = malloc(sizeof(struct flex) + n * sizeof(double));
</strong>    pf2->count = n;
    for (i = 0; i &#x3C; n; i++)
    {
        pf2->scores[i] = 20.0 - i/2.0;
        tot += pf2->scores[i];
    }
    pf2->average = tot / n;
    showFlex(pf2);
    free(pf1);
    free(pf2);
    
    return 0;
}

void showFlex(const struct flex * p)
{
    int i;
    printf("Scores : ");
    for (i = 0; i &#x3C; p->count; i++)
        printf("%g ", p->scores[i]);
    printf("\nAverage: %g\n", p->average);
}

</code></pre>

</details>

<details>

<summary>匿名结构（C11）</summary>

<pre class="language-c"><code class="lang-c">struct person
{
    int id;
<strong>    struct {char first[20]; char last[20];}; // 匿名结构
</strong>};

// 初始化
struct person ted = {8483, {"ted", "grass"}};
</code></pre>

</details>

<details>

<summary>结构体保存在文件中</summary>

<pre class="language-c"><code class="lang-c"><strong>#define MAXTITL 40  
</strong>#define MAXAUTL 40  
struct book {    
char title[MAXTITL];   
char author[ MAXAUTL ];    
float value;  
};  
</code></pre>

1. 可以用 fprintf

```c
fprintf(pbooks, "%s. %s. %.2f\n", primer.title, primer.author, primer.value);
```

2. fprintf + 固定宽度

```c
fprintf(pbooks, "%39s%39s%8.2f\n", primer.title, primer.author, primer.value);
```

3. 保存二进制文件

以二进制表示法储存数据的缺点是,不同的系统可能使用不同的二进制表示法,所以数据文件可能不具可移植性。甚至同一个系统,不同编译器设置也可能导致不同的二进制布局。

```c
fwrite(&primer, sizeof(struct book),l,pbooks);  
```

</details>

***

## union

只能存一个变量的数组，推荐使用方式：结构+联合

```c
struct owner {
    char sosecurity[12];
    ...
};

struct leasecompany {
    char name[40];
    char headquarters[40];
    ...
};

union data {
    struct owner owncar;
    struct leasecompany leasecar;
};

struct car_data {
    char make[15];
    int status; /* 私有为0，租赁为1 */
    union data ownerinfo;
    ...
};
```

***

## enum

枚举，默认值是从 0 开始的 int，也可以自定义数值

```c
enum week = {Mon, Tus, Wen, Thr, Fri, Sat, Sun};
enum levels = {lows = 100, medium = 500, high = 2000};
```

Demo

```c
/* enum.c -- uses enumerated values */
#include <stdio.h>
#include <string.h>    // for strcmp(), strchr()
#include <stdbool.h>   // C99 feature
char * s_gets(char * st, int n);

enum spectrum {red, orange, yellow, green, blue, violet};
const char * colors[] = {"red", "orange", "yellow",
    "green", "blue", "violet"};
#define LEN 30

int main(void)
{
    char choice[LEN];
    enum spectrum color;
    bool color_is_found = false;
    
    puts("Enter a color (empty line to quit):");
    while (s_gets(choice, LEN) != NULL && choice[0] != '\0')
    {
        for (color = red; color <= violet; color++)
        {
            if (strcmp(choice, colors[color]) == 0)
            {
                color_is_found = true;
                break;
            }
        }
        if (color_is_found)
            switch(color)
        {
            case red    : puts("Roses are red.");
                break;
            case orange : puts("Poppies are orange.");
                break;
            case yellow : puts("Sunflowers are yellow.");
                break;
            case green  : puts("Grass is green.");
                break;
            case blue   : puts("Bluebells are blue.");
                break;
            case violet : puts("Violets are violet.");
                break;
        }
        else
            printf("I don't know about the color %s.\n", choice);
        color_is_found = false;
        puts("Next color, please (empty line to quit):");
    }
    puts("Goodbye!");
    
    return 0;
}

char * s_gets(char * st, int n)
{
    char * ret_val;
    char * find;
    
    ret_val = fgets(st, n, stdin);
    if (ret_val)
    {
        find = strchr(st, '\n');   // look for newline
        if (find)                  // if the address is not NULL,
            *find = '\0';          // place a null character there
        else
            while (getchar() != '\n')
                continue;          // dispose of rest of line
    }
    return ret_val;
}


```


***

## typedef

typedef 是编译器解释的，#define 是预处理器解释的。

typedef+结构(上边结构里边)

***

## 复杂声明

`int a[2][3];`

![[../assets/nested-array-drawing|1000]]

* 数组明后边的\[]和函数名后边的()具有相同优先级，他们优先级高于\*

```c
int *p[10]; // 含有十个指针的数组
int (*p)[10]; // 指向含有十个整数的数组的指针
```

```c
// 含有4 个指针的数组
    int *p[4];
    p[0] = &a[0][0];
    p[1] = &a[0][1];
    p[2] = &a[1][0];
    p[3] = &a[1][1];
    printf("%p %p %p %p\n", p[0], p[1], p[2], p[3]);
    printf("%d %d %d %d\n", *p[0], *p[1], *p[2], *p[3]);
    // 0x7ff7ba96b810 0x7ff7ba96b814 0x7ff7ba96b81c 0x7ff7ba96b820
    // 11 12 21 22

    // 指向数组的指针
    int num[4] = {100, 200, 300, 400};
    int(*q)[4] = num;
    printf("%p, sizeof(int)=%u,sizeof(q)=%u, sizeof(*q)=%u\n", q, sizeof(int), sizeof(q), sizeof(*q));
    printf("%d %d %d %d\n", (*q)[0], (*q)[1], (*q)[2], (*q)[3]);
    // 0x7ff7be28a7e0, sizeof(int)=4,sizeof(q)=8, sizeof(*q)=16
    // 100 200 300 400
```
