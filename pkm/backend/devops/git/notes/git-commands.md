# Git 命令

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="CYGdy" class="ne-image">

我们上面一直都是用图形化界面完成的操作。其实这些图形化界面上的操作底层都对应了 Git 相关的命令。

接下来我们学习一下 Git 的命令。

---

## 仓库操作

执行命令，我们用它就行：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766962243022-6edefd55-0162-4a53-a516-daa6e500cc98.png" width="212.8" title="" crop="0,0,1,1" id="u42bdb967" class="ne-image">

### 查看 git 版本

`git -v`

### 创建本地仓库

**先创建仓库的根目录，并进入根目录：实际上这两个命令和 git 无关，只是普通的 Linux 命令：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766962370986-b3642f45-6c92-49d1-b21a-81b3778a8fa5.png" width="541.6" title="" crop="0,0,1,1" id="u53c161dc" class="ne-image">

**通过 **`**git init**`**命令来初始化仓库：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766962598081-e04db190-3634-4774-bf45-e13596ba0534.png" width="964" title="" crop="0,0,1,1" id="u3f757399" class="ne-image">

到这里，本地仓库就创建成功了：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766962628385-dbb6f6ac-837b-4b65-b866-e88ea229e17d.png" width="238.4" title="" crop="0,0,1,1" id="u54578289" class="ne-image">

### 克隆远程仓库

**克隆远程仓库的核心命令：**`**git clone**`

**首先你需要获取到 gitee 上项目的克隆地址：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766963691311-b51afb88-98a6-4c6f-bbd2-ab7a25fc2fbe.png" width="696.8" title="" crop="0,0,1,1" id="u34597f42" class="ne-image">

**将 github 上的项目克隆下来：**

```shell
git clone https://github.com/dujubinaliyun/remote-test.git
```

**另外，克隆时也可以给仓库起别名：**

```shell
git clone https://gitee.com/du-jubin/remote-gitee-test.git remote-gitee-test2
```

### 配置仓库（局部配置）

配置仓库使用 `git config`命令。例如以下配置 `user.name`和 `user.email`：

如果你想对**某一个仓库进行配置**，可以进入到仓库的根目录，执行 `git config`：

```shell
git config user.name dujubinaliyun
git config user.email dujubin@aliyun.com
```

实际上修改的是这个文件：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766964135933-c1f8a914-e533-42d1-a031-8bc07a77d48e.png" width="217.6" title="" crop="0,0,1,1" id="u7702f9e1" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766964246686-bc5eaf66-a9d4-4af9-a1a6-88852c626904.png" width="329.6" title="" crop="0,0,1,1" id="u62f10b62" class="ne-image">

### 配置仓库（全局配置）

也可以通过 `--global`参数来设置仓库的全局配置：

```shell
git config --global user.name dujubinaliyun

git config --global user.email dujubin@aliyun.com
```

这个全局配置，在当前系统用户的主目录下会生成这样一个文件：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766964445187-d5749303-e205-4b81-8c19-9aeada90fb0c.png" width="211.2" title="" crop="0,0,1,1" id="u050c565e" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766964469634-ccf8b636-87dd-4ccc-ae6f-a66d7fbd65df.png" width="361.6" title="" crop="0,0,1,1" id="u0c6338cf" class="ne-image">

---

## 文件操作

### 查看暂存区状态

```shell
git status
```

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766966902403-49901661-afb7-4fdb-a8ef-a302fe1fca9b.png" width="823.2" title="" crop="0,0,1,1" id="ufd745fa8" class="ne-image">

### 添加文件到暂存区

```shell
