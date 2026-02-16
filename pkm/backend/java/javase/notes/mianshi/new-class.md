# 面试题：创建对象有哪⼏种⽅式

四种方式

1. new 关键字创建，这是最常⻅和直接的⽅式，通过调⽤类的构造⽅法来创建对象。
	```java
	Person person = new Person();
	```
2. 反射机制创建，反射机制允许在运⾏时创建对象，并且可以访问类的私有成员，在框架和⼯具类中⽐较常⻅。
	```java
	Class clazz = Class.forName("Person");
	Person person = (Person) clazz.newInstance();
	```
3. clone 拷⻉创建，通过 clone ⽅法创建对象，需要实现 Cloneable 接⼝并重写 clone ⽅法。
	```java
	Person person = new Person();
	Person person2 = (Person) person.clone();
	```
4. 序列化机制创建，通过序列化将对象转换为字节流，再通过反序列化从字节流中恢复对象。需要实现Serializable 接⼝。
	```java
	Person person = new Person();
	ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("person.txt"));
	oos.writeObject(person);
	ObjectInputStream ois = new ObjectInputStream(new FileInputStream("person.txt"));
	Person person2 = (Person) ois.readObject();
	```