通过反编译(javap)，可以看到上边的季节类型如下
```java
// 可以看到这是一个 final 类所以不能有子类了，但是可以弄接口
// 也可以发现， Season 默认继承了 Enum
final class ex_enum.Season extends java.lang.Enum<ex_enum.Season>{
  // 我们用 enum 定义的和 public static final 其实是一样的
  public static final ex_enum.Season SPRING; 
  public static final ex_enum.Season SUMMER;
  public static final ex_enum.Season AUTUMN;
  public static final ex_enum.Season WINTER;
  public static ex_enum.Season[] values(); // 可以看到这里有一个方法
  public static ex_enum.Season valueOf(java.lang.String);
  public java.lang.String getName();
  public java.lang.String getDesc();
  public java.lang.String toString();
  static {};
}
```