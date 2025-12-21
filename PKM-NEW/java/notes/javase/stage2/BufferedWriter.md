# BufferedWriter

提供了缓冲机制，能够减少对底层流的频繁访问，从而提高写入效率。

```java
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class BufferedWriterExample{
    public static void main(String[] args) {
        String path = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/a.txt";
        // try (BufferedWriter bw = new BufferedWriter(new FileWriter(path, true))) { // 追加模式
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(path))) { // 覆盖模式
            System.out.println("\n--- 使用BufferedWriter写入文件 ---");
            bw.write("Hello, BufferedWriter!");
            bw.newLine(); // 写入换行符, 会根据系统自动转换为对应的换行符
            bw.write("This is a test.");
        }catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

案例：文件拷贝

注意⚠️，`BufferedReader`和`BufferedWriter`是字符流，不要去操作二进制文件，如图片、视频等，因为字符流是按字符操作的，而二进制文件是按字节操作的。

```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class FileCopyExample {
    public static void main(String[] args) {
        String sourceFile = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/a.txt";
        String targetFile = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/a_copy.txt";
        try{
            BufferedReader br = new BufferedReader(new FileReader(sourceFile));
            BufferedWriter bw = new BufferedWriter(new FileWriter(targetFile));
            String line;
            while ((line = br.readLine()) != null) {
                bw.write(line);
                bw.newLine();
            }
            System.out.println("文件拷贝完成！");
            br.close();
            bw.close();
        }catch (IOException e) {
            e.printStackTrace();
        }
    }
}