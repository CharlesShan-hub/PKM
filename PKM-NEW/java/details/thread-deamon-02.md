
```java
package ex_thread;  
  
public class Deamon {  
    public static void main(String[] args) throws InterruptedException {  
        MyDeamon myDeamon = new MyDeamon();  
        myDeamon.setDaemon(true);
        myDeamon.start();
        for(int i=0; i<5; i++){  
            System.out.println("宝强在工作...");  
            Thread.sleep(100);  
        }
        System.out.println("宝强回家了");
        if(myDeamon.isAlive()){
	        System.out.println("💥被发现了");
	        // 因为现在JVM这个进程还没结束，所以还是被发现了😆
        }else{
	        System.out.println("💚无事发生");
        }
    }
}
  
class MyDeamon extends Thread{  
    @Override  
    public void run() {  
        while(true){  
            System.out.println("马蓉和宋喆在开心聊天~~");
            try{  
                Thread.sleep(50);
            }catch(InterruptedException e){
                e.printStackTrace();  
            }
        }
    }
}  
 
//马蓉和宋喆在开心聊天~~  
//宝强在工作...  
//马蓉和宋喆在开心聊天~~  
//马蓉和宋喆在开心聊天~~  
//宝强在工作...  
//马蓉和宋喆在开心聊天~~  
//宝强在工作...  
//马蓉和宋喆在开心聊天~~  
//马蓉和宋喆在开心聊天~~  
//宝强在工作...  
//马蓉和宋喆在开心聊天~~  
//马蓉和宋喆在开心聊天~~  
//宝强在工作...  
//马蓉和宋喆在开心聊天~~  
//马蓉和宋喆在开心聊天~~  
//  
//Process finished with exit code 0
```
