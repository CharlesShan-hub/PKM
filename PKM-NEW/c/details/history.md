# History of C

## Small Talks
* **Before C**
	* （1954-`Fortran`）Fortran（FormulaTranslation）是世界上第一个计算机高级语言，由约翰·巴克斯开发。在巴科斯大学将近毕业的时候，他参观了IBM计算机中心，看到当时的一台可选循序电子计算机(SSEC)，程序员们在编写程序上也是十分的艰难。在巴科斯开发了Speedcoding利用浮点数来支持运算的程序后，在1951年他跟他的团队开始针对汇编语言的缺点着手研究开发FORTRAN语言，最终在1954年正式对外发布。
	* （1958-`ALGOL`）计算机硬件的快速发展，比如著名的单个体系结构计算机UNIVAC计算机、IBM700系列计算机等，大量的新增计算机语言也围绕着这些计算机开始涌现，但此时的计算机语言都是专用于某一型号计算机的语言，不同计算机系统之间是无法交流。为了开发一种与计算机无关的科学用程序设计语言，德国的应用数学和力学学会(Gesellschaft für Angewandte Mathematik und Mechanik,GAMM)和国际计算机学会(Association for Computing Machinery，ACM)各有4人出席在苏黎世举行第一次设计会议，为新语言定下目标。亦因应语言特性，先被命名为国际代数语言(International Algebraic Language，IAL) ，转辗后定名为ALGOL（Algorithmic Language），即算法语言。
	* （1963-`CPL`）CPL（Combined Programming Language）是基于 ALGOL 60 的高级语言，由剑桥大学推出。CPL（Combined Programming Language）是一种混合编程语言，用于嵌入式系统和科学计算领域。它结合了高级语言和汇编语言的特点，既具备高级语言的易用性和可读性，又能充分发挥汇编语言的灵活性和效率。CPL被认为是ALGOL 60的一个子集，与ALGOL相比，CPL增加了一些新的特性和更丰富的数据类型。
	* （1967-`BCPL`）CPL语言在 ALGOL 60 的基础上接近硬件一些，但规模比较大，难以实现。英国剑桥大学的 Matin Richards 对 CPL 语言做了简化，推出了 BCPL （the Basic Combined Programming Language）语言。
	* （1970-`B`）美国贝尔实验室的 Ken Thompson 以 BCPL 语言为基础，又作了进一步的简化，设计出了很简单的而且很接近硬件的 B 语言（取BCPL的第一个字母），并用B语言写出了第一个 UNIX 操作系统。但 B 语言过于简单，功能有限。B可被视为没有类型的C。
* **Early C**
	* （1971-`NB`）为了让 B 从 PDP-7 移植到 PDP-11，开发了NB（New B），这次支持了类型比如 int、char、array、pointer等等。
	* （1972-`C`）语言重新命名成C。并增加了struct、`&&`与`||`运算符、预处理器和便携式IO。
	* （1973）用 C 重写 Unix。
	* （1978）The C Programming Language, 1st edition（俗称K&R）
* **Standard C**
	* （1983）ANSI成立 X3J11 委员会。
	* （1988）The C Programming Language, 2st edition。
	* （1989-C89）即 ANSI C，C语言的第一个官方标准。增加了volatile、enum、signed、void、locales，从 C++ 借鉴了 const 和 function prototypes。
	* （1999-C99）C99 引入了许多新特性，如变长数组、布尔类型、复合字面量、长长整型、新的整数类型、自定义字符串处理函数、对齐约束、更好的浮点数处理、原子操作等。
	* （2011-C11）C11 引入了更现代的特性，如静态断言、自动类型推导、右值引用、原子类型、threads和原子操作库、泛型编程支持、基于范围的for循环、改进的字符串处理等。

![[../assets/languages.png]]

## Reference
1. BCPL、B、C：https://www.cnblogs.com/ningskyer/articles/7286932.html
2. 官方C语言历史：https://en.cppreference.com/w/c/language/history
3. https://comp-think.github.io/