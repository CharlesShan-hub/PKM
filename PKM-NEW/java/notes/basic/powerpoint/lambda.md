![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=UoroU&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
# Lambda表达式

---
## 主要内容

1. Lambda表达式的概述
2. Lambda表达式的使用
3. Lambda表达式的方法引用
4. Lambda表达式的在集合中的使用

---
## 学习目标

|**知识点**|**要求**|
|---|---|
|Lambda表达式的概述|理解|
|Lambda表达式的使用|了解|
|Lambda表达式的方法引用|掌握|
|Lambda表达式的在集合中的使用|理解|

---
## Lambda表达式的概述

### Lambda表达式的引入

Lambda表达式是JDK1.8的一个新特性，可以取代大部分的匿名内部类，以便写出更优雅的Java代码，尤其在集合的遍历和其他集合操作中，可以极大地优化代码结构。 在以前的学习中，想要实现对List集合的“降序”排序操作，就需要使用匿名内部类来实现，这样的代码非常的复杂和繁琐，代码如下：

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

针对以上对List集合的的“降序”排序操作，除了使用匿名内部类来实现外，还可以使用Lambda表达式来实现，使用Lambda表达式的代码非常优雅，并且还非常的简洁，代码如下：

// 方式二：使用Lambda表达式来实现  
List<Integer> list = Arrays.asList(3, 6, 1, 7, 2, 5, 4);  
Collections.sort(list, (o1, o2) -> o2 - o1);  
System.out.println("排序后：" + list);
```

### 函数式编程思想的概述

Java从诞生之日起就一直倡导“一切皆对象”，在Java语言中面向对象（OOP）编程就是一切，但是随着Python和Scala等语言的崛起和新技术的挑战，Java也不得不做出调整以便支持更加广泛的技术要求，即Java语言不但支持OOP还支持OOF（面向函数编程）。 JDK1.8引入Lambda表达式之后，Java语言也开始支持函数式编程，但是Lambda表达式不是Java语言最早使用的，目前C++、C#、Python、Scala等语言都支持Lambda表示。

- 面向对象的思想
    
    - 做一件事情，找一个能解决这个事情的对象，然后调用对象的方法，最终完成事情。
        
- 函数式编程思想
    
    - 只要能获得结果，谁去做的，怎么做的都不重要，重视的是结果，不重视实现过程。
        

在函数式编程语言中，函数被当成一等公民对待。在将函数当成一等公民的编程语言中，Lambda表达式的类型是函数，但是Lambda表达式却是一个对象，而不是函数，它们必须依附于一类特别的对象类型，也就是所谓的函数式接口。 简单点说，JDK1.8中的Lambda表达式就是一个函数式接口的实例，这就是Lambda表达式和函数式接口的关系。也就是说，**只要一个对象是函数式接口的实例，那么该对象就可以使用Lambda表达式来表示**。

### 如何去理解函数式接口

能够使用Lambda表达式的一个重要依据是必须有相应的函数式接口，所谓的函数式接口，指的就是“一个接口中有且只能有一个抽象方法”。也就是说，如果一个接口只有一个抽象方法，那么该接口就是一个函数式接口。 如果我们在接口上声明了 @FunctionalInterface 注解，那么编译器就会按照函数式接口的定义来要求该接口，也就是该接口中有且只能定义一个抽象方法，如果该接口中定义了多个或0个抽象方法，则程序编译时就会报错。 【示例】定义一个函数式接口

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

另外，从某种意义上来说，只要你保证你的接口中有且只有一个抽象方法，则接口中没有使用 @FunctionalInterface 注解来标注，那么该接口也依旧属于函数式接口。 在以下代码中，Flyable接口中没有使用@FunctionalInterface 注解，但是Flyable接口中只存在一个抽象方法，因此Flyable接口依旧属于函数式接口，那么使用Lambda表达式就可以表示Flyable 接口的实例，代码如下：

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
        
    - Lambda表达式：只能是接口。
        
- 使用限制不同
    
    - 如果接口中有且仅有一个抽象方法，可以使用Lambda表达式，也可以使用匿名内部类。
        
    - 如果接口中有多个抽象方法，则就只能使用匿名内部类，而不能使用Lambda表达式。
        
- 实现原理不同
    
    - 匿名内部类：编译之后，会生成一个单独的.class字节码文件。
        
    - Lambda表达式：编译之后，没有生成一个单独的.class字节码文件。
        

---
## Lambda表达式的使用

### Lambda表达式的语法

Lambda表达式本质就是一个匿名函数，在函数的语法中包含返回值类型、方法名、形参列表和方法体等，而在Lambda表达式中我们只需要关心形参列表和方法体即可。 在Java语言中，Lambda表达式的语法为“(形参列表) -> {方法体}”，其中“->”为 lambda操作符或箭头操作符，“形参列表”为对应接口实现类中重写方法的形参列表，“方法体”为对应接口实现类中重写方法的方法体。 接下来，我们就以匿名内部类为例，从而将匿名内部类演化为Lambda表达式，代码如下：

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

在以上的匿名内部类中，黄色背景颜色标注的代码都属于不可变的固定代码，而红色背景颜色标注的代码，属于可变的并且是完成该功能的核心代码。因此，将此处的匿名内部类转化为Lambda表达式，我们只需保留红色部分的形参列表和方法体即可，对应的Lambda表达式代码实现如下：

```java
List<Integer> list = Arrays.asList(3, 6, 1, 7, 2, 5, 4);  
Collections.sort(list, (Integer o1, Integer o2) -> {  
    return o2 - o1;  
});  
System.out.println("排序后：" + list);
```

在以上代码中，黄色背景颜色标注的就是重写于Comparator接口中抽象方法的形参列表，而红色背景颜色标注的就是重写方法对应方法体的代码实现。因此Lambda本质上就是去掉了一堆没有意义的代码，只留下核心的代码逻辑，从而让代码看起来更加的简洁且优雅。

### Lambda表达式的使用

#### Lambda表达式的基本使用

接下来，我们以自定义的函数式接口为例，先从匿名对象的实现过程，慢慢演变为Lambda表达式的实现过程。另外，使用Lambda表达式的时候，则必须有上下文环境，才能推导出Lambda对应的接口类型。

##### 无返回值函数式接口

情况一：无返回值无参数

```java
// 情况一：无返回值无参数  
interface NoParameterNoReturn {  
    void test();  
}  
​  
public class Test01 {  
    public static void main(String[] args) {  
        // 方式一：使用匿名内部类来实现  
        NoParameterNoReturn obj1 = new NoParameterNoReturn() {  
            @Override  
            public void test() {  
                System.out.println("无参无返回值");  
            }  
        };  
        obj1.test();  
​  
        // 方式二：使用Lambda表达式来实现  
        NoParameterNoReturn obj2 = () -> {  
            System.out.println("无参无返回值");  
        };  
        obj2.test();  
    }  
}
```

情况二：无返回值一个参数

```java
// 情况二：无返回值一个参数  
interface OneParameterNoReturn {  
    void test(int num);  
}  
​  
public class Test01 {  
    public static void main(String[] args) {  
        // 方式一：使用匿名内部类来实现  
        OneParameterNoReturn obj1 = new OneParameterNoReturn() {  
            @Override  
            public void test(int num) {  
                System.out.println("无返回值一个参数 --> " + num);  
            }  
        };  
        obj1.test(10);  
​  
        // 方式二：使用Lambda表达式来实现  
        OneParameterNoReturn obj2 = (int num) -> {  
            System.out.println("无返回值一个参数 --> " + num);  
        };  
        obj2.test(20);  
    }  
}
```

情况三：无返回值多个参数

```java
// 情况三：无返回值多个参数  
interface MoreParameterNoReturn {  
    void test(String str1, String str2);  
}  
public class Test01 {  
    public static void main(String[] args) {  
        // 方式一：使用匿名内部类来实现  
        MoreParameterNoReturn obj1 = new MoreParameterNoReturn() {  
            @Override  
            public void test(String str1, String str2) {  
                System.out.println(str1 + " : " + str2);  
            }  
        };  
        obj1.test("hello", "world");  
​  
        // 方式二：使用Lambda表达式来实现  
        MoreParameterNoReturn obj2 = (String str1, String str2) -> {  
            System.out.println(str1 + " : " + str2);  
        };  
        obj2.test("你好", "世界");  
    }  
}
```

##### 有返回值函数接口

情况一：有返回值无参数

```java
// 情况一：有返回值无参数  
interface NoParameterHasReturn {  
    int test();  
}  
  
public class Test01 {  
    public static void main(String[] args) {  
        // 方式一：使用匿名内部类来实现  
        NoParameterHasReturn obj1 = new NoParameterHasReturn() {  
            @Override  
            public int test() {  
                return 520;  
            }  
        };  
        System.out.println(obj1.test()); // 输出：520  
  
        // 方式二：使用Lambda表达式来实现  
        NoParameterHasReturn obj2 = () -> {  
            return 1314;  
        };  
        System.out.println(obj2.test()); // 输出：1314  
    }  
}
```

情况二：有返回值一个参数

```java
// 情况二：有返回值一个参数  
interface OneParameterHasReturn {  
    String test(double num);  
}  
  
public class Test01 {  
    public static void main(String[] args) {  
        // 方式一：使用匿名内部类来实现  
        OneParameterHasReturn obj1 = new OneParameterHasReturn() {  
            @Override  
            public String test(double num) {  
                return "传入的小数为：" + num;  
            }  
        };  
        System.out.println(obj1.test(520.0));  
  
        // 方式二：使用Lambda表达式来实现  
        OneParameterHasReturn obj2 = (double num) -> {  
            return "传入的小数为：" + num;  
        };  
        System.out.println(obj2.test(1314.0));  
    }  
}
```

情况三：有返回值多个参数

```java
// 情况三：有返回值多个参数  
interface MoreParameterHasReturn {  
    String test(int num1, int num2);  
}  
public class Test01 {  
    public static void main(String[] args) {  
        // 方式一：使用匿名内部类来实现  
        MoreParameterHasReturn obj1 = new MoreParameterHasReturn() {  
            @Override  
            public String test(int num1, int num2) {  
                return "运算的结果为：" + (num1 + num2);  
            }  
        };  
        System.out.println(obj1.test(10, 20));  
  
        // 方式二：使用Lambda表达式来实现  
        MoreParameterHasReturn obj2 = (int num1, int num2) -> {  
            return "运算的结果为：" + (num1 + num2);  
        };  
        System.out.println(obj2.test(20, 30));  
    }  
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

语法：对象 :: 实例方法 特点：在Lambda表达式的方法体中，通过“对象”来调用指定的某个“实例方法”。 要求：函数式接口中抽象方法的返回值类型和形参列表 与 内部通过对象调用某个实例方法的返回值类型和形参列表 保持一致。 【示例】实例化Consumer接口的实现类对象，并在重写的accept()方法中输出形参的值

```java
// 方式一：使用匿名内部类来实现  
Consumer<String> consumer1 = new Consumer<String>() {  
    @Override  
    public void accept(String str) {  
        System.out.println(str);  
    }  
};  
consumer1.accept("hello world");  
  
// 方式二：使用Lambda表达式来实现  
Consumer<String> consumer2 = str -> System.out.println(str);  
consumer2.accept("hello world");  
  
// 方式三：使用方法引用来实现  
Consumer<String> consumer3 = System.out :: println;  
consumer3.accept("hello world");
```

【示例】实例化Supplier接口的实现类对象，并在重写方法中返回Teacher对象的姓名

```java
Teacher teacher = new Teacher("ande", 18);  
// 方式一：使用匿名内部类来实现  
Supplier<String> supplier1 = new Supplier<String>() {  
    @Override  
    public String get() {  
        return teacher.getName();  
    }  
};  
System.out.println(supplier1.get());  
  
// 方式二：使用Lambda表达式来实现  
Supplier<String> supplier2 = () -> teacher.getName();  
System.out.println(supplier2.get());  
  
// 方式三：使用方法引用来实现  
Supplier<String> supplier3 = teacher :: getName;  
System.out.println(supplier3.get());
```


### 静态方法引用

语法：类 :: 静态方法 特点：在Lambda表达式的方法体中，通过“类名”来调用指定的某个“静态方法”。 要求：函数式接口中抽象方法的返回值类型和形参列表 与 内部通过类名调用某个静态方法的返回值类型和形参列表保持一致。

【示例】实例化Function接口的实现类对象，并在重写的方法中返回小数取整的结果

```java
// 方式一：使用匿名内部类来实现  
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

### 特殊方法引用

语法：类名 :: 实例方法 特点：在Lambda表达式的方法体中，通过方法的第一个形参来调用指定的某个“实例方法”。 要求：把函数式接口中抽象方法的第一个形参作为方法的调用者对象，并且从第二个形参开始（或无参）可以对应到被调用实例方法的参数列表中，并且返回值类型保持一致。 【示例】使用Comparator比较器，来判断两个小数的大小

```java
// 方式一：使用匿名内部类来实现  
Comparator<Double> comparator1 = new Comparator<Double>() {  
    @Override  
    public int compare(Double o1, Double o2) {  
        return o1.compareTo(o2);  
    }  
};  
System.out.println(comparator1.compare(10.0, 20.0));  
  
// 方式二：使用Lambda表达式来实现  
Comparator<Double> comparator2 = (o1, o2) -> o1.compareTo(o2);  
System.out.println(comparator2.compare(10.0, 20.0));  
  
// 方式三：使用方法引用来实现  
Comparator<Double> comparator3 = Double :: compareTo;  
System.out.println(comparator3.compare(10.0, 20.0));
```

需求：实例化Function接口的实现类对象，然后获得传入Teacher对象的姓名。

```java
// 方式一：使用匿名内部类来实现  
Teacher teacher = new Teacher("ande", 18);  
Function<Teacher, String> function1 = new Function<Teacher, String>() {  
    @Override  
    public String apply(Teacher teacher) {  
        return teacher.getName();  
    }  
};  
System.out.println(function1.apply(teacher));  
  
// 方式二：使用Lambda表达式来实现  
Function<Teacher, String> function2 = e -> e.getName();  
System.out.println(function2.apply(teacher));  
  
// 方式三：使用方法引用来实现  
Function<Teacher, String > function3 = Teacher :: getName;  
System.out.println(function3.apply(teacher));
```

### 构造方法引用

语法：类名 :: new 特点：在Lambda表达式的方法体中，返回指定“类名”来创建出来的对象。 要求：创建对象所调用构造方法形参列表 和 函数式接口中的方法的形参列表 保持一致，并且方法的返回值类型和创建对象的类型保持一致。 【示例】实例化Supplier接口的实现类对象，然后调用重写方法返回Teacher对象

```java
// 方式一：使用匿名内部类来实现  
Supplier<Teacher> supplier1 = new Supplier<Teacher>() {  
    @Override  
    public Teacher get() {  
        return new Teacher();  
    }  
};  
System.out.println(supplier1.get());  
  
// 方式二：使用Lambda表达式来实现  
Supplier<Teacher> supplier2 = () -> new Teacher();  
System.out.println(supplier2.get());  
  
// 方式二：使用构造方法引用来实现  
// 注意：根据重写方法的形参列表，那么此处调用了Teacher类的无参构造方法  
Supplier<Teacher> supplier3 = Teacher :: new;  
System.out.println(supplier3.get());
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

语法：数组类型 :: new 特点：在Lambda表达式的方法体中，创建并返回指定类型的“数组”。 要求：重写的方法有且只有一个整数型的参数，并且该参数就是用于设置数组的空间长度，并且重写方法的返回值类型和创建数组的类型保持一致。 【示例】实例化Function接口的实现类对象，并在重写方法中返回指定长度的int类型数组

```java
// 方式一：使用匿名内部类来实  
Function<Integer, int[]> function1 = new Function<Integer, int[]>() {  
    @Override  
    public int[] apply(Integer integer) {  
        return new int[integer];  
    }  
};  
System.out.println(Arrays.toString(function1.apply(10)));  
  
// 方式二：使用Lambda表达式来实现  
Function<Integer, int[]> function2 = num -> new int[num];  
System.out.println(Arrays.toString(function2.apply(20)));  
  
// 方式三：使用方法引用来实现  
Function<Integer, int[]> function3 = int[] :: new;  
System.out.println(Arrays.toString(function3.apply(30)));
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

【示例】遍历Set集合中的元素

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

在Map集合中，提供的forEach()方法的形参为BiConsumer接口，而BiConsumer接口属于两个参数的消费型接口，通过该方法再配合Lambda表达式就可以遍历Map集合中的元素。 【示例】遍历Map集合中的元素

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
