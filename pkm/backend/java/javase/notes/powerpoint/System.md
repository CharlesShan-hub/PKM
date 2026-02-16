# java.lang.System类的常用方法

常用属性
```java
static final PrintStream err //标准错误输出流（System.err.println(“错误信息”);输出红色字体）
static final InputStream in 标准输入流
static final PrintStream out 标准输出流
```

比如把`system.out`保存成`PrintStream`

```java
package com.powernode.javase.systemtest;  
  
import java.io.InputStream;  
import java.io.PrintStream;  
import java.util.Scanner;  
  
/**  
 * java.lang.System 系统类。  
 */  
public class SystemTest {  
    public static void main(String[] args) {  
  
        // 标准的错误输出  
        System.err.println("这是一个错误信息");  
  
        try {  
            int a = 10;  
            int b = 0;  
            System.out.println(a / b);  
        } catch(ArithmeticException e){  
            System.err.println("除数不能为0");  
        }  
  
        System.out.println("hello world!");  
  
        PrintStream printStream = System.out;  
        printStream.println(100);  
        printStream.println(false);  
        printStream.println("123");  
        printStream.println(1.23);  
  
        Scanner s = new Scanner(System.in);  
        System.out.println(s.next());  
  
        InputStream inputStream = System.in;  
        Scanner s2 = new Scanner(inputStream);  
        System.out.println(s2.next());  
    }  
}
```

常用方法：
```java
static void arraycopy(Object src, int srcPos, Object dest, int destPos, int length); 数组拷贝
static void exit(int status); 退出虚拟机
static void gc(); 建议启动垃圾回收器
static long currentTimeMillis(); 获取自1970-01-01 00:00:00 000到系统当前时间的总毫秒数
static long nanoTime(); 获取自1970年1月1日0时0分0秒以来，当前时间的纳秒数
static Map<String,String> getenv(); 获取当前系统的环境变量，例如Path，JAVA_HOME，CLASSPATH等。
static Properties getProperties(); 获取当前系统的属性。
static String getProperty(String key); 通过key获取指定的系统属性。
```

```java
package com.powernode.javase.systemtest;  
  
import java.util.Enumeration;  
import java.util.Map;  
import java.util.Properties;  
  
public class SystemTest02 {  
    public static void main(String[] args) {  
        // 获取自1970-1-1 0:0:0 000到系统当前时间的总毫秒数  
        long l = System.currentTimeMillis();  
        System.out.println(l);  
  
        // 获取自1970-1-1 0:0:0 000到系统当前时间的总纳秒数  
        long l1 = System.nanoTime();  
        System.out.println(l1);  
  
        // 获取系统的环境变量  
        Map<String, String> map = System.getenv();  
        System.out.println(map);  
        System.out.println(map.get("Path"));  
          
        // 获取系统所有的属性  
        Properties pro = System.getProperties();  
        System.out.println(pro);  
  
        System.out.println("==========================");  
        Enumeration<Object> keys = pro.keys(); // 获取所有属性的名字。  
        // 遍历名字。  
        while(keys.hasMoreElements()){  
            Object o = keys.nextElement();  
            System.out.println(o);  
        }  
        System.out.println("==========================");  
  
        // 根据系统属性的名字获取属性的值  
        String vmName = System.getProperty("java.vm.name");  
        System.out.println(vmName);  
  
        System.out.println(System.getProperty("os.name"));  
    }  
}
```