1. exit 退出当前程序
	```java
	exit(0);
	```
2. arraycopy : 复制数组元素，比较适合底层调用，一般使用 Arrays.copyOf 完成复制数组. 
	```java
	int[] src={1,2,3};  
	int[] dest = new int[3];  
	System.arraycopy(src, 0, dest, 0, 3);
	// 翻译一下就是从「A」的第「几」个，复制到「B」的第「几」个，一共赋值「n」的元素
	// `src`: 源数组。
	// `srcPos`: 从源数组的哪个索引位置开始拷贝。
	// `dest`: 目标数组，即将源数组的数据拷贝到的数组。
	// `destPos`: 把源数组的数据拷贝到目标数组的哪个索引位置。
	// `length`: 从源数组拷贝多少个数据到目标数组。
	```
3. currentTimeMillens：返回当前时间距离1970-1-1 的毫秒数
4. gc:运行垃圾回收机制 System.gc();