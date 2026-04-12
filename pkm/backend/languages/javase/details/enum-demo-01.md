按照传统方法创建`Season`类：
```java
package ex_enum;  

public class Test {  
  public static void main(String[] args){  
    Season spring = new Season("春天", "当第一株小草🪴发芽，我在想你");  
    Season summer = new Season("夏天", "当第一声蝉鸣🌳划过，我在想你");  
    Season autumn = new Season("秋天", "当第一棵树木🍁变黄，我在想你");  
    Season winter = new Season("冬天", "当第一片雪花❄️飘落，我在想你");  
    Season night  = new Season("黑天", "当太阳褪去光辉✨，我在想你");  
    Season day    = new Season("白天", "当星星沉入海底☀️，我在想你");  

    // 这样不能提现对象的有限性，所以需要枚举  
    // 思念跨越时间，而我只有四季  
  }  
}  

class Season{  
  private String name;  
  private String decs;  
  public Season(String name, String decs){  
    this.name = name;  
    this.decs = decs;  
  }  
  public String getDecs() {  
    return decs;  
  }  
  public String getName() {  
    return name;  
  }  
  public void setName(String name) {  
    this.name = name;  
  }  
  public void setDecs(String decs) {  
    this.decs = decs;  
  }
}
```
