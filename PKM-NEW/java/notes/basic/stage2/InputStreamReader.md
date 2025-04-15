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