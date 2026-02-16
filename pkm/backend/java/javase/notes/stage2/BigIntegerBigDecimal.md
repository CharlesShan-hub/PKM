# BigInteger and BigDecimal
---

1. 加减乘除需要调用方法
	```java
	BigDecimal a = new BigDecimal("1111111111111111111111111.");  
	System.out.println(a);  
	BigInteger b = new BigInteger("1111111111111111111111111");  
	System.out.println(b);  
	// a+b 不行，不能直接加减乘除，需要使用相应的方法  
	System.out.println(a.add(new BigDecimal("100")));  
	System.out.println(b.add(new BigInteger("200")));
	```

2. ❗️BigDecimal，除法，如果除不尽，会抛出异常！！
	```java
	import java.math.BigDecimal;
	import java.math.RoundingMode;
	
	public class BigDecimalDivisionExample {
	    public static void main(String[] args) {
	        // 创建两个 BigDecimal 对象
	        BigDecimal dividend = new BigDecimal("10");
	        BigDecimal divisor = new BigDecimal("3");
	
	        // 指定除法运算的精度和小数点后的舍入模式
	        int scale = 2; // 指定小数点后保留两位（这里是通过保留分子的精度，然后一起保留结果的精度）
	        RoundingMode roundingMode = RoundingMode.HALF_UP; // 四舍五入
	
	        // 执行除法运算并指定精度
	        BigDecimal result = dividend.divide(divisor, scale, roundingMode);
	
	        // 输出结果
	        System.out.println("除法结果（保留两位小数）: " + result);
	    }
	}
	
	```

3. 格式化
java.text.DecimalFormat 类是专门用来对数字进行格式的。
常用数字格式：
###,###.##    // 三个数字为一组，组和组之间使用逗号隔开，保留两位小数
###,###.0000  // 三个数字为一组，组和组之间使用逗号隔开，保留4位小数，不够补0
构造方法：DecimalFormat(String pattern)
常用方法：String format(数字);

```java
package com.powernode.javase.bignumtest;  
  
import java.text.DecimalFormat;  
  
/**  
 * 数字的格式化展示的时候，需要使用这个类。  
 */  
public class DecimalFormatTest {  
    public static void main(String[] args) {  
  
        // 创建一个数字格式化对象  
        DecimalFormat df = new DecimalFormat("###,###.##");  
  
        // 格式化  
        String s = df.format(12345678.123);  
  
        System.out.println(s); // "12,345,678.12"  
  
        // 保留四位小数，要求不够补0  
        DecimalFormat df2 = new DecimalFormat("###,###.0000");  
        String s2 = df2.format(12345678.123);  
        System.out.println(s2); // "12,345,678.1230"  
    }  
}
```

