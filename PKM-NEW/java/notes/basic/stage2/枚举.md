# 枚举

---
## 枚举介绍

创建 Season 对象
```java
package ex_enum;  
  
public class Test {  
    public static void main(String[] args){  
        Season spring = new Season("春天", "当第一株小草🪴发芽，我在想你");  
        Season summer = new Season("夏天", "当第一声蝉鸣🌳划过，我在想你");  
        Season autumn = new Season("秋天", "当第一棵树木🍁变黄，我在想你");  
        Season winter = new Season("冬天", "当第一片雪花❄️飘落，我在想你");  
        Season night  = new Season("黑天", "当太阳褪去光辉✨，我在想你");  
        Season day    = new Season("白天", "当星星沉入海底☀️，我在想你");  
  
        // 这样不能提现对象的有限性，所以需要枚举  
        // 思念跨越时间，而我只有四季  
    }  
}  
  
class Season{  
    private String name;  
    private String decs;  
    public Season(String name, String decs){  
        this.name = name;  
        this.decs = decs;  
    }  
    public String getDecs() {  
        return decs;  
    }  
    public String getName() {  
        return name;  
    }  
    public void setName(String name) {  
        this.name = name;  
    }  
    public void setDecs(String decs) {  
        this.decs = decs;  
    }
}
```

---
## 自定义类实现枚举

```java
package ex_enum;  
  
public class Test {  
    public static void main(String[] args){  
        System.out.println(Season.SPRING); // 没有你的春天，那便沉沉睡去...  
        System.out.println(Season.SUMMER); // 没有你的夏天，那便沉沉睡去...  
        System.out.println(Season.AUTUMN); // 没有你的秋天，那便沉沉睡去...  
        System.out.println(Season.WINTER); // 没有你的冬天，那便沉沉睡去...  
    }  
}  
  
class Season{  
    private String name;  
    private String decs;  
  
    public final static Season SPRING = new Season("春天","春困");  
    public final static Season SUMMER = new Season("夏天","夏打盹");  
    public final static Season AUTUMN = new Season("秋天","秋乏");  
    public final static Season WINTER = new Season("冬天","冬三月");  
    // 1. 将构造器私有化, 目的防止直接 new    
    // 2. 去掉 setter，防止属性被篡改  
    // 3. 在 Season 内部，直接创建固定的对象  
    // 4. 还可以加入 final，优化一下性能  
    private Season(String name, String decs){  
        this.name = name;  
        this.decs = decs;  
    }  
    @Override  
    public String toString(){  
        return "没有你的"+this.name+"，那便沉沉睡去...";  
    }  
    public String getDecs() {  
        return decs;  
    }  
    public String getName() {  
        return name;  
    }  
  
}
```

---
## enum 关键字实现枚举

```java
package ex_enum;  
  
public class Test {  
    public static void main(String[] args){  
        System.out.println(Season.SPRING); // 没有你的春天，那便沉沉睡去...  
        System.out.println(Season.SUMMER); // 没有你的夏天，那便沉沉睡去...  
        System.out.println(Season.AUTUMN); // 没有你的秋天，那便沉沉睡去...  
        System.out.println(Season.WINTER); // 没有你的冬天，那便沉沉睡去...  
    }  
}  
  
enum Season{  
    // 1. 使用关键字 enum 替代 class    // 2. 定义的对象，使用名称替代  
    // 3. 把属性定义放到后边  
    // 4. 多个对象使用对象间  
    SPRING("春天","春困"),  
    SUMMER("夏天","夏打盹"),  
    AUTUMN("秋天","秋乏"),  
    WINTER("冬天","冬三月");  
    // public final static Season SPRING = new Season("春天","春困");  
    // public final static Season SUMMER = new Season("夏天","夏打盹");  
    // public final static Season AUTUMN = new Season("秋天","秋乏");  
    // public final static Season WINTER = new Season("冬天","冬三月");  
  
    private String name;  
    private String decs;  
  
    private Season(String name, String decs){  
        this.name = name;  
        this.decs = decs;  
    }  
    @Override  
    public String toString(){  
        return "没有你的"+this.name+"，那便沉沉睡去...";  
    }  
    public String getDecs() {  
        return decs;  
    }  
    public String getName() {  
        return name;  
    }  
}
```

enum的细节
1. 通过反编译(javap)，可以看到上边的季节类型如下
	```java
	// 可以看到这是一个 final 类所以不能有子类了，但是可以弄接口
	// 也可以发现， Season 默认继承了 Enum
	final class ex_enum.Season extends java.lang.Enum<ex_enum.Season>{
	    // 我们用 enum 定义的和 publicstatic final 其实是一样的
		public static final ex_enum.Season SPRING; 
		public static final ex_enum.Season SUMMER;
		public static final ex_enum.Season AUTUMN;
		public static final ex_enum.Season WINTER;
		public static ex_enum.Season[] values(); // 可以看到这里有一个方法
		public static ex_enum.Season valueOf(java.lang.String);
		public java.lang.String getName();
		public java.lang.String getDesc();
		public java.lang.String toString();
		static {};
	}
	```
2. 如果枚举定义的时候，并不需要参数，这样写
	```java
	enum Season{  
	    SPRING, SUMMER, AUTUMN, WINTER;
    }
	```
3. 用 enum 的话，必须放在类的最前边

练习

```java
enum Gender{
	BOY, GRIL;
}
Gender b1 = Gender.BOY;
Gender b2 = Gender.BOY;
System.out.println(boy); // boy.toString() -> 调用的是java.lang.Enum的 toString
System.out.println(boy1 == boy2); // trye
```

```java
// java.lang.Enum的 toString
public String toString(){
	return name;  // 所以这个题输出 BOY
}
```

enum常用方法（GPT）

| 方法名               | 详细描述                                                                                                                  |
| ----------------- | --------------------------------------------------------------------------------------------------------------------- |
| valueOf           | 传递枚举类型的 Class 对象和枚举常量名称给静态方法 valueOf，会得到与参数匹配的枚举常量。                                                                   |
| toString          | 得到当前枚举常量的名称。你可以通过重写这个方法来使得得到的结果更易读。                                                                                   |
| equals            | 在枚举类型中可以直接使用 `==` 来比较两个枚举常量是否相等。Enum 提供的这个 equals() 方法，也是直接使用 `==` 实现的。它的存在是为了在 Set、List 和 Map 中使用。注意，equals() 是不可变的。 |
| hashCode          | Enum 实现了 hashCode() 来和 equals() 保持一致。它也是不可变的。                                                                         |
| getDeclaringClass | 得到枚举常量所属枚举类型的 Class 对象。可以用它来判断两个枚举常量是否属于同一个枚举类型。                                                                      |
| name              | 得到当前枚举常量的名称。建议优先使用 toString()。                                                                                        |
| ordinal           | 得到当前枚举常量的次序。                                                                                                          |
| compareTo         | 枚举类型实现了 Comparable 接口，这样可以比较两个枚举常量的大小（按照声明的顺序排列）。                                                                     |
| clone             | 枚举类型不能被 Clone。为了防止子类实现克隆方法，Enum 实现了一个仅抛出 CloneNotSupportedException 异常的不变 Clone()。                                    |

案例：

```java
enum Color {
    RED, GREEN, BLUE;
}

public class EnumExample {
    public static void main(String[] args) {
        Color myColor = Color.RED;

        // 使用 valueOf 获取枚举常量
        Color color = Enum.valueOf(Color.class, "RED");
        System.out.println("ValueOf: " + color);//ValueOf: RED

        // 使用 toString 获取枚举常量名称
        System.out.println("ToString: " + myColor.toString());//ToString: RED

        // 使用 equals 比较两个枚举常量
        if (myColor.equals(color)) {
            System.out.println("The colors are the same.");//The colors are the same.
        }

        // 使用 hashCode 和 equals 保持一致
        int hashCode = myColor.hashCode();
        System.out.println("HashCode: " + hashCode);//HashCode: 1867083167

        // 获取 Class 对象
        Class<? extends Color> colorClass = myColor.getDeclaringClass();
        System.out.println("Class: " + colorClass);//Class: class ex_enum.Color

        // 使用 name 获取枚举常量名称
        System.out.println("Name: " + myColor.name());//Name: RED

        // 使用 ordinal 获取枚举常量的次序
        int ordinal = myColor.ordinal();
        System.out.println("Ordinal: " + ordinal);//Ordinal: 0

        // 使用 compareTo 比较枚举常量
        int comparison = myColor.compareTo(Color.GREEN);
        System.out.println("Comparison: " + comparison);//Comparison: -1

        // 尝试克隆枚举常量
        try {
           Color clonedColor = myColor.clone();
       } catch (CloneNotSupportedException e) {
           System.out.println("Clone not supported: " + e.getMessage());
       }
    }
}
```

在这个案例中，我们定义了一个名为 `Color` 的枚举类型，并演示了如何使用枚举的各种方法，包括 `valueOf`、`toString`、`equals`、`hashCode`、`getDeclaringClass`、`name`、`ordinal` 和 `compareTo`。此外，我们还尝试克隆一个枚举常量，以展示 `CloneNotSupportedException` 的异常。

练习，声明 Week 枚举类，定义周一到周日，用  增强 for 循环
```java
package ex_enum;  
  
enum Week{  
    MONDAY("星期一"),TUESDAY("星期二"),WEDNESDAY("星期三"),
    THURSDAY("星期四"),FRIDAY("星期五"),SATURDAY("星期六"),
    SUNDAY("星期日");  
    private String name;  
    Week(String name){  
        this.name = name;  
    }    @Override  
    public String toString(){  
        return name;  
    }
}  
  
public class TestWeek {  
    public static void main(String[] args){  
        for(Week weekday: Week.values())  
            System.out.println(weekday);  
        //星期一  
        //星期二  
        //星期三  
        //星期四  
        //星期五  
        //星期六  
        //星期日  
    }  
}
```
