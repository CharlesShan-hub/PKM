# FileWriter

注意⚠️
1. 如果不调用`flush()`或者`close()`方法，数据不会被写入文件。
2. 构造的时候如果传入的是`true`，则会在文件末尾追加写入，而不是覆盖。
3. 构造的时候如果传入的是`false`（默认），则会覆盖写入。

```java
import java.io.FileWriter;
import java.io.IOException;

public class FileExample {
    public static void main(String[] args) {
        String path = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/a.txt";
        try (FileWriter fos = new FileWriter(path)) { // 覆盖写
            System.out.println("写入单个字符");
            fos.write('I');
            System.out.println("写入字符数组");
            char[] chars = {'H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!'};
            fos.write(chars);
            System.out.println("写入字符串");
            fos.write("Hello, World! I'm FileWriter.");
            System.out.println("写入字符串/字符数组的一部分");
            fos.write("Hello, World! I'm FileWriter.", 0, 13); // 写入字符串的前13个字符
            fos.close(); // 关闭文件写入器，释放资源
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
