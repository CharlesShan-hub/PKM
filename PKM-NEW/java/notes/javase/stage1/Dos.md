# DOS指令

---

## 基础概念

### 运行原理
- 接受指令 → 解析指令 → 执行指令

### 参考资料
- [Microsoft DOS and Windows command line](https://www.computerhope.com/msdos.htm)

### 路径处理
- **相对路径与绝对路径**
- **路径中有空格的处理方法**：[DOS命令中文件路径有空格的处理方法](http://t.csdn.cn/8C1bi)
  1. 用双引号把路径括起来
  2. 使用8.3格式缩写：
     - 规则：取前6个字符（略去空格）+ `~` + 数字
     - 示例：
       - `C:\Program Files` → `C:\Progra~1`
       - `Documents and Settings` → `DOCUME~1`
       - `Local Settings` → `LOCALS~1`
       - 如果有多个相似名称：`Progra~1`, `Progra~2`, `Progra~3`
       - 总字母不足6个：`C:\aa bb` → `C:\aabb~1`
  3. 路径映射：
     - 命令：`subst w: "C:\Documents and Settings"`
     - 使用：`w:\` 替代 `C:\Documents and Settings`

---

## 常用命令

### 目录操作
- **`dir`** - 列出目录内容（类似Linux的`ls`）
  - 查看指定目录：`dir 绝对路径`
- **`cd`** - 切换目录
  - 切换盘符（**重点**）：`盘符:`（如：`D:`）
  - 跨盘并进入指定目录：`cd /D 绝对路径`（如：`cd /D D:\path`）
- **`tree`** - 显示目录树
  - 使用案例：[MS-DOS and Windows command line tree command](https://www.computerhope.com/treehlp.htm)
- **`md`** - 创建目录
- **`rd`** - 删除目录

### 文件操作
- **`copy`** - 复制文件
- **`del`** - 删除文件
- **`move`** - 移动文件
- **`type`** - 显示文件内容（类似Unix的`cat`）
- **`echo`** - 输出内容到文件

### 系统操作
- **`cls`** - 清屏（类似Mac的`clear`）
- **`exit`** - 退出DOS

---

## Windows快捷键

### 窗口管理
- **Win + D** - 显示桌面
- **Win + E** - 打开文件资源管理器
- **Win + R** - 打开运行窗口
- **Win + L** - 锁屏
- **Alt + Tab** - 应用之间的切换

---

## 使用技巧

1. **路径引用**：当路径包含空格时，始终使用双引号
2. **快速切换**：使用`cd /D`在不同驱动器间切换
3. **目录查看**：使用`tree /F`查看包含文件的目录树
4. **命令帮助**：大多数命令支持`/？`参数查看帮助（如：`dir /？`）