
有这样一个需求：请用你当前所学知识，分别计算 100 和 111、222、666、888、999 的和，你该怎么编写代码？

```java
System.out.println(100 + 111);
System.out.println(100 + 222);
System.out.println(100 + 666);
System.out.println(100 + 888);
System.out.println(100 + 999);
```

现在需求变化了，要求计算 234 和 111、222、666、888、999 的和，你需要将以上代码中所有的 100 全部进行修改：

```java
System.out.println(234 + 111);
System.out.println(234 + 222);
System.out.println(234 + 666);
System.out.println(234 + 888);
System.out.println(234 + 999);
```

修改了 5 个位置，如果求和的数据更多，那么修改的位置也会更多，显然：可维护性太差。怎么解决？使用变量可以解决。

```java
int num = 100;
System.out.println(num + 111);
System.out.println(num + 222);
System.out.println(num + 666);
System.out.println(num + 888);
System.out.println(num + 999);
```

如果需求变化了，只需要修改一个位置即可：

```java
int num = 234;
System.out.println(num + 111);
System.out.println(num + 222);
System.out.println(num + 666);
System.out.println(num + 888);
System.out.println(num + 999);
```

再比如，又有这样一个需求：现在有三个圆，半径分别是 10cm，20cm，30cm，π 取值 3.14，请分别计算他们的面积，如果不使用变量，程序是这样的：

```java
System.out.println(3.14 * 10 * 10); // 314
System.out.println(3.14 * 20 * 20); // 1256
System.out.println(3.14 * 30 * 30); // 2826
```

上面程序存在的最大问题就是：可读性太差。使用变量可以提高程序的可读性：

```java
double π = 3.14;
int r1 = 10;
int r2 = 20;
int r3 = 30;
System.out.println(π * r1 * r1);
System.out.println(π * r2 * r2);
System.out.println(π * r3 * r3);
```
