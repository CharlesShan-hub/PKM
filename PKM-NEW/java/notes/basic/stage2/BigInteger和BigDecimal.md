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