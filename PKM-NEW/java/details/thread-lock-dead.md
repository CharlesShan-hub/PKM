
```java
package ex_thread;  

public class DeadClock {  
  public static void main(String[] args) {  
    new DeadClockThread(true).start();  
    new DeadClockThread(false).start();  
    // Thread-12  
    // Thread-01    
  }  
}  

class DeadClockThread extends Thread{  
  static Object o1 = new Object();  
  static Object o2 = new Object();  
  boolean flag = true;  

  public DeadClockThread(boolean flag){  
    this.flag = flag;  
  }  

  @Override  
  public void run() {  
    if(flag){  
      synchronized (o1) {  
        System.out.println(Thread.currentThread().getName()+"1");  
        try {  
          Thread.sleep(10000);  
        } catch (InterruptedException e) {  
          throw new RuntimeException(e);  
        }                
        synchronized (o2) {  
          System.out.println(Thread.currentThread().getName()+"2");  
        }            
      }        
    }else{  
      synchronized (o2) {  
        System.out.println(Thread.currentThread().getName()+"2");  
        try {  
          Thread.sleep(10000);  
        } catch (InterruptedException e) {  
          throw new RuntimeException(e);  
        }                
        synchronized (o1) {  
          System.out.println(Thread.currentThread().getName()+"1");
        }            
      }        
    }   
  }
}
```
