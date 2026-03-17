# 注解
---
## 概述
什么是注解？
* 注解是JDK1.5才引入的。
* 注解可以标注在 类上，属性上，方法上 等。
* 注解可以做到在不改变代码逻辑的前提下在代码中嵌入补充信息。

注解与注释
* 注**释**：给程序员看的，编译器编译时会忽略注释。
* 注**解**：给编译器看的，或给其它程序看的，程序根据有没有这个注解来决定不同的处理方式。

注解的重要性
* 框架是如何实现的：**框架 = 反射 + 注解 + 设计模式**。


---
## JDK 内置的基本注解类型

1. `@Override`
    1. 只能用于重写父类的方法
    2. 如果写了`@Override`编译器会去验证是否构成了重载，如果没写，就按默认执行。
2. `@Deprecated`：某个类或者成员过时了
    ```java
    package com.powernode.javase.annotation;  
      
    /**  
     * JDK的内置注解：@Deprecated  
     * 1. 被这个注解标注的元素已过时。  
     * 2. 这个注解是给编译器看的。编译器看到这个注解之后会有警告提示信息。  
     * 3. 经过测试 @Deprecated 注解可以标注的元素很多，例如：类上，方法上，属性上....  
     */public class AnnotationTest01 {  
        public static void main(String[] args) {  
            MyClass1 myClass1 = new MyClass1();  
            System.out.println(myClass1.num);  
            myClass1.doSome();  
        }  
    }  
      
    // 标注这个类已过时，不建议使用了  
    @Deprecated  
    class MyClass1 {  
      
        // since属性值表示从哪个版本开始已过时。  
        // forRemoval属性值如果是true表示已移除。  
        @Deprecated(since = "9", forRemoval = true)  
        public int num = 100;  
      
        @Deprecated  
        public void doSome(){  
      
        }  
    }
    ```
3. `@SuppressWarnings`：抑制警告
    1. `@SuppressWarnings` 注解是 Java 编程语言中的一个特性，它用于抑制编译器生成的警告信息。这个注解可以应用于类型、字段、方法、参数、构造函数以及局部变量声明。下面是 `@SuppressWarnings` 支持的所有警告类型（也称为注解的值）的总结：  
    2. @SuppressWarnings("rawtypes")：抑制未使用泛型的警告
    3. @SuppressWarnings("resource")：抑制未关闭资源的警告
    4. @SuppressWarnings("deprecation")：抑制使用了已过时资源时的警告
    5. @SuppressWarnings("all")：抑制所有警告
    6. 可以单独使用这些值，或者将它们组合起来传递给 `@SuppressWarnings` 注解，以抑制多种类型的警告。例如： 
    ```java  
    @SuppressWarnings({"unchecked", "rawtypes"})  
    public void myMethod() {  
        // 方法实现，这里可能会有未检查的转换或未指定泛型参数的警告  
    }  
    ```  
    7. 可以通过标在不同的地方，表示不同的作用域
    ```java  
    package ex_at;  
    
    import java.util.ArrayList;  
    
    public class Test {  
        public static void main(String[] args){  
            @SupressWarnings({"rawypes"})
            List list = new ArrayList();  
            list.add("Jack");  
            @SupressWarnings({"unused"})
            int i;  
            System.out.println(list.get(1));  
        }
    
        @SupressWarnings({"all"})
        public static void main(String[] args){  
            List list = new ArrayList();  
            list.add("Jack");  
            int i;  
            System.out.println(list.get(1));  
        }
    }  
    ```  
4. `@FunctionalInterface`
    1. 函数式接口”的注解，这个是 JDK1.8 版本引入的新特性。
    2. 使用@FunctionalInterface标注的接口，则该**接口就有且只能存在一个抽象方法**，否则就会发生编译错误。（注意：接口中的默认方法或静态方法可以有多个。）
```java
package com.powernode.javase.annotation;  
  
/**  
 * 关于Java内置注解：@FunctionalInterface  
 *      1. 这个注解是专门用来标注接口的。  
 *      2. 被标注的接口必须是一个函数式接口，如果不是函数式接口，则编译器报错。  
 *      3. 这个注解也是给编译器看的。  
 *      4. 什么是函数式接口？  
 *          如果这个接口中抽象方法只有一个（有且仅有一个）。称为函数式接口。  
 *      5. 被 @FunctionalInterface 标注的接口中，允许有多个默认方法和静态方法。  
 */  
public class AnnotationTest04 {  
}  
  
@FunctionalInterface  
interface Flyable {  
    void fly();  
  
    //void run();  
  
    default void run(){  
        System.out.println("默认方法是可以的");  
    }  
  
    static void doSome(){  
        System.out.println("静态方法");  
    }  
}
```
---
## 自定义注解
自定义注解
* 使用 @interface 来定义注解。
* 默认情况下注解可以出现在类上、方法上、属性上、构造方法上、方法参数上等......
* 所有自定义的注解，它的父类是：java.lang.annotation.Annotation
```java
package com.powernode.javase.annotation;  
  
/**  
 * 自定义的注解。（以下这是注解的定义过程！！！！！）  
 */  
public @interface MyAnnotation {  
}
```

```java
package com.powernode.javase.annotation;  
  
/**  
 * 以下是使用注解的过程！！！！！！  
 */  
@MyAnnotation  
public class AnnotationTest05 {  
    @MyAnnotation  
    private String name;  
  
    @MyAnnotation  
    public void doSome(){  
  
    }  
  
    public void doOther(@MyAnnotation String name, @MyAnnotation String password){  
  
    }  
  
    public void toDo(  
            @MyAnnotation  
            String name,  
            @MyAnnotation  
            String password){  
  
    }  
}
```

注解也可以定义属性
* 注解也可以定义属性，不过属性定义时，属性名后面必须加一个小括号。
* 属性的类型只能是：
    * byte，short，int，long，float，double，boolean，char，String、Class、枚举类型、注解类型
    * 以上所有类型的一维数组形式
```java
package com.powernode.javase.annotation;  
  
/**  
 * 这是一个数据库信息的注解（自定义的注解）  
 */  
public @interface DataBaseInfo {  
    /**  
     * 注解也可以定义属性，但是属性定义时有要求，属性名后面必须添加：()  
     * 语法：  
     *      属性的类型 属性的名字();  
     */    
     String driver() default "com.mysql.cj.jdbc.Driver"; // 使用 default 关键字来指定属性的默认值。  
    String url();  
    String user();  
    String password();  
  
    byte b() default 0;  
    short s() default 0;  
    int i() default 0;  
    long l() default 0L;  
    float f() default 0.0F;  
    double d() default 0.0;  
    boolean flag() default false;  
    char c() default '0';  
    Class clazz() default String.class;  
    Season season() default Season.SPRING;  
    MyAnnotation myAnnotation();  
  
    /**  
     * 可以是一维数组形式  
     * @return  
     */  
    String[] names();  
  
    // 注解的属性的数据类型，必须是以上的几种类型，或者这几种类型的一维数组，不能是其他类型。  
    //Object obj();  
}
```

```java
package com.powernode.javase.annotation;  
  
/**  
 * 使用自定义的注解：@DataBaseInfo  
 */public class AnnotationTest06 {  
  
    // 语法规则：如果这个注解中有属性，那么使用的时候，必须给属性赋值。没有赋值则报错。  
    // 除非你定义注解的时候给属性指定了默认值。  
    // 怎么给属性赋值？语法：@DataBaseInfo(属性名=值,属性名=值,属性名=值,属性名=值,属性名=值)  
    @DataBaseInfo(  
            //driver="oracle.jdbc.driver.OracleDriver",  
            url="jdbc:mysql://localhost:3306/powernode",  
            user="root",  
            password="123456",  
            myAnnotation=@MyAnnotation,  
            names={"zhangsan", "lisi", "wangwu"},  
            flag=true,  
            i=100,  
            clazz=Integer.class,  
            season=Season.WINTER)  
    public void connDB(){  
  
    }  
  
}
```

注解的使用
* 注解在使用时必须给属性赋值，除非你使用了default关键字为属性指定了默认值。
* 如果属性只有一个，并且属性名是value时，使用注解时value可以省略不写。
* 如果属性是一个数组，使用注解时，数组值只有一个，数组的大括号是可以省略的。

```java
package com.powernode.javase.annotation;  
  
public @interface Table {  
  
    /**  
     * 有一个属性，并且这个属性的名字是value  
     */    
    //String value();  
    String[] value();  
}
```

```java
package com.powernode.javase.annotation;  
  
//@Table(value="t_user")  
// 如果属性名是value的话， 在使用注解的时候，该属性名可以省略。  
//@Table("t_user")  
//@Table(value={"t_user1", "t_user2"})  
// value可以省略。  
//@Table({"t_user1", "t_user2"})  
//@Table({"t_user"})  
@Table("t_user")  
public class AnnotationTest07 {  
  
    @SuppressWarnings("all")  
    public static void main(String[] args) {  
  
    }  
}
```

---
## 元注解：对注解进行注解

元注解的种类（使用不多，了解，不用深入研究）
1) Retention // 指定注解的作用范围，三种 SOURCE, CLASS, RUNTIME  
2) Target // 指定注解可以在哪些地方使用  
3) Documented // 指定该注解是否会在 javadoc 体现  
4) Inherited // 子类会继承父类注解  

比如 Deprecated 的源码

```java
@Documented  
@Retention(RetentionPolicy.RUNTIME)  
@Target(value={CONSTRUCTOR, FIELD, LOCAL_VARIABLE, METHOD, PACKAGE, MODULE, PARAMETER, TYPE})  
public @interface Deprecated {  
    /**  
     * Returns the version in which the annotated element became deprecated.     
     * The version string is in the same format and namespace as the value of     
     * the {@code @since} javadoc tag. The default value is the empty  
     * string.     
     *     
     * @return the version string  
     * @since 9  
     */    
     String since() default "";  
  
    /**  
     * Indicates whether the annotated element is subject to removal in a     
     * future version. The default value is {@code false}.  
     *     
     * @return whether the element is subject to removal  
     * @since 9  
     */    
     boolean forRemoval() default false;  
}
```

用来标注注解的注解叫做元注解。(也是JDK内置的注解。)
常用的元注解：
@Retention：设置注解的保持性
@Target：设置注解可以出现的位置
@Documented：设置注解是否可以生成到帮助文档中
@Inherited：设置注解是否支持继承
@Repeatable：设置注解在某一个元素上是否可以重复使用（Java8的新特性。）

### @Retention
Retention英文意思有保留、保持的意思，它表示注解存在阶段是保留在源代码（编译期），字节码（类加载）或者运行时（JVM中运行）。
在@Retention注解中使用枚举RetentionPolicy来表示注解保留时期。
@Retention(RetentionPolicy.SOURCE)：注解仅存在于源代码中，在字节码文件中不包含。
@Retention(RetentionPolicy.CLASS)：注解在字节码文件中存在，但运行时无法获得（默认）。
@Retention(RetentionPolicy.RUNTIME)：注解在字节码文件中存在，且运行时可通过反射获取。

```java
package com.powernode.javase.annotation.meta1;  
  
import java.lang.annotation.Annotation;  
import java.lang.annotation.Retention;  
import java.lang.annotation.RetentionPolicy;  


@MyAnnotation // 这个注解会被保留到字节码中，并且在运行时可以被反射。  
public class Test {  
  
    public static void main(String[] args) {  
  
        // 获取这个类  
        Class<Test> testClass = Test.class;  
  
        // 获取这个类上的注解  
        //MyAnnotation annotation = testClass.getAnnotation(MyAnnotation.class);  
        // java.lang.annotation.Annotation是所有注解的老祖宗。  
        Annotation annotation = testClass.getAnnotation(MyAnnotation.class);  
  
        System.out.println(annotation);  
    }  
}

//@Retention(value= RetentionPolicy.SOURCE) // @MyAnnotation 注解保留在源码中。  
//@Retention(value= RetentionPolicy.CLASS) // @MyAnnotation 注解保留在字节码中，这是默认的行为，但不能被反射。  
//@Retention(value= RetentionPolicy.RUNTIME) // @MyAnnotation 注解保留在字节码中，并且在运行时可以被反射。  
@Retention(RetentionPolicy.SOURCE)  
@interface MyAnnotation {  
}
```
### @Target
用于描述注解可以使用的位置，该注解使用ElementType枚举类型用于描述注解可以出现的位置，
ElementType有如下枚举值：
@Target(ElementType.TYPE)：作用于接口、类、枚举、注解
@Target(ElementType.FIELD)：作用于属性、枚举的常量
@Target(ElementType.METHOD)：作用于方法
@Target(ElementType.PARAMETER)：作用于方法参数
@Target(ElementType.CONSTRUCTOR)：作用于构造方法
@Target(ElementType.LOCAL_VARIABLE)：作用于局部变量
@Target(ElementType.ANNOTATION_TYPE)：作用于注解
@Target(ElementType.PACKAGE)：作用于包
@Target(ElementType.TYPE_PARAMETER)：作用于泛型，即泛型方法、泛型类和泛型接口。 
@Target(ElementType.TYPE_USE)：作用于任意类型。

```java
package com.powernode.javase.annotation.meta2;  

import java.lang.annotation.ElementType;  
import java.lang.annotation.Target;  

@MyAnnotation  
public class Test {  
  
    @MyAnnotation  
    int num = 100;  
  
    @MyAnnotation  
    public static void main(String[] args) {  
  
    }  
}
  
//@Target(value={ElementType.METHOD})  
//@Target(ElementType.METHOD) // 限定注解只能出现在方法上  
@Target({ElementType.METHOD, ElementType.TYPE, ElementType.FIELD})  
@interface MyAnnotation {  
}
```

### @Documented
Documented的英文意思是文档。使用javadoc.exe工具可以从程序源代码中抽取类、方法、属性等注释形成一个源代码配套的API帮助文档，而该工具抽取时默认不包括注释内容。如果使用的注解被@Documented标注，那么该注解就能被javadoc.exe工具提取到API文档。

### @Inherited
Inherited的英文意思是继承，但是这个继承和我们平时理解的继承大同小异，一个被@Inherited注解了的注解修饰了一个父类，则它的子类也继承了父类的注解。

### @Repeatable
Repeatable表示可重复的含义，该注解属于JDK1.8版本的新特性。


