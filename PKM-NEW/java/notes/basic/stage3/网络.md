# 网络
---
## INetAddress

```java
import java.net.InetAddress;
import java.net.UnknownHostException;

public class INetAddressExample {
    public static void main(String[] args) {
        try {
            // 1. 获取本地主机的IP地址
            InetAddress localHost = InetAddress.getLocalHost();
            System.out.println("本地主机信息:");
            System.out.println("主机名: " + localHost.getHostName());
            System.out.println("IP地址: " + localHost.getHostAddress());
            System.out.println("规范主机名: " + localHost.getCanonicalHostName());
            System.out.println("是否为回环地址: " + localHost.isLoopbackAddress());
            System.out.println();
            
            // 2. 通过主机名获取IP地址
            InetAddress googleAddress = InetAddress.getByName("www.google.com");
            System.out.println("Google服务器信息:");
            System.out.println("主机名: " + googleAddress.getHostName());
            System.out.println("IP地址: " + googleAddress.getHostAddress());
            System.out.println("是否为多播地址: " + googleAddress.isMulticastAddress());
            System.out.println();
            
            // 3. 获取一个域名的所有IP地址
            InetAddress[] allGoogleAddresses = InetAddress.getAllByName("www.google.com");
            System.out.println("Google所有IP地址:");
            for (InetAddress addr : allGoogleAddresses) {
                System.out.println(addr.getHostAddress());
            }
            System.out.println();
            
            // 4. 创建回环地址
            InetAddress loopback = InetAddress.getByName("127.0.0.1");
            System.out.println("回环地址信息:");
            System.out.println("是否为回环地址: " + loopback.isLoopbackAddress());
            System.out.println("是否为IPv4地址: " + (loopback.getAddress().length == 4));
            System.out.println();
            
            // 5. 检查可达性
            System.out.println("检查本地主机是否可达(5000ms超时): " + localHost.isReachable(5000));
            
        } catch (UnknownHostException e) {
            System.err.println("无法解析主机名: " + e.getMessage());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

---
## URL
1. URL类的构造方法：URL url = new URL(“http://127.0.0.1:8080/oa/index.html?name=zhangsan#tip”);
2. URL类的常用方法：
	1. 获取协议：url.getProtocol()		获取域名：url.getHost()		获取默认端口：url.getDefaultPort()
	2. 获取端口：url.getPort()			获取路径：url.getPath()		获取资源：url.getFile()		
	3. 获取数据：url.getQuery()		获取锚点：url.getRef()
3. 使用URL类的openStream()方法可以打开到此URL的连接并返回一个用于从该连接读入的InputStream，实现最简单的网络爬虫
```java
package com.powernode.javase.net;  
  
/**  
 * ClassName: URLTest01 * Description: 
 *      URL包括四部分：协议，IP地址，端口号，资源名称  
 *      URL是网络中某个资源的地址。某个资源的唯一标识。  
 *      通过URL是可以真实的定位到资源的。  
 *      在Java中，java类库提供了一个URL类，来提供对URL的支持。  
 *  
 *      URL类的构造方法  
 *          URL url = new URL("url");  
 * 
 *      URL类的常用方法  
 *          url.getXxx();  
 * <p> 
 * Datetime: 2024/2/1 10:20 * Author: 老杜@动力节点  
 * Version: 1.0  
 */
import java.net.URL;  
  
public class URLTest01 {  
    public static void main(String[] args) throws Exception{  
        // 创建URL类型的对象  
        URL url = new URL("http://www.baidu.com:8888/oa/index.html?name=zhangsan&password=123#tip");  
  
        // 获取URL中的信息  
        String protocol = url.getProtocol();  
        System.out.println("协议：" + protocol);  
  
        // 获取资源路径  
        String path = url.getPath();  
        System.out.println("资源路径：" + path);  
  
        // 获取默认端口（HTTP协议的默认端口是80）  
        int defaultPort = url.getDefaultPort();  
        System.out.println("默认端口：" + defaultPort);  
  
        // 获取当前的端口  
        int port = url.getPort();  
        System.out.println("当前端口号：" + port);  
  
        // 获取URL中的IP地址  
        String host = url.getHost();  
        System.out.println("主机地址：" + host);  
  
        // 获取URL准备传送的数据  
        String query = url.getQuery();  
        System.out.println("需要提交给服务器的数据：" + query);  
  
        // 获取锚点  
        String ref = url.getRef();  
        System.out.println("获取锚点：" + ref);  
  
        // 获取 资源路径 + 数据  
        String file = url.getFile();  
        System.out.println("资源路径+数据：" + file);  
    }  
}
```

爬虫案例
```java
package com.powernode.javase.net;  
  
import java.io.BufferedReader;  
import java.io.InputStream;  
import java.io.InputStreamReader;  
import java.net.URL;  
  
/**  
 * ClassName: URLTest02 
 * Description: 
 * <p> 
 * Datetime: 2024/2/1 15:53 
 * Author: 老杜@动力节点  
 * Version: 1.0  
 */
public class URLTest02 {  
    public static void main(String[] args) throws Exception{  
        URL url = new URL("https://tianqi.qq.com/");  
        InputStream inputStream = url.openStream();  
        BufferedReader br = new BufferedReader(new InputStreamReader(inputStream));  
  
        String s = null;  
        while((s = br.readLine()) != null){  
            System.out.println(s);  
        }  
  
        br.close();  
    }  
}
```
---
## Socket

Socket类概述
1. Socket类实现客户端套接字(Client），套接字是两台机器间通信的端点
2. Socket类构造方法：
	1. public Socket(InetAddress a, int p)  创建套接字并连接到指定IP地址的指定端口号
3. Socket类实例方法：
	1. public InetAddress getInetAddress()		返回此套接字连接到的远程 IP 地址。
	2. public InputStream getInputStream()		返回此套接字的输入流（接收网络消息）。
	3. public OutputStream getOutputStream()		返回此套接字的输出流（发送网络消息）。
	4. public void shutdownInput()				禁用此套接字的输入流
	5. public void shutdownOutput()				禁用此套接字的输出流。
	6. public synchronized void close()			关闭此套接字（默认会关闭IO流）。

ServerSocket类概述
1. ServerSocket类用于实现服务器套接字(Server服务端)。服务器套接字等待请求通过网络传入。它基于该请求执行某些操作，然后可能向请求者返回结果
2. ServerSocket构造方法：
	1. public ServerSocket(int port)
3. ServerSocket实例方法：
	1. public Socket accept()				侦听要连接到此套接字并接受它。
	2. public InetAddress getInetAddress()	返回此服务器套接字的本地地址。
	3. public void close()					关闭此套接字。

### 案例一

1. ​**​编写一个服务器端，和一个客户端​**​
2. ​**​服务器端在9999端口监听​**​
3. ​**​客户端连接到服务器端，发送"hello，server"，然后退出​**​
4. ​**​服务器端接收到客户端发送的信息，输出，并退出​**

服务器：

```java
import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) {
        try {
            // 1. 创建ServerSocket，监听9999端口
            ServerSocket serverSocket = new ServerSocket(9999);
            System.out.println("服务器启动，等待客户端连接...");

            // 2. 等待客户端连接（accept()会阻塞，直到有客户端连接）
            Socket socket = serverSocket.accept();
            System.out.println("客户端已连接！");

            // 3. 获取输入流，读取客户端发送的数据
            BufferedReader reader = new BufferedReader(
                new InputStreamReader(socket.getInputStream())
            );
            String message = reader.readLine();
            System.out.println("收到客户端消息: " + message);

            // 4. 关闭资源
            reader.close();
            socket.close();
            serverSocket.close();
            System.out.println("服务器已关闭。");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

客户端：

```java
import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        try {
            // 1. 创建Socket，连接到服务器（IP: 127.0.0.1，端口: 9999）
            Socket socket = new Socket("127.0.0.1", 9999);
            System.out.println("已连接到服务器...");

            // 2. 获取输出流，向服务器发送数据
            PrintWriter writer = new PrintWriter(
                socket.getOutputStream(), true
            );
            writer.println("hello, server");
            System.out.println("已发送消息: hello, server");

            // 3. 关闭资源
            writer.close();
            socket.close();
            System.out.println("客户端已关闭。");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### 案例二

1. **编写一个服务端，和一个客户端**
2. **服务器端在9999端口监听**
3. **客户端连接到服务端，发送 `"hello, server"`，并接收服务器端回发的 `"hello, client"`，再退出**
4. **服务器端接收到客户端发送的信息，输出，并发送 `"hello, client"`，再退出**

服务器：

```java
import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) throws IOException {
        // 1. 创建ServerSocket，监听9999端口
        ServerSocket serverSocket = new ServerSocket(9999);
        System.out.println("服务端启动，等待客户端连接...");

        // 2. 阻塞等待客户端连接
        Socket socket = serverSocket.accept();
        System.out.println("客户端已连接！");

        // 3. 获取输入流（接收客户端消息）
        InputStream inputStream = socket.getInputStream();
        byte[] buf = new byte[1024];
        int len = inputStream.read(buf);
        String clientMessage = new String(buf, 0, len);
        System.out.println("收到客户端消息: " + clientMessage);

        // 4. 获取输出流（向客户端发送响应）
        OutputStream outputStream = socket.getOutputStream();
        outputStream.write("hello,client".getBytes());

        // 5. 关闭资源
        outputStream.close();
        inputStream.close();
        socket.close();
        serverSocket.close();
        System.out.println("服务端已关闭。");
    }
}
```

客户端：

```java
import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) throws IOException {
        // 1. 连接服务端（IP: 127.0.0.1，端口: 9999）
        Socket socket = new Socket("127.0.0.1", 9999);
        System.out.println("已连接到服务端...");

        // 2. 获取输出流（向服务端发送消息）
        OutputStream outputStream = socket.getOutputStream();
        outputStream.write("hello,server".getBytes());
        System.out.println("已发送消息: hello,server");

        // 3. 获取输入流（接收服务端响应）
        InputStream inputStream = socket.getInputStream();
        byte[] buf = new byte[1024];
        int len = inputStream.read(buf);
        String serverResponse = new String(buf, 0, len);
        System.out.println("收到服务端响应: " + serverResponse);

        // 4. 关闭资源
        inputStream.close();
        outputStream.close();
        socket.close();
        System.out.println("客户端已关闭。");
    }
}
```

### 案例三：字符流版本

 1. ​**​最底层：`OutputStream`（字节流）​**​
	- `socket.getOutputStream()`  
	    ▶️ 获取Socket原始的​**​字节输出流​**​，只能处理`byte[]`类型数据

2. ​**​中间层：`OutputStreamWriter`（桥梁）​**​
	- `new OutputStreamWriter(outputStream)`  
	    ▶️ 将字节流​**​转换为字符流​**​，实现字节到字符的编码（默认UTF-8）  
	    ▶️ 关键作用：​**​字节流 → 字符流​**​的转换

3. ​**​最外层：`BufferedWriter`（缓冲包装）​**​
	- `new BufferedWriter(writer)`  
	    ▶️ 添加​**​缓冲功能​**​，避免频繁IO操作  
	    ▶️ 提供`write()`、`newLine()`等便捷方法  
	    ▶️ 必须调用`flush()`强制刷出缓冲区数据


服务器

```java
import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) throws IOException {
        // 1. 启动服务端监听9999端口
        ServerSocket serverSocket = new ServerSocket(9999);
        System.out.println("服务端启动（字符流版）...");

        // 2. 接受客户端连接
        Socket socket = serverSocket.accept();
        System.out.println("客户端已连接");

        // 3. 获取输入流（字符流）
        BufferedReader reader = new BufferedReader(
            new InputStreamReader(socket.getInputStream(), "UTF-8")
        );

        // 4. 读取客户端消息（按行读取）
        String clientData = reader.readLine();
        System.out.println("收到客户端数据: " + clientData);

        // 5. 关闭资源
        reader.close();
        socket.close();
        serverSocket.close();
    }
}
```

客户端

```java
import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) throws IOException {
        // 1. 创建Socket连接本地9999端口（完全匹配图片）
        Socket socket = new Socket(InetAddress.getLocalHost(), 9999);
        System.out.println("客户端Socket返回: " + socket.getClass());

        // 2. 获取输出流并转换为字符流（严格按图片实现）
        OutputStream outputStream = socket.getOutputStream();
        BufferedWriter bufferedWriter = new BufferedWriter(
            new OutputStreamWriter(outputStream, "UTF-8")
        );

        // 3. 写入数据（还原图片中的换行和刷新操作）
        bufferedWriter.write("hello，server字符流");  // 注意使用中文逗号
        bufferedWriter.newLine();  // 换行符
        bufferedWriter.flush();    // 手动刷新
        System.out.println("已写入字符流数据");

        // 4. 设置结束标记（完全匹配图片）
        socket.shutdownOutput();

        // 5. 关闭资源（图片中未展示但必要的操作）
        bufferedWriter.close();
        socket.close();
    }
}
```

### 案例四：上传图片

1. 编写一个服务端，和一个客户端
2. 服务器端在8889端口监听
3. 客户端连接到服务端，发送一张图片 `e:\qie.png`
4. 服务器端接收到客户端发送的图片，保存到 `src` 下，发送`"收到图片"`再退出
5. 客户端接收到服务端发送的`"收到图片"`，再退出
6. 该程序要求使用 `StreamUtils.java`

服务器

```java
import java.io.*;
import java.net.*;

public class Server {
	public static byte[] streamToByteArray(InputStream is) throws Exception {
		// 创建输出流对象
		ByteArrayOutputStream bos = new ByteArrayOutputStream();
		// 字节数组
		byte[] b = new byte[1024];
		int len;
		while ((len = is.read(b)) != -1) {
			// 循环读取
			// 把读取到的数据，写入 bos
			bos.write(b, 0, len);
		}
		byte[] array = bos.toByteArray();
		bos.close();
		return array;
	}
    public static void main(String[] args) {
        try {
            // 1. 在8888端口监听
            ServerSocket serverSocket = new ServerSocket(8889);
            System.out.println("服务端启动，等待连接...");

            // 2. 接受客户端连接
            Socket socket = serverSocket.accept();

            // 3. 使用缓冲流接收图片（处理Exception）
            BufferedInputStream bis = new BufferedInputStream(socket.getInputStream());
            byte[] imageData = streamToByteArray(bis);

            // 4. 保存图片到src目录（严格匹配图片要求）
            String savePath = "/Users/kimshan/Downloads/pic1.png";  // 图片指定路径
            BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(savePath));
            bos.write(imageData);
            bos.close();
            System.out.println("图片保存成功：" + savePath);

            // 5. 发送确认消息
            BufferedOutputStream out = new BufferedOutputStream(socket.getOutputStream());
            out.write("收到图片".getBytes());
            out.flush();

            // 6. 关闭资源
            out.close();
            bis.close();
            socket.close();
            serverSocket.close();
        } catch (Exception e) {
            System.err.println("服务端错误: " + e.getMessage());
        }
    }
}
```

客户端

```java
import java.io.*;
import java.net.*;

public class Client {
    public static String streamToString(InputStream is) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(is));
        StringBuilder builder = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
            builder.append(line + "\r\n");
        }
        return builder.toString();
    }
    public static byte[] streamToByteArray(InputStream is) throws Exception {
		// 创建输出流对象
		ByteArrayOutputStream bos = new ByteArrayOutputStream();
		// 字节数组
		byte[] b = new byte[1024];
		int len;
		while ((len = is.read(b)) != -1) {
			// 循环读取
			// 把读取到的数据，写入 bos
			bos.write(b, 0, len);
		}
		byte[] array = bos.toByteArray();
		bos.close();
		return array;
	}
    
    public static void main(String[] args) throws IOException {
        try{
	        // 1. 连接服务端（8888端口）
	        Socket socket = new Socket("127.0.0.1", 8889);
	
	        // 2. 读取本地图片（使用缓冲流）
	        String imagePath = "/Users/kimshan/Downloads/pic.png"; // 严格匹配图片路径
	        BufferedInputStream bis = new BufferedInputStream(new FileInputStream(imagePath));
	        byte[] imageData = streamToByteArray(bis);
	        bis.close();
	
	        // 3. 发送图片数据（带缓冲）
	        BufferedOutputStream bos = new BufferedOutputStream(socket.getOutputStream());
	        bos.write(imageData);
	        bos.flush();
	        socket.shutdownOutput(); // 重要！通知服务端发送完成
	
	        // 4. 等待服务端确认（带缓冲）
	        BufferedInputStream in = new BufferedInputStream(socket.getInputStream());
	        String response = streamToString(in); // 使用工具类
	        System.out.println("服务端响应：" + response);
	
	        // 5. 关闭连接
	        in.close();
	        bos.close();
	        socket.close();
        } catch (Exception e) {
            System.err.println("服务端错误: " + e.getMessage());
        }
    }
}
```

## TCP/UDP

### 概述

* TCP协议
	* 使用TCP协议，须先建立TCP连接，形成传输数据通道，似于拨打电话。
	* 传输前，采用“三次握手”方式，属于**4️⃣点对点**通信，是**1️⃣面向连接**的，效率低。
	* 仅支持单播传输，每条TCP传输连接只能有两个端点（客户端、服务端）。
	* 两个端点的数据传输，采用的是“**2️⃣字节流**”来传输，属于**3️⃣可靠的**数据传输。
	* 传输完毕，需释放已建立的连接，开销大，速度慢，**5️⃣适用于文件传输、邮件**等。
* UDP协议
	* 采用数据报（数据、源、目的）的方式来传输，**1️⃣无需建立连接**，类似于发短信。
	* 每个**2️⃣数据报**的大小限制在64K内，超出64k可以分为多个数据报来发送。
	* 发送不管对方是否准备好，接收方即使收到也不确认，因此属于**3️⃣不可靠的**。
	* 可以广播发送，也就是属于**4️⃣一对一、一对多和多对一**连接的通信协议。
	* 发送数据结束时无需释放资源，开销小，速度快，适用于**5️⃣视频会议、直播**等

### TCP三次握手

三次握手的过程如下：
1. 客户端发送 SYN（同步）数据包。这个数据包包含客户端的初始序列号（ISN）。
2. 服务器收到 SYN 数据包后，发送 SYN-ACK（同步确认）数据包。这个数据包包含服务器的初始序列号（ISN）和对客户端 ISN 的确认号（ACK）。
3. 客户端收到 SYN-ACK 数据包后，发送 ACK（确认）数据包。这个数据包包含对服务器 ISN 的确认号（ACK）。
三次握手完成后，客户端和服务器就可以开始交换数据了。

> 我复述一下：
> 第一次握手是客户端向服务器发送一个同步数据包，其中包含客户端的初始序列号。
> 第二次握手是服务器向客户端发送对同步数据包的确认同步数据包，其中包含服务器的初始序列号和对客户端的初始序列号的确认号
> 第三次握手是客户端向服务器发送一个确认数据包，其中包含对服务器发送对初始序列号的确认号


| 握手  | 初始序列号 | 确认数据号 |
| --- | ----- | ----- |
| 1   | ✅     |       |
| 2   | ✅     | ✅     |
| 3   |       | ✅     |


三次握手的意义：
三次握手可以确保数据在两个设备之间可靠地传输。它可以防止以下情况的发生：
不会丢失：如果没有三次握手，客户端和服务器可能会同时发送数据，导致数据丢失。
不会重复：如果没有三次握手，客户端和服务器可能会重复发送数据，导致数据重复。
不会乱序：如果没有三次握手，客户端和服务器可能会乱序发送数据，导致数据乱序。

### TCP四次挥手

使用四次挥手来关闭连接，以确保数据在两个设备之间可靠地传输。
四次挥手的过程如下：
1. 客户端发送 FIN（结束）数据包。这个数据包表示客户端已经完成数据传输，并希望关闭连接。
2. 服务器收到 FIN 数据包后，发送 ACK（确认）数据包。这个数据包表示服务器已经收到客户端的 FIN 数据包，并同意关闭连接。
3. 服务器发送 FIN 数据包。这个数据包表示服务器已经完成数据传输，并希望关闭连接。
4. 客户端收到 FIN 数据包后，发送 ACK（确认）数据包。这个数据包表示客户端已经收到服务器的 FIN 数据包，并同意关闭连接。四次挥手完成后，客户端和服务器之间的连接就关闭了。
四次挥手的意义
四次挥手可以确保数据在两个设备之间可靠地传输。它可以防止以下情况的发生：
如果没有四次挥手，客户端和服务器可能会同时关闭连接，导致数据丢失。
如果没有四次挥手，客户端和服务器可能会重复发送数据，导致数据重复。
如果没有四次挥手，客户端和服务器可能会乱序发送数据，导致数据乱序。
