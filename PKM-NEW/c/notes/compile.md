
# Compile

## 编译多个 c 文件

gcc file1.c file2.c

```c
/* hotel.h -- constants and declarations for hotel.c */
#define QUIT       5
#define HOTEL1   180.00
#define HOTEL2   225.00
#define HOTEL3   255.00
#define HOTEL4   355.00
#define DISCOUNT   0.95
#define STARS "**********************************"

// shows list of choices
int menu(void);

// returns number of nights desired
int getnights(void);

// calculates price from rate, nights
// and displays result
void showprice(double rate, int nights);

```

```c
/* hotel.c -- hotel management functions */
#include <stdio.h>
#include "hotel.h"
int menu(void)
{
    int code, status;
    
    printf("\n%s%s\n", STARS, STARS);
    printf("Enter the number of the desired hotel:\n");
    printf("1) Fairfield Arms           2) Hotel Olympic\n");
    printf("3) Chertworthy Plaza        4) The Stockton\n");
    printf("5) quit\n");
    printf("%s%s\n", STARS, STARS);
    while ((status = scanf("%d", &code)) != 1  ||
           (code < 1 || code > 5))
    {
        if (status != 1)
            scanf("%*s");   // dispose of non-integer input
        printf("Enter an integer from 1 to 5, please.\n");
    }
    
    return code;
}

int getnights(void)
{
    int nights;
    
    printf("How many nights are needed? ");
    while (scanf("%d", &nights) != 1)
    {
        scanf("%*s");       // dispose of non-integer input
        printf("Please enter an integer, such as 2.\n");
    }
    
    return nights;
}

void showprice(double rate, int nights)
{
    int n;
    double total = 0.0;
    double factor = 1.0;
    
    for (n = 1; n <= nights; n++, factor *= DISCOUNT)
        total += rate * factor;
    printf("The total cost will be $%0.2f.\n", total);
}

```

```c
/* usehotel.c -- room rate program */
/* compile with  Listing 9.10      */
#include <stdio.h>
#include "hotel.h" /* defines constants, declares functions */

int main(void)
{
    int nights;
    double hotel_rate;
    int code;
    
    while ((code = menu()) != QUIT)
    {
        switch(code)
        {
            case 1 : hotel_rate = HOTEL1;
                break;
            case 2 : hotel_rate = HOTEL2;
                break;
            case 3 : hotel_rate = HOTEL3;
                break;
            case 4 : hotel_rate = HOTEL4;
                break;
            default: hotel_rate = 0.0;
                printf("Oops!\n");
                break;
        }
        nights = getnights();
        showprice(hotel_rate, nights);
    }
    printf("Thank you and goodbye.\n");
    
    return 0;
}

```

```
(base) kimshan@MacBook-Pro Ch09 % gcc usehotel.c hotel.c
(base) kimshan@MacBook-Pro Ch09 % ./a.out 

********************************************************************
Enter the number of the desired hotel:
1) Fairfield Arms           2) Hotel Olympic
3) Chertworthy Plaza        4) The Stockton
5) quit
********************************************************************
1
How many nights are needed? 2
The total cost will be $351.00.

********************************************************************
Enter the number of the desired hotel:
1) Fairfield Arms           2) Hotel Olympic
3) Chertworthy Plaza        4) The Stockton
5) quit
********************************************************************
2
How many nights are needed? 2
The total cost will be $438.75.

********************************************************************
Enter the number of the desired hotel:
1) Fairfield Arms           2) Hotel Olympic
3) Chertworthy Plaza        4) The Stockton
5) quit
********************************************************************
3
How many nights are needed? 1
The total cost will be $255.00.

********************************************************************
Enter the number of the desired hotel:
1) Fairfield Arms           2) Hotel Olympic
3) Chertworthy Plaza        4) The Stockton
5) quit
********************************************************************
4
How many nights are needed? 1
The total cost will be $355.00.

********************************************************************
Enter the number of the desired hotel:
1) Fairfield Arms           2) Hotel Olympic
3) Chertworthy Plaza        4) The Stockton
5) quit
********************************************************************
5
Thank you and goodbye.
```


## 命令行参数

```c
/* repeat.c -- main() with arguments */
#include <stdio.h>
int main(int argc, char *argv[])
{
    int count;

    printf("The command line has %d arguments:\n", argc - 1);
    for (count = 1; count < argc; count++)
        printf("%d: %s\n", count, argv[count]);
    printf("\n");

    return 0;
}
```

```shell
(base) kimshan@MacBook-Pro output % ./"repeat" a b c
The command line has 3 arguments:
1: a
2: b
3: c
```
