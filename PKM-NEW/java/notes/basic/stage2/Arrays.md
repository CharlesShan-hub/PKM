## toString

比如要输出一个数组，可以循环的输出，也可以用 Arrays

```java
package ex_commom;  
  
import java.util.Arrays;  
  
public class ArrayExample {  
    public static void main(String[] args) {  
        double[] nums = {10, 20, 30};  
        for(int i=0; i<nums.length; i++)  
            System.out.println(nums[i]);  
        System.out.println(Arrays.toString(nums));  
    }  
}
```

Arrays类的 toString 的源码如下（JDK21）

```java
public final class Arrays {
	public static String toString(long[] a) {  
	    if (a == null)  
	        return "null";  
	    int iMax = a.length - 1;  
	    if (iMax == -1)  
	        return "[]";  
	  
	    StringBuilder b = new StringBuilder();  
	    b.append('[');  
	    for (int i = 0; ; i++) {  
	        b.append(a[i]);  
	        if (i == iMax)  
	            return b.append(']').toString();  
	        b.append(", ");  
	    }  
	}
}
```

## sort

Arrays 还可以进行排序。注意数组是引用类型，所以排序的是直接改变传入的变量

```java
double[] nums = {10, 20, 30, 25, 15};  
System.out.println(Arrays.toString(nums));  
// [10.0, 20.0, 30.0, 25.0, 15.0]  
Arrays.sort(nums);  
System.out.println(Arrays.toString(nums));  
// [10.0, 15.0, 20.0, 25.0, 30.0]
```

可以通过传入接口 Comparator 来实现自己的排序

```java
package ex_commom;  
  
import java.util.Arrays;  
import java.util.Comparator;  
  
public class ArrayExample {  
    public static void main(String[] args) {  
        Student[] students = new Student[3];  
        students[0] = new Student(18, 90);  
        students[1] = new Student(20, 85);  
        students[2] = new Student(19, 100);  
        System.out.println("Sort by age");  
        Arrays.sort(students, new Comparator() {  
            @Override  
            public int compare(Object o1, Object o2) {  
                return ((Student)o1).getAge() - ((Student)o2).getAge();  
            }  
        });  
        System.out.println(students[0]);  
        System.out.println(students[1]);  
        System.out.println(students[2]);  
        //Age: 18, Score90  
        //Age: 19, Score100        //Age: 20, Score85  
        System.out.println("Sort by score");  
        Arrays.sort(students, new Comparator(){  
            @Override  
            public int compare(Object o1, Object o2){  
                return ((Student)o1).getScore() - ((Student)o2).getScore();  
            }  
        });  
        System.out.println(students[0]);  
        System.out.println(students[1]);  
        System.out.println(students[2]);  
        //Age: 20, Score85  
        //Age: 18, Score90        //Age: 19, Score100        }  
}  
  
class Student{  
    private int age;  
    private int score;  
  
    public Student(int age, int score) {  
        this.age = age;  
        this.score = score;  
    }  
  
    public int getAge() {  
        return age;  
    }  
  
    public int getScore() {  
        return score;  
    }  
  
    @Override  
    public String toString() {  
        return "Age: "+getAge()+", Score"+getScore();  
    }  
}
```

更好的写法

```java
Arrays.sort(students, new Comparator<Student>() {  
    @Override  
    public int compare(Student o1, Student o2) {  
        return o1.getAge() - o2.getAge();  
    }  
});
```

## binarySort

要求对升序的数组进行查找

```java
int[] nums = new int[]{1,3,5,7,8,9,10};  
// 找到了  
System.out.println(Arrays.binarySearch(nums,8)); // 4  
// 没找到  
System.out.println(Arrays.binarySearch(nums,11)); // -8  
System.out.println(Arrays.binarySearch(nums,0)); // -1
```

为什么没找到 11 会返回 -8，因为如果 11 存在，他理论上应该在 第 8 个位置。
同理如果 0 存在，他应该在第一个位置。

## copyOf

深拷贝，如果位置不够，就加一个空

```java
Integer[] nums = new Integer[]{1,3,5,7,8,9,10};  
Integer[] newArr = Arrays.copyOf(nums, nums.length+1);  
System.out.println(Arrays.toString(newArr));  
// [1, 3, 5, 7, 8, 9, 10, null]  
Integer[] newArr2 = Arrays.copyOf(nums, 0);  
// []  
System.out.println(Arrays.toString(newArr2));  
// Integer[] newArr2 = Arrays.copyOf(nums, -1); 异常
```

## fill

填充 

```java
Integer[] array = new Integer[4];  
Arrays.fill(array, 100);  
System.out.println(Arrays.toString(array));  
// [100, 100, 100, 100]
```

## equals

```java
Integer[] a1 = new Integer[]{1,2,3};  
Integer[] a2 = new Integer[]{1,2,3};  
Integer[] a3 = new Integer[]{1,2,3,4};  
System.out.println(Arrays.equals(a1,a2)); // true  
System.out.println(Arrays.equals(a1,a3)); // false 
```

## asList

```java
Integer[] a1 = new Integer[]{1,2,3};  
List l1 = Arrays.asList(a1);  
System.out.println(l1.toString()); // [1, 2, 3]
System.out.println(l1.getClass()); // class java.util.Arrays$ArrayList(这个是运行类型)
```

## 练习

Arrays类课堂练习
ArrayExercise.java
案例: 自定义Book类, 里面包含name和price, 按price排序(从大到小)。要求使用两种方式排序，对对象的某个属性排序, 有一个 Book[] books = 5本书对象.
使用前面学习过的传递实现Comparator接口匿名内部类, 也称为定制排序。[同学们完成这个即可10min]
```java
Book[] books = new Book[4];
books[0] = new Book("红楼梦", 100);
books[1] = new Book("金瓶梅", 90);
books[2] = new Book("青年文摘", 5);
books[3] = new Book("java从入门到放弃", 300);
```

```java
package ex_commom;  
  
import java.util.Arrays;  
import java.util.Comparator;  
  
public class Array01 {  
    public static void main(String[] args){  
        Book[] books = new Book[4];  
        books[0] = new Book("红楼梦", 100);  
        books[1] = new Book("金瓶梅", 90);  
        books[2] = new Book("青年文摘", 5);  
        books[3] = new Book("java从入门到放弃", 300);  
  
        System.out.println("按照价格升序");  
        Arrays.sort(books, new Comparator<Book>() {  
            @Override  
            public int compare(Book o1, Book o2) {  
                return o1.getPrice()-o2.getPrice();  
            }  
        });  
        for(Book b : books)  
            System.out.println(b.toString());  
  
        System.out.println("按照价格降序");  
        Arrays.sort(books, new Comparator<Book>() {  
            @Override  
            public int compare(Book o1, Book o2) {  
                return o2.getPrice()-o1.getPrice();  
            }  
        });  
        for(Book b : books)  
            System.out.println(b.toString());  
  
        System.out.println("按照名字长度");  
        Arrays.sort(books, new Comparator<Book>() {  
            @Override  
            public int compare(Book o1, Book o2) {  
                return o1.getName().length()-o2.getName().length();  
            }  
        });  
        for(Book b : books)  
            System.out.println(b.toString());  
          
        // 按照价格升序  
        //name: 青年文摘,price: 5  
        //name: 金瓶梅,price: 90  
        //name: 红楼梦,price: 100  
        //name: java从入门到放弃,price: 300  
        //按照价格降序  
        //name: java从入门到放弃,price: 300  
        //name: 红楼梦,price: 100  
        //name: 金瓶梅,price: 90  
        //name: 青年文摘,price: 5  
        //按照名字长度  
        //name: 红楼梦,price: 100  
        //name: 金瓶梅,price: 90  
        //name: 青年文摘,price: 5  
        //name: java从入门到放弃,price: 300  
    }  
}  
  
class Book{  
    private String name;  
    private int price;  
  
    public Book(String name, int price) {  
        this.name = name;  
        this.price = price;  
    }  
  
    public String getName() {  
        return name;  
    }  
  
    public int getPrice() {  
        return price;  
    }  
  
    @Override  
    public String toString(){  
        return "name: "+name+",price: "+price;  
    }  
}
```