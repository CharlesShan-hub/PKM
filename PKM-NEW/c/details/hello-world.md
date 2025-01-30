# Hello World
1. Hello World 程序
	```c
	// first.c
	#include <stdio.h>
	int main(void)           /* a simple program             */
	{
	    int num;             /* define a variable called num */
	    num = 1;             /* assign a value to num        */
	    
	    printf("I am a simple ");/* use the printf() function*/
	    printf("computer.\n");
	    printf("My favorite number is %d because it is first.\n",num);
	    
	    return 0;
	}
	```

1. 编译（在类Unix系统中，我们使用 `cc`）
	* 如果直接执行 `cc first.c` 会生成 `a.out`
	* 指定输出文件的名字要用 `-o`，比如 `cc -o first first.c`，会得到科执行文件 `first`
	* [[../details/cc|👉 cc命令简介]]
2. `int main(void)`是标准形式，如果写`main()`或者`void main()`，也可以成功编译。
3. C99和C11允许使用更长的标识符名，但是编译器只识别前63个字符。对于外部标识符（参阅C primer plus第12章），只允许使用31个字符。

