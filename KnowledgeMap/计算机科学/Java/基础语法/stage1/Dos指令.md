# Dos指令
* [Microsoft DOS and Windows command line](https://www.computerhope.com/msdos.htm)
* 运行思路：接受指令 -> 解析指令 -> 执行指令
* 路径
	* 相对路径与绝对路径
	* [DOS命令中文件路径有空格的处理方法](http://t.csdn.cn/8C1bi)
		* 可以用双引号把路径括起来
		* 缩写：比如c:\\Program Files缩写为c:\\Progra~1，采用8个字符缩写，即写头六个字母(略去空白），另加波浪号和1,首字母不足六个字母，略去空白，用了第二个词的字母，凑成六个。例如：  "Documents and Settings“ -- DOCUME~1  ，"Local Settings" -- LOCALS~1
		* Program Files  Progra file  Progra zhang  则三个目录分别表示为：C:\Progra~1; C:\Progra~2; C:\Progra~3;
		* 如果是总字母不足6个，例如 C:\\aa bb 则表示为C:\\aabb~1
		* 路径映射：例如：在CMD中输入 subst w: "C:\\Documents and Settings" 然后就可以直接用w:\\替代C:\\Documents and Settings了
* dir（类似于Mac的ls）
	* 可以通过`dir 绝对路径` 来查看制定目录的dir
* cd
	* 从其他盘切换到C盘：`cd /D C`
* tree：查看文件树
	* 使用案例：[MS-DOS and Windows command line tree command](https://www.computerhope.com/treehlp.htm)
* cls：清除屏幕，类似于Mac的clear
* exit：退出dos
* md：创建目录
* rd：删除目录
* copy：拷贝文件
* del：删除文件
* echo：输入内容到文件
* type：类似于unix的cat，显示文件
* move：移动文件