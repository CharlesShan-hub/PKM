
```java
package ex_thread;  

public class Yield{  
  public static void main(String[] args) throws InterruptedException{  
    T1 t1 = new T1();  
    t1.start();  
    for(int i=0;i<10;i++){  
      System.out.println(Thread.currentThread().getName()+i);  
      Thread.sleep(100);  
      if(i == 5){  
        t1.join();  
      }        
    }    
  }
}  

class T1 extends Thread{  
  @Override  
  public void run() {  
    for(int i=0;i<10;i++){  
      System.out.println(Thread.currentThread().getName()+i);  
      try{  
        Thread.sleep(100);  
      }catch(InterruptedException e){  
        throw new RuntimeException(e);  
      }        
    }    
  }
}
```

```txt
main0
Thread-00
main1
Thread-01
main2
Thread-02
main3
Thread-03
Thread-04
main4
Thread-05
main5
Thread-06
Thread-07
Thread-08
Thread-09
main6
main7
main8
main9
```
