
注意下边的调用方法进行了更换，要使用
```java
ThreadTicket ticket = new ThreadTicket("窗口");  
new Thread(ticket, "窗口1").start(); 
new Thread(ticket, "窗口2").start(); 
new Thread(ticket, "窗口3").start();
```

完整代码如下

```java
public class Ticket {
  public static void main(String[] args) {
    ThreadTicket ticket = new ThreadTicket();  
    new Thread(ticket, "窗口1").start(); 
    new Thread(ticket, "窗口2").start(); 
    new Thread(ticket, "窗口3").start();
  }
}

class ThreadTicket extends Thread {  
  private static int ticket = 300; // 让多个线程共享票数  

  public boolean sell(){  
    synchronized(this) {
      if (ticket <= 0) {  
        System.out.println("已卖完");  
        return false;  
      }else{  
        try{  
          Thread.sleep(50);  
        }catch (InterruptedException e){  
          e.printStackTrace();  
        }            
        System.out.println(Thread.currentThread().getName()+"售出一张票, 还剩余"+ --ticket);  
        return true;  
      }   
    } 
  }    
  @Override  
  public void run() {  
    System.out.println("Start");  
    while (true) {  
      if(!sell()){  
        break;  
      }        
    }    
  }
}
```

**三个 Thread 操作的是同一个对象！这样才能成功的锁上**，所以就算传入的是别的，比如 object，也可以，只要他们是一个对象

```java
public class Ticket {
    public static void main(String[] args) {
	    ThreadTicket ticket = new ThreadTicket();  
        new Thread(ticket, "窗口1").start(); 
        new Thread(ticket, "窗口2").start(); 
        new Thread(ticket, "窗口3").start();
    }
}

class ThreadTicket extends Thread {  
    private static int ticket = 300; // 让多个线程共享票数  
    private Object obj = new Object(); // <- 这样
  
    public boolean sell(){  
        synchronized(obj) { // <- 这样
	        if (ticket <= 0) {  
	            System.out.println("已卖完");  
	            return false;  
	        }else{  
	            try{  
	                Thread.sleep(50);  
	            }catch (InterruptedException e){  
	                e.printStackTrace();  
	            }            
	            System.out.println(Thread.currentThread().getName()+"售出一张票, 还剩余"+ --ticket);  
	            return true;  
	        }   
        } 
    }
    @Override  
    public void run() {  
        System.out.println("Start");  
        while (true) {  
            if(!sell()){  
                break;  
            }        
        }    
    }
}
```

最后，我们的`synchronized(this)`如果是对一个方法整体进行同步，那么就可以等价于对方法进行`synchronized`并且共享对象就是`this`
