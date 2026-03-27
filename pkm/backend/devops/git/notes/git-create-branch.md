# 创建分支

git branch user

```

控制台提示信息如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766971137193-55fe1ff0-d8ac-4bcc-8196-97f5bd2ad9d1.png" width="614.4" title="" crop="0,0,1,1" id="u383f3555" class="ne-image">

**这个错误**`**fatal: not a valid object name: 'master'**`**的意思是：**当前仓库中不存在名为**`**master**`**的分支或提交对象**。注意：**这是一个全新的、完全空的仓库，**还没有进行任何提交。当你做了第一个提交动作之后，master 分支就创建了。创建新文件，提交到仓库，然后再创建 user 分支：**

```shell

touch a.txt
git add a.txt
git commit -m 提交a文件

