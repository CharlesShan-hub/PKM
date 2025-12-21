# FileReader

• FileReader和FileWriter是字符流，按字符操作IO  
• FileReader继承体系：  
	• java.lang.Object  
	• java.io.Reader  
	• java.io.InputStreamReader  
	• java.io.FileReader  
• FileReader常用方法：  
	• `new FileReader(File/String)`：构造方法  
	• `read()`：每次读取单个字符，返回字符（ASCII值），文件末尾返回-1  
	• `read(char[])`：批量读取字符到数组，返回读取的字符数，文件末尾返回-1  
• 相关API：  
	• `new String(char[])`：将char数组转为String  
	• `new String(char[], off, len)`：将char数组指定部分转为String  

方式1：单个字符读取
```java
import java.io.FileReader;
import java.io.IOException;

public class FileExample {  
    public static void main(String[] args){  
        String path = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/a.txt";  
        // 使用try-with-resources自动关闭资源
        try(FileReader fis = new FileReader(path)) {
            System.out.println("--- 单个字符读取 ---");
            int singleChar;
            while((singleChar = fis.read()) != -1) {
                System.out.print((char)singleChar);
            }
        } catch(IOException e) {  
            e.printStackTrace();  
        }    
    }
}
```

方式2：批量字符读取（更高效）

```java
import java.io.FileReader;
import java.io.IOException;

public class FileExample {  
    public static void main(String[] args){  
        String path = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/a.txt";  
        try(FileReader fis = new FileReader(path)) {
            System.out.println("\n--- 批量字符读取 ---");
            char[] buffer = new char[1024];
            int charsRead;
            while((charsRead = fis.read(buffer)) != -1) {
                System.out.print(new String(buffer, 0, charsRead)); // 注意这里使用charsRead来确定实际读取的字符数
            }
        } catch(IOException e) {  
            e.printStackTrace();  
        }    
    }
}
```