# 基于某个历史提交id（61393eb）创建一个分支（hehe）

git checkout -b hehe 61393eb

```

### 合并

注意分支合并原则：假设有 a 分支和 b 分支，如果要将 b 分支合并到 a 分支上，你需要先切换到 a 分支上，在 a 分支上执行 `git merge`命令。

基于上面的分支继续操作，当前我们有 `master`分支和 order 分支。

我们要完成的效果是：将 order 分支合并到 master 分支上。

**第一步：**在 order 分支上创建 Test.java 文件，并且提交到本地仓库

```shell

git checkout order
touch Test.java
git add Test.java
git commit -m 添加Test Test.java

```

**第二步：**将 order 分支合并到 master 分支，首先你需要将分支切换到 master 分支

```shell

git checkout master
git merge order

```

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766972642113-c60de22d-110c-40ac-aae0-a650fd3db55b.png" width="596" title="" crop="0,0,1,1" id="u343b0241" class="ne-image">

合并后可以看看 master 分支上是否存在 Test.java 文件。

### 合并时的冲突问题

假设现在我将 master 分支上的 Test.java 内容修改并提交到本地仓库。

```shell

git checkout master
echo hello >> Test.java
git add Test.java
git commit -m 修改Test Test.java

```

然后再将 order 分支上的 Test.java 内容修改并提交到本地仓库。

```shell

git checkout order
echo world >> Test.java
git add Test.java
git commit -m 修改Test Test.java

```

最后再将 order 分支合并到 master 分支上，会不会冲突呢？

```shell

git checkout master
git merge order

```

冲突如下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766972975611-1fc11b51-b807-433b-8eeb-1e06fae9f3bc.png" width="792" title="" crop="0,0,1,1" id="u54e9612c" class="ne-image">

必须人为干涉解决冲突：

```shell
