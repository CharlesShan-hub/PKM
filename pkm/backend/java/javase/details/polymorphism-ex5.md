
多态数组：有一个Person对象，两个Student对象，两个Teacher对象

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

