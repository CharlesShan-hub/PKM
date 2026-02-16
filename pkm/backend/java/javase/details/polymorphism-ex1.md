
```java
public class Exercise1{
	public static void main(String[] args){
		double d = 13.4;
		long l = (long)d;
		System.out.println(l);
		int in = 5;
		boolean b = (boolean)in;
		Object obj = "Hello";
		String objStr = (String)obj;
		System.out.println(objStr);
		Object obj = new Integer(5);
		String str = (String)objPri;
		Integer str1 = (Integer)objPri;
	}
}
```

```java
public class Exercise1{
	public static void main(String[] args){
		// 可以
		double d = 13.4;
		// 可以
		long l = (long)d;
		// 可以，13
		System.out.println(l);
		int in = 5;
		// 不可以，int不能转成boolean
		boolean b = (boolean)in;
		// 可以，向上转型，Hello
		Object obj = "Hello";
		// 可以，向下转型  
		String objStr = (String)obj;
		System.out.println(objStr);
		// 可以，向上转型
		Object obj = new Integer(5);
		// 错误，只能向下转型到int
		String str = (String)objPri;
		// 可以，向下转型
		Integer str1 = (Integer)objPri;
	}
}
```
