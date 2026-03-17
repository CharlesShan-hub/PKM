使用单例设计模式：
1. 将构造器**私有化**, 目的防止直接 `new`
2. 去掉 `setter`，防止属性被篡改
3. 在 `Season` 内部，直接创建固定的对象
4. 还可以加入 `final`，优化一下性能
```java
package ex_enum;

public class Test {
  public static void main(String[] args){
    System.out.println(Season.SPRING); // 没有你的春天，那便沉沉睡去...
    System.out.println(Season.SUMMER); // 没有你的夏天，那便沉沉睡去...
    System.out.println(Season.AUTUMN); // 没有你的秋天，那便沉沉睡去...
    System.out.println(Season.WINTER); // 没有你的冬天，那便沉沉睡去...
  }
}

class Season{
  private String name;
  private String decs;

  public final static Season SPRING = new Season("春天","春困");
  public final static Season SUMMER = new Season("夏天","夏打盹");
  public final static Season AUTUMN = new Season("秋天","秋乏");
  public final static Season WINTER = new Season("冬天","冬三月");
    
  private Season(String name, String decs){
    this.name = name;
    this.decs = decs;
  }
  @Override
  public String toString(){
    return "没有你的"+this.name+"，那便沉沉睡去...";
  }
  public String getDecs() {
    return decs;
  }
  public String getName() {  
    return name;  
  }
}
```
