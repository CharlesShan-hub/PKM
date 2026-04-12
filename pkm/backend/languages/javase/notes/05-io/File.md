# File

---

## 文件的创建

| 构造函数                   | 参数形式      | 适用场景     |
| ---------------------- | --------- | -------- |
| `File(String)`         | 路径字符串     | 快速创建文件对象 |
| `File(String, String)` | 父路径 + 子路径 | 路径拼接     |
| `File(File, String)`   | 父对象 + 子路径 | 面向对象路径处理 |
| `File(URI)`            | URI 对象    | 网络或标准化路径 |

1. `File(String pathname)`
    ```java
    File file = new File("C:/test/example.txt");
    ```
    *  **用途**：通过**路径名字符串**创建**文件**或**目录**对象。  
    *  **参数**：  
        * `pathname`：绝对路径或相对路径（如 `"data/config.ini"`）。  
    *  **注意**： 
       *  路径分隔符需兼容系统（Windows用`\`需转义为`\\`，或直接用`/`）。  
       *  文件/目录可能不存在，需调用 `exists()` 检查。  

2. `File(String parent, String child)`
    ```java
    File file = new File("C:/test", "example.txt");
    ```
    * **用途**：**父路径 + 子路径**组合创建文件对象（避免手动拼接路径）。  
    * **参数**：  
      * `parent`：父目录路径（如 `"C:/test"`）。  
      * `child`：子文件/目录名（如 `"example.txt"`）。  
    * **优势**：跨平台路径分隔符自动处理。  

3. `File(File parent, String child)`
    ```java
    File parentDir = new File("C:/test");
    File file = new File(parentDir, "example.txt");
    ```
    * **用途**：**父路径对象 + 子路径**组合创建文件对象（面向对象风格）。  
    * **参数**：  
        * `parent`：父目录的 `File` 对象。  
        * `child`：子文件/目录名。  
    * **适用场景**：需要复用父目录对象时更高效。  

4. `File(URI uri)`
    ```java
    URI uri = new URI("file:///C:/test/example.txt");
    File file = new File(uri);
    ```
    * **用途**：通过**统一资源标识符 (URI)** 创建文件对象。  
    * **参数**：  
      * `uri`：格式必须为 `file://` 开头的合法 URI。  
    * **注意**：  
      * 适用于网络或标准化路径处理场景。  
      * URI 需编码特殊字符（如空格转为 `%20`）。  

---
## 文件常用操作

以下是图片中提到的 `File` 类方法的完整代码示例，每个方法对应一个实际使用场景：

1. 获取文件名
```java
File file = new File("data/test.txt");
String name = file.getName(); 
System.out.println("文件名: " + name); // 输出: test.txt
```

  2. 获取绝对路径  
```java
File file = new File("data/test.txt");
String absPath = file.getAbsolutePath();
System.out.println("绝对路径: " + absPath); // 输出: /Users/xxx/data/test.txt
```

3. 获取父目录路径
```java
File file = new File("data/test.txt");
String parent = file.getParent();
System.out.println("父目录: " + parent); // 输出: data
```

4. 获取文件大小（字节）
```java
File file = new File("data/test.txt");
long size = file.length();
System.out.println("文件大小: " + size + "字节");
```

5. 检查文件/目录是否存在
```java
File file = new File("data/test.txt");
boolean exists = file.exists();
System.out.println("是否存在: " + exists); // true 或 false
```

6. 判断是否为文件
```java
File file = new File("data/test.txt");
boolean isFile = file.isFile();
System.out.println("是文件吗: " + isFile); // true
```

7. 判断是否为目录
```java
File dir = new File("data");
boolean isDir = dir.isDirectory();
System.out.println("是目录吗: " + isDir); // true
```

8. 获取路径前缀长度（内部方法）
```java
// JDK内部方法，开发者通常无需直接调用
int prefixLen = file.getPrefixLength(); // 例如Windows返回3（C:\）
```

9. 获取父目录对象
```java
File file = new File("data/test.txt");
File parentFile = file.getParentFile();
System.out.println("父目录对象: " + parentFile); // 输出: data
```

10. 判断是否为绝对路径
```java
File file1 = new File("/data/test.txt");
File file2 = new File("data/test.txt");
System.out.println("file1是绝对路径吗: " + file1.isAbsolute()); // true
System.out.println("file2是绝对路径吗: " + file2.isAbsolute()); // false
```

11. 实现 `Comparable` 接口
```java
File file1 = new File("data/a.txt");
File file2 = new File("data/b.txt");
int result = file1.compareTo(file2); // 按路径名字典序比较
System.out.println("比较结果: " + result); // 负数表示file1在前
```

12. `mkdir()` - 创建单级目录
```java
File dir = new File("data");
boolean success = dir.mkdir(); // 创建data目录
System.out.println("创建单级目录是否成功: " + success); // true（需父目录存在）
```

- **功能**：创建**一级目录**​（父目录必须存在）。
- **返回值**：`boolean`（成功返回 `true`，失败返回 `false`）。
- **失败场景**：父目录不存在或目录已存在。

13. `mkdirs()` - 创建多级目录

```java
File dirs = new File("data/sub1/sub2");
boolean success = dirs.mkdirs(); // 递归创建data/sub1/sub2
System.out.println("创建多级目录是否成功: " + success); // true（自动创建父目录）
```

- **功能**：递归创建**多级目录**​（父目录不存在时自动创建）。
- **返回值**：`boolean`（全部目录创建成功返回 `true`）。
- **优势**：无需手动逐级创建父目录。

14. `delete()` - 删除空目录或文件
```java
File file = new File("data/test.txt");
boolean deleted = file.delete(); // 删除文件
System.out.println("删除是否成功: " + deleted); // true（文件存在且未被占用）

File emptyDir = new File("data/sub1");
deleted = emptyDir.delete(); // 删除空目录
System.out.println("删除空目录是否成功: " + deleted); // true
```

- **功能**：删除**文件**或**空目录**。
- **返回值**：`boolean`（成功返回 `true`）。
- **失败场景**：
    - 目录非空（需先删除子内容）。
    - 文件被占用或无权限。

---

## 文件拷贝案例

1. `File[] listFiles(); `

   * 当主调是文件，或者路径不存在时，返回null

   * 当主调是空文件夹时，返回一个长度为0的数组

   * 主调是一个有内容的文件夹时，将里面所有一级文件和文件夹的路径放在File数组中返回

   * 当主调是一个文件夹，且里面有隐藏文件时，将里面所有文件和文件夹的路径放在File数组中返回，包含隐藏文件

   * 当主调是一个文件夹，但是没有权限访问该文件夹时，返回null

2. 递归拷贝

   ```java
   package com.powernode.javase.io;  
   
   import java.io.File;  
   import java.io.FilenameFilter;  
   
   /**  
    * File类的常用方法：File[] listFiles();  
    */public class FileTest04 {  
      public static void main(String[] args) {  
   
        File file = new File("E:\\powernode\\02-JavaSE\\document");  
   
        // 获取所有的子文件，包括子目录。  
        File[] files = file.listFiles();  
   
        // 遍历数组  
        for(File f : files){  
          System.out.println(f.getName());  
        }  
   
        System.out.println("=====================================");  
   
        File file1 = new File("E:\\powernode\\02-JavaSE\\document");  
   
        //File[] files1 = file1.listFiles(new FilenameFilter() {  
        //  @Override  
        //  public boolean accept(File dir, String name) {  
        //    /*if (name.endsWith(".mdj")) {  
        //               return true;                
          //             }                
          //             return false;
        //          */                
        //    return name.endsWith(".mdj");  
        //  }  
        //});  
        File[] files1 = file1.listFiles((dir,name) -> name.endsWith(".mdj")); 
   
        for(File f : files1){  
          System.out.println(f.getName());  
        }  
      }  
    }
   ```

3. 拷贝目录

   ```java
   package com.powernode.javase.io;  
   
   import java.io.File;  
   import java.io.FileInputStream;  
   import java.io.FileOutputStream;  
   import java.io.IOException;  
   
   /**  
    * 目录拷贝。  
    */  
   public class CopyDir {  
     public static void main(String[] args) {  
   
       // 拷贝源  
       File src = new File("E:\\powernode\\02-JavaSE\\code"); // E:\powernode\02-JavaSE\code\chapter01\A.java  
   
       // 拷贝目标  
       File dest = new File("E:\\a\\b\\c"); // E:\a\b\c\powernode\02-JavaSE\code\chapter01\A.java  
   
       // 开始拷贝  
       copy(src, dest);  
     }  
   
     /**  
        * 拷贝目录的方法  
        * @param src 拷贝源  
        * @param dest 拷贝目标  
        */  
     private static void copy(File src, File dest) {  
       if(src.isFile()){  
         // 是文件的时候要拷贝。  
         try(FileInputStream in = new FileInputStream(src);  
             FileOutputStream out = new FileOutputStream(dest.getAbsoluteFile() + src.getAbsolutePath().substring(2))){  
           // 开始拷贝  
           byte[] bytes = new byte[1024 * 1024];  
           int readCount = 0;  
           while((readCount = in.read(bytes)) != -1){  
             out.write(bytes, 0, readCount);  
           }  
           out.flush();  
         }catch(IOException e){  
           e.printStackTrace();  
         }  
         return;  
       }  
       // 假设src是一个目录  
       // 程序能够执行到此处一定是一个目录  
       // 创建目录  
       File newDir = new File(dest.getAbsolutePath() + src.getAbsolutePath().substring(2));  
       if(!newDir.exists()){  
         newDir.mkdirs();  
       }  
       File[] files = src.listFiles();  
       for (File file : files){  
         //System.out.println(file.getAbsolutePath());  
         copy(file, dest);  
       }  
     }  
   }
   ```
