# 需要提交所有

git commit -m 解决冲突

```

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766973282361-7a7e589e-12ec-4931-acf5-9597d4173908.png" width="689.6" title="" crop="0,0,1,1" id="u0ff95774" class="ne-image">

---

## 标签操作

### 为什么需要标签

目的是：语义化，增强可读性，增强可维护性。

打标签本质上是给某个提交记录起别名。

### 查看当前仓库中有哪些标签

```shell

git tag

```

当你没有创建任何标签时，什么也不会输出。

### 创建标签

创建一个新的仓库：

1. 创建 a.txt 并提交
2. 创建 b.txt 并提交
3. 创建 c.txt 并提交
4. 查看历史提交记录

```shell

mkdir repo-7
cd repo-7
touch a.txt
git add a.txt
git commit -m 创建a

touch b.txt
git add b.txt
git commit -m 创建b

touch c.txt
git add c.txt
git commit -m 创建c

git log --oneline

```

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766973852930-5b9052b9-6b1c-44cd-8279-4a6fd5b35dcd.png" width="436.8" title="" crop="0,0,1,1" id="u55a5b959" class="ne-image">

**为创建 a 这一次的提交打一个标签：**

```shell

git tag newFileA 985455a

```

**再次查看标签，此时当前分支中就有一个标签了：**

```shell

git tag

```

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766974210004-91dfec0b-7497-441f-a639-ce6b041131df.png" width="584" title="" crop="0,0,1,1" id="u2d0ee0d9" class="ne-image">

### 再次查看历史记录时也有标签了

```shell

git log --oneline

```

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766974399878-8ca4e1b4-031a-482b-a7ac-eef10b8267a1.png" width="392.8" title="" crop="0,0,1,1" id="uc44d7d15" class="ne-image">

而且也可以通过下面的命令查看某个标签之前的所有历史提交记录了：

```shell

git log newFileA

```

### 删除标签

```shell

git tag -d newFileA

```

删除之后，标签就没有了：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766974559050-779d3a0c-3879-49c0-a232-d3c51f9811aa.png" width="616.8" title="" crop="0,0,1,1" id="ufc0f4a10" class="ne-image">

### 基于标签创建分支

我们之前可以根据历史提交 id 来创建分支，当然也可以通过标签名来创建分支：

```shell

git checkout -b haha newFileA

```

---

## 远程仓库的操作

### 公司只提供 SSH 的远程仓库怎么办

将远程仓库的项目 clone 到本地：

```shell

git clone https://gitee.com/du-jubin/remote-gitee-test.git

```

**打开克隆的项目，找到 **`**.git/config**`**文件，如下：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766975715009-92ad5cf6-c368-4256-b921-b7ba8c5a3ace.png" width="463.2" title="" crop="0,0,1,1" id="ua8c01966" class="ne-image">

其中 url 就是远程仓库的地址。但实际开发中，**很多公司（尤其是注重安全和内部网络管理的）**不提供或不推荐使用 HTTPS 协议**访问 Git 仓库，而是**仅提供 SSH 协议咱们来模拟一下，一些公司只提供 SSH 的场景：第一步：**找到远程仓库的 SSH 链接，如下，拷贝 SSH 地址

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766976034660-85713c40-9eff-43bd-a08d-8a5aad2cd56a.png" width="678.4" title="" crop="0,0,1,1" id="u4758d006" class="ne-image">

**第二步：**将 SSH 地址修改到 config 文件中

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766976081219-909335d0-2a51-4d6a-bec4-5ec9a78d3128.png" width="434.4" title="" crop="0,0,1,1" id="ud3ec8943" class="ne-image">

**第三步：**在本地工作区中创建文件，并添加到暂存区，提交到本地仓库

```shell

cd remote-gitee-test/
touch Test.java
git add Test.java
git commit -m 提交Test

```

**第四步：**push 到远程仓库

```shell
