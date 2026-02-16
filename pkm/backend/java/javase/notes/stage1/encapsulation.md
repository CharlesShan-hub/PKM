# 封装

浏览顺序：本文 👉 [extends](extends.md) 👉 [polymorphism](polymorphism.md)

1. 封装（encapsulation）：把抽象出来的数据（属性）和对数据的操作（方法）封装在一起，数据被保护在内部，程序的其他部分只有通过被授权的操作（方法），才能对数据进行访问。
2. 案例一[encapsulation-demo-01](../../details/encapsulation-demo-01.md)：getter和setter（与构造器结合）
3. 案例二[encapsulation-demo-02](../../details/encapsulation-demo-02.md)：对赋值进行规则判断
4. Java Bean（实体类标准）：👉 [java bean](../heima/javabean.md)
	1. 类中所有的成员变量全部私有，并提供 `public` 修饰的 `getter/setter` 方法
	2. 类中需要提供一个无参数构造器，有参数构造器可选