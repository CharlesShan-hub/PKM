# BufferedReader

* BufferedReader是带缓冲的字符输入流，可以提高读取效率
* 继承体系：
    * java.lang.Object
    * java.io.Reader
    * java.io.BufferedReader
* 主要特点：
    * 内置缓冲区(默认8KB)，减少实际IO操作次数
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