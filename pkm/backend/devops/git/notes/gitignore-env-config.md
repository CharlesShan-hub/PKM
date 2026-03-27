# 环境配置（包含密码）

application-dev.properties

```

### 演示忽略机制

**第一步：创建一个仓库。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766930203939-f48ee419-3452-4ec3-9d08-b466ea3974e5.png" width="386.4" title="" crop="0,0,1,1" id="ufd61bb72" class="ne-image">

创建完成后，会看到根目录下有这样一个文件：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766930252352-efb01b4c-499a-4ebd-bbbd-ef99a0a5f483.png" width="226.4" title="" crop="0,0,1,1" id="u942958b0" class="ne-image">

打开看看：可以看到，它自动生成的忽略机制中忽略 `.log`文件。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766930283504-961ec20e-5f20-4f6c-bf99-cd17e398b18e.png" width="722.4" title="" crop="0,0,1,1" id="u30071932" class="ne-image">

**第二步：向仓库中添加被忽略的文件试试**

我们来创建一个 `.log`文件。看看是什么情况。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766930353805-cd85f8cf-f664-42b3-a9fa-f2dcb9c1c9de.png" width="327.2" title="" crop="0,0,1,1" id="uc05fd63f" class="ne-image">

可以看到，压根不会让文件进入暂存区，也就是没有执行 `git add`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766930404080-c2721c72-60d0-4877-9d80-3ec94f78e257.png" width="283.2" title="" crop="0,0,1,1" id="uf32dfd38" class="ne-image">

我们再创建一个 java 文件试试：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766930435380-6fc54ff2-6a2d-473c-8c3d-808769fa792a.png" width="213.6" title="" crop="0,0,1,1" id="ubd86761d" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766930445203-0109a349-10d9-49f5-92f0-ffaa2de9e66f.png" width="249.6" title="" crop="0,0,1,1" id="u3181b6b1" class="ne-image">

### 在 GitHub Desktop 中通过操作也可以忽略

这样测试一下：我们在仓库的根目录下创建多个 `.bak`结尾的文件。默认它是不会忽略的。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766930530149-bd16c786-22e7-405e-b989-0147e62c28d6.png" width="174.4" title="" crop="0,0,1,1" id="u258b970e" class="ne-image">

可以看到被 git 追踪了：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766930544697-8a7d2571-4c11-4978-8b36-4cfb1c65c276.png" width="280" title="" crop="0,0,1,1" id="uee4e10d3" class="ne-image">

你通过客户端工具也可以来进行设置：忽略所有的 bak 文件

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766930571225-292bb96b-c2db-4d7c-986c-c00dcb5b19cb.png" width="366.4" title="" crop="0,0,1,1" id="ud0dbc410" class="ne-image">

你会看到，`.gitignore`文件中多了这个配置，bak 文件就被忽略了：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766930730224-461280cd-21da-4289-8b33-b51b88bb49e3.png" width="140.8" title="" crop="0,0,1,1" id="u746503e9" class="ne-image">

---

## 图标与文件比对

创建仓库 `repo-4`：

**第一步：**先创建文件：`a.txt`、`b.txt`，提交到本地仓库。

**第二步：**删除文件 a.txt、修改 b.txt、新建 c.txt，你会看到如下图标。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766931496060-97eecb2e-ba9a-4140-a5ed-5de8d3443cee.png" width="552" title="" crop="0,0,1,1" id="u6d9855b8" class="ne-image">

**另外还有比对功能：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766931687572-560039d4-bb68-4dd8-8e6f-9fc22986cbeb.png" width="543.2" title="" crop="0,0,1,1" id="ubef20ae6" class="ne-image">

`**@@ -0,0 +1 @@**`

+ `**-0,0**`**：代表“原始文件”（**`**-**`**）在第0行开始，有0行内容。也就是**这个文件原本不存在**。**
+ `**+1**`**：代表“新文件”（**`**+**`**）在第1行开始，有1行内容。也就是**现在这个文件从第1行开始有1行内容**。**
+ **这个**`**@@ ... @@**`**是 Git 用来定位更改位置范围的标记。再修改一下**`**b.txt**`**，再来看看比对结果：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766931792967-417e1810-43c5-4846-8e0e-f0954e1f9758.png" width="306.4" title="" crop="0,0,1,1" id="ud1a7b9a1" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766931816639-0a4ac38e-58de-411d-b645-076792e40895.png" width="270.4" title="" crop="0,0,1,1" id="u2a113311" class="ne-image">

