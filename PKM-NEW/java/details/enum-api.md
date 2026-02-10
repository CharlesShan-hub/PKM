
```java
enum Color {
  RED, GREEN, BLUE;
}

public class EnumExample {
  public static void main(String[] args) {
    Color myColor = Color.RED;

    // 使用 valueOf 获取枚举常量
    Color color = Enum.valueOf(Color.class, "RED");
    System.out.println("ValueOf: " + color);//ValueOf: RED

    // 使用 toString 获取枚举常量名称
    System.out.println("ToString: " + myColor.toString());//ToString: RED

    // 使用 equals 比较两个枚举常量
    if (myColor.equals(color)) {
      System.out.println("The colors are the same.");//The colors are the same.
    }

    // 使用 hashCode 和 equals 保持一致
    int hashCode = myColor.hashCode();
    System.out.println("HashCode: " + hashCode);//HashCode: 1867083167

    // 获取 Class 对象
    Class<? extends Color> colorClass = myColor.getDeclaringClass();
    System.out.println("Class: " + colorClass);//Class: class ex_enum.Color

    // 使用 name 获取枚举常量名称
    System.out.println("Name: " + myColor.name());//Name: RED

    // 使用 ordinal 获取枚举常量的次序
    int ordinal = myColor.ordinal();
    System.out.println("Ordinal: " + ordinal);//Ordinal: 0

    // 使用 compareTo 比较枚举常量
    int comparison = myColor.compareTo(Color.GREEN);
    System.out.println("Comparison: " + comparison);//Comparison: -1

    // 尝试克隆枚举常量
    try {
      Color clonedColor = myColor.clone();
    } catch (CloneNotSupportedException e) {
      System.out.println("Clone not supported: " + e.getMessage());
    }
  }
}
```
