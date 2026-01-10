# Arrays

数组专题推荐浏览顺序：[array](../stage1/array.md) 👉 本文

---
## Arrays 类简介

Arrays 类是 Java 中 java.util 包提供的一个工具类，主要用于操作数组（如排序、搜索、比较、填充等）。它包含了一系列静态方法，可以方便地对数组进行各种操作。

* `Arrays.toString()`：将数组转换成字符串
* `Arrays.deepToString()`：可以将二维数组转换成字符串
* `Arrays.equals(int[] arr1, int[] arr2)`：判断两个数组是否相等
* `Arrays.equals(Object[] arr1, Object[] arr2)`
* `Arrays.deepEquals(Object[] arr1, Object[] arr2)`：判断两个二维数组是否相等
* `Arrays.sort(int[] arr)`：基于快速排序算法，适合小型数据量排序。
* `Arrays.sort(String[] arr)`
* `Arrays.parallelSort(int[] arr)`：基于分治的归并排序算法，支持多核CPU排序，适合大数据量排序。
* `int binarySearch(int[] arr, int elt)`：二分法查找
* `Arrays.fill(int[] arr, int data)`：填充数组
* `Arrays.fill(int[] a, int fromIndex, int toIndex, int val)`
* `int[] Arrays.copyOf(int[] original, int newLength)`：数组拷贝
* `int[] Arrays.copyOfRange(int[] original, int from, int to)`
* `Arrays.asList(T... data)`：将一组数据转换成List集合。


### 主要功能

1. **​排序​**​：对数组进行排序
   
    ```
    int[] numbers = {3, 1, 4, 2};
    Arrays.sort(numbers); // 排序后：[1, 2, 3, 4]
    ```
    
2. **​二分查找​**​：在已排序数组中查找元素
   
    ```
    int index = Arrays.binarySearch(numbers, 3); // 返回2
    ```
    
3. **​比较数组​**​：比较两个数组是否相等
   
    ```
    int[] arr1 = {1, 2, 3};
    int[] arr2 = {1, 2, 3};
    boolean isEqual = Arrays.equals(arr1, arr2); // 返回true
    ```
    
4. **​填充数组​**​：用指定值填充数组
   
    ```
    int[] filled = new int[5];
    Arrays.fill(filled, 7); // [7, 7, 7, 7, 7]
    ```
    
5. **​数组转字符串​**​：方便打印数组内容
   
    ```
    String arrayStr = Arrays.toString(numbers); // "[1, 2, 3, 4]"
    ```
    
6. **​复制数组​**​：复制数组的全部或部分
   
    ```
    int[] copy = Arrays.copyOf(numbers, numbers.length);
    ```
    
7. **​流操作​**​（Java 8+）：将数组转换为流
   
    ```
    Arrays.stream(numbers).forEach(System.out::println);
    ```
    
### 特点

- 所有方法都是静态的，无需创建 Arrays 实例
- 支持基本类型数组和对象数组
- 线程安全（因为方法都是无状态的）

---
## toString

比如要输出一个数组，可以循环的输出，也可以用 Arrays

```java
package ex_commom;  
  
import java.util.Arrays;  
  
public class ArrayExample {  
    public static void main(String[] args) {  
        double[] nums = {10, 20, 30};  
        // 1. 循环
        for(int i=0; i<nums.length; i++)  
            System.out.println(nums[i]);  
        // 2. toString
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

`toString`的案例

```java
int[] intArray = {1, 2, 3, 4, 5};
System.out.println(Arrays.toString(intArray)); 
// 输出: [1, 2, 3, 4, 5]

String[] strArray = {"Java", "Python", "C++"};
System.out.println(Arrays.toString(strArray));
// 输出: [Java, Python, C++]

boolean[] boolArray = {true, false, true};
System.out.println(Arrays.toString(boolArray));
// 输出: [true, false, true]
```

---
## deepToString

`deepToString()` 方法用于将多维数组转换为字符串表示形式，可以正确处理嵌套数组。
- 专门用于多维数组或对象数组
- 递归地转换嵌套数组
- 输出格式为：`[[元素1, 元素2], [元素3, 元素4]]`
- 如果数组为null，返回"null"
- 可以处理任意深度的嵌套数组

```java
int[][] deepIntArray = {{1, 2}, {3, 4}, {5, 6}};
System.out.println(Arrays.deepToString(deepIntArray));
// 输出: [[1, 2], [3, 4], [5, 6]]

String[][] deepStrArray = {{"Java", "Python"}, {"C++", "JavaScript"}};
System.out.println(Arrays.deepToString(deepStrArray));
// 输出: [[Java, Python], [C++, JavaScript]]

Object[] mixedArray = {1, "two", new int[]{3, 4}};
System.out.println(Arrays.deepToString(mixedArray));
// 输出: [1, two, [3, 4]]
```

错误案例（用普通的 toString 处理嵌套数组）

```java
int[][] deepArray = {{1, 2}, {3, 4}};
System.out.println(Arrays.toString(deepArray));
// 错误输出: [[I@15db9742, [I@6d06d69c]
// 应该使用deepToString
```

---
## equals

- `equals()` - 比较两个数组是否相等
- `deepEquals()` - 比较两个多维数组是否相等

```java
Integer[] a1 = new Integer[]{1,2,3};  
Integer[] a2 = new Integer[]{1,2,3};  
Integer[] a3 = new Integer[]{1,2,3,4};  
System.out.println(Arrays.equals(a1,a2)); // true  
System.out.println(Arrays.equals(a1,a3)); // false 
```

---
## sort

### 排序规则

Arrays 还可以进行排序。注意数组是引用类型，所以排序的是直接改变传入的变量。

```java
double[] nums = {10, 20, 30, 25, 15};  
System.out.println(Arrays.toString(nums));  
// [10.0, 20.0, 30.0, 25.0, 15.0]  
Arrays.sort(nums);  
System.out.println(Arrays.toString(nums));  
// [10.0, 15.0, 20.0, 25.0, 30.0]
```

如果是对字符串数组进行排序。

```java
String[] strs = {"a", "ac", "ab", "b"};  
// 应该是根据字典的顺序排序的。  
Arrays.sort(strs);  
System.out.println(Arrays.toString(strs));
// [a, ab, ac, b]
```

### Comparator

可以通过传入接口 Comparator 来实现自己的排序

```java
package ex_array;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.Getter;

import java.util.Arrays;
import java.util.Comparator;

public class Test {
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
    //Age: 19, Score100
    //Age: 20, Score85
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
    //Age: 18, Score90
    //Age: 19, Score100
  }
}

@Data
@Getter
@AllArgsConstructor
class Student{
  private int age;
  private int score;

  @Override
  public String toString() {
    return "Age: "+getAge()+", Score: "+getScore();
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

### parallelSort

`parallelSort()` 是 Java 8 引入的一个并行排序方法，属于 `java.util.Arrays` 类，它利用多核处理器的优势对数组进行并行排序。

基本类型数组排序

```java
int[] numbers = {5, 3, 9, 1, 7, 2, 8, 4, 6}; 
Arrays.parallelSort(numbers); 
System.out.println(Arrays.toString(numbers)); 
// 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

对象数组排序

```java
String[] languages = {"Java", "Python", "C++", "JavaScript", "Go"}; 
Arrays.parallelSort(languages); 
System.out.println(Arrays.toString(languages)); 
// 输出: [C++, Go, Java, JavaScript, Python]```
```

指定范围排序

```java
int[] data = {9, 5, 7, 3, 1, 8, 6, 2, 4}; 
Arrays.parallelSort(data, 2, 7); // 只排序索引2到6的元素
System.out.println(Arrays.toString(data)); 
// 输出: [9, 5, 1, 3, 6, 7, 8, 2, 4]
```

性能考虑
1. **​数据集大小​**​：
    - 小数组（≤ 8192 元素）：`parallelSort()` 可能比 `sort()` 稍慢（由于并行开销）
    - 大数组：`parallelSort()` 通常更快
2. **​处理器核心数​**​：
    - 核心越多，并行优势越明显
3. **​内存考虑​**​：
    - `parallelSort()` 需要额外的内存空间（约为原数组大小）

```java
/**  
 * 启用多核CPU并行排序。  
 * 首先你的电脑是支持多核的。  
 * 注意：数据量太小的话，不要调用这个方法，因为启动多核也是需要耗费资源的。  
 * Java8引入的方法。  
 * 数据量较大的时候，建议使用这个方法效率比较高。  
 *  
 * 通过源码分析：如果超过4096个长度，则会启用多核。  
 * 4096以内就自动调用sort方法就行了。  
 */  
@Test  
public void testParallelSort(){  
    int[] arr = new int[100000000];  
    Random random = new Random();  
    for (int i = 0; i < arr.length; i++) {  
        int num = random.nextInt(100000000);  
        arr[i] = num;  
    }  
  
    // 获取系统当前时间的毫秒数（1970-1-1 0:0:0 000到当前系统时间的总毫秒数 1秒=1000毫秒）  
    long begin = System.currentTimeMillis();  
  
    // 排序  
    Arrays.parallelSort(arr);  
  
    // 获取系统当前时间的毫秒数  
    long end = System.currentTimeMillis();  
  
    // 耗时  
    System.out.println(end - begin);  
}
```

### binarySort

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

---
## binarySearch

```java
@Test  
public void testBinarySearch(){  
    int[] arr = {1,2,3,4,5,6,7};  
    System.out.println(Arrays.binarySearch(arr, 5)); // 4  
}
```

---
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

---
## fill

填充 

```java
@Test  
public void testFill(){  
    int[] arr = new int[5]; // 5个0  
    Arrays.fill(arr, 10);  
    System.out.println(Arrays.toString(arr));  
  
    // 不包含toIndex  
    Arrays.fill(arr, 1, 3, 100);  
    System.out.println(Arrays.toString(arr));  
}
```

---
## asList

```java
Integer[] a1 = new Integer[]{1,2,3};  
List l1 = Arrays.asList(a1);  
System.out.println(l1.toString()); // [1, 2, 3]
System.out.println(l1.getClass()); // class java.util.Arrays$ArrayList(这个是运行类型)
```

---
## 练习

Arrays类课堂练习
ArrayExercise.java
案例: 自定义Book类, 里面包含name和price, 按price排序(从大到小)。要求使用两种方式排序，对对象的某个属性排序, 有一个 Book[] books = 5本书对象.
使用前面学习过的传递实现Comparator接口匿名内部类, 也称为定制排序。
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

通过流的方式简化一下
```java
System.out.println("按照价格升序");
Arrays.sort(books, Comparator.comparingInt(Book::getPrice));
Arrays.stream(books).forEach(System.out::println);

System.out.println("按照价格降序");
Arrays.sort(books, Comparator.comparingInt(Book::getPrice).reversed());
Arrays.stream(books).forEach(System.out::println);

System.out.println("按照名字长度");
Arrays.sort(books, Comparator.comparingInt(book -> book.getName().length()));
Arrays.stream(books).forEach(System.out::println);
```