
```java
package ex_poly;

public class Test{
	public static void main(String[] args){
		Person p = new Person("Peter");
		System.out.println(p.feed(new Cat(), new Fish()));
		//Peter feed Fish🍣 to Cat🐱 
		System.out.println(p.feed(new Dog(), new Meat()));
		//Peter feed Meat🥩 to Dog🐶 
		System.out.println(p.feed(new Pig(), new Cake()));
		//Peter feed Cake🍰 to Pig🐽
		
		// animal 编译类型就是 Animal，运行类型 Dog
	    Animal animal = new Dog();
	    // 因为运行时，执行到改行时，animal 运行类型是 Dog，所以 cry 就是 Dog 的 cry
	    animal.cry(); // Woof~
	
	    // animal 编译类型 Animal，运行类型就是 Cat
	    animal = new Cat();
	    animal.cry(); // Miao
	}
}

class Person{
	private String name;
	public Person(String name) {
		this.name = name;
	}
	// 没有使用多态, 每一种宠物与饭的组合都要定一个方法，组合爆炸!
	//public String feed(Cat c, Fish f){
	//	return name+" feed "+f+" to "+c;
	//}
	//public String feed(Dog d, Meat m){
	//	return name+" feed "+m+" to "+d;
	//}
	//public String feed(Pig p, Cake c){
	//	return name+" feed "+c+" to "+p;
	//}
	// 使用多态👌
	public String feed(Animal a, Food f){
		return name+" feed "+f+" to "+a;
	}
}

abstract class Animal{
	abstract void cry();
}
class Cat extends Animal{
	@Override
	public String toString(){return "Cat🐱";}
	@Override
	public void cry(){System.out.println("Miao~");}
}
class Dog extends Animal{
	@Override
	public String toString(){return "Dog🐶";}
	@Override
	public void cry(){System.out.println("Woof~");}
}
class Pig extends Animal{
	@Override
	public String toString(){return "Pig🐽";}
	@Override
	public void cry(){System.out.println("Heng~");}
}

abstract class Food{}
class Fish extends Food{
	@Override
	public String toString(){return "Fish🍣";}
}
class Meat extends Food{
	@Override
	public String toString(){return "Meat🥩";}
}
class Cake extends Food{
	@Override
	public String toString(){return "Cake🍰";} 
}
```

