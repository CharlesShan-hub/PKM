# IO流

---
## ✏️ IO 流

### 流的原理
1. 字符流（文本文件）、字节流（二进制文件）
2. 输入流、输出流
3. 节点流/低级流、处理流/包装流：包装流就是本身不能工作，需要包装进来一个别的类来工作。
4. 四个抽象基类
	1. 字节流+输入流：`InputStream`
	2. 字节流+输出流：`OutPutStream`
	3. 字符流+输入流：`Reader`
	4. 字符流+输出流：`Writer`

### 流的分类
![io-drawing|1000](../../../assets/io-drawing.md)

|       分类       |                      字节输入流                      |                       字节输出流                       |                字符输入流                |                字符输出流                | 节点流/处理流 |
| :------------: | :---------------------------------------------: | :-----------------------------------------------: | :---------------------------------: | :---------------------------------: | :-----: |
|  ​**​抽象基类​**​  |                   InputStream                   |                   OutputStream                    |               Reader                |               Writer                |  （基类）   |
|  ​**​访问文件​**​  |      [FileInputStream](FileInputStream.md)      |      [FileOutputStream](FileOutputStream.md)      |     [FileReader](FileReader.md)     |     [FileWriter](FileWriter.md)     |   节点流   |
| ​**​访问字节数组​**​ | [ByteArrayInputStream](ByteArrayInputStream.md) | [ByteArrayOutputStream](ByteArrayOutputStream.md) |           CharArrayReader           |           CharArrayWriter           |   节点流   |
|  ​**​访问管道​**​  |                PipedInputStream                 |                 PipedOutputStream                 |             PipedReader             |             PipedWriter             |   节点流   |
|  ​**​缓冲流​**​   |               BufferedInputStream               |               BufferedOutputStream                | [BufferedReader](BufferedReader.md) | [BufferedWriter](BufferedWriter.md) |   处理流   |
|  ​**​转换流​**​   |    [InputStreamReader](InputStreamReader.md)    |    [OutputStreamWriter](OutputStreamWriter.md)    |                  -                  |                  -                  |   处理流   |
|  ​**​对象流​**​   |    [ObjectInputStream](ObjectInputStream.md)    |    [ObjectOutputStream](ObjectOutputStream.md)    |                  -                  |                  -                  |   处理流   |
|  ​**​抽象基类​**​  |                FilterInputStream                |                FilterOutputStream                 |            FilterReader             |            FilterWriter             | 处理流（基类） |
|  ​**​打印流​**​   |          [PrintStream](PrintStream.md)          |                         -                         |    [PrintWriter](PrintWriter.md)    |                  -                  |   处理流   |
| ​**​推回输入流​**​  |               PushbackInputStream               |                         -                         |           PushbackReader            |                  -                  |   处理流   |
|  ​**​特殊流​**​   |      [DataInputStream](DataInputStream.md)      |      [DataOutputStream](DataOutputStream.md)      |            StringReader             |            StringWriter             |   节点流   |

---
## 🍭 标准输入输出

### 标准输入

* 源码：`public final static InputStream in = null;`
* `System.in`编译类型：`InputStream`
* `System.in`运行类型：`BufferedInputStream`
```java
public class SystemInTest {
	public static void main(String[] args) {
		System.out.println(System.in.getClass());
		// class java.io.BufferedInputStream
	}
}
```
* 案例
```java
package com.powernode.javase.io;  
  
import java.io.FileInputStream;  
import java.io.InputStream;  
import java.util.Scanner;  
  
/**  
 * 标准输入流：System.in  
 *      1. 标准输入流怎么获取？  
 *          System.in  
 *      2. 标准输入流是从哪个数据源读取数据的？  
 *          控制台。  
 *      3. 普通输入流是从哪个数据源读取数据的？  
 *          文件或者网络或者其他.....  
 *      4. 标准输入流是一个全局的输入流，不需要手动关闭。JVM退出的时候，JVM会负责关闭这个流。  
 */  
public class SystemInTest {  
    public static void main(String[] args) throws Exception{  
  
        // 获取标准输入流对象。（直接通过系统类System中的in属性来获取标准输入流对象。）  
        InputStream in = System.in;  
  
        // 开始读  
        byte[] bytes = new byte[1024];  
        int readCount = in.read(bytes);  
  
        for (int i = 0; i < readCount; i++) {  
            System.out.println(bytes[i]);  
        }  
    }  
}
```
* 修改数据源
```java
package com.powernode.javase.io;  
  
import java.io.FileInputStream;  
import java.io.InputStream;  
  
/**  
 * 对于标准输入流来说，也是可以改变数据源的。不让其从控制台读数据。也可以让其从文件中或网络中读取数据。  
 */  
public class SystemInTest02 {  
    public static void main(String[] args) throws Exception{  
        // 修改标准输入流的数据源。  
        System.setIn(new FileInputStream("log2"));  
  
        // 获取标准输入流  
        InputStream in = System.in;  
  
        byte[] bytes = new byte[1024];  
        int readCount = 0;  
        while((readCount = in.read(bytes)) != -1){  
            System.out.print(new String(bytes, 0, readCount));  
        }  
  
    }  
}
```
### 标准输出

* 源码：`public final static PrintStream out = null;`
* `System.out.print()`就是`System.in.write()`
* `System.out`编译类型：`PrintStream`
* `System.out`运行类型：`PrintStream`
```java
public class SystemInTest {
	public static void main(String[] args) {
		System.out.println(System.out.getClass());
		// class java.io.PrintStream
	}
}
```

```java
package com.powernode.javase.io;  
  
import java.io.PrintStream;  
import java.text.SimpleDateFormat;  
import java.util.Date;  
  
/**  
 * 标准输出流：System.out  
 *      1. 标准输出流怎么获取？  
 *          System.out  
 *      2. 标准输出流是向哪里输出呢？  
 *          控制台。  
 *      3. 普通输出流是向哪里输出呢？  
 *          文件或者网络或者其他.....  
 *      4. 标准输出流是一个全局的输出流，不需要手动关闭。JVM退出的时候，JVM会负责关闭这个流。  
 */  
public class SystemOutTest {  
    public static void main(String[] args) throws Exception {  
  
        // 获取标准输出流，标准输出流默认会向控制台输出。  
        PrintStream out = System.out;  
  
        // 输出  
        out.println("hello world");  
        out.println("hello world");  
  
        // 标准输出流也是可以改变输出方向的。  
        System.setOut(new PrintStream("log"));  
  
        System.out.println("zhangsan");  
        System.out.println("lisi");  
        System.out.println("wangwu");  
        System.out.println("zhaoliu");  
  
        // 获取系统当前时间  
        Date now = new Date();  
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss SSS");  
        String str = sdf.format(now);  
        System.out.println(str + ": SystemOutTest's main method invoked!");  
    }  
}
```

---
## 🍭 配置文件
### Properties

1. 介绍：
	* `Properties`类继承自`Hashtable`类，用于处理属性文件
	* 键值对都是字符串类型
	* 常用于读取配置文件
2. 常用方法：
	* `load(InputStream inStream)`：从输入流中加载属性列表
	* `list(PrintStream out)`：将属性列表输出到指定的输出流
	* `setProperty(String key, String value)`：设置属性值
	* `getProperty(String key)`：获取属性值
	* `store(OutputStream out, String comments)`：将属性列表写入输出流
3. 示例：
	```java
	import java.io.*;
	import java.util.Properties;
	
	public class PropertiesExample {
	    public static void main(String[] args) {
	        String filePath = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/config.properties";
			File file = new File(filePath);
			if(!file.exists()){
				try {
					file.createNewFile();
				} catch (IOException e) {
					throw new RuntimeException(e);
				}
			}
			Properties props = new Properties();
	        // 加载属性文件
	        try (InputStream in = new FileInputStream(filePath)) {
	            props.load(in);
				System.out.println(props.getProperty("username"));
				props.list(System.out);
	            // 获取属性值
	            String username = props.getProperty("username");
	            String password = props.getProperty("password");
				props.store(new FileOutputStream(filePath), "update");
	        }catch (IOException e) {
	            e.printStackTrace();
	        }
	    }
	}
	```
	
### ResourceBundle资源绑定

配置文件如下

```properties
#connect mysql database info  
driver=com.mysql.cj.jdbc.Driver  
url=jdbc:mysql://192.168.137.154:3306/powernode  
user=admin  
password=11111
```

代码
```java
package com.powernode.javase.io;  
  
import java.util.ResourceBundle;  
  
/**  
 * 使用JDK中提供的资源绑定器来绑定属性配置文件。  
 */  
public class BundleProperties {  
    public static void main(String[] args) {  
        // 获取资源绑定器对象  
        // 使用这个工具要求文件也必须是一个属性配置文件，比如 jdbc.properties  
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.javase.io.jdbc");  
        //ResourceBundle bundle = ResourceBundle.getBundle("com/powernode/javase/io/jdbc"); // 这种也可以
  
        // 这个获取的是类的根路径下的jdbc.properties文件。  
        //ResourceBundle bundle = ResourceBundle.getBundle("jdbc");  
        // 这个代码的意思是从类的根路径下找db.properties文件。  
        //ResourceBundle bundle = ResourceBundle.getBundle("db");  
  
        // 以下两行都是错误的：资源找不到。  
        //ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.javase.io.db.properties");  
        //ResourceBundle bundle = ResourceBundle.getBundle("com/powernode/javase/io/db.properties");  
        // 通过key获取value  
        String driver = bundle.getString("driver");  
        String url = bundle.getString("url");  
        String user = bundle.getString("user");  
        String password = bundle.getString("password");  
  
        System.out.println(driver);  
        System.out.println(url);  
        System.out.println(user);  
        System.out.println(password);  
    }  
}
```

