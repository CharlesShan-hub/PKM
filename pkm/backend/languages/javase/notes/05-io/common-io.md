# Commons IO

Apache Commons IO 是一个常用的 Java IO 工具库，提供了许多方便的类和方法来处理文件和流的操作，大大简化了 IO 编程。

> <https://commons.apache.org/proper/commons-io/>

## 引入依赖

```xml
<dependency>  
    <groupId>commons-io</groupId>  
    <artifactId>commons-io</artifactId>  
    <version>2.15.1</version>  
</dependency>
```

## 核心工具类

|工具类|描述|
|---|---|
|**FileUtils**|提供文件操作（移动、复制、读取、写入等）的工具方法。|
|**IOUtils**|提供流操作（复制、关闭、转换等）的工具方法。|
|**FilenameUtils**|提供文件名和路径操作（获取扩展名、获取路径等）的工具方法。|

## 常用操作示例

FileUtils 文件操作

```java
import org.apache.commons.io.FileUtils;  
import java.io.File;  
import java.io.IOException;  
import java.nio.charset.StandardCharsets;  

public class FileUtilsExample {  
  public static void main(String[] args) throws IOException {  
    File srcFile = new File("src.txt");  
    File destFile = new File("dest.txt");  
    File dir = new File("backup");  

    // 1. 复制文件  
    FileUtils.copyFile(srcFile, destFile);  

    // 2. 复制文件到目录  
    FileUtils.copyFileToDirectory(srcFile, dir);  

    // 3. 读取文件内容到字符串  
    String content = FileUtils.readFileToString(srcFile, StandardCharsets.UTF_8);  

    // 4. 写入字符串到文件  
    FileUtils.writeStringToFile(destFile, "Hello Commons IO", StandardCharsets.UTF_8);  

    // 5. 删除目录（递归）  
    FileUtils.deleteDirectory(dir);  
  }  
}
```

IOUtils 流操作

```java
import org.apache.commons.io.IOUtils;  
import java.io.FileInputStream;  
import java.io.FileOutputStream;  
import java.io.IOException;  

public class IOUtilsExample {  
  public static void main(String[] args) {  
    try (FileInputStream in = new FileInputStream("src.txt");  
         FileOutputStream out = new FileOutputStream("dest.txt")) {  

      // 1. 流的复制 (自动处理缓冲)  
      IOUtils.copy(in, out);  

      // 2. 从流中读取内容到字节数组  
      // byte[] data = IOUtils.toByteArray(in);  

    } catch (IOException e) {  
      e.printStackTrace();  
    }  
  }  
}
```

FilenameUtils 文件名操作

```java
import org.apache.commons.io.FilenameUtils;  

public class FilenameUtilsExample {  
  public static void main(String[] args) {  
    String path = "/home/user/docs/report.pdf";  

    // 1. 获取文件名 (report.pdf)  
    System.out.println(FilenameUtils.getName(path));  

    // 2. 获取扩展名 (pdf)  
    System.out.println(FilenameUtils.getExtension(path));  

    // 3. 获取不带扩展名的文件名 (report)  
    System.out.println(FilenameUtils.getBaseName(path));  

    // 4. 标准化路径 (处理 ../ 等)  
    System.out.println(FilenameUtils.normalize("/home/user/../docs/./report.pdf"));  
  }  
}
```
