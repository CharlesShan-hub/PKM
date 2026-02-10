
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

enum Season{  
  // 1. 使用关键字 enum 替代 class    
  // 2. 定义的对象，使用名称替代  
  // 3. 把属性定义放到后边  
  // 4. 多个对象使用对象间  
  SPRING("春天","春困"),  
  SUMMER("夏天","夏打盹"),  
  AUTUMN("秋天","秋乏"),  
  WINTER("冬天","冬三月");  
  // public final static Season SPRING = new Season("春天","春困");  
  // public final static Season SUMMER = new Season("夏天","夏打盹");  
  // public final static Season AUTUMN = new Season("秋天","秋乏");  
  // public final static Season WINTER = new Season("冬天","冬三月");  

  private String name;  
  private String decs;  

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
