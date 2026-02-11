# 多态

浏览顺序：[encapsulation](encapsulation.md) 👉 [extends](extends.md) 👉 本文

---
## 方法的多态

> **方法重载**和**方法重写**也是多态，叫做方法的多态

1. **方法重载**（`Overload`）👉 [overload-detail](../../../details/overload-detail.md)
	1. 同一个类中，多个同名方法存在，单要求形参不同
2. **方法重写**/覆盖（`Override`）👉 [override-detail](../../../details/override-detail.md)
	1. 需要名称、返回类型和参数都一样
	2. 注意⚠️：方法重写前两个字是“方法”，<u>属性是不能重写的</u>
	3. 返回类型可以一样，也可以是子类
	4. 访问权限可以一样，也可以变大
	5. 调用多个重载的方法，遵循“就近原则”
3. 比较
	
	|            | 方法重载 | 方法重写  |
	| :--------: | :------: | :-------: |
	|    位置    |   本类   |   子类    |
	|   方法名   |   一样   |   一样    |
	|  形参列表  |   不同   |   相同    |
	|  返回类型  |  无要求  | 缩小/一样 |
	| 访问修饰符 |  无要求  | 扩大/一样 |

---
## 对象的多态

> 对象的多态，是重点。

1. 没有多态的世界。主人需要为宠物吃饭，有好多饭，好多宠物。
	```java
	package ex_poly;  
	
	public class Test{  
	  public static void main(String[] args){  
	    Person p = new Person("Peter");  
	    System.out.println(p.feed(new Cat(), new Fish()));  
	    // Peter feed Fish to Cat  
	    System.out.println(p.feed(new Dog(), new Meat()));  
	    // Peter feed Dog to Meat  
	  }  
	}  
	
	class Person{  
	  private String name;  
	  public Person(String name) {  
	    this.name = name;  
	  }    
	  public String feed(Cat c, Fish f){  
	    return name+" feed "+f+" to "+c;  
	  }    
	  public String feed(Dog d, Meat m){  
	    return name+" feed "+d+" to "+m;  
	  }
	}  
	
	class Animal{  
	}  
	class Cat extends Animal{  
	  public String toString(){return "Cat";}  
	}  
	class Dog extends Animal{  
	  public String toString(){return "Dog";}  
	}  
	class Pig extends Animal{  
	  public String toString(){return "Pig";}  
	}  
	
	class Food{  
	}  
	class Fish extends Food{  
	  public String toString(){return "Fish";}  
	}  
	class Meat extends Food{  
	  public String toString(){return "Meat";}  
	}
	```

2. 多态的定义
	1. 一个对象的编译类型（赋值号左边）和运行类型（赋值号右边）可以不一致（`Animal d = new Dog();`）
	2. 编译类型在定义对象时，就确定了，不能改变 
	3. **运行类型**是可以变化的（`d = new Cat();`之前的 d 从 Dog 变成了 Cat）
	4. **编译类型**看定义时 `=` 号的左边，运行类型看 `=` 号的右边
	```java
	public class PolyObject {
	  public static void main(String[] args) {
	    // 体验对象多态特点
	
	    // animal 编译类型就是 Animal，运行类型 Dog
	    Animal animal = new Dog();
	    // 因为运行时，执行到改行时，animal 运行类型是 Dog，所以 cry 就是 Dog 的 cry
	    animal.cry(); // 小狗汪汪叫
	
	    // animal 编译类型 Animal，运行类型就是 Cat
	    animal = new Cat();
	    animal.cry(); // 小猫喵喵叫
	  }
	}
	
	// 动物基类
	abstract class Animal {
	  // 抽象方法，具体动物类需要实现
	  abstract void cry();
	}
	
	// 狗类继承自动物类
	class Dog extends Animal {
	  @Override
	  void cry() {
	    System.out.println("小狗汪汪叫");
	  }
	}
	
	// 猫类继承自动物类
	class Cat extends Animal {
	  @Override
	  void cry() {
	    System.out.println("小猫喵喵叫");
	  }
	}
	
	```

3. 我们可以使用刚才的方法的多态初步实现：

   ```java
   class Person{// 没有多态
     public feed(Cat a, Fish f){
       System.out.println(a.toString()+" eat "+f.toString());
     }
     public feed(Dog a, Meat f){
       System.out.println(a.toString()+" eat "+f.toString());
     }
     public feed(Pig a, Fish f){
       System.out.println(a.toString()+" eat "+f.toString());
     }
     public feed(Pig a, Meat f){
       System.out.println(a.toString()+" eat "+f.toString());
     }
   }
   ```
	
	多态改进实现：
	
   ```java
   class Person{
     public feed(Aninmal a, Food d){// 这就是多态
       System.out.println(a.toString()+" eat "+f.toString());
     }
   }
   ```

4. 向上转型

   ```java
   class Father{}
   class Child extends Father{}
   ```

   ```java
   Father obj = new Child();
   ```

   * 本质：父类的引用指向了子类的对象
   * obj的编译类型：Father，所以不能访问Child的private变量和方法
   * obj的运行类型：Child，所以找方法的时候还是从Child开始找
   * 注意⚠️，**属性是不能重写的**，obj.属性，返回的是父类的属性

   下面看一个案例：

   ```java
   class Animal{
     public void say(){
       System.out.println("...");
     }
   }
   class Cat extends Animal{
     public void say(){
       System.out.println("Miao~");
     }
     protected void secret(){
       System.out.println("不能说的秘密");
     }
   }
   ```

   ```java
   public class Program{
     public static void main(String[] args){
       Animal a = new Cat();
       a.say();
       System.out.println(a instanceof Cat);
       //a.secret(); // 不能调用，因为secret是Cat的方法，不是Animal的方法
     }
   }
   ```

   ```
   >>> Miao~
   >>> true
   ```

5. 向下转型

	```java
	class Father{}
	class Child extends Father{}
	```

	```java
	Father obj = new Child();
	(Child)obj // 通过强制转换，向下转型
	```

   * 向上转上去的，才能向下转回来
   * 可以调用子类所有内容

	```java
	class Animal{
	 public void say(){
	   System.out.println("...");
	 }
	}
	class Cat extends Animal{
	 public void say(){
	   System.out.println("Miao~");
	 }
	 protected void secret(){
	   System.out.println("不能说的秘密");
	 }
	}
	```

	```java
	public class Program{
	 public static void main(String[] args){
	   Animal a = new Cat();
	   ((Child)a).secret();
	 }
	}
	```

	```
	>>> 不能说的秘密
	```

6. **方法重写前两个字是“方法”，属性是不能重写的！！！！**

   ```java
   class Animal{
     int age = 1;
   }
   class Cat extends Animal{
     int age = 2;
   }
   public class Program{
     public static void main(String[] args){
       Animal a = new Cat();
       System.out.println(a.age);
     }
   }
   ```

   ```
   >>> 1
   ```

7. `instanceof`(判断的是**运行类型**是否是**后边的类型或者后边类型的子类型**)
	```java
	class Base{}
	class Child extends Base{}
	
	public class Test(){
		public static void main(String[] args){
			Base b1 = new Base();
			Base b2 = new Child();
			System.out.println(b1 instanceof Base); // true
			System.out.println(b1 instanceof Child);// false
			System.out.println(b2 instanceof Base); // true
			System.out.println(b2 instanceof Child);// true
		}
	}
	```

* 例题

  1. 判断对错

  ```java
  public class Exercise1{
    public static void main(String[] args){
      double d = 13.4;
      long l = (long)d;
      System.out.println(l);
      int in = 5;
      boolean b = (boolean)in;
      Object obj = "Hello";
      String objStr = (String)obj;
      System.out.println(objStr);
      Object obj = new Integer(5);
      String str = (String)objPri;
      Integer str1 = (Integer)objPri;
    }
  }
  
  ```

  ```java
  public class Exercise1{
    public static void main(String[] args){
      // 可以
      double d = 13.4;
      // 可以
      long l = (long)d;
      // 可以，13
      System.out.println(l);
      int in = 5;
      // 不可以，int不能转成boolean
      boolean b = (boolean)in;
      // 可以，向上转型，Hello
      Object obj = "Hello";
      // 可以，向下转型  
      String objStr = (String)obj;
      System.out.println(objStr);
      // 可以，向上转型
      Object obj = new Integer(5);
      // 错误，只能向下转型到int
      String str = (String)objPri;
      // 可以，向下转型
      Integer str1 = (Integer)objPri;
    }
  }
  ```

  2. 练习2

  ```java
  class Base{
    int count = 10;
    public void display(){
      System.out.println(this.count);
    }
  }
  class Sub extends Base{
    int count = 20;
    public void display(){
      System.out.println(this.count);
    }
  }
  public class Program{
    public static void main(String[] args){
      Sub s = new Sub();
      System.out.println(s.count);
      s.display();
      Base b = s;
      System.out.println(b==s);
      System.out.println(b.count);
      b.display();
    }
  }
  ```

  ```java
  public class Program{
    public static void main(String[] args){
      Sub s = new Sub();
      System.out.println(s.count);
      // 20
      s.display();
      // 20
      Base b = s;
      System.out.println(b==s);
      // True
      System.out.println(b.count);
      // 10
      b.display();
      // 20
    }
  }
  ```

---
## 动态绑定机制

1. 引入例子

	```java
	class A{
		public int i = 10;
		public int sum(){
			return getI() + 10;
		}
		public int sum1(){
			return i+10;
		}
		public int getI(){
		return i;
		}
	}
	```

	```java
	class B extends A{
		public int i = 20;
		public int sum(){
			return i + 20;
		}
		public int getI(){
			return i;
		}
		public int sum1(){
			return i+10;
		}
	}
	```

   ```java
   // main
   A a = new B();
   System.out.println(a.sum());
   System.out.println(a.sum1());
   ```

   ```
   >>> 40
   >>> 30
   ```

2. 修改上面的例子，注释掉子类的方法

	```java
	class A{
		public int i = 10;
		public int sum(){
			return getI() + 10; // 方法有动态绑定机制，所以 getI 是 B 的 getI
		}
		public int sum1(){
			return i+10; // 属性没有动态绑定机制，所以 i 是 A 的 i
		}
		public int getI(){
			return i;
		}
	}
	```

	```java
	class B extends A{
		public int i = 20;
		// public int sum(){
		//   return getI() + 20;
		// }
		// public int sum1(){
		//   return i+10;
		// }
		public int getI(){
			return i;
		}
	}
	```

   ```java
   // main
   A a = new B();
   System.out.println(a.sum());
   System.out.println(a.sum1());
   ```

   ```
   >>> 30
   >>> 20
   ```

3. 当调用对象的**方法**的时候，该方法会和该对象的**内存地址/运行类型**绑定

4. 当调用对象**属性**时，**没有动态绑定机制**，哪里声明就在哪里用

* 面试题：多态解决了什么问题
	* 多态指同⼀个接⼝或⽅法在不同的类中有不同的实现，⽐如说动态绑定，⽗类引⽤指向⼦类对象，**⽅法的具体调⽤会延迟到运⾏时决定**。
* 面试题：多态的实现原理是什么
	* 多态通过**动态绑定**实现，Java 使⽤**虚⽅法表**存储**⽅法指针**，⽅法调⽤时根据对象实际类型从虚⽅法表查找具体实现。
	![multy](../../../assets/multy.png)
---
## 多态的应用

1. 多态数组：有一个Person对象，两个Student对象，两个Teacher对象

   ```java
   class Person{
     public String name;
     public int age;
     public Person(String name, int age){
       this.name = name;
       this.age = age;
     }
     public String say(){
       return name+"\t"+age;
     }
   }
   
   class Student extends Person{
     public double score;
     public Student(String name,int age,double score){
       super(name,age);
       this.score = score;
     }
     @Override
     public String say(){
       return "学生 " + super.say() + " score=" + score;
     }
     //特有方法
     public void study(){
       System.out.println("学生 " + name + " 正在学习..."); 
     }
   }
   
   class Teacher extends Person{
     public double salary;
     public Teacher(String name,int age,double salary){
       super(name,age);
       this.salary = salary;
     }
     @Override
     public String say(){
       return "老师 " + super.say() + " salary=" + salary;
     }
     //特有方法
     public void teach() {
       System.out.println("老师 " + name + " 正在讲课..."); 
     }
   }
   ```

   应用：

   ```java
   public class Program{
     public static void main(String[] args){
       // main
       Person[] persons = new Person[5];
       persons[0] = new Person("jack", 20); 
       persons[1] = new Student("mary", 18, 100); 
       persons[2] = new Student("smith", 19, 30.1); 
       persons[3] = new Teacher("scott", 30, 20000); 
       persons[4] = new Teacher("king", 50, 25000);
   
       for(int i=0; i<persons.length; i++){
         // 动态绑定机制
         System.out.println(persons[i].say());
         // 运行特殊的功能，向下转型
         if(persons[i] instanceof Student){
           Student s = (Student)persons[i];
           s.study();
         }else if(persons[i] instanceof Teacher){
           Teacher t = (Teacher)persons[i];
           t.teach();
         }else{
           System.out.println("你的类型有误, 请自己检查...");
         }
       }
     }
   }
   ```

   ```
   jack  20
   你的类型有误, 请自己检查...
   学生 mary 18 score=100.0
   学生 mary 正在学习...
   学生 smith  19 score=30.1
   学生 smith 正在学习...
   老师 scott  30 salary=20000.0
   老师 scott 正在讲课...
   老师 king 50 salary=25000.0
   老师 king 正在讲课...
   ```

   



