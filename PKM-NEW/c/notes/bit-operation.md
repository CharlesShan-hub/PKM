# Bit Operation

## 位运算符

按位与，或，非，异或

```c
#include <stdio.h>

void printBits(int num)
{
    // 获取整数的位数
    int bits = sizeof(num) * 8; // sizeof(num) 返回整数的大小（以字节为单位），乘以 8 得到位数

    // 遍历整数的每一位
    for (int i = bits - 1; i >= 0; i--)
    {
        // 检查当前位是否为 1
        if (num & (1 << i))
        {
            printf("1"); // 如果当前位是 1，则打印 1
        }
        else
        {
            printf("0"); // 如果当前位是 0，则打印 0
        }
    }
    printf("\n"); // 打印换行符，以便在不同的位之间分隔
}

int main()
{
    int a = 0b011;
    printBits(a); // 00000000000000000000000000000011
    // 按位取反：～
    printBits(~a); // 11111111111111111111111111111100
    // 按位与: &
    printBits(0b10001 & 0b10010); // 00000000000000000000000000010000
    // 按位或: |
    printBits(0b10001 | 0b10010); // 00000000000000000000000000010011
    // 按位异或: ^
    printBits(0b10001 ^ 0b10010); // 00000000000000000000000000000011
}

```

移位：左右

```c
#include <stdio.h>

void printBits(int num)
{
    // 获取整数的位数
    int bits = sizeof(num) * 8; // sizeof(num) 返回整数的大小（以字节为单位），乘以 8 得到位数

    // 遍历整数的每一位
    for (int i = bits - 1; i >= 0; i--)
    {
        // 检查当前位是否为 1
        if (num & (1 << i))
        {
            printf("1"); // 如果当前位是 1，则打印 1
        }
        else
        {
            printf("0"); // 如果当前位是 0，则打印 0
        }
    }
    printf("\n"); // 打印换行符，以便在不同的位之间分隔
}

int main()
{
    int positive = 3;
    int negtiave = -3;
    printBits(positive);
    printBits(positive << 1);
    printBits(positive << 2);
    printBits(positive << 3);
    printBits(positive >> 1);
    printBits(positive >> 2);
    printBits(positive >> 3);
    // 00000000000000000000000000000011
    // 00000000000000000000000000000110
    // 00000000000000000000000000001100
    // 00000000000000000000000000011000
    // 00000000000000000000000000000001
    // 00000000000000000000000000000000
    // 00000000000000000000000000000000

    printBits(negtiave);
    printBits(negtiave << 1);
    printBits(negtiave << 2);
    printBits(negtiave << 3);
    printBits(negtiave >> 1);
    printBits(negtiave >> 2);
    printBits(negtiave >> 3);
    // 11111111111111111111111111111101
    // 11111111111111111111111111111010
    // 11111111111111111111111111110100
    // 11111111111111111111111111101000
    // 11111111111111111111111111111110
    // 11111111111111111111111111111111
    // 11111111111111111111111111111111
}
```


## 位字段

```c
/* dualview.c -- bit fields and bitwise operators */
#include <stdio.h>
#include <stdbool.h>
#include <limits.h>
/* BIT-FIELD CONSTANTS */
/* line styles     */
#define SOLID 0
#define DOTTED 1
#define DASHED 2
/* primary colors  */
#define BLUE 4
#define GREEN 2
#define RED 1
/* mixed colors    */
#define BLACK 0
#define YELLOW (RED | GREEN)
#define MAGENTA (RED | BLUE)
#define CYAN (GREEN | BLUE)
#define WHITE (RED | GREEN | BLUE)

/* BITWISE CONSTANTS   */
#define OPAQUE 0x1
#define FILL_BLUE 0x8
#define FILL_GREEN 0x4
#define FILL_RED 0x2
#define FILL_MASK 0xE
#define BORDER 0x100
#define BORDER_BLUE 0x800
#define BORDER_GREEN 0x400
#define BORDER_RED 0x200
#define BORDER_MASK 0xE00
#define B_SOLID 0
#define B_DOTTED 0x1000
#define B_DASHED 0x2000
#define STYLE_MASK 0x3000

const char *colors[8] = {"black", "red", "green", "yellow",
                         "blue", "magenta", "cyan", "white"};
struct box_props
{
    bool opaque : 1;
    unsigned int fill_color : 3;
    unsigned int : 4;
    bool show_border : 1;
    unsigned int border_color : 3;
    unsigned int border_style : 2;
    unsigned int : 2;
};

union Views /* look at data as struct or as unsigned short */
{
    struct box_props st_view;
    unsigned short us_view;
};

void show_settings(const struct box_props *pb);
void show_settings1(unsigned short);
char *itobs(int n, char *ps);

int main(void)
{
    /* create Views object, initialize struct box view */
    union Views box = {{true, YELLOW, true, GREEN, DASHED}};
    char bin_str[8 * sizeof(unsigned int) + 1];

    printf("Original box settings:\n");
    show_settings(&box.st_view);
    printf("\nBox settings using unsigned int view:\n");
    show_settings1(box.us_view);

    printf("bits are %s\n",
           itobs(box.us_view, bin_str));
    box.us_view &= ~FILL_MASK;               /* clear fill bits */
    box.us_view |= (FILL_BLUE | FILL_GREEN); /* reset fill */
    box.us_view ^= OPAQUE;                   /* toggle opacity */
    box.us_view |= BORDER_RED;               /* wrong approach */
    box.us_view &= ~STYLE_MASK;              /* clear style bits */
    box.us_view |= B_DOTTED;                 /* set style to dotted */
    printf("\nModified box settings:\n");
    show_settings(&box.st_view);
    printf("\nBox settings using unsigned int view:\n");
    show_settings1(box.us_view);
    printf("bits are %s\n",
           itobs(box.us_view, bin_str));

    return 0;
}

void show_settings(const struct box_props *pb)
{
    printf("Box is %s.\n",
           pb->opaque == true ? "opaque" : "transparent");
    printf("The fill color is %s.\n", colors[pb->fill_color]);
    printf("Border %s.\n",
           pb->show_border == true ? "shown" : "not shown");
    printf("The border color is %s.\n", colors[pb->border_color]);
    printf("The border style is ");
    switch (pb->border_style)
    {
    case SOLID:
        printf("solid.\n");
        break;
    case DOTTED:
        printf("dotted.\n");
        break;
    case DASHED:
        printf("dashed.\n");
        break;
    default:
        printf("unknown type.\n");
    }
}

void show_settings1(unsigned short us)
{
    printf("box is %s.\n",
           (us & OPAQUE) == OPAQUE ? "opaque" : "transparent");
    printf("The fill color is %s.\n",
           colors[(us >> 1) & 07]);
    printf("Border %s.\n",
           (us & BORDER) == BORDER ? "shown" : "not shown");
    printf("The border style is ");
    switch (us & STYLE_MASK)
    {
    case B_SOLID:
        printf("solid.\n");
        break;
    case B_DOTTED:
        printf("dotted.\n");
        break;
    case B_DASHED:
        printf("dashed.\n");
        break;
    default:
        printf("unknown type.\n");
    }
    printf("The border color is %s.\n",
           colors[(us >> 9) & 07]);
}

char *itobs(int n, char *ps)
{
    int i;
    const static int size = CHAR_BIT * sizeof(int);

    for (i = size - 1; i >= 0; i--, n >>= 1)
        ps[i] = (01 & n) + '0';
    ps[size] = '\0';

    return ps;
}

// (base) kimshan@MacBook-Pro output % ./"dualview"
// Original box settings:
// Box is opaque.
// The fill color is yellow.
// Border shown.
// The border color is green.
// The border style is dashed.

// Box settings using unsigned int view:
// box is opaque.
// The fill color is yellow.
// Border shown.
// The border style is dashed.
// The border color is green.
// bits are 00000000000000000010010100000111

// Modified box settings:
// Box is transparent.
// The fill color is cyan.
// Border shown.
// The border color is yellow.
// The border style is dotted.

// Box settings using unsigned int view:
// box is transparent.
// The fill color is cyan.
// Border shown.
// The border style is dotted.
// The border color is yellow.
// bits are 00000000000000000001011100001100
```
