# 枚举

---
## 引入枚举类

我们现在用一个例子引入枚举类。我们要创建`Season`类，并且得到`spring`，`summer`，`autumn`，`winter`四个变量。我们会从手动创建逐步引出`enum`。

1. 👉 [enum-demo-01](../../../details/enum-demo-01.md)：创建`Season`类实现枚举。但这样有个缺点，我们没办法限制实例化的变量的内容，我们可以创建春夏秋冬，但也可以创建白天黑夜，这与季节的设计初衷违背。
2. 👉 [enum-demo-02](../../../details/enum-demo-02.md)：使用**单例设计模式**实现枚举。这样解决了限制实例化的变量的内容的需求。
3. 👉 [enum-demo-03](../../../details/enum-demo-03.md)：使用`enum`关键字实现枚举。java为了简化这种单例设计模式，引入了枚举。

---
## enum的细节

1. 通过反编译(javap)，可以证明`enum`和`public static final` 其实是一样的。👉 [enum-javap](../../../details/enum-javap.md)
2. 如果枚举定义的时候，并不需要参数，这样写
	```java
	enum Season{  
	  SPRING, SUMMER, AUTUMN, WINTER;
   }
	```
3. 用 `enum` 的话，必须放在类的最前边。
4. 使用`System.out.println`枚举对象调用的是`java.lang.Enum`的 `toString`。
	```java
	enum Gender{
	  BOY, GRIL;
	}
	Gender b1 = Gender.BOY;
	Gender b2 = Gender.BOY;
	System.out.println(boy); 
	// boy.toString() -> 调用的是java.lang.Enum的 toString
	System.out.println(boy1 == boy2); // true
	```
	
	```java
	// java.lang.Enum的 toString
	public String toString(){
	  return name;  // 所以这个题输出 BOY
	}
	```

---
## enum常用方法

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
| clone             | **枚举类型不能被 Clone**。为了防止子类实现克隆方法，Enum 实现了一个仅抛出 CloneNotSupportedException 异常的不变 Clone()。                                |
👉 [enum-api](../../../details/enum-api.md)
👉 [enum-clone-exception](../../../details/enum-clone-exception.md)
