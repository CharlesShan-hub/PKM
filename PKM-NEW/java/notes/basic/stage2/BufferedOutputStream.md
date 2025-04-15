# BufferedOutputStream

在案例[[BufferedWriter]]中，我们不能备份二进制文件，因为BufferedWriter是字符流，只能处理文本文件。

这时就需要用到 BufferedOutputStream 和 BufferedInputStream 来处理二进制文件。


```java
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class FileCopyExample {
    public static void main(String[] args) {
        String sourceFile = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/mc.png";
        String targetFile = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/mc1.png";
        try{
            BufferedInputStream bis = new BufferedInputStream(new FileInputStream(sourceFile));
            BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(targetFile));
            byte[] buffer = new byte[1024];
            int bytesRead;
            while ((bytesRead = bis.read(buffer))!= -1) {
                bos.write(buffer, 0, bytesRead);
            }
            bis.close();
            bos.close();
            System.out.println("文件复制完成");
        }catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```