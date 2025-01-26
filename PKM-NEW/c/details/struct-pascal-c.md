struct in Pascal

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
#include <stdio.h>
#include <string.h>
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
    struct book library; /* declare library as a book variable  */
    
    printf("Please enter the book title.\n");
    s_gets(library.title, MAXTITL); /* access to the title portion         */
    printf("Now enter the author.\n");
    s_gets(library.author, MAXAUTL);
    printf("Now enter the value.\n");
    scanf("%f", &library.value);
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
