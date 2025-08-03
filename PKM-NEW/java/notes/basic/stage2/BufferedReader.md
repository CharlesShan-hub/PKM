# BufferedReader

## 简介

* BufferedReader是带缓冲的字符输入流，可以提高读取效率
* 继承体系：
    * java.lang.Object
    * java.io.Reader
    * java.io.BufferedReader
* 主要特点：
    * 内置缓冲区(**默认8KB**)，减少实际IO操作次数
    * 提供readLine()方法，方便按行读取文本
    * 通常包装其他Reader(如FileReader)使用

* 常用构造方法：
    * `BufferedReader(Reader in)`：使用默认缓冲区大小
    * `BufferedReader(Reader in, int size)`：指定缓冲区大小

* 常用方法：
    * `read()`：读取单个字符
    * `read(char[] cbuf)`：读取字符到数组
    * `readLine()`：读取一行文本(不包含换行符)
    * `lines()`：返回包含所有行的Stream\<String\>
    * `close()`：关闭流

* 示例代码：

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class BufferedReaderExample {
    public static void main(String[] args) {
        String filePath = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/a.txt";
        
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            // 方式1：逐行读取
            System.out.println("--* 逐行读取 ---");
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            // 方式2：使用Stream API
            System.out.println("\n--* 使用Stream API ---");
            br.lines().forEach(System.out::println);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

源码的构造方法中可以看到，提供了缓冲机制。可以看到默认有8192长度的缓冲。

```java
public class BufferedReader extends Reader {
	private Reader in;
	// ...
	private static final int DEFAULT_CHAR_BUFFER_SIZE = 8192;
	// ...  
	
	public BufferedReader(Reader in, int sz) {  
	    super(in);  
	    if (sz <= 0)  
	        throw new IllegalArgumentException("Buffer size <= 0");  
	    this.in = in;  
	    cb = new char[sz];  
	    nextChar = nChars = 0;  
	}  
	  
	/**  
	 * Creates a buffering character-input stream that uses a default-sized 
	 * input buffer. 
	 * 
	 * @param  in   A Reader  
	 */
	 public BufferedReader(Reader in) {  
	    this(in, DEFAULT_CHAR_BUFFER_SIZE);  
	}
	// ...
}
```

## `mark`和`reset`

```java
package hsp.ex_file;  
  
import java.io.*;  
  
public class Buffered {  
    public static void main(String[] args) throws IOException {  
        File file = new File("/Users/kimshan/Downloads/S0030399225006668.bib");  
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {  
            // 设置标记前需要先检查是否支持mark操作  
            if (br.markSupported()) {  
                System.out.println("BufferedReader支持mark操作");  
  
                // 读取第一行  
                String line1 = br.readLine();  
                System.out.println("第一行: " + line1);  
  
                // 设置标记，参数表示在重置前可以读取的最大字符数  
                // 高版本JDK失效  
                br.mark(1000);  
  
                // 继续读取几行  
                String line2 = br.readLine();  
                System.out.println("第二行: " + line2);  
  
                String line3 = br.readLine();  
                System.out.println("第三行: " + line3);  
  
                // 重置到标记位置  
                System.out.println("执行reset操作...");  
                br.reset();  
  
                // 重新读取标记后的行  
                String resetLine2 = br.readLine();  
                System.out.println("重置后第二行: " + resetLine2);  
  
                String resetLine3 = br.readLine();  
                System.out.println("重置后第三行: " + resetLine3);  
            } else {  
                System.out.println("BufferedReader不支持mark操作");  
            }  
        }catch (IOException e){  
            e.printStackTrace();  
        }  
    }  
}  
  
// BufferedReader支持mark操作  
//第一行: @article{WU2025113075,  
//第二行: title = {FoggyFuse: Infrared and visible image fusion method based on saturation line prior in foggy conditions},  
//第三行: journal = {Optics & Laser Technology},  
//执行reset操作...  
//重置后第二行: title = {FoggyFuse: Infrared and visible image fusion method based on saturation line prior in foggy conditions},  
//重置后第三行: journal = {Optics & Laser Technology},
```
