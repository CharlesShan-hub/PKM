# InputStreamReader

用来指定编码

```java
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
public class FileExample {
    public static void main(String[] args) {
        String path = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/a.txt";
        try{
            String encoding = "UTF-8";
            InputStreamReader isr = new InputStreamReader(new FileInputStream(path), encoding);
            int singleChar;
            while((singleChar = isr.read())!= -1) {
                System.out.print((char)singleChar);
            }
        }catch(IOException e) {
            e.printStackTrace();
        }
    }
}
```

写：[[OutputStreamWriter]]

完全可以用 InputStreamReader 的子类 [[FileReader]]，这也可以直接指定字符集，这就是Java本身简化了代码，所以直接使用中，直接用FileReader和FilerWriter