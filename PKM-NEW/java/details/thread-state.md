
```java
package ex_thread;  
  
public class State {  
    public static void main(String[] args) throws InterruptedException {  
        T t = new T();  
        System.out.println(t.getName()+"  "+t.getState()); // NEW
        t.start();  
        while(Thread.State.TERMINATED != t.getState()) {  
            System.out.println(t.getName()+"  "+t.getState());  
            Thread.sleep(10);  
        }  
        System.out.println(t.getName()+"  "+t.getState());  
    }
}  
  
class T extends Thread{  
    @Override  
    public void run() {  
        for(int i=0; i<5; i++){  
            System.out.println(Thread.currentThread().getName()+i);  
            try {  
                Thread.sleep(5);  
            } catch (InterruptedException e) {  
                throw new RuntimeException(e);  
            }        
        }    
    }
}
```
