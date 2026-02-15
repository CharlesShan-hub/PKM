
```java
package ex_thread;  

public class Demo {  
  public static void main(String[] args) {  
    People people = new People();  
    people.setName("Charles");  
    people.setPriority(Thread.MIN_PRIORITY);  
    people.start();  
    try {  
      Thread.sleep(5000);  
    } catch (InterruptedException e) {  
      throw new RuntimeException(e);  
    }        
    people.interrupt();  
  }
}  

class People extends Thread {  
  @Override  
  public void run() {  
    for (int i = 0; i < 10; i++) {  
      System.out.println(Thread.currentThread().getName()+"在吃包子"+i);  
    }        
    System.out.println(Thread.currentThread().getName()+"开始休息");  
    try {  
      Thread.sleep(20000);  
    } catch (InterruptedException e) {  
      System.out.println(Thread.currentThread().getName()+"的休息被中断");  
    }        
    for (int i = 0; i < 10; i++) {  
      System.out.println(Thread.currentThread().getName()+"在继续吃包子"+i);  
    }    
  }
}
```
