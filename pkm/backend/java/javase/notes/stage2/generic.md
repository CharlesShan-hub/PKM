# 泛型

---
## 泛型的引出

```java
public class Demo{
	public static void main(String[] args){
		ArrayList a = new ArrayList();
		a.push(new Cat("a"));
		a.push(new Cat("b"));
		a.push(new Dog("c")); // ops!!! goes wrong!
	}
	for(Object o: a){
		(Cat)o.miao(); // Dog is not Cat
	}
}
```

所以我们需要，泛型

```java
public class Demo{
	public static void main(String[] args){
		//ArrayList<Cat> a = new ArrayList<Cat>();
		ArrayList<Cat> a = new ArrayList<>(); // java7开始后边可以不写类型
		a.push(new Cat("a"));
		a.push(new Cat("b"));
		a.push(new Dog("c")); // 编译报错
	}
}
```

---
## 泛型的擦除与补偿

1. 泛型的出现提高了编译时的安全性，正因为编译时对添加的数据做了检查，则程序运行时才不会抛出类型转换异常。因此**泛型本质上是编译时期的技术**，是专门给编译器用的。**加载类的时候，会将泛型擦除掉**（擦除之后的类型为Object类型），这个称为泛型擦除。
2. 为什么要有泛型擦除呢？其本质是为了**让JDK1.4和JDK1.5能够兼容同一个类加载器**。在JDK1.5版本中，程序编译时期会对集合添加的元素进行安全检查，如果检查完是安全的、没有错误的，那么就意味着添加的元素都属于同一种数据类型，则加载类时就可以把这个泛型擦除掉，将泛型擦除后的类型就是Object类，这样擦除之后的代码就与JDK1.4的代码一致。
3. 由于加载类的时候，会默认将类中的泛型擦除为Object类型，所以添加的元素就被转化为Object类型，同时取出的元素也默认为Object类型。而我们获得集合中的元素时，按理说取出的元素应该是Object类型，为什么取出的元素却是实际添加的元素类型呢？
4. 这里又做了一个默认的操作，我们称之为泛型的补偿。在**程序运行时，通过获取元素的实际类型进行强转，这就叫做泛型补偿（不必手动实现强制转换）**。获得集合中的元素时，虚拟机会根据获得元素的实际类型进行向下转型，也就是会恢复获得元素的实际类型，因此我们就无需手动执行向下转型操作，从本质上避免了抛出类型转换异常。

---
## 使用泛型

1. 实例化

	```java
	List<String> strList = new ArrayList<String>();
	Iterator<Customer> iterator = customers.iterator();
	```
2. Demo
	  ```java
	  package ex_generic;
	  
	  import lombok.AllArgsConstructor;
	  import lombok.Getter;
	  import lombok.Setter;
	  
	  import java.util.HashMap;
	  import java.util.Iterator;
	  import java.util.Map;
	  import java.util.Set;
	  
	  public class Demo01 {
	    public static void main(String[] args) {
	      HashMap<String,Student> map = new HashMap<>();
	      map.put("Tom",new Student("Charles",10));
	      map.put("Jerry",new Student("Bob",20));
	  
	      Set<Map.Entry<String, Student>> s = map.entrySet();
	      Iterator<Map.Entry<String, Student>> iterator1 = s.iterator();
	    }
	  }
	  
	  @Setter
	  @Getter
	  @AllArgsConstructor
	  class Student {
	    private String name;
	    private int age;
	  }
	```
3. 注意：泛型只能是**引用类型**，不能是基本类型
	```java
	List<Integer> l1 = new List<Integer>(); // 可以
	List<int> l1 = new List<int>(); // 不可以❌
	```
4. 不写泛型就默认是 `Object`
	```java
	ArrayList a = new ArrayList();
	//等价于
	ArrayList<Object> a = new ArrayList<>();
	```
5. 前边的类型可以后边是子类（其实很好理解，默认是`Object`时，一切都是`Object`的子类）
	```java
	package ex_generic;
	
	import java.util.ArrayList;
	
	public class Demo02 {
	  public static void main(String[] args) {
	    ArrayList<Father> a1 = new ArrayList<>();
	    a1.add(new Father());
	    ArrayList<Father> a2 = new ArrayList<>();
	    a1.add(new Child());
	    ArrayList<Father> a3 = new ArrayList<>();
	    // a1.add(new Other());  // wrong
	  }
	}
	
	class Father{}
	class Child extends Father{}
	class Other{}
	```
6. 例题，定义 Employee 类：
	1. **包含成员变量**：
	    - `private` 成员变量：`name`（姓名），`sal`（薪水），`birthday`（生日，`MyDate` 类的对象）
	2. **属性访问方法**：
	    - 为每个属性定义 `getter` 和 `setter` 方法
	3. **重写 toString 方法**：
	    - 输出 `name`、`sal`、`birthday`
	4. **MyDate 类**：
	    - 包含 `private` 成员变量：`month`（月份），`day`（日），`year`（年）
	    - 为每个属性定义 `getter` 和 `setter` 方法
	5. **创建对象并排序**：
	    - 创建该类的 3 个对象
	    - 将这些对象放入 `ArrayList` 集合中（需使用泛型定义）
	    - 对集合中的元素进行排序，并遍历输出
	6. 排序方式
	- 调用 `ArrayList` 的 `sort` 方法
	- 传入 `Comparator` 对象（使用泛型）
	    - 先按照 `name` 排序
	    - 如果 `name` 相同，则按生日日期的先后排序（即：定制排序）

	```java
	package ex_generic;
	
	import lombok.AllArgsConstructor;
	import lombok.Getter;
	import lombok.Setter;
	import lombok.ToString;
	
	import java.util.ArrayList;
	import java.util.Comparator;
	import java.util.Iterator;
	
	public class Demo03 {
	  public static void main(String[] args) {
	    ArrayList<Employee> employees = new ArrayList<>();
	    employees.add(new Employee("Jack",18000, new Birthday(1999,10,5)));
	    employees.add(new Employee("Tom",19000, new Birthday(1999,10,6)));
	    employees.add(new Employee("Peter",20000, new Birthday(2010,1,1)));
	    employees.add(new Employee("Jack",18000, new Birthday(1999,10,6)));
	    employees.add(new Employee("Tom",19000, new Birthday(1999,11,6)));
	    employees.add(new Employee("Peter",20000, new Birthday(2010,2,1)));
	    employees.sort(new Comparator<Employee>() {
	      @Override
	      public int compare(Employee o1, Employee o2) {
	        if(o1 == null || o2 == null)
	          throw new NullPointerException();
	        int res = o1.getName().compareTo(o2.getName());
	        return res==0?o1.getBirthday().compareTo(o2.getBirthday()):res;
	      }
	    });
	    Iterator<Employee> iterator = employees.iterator();
	    while (iterator.hasNext()) {
	      Employee employee = iterator.next();
	      System.out.println(employee);
	    }
	    //Employee(name=Jack, salary=18000, birthday=Birthday(year=1999, month=10, day=6))
	    //Employee(name=Jack, salary=18000, birthday=Birthday(year=1999, month=10, day=5))
	    //Employee(name=Peter, salary=20000, birthday=Birthday(year=2010, month=2, day=1))
	    //Employee(name=Peter, salary=20000, birthday=Birthday(year=2010, month=1, day=1))
	    //Employee(name=Tom, salary=19000, birthday=Birthday(year=1999, month=11, day=6))
	    //Employee(name=Tom, salary=19000, birthday=Birthday(year=1999, month=10, day=6))
	  }
	}
	
	@Setter
	@Getter
	@AllArgsConstructor
	@ToString
	class Employee{
	  private String name;
	  private int salary;
	  private Birthday birthday;
	}
	
	@Setter
	@Getter
	@AllArgsConstructor
	@ToString
	class Birthday implements Comparable<Birthday> {
	  private int year;
	  private int month;
	  private int day;
	  @Override
	  public int compareTo(Birthday o) {
	    if(o==null)
	      throw new NullPointerException();
	    if(this.year==o.year && this.month==o.month && this.day==o.day)
	      return 0;
	    if(this.year<o.year)
	      return 1;
	    if(this.month<o.month)
	      return 1;
	    if (this.day<o.day)
	      return 1;
	    return -1;
	  }
	}
	```

---
## 自定义泛型类/接口

1. 定义泛型类时，可以在类名后面使用尖括号 `<T, R...>` 来指定泛型类型参数，其中 `T` 和 `R` 是类型参数的名称，`...` 表示可以有多个泛型成员。
  ```java
  class 类名<T, R...> {
  // 类体
  }
  
  interface 接口名<T, R...> {
  // ...
  }
  ```

2. **普通成员使用泛型**：类的属性和方法可以使用泛型类型参数.
  ```java
  class Box<T> {
    private T t;
  
    public void set(T t) {
      this.t = t;
    }
  
    public T get() {
      return t;
    }
  
    public static void main(String[] args) {
      Box<Integer> integerBox = new Box<>();
      integerBox.set(123);
      System.out.println(integerBox.get());
  
      Box<String> stringBox = new Box<>();
      stringBox.set("Hello, World!");
      System.out.println(stringBox.get());
    }
  }
  ```

3. **泛型数组初始化限制**：不能创建泛型数组，即不能直接对泛型类型数组进行初始化。

4. **类型确定时机**：泛型类的类型是在创建对象时确定的，因为创建对象时需要指定具体的类型。

  1. 静态成员不能使用泛型。
  2. 静态方法中不能使用类的泛型类型参数。

  ```java
  class A<T>{
  	T name1; // succeed
    
    // 静态成员不能使用泛型
    // static T name2; // failed
    
    // 静态方法中不能使用类的泛型类型参
    //static void f1(T t) { // failed
    //}
    //static void f2() {
    //  T t; // failed
    //}
  }
  ```

* 继承/实现的时候写指定泛型

	```java
	interface I<U,R>{
	}
	
	class A implements I<String,Double>{} // 可以
	```

---
## 自定义泛型方法

1. 基本语法

	```java
	修饰符 <T, R...> 返回类型 方法名(参数列表) {
	  // 方法体
	}
	```
	
	1. **定义位置**：泛型方法可以定义在普通类中，也可以定义在泛型类中。
	2. **类型确定时机**：当泛型方法**被调用**时，类型参数会确定。
	3. **方法签名**：在方法签名中，泛型参数列表位于返回类型之前。

4. 示例代码

	```java
	package ex_generic;
	
	public class Demo04{
	  public static void main(String[] args) {
	    ZooKeeper keeper = new ZooKeeper();
	    keeper.feed(new Lion(), new Meat());      // Feed Lion with Meat
	    keeper.feed(new Panda(), new Bamboo());   // Feed Panda with Bamboo
	    keeper.feed(new Fish(), new FishFood());  // Feed Fish with FishFood
	  }
	}
	
	class ZooKeeper {
	  public <T, R> void feed(T animal, R food) {
	    System.out.println("Feed " + animal.getClass().getSimpleName() +
	                       " with " + food.getClass().getSimpleName());
	  }
	}
	
	class Lion{}
	class Meat{}
	class Panda{}
	class Bamboo{}
	class Fish{}
	class FishFood{}
	```

3. 练习

	```java
	class Apple<T,R,M>{
	  public<E> void fly(E e){ // 正确，泛型方法
	    System.out.println(e.getClass().getSimpleName());
	  }
	  public void eat(U u) {} // 错误，因为 U 没有声明
	  public void run(M m) {} // 正确
	}
	
	class Dog {}
	
	//下面代码输出什么？
	Apple<String, Integer, Double> apple= new Apple<>();
	apple.fly(10); // Integer（自动装箱）
	apple.fly(new Dog()); // Dog
	```

---
## 泛型的继承和通配符

1. **泛型没有继承性**
	
	```java
	Object a = new String("Hello"); //可以
	List<Object> la = new ArrayList<String>(); //不可以
	```
	
2. **通配符使用**`<?>`：在**使用泛型**的时候支持任意泛型类型。
   
3. **上界通配符**`<? extends A>`：在**使用泛型**的时候支持A类以及A类的子类，规定了泛型的上限。
   
4. **下界通配符**`<? super A>`：在**使用泛型**的时候支持A类以及A类的父类，不限于直接父类，规定了泛型的下限。


```java
public class GenericExtends {
  public static void printCollection1(List<?> c) {
    for (Object object : c) {
      System.out.println(object);
    }
  }

  public static void printCollection2(List<? extends AA> c) {
    for (Object object : c) {
      System.out.println(object);
    }
  }

  public static void printCollection3(List<? super AA> c) {
    for (Object object : c) {
      System.out.println(object);
    }
  }

  public static void main(String[] args) {
    ArrayList<Object> a1 = new ArrayList<Object>();
    ArrayList<String> a2 = new ArrayList<String>();
    ArrayList<AA> a3 = new ArrayList<AA>();
    ArrayList<BB> a4 = new ArrayList<BB>();
    ArrayList<CC> a5 = new ArrayList<CC>();

    // <?>可以接受任意的类型
    printCollection1(a1); // 可以
    printCollection1(a2); // 可以
    printCollection1(a3); // 可以
    printCollection1(a4); // 可以
    printCollection1(a5); // 可以

    // <? extends AA>继承了 AA 的子类或者 AA 本身
    printCollection2(a1); // 不可以
    printCollection2(a2); // 不可以
    printCollection2(a3); // 可以
    printCollection2(a4); // 可以
    printCollection2(a5); // 可以

    // <? super AA> AA 以及 AA 的父类们
    printCollection3(a1); // 可以
    printCollection3(a2); // 不可以
    printCollection3(a3); // 可以
    printCollection3(a4); // 不可以
    printCollection3(a5); // 不可以
  }
}

class AA {}
class BB extends AA {}
class CC extends BB {}
```
