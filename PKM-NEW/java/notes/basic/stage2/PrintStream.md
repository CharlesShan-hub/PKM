# PrintStreams

```java
// PrintStream 示例（字节流）
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;

// PrintWriter 示例（字符流）
import java.io.PrintWriter;
import java.io.OutputStreamWriter;

public class PrintStreamAndPrintWriterExample {
    public static void main(String[] args) {
        try{
            // PrintStream ps = new PrintStream(new FileOutputStream(filePath));
            PrintStream ps = new PrintStream(System.out);
            ps.println(64);
            ps.write((byte)64);
            ps.write("\nHello, PrintStream!".getBytes());
            ps.close();
        }catch(IOException e) {
            e.printStackTrace();
        }
    }
}
```