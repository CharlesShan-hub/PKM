# DataOutputStream

```java
package com.powernode.javase.io;  
  
import java.io.DataOutputStream;  
import java.io.FileOutputStream;  
  
/**  
 * java.io.DataOutputStream：数据流（数据字节输出流）  
 * 作用：将java程序中的数据直接写入到文件，写到文件中就是二进制。  
 * DataOutputStream写的效率很高，原因是：写的过程不需要转码。  
 * DataOutputStream写到文件中的数据，只能由DataInputStream来读取。  
 */  
public class DataOutputStreamTest {  
    public static void main(String[] args) throws Exception{  
        // 节点流  
        //OutputStream os = new FileOutputStream("data");  
        // 包装流  
        //DataOutputStream dos = new DataOutputStream(os);  
  
        DataOutputStream dos = new DataOutputStream(new FileOutputStream("data"));  
  
        // 准备数据  
        byte b = -127;  
        short s = 32767;  
        int i = 2147483647;  
        long l = 1111111111L;  
        float f = 3.0F;  
        double d = 3.14;  
        boolean flag = false;  
        char c = '国';  
        String str = "动力节点";  
  
        // 开始写  
        dos.writeByte(b);  
        dos.writeShort(s);  
        dos.writeInt(i);  
        dos.writeLong(l);  
        dos.writeFloat(f);  
        dos.writeDouble(d);  
        dos.writeBoolean(flag);  
        dos.writeChar(c);  
        dos.writeUTF(str);  
  
        dos.flush();  
        dos.close();  
    }  
}
```

[[DataInputStream]]