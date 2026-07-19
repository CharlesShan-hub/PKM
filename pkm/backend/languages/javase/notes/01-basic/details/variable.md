# 变量

## 变量三要素

变量可以看做是一个盒子，这个盒子可以存储数据。本质上，变量是内存当中的一块空间，这块空间有三要素（变量的三要素）：

- 要素一：**数据类型**（决定了空间大小）。例如有一种数据类型叫做整数型：int
- 要素二：**名字**（只要是合法的**标识符**就行）。例如：age（年龄）
- 要素三：**值**（盒子中具体存储的**数据**，需要和数据类型对应）。例如：20

![java-basic-var](../assets/java-basic-var.svg)
(详细介绍（可跳过）：[var-detail1](var-detail1.md))

## 变量的作用

* 变量的存在，可以让程序更加易维护
* 因此变量的出现可以提高程序的可读性
* (详细介绍（可跳过）：[var-detail2](var-detail2.md))

## 变量的声明

语法如下：

```java
数据类型 变量名;
```

例如：

```java
int age;
String name;
double π;
```

数据类型后面详细讲。

变量名只要是合法的标识符即可。规范中要求：变量名首字母小写，后面每个单词首字母大写。

## 变量的赋值

使用赋值运算符“=”完成赋值，例如：

```java
age = 20;
name = "jack";
π = 3.14;
```

注意：等号运算符叫做赋值运算符，“=”右边表达式优先级高，先执行右边，将执行结果赋值给左边的变量。

变量中的“变”是因为变量赋值后可以重新赋值：

```java
age = 30;
name = "lucy";
```

需要注意的是：变量虽然可以重新赋值，但在赋值的时候，值的数据类型一定要和变量的数据类型一致，不能这样：

```java
age = "张三";
```

另外，变量的声明和赋值也是可以在一行代码中完成的，例如：在声明的时候直接赋值：

```java
int num = 200;
```

## 变量的访问

变量的访问不外乎包括两种情况：

- 读取
- 修改

读取变量的值：

```java
int age = 20;
System.out.println(age);
```

修改变量的值：

```java
age = 30;
```

将变量的值读取出来，**复制一份**传递给另一个变量：

```java
int num1 = 10;
int num2 = num1;
int num3 = num1 + num2;
```

## 变量的小细节

1. 变量必须先声明，再赋值，才能访问。

```java
int age;
System.out.println(age); // 报错，原因是变量 age 没有赋值
```

2. 方法体当中的代码遵循自上而下的顺序依次逐行执行，变量先访问，再声明肯定是不行的。

```java
System.out.println(num);
int num = 20;
```

3. 一行代码上可以同时声明多个变量。

```java
int a, b, c = 300; // 表示声明三个 int 类型变量，分别起名 a b c，但是 a 和 b 没有赋值，c 赋值 300
```

4. 在同一个作用域当中，变量名不能重名，可以重新赋值。

```java
public static void main(String[] args){
    int a = 100;
    // 重新赋值没问题
    a = 200;
    a = 300;
    // 重复声明肯定不行
    int a = 900; // 报错
}
```

## 变量的作用域

### 什么是变量作用域

作用域就是变量的有效范围。变量的作用域是怎样的呢？用一句大白话就可以概括了：**出了大括号就不认识了**。

```java
public class MyClass {
    static int e = 100;

    public static void main(String[] args){
        int i = 100;
        System.out.println(i);

        for(int k = 0; k < 10; i++){
            int f = 100;
        }

        // 这里是无法访问 f 变量的
        System.out.println(f);

        // 这里是可以访问 e 的
        System.out.println(e);
    }

    public static void m(){
        // 这里无法访问 main 方法中的 i
        System.out.println(i);
    }
}
```

作用域的不同主要是因为声明在不同位置的变量具有不同的生命周期。所谓的生命周期是：从内存开辟到内存释放。

### Java 的就近原则

```java
public class MyClass {
    static int num = 10;

    public static void main(String[] args){
        int num = 200;
        // 输出结果是 200，这就是就近原则。
        System.out.println(num);
    }
}
```

### Java不支持变量遮蔽（与C、Rust不同）

```java
public class Main {
    public static void main(String[] args) {
        int a = 1;
        {
            // 错误：不能像C语言一样遮蔽变量
            // double a = 1; 
        }
    }
}
```

## 变量的分类

Java 中的变量可以按照作用域的不同划分为以下几类：

1. 局部变量：定义在方法、语句块、形式参数中的变量。
2. 成员变量：定义在类中，但在方法之外的变量。
3. 静态变量：使用 static 关键字定义的变量。
4. 实例变量：没有使用 static 关键字定义的变量。

