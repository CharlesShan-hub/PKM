流程是：`start()` → `start0()`（JVM）→ 新线程执行 → `run()`
- `start()`：Java 层面的启动入口（安全检查 + 状态管理）
- `start0()`：JVM 层面的线程创建和启动（操作系统线程创建）
- `run()`：线程实际执行的业务逻辑

```java
// Thread.java (java21)

/**  
 * Schedules this thread to begin execution. The thread will execute
 * independently of the current thread. 
 * 
 * <p> A thread can be started at most once. In particular, a thread can not 
 * be restarted after it has terminated. 
 *
 * @throws IllegalThreadStateException if the thread was already started  
 */
public void start() {  
    synchronized (this) {  
        // zero status corresponds to state "NEW".  
        if (holder.threadStatus != 0)  
            throw new IllegalThreadStateException();  
        start0();  
    }
}  
  
/**  
 * Schedules this thread to begin execution in the given thread container. 
 * @throws IllegalStateException if the container is shutdown or closed  
 * @throws IllegalThreadStateException if the thread has already been started  
 */
void start(ThreadContainer container) {  
    synchronized (this) {  
        // zero status corresponds to state "NEW".  
        if (holder.threadStatus != 0)  
            throw new IllegalThreadStateException();  
  
        // bind thread to container  
        if (this.container != null)  
            throw new IllegalThreadStateException();  
        setThreadContainer(container);  
  
        // start thread  
        boolean started = false;  
        container.onStart(this);  // may throw  
        try {  
            // scoped values may be inherited  
            inheritScopedValueBindings(container);  
  
            start0();  
            started = true;  
        } finally {  
            if (!started) {  
                container.onExit(this);  
            }        
        }    
    }
}  
  
private native void start0();  
  
/**  
 * This method is run by the thread when it executes. Subclasses of {@code  
 * Thread} may override this method.  
 * 
 * <p> This method is not intended to be invoked directly. If this thread is a
 * platform thread created with a {@link Runnable} task then invoking this method  
 * will invoke the task's {@code run} method. If this thread is a virtual thread  
 * then invoking this method directly does nothing. 
 * 
 * @implSpec The default implementation executes the {@link Runnable} task that  
 * the {@code Thread} was created with. If the thread was created without a task  
 * then this method does nothing. 
 */
@Override  
public void run() {  
    Runnable task = holder.task;  
    if (task != null) {  
        Object bindings = scopedValueBindings();  
        runWith(bindings, task);  
    }
}
```
