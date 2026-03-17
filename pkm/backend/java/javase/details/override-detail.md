1. 方法重写前两个字是“方法”，<u>属性是不能重写的</u>
2. 需要名称、返回类型和参数都一样
    ```java
    class People{
     public void say(){
       System.out.println("I love sleep!");
     }
    }
    class Student extends People{
     @Override
     public void say(){
       System.out.println("I LOVE STUDY!");
     }
    }
    ```
3. 返回类型和访问权限规则
    1. 返回类型可以一样，也可以是子类（如下案例，从 Child 变成了 Father）
    2. 访问权限可以一样，也可以变大（如下案例，从 protected 变成了 public）
    3. （访问权限为什么要这么设计） **里氏替换原则（LSP）**：子类对象应该能够替换父类对象而不破坏程序逻辑。如果子类方法访问权限更严格（如 `public` → `protected`），那么通过父类引用调用该方法时，原本可访问的方法可能变得不可访问，违反了替换原则。
   ```java
   class Father{}
   class Child extends Father{}
   
   class People{
     protected Father hello(){
       return new Father();
     }
   }
   class Student extends People{
     @Override
     public Child hello(){
       return new Child();
     }
   }
    // 从 Father 到 Child, 返回到类越缩越小
    // 这么想，爸爸的理想是“有出息”，儿子的理想是当公务员，越来越具体了
    
    // 从 protected 到 public, 返回类型越扩越大
    // 这么想，富豪爸爸的钱都留给儿子（父亲的钱只能儿子访问），儿子拿钱投身伟大事业（儿子的钱大家都能访问）
   ```
4. 调用多个重载的方法，遵循“就近原则”
    ```java
    @Test  
    public void test2(){  
      // 就近原则。  
      m(null);  
    }
    
    public void m(Object o){  
      System.out.println("Object...");  
    }  
    public void m(String o){  
      System.out.println("String...");  
    }
    //答案：会执行m(String o)，因为就近原则。
    ```