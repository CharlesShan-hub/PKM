# Random

![1000](java-basic-random.excalidraw)
```java
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;
import java.util.stream.IntStream;

public class RandomExample {
    public static void main(String[] args) {
        System.out.println("=== 1. 基本 Random 类 ===");
        Random random = new Random();
        
        // 1.1 生成随机整数
        System.out.println("随机整数: " + random.nextInt());
        System.out.println("0-99的随机整数: " + random.nextInt(100));
        
        // 1.2 生成随机长整数
        System.out.println("随机长整数: " + random.nextLong());
        
        // 1.3 生成随机浮点数
        System.out.println("随机float (0.0-1.0): " + random.nextFloat());
        System.out.println("随机double (0.0-1.0): " + random.nextDouble());
        
        // 1.4 生成随机布尔值
        System.out.println("随机布尔值: " + random.nextBoolean());
        
        // 1.5 生成随机字节数组
        byte[] bytes = new byte[5];
        random.nextBytes(bytes);
        System.out.print("随机字节数组: ");
        for (byte b : bytes) {
            System.out.print(b + " ");
        }
        System.out.println();
        
        // 1.6 设置种子（可重现的随机序列）
        Random seededRandom = new Random(12345L);
        System.out.println("带种子的随机数1: " + seededRandom.nextInt(100));
        System.out.println("带种子的随机数2: " + seededRandom.nextInt(100));
        
        System.out.println("\n=== 2. 高斯分布（正态分布） ===");
        System.out.println("高斯分布随机数: " + random.nextGaussian());
        
        System.out.println("\n=== 3. 使用 Stream API ===");
        IntStream randomInts = random.ints(5, 0, 100);
        System.out.print("5个0-99的随机数: ");
        randomInts.forEach(n -> System.out.print(n + " "));
        System.out.println();
        
        System.out.print("5个随机double: ");
        random.doubles(5).forEach(d -> System.out.print(d + " "));
        System.out.println();
        
        System.out.println("\n=== 4. ThreadLocalRandom（多线程推荐） ===");
        ThreadLocalRandom tlr = ThreadLocalRandom.current();
        System.out.println("ThreadLocalRandom 整数: " + tlr.nextInt(100));
        System.out.println("指定范围的随机数: " + tlr.nextInt(10, 100)); // 10-99
        
        System.out.println("\n=== 5. 数学类 Math.random() ===");
        System.out.println("Math.random(): " + Math.random()); // 0.0-1.0的double
        
        System.out.println("\n=== 6. 实用示例 ===");
        // 6.1 随机选择数组元素
        String[] colors = {"红", "绿", "蓝", "黄", "紫"};
        System.out.println("随机颜色: " + colors[random.nextInt(colors.length)]);
        
        // 6.2 生成指定范围的随机数
        int min = 50, max = 100;
        int rangeRandom = random.nextInt(max - min + 1) + min;
        System.out.println("50-100的随机数: " + rangeRandom);
        
        // 6.3 概率判断
        double probability = 0.3; // 30%概率
        System.out.println("30%概率事件发生: " + (random.nextDouble() < probability));
    }
}
```