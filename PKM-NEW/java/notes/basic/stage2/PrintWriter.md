# PrintWriter

```java
// PrintStream 示例（字节流）
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintWriter;

public class PrintStreamAndPrintWriterExample {
    public static void main(String[] args) {
        // Using try-with-resources for auto-close
        try (PrintWriter ps = new PrintWriter(System.out)) {
            ps.println(64);
            ps.write((char)64);
            ps.write("\nHello, PrintWriter!");
            
            // Check for errors if needed
            if (ps.checkError()) {
                System.err.println("An error occurred during writing");
            }
        }
        // No catch block needed since PrintWriter doesn't throw IOExceptions
    }
}
```
