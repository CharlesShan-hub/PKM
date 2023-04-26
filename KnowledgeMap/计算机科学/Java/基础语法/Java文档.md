# Java文档
* Java API
	* [官方Java17 API](https://docs.oracle.com/en/java/javase/17/)
* [Java文档注释](https://www.runoob.com/java/java-documentation.html)
    * 案例
      ```java
      /*** 这个类绘制一个条形图
       * @author runoob
       * @version 1.2
       */
      public class Comment{
        public static void main(String[] args){
        }
      }
      ```
    * 命令：`>javadoc -d 生成文档的文件夹 -x -y xxx.java`，比如`>javadoc -d ./doc -author -version Comment.java`