# OutputStreamWriter

```java
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
public class FileExample {
    public static void main(String[] args) {
        String path = "/Users/kimshan/Public/project/javanote/out/production/javanote/assets/a.txt";    
        try{
            String encoding = "UTF-8";
            OutputStreamWriter osw = new OutputStreamWriter(new FileOutputStream(path), encoding);
            osw.write("Hello, 世界!");
            osw.close();
        }catch(IOException e) {
            e.printStackTrace();
        }
    }
}
```

读：[[InputStreamReader]]