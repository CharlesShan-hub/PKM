# C\#

## 基础语法

### Hello World

* 自动换行`Console.WriteLine("Hello World");`
* 不换行`Console.Write("Hello World");`

### 变量

* `int age = 10;`
* `double height = 180.3;`
* `char sex = 'f';`
* `string name = "Charles";`

### ASCII

* A是65，a是97

* 转义字符

  ```C#
  Console.WriteLine("c:\\a\\b\\c");
  //print:c:\a\b\c
  Console.WriteLine(@"c:\a\b\c"); // @可以让转义字符失效
  //print:c:\a\b\c
  Console.WriteLine(@"a
  b");
  //print:a
  //b
  Console.WriteLine(@"a""
  b");
  //print:a"
  //b
  ```

### 类型转换

* ```C#
  char a = 'a';
  int b = a; // 可以
  ```

* ```c#
  int a = 97;
  char b = a; // 不可以
  ```

* ```C#
  int a = 97;
  char b = (char)a; // 可以
  ```

### 输入

* 输入`String str = Console.ReadLine();`

* 输入一个整数

  ```C#
  String str = Console.ReadLine();
  int strInt = Convert.ToInt32(str);
  Console.WriteLine(strInt);
  ```

### 格式化输出

* ```C#
  int a = 1, b = 2;
  Console.WriteLine(a + "+" + b + "=" (a+b));
  Console.WriteLine("{0}+{1}={2}",a,b,a+b);
  ```

### 数组

* `int[] num = {1,2,3,4,5};`
* `int[] num = new int[10];`
* `int[] num = new int[] {1,2,3,4,5};`
* `Console.WriteLine(num.Length);`
* `foreach(int item in list){ ... }`

### 字符串

* ```C#
  string str = "Hello World";
  str.ToLower(); // 换成小写
  str.ToUpper(); // 换成大写
  str.Trim();    // 去除空格
  str.TrimStart();//去除前面的空格
  str.TrimEnd(); // 去除后边的空格
  str.split(",");// 根据某内容做切割
  ```

### 枚举

```C#
enum Day
{
  Mon, Teu, Wen, Thu, Fri, Sat, Sun
};

Day day = Day.Mon;
```

### 结构体函数

```C#
struct Position
{
  public double x;
  public double y;
  public double z;
  public void PrintPosition()
  {
		Console.WriteLine(x+","+y+","+z);
  }
}

static void main(string[] str)
{
  Position p;
  p.x = 1;
  p.y = 2;
  p.z = 3;
  p.PrintPosition()
}
```

### 委托

```C#
using System;

namespace _048_委托
{
    class Program
    {

        static double Multiply(double param1,double param2)//函数体
        {
            return param1 * param2;
        }

        static double Divide(double param1,double param2)
        {
            return param1 / param2;
        }

        static void Test()
        {
            Console.WriteLine("Test");
        }

        delegate double MyDelegate(double param1, double param2);

        delegate void MyDelegate2();

        static void Main(string[] args)
        {
            //Console.WriteLine(Multiply(2.3, 2));
            //Console.WriteLine(Divide(4.5, 3));

            MyDelegate delegate1;
            MyDelegate2 delegate2;

            delegate1 = Multiply;
            delegate1 = Divide;

            //delegate1 = Test;
            delegate2 = Test;

            Console.WriteLine(delegate1(2, 4));
            delegate2();
        }
    }
}

```







