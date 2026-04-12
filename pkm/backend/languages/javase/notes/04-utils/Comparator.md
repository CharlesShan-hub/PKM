# Comparator

---

## 1. Comparator 概述

`java.util.Comparator`是一个功能接口，用于对对象集合进行总排序。

```java
int compare(T o1, T o2)
```

* 当 o1 < o2 时，返回负整数
* 当 o1 = o2 时，返回 0
* 当 o1 > o2 时，返回正整数

## 2. 基本使用方法

### 2.1 Lambda 表达式定义比较器

```java
Comparator<Student> ageComp = (s1, s2) -> s1.getAge() - s2.getAge();
Comparator<Student> nameComp = (s1, s2) -> s1.getName().compareTo(s2.getName());
```

### 2.2 自定义 Comparator 实现

```java
class AgeComparator implements Comparator<Student>, Serializable {
    @Override
    public int compare(Student s1, Student s2) {
        return s1.getAge() - s2.getAge();
    }
}
```

## 3. Comparator 的使用场景

### 3.1 Stream.sorted

```java
list.stream().sorted(ageComp).forEach(s -> System.out.println(s));
```

### 3.2 Collections.sort

```java
Collections.sort(list, ageComp);
```

### 3.3 List.sort

```java
list.sort(ageComp);
```

### 3.4 Arrays.sort

```java
Arrays.sort(array, ageComp);
```

## 4. Comparator 的重要方法

### 4.1 reversed() - 反向排序

```java
list.stream().sorted(ageComparator.reversed())
```

### 4.2 reverseOrder() - 反向自然排序

```java
Collections.sort(numList, Comparator.reverseOrder());
```

### 4.3 naturalOrder() - 自然排序

```java
numList.sort(Comparator.naturalOrder());
```

### 4.4 nullsFirst() / nullsLast() - 处理 null 值

```java
// null 值排在前面
Collections.sort(list, Comparator.nullsFirst(Comparator.comparing(Student::getName)));

// null 值排在后面
Collections.sort(list, Comparator.nullsLast(Comparator.comparing(Student::getName)));
```

### 4.5 comparing() 方法族

```java
// 基本形式
Comparator<Student> nameComparator = Comparator.comparing(Student::getName);

// 带自定义比较器
Comparator<Student> nameComparator = Comparator.comparing(Student::getName, 
    (s1, s2) -> s2.compareTo(s1));

// 基本数据类型专用
Comparator.comparingInt(Student::getAge)
Comparator.comparingLong(Student::getHomeDistance)
Comparator.comparingDouble(Student::getWeight)
```

### 4.6 thenComparing() 方法族 - 多级排序

```java
// 多级排序示例
Comparator<Student> comparator = Comparator.comparing(Student::getSchool)
    .thenComparing(Student::getAge)
    .thenComparing(Student::getName);

// 基本数据类型专用
.thenComparingInt(Student::getAge)
.thenComparingLong(Student::getHomeDistance)
.thenComparingDouble(Student::getWeight)
```

## 5. 在集合中的使用

### 5.1 SortedSet 中使用（TreeSet, ConcurrentSkipListSet）

```java
// TreeSet 使用比较器
Comparator<Student> ageComparator = Comparator.comparing(Student::getAge);
TreeSet<Student> myTreeSet = new TreeSet<>(ageComparator);

// ConcurrentSkipListSet 使用比较器
ConcurrentSkipListSet<Student> mySet = new ConcurrentSkipListSet<>(ageComparator);
```

### 5.2 SortedMap 中使用（TreeMap, ConcurrentSkipListMap）

```java
// TreeMap 使用比较器
TreeMap<Student, String> myTreeMap = new TreeMap<>(ageComparator);

// ConcurrentSkipListMap 使用比较器
ConcurrentSkipListMap<Student, String> myMap = new ConcurrentSkipListMap<>(ageComparator);
```

## 6. 完整示例代码

### Student 类定义

```java
public class Student implements Comparable<Student> {
    private String name;
    private int age;
    private long homeDistance;
    private double weight;
    private School school;
    
    // 构造方法、getter、setter
    
    @Override
    public int compareTo(Student s) {
        return name.compareTo(s.getName());
    }
    
    public static List<Student> getStudentList() {
        // 返回学生列表
    }
}
```

### School 类定义

```java
public class School implements Comparable<School> {
    private String sname;
    private String city;
    
    @Override
    public int compareTo(School s) {
        return s.getCity().compareTo(city);
    }
}
```

## 7. 参考资料

* https://blog.csdn.net/qq_31635851/article/details/120269813