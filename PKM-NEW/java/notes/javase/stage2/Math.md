# Math

```java
public class MathDemo {
    public static void main(String[] args) {
        // 绝对值
        double absValue = Math.abs(-5.5);
        System.out.println("绝对值: " + absValue);

        // 最大值和最小值
        double maxVal = Math.max(3.14, 2.71);
        double minVal = Math.min(3.14, 2.71);
        System.out.println("最大值: " + maxVal);
        System.out.println("最小值: " + minVal);

        // 四舍五入
        int roundVal = Math.round(3.14159);
        System.out.println("四舍五入: " + roundVal);

        // 向上取整
        double ceilVal = Math.ceil(3.14);
        System.out.println("向上取整: " + ceilVal);

        // 向下取整
        double floorVal = Math.floor(3.14);
        System.out.println("向下取整: " + floorVal);

        // 指数
        double expVal = Math.exp(2);
        System.out.println("e 的指数: " + expVal);

        // 对数
        double logVal = Math.log(8);
        System.out.println("自然对数: " + logVal);

        // 平方根
        double sqrtVal = Math.sqrt(16);
        System.out.println("平方根: " + sqrtVal);

        // 随机数
        double randomVal = Math.random();
        System.out.println("随机数: " + randomVal);

        // 角度和弧度转换
        double toRadians = Math.toRadians(90);
        double toDegrees = Math.toDegrees(toRadians);
        System.out.println("角度转弧度: " + toRadians);
        System.out.println("弧度转角度: " + toDegrees);

        // 三角函数
        double sinVal = Math.sin(Math.toRadians(30));
        double cosVal = Math.cos(Math.toRadians(30));
        double tanVal = Math.tan(Math.toRadians(30));
        System.out.println("正弦值: " + sinVal);
        System.out.println("余弦值: " + cosVal);
        System.out.println("正切值: " + tanVal);
    }
}
```