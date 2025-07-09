# jUnit

```java
package com.powernode.javase;  
  
import org.junit.jupiter.api.*;  
  
/**  
 * 测试用例  
 */  
public class MathTest {  
  
    @BeforeAll  
    public static void before(){  
        System.out.println("(BeforeAll)开始执行单元测试了！");  
    }  
  
    @AfterAll  
    public static void after(){  
        System.out.println("(AfterAll)单元测试执行完毕！");  
    }  
  
    @BeforeEach  
    public void beforeEach(){  
        System.out.println("(BeforeEach)单元测试方法开始执行");  
    }  
  
    @AfterEach  
    public void afterEach(){  
        System.out.println("(AfterEach)单元测试方法执行结束");  
    }  
  
    /**  
     * 单元测试方法  
     */  
    @Test  
    public void testSum() {  
        System.out.println("(Test)testSum");  
        // 实际值：程序运行之后的结果  
        int actual = Math.sum(10, 20);  
        // 期望值：你觉得这个结果应该是多少  
        int expected = 30;  
        // 断言（断言机制）  
        Assertions.assertEquals(expected, actual);  
    }  
  
    @Test  
    public void testSub() {  
        System.out.println("(Test)testSub");  
        int actual = Math.sub(20, 10);  
        int expected = 10;  
        Assertions.assertEquals(expected, actual);  
    }  
  
    @Test  
    public void testMul() {  
        System.out.println("(Test)testMul");  
        int actual = Math.mul(20, 10);  
        int expected = 200;  
        Assertions.assertEquals(expected, actual);  
    }  
  
    @Test  
    public void testDiv() {  
        System.out.println("(Test)testDiv");  
        int actual = Math.div(20, 10);  
        int expected = 2;  
        Assertions.assertEquals(expected, actual);  
    }  
  
}
```

```
(BeforeAll)开始执行单元测试了！
(BeforeEach)单元测试方法开始执行
(Test)testDiv
(AfterEach)单元测试方法执行结束
(BeforeEach)单元测试方法开始执行
(Test)testMul
(AfterEach)单元测试方法执行结束
(BeforeEach)单元测试方法开始执行
(Test)testSub
(AfterEach)单元测试方法执行结束
(BeforeEach)单元测试方法开始执行
(Test)testSum
(AfterEach)单元测试方法执行结束
(AfterAll)单元测试执行完毕！
```