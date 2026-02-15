
join练习：
1. **主线程任务**：
   - 每隔1秒输出"hi"
   - 共输出10次
2. **子线程触发条件**：
   - 当主线程输出到第5次"hi"时
   - 启动一个实现`Runnable`接口的子线程
3. **子线程任务**：
   - 每隔1秒输出"hello"
   - 输出满10次后自动退出
4. **线程后续**：
   - 子线程结束后继续输出剩余"hi"
   - 直到完成10次输出

```java
package ex_thread;  

public class Ex02 {  
  public static void main(String[] args) throws InterruptedException {  
    Thread thread = new Thread(new Child());  

    for(int i = 0;i < 10;i++){  
      System.out.println("hi"+i);  
      Thread.sleep(1000);  
      if(i == 5){  
        thread.start();  
        thread.join();  
      }        
    }  
  }
}  

class Child implements Runnable {  
  @Override  
  public void run(){  
    for(int i=0;i<10;i++){  
      System.out.println("hello"+i);  
      try{  
        Thread.sleep(50);  
      }catch(InterruptedException e){  
        e.printStackTrace();  
      }        
    }    
  }
}  

//hi0  
//hi1  
//hi2  
//hi3  
//hi4  
//hi5  
//hello0  
//hello1  
//hello2  
//hello3  
//hello4  
//hello5  
//hello6  
//hello7  
//hello8  
//hello9  
//hi6  
//hi7  
//hi8  
//hi9
```
