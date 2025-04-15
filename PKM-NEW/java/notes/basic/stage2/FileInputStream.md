# FileInputStream

`FileInputStream` 是Java I/O体系中**字节输入流（InputStream）​**的子类，专门用于从文件系统中读取原始字节数据（8位字节流）。

| 特性        | 说明                                                |
| --------- | ------------------------------------------------- |
| ​**继承关系** | `java.io.InputStream` → `java.io.FileInputStream` |
| ​**数据单位** | 以**字节（byte）​**为单位读取（适合二进制数据）                      |
| ​**读取方式** | 顺序读取（不可随机访问，需用`RandomAccessFile`实现随机访问）           |
| ​**资源管理** | 必须显式调用`close()`关闭流（推荐用try-with-resources自动关闭）     |
|           |                                                   |

适用场景：

1. ​**读取二进制文件**
    
    - 图片（`.jpg/.png`）、音频（`.mp3`）、视频（`.mp4`）、压缩文件等。
    
    ```java
    try (FileInputStream fis = new FileInputStream("image.jpg")) {
        byte[] buffer = new byte[1024];
        while (fis.read(buffer) != -1) {
            // 处理二进制数据...
        }
    }
    ```
    
2. ​**低层级文本文件读取**
    
    - 需手动处理编码转换（建议用`InputStreamReader`包装为字符流）。
    
    ```java
    FileInputStream fis = new FileInputStream("text.txt");
    InputStreamReader isr = new InputStreamReader(fis, "UTF-8"); // 指定编码
    ```
    
3. ​**与其他字节流配合**
    
    - 可作为`BufferedInputStream`、`ObjectInputStream`等装饰器模式的基础流。
    
    ```java
    InputStream bis = new BufferedInputStream(new FileInputStream("data.bin"));
    ```
    

不适用场景：

- ​**直接读取文本文件**：需额外处理字节到字符的转换（推荐用`FileReader`）。
- ​**需要字符编码的场景**：如读取UTF-8文本，应使用字符流（`Reader`体系）。
- ​**随机访问文件**：需改用`RandomAccessFile`。

通过`read()`一个字节一个字节的读，返回-1代表结束了，否则返回读入的字节数

```java
package ex_file;  
  
import java.io.FileInputStream;  
import java.io.IOException;  
  
public class FileExample {  
    public static void main(String[] args){  
        String path = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/a.txt";  
        try{  
            FileInputStream fis = new FileInputStream(path);  
            int num;  
            while ((num = fis.read())!=-1) {  
                System.out.print((char)num);  
            }            
            System.out.println();   
            // Hello, World!  
            fis.close();  
        }catch(IOException e){  
            e.printStackTrace();  
        }    
    }
}
```

也可以把内容一次性读到 `byte[]`里边

```java
package ex_file;  
  
import java.io.File;  
import java.io.FileInputStream;  
import java.io.IOException;  
  
public class FileExample {  
    public static void main(String[] args){  
        String path = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/a.txt";  
        try{  
            File file = new File(path);  
            FileInputStream fis = new FileInputStream(path);  
            byte[] num = new byte[(int)file.length()];  
            fis.read(num);   // 会返回实际读取的字节数 
            System.out.println(new String(num));
            // Hello, World!  
            fis.close();  
        }catch(IOException e){  
            e.printStackTrace();  
        }    
    }
}
```

也可以把内容分多次读到 `byte[]`里边，拼起来得到完整内容

```java
package ex_file;  
  
import java.io.FileInputStream;  
import java.io.IOException;  
  
public class FileExample {  
    public static void main(String[] args){  
        String path = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/a.txt";  
        try{  
            FileInputStream fis = new FileInputStream(path);  
            byte[] nums = new byte[8];  
            int count;  
            while((count = fis.read(nums)) != -1){  
                System.out.print(new String(nums, 0, count));  
            }            
            System.out.println();  
            // Hello, World!  
            fis.close();  
        }catch(IOException e){  
            e.printStackTrace();  
        }    
    }
}
```

