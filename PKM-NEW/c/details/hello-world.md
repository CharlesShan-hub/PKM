# Hello World

1. Hello World 程序
	```c
	// first.c
	#include <stdio.h>
	int main(void)          /* a simple program             */
	{
		int num;             /* define a variable called num */
		num = 1;             /* assign a value to num        */
		
		printf("I am a simple ");/* use the printf() function*/
		printf("computer.\n");
		printf("My favorite number is %d because it is first.\n",num);
		
		return 0;
	}
	```
2. 流程
	![c-workflows-drawing|1000](../assets/c-workflows-drawing.md)
3. 编译（在类Unix系统中，我们使用 `cc`）
	* 如果直接执行 `cc first.c` 会生成 `a.out`
	* 指定输出文件的名字要用 `-o`，比如 `cc -o first first.c`，会得到科执行文件 `first`
	* 👉 [cc命令简介](cc.md)
4. `int main(void)`是标准形式，如果写`main()`或者`void main()`，也可以成功编译但不推荐。
5. 关键字（keyword）：C 语言保留的不能做其他用途的词，比如`int`。
6. 标识符（identifier）：一个变量、函数或其他实体的名称，比如`int num`的`num`。标识符的组成是小写字母、大写字母、数字和下划线，并且第1个字符必须是字符或下划线，不能是数字。
7. 库标识符：操作系统和C库经常使用以一个或两个下划线字符开始的标识符（如，`_kcab`）。
8. C99和C11允许使用更长的标识符名，但是编译器只识别前63个字符。对于外部标识符（参阅C primer plus第12章），只允许使用31个字符。

