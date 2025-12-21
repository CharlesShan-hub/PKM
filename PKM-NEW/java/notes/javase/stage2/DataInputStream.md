# DataInputStream

```java
package com.powernode.javase.io;  
  
import java.io.DataInputStream;  
import java.io.FileInputStream;  
  
/**  
 * java.io.DataInputStream：数据流（数据字节输入流）  
 * 作用：专门用来读取使用DataOutputStream流写入的文件。  
 * 注意：读取的顺序要和写入的顺序一致。（要不然无法恢复原样。）  
 */  
public class DataInputStreamTest {  
    public static void main(String[] args) throws Exception{  
        // 创建数据字节输入流对象  
        DataInputStream dis = new DataInputStream(new FileInputStream("data"));  
  
        //System.out.println(dis.readBoolean());  
  
        // 开始读  
        byte b = dis.readByte();  
        short s = dis.readShort();  
        int i = dis.readInt();  
        long l = dis.readLong();  
        float f = dis.readFloat();  
        double d = dis.readDouble();  
        boolean flag = dis.readBoolean();  
        char c = dis.readChar();  
        String str = dis.readUTF();  
  
        System.out.println(b);  
        System.out.println(s);  
        System.out.println(i);  
        System.out.println(l);  
        System.out.println(f);  
        System.out.println(d);  
        System.out.println(flag);  
        System.out.println(c);  
        System.out.println(str);  
  
        // 关闭流  
        dis.close();  
  
        /*
        FileInputStream fis = new FileInputStream("data");  
  
        System.out.println(fis.read());        
        System.out.println(fis.read());        
        System.out.println(fis.read());        
        System.out.println(fis.read());  
        fis.close();
        */  
  
    }  
}
```

[[DataOutputStream]]