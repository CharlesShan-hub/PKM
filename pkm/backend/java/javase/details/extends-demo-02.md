子类会调用父类的构造器

```java
// Test.java
package ex_extend;  
import ex_extend.Parent;  
import ex_extend.Child;  
  
public class Test {  
	public static void main(String[] args){  
		Parent p = new Parent();  
		// Constructor of Parent.  
		Child c = new Child();  
		// Constructor of Parent.  
		// Constructor of Child.        
		Parent p2 = new Parent("P");  
		// Constructor of Parent P  
		Child c2 = new Child("C");  
		// Constructor of Parent C  
		// Constructor of Child C    
	}  
}
```

```java
// Parent.java
package ex_extend;  
  
class Parent {  
	public Parent(){  
		System.out.println("Constructor of Parent.");  
	} 
	public Parent(String name){  
		System.out.println("Constructor of Parent "+name);  
	}
}  
  
class Child extends Parent{  
	public Child(){  
		// super();  默认调用父类无参构造器
		System.out.println("Constructor of Child.");  
	}
	public Child(String name){
		super(name); // 调用父类有参构造器需要手动调用
		System.out.println("Constructor of Child "+name);  
	}
}
```
