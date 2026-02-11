# Lambda表达式

---
## 主要内容

| **知识点**           | **要求** |
| ----------------- | ------ |
| Lambda表达式的概述      | 理解     |
| Lambda表达式的使用      | 了解     |
| Lambda表达式的方法引用    | 掌握     |
| Lambda表达式的在集合中的使用 | 理解     |

---
## Lambda表达式的概述

### Lambda表达式的引入

Lambda表达式是**JDK1.8**的一个新特性，可以取代大部分的匿名内部类，以便写出更优雅的Java代码，尤其在集合的遍历和其他集合操作中，可以极大地优化代码结构。

在以前的学习中，想要实现对List集合的“降序”排序操作，就需要使用匿名内部类来实现，这样的代码非常的复杂和繁琐，代码如下：

```java
// 方式一：使用匿名内部类来实现  
List<Integer> list = Arrays.asList(3, 6, 1, 7, 2, 5, 4);  
Collections.sort(list, new Comparator<Integer>() {  
    @Override
    public int compare(Integer o1, Integer o2) {  
        return o2 - o1;  
    }  
});  
System.out.println("排序后：" + list);
```

针对以上对List集合的的“降序”排序操作，可以使用Lambda表达式来实现：

```java
// 方式二：使用Lambda表达式来实现  
List<Integer> list = Arrays.asList(3, 6, 1, 7, 2, 5, 4);  
Collections.sort(list, (o1, o2) -> o2 - o1);
System.out.println("排序后：" + list);
```

案例
```java
package ex_array;

import java.util.Comparator;
import java.util.Arrays;
import java.util.TreeSet;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

/**
 * 用户类 - 使用Lombok注解简化代码
 */
@Getter
@Setter
@AllArgsConstructor
@ToString
class User {
  private int age;
}

/**
 * ClassName: LambdaTest01
 * Description: 先体会一下Java8的新特性：Lambda表达式
 * <p>
 * Datetime: 2024/2/2 8:38
 * Author: 老杜@动力节点
 * Version: 1.0
 */
public class LambdaTest01 {
  public static void main(String[] args) {
    // TreeSet集合中的元素是可以自动排序的。
    // TreeSet集合是怎么排序的？ 两种方式
    // 第一种方式：如果比较规则固定不变，可以让TreeSet集合中的元素实现java.lang.Comparable接口。
    // 第二种方式：创建TreeSet集合的时候，给TreeSet集合传递一个比较器对象，比较器实现java.util.Comparator接口。
    // 第二种 匿名内部类的方式实现
    TreeSet<User> users1 = new TreeSet<>(new Comparator<User>() {
      @Override
      public int compare(User o1, User o2) {
        return o1.getAge() - o2.getAge();
      }
    });
    // 第二种 lambda表达式的方式实现
    TreeSet<User> users2 = new TreeSet<>((User o1, User o2) -> { return o1.getAge() - o2.getAge(); });
    // 第二种 lambda表达式的简化的方式实现
    TreeSet<User> users3 = new TreeSet<>((o1, o2) ->  o1.getAge() - o2.getAge() );

    User[] users = new User[]{new User(20),new User(30),new User(40),new User(10)};
    users1.addAll(Arrays.asList(users));
    users2.addAll(Arrays.asList(users));
    users3.addAll(Arrays.asList(users));
    System.out.println(users1);
    System.out.println(users2);
    System.out.println(users3);
    // 都是 [User(age=10), User(age=20), User(age=30), User(age=40)]
  }
}
```

### 函数式编程思想的概述

Java从诞生之日起就一直倡导“一切皆对象”，在Java语言中面向对象（OOP）编程就是一切，但是随着Python和Scala等语言的崛起和新技术的挑战，Java也不得不做出调整以便支持更加广泛的技术要求，即Java语言不但支持OOP还支持OOF（面向函数编程）。 JDK1.8引入Lambda表达式之后，Java语言也开始支持函数式编程，但是Lambda表达式不是Java语言最早使用的，目前C++、C#、Python、Scala等语言都支持Lambda表示。

- 面向对象的思想：做一件事情，找一个能解决这个事情的对象，然后调用对象的方法，最终完成事情。
- 函数式编程思想：只要能获得结果，谁去做的，怎么做的都不重要，重视的是结果，不重视实现过程。

在函数式编程语言中，函数被当成一等公民对待。在将函数当成一等公民的编程语言中，Lambda表达式的类型是函数，但是Lambda表达式却是一个对象，而不是函数，它们必须依附于一类特别的对象类型，也就是所谓的函数式接口。 简单点说，JDK1.8中的Lambda表达式就是一个函数式接口的实例，这就是Lambda表达式和函数式接口的关系。也就是说，**只要一个对象是函数式接口的实例，那么该对象就可以使用Lambda表达式来表示**。

### 如何去理解函数式接口

能够使用Lambda表达式的一个重要依据是必须有相应的函数式接口，所谓的函数式接口，指的就是“一个接口中有且只能有一个抽象方法”。也就是说，如果一个接口只有一个抽象方法，那么该接口就是一个函数式接口。 如果我们在接口上声明了 `@FunctionalInterface` 注解，那么编译器就会按照函数式接口的定义来要求该接口，也就是该接口中有且只能定义一个抽象方法，如果该接口中定义了多个或0个抽象方法，则程序编译时就会报错。 

【示例】定义一个函数式接口

```java
@FunctionalInterface  
public interface Flyable {  
    // 在函数式接口中，我们有且只能定义一个抽象方法  
    void showFly();  
    // 但是，可以定义任意多个默认方法或静态方法  
    default void show() {  
        System.out.println("JDK1.8之后，接口还可以定义默认方法和静态方法");  
    }  
}
```

另外，从某种意义上来说，只要你保证你的**接口中有且只有一个抽象方法**，则接口中没有使用 `@FunctionalInterface` 注解来标注，那么该接口也依旧属于函数式接口。 在以下代码中，Flyable接口中没有使用`@FunctionalInterface` 注解，但是`Flyable`接口中只存在一个抽象方法，因此`Flyable`接口依旧属于函数式接口：

```java
/**  
 * 没有使用@FunctionalInterface标注的接口  
 */  
public interface Flyable {  
    void showFly();  
}  
/**  
 * 测试类  
 */  
public class Test01 {  
    public static void main(String[] args) {  
        // 使用lambda表示来表示Flyable接口的实例  
        Flyable flyable = () -> {  
            System.out.println("小鸟自由自在的飞翔");  
        };  
        // 调用Flyable接口的实例的showFly()方法  
        flyable.showFly();  
    }  
}
```

### Lambda和匿名内部类

- 所需类型不同
  
    - 匿名内部类：可以是接口，抽象类，具体类。
    - Lambda表达式：**只能是接口**。
    
- 使用限制不同
  
    - 如果接口中有且仅有一个抽象方法，可以使用Lambda表达式，也可以使用匿名内部类。
    - 如果接口中有多个抽象方法，则就只能使用匿名内部类，而不能使用Lambda表达式。
    
- 实现原理不同
  
    - 匿名内部类：编译之后，会生成一个单独的.class字节码文件。
    - Lambda表达式：编译之后，**没有生成一个单独的.class字节码文件**。
      
```java
package com.powernode.javase.lambda;

/**
 * ClassName: LambdaTest02
 * Description:
 *      Lambda表达式和匿名内部类的区别：
 *          所需类型不同：
 *              匿名内部类，可以是抽象类，也可以是接口。
 *              Lambda表达式，只能是接口。
 *          使用限制不同：
 *              Lambda表达式使用的接口中要求有且只有一个抽象方法。
 *              匿名内部类方式使用的接口可以有多个抽象方法。
 *          实现原理不同：
 *              采用匿名内部类的话，编译之后会生成一个.class文件。
 *              采用Lambda表达式的话，编译之后不会生成单独的.class文件。
 * <p>
 * Datetime: 2024/2/2 9:10
 * Author: 老杜@动力节点
 * Version: 1.0
 */
public class LambdaTest02 {

    public static void main(String[] args) {

        // 匿名内部类方式（匿名内部类可以是一个抽象类）
        LambdaTest02.test(new Animal() {
            @Override
            public void run() {
                System.out.println("Animal run....");
            }
        });

        // 尝试将上面的代码修改为Lambda表达式方式
        // 编译报错，原因是：只有接口才可以使用Lambda表达式
        //LambdaTest02.test(() -> { System.out.println("Animal run...."); });

        // 匿名内部类
        /*LambdaTest02.doFly(new Flyable() {
            @Override
            public void run() {
                System.out.println("run.....");
            }

            @Override
            public void fly() {
                System.out.println("fly.....");
            }
        });*/

        // 尝试使用Lambda表达式
        // Lambda表达式使用的接口必须是函数式接口。（必须是接口，而且接口中有且只有一个抽象方法。）
        //LambdaTest02.doFly(() -> { System.out.println("run....."); });
    }

    public static void test(Animal a){
        a.run();
    }

    public static void doFly(Flyable f){
        f.fly();
        f.run();
    }
}

abstract class Animal{
    public abstract void run();
}

interface Flyable {
    void run();
    void fly();
}
```
---
## Lambda表达式的使用

### Lambda表达式的语法

Lambda表达式本质就是一个匿名函数，在函数的语法中包含返回值类型、方法名、形参列表和方法体等，而在Lambda表达式中我们只需要关心形参列表和方法体即可。 在Java语言中，Lambda表达式的语法为`“(形参列表) -> {方法体}”`，其中“->”为 lambda操作符或箭头操作符，“形参列表”为对应接口实现类中重写方法的形参列表，“方法体”为对应接口实现类中重写方法的方法体。 接下来，我们就以匿名内部类为例，从而将匿名内部类演化为Lambda表达式，代码如下：

```java
List<Integer> list = Arrays.asList(3, 6, 1, 7, 2, 5, 4);  
Collections.sort(list, new Comparator<Integer>() {  
    @Override  
    public int compare(Integer o1, Integer o2) {  
        return o2 - o1;  
    }  
});  
System.out.println("排序后：" + list);
```

在以上的匿名内部类对应的Lambda表达式代码实现如下：

```java
List<Integer> list = Arrays.asList(3, 6, 1, 7, 2, 5, 4);  
Collections.sort(list, (Integer o1, Integer o2) -> {  
    return o2 - o1;  
});  
System.out.println("排序后：" + list);
```

最后可以进一步精简Lambda表达式：

```java
List<Integer> list = Arrays.asList(3, 6, 1, 7, 2, 5, 4);  
Collections.sort(list, (o1, o2) -> o2 - o1);  
System.out.println("排序后：" + list);
```

### Lambda表达式的使用

#### Lambda表达式的基本使用

接下来，我们以自定义的函数式接口为例，先从匿名对象的实现过程，慢慢演变为Lambda表达式的实现过程。另外，使用Lambda表达式的时候，则必须有上下文环境，才能推导出Lambda对应的接口类型。

##### 无返回值函数式接口

情况一：无返回值无参数

```java
package com.powernode.javase.lambda;

/**
 * ClassName: LambdaTest04
 * Description:
 *          Lambda表达式的使用：关于无返回值无参数的函数式接口。
 * <p>
 * Datetime: 2024/2/2 10:00
 * Author: 老杜@动力节点
 * Version: 1.0
 */
public class LambdaTest04 {
    public static void main(String[] args) {
        // 匿名内部类方式
        NoParameterNoReturn npnr = new NoParameterNoReturn() {
            @Override
            public void test() {
                System.out.println("无返回值无参数的test方法执行了。");
            }
        };
        npnr.test();

        // 改成Lambda表达式
        NoParameterNoReturn npnr2 = () -> { System.out.println("无返回值无参数的test方法执行了。"); };
        npnr2.test();

        // 精简
        NoParameterNoReturn npnr3 = () -> System.out.println("无返回值无参数的test方法执行了。");
        npnr3.test();
    }
}

@FunctionalInterface
interface NoParameterNoReturn {
    void test();
}

```

情况二：无返回值一个参数

```java
package com.powernode.javase.lambda;

/**
 * ClassName: LambdaTest05
 * Description:
 *          Lambda表达式的使用：关于无返回值一个参数的函数式接口。
 * <p>
 * Datetime: 2024/2/2 10:04
 * Author: 老杜@动力节点
 * Version: 1.0
 */
public class LambdaTest05 {
    public static void main(String[] args) {
        // 匿名内部类的方式
        OneParameterNoReturn opnr = new OneParameterNoReturn() {
            @Override
            public void test(Integer value) {
                System.out.println("Integer-->" + value);
            }
        };
        opnr.test(1000);

        // Lambda表达式方式
        OneParameterNoReturn opnr2 = (Integer value) -> { System.out.println("Integer-->" + value); };
        opnr2.test(2000);

        // 精简：一个参数时可以省略括号
        OneParameterNoReturn opnr3 = value -> System.out.println("Integer-->" + value);
        opnr3.test(2000);
    }
}

@FunctionalInterface
interface OneParameterNoReturn {
    void test(Integer value);
}

```

情况三：无返回值多个参数

```java
package com.powernode.javase.lambda;

/**
 * ClassName: LambdaTest06
 * Description:
 *          Lambda表达式的使用：关于无返回值多个参数的函数式接口。
 * <p>
 * Datetime: 2024/2/2 10:06
 * Author: 老杜@动力节点
 * Version: 1.0
 */
public class LambdaTest06 {
    public static void main(String[] args) {
        // 匿名内部类的方式
        MoreParameterNoReturn mpnr = new MoreParameterNoReturn() {
            @Override
            public void test(Integer value1, Integer value2) {
                System.out.println(value1 + value2);
            }
        };
        mpnr.test(100, 200);

        // Lambda表达式方式
        MoreParameterNoReturn mpnr2 = (Integer value1, Integer value2) -> { System.out.println(value1 + value2); };
        mpnr2.test(300, 400);

        // 精简：多参数，不能省略括号，只能省略数据类型
        MoreParameterNoReturn mpnr3 = (value1, value2) -> System.out.println(value1 + value2);
        mpnr3.test(300, 400);
    }
}

@FunctionalInterface
interface MoreParameterNoReturn {
    void test(Integer value1, Integer value2);
}

```

##### 有返回值函数接口

情况一：有返回值无参数

```java
package com.powernode.javase.lambda;

/**
 * ClassName: LambdaTest07
 * Description:
 *          Lambda表达式的使用：关于有返回值无参数的函数式接口。
 * <p>
 * Datetime: 2024/2/2 10:09
 * Author: 老杜@动力节点
 * Version: 1.0
 */
public class LambdaTest07 {
    public static void main(String[] args) {
        // 匿名内部类的方式
        NoParameterHasReturn nphr = new NoParameterHasReturn() {
            @Override
            public Integer test() {
                return 300;
            }
        };
        System.out.println(nphr.test());

        // Lambda表达式的方式
        NoParameterHasReturn nphr2 = () -> { return 500; };
        System.out.println(nphr2.test());

        // 精简
        NoParameterHasReturn nphr3 = () -> 500;
        System.out.println(nphr3.test());
    }
}

@FunctionalInterface
interface NoParameterHasReturn {
    Integer test();
}
```

情况二：有返回值一个参数

```java
package com.powernode.javase.lambda;

/**
 * ClassName: LambdaTest08
 * Description:
 *          Lambda表达式的使用：关于有返回值一个参数的函数式接口。
 * <p>
 * Datetime: 2024/2/2 10:12
 * Author: 老杜@动力节点
 * Version: 1.0
 */
public class LambdaTest08 {
    public static void main(String[] args) {
        // 匿名内部类的方式
        OneParameterHasReturn ophr = new OneParameterHasReturn() {
            @Override
            public Integer test(Integer value) {
                return value * 2;
            }
        };
        System.out.println(ophr.test(100));

        // Lambda表达式的方式
        OneParameterHasReturn ophr2 = (Integer value) -> { return value * 2; };
        System.out.println(ophr2.test(200));

        // 精简
        OneParameterHasReturn ophr3 = value -> value * 2;
        System.out.println(ophr3.test(200));
    }
}

@FunctionalInterface
interface OneParameterHasReturn {
    Integer test(Integer value);
}

```

情况三：有返回值多个参数

```java
package com.powernode.javase.lambda;

/**
 * ClassName: LambdaTest09
 * Description:
 *          Lambda表达式的使用：关于有返回值多个参数的函数式接口。
 * <p>
 * Datetime: 2024/2/2 10:15
 * Author: 老杜@动力节点
 * Version: 1.0
 */
public class LambdaTest09 {
    public static void main(String[] args) {
        // 匿名内部类方式
        MoreParameterHasReturn mphr = new MoreParameterHasReturn() {
            @Override
            public Integer test(Integer value1, Integer value2) {
                return value1 + value2;
            }
        };
        System.out.println(mphr.test(1, 2));

        // Lambda表达式的方式
        MoreParameterHasReturn mphr2 = (Integer value1, Integer value2) -> { return value1 + value2; };
        System.out.println(mphr2.test(3, 4));

        // 精简
        MoreParameterHasReturn mphr3 = (a, b) -> a + b;
        System.out.println(mphr3.test(3, 4));

    }
}

@FunctionalInterface
interface MoreParameterHasReturn {
    Integer test(Integer value1, Integer value2);
}
```

#### Lambda表达式的语法精简

在以上代码中，虽然Lambda表达式的语法已经很简洁了，但是Lambda表达式的语法格式还可以更加的精简，从而写出更加优雅的代码，但是相应的代码可读性也会变差。 在以下的应用场景中，我们就可以对Lambda表达式的语法进行精简，场景如下：

1. 形参类型可以省略，如果需要省略，则每个形参的类型都要省略。
   
2. 如果形参列表中只存在一个形参，那么形参类型和小括号都可以省略。
   
3. 如果方法体当中只有一行语句，那么方法体的大括号也可以省略。
   
4. 如果方法体中只有一条return语句，那么大括号可以省略，且必须去掉return关键字。
   

接下来，我们就对以下的Lambda表达式代码进行精简，从而写出更加优雅的代码。

```java
public class Test01 {  
    public static void main(String[] args) {  
        // (1)形参类型可以省略，如果需要省略，每个形参的类型都要省略。  
        // 没有精简的Lambda表达式代码  
        MoreParameterNoReturn obj1 = (String str1, String str2) -> {  
            System.out.println(str1 + " : " + str2);  
        };  
        obj1.test("hello", "world");  
        // 精简之后的Lambda表达式代码  
        MoreParameterNoReturn obj2 = (str1, str2) -> {  
            System.out.println(str1 + " : " + str2);  
        };  
        obj2.test("你好", "世界");  
  
        // (2)如果形参列表中只有一个形参，那么形参类型和小括号都可以省略。  
        // 没有精简的Lambda表达式代码  
        OneParameterHasReturn obj3 = (double num) -> {  
            return "传入的小数为：" + num;  
        };  
        System.out.println(obj3.test(520.0));  
        // 精简之后的Lambda表达式代码  
        OneParameterHasReturn obj4 = num -> {  
            return "传入的小数为：" + num;  
        };  
        System.out.println(obj4.test(1314.0));  
  
        // (3)如果方法体当中只有一行代码，那么方法体的大括号也可以省略。  
        // 没有精简的Lambda表达式代码  
        NoParameterNoReturn obj5 = () -> {  
            System.out.println("无参无返回值");  
        };  
        obj5.test();  
        // 精简之后的Lambda表达式代码  
        NoParameterNoReturn obj6 = () -> System.out.println("无参无返回值");  
        obj6.test();  
  
        // (4)方法体中只有一条return语句，则大括号可以省略，且必须去掉return关键字  
        // 没有精简的Lambda表达式代码  
        MoreParameterHasReturn obj7 = (int a, int b) -> {  
            return "运算的结果为：" + (a + b);  
        };  
        System.out.println(obj7.test(10, 20));  
        // 精简之后的Lambda表达式代码  
        MoreParameterHasReturn obj8 = (a, b) -> "运算的结果为：" + (a + b);  
        System.out.println(obj8.test(20, 30));  
    }  
}
```

### 四个基本的函数式接口

|名字|接口名|对应的抽象方法|
|---|---|---|
|消费|Consumer<T>|void accept(T t);|
|生产|Supplier<T>|T get();|
|转换|Function<T, R>|R apply(T t);|
|判断|Predicate<T>|boolean test(T t);|

以上的函数式接口都在java.util.function包中，通常函数接口出现的地方都可以使用Lambda表达式，所以不必记忆函数接口的名字，这些函数式接口及子接口在后续学习中很常用。

---
## Lambda表达式的方法引用

### 方法引用的概述

我们在使用Lambda表达式的时候，如果Lambda表达式的方法体中除了调用现有方法之外什么都不做，满足这样的条件就有机会使用方法引用来实现。 在以下的代码中，在重写的apply()方法中仅仅只调用了现有Math类round()方法，也就意味着Lambda表达式中仅仅只调用了现有Math类round()方法，那么该Lambda表达式就可以升级为方法引用，案例如下：

```java
// 需求：实现小数取整的操作  
// 方式一：使用匿名对象来实现  
Function<Double, Long> function1 = new Function<Double, Long>() {  
    @Override  
    public Long apply(Double aDouble) {  
        return Math.round(aDouble);  
    }  
};  
System.out.println(function1.apply(3.14));  
  
// 方式二：使用Lambda表达式来实现  
Function<Double, Long> function2 = aDouble -> Math.round(aDouble);  
System.out.println(function2.apply(3.14));  
  
// 方式三：使用方法引用来实现  
Function<Double, Long> function3 = Math :: round;  
System.out.println(function3.apply(3.14));
```

对于方法引用，我们可以看做是Lambda表达式深层次的表达。换句话说，方法引用就是Lambda表达式，也就是函数式接口的一个实例，通过方法的名字来指向一个方法，可以认为是Lambda表达式的一个语法糖。 在Lambda表达式的方法引用中，主要有实例方法引用、静态方法引用、特殊方法引用和构造方法引用、数组引用这五种情况，接下来我们就对这五种情况进行讲解。

### 实例方法引用

语法：`对象 :: 实例方法` 特点：在Lambda表达式的方法体中，通过“对象”来调用指定的某个“实例方法”。 要求：函数式接口中抽象方法的返回值类型和形参列表 与 内部通过对象调用某个实例方法的返回值类型和形参列表 保持一致。 【示例】实例化Consumer接口的实现类对象，并在重写的accept()方法中输出形参的值

```java
package com.powernode.javase.lambda;  
  
import java.util.function.Supplier;  
  
/**  
 * ClassName: LambdaTest10 * Description: 实例方法引用  
 *          语法格式：  
 *              对象::实例方法名  
 *  
 *          满足什么条件的时候可以使用实例方法引用？  
 *              函数式接口中的   返回值类型   和    形参  
 *              与  
 *              内部调用的方法的 返回值类型   和    形参  
 *              一致。  
 * <p>  
 * Datetime: 2024/2/2 11:28 
 * Author: 老杜@动力节点  
 * Version: 1.0  
 */
public class LambdaTest10 {  
    public static void main(String[] args) {  
        // 使用生产型接口：Supplier  
        // 匿名内部类的方式  
        Teacher teacher = new Teacher("老杜");  
        Supplier<String> supplier = new Supplier<String>() {  
            @Override  
            public String get() {  
                return teacher.getName();  
            }  
        };  
        System.out.println(supplier.get());  
  
        // 以上是否符合“实例方法引用”的条件？  
        // 先修改为Lambda表达式  
        Supplier<String> supplier1 = () -> teacher.getName();  
        System.out.println(supplier1.get());  
  
        // 使用“实例方法引用”精简  
        Supplier<String> supplier2 = teacher::getName;  
        System.out.println(supplier2.get());  
  
    }  
}  
  
class Teacher {  
    private String name;  
  
    public Teacher(String name) {  
        this.name = name;  
    }  
  
    public String getName() {  
        return name;  
    }  
  
    public void setName(String name) {  
        this.name = name;  
    }  
  
    @Override  
    public String toString() {  
        return "Teacher{" +  
                "name='" + name + '\'' +  
                '}';  
    }  
}
```

【示例】实例化Supplier接口的实现类对象，并在重写方法中返回Teacher对象的姓名

```java
package com.powernode.javase.lambda;

import java.util.function.Consumer;

/**
 * ClassName: LambdaTest11
 * Description: 实例方法引用
 * <p>
 * Datetime: 2024/2/2 11:36
 * Author: 老杜@动力节点
 * Version: 1.0
 */
public class LambdaTest11 {
    public static void main(String[] args) {
        // 匿名内部类的方式
        // 使用消费型的函数式接口
        Consumer<String> consumer = new Consumer<String>() {
            @Override
            public void accept(String s) {
                System.out.println(s);
            }
        };
        consumer.accept("动力节点");

        // 修改为Lambda表达式
        Consumer<String> consumer1 = s -> System.out.println(s);
        consumer1.accept("动力节点");

        // 使用 实例方法引用 精简
        Consumer<String> consumer2 = System.out::println;
        consumer2.accept("动力节点");
    }
}
```


### 静态方法引用

语法：`类 :: 静态方法` 特点：在Lambda表达式的方法体中，通过“类名”来调用指定的某个“静态方法”。 要求：函数式接口中抽象方法的返回值类型和形参列表 与 内部通过类名调用某个静态方法的返回值类型和形参列表保持一致。

【示例】实例化Function接口的实现类对象，并在重写的方法中返回小数取整的结果

```java
package com.powernode.javase.lambda;

import java.util.function.Function;

/**
 * ClassName: LambdaTest12
 * Description: 静态方法引用
 *
 *          语法格式：
 *              类名::静态方法名
 *
 *          条件：
 *              函数式接口中的方法的     返回值类型     和    形参
 *              与
 *              内部调用静态方法的      返回值类型      和    形参
 *              一致。
 * <p>
 * Datetime: 2024/2/2 11:41
 * Author: 老杜@动力节点
 * Version: 1.0
 */
public class LambdaTest12 {
    public static void main(String[] args) {
        // 匿名内部类方式
        // 使用转换型函数式接口
        Function<Double, Long> function = new Function<Double, Long>() {
            @Override
            public Long apply(Double value) {
                return Math.round(value);
            }
        };
        System.out.println(function.apply(3.14));

        // Lambda表达式
        Function<Double, Long> function2 = value -> Math.round(value);
        System.out.println(function2.apply(5.67));

        // 静态方法引用改进
        Function<Double, Long> function3 = Math::round;
        System.out.println(function3.apply(5.67));
    }
}
```

### 特殊方法引用

语法：`类名 :: 实例方法` 特点：在Lambda表达式的方法体中，通过方法的第一个形参来调用指定的某个“实例方法”。 要求：把函数式接口中抽象方法的第一个形参作为方法的调用者对象，并且从第二个形参开始（或无参）可以对应到被调用实例方法的参数列表中，并且返回值类型保持一致。 【示例】使用Comparator比较器，来判断两个小数的大小

```java
package com.powernode.javase.lambda;

import java.util.Comparator;

/**
 * ClassName: LambdaTest13
 * Description: 特殊方法引用
 *          语法格式：
 *              类名::实例方法
 *
 *          条件：
 *              1. 函数式接口中抽象方法的第一个参数作为内部方法调用对象。
 *              2. 从函数式接口的抽象方法的第二参数开始 与 内部调用方法时的参数类型  一致。
 *              3. 函数式接口中的抽象方法返回值类型  与  内部方法返回值类型  一致。
 * <p>
 * Datetime: 2024/2/2 11:52
 * Author: 老杜@动力节点
 * Version: 1.0
 */
public class LambdaTest13 {
    public static void main(String[] args) {
        // 匿名内部类
        Comparator<Double> comparator = new Comparator<Double>() {
            @Override
            public int compare(Double o1, Double o2) {
                return o1.compareTo(o2);
            }
        };
        System.out.println(comparator.compare(3.14, 5.6));

        // Lambda表达式
        Comparator<Double> comparator2 = (o1, o2) -> o1.compareTo(o2);
        System.out.println(comparator2.compare(3.14, 5.6));

        // 特殊方法引用
        Comparator<Double> comparator3 = Double::compareTo;
        System.out.println(comparator3.compare(3.14, 5.6));

    }
}

```

需求：实例化Function接口的实现类对象，然后获得传入Teacher对象的姓名。

```java
package com.powernode.javase.lambda;

import java.util.function.Function;

/**
 * ClassName: LambdaTest14
 * Description: 特殊方法引用
 *          语法格式：
 *              类名::实例方法名
 * <p>
 * Datetime: 2024/2/2 14:02
 * Author: 老杜@动力节点
 * Version: 1.0
 */
public class LambdaTest14 {
    public static void main(String[] args) {
        // 转换型的函数式接口
        // 匿名内部类
        Function<Vip, String> function = new Function<Vip, String>() {
            @Override
            public String apply(Vip vip) {
                return vip.getName();
            }
        };

        Vip vip = new Vip("老杜");
        System.out.println(function.apply(vip));

        // Lambda表达式
        //Function<Vip, String> function2 = (Vip v) -> {return v.getName();};
        Function<Vip, String> function2 = v -> v.getName();
        System.out.println(function2.apply(vip));

        // 使用“特殊方法引用”来进行精简
        Function<Vip, String> function3 = Vip::getName;
        System.out.println(function3.apply(vip));
    }
}

class Vip {
    private String name;

    @Override
    public String toString() {
        return "Vip{" +
                "name='" + name + '\'' +
                '}';
    }

    public Vip(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```

### 构造方法引用

语法：`类名 :: new` 特点：在Lambda表达式的方法体中，返回指定“类名”来创建出来的对象。 要求：创建对象所调用构造方法形参列表 和 函数式接口中的方法的形参列表 保持一致，并且方法的返回值类型和创建对象的类型保持一致。 【示例】实例化Supplier接口的实现类对象，然后调用重写方法返回Teacher对象

```java
package com.powernode.javase.lambda;

import java.util.function.Supplier;

/**
 * ClassName: LambdaTest15
 * Description: 构造方法引用
 *      语法格式：
 *          类名::new
 *      条件：
 *          函数式接口中的方法的形式参数列表
 *          与
 *          构造方法上的形式参数列表
 *          一致。
 *          并且返回值类型相同。
 * <p>
 * Datetime: 2024/2/2 14:09
 * Author: 老杜@动力节点
 * Version: 1.0
 */
public class LambdaTest15 {
    public static void main(String[] args) {
        // 匿名内部类方式
        // 使用生产型的函数式接口
        Supplier<Bird> supplier = new Supplier<Bird>() {
            @Override
            public Bird get() {
                return new Bird();
            }
        };
        System.out.println(supplier.get());

        // Lambda表达式
        Supplier<Bird> supplier1 = () -> new Bird();
        System.out.println(supplier1.get());

        // 使用    构造方法引用    精简
        Supplier<Bird> supplier2 = Bird::new;
        System.out.println(supplier2.get());
    }
}

class Bird {

}

```

【示例】实例化Function接口的实现类对象，然后调用重写方法返回Teacher对象

```java
// 方式一：使用匿名内部类来实现  
Function<String, Teacher> function1 = new Function<String, Teacher>() {  
    @Override  
    public Teacher apply(String name) {  
        return new Teacher(name);  
    }  
};  
System.out.println(function1.apply("ande"));  
  
// 方式二：使用Lambda表达式来实现  
Function<String, Teacher> function2 = name -> new Teacher(name);  
System.out.println(function2.apply("ande"));  
  
// 方式二：使用构造方法引用来实现  
// 注意：根据重写方法的形参列表，那么此处调用了Teacher类name参数的构造方法  
Function<String, Teacher> function3 = Teacher :: new;  
System.out.println(function3.apply("ande"));
```

### 数组引用

语法：`数组类型 :: new` 特点：在Lambda表达式的方法体中，创建并返回指定类型的“数组”。 要求：重写的方法有且只有一个整数型的参数，并且该参数就是用于设置数组的空间长度，并且重写方法的返回值类型和创建数组的类型保持一致。 【示例】实例化Function接口的实现类对象，并在重写方法中返回指定长度的int类型数组

```java
package com.powernode.javase.lambda;

import java.util.Arrays;
import java.util.function.Function;

/**
 * ClassName: LambdaTest17
 * Description: 数组引用
 *          语法格式：
 *              数组::new
 *          条件：
 *              1. 函数式接口中的方法只有一个整数型参数。
 *              2. 这个整数型参数正好是数组的长度。
 *              3. 返回值类型相同。
 * <p>
 * Datetime: 2024/2/2 14:18
 * Author: 老杜@动力节点
 * Version: 1.0
 */
public class LambdaTest17 {
    public static void main(String[] args) {
        // 匿名内部类的方式
        // 转换型函数式接口
        Function<Integer, int[]> function = new Function<Integer, int[]>() {
            @Override
            public int[] apply(Integer integer) {
                return new int[integer];
            }
        };
        int[] nums = function.apply(10);
        System.out.println(Arrays.toString(nums));

        // Lambda表达式
        Function<Integer, int[]> function1 = length -> new int[length];
        nums = function1.apply(20);
        System.out.println(Arrays.toString(nums));

        // 构造方法引用  精简
        Function<Integer, int[]> function2 = int[]::new;
        nums = function2.apply(30);
        System.out.println(Arrays.toString(nums));

    }
}

```

---
## Lambda在集合当中的使用

为了能够让Lambda和Java的集合类集更好的一起使用，集合当中也新增了部分方法，以便与Lambda表达式对接，要用Lambda操作集合就一定要看懂源码。

### forEach()方法

在Collection集合和Map集合中，都提供了forEach()方法用于遍历集合。 在Collection集合中，提供的forEach()方法的形参为Consumer接口（消费型接口），通过该方法再配合Lambda表达式就可以遍历List和Set集合中的元素。 【示例】遍历List集合中的元素

```java
List<Integer> list = Arrays.asList(11, 22, 33, 44, 55);  
// 方式一：使用匿名内部类来实现  
list.forEach(new Consumer<Integer>() {  
    /**  
     * 获得遍历出来的元素  
     * @param element 遍历出来的元素  
     */  
    @Override  
    public void accept(Integer element) {  
        System.out.println(element);  
    }  
});  
  
// 方式二：使用Lambda表达式来实现  
list.forEach(element -> System.out.println(element));  
  
// 方式三：使用方法引用来实现  
list.forEach(System.out :: println);
```

【示例】遍历Set集合中的元素

```java
List<String> list = Arrays.asList("aa", "bb", "cc", "dd");  
HashSet<String> hashSet = new HashSet<>(list);  
// 方式一：使用匿名内部类来实现  
hashSet.forEach(new Consumer<String>() {  
    /**  
     * 获得遍历出来的元素  
     * @param element 遍历出来的元素  
     */  
    @Override  
    public void accept(String element) {  
        System.out.println(element);  
    }  
});  
// 方式二：使用Lambda表达式来实现  
hashSet.forEach(element -> System.out.println(element));  
  
// 方式三：使用方法引用来实现  
hashSet.forEach(System.out :: println);

```

在Map集合中，提供的forEach()方法的形参为BiConsumer接口，而BiConsumer接口属于两个参数的消费型接口，通过该方法再配合Lambda表达式就可以遍历Map集合中的元素。 【示例】遍历Map集合中的元素

```java
// 实例化Map集合并添加键值对  
HashMap<String, String> map = new HashMap<>();  
map.put("张三", "成都");  
map.put("李四", "重庆");  
map.put("王五", "西安");  
// 方式一：使用匿名内部类来实现  
map.forEach(new BiConsumer<String, String>() {  
    /**  
     * 获得遍历出来的key和value  
     * @param key 键  
     * @param value 值  
     */  
    @Override  
    public void accept(String key, String value) {  
        System.out.println("key：" + key + "，value：" + value);  
    }  
});  
// 方式二：使用Lambda表达式来实现  
map.forEach((k, v) -> System.out.println("key：" + k + "，value：" + v));
```

### removeIf()方法

在Collection集合中，提供的removeIf()方法的形参为Predicate接口（判断型接口），通过该方法再配合Lambda表达式就可以遍历List和Set集合中的元素。 【示例】删除List集合中的某个元素

```java
// 创建List集合并添加元素  
List<String> list = new ArrayList<>(Arrays.asList("aa", "bb", "cc", "dd"));  
// 方式一：使用匿名内部类来实现  
list.removeIf(new Predicate<String>() {  
    /**  
     * 删除指定的某个元素  
     * @param element 用于保存遍历出来的某个元素  
     * @return 返回true，代表删除；返回false，代表不删除  
     */  
    @Override  
    public boolean test(String element) {  
        return "bb".equals(element);  
    }  
});  
System.out.println(list); // 输出：[aa, cc, dd]  
  
// 方式二：使用Lambda表达式来实现  
list.removeIf("cc" :: equals);  
System.out.println(list); // 输出：[aa, dd]
```

【示例】删除Set集合中的某个元素

```java
List<String> list = Arrays.asList("aa", "bb", "cc", "dd");  
HashSet<String> hashSet = new HashSet<>(list);  
// 方式一：使用匿名内部类来实现  
hashSet.removeIf(new Predicate<String>() {  
    /**  
     * 删除指定的某个元素  
     * @param element 用于保存遍历出来的某个元素  
     * @return 返回true，代表删除；返回false，代表不删除  
     */  
    @Override  
    public boolean test(String element) {  
        return "bb".equals(element);  
    }  
});  
System.out.println(hashSet); // 输出：[aa, cc, dd]  
  
// 方式二：使用Lambda表达式来实现  
hashSet.removeIf("cc" :: equals);  
System.out.println(hashSet); // 输出：[aa, dd]
```
