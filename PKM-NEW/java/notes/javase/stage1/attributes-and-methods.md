# 属性与成员方法

---
## 属性

1. 属性的定义：`访问修饰符 属性类型 属性名;`
2. 访问修饰符：`public`、`protected`、默认(空着不写)、`private`
3. 属性可以是基本数据类型，也可以是引用类型比如字符串和数组
4. 属性如果不赋值，有默认值，规则和数组一致
	1. 整数：`0`
	2. 浮点数：`0.0`
	3. 布尔：`false`
	4. 字符：`\u0000`
	5. String：`null`

---
## 成员方法

1. 成员方法案例

   ```java
   public class Program{
     public static void main(String[] args){
       Cat cat = new Cat();
       cat.say(); // 调用方法
     }
   }
   
   class Cat{
     // 方法
     public void say(){
       System.out.println("小猫爱吃小鱼干");
     }
   }
   ```

   ```
   >>>小猫爱吃小鱼干
   ```

2. 传参的成员方法案例

	```java
	public class Program{
		public static void main(String[] args){
			Cat cat = new Cat();
			cat.say("小老鼠"); // 调用方法
		}
	}
	
	class Cat{
		// 方法
		public void say(String food){
			System.out.println("小猫爱吃"+food);
		}
	}
	```

   ```
   >>>小猫爱吃小老鼠
   ```

3. 成员方法定义

   ```java
   访问修饰符 返回数据类型 方法名(形参列表..){
     语句;
     return 返回值;
   }
   ```

4. 返回值

   1. 返回多个返回值，建议使用数组

      ```java
      public int[] getSubAndSum(int x, int y){
        int[] arr = new int[2];
        arr[0] = x - y;
        arr[1] = x + y;
        return arr;
      }
      ```

   2. return类型需要与声明的一直或兼容：比如`public double getMoney(int i){..}`然后里边`int a = 1; return a; `是可以的，这里int会自动转化成double

5. 方法名：建议使用小驼峰命名法

6. 形参列表

   1. 一个方法可以有多个参数也可以没有参数
   2. 参数类型可以为基本类型和引用类型
   3. 调用带参数的方法，要传入相同或兼容的类型的参数

7. 方法中不能定义方法

8. 方法调用

   1. 同一个类中：直接调用

      ```java
      class Cat{
      	public void miao(){
      		System.out.println("Miao~");
      	}
        public void doubleMiao(){
          miao();//同一个类中：直接调用 (和 python 不一样)
          miao();
        }
      }
      ```

   2. 跨类中的方法（A类调用B类）：需要通过对象名调用

      ```java
      class Cat{
      	public void miao(){
      		System.out.println("Miao~");
      	}
      }
      class Dog{
        public void biteCat(){
          System.out.println("Woof!");
          Cat cat = new Cat();
          cat.miao(); //跨类中的方法
        }
      }
      ```

---
## 成员方法的调用机制

讨论下面代码，成员方法的调用机制

```java
public class Program{
  public static void main(String[] args){
    Calculator cal = new Calculator();
    System.out.println('1+2=',calculator.sum(1,2));
  }
}
class Calculator{
  public double sum(double x,double y){
    x+y;
  }
}
```

1. 执行main的第0句，在常量池加载类，在堆中开辟空间，在栈中保存地址
2. 当程序执行到方法时，就会开辟一个独立的空间（栈空间），比如main栈、sum栈
3. 当方法执行到return（执行完毕），就会返回到调用方法的地方

```json
{	
	"栈": 
  {
    "main栈":
    {
      0:"Calculater cal = new Calculater();",
      1:"System.out.println('1+2=',calculator.sum(1,2));" //<---执行到这里
    },
    "sum栈": //<---return后sum栈自动销毁
    {
      0: x->1,
      1: y->2,
      3:"return x+y;"
    }
  },
  "堆": 
  {
    "0x0011": "cal对象"
  },
  "方法区": 
  {}
}
```

---
## 成员方法的传参机制

方法会改变调用位置的引用类型的参数，不会改变基础类型的参数

```java
public class Program{
  public static void main(String[] args){
    int x = 1;
    String y = "Hello";
    Cat z1 = new Cat(2);
    Cat z2 = new Cat(2);
    Tester tester = new Tester();
    tester.change(x,y,z1,z2);
    System.out.println("x="+x);          // x=1
    System.out.println("y="+y);          // 
    System.out.println("z1.age="+z1.age);//
    System.out.println("z2.age="+z2.age);//
  }
}

class Tester{
  int num=0;
  public void change(int x,String y,Cat z1, Cat z2){
    x = 10;
    y = "World";
    z1.age = 3;
    z2 = null;
  }
}

class Cat{
  int age;
  public Cat(int age){
    this.age = age;
  }
}
```

```java
// 答案
System.out.println("x="+x);           //1
System.out.println("y="+y);           //Hello
System.out.println("z1.age="+z1.age); //3
System.out.println("z2.age="+z2.age); //2
```

分析上面的代码：

1. `int x = 1;`
   * x并不会被改变
2. `String y = "Hello";`
   * y不会被改变
   * main的y指向"Hello"，change的y也指向"Hello"。后来change的y指向"World"，但是main的y还是指向"Hello"
3. `Cat z1 = new Cat(2);`
   * z1.age会被改变
   * main的z1和change的z1同时指向一个对象，这一个对象内部的值进行了修改
4. `Cat z2 = new Cat(2);`
   * z2.age不会被改变
   * main的z2和change的z2同时指向一个对象，后来change的z2指向null，main的z2仍指向对象

---
## 可变参数

* 可变参数：参数个数不确定，`function(int... a)`，上例中的a可以方程数组

* 小案例

  ```java
  public class Program{
    public static void main(String[] args){
      T t = new T();
      System.out.println(t.plus(1,2,3,4)); // 10.0
    }
  }
  
  class T{
    public double plus(double... num){
      double sum = 0;
      for(int i=0;i<num.length;i++)
        sum+=num[i];
      return sum;
    }
    public double plus2(String str, double... num){
      System.out.print(str);
      return plus(num);
    }
  }
  ```

* 细节

  ```java
  // 可变参数的实参可以为0或任意多个
  System.out.println(t.plus(1,2,3,4)); // 10.0
  // 可变参数的实参可以为数组 - 可变参数本质就是数组
  System.out.println(t.plus(new double[]{1,2,3,4})); //10.0
  // 可变参数可以和普通参数放在一起，可变参数要在最后
  System.out.println(t.plus2("结果为:",new double[]{1,2}));//结果为:3.0
  // 形参列表只能有一个可变参数
  ```

* 案例：有三个方法，分别实现返回姓名和两门课成绩（总分），返回姓名和三门课成绩（总分），返回姓名和五门课成绩（总分）。封装成一个可变参数的方法

	```java
	public class Demo{
		public static void main(String[] args){
			System.out.println(format("Charles",90,95,100));
		}
	
		public static String format(String name, double... scores){
			double total = 0;
			for(int i=0; i<scores.length; i++)
				total += scores[i];
			return name + scores.length + "门课, 成绩总分为: " + total;
		}
	}
	```

---
## Overload（方法重载）

* 方法重载：同一个类中，多个同名方法存在，单要求形参不同

* 小案例

  ```java
  public class Program{
    public static void main(String[] args){
      T t = new T();
      // 调用了 public int plus(int a, int b)
      System.out.println(t.plus(1,2)); // 3
      // 调用了 public double plus(double a, double b)
      System.out.println(t.plus(1.1,2.2)); // 3.3
      // 调用了 public double plus(double a, double b)
      // 1隐形转换成了1.0
      System.out.println(t.plus(1,2.0)); // 3.0
    }
  }
  
  class T{
    public int plus(int a, int b){
      return a+b;
    }
    public double plus(double a, double b){
      return a+b;
    }
  }
  ```

* 要求：方法名必须相同，参数列表必须不同，对返回类型无要求

	```java
	// 与下边构成方法重载的
	void show(int a, char b, double c){}
	
	void show(int x, char y, double z){} // 不是
	int show(int a, double c, char b){}  // 是
	void show(int a, double c, char b){} // 是
	boolean show(int c, char b){}        // 是
	void show(double c){}                // 是
	double show(int x, char y, double z){}//不是
	void shows(){}                       // 不是
	```

> 方法重载和方法重写怎么区分？（我的理解）重载是 load，是不同的载入，同时存在了多份。重写是 write(ride)，之前的没了，变成了新的。


---
## 作用域

|        |   全局变量    |   局部变量   |
| :----: | :-----------: | :----------: |
|  别称  | 成员变量/属性 |      -       |
|  位置  |   class里边   |   函数里边   |
| 默认值 |      有       |      无      |
| 修饰符 | 可以加修饰符  | 不能加修饰符 |

```java
public class Demo{
	public static void main(String[] args){
	}
}

class Cat{
	double weight; // 默认是 0.0，属性（全局变量）会有默认值
	public void hi(){
		double weight2;
		System.out.println(weight2);// 这个报错，因为局部变量没有初始化
	}
}
```

```java
public class Demo{
	public static void main(String[] args){
	}
}

class Cat{
	double weight = 10.0;
	public void hi(){
		double weight = 20.0;// 可以重名，访问按照就近原则
		System.out.println(weight);// 20.0
	}
}
```

---

## (面试题)成员变量和局部变量的区别

1. 从语法形式上看：成员变量是属于类的，⽽局部变量是在⽅法中定义的变量或是⽅法的参数；成员变量可以被 public , private , static 等修饰符所修饰，⽽局部变量不能被访问控制修饰符及 static 所修饰；但是，成员变量和局部变量都能被 final 所修饰。
2. 从变量在内存中的存储⽅式来看：如果成员变量是使⽤ static 修饰的，那么这个成员变量是属于类的，如果没有使⽤ static 修饰，这个成员变量是属于实例的。对象存于堆内存，如果局部变量类型为基本数据类型，那么存储在栈内存，如果为引⽤数据类型，那存放的是指向堆内存对象的引⽤或者是指向常量池中的地址。
3. 从变量在内存中的⽣存时间上看：成员变量是对象的⼀部分，它随着对象的创建⽽存在，⽽局部变量随着⽅法的调⽤⽽⾃动消失。
4. 成员变量如果没有被赋初值：则会⾃动以类型的默认值⽽赋值（⼀种情况例外:被 final 修饰的成员变量也必须显式地赋值），⽽局部变量则不会⾃动赋值

---

## (面试题)Java 是值传递，还是引⽤传递

Java 是**值传递**，不是引⽤传递。

当⼀个对象被作为参数传递到⽅法中时，参数的值就是该对象的引⽤。引⽤的值是对象在堆中的地址。

对象是存储在堆中的，所以传递对象的时候，可以理解为把变量存储的对象地址给传递过去。