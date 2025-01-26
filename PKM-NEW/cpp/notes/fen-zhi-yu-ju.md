
# 分支语句

第6章 分支语句和逻辑运算符:如果程序可以根据实际情况调整执行，我们就说程序能够智能地行动。在本章，您将了解到如何使用 if、if else和switch语句及条件运算符来控制程序流程，学习如何使用逻辑运算符来表达决策测试。另外，本章还将介绍确定字符关系 (如测试字符是数字还是非打印字符)的函数库cctype。最后，还将简要地介绍文件输入/输出。

## 6.1 if

```cpp
// if
if(condition)
    statement
    
// if else
if(condition)
    statement1
else
    statement2
    
// if else if else
if(condition)
    statement1
else if 
    statement2
...
else
    statementn
```

***

## 6.2 逻辑表达式

* 逻辑 `OR (||)`、逻辑 `AND (&&)`和逻辑 `NOT (!)`
* 标识符`and`、`or`和`not`都是C++保留字，可以直接使用，C 需要加入[[../../c/library/iso646|iso646]]

***

## 6. 3 字符函数库 cctype

* [[../../c/library/ctypes|ctypes]]

***

## 6.4 ?:运算符

```c
int c = a > b ? a : b;
// c = a if a > b, else c = b
```

***

## 6.5 switch

<details>

<summary>enum + switch</summary>

```cpp
// enum.cpp -- using enum
#include <iostream>
// create named constants for 0 - 6
enum {red, orange, yellow, green, blue, violet, indigo};

int main()
{
    using namespace std;
    cout << "Enter color code (0-6): ";
    int code;
    cin >> code;
    while (code >= red && code <= indigo)
    {
        switch (code)
        {
            case red     : cout << "Her lips were red.\n"; break;
            case orange  : cout << "Her hair was orange.\n"; break;
            case yellow  : cout << "Her shoes were yellow.\n"; break;
            case green   : cout << "Her nails were green.\n"; break;
            case blue    : cout << "Her sweatsuit was blue.\n"; break;
            case violet  : cout << "Her eyes were violet.\n"; break;
            case indigo  : cout << "Her mood was indigo.\n"; break;
        }
        cout << "Enter color code (0-6): ";
        cin >> code;
    }
    cout << "Bye\n";
    // cin.get();
    // cin.get();
    return 0; 
}

```

```
(base) kimshan@MacBook-Pro output % ./"enum"
Enter color code (0-6): 2
Her shoes were yellow.
Enter color code (0-6): 5
Her eyes were violet.
Enter color code (0-6): 7
Bye
```

</details>

***

## 6.6 break, continue

和 C 一样，只能破一层。不能指定层。

***

## 6.7 读取数字的循环

<details>

<summary>Demo</summary>

```cpp
// cingolf.cpp -- non-numeric input skipped
#include <iostream>
const int Max = 5;
int main()
{
    using namespace std;
// get data
    int golf[Max];
    cout << "Please enter your golf scores.\n";
    cout << "You must enter " << Max << " rounds.\n";
    int i;
    for (i = 0; i < Max; i++)
    {
        cout << "round #" << i+1 << ": ";
        while (!(cin >> golf[i])) {
            cin.clear();     // reset input
            while (cin.get() != '\n')
                continue;    // get rid of bad input
            cout << "Please enter a number: ";
        }
    }
// calculate average
    double total = 0.0;
    for (i = 0; i < Max; i++)
        total += golf[i];
// report results
    cout << total / Max << " = average score "
            << Max << " rounds\n";
    // cin.get();
    // cin.get();
    return 0; 
}
```

```
(base) kimshan@MacBook-Pro output % ./"cingolf"
Please enter your golf scores.
You must enter 5 rounds.
round #1: 90
round #2: 98
round #3: 91
round #4: 97
round #5: 95
94.2 = average score 5 rounds
```

</details>

***

## 6.8 简单文件输入/输出

<details>

<summary>读文件并做错误处理的 Demo</summary>

```cpp
// sumafile.cpp -- functions with an array argument
#include <iostream>
#include <fstream>          // file I/O support
#include <cstdlib>          // support for exit()
const int SIZE = 60;
int main()
{
    using namespace std;
    char filename[SIZE];
    ifstream inFile;        // object for handling file input

    cout << "Enter name of data file: ";
    cin.getline(filename, SIZE);
    inFile.open(filename);  // associate inFile with a file
    if (!inFile.is_open())  // failed to open file
    {
        cout << "Could not open the file " << filename << endl;
        cout << "Program terminating.\n";
        // cin.get();    // keep window open
        exit(EXIT_FAILURE);
    }
    double value;
    double sum = 0.0;
    int count = 0;          // number of items read

    inFile >> value;        // get first value
    while (inFile.good())   // while input good and not at EOF
    {
        ++count;            // one more item read
        sum += value;       // calculate running total
        inFile >> value;    // get next value
    }
    if (inFile.eof())
        cout << "End of file reached.\n";
    else if (inFile.fail())
        cout << "Input terminated by data mismatch.\n";
    else
        cout << "Input terminated for unknown reason.\n";
    if (count == 0)
        cout << "No data processed.\n";
    else
    {
        cout << "Items read: " << count << endl;
        cout << "Sum: " << sum << endl;
        cout << "Average: " << sum / count << endl;
    }
    inFile.close();         // finished with the file
    // cin.get();
    return 0;
}

```

</details>
