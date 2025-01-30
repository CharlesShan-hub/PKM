# History of C

## Overview

1972年，贝尔实验室的丹尼斯·里奇（Dennis Ritch）和肯·汤普逊（Ken Thompson）在开发UNIX操作系统时设计了C语言。然而，C语言不完全是里奇突发奇想而来，他是在B语言（汤普逊发明）的基础上进行设计。至于B语言的起源，那是另一个故事。C语言设计的初衷是将其作为程序员使用的一种编程工具，因此，其主要目标是成为有用的语言。

虽然绝大多数语言都以实用为目标，但是通常也会考虑其他方面。例如，Pascal的主要目标是为更好地学习编程原理提供扎实的基础；而BASIC的主要目标是开发出类似英文的语言，让不熟悉计算机的学生轻松学习编程。这些目标固然很重要，但是随着计算机的迅猛发展，它们已经不是主流语言。然而，最初为程序员设计开发的C语言，现在已成为首选的编程语言之一。

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
	* （1978）The C Programming Language, 1st edition（俗称K&R）。C语言发展之初，并没有所谓的C标准。1987年，布莱恩·柯林汉（Brian Kernighan）和丹尼斯·里奇（Dennis Ritchie）合著的The C Programming Language（《C语言程序设计》）第1版是公认的C标准，通常称之为K&R C或经典C。特别是，该书中的附录中的“C语言参考手册”已成为实现C的指导标准。例如，编译器都声称提供完整的K&R实现。虽然这本书中的附录定义了C语言，但却没有定义C库。与大多数语言不同的是，C语言比其他语言更依赖库，因此需要一个标准库。实际上，由于缺乏官方标准，UNIX实现提供的库已成为了标准库。
* **Standard C**
	* （1983）美国国家标准协会（ANSI）成立 X3J11 委员会。
	* （1988）The C Programming Language, 2st edition。
	* （1989-C89）即 ANSI C，C语言的第一个官方标准。增加了volatile、enum、signed、void、locales，从 C++ 借鉴了 const 和 function prototypes。该标准（ANSI C）定义了C语言和C标准库。国际标准化组织于1990年采用了这套C标准（ISO C）。ISO C和ANSI C是完全相同的标准。ANSI/ISO标准的最终版本通常叫作C89（因为ANSI于1989年批准该标准）或C90（因为ISO于1990年批准该标准）。另外，由于ANSI先公布C标准，因此业界人士通常使用ANSI C。
	* （1999-C99）C99 引入了许多新特性，如变长数组、布尔类型、复合字面量、长长整型、新的整数类型、自定义字符串处理函数、对齐约束、更好的浮点数处理、原子操作等。ANSI/ISO联合委员会（C9X委员会）遵循了最初C90标准的原则，包括保持语言的精练简单。委员会的用意不是在C语言中添加新特性，而是为了达到新的目标。第1个目标是，支持国际化编程。例如，提供多种方法处理国际字符集。第2个目标是，“调整现有实践致力于解决明显的缺陷”。因此，在遇到需要将C移至64位处理器时，委员会根据现实生活中处理问题的经验来添加标准。第3个目标是，为适应科学和工程项目中的关键数值计算，提高C的适应性，让C比FORTRAN更有竞争力。这3点（国际化、弥补缺陷和提高计算的实用性）是主要的修订目标。在其他方面的改变则更为保守，例如，尽量与C90、C++兼容，让语言在概念上保持简单。用委员会的话说：“...委员会很满意让C++成为大型、功能强大的语言”。
	* （2011-C11）C11 引入了更现代的特性，如静态断言、自动类型推导、右值引用、原子类型、threads和原子操作库、泛型编程支持、基于范围的for循环、改进的字符串处理等。

![[../assets/languages.png]]

## Reference
1. BCPL、B、C：https://www.cnblogs.com/ningskyer/articles/7286932.html
2. 官方C语言历史：https://en.cppreference.com/w/c/language/history
3. https://comp-think.github.io/