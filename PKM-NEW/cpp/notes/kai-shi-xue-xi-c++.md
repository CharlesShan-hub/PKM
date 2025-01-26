# 开始学习 C++

第2章 开始学习C++:本章介绍创建简单C++程序的步骤。您可以学习到main( )函数扮演的角色以及C++程序使用的一些语句。您将使用预定义的cout和cin对象来实现程序输出和输入，学习如何创建和使用变量。最后，本章还将介绍函数——C++的编程模块。

### 2.1 进入 C++

```cpp
/* displays a message
 */

#include <iostream>                           // a PREPROCESSOR directive

int main() {                                 // function header
    // start of function body
    using namespace std;                      // make definitions visible
    cout << "Hello world!" << endl;           // message

    cout << "Comme up and C++ me some time."
         << endl;
    cout << "You won't regret it! " << endl;

    // If the output window closes before you can read it,
    // add the following code:
    cout << "Press any key to continue." << endl;
    cin.get();
    return 0;                                 // terminate main()
}                                             // end of function body
```

> int main，注释，isotream，头文件名(.h？)，命名空间，代码风格（标记与空白）

1. &#x20;C++ 的 using namespace 和 python 的 import 好像。
2. cout 的箭头是向左的，cin 的箭头是向右的。想象着语句左边是 io 的一个“洞口”，箭头代表数据流来回流动的方向。
3. endl 换行符要比\n快，可能 C 语言里边那个“行缓冲”。

***

### 2.2 C++语句

> 声明，赋值，cout

为什么需要声明语句？因为 BASIC 和 Python 使用新名称就会创建新变量，C++认为如果人写错了，很难检查出来自己不知道什么时候建了个新变量。

为什么 cout 而不是 printf？因为 cout 是 OOP 的，利用对象的方法可以得到 string，C 的话里边的%d,%c等等容易混淆。

***

### 2.3 其他 C++语句

> cout多行，cout 其实是对象

***

### 2.4 函数

> 返回值，库函数，函数的定义与调用

* 使用库函数（比如 math.h）：`#include<cmath>`
* 用户定义的函数（和 C 一样）

<details>

<summary>注意，没必要让某个函数接触太多内容，别在全局引入一堆库</summary>

```cpp
// ourfunc.cpp -- defining your own function
#include <iostream>
void simon(int);    // function prototype for simon()
// using namespace std; // don't do this

int main()
{
    using namespace std; // import here
    simon(3);       // call the simon() function
    cout << "Pick an integer: ";
    int count;
    cin >> count;
    simon(count);   // call it again
    cout << "Done!" << endl;
	// cin.get();
    // cin.get();
    return 0;
}

void simon(int n)   // define the simon() function
{
    using namespace std;

    cout << "Simon says touch your toes " << n << " times." << endl;
}                   // void functions don't need return statements

```

</details>





























