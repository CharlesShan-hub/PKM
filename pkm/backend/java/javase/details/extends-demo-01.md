基础案例

```java
package com.charles.extends_;
public class AiGuo{
   public static void main(String[] args){
       Province p = new Province();
       System.out.println(p.toString());
   }
}
class Country{
   String country = "中国";
   @Override
   public String toString(){
       return "这里是"+this.country;
   }
}
class Province extends Country{
   String province = "台湾省";
   @Override
   public String toString(){
       return "这里是"+this.country+this.province;
   }
}
// print:
// 这里是中国台湾省
```
