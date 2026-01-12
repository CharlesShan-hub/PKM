# 常见的异常(AI)

常见的运行时异常：

1. **NullPointerException 空指针异常**
   - 当尝试访问一个未初始化的对象时，会抛出此异常。
   ```java
   public class Test {
       public static void main(String[] args) {
           Object obj = null;
           System.out.println(obj.toString()); // 尝试访问 null 对象
       }
   }
   ```
   运行上述代码将抛出 `NullPointerException`。

2. **ArithmeticException 数学运算异常**
   - 当执行非法的数学运算时，例如除以零，会抛出此异常。
   ```java
   public class Test {
       public static void main(String[] args) {
           int result = 10 / 0; // 除以零
       }
   }
   ```
   运行上述代码将抛出 `ArithmeticException`。

3. **ArrayIndexOutOfBoundsException 数组下标越界异常**
   - 当访问数组时，如果下标超出数组的有效范围，会抛出此异常。
   ```java
   public class Test {
       public static void main(String[] args) {
           int[] array = new int[5];
           System.out.println(array[5]); // 越界访问
       }
   }
   ```
   运行上述代码将抛出 `ArrayIndexOutOfBoundsException`。

4. **ClassCastException 类型转换异常**
   - 当尝试将对象强制转换为不兼容的类型时，会抛出此异常。
   ```java
   public class Test {
       public static void main(String[] args) {
           Object obj = "Hello";
           int str = (int) obj; // 类型转换错误
       }
   }
   ```
   运行上述代码将抛出 `ClassCastException`。

5. **NumberFormatException 数字格式不正确异常**
   - 当尝试将字符串转换为数字，但字符串格式不正确时，会抛出此异常。
   ```java
   public class Test {
       public static void main(String[] args) {
           double num = Double.parseDouble("abc"); // 格式错误
       }
   }
   ```
   运行上述代码将抛出 `NumberFormatException`。

常见的编译异常：

1. SQLException // 操作数据库时，查询表可能发生异常
2. IOException // 操作文件时，发生的异常
3. FileNotFoundException // 当操作一个不存在的文件时，发生异常
4. ClassNotFoundException // 加载类，而该类不存在时，异常
5. EOFException // 操作文件，到文件末尾，发生异常
6. IllegalArgumentException // 参数异常

以下是每种异常的示例代码：

1. **SQLException**
   ```java
   import java.sql.*;
   
   public class Test {
       public static void main(String[] args) {
           Connection conn = null;
           try {
               conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/yourdb", "username", "password");
               Statement stmt = conn.createStatement();
               ResultSet rs = stmt.executeQuery("SELECT * FROM your_table");
            while (rs.next()) {
               System.out.println(rs.getString(1));
           }
           } catch (SQLException e) {
               e.printStackTrace();
          } finally {
              if (conn != null) {
                  try {
                      conn.close();
                  } catch (SQLException ex) {
                     ex.printStackTrace();
                  }
              }
          }
       }
   }
   ```
   上述代码尝试连接到 MySQL 数据库并查询一个表，如果发生异常（例如，数据库连接信息错误），将捕获 `SQLException`。

2. **IOException**
   ```java
   import java.io.*;
   
   public class Test {
       public static void main(String[] args) {
           FileInputStream fis = null;
           try {
               fis = new FileInputStream("nonexistent.txt");
          int i = fis.read();
          System.out.println(i);
          } catch (IOException e) {
              e.printStackTrace();
          } finally {
              if (fis != null) {
                  try {
                      fis.close();
                  } catch (IOException ex) {
                     ex.printStackTrace();
                  }
              }
          }
       }
   }
   ```
   上述代码尝试打开一个不存在的文件，将抛出 `IOException`。

3. **FileNotFoundException**
   ```java
   import java.io.*;
   
   public class Test {
       public static void main(String[] args) {
          File file = new File("nonexistent.txt");
          if (file.exists()) {
              System.out.println("File exists");
          } else {
              System.out.println("File does not exist");
          }
       }
   }
   ```
   上述代码检查一个文件是否存在，如果不存在，将不抛出 `FileNotFoundException`。

4. **ClassNotFoundException**
   ```java
   public class Test {
       public static void main(String[] args) {
          try {
              Class.forName("NonExistentClass");
          } catch (ClassNotFoundException e) {
              e.printStackTrace();
          }
       }
   }
   ```
   上述代码尝试加载一个不存在的类，将抛出 `ClassNotFoundException`。

5. **EOFException**
   ```java
   import java.io.*;
   
   public class Test {
       public static void main(String[] args) {
          FileInputStream fis = null;
          try {
             fis = new FileInputStream("yourfile.txt");
            int i;
            while ((i = fis.read()) != -1) {
               System.out.println((char) i);
           }
          } catch (EOFException e) {
              e.printStackTrace();
          } finally {
              if (fis != null) {
                  try {
                      fis.close();
                  } catch (IOException ex) {
                     ex.printStackTrace();
                  }
              }
          }
       }
   ```
   上述代码尝试读取一个文件直到文件末尾，将抛出 `EOFException`。

6. **IllegalArgumentException**
   ```java
   public class Test {
       public static void main(String[] args) {
          try {
              System.out.println(Math.random() + " invalid argument");
          } catch (IllegalArgumentException e) {
              e.printStackTrace();
          }
       }
   }
   ```
   上述代码尝试将一个非法参数传递给 `System.out.println()` 方法，将抛出 `IllegalArgumentException`。
