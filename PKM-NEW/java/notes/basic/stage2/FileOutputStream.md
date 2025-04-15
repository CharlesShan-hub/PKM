# FileOutputStream

写入一个字节

```java
package ex_file;
import java.io.FileOutputStream;
import java.io.IOException;
public class FileExample {
    public static void main(String[] args){
        String path = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/a.txt";
        try{
            FileOutputStream fis = new FileOutputStream(path);
            fis.write('a');
            fis.close();
        }catch(IOException e){
            e.printStackTrace();
        }
    }
}
```

写入字符串

```java
package ex_file;
import java.io.FileOutputStream;
import java.io.IOException;
public class FileExample {
    public static void main(String[] args){
        String path = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/a.txt";
        try{
            FileOutputStream fis = new FileOutputStream(path);
            fis.write("Hello World".getBytes());
            fis.close();
        }catch(IOException e){
            e.printStackTrace();
        }
    }
}
```

写入字符串并制定从哪里开始写几位

```java
package ex_file;  
  
import java.io.FileOutputStream;  
import java.io.IOException;  
  
public class FileExample {  
    public static void main(String[] args){
        String path = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/a.txt";  
        try{  
            FileOutputStream fis = new FileOutputStream(path);  
            byte[] content = "Hello World".getBytes();  
            fis.write(content,0,5);  // 这里
            fis.close();  
        }catch(IOException e){  
            e.printStackTrace();  
        }    
    }
}
```

以上内容都是覆盖写，如果要追加写：`FileOutputStream fis = new FileOutputStream(path, true);`，加一个`true`

案例：完成图片/音乐的拷贝

```java
package ex_file;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class FileCopy {
    public static void main(String[] args){
        String srcPath = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/a.txt";
        String distPath =  "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/b.txt";
        try{
            FileInputStream srcFis = new FileInputStream(srcPath);
            FileOutputStream distFis = new FileOutputStream(distPath);
            while(srcFis.available() > 0)
                distFis.write(srcFis.read());
            distFis.close();
            srcFis.close();
        }catch(IOException e){
            e.printStackTrace();
        }
    }
}
```

```java
package ex_file;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class FileCopy {
    public static void main(String[] args){
        String srcPath = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/c.txt";
        String distPath =  "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/d.txt";
        try{
            FileInputStream srcFis = new FileInputStream(srcPath);
            FileOutputStream distFis = new FileOutputStream(distPath,true);
            byte[] buffer = new byte[8];
            int bytesRead;
            while((bytesRead = srcFis.read(buffer)) != -1)
                distFis.write(buffer, 0, bytesRead); // 一定要这样，否则会最后多写入乱码
            distFis.close();
            srcFis.close();
        }catch(IOException e){
            e.printStackTrace();
        }
    }
}
```

