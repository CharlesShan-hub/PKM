# IDEA 使用 Git

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="V2HMx" class="ne-image">

---

## 创建空项目

在 IDEA 中创建一个空的项目，在空项目中随便创建一个文件。随便编写一些内容。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766932603985-5777e184-a30e-4571-96e4-00adee263401.png" width="764.8" title="" crop="0,0,1,1" id="ub6f5287f" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766932641344-5a806ca2-6819-4354-af5d-825d01dd6f07.png" width="439.2" title="" crop="0,0,1,1" id="u0d35e30e" class="ne-image">

---

## 将项目推送到 github

**点击菜单中的 VCS，选择 Share Project on GitHub

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766932771377-a23449f0-5aa6-4754-9d62-092a9d8b84c2.png" width="718.4" title="" crop="0,0,1,1" id="ufbcb9c82" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766932822369-c18e00c1-3b10-4317-88ff-c5c8340fe048.png" width="524.8" title="" crop="0,0,1,1" id="ufe24e78b" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766932859120-f21349db-1bb8-44b6-91b5-8783516b5599.png" width="288" title="" crop="0,0,1,1" id="u8e75d5ea" class="ne-image">

然后会打开浏览器，用你的 github 账号给 IDEA 授权：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766932963730-386d135b-30cb-4025-909d-ea9cf35d3d04.png" width="520" title="" crop="0,0,1,1" id="uea966731" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766933078150-e33fdb9a-d40c-4ef8-976e-e830dab6c406.png" width="367.2" title="" crop="0,0,1,1" id="uaf419955" class="ne-image">

看看 GitHub 上有没有项目：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766933175175-7097b783-5167-4d79-b46d-93b4803771f0.png" width="404" title="" crop="0,0,1,1" id="ude835dfd" class="ne-image">

---

## 将修改提交到本地仓库或远程仓库

**将文件 **`**a.txt**`**的内容修改一下：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766933320662-a1481390-0734-4f58-a6c8-d02e2293cc0f.png" width="442.4" title="" crop="0,0,1,1" id="u2837734e" class="ne-image">

**然后在文件上右键：选择 **`**Commit File**`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766933379724-d18de940-3bef-4a62-b1e3-e97004f210dc.png" width="584" title="" crop="0,0,1,1" id="u4650376d" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766933459971-ccb7fba3-2c69-44d8-b740-89cfd56c5224.png" width="240.8" title="" crop="0,0,1,1" id="uf8ce11fd" class="ne-image">

但当你第一次选择提交到本地仓库后，如果没有再做任何修改，点击右侧按钮是无法推送到远程仓库的。

**你可以这样做：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766933719778-d06d534d-83b6-4c7a-964f-808405a3b6d2.png" width="699.2" title="" crop="0,0,1,1" id="u10091644" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766933788691-7d062717-5226-4eb3-8535-60b08d37effe.png" width="761.6" title="" crop="0,0,1,1" id="ucf02324d" class="ne-image">

---

## 代码合并（将 github 仓库中代码修改后合并到本地仓库）

在 GitHub 的仓库中直接修改代码：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766934021661-394a80da-4552-495f-81f4-40e9c6807f8f.png" width="1167.2" title="" crop="0,0,1,1" id="u532775ac" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766934062348-ab4282a1-f47d-444e-b619-4c7e12510a32.png" width="1140" title="" crop="0,0,1,1" id="ua42d5a0d" class="ne-image">

**将 GitHub 远程仓库中的代码拉取下来并自动合并：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766934145130-428938ad-43a1-40b6-8572-f8343a048671.png" width="319.2" title="" crop="0,0,1,1" id="ue0cc0d73" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766934175920-00548f91-17ef-481b-b350-65d6e95bc868.png" width="452.8" title="" crop="0,0,1,1" id="ud0275880" class="ne-image">

**注意：pull 下面还有一个 fetch，他俩的区别是：**

`**pull**`**=**`**fetch**`**（获取更新） +**`**merge**`**（自动合并），而**`**fetch**`**只获取不合并。

**fetch 成功的效果是：静默地将远程仓库的最新信息（如新分支、新提交）下载到你的本地仓库，但完全不会改动你正在工作的代码文件。在 IDEA 的**Git → Log**视图里，原本只显示你本地的提交历史。**`**fetch**`**成功后，你可以看到远程分支已经跑到前面去了，领先于你的本地分支。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766934834196-f1559cf8-0915-40b7-9cc2-65490489d63a.png" width="1186.4" title="" crop="0,0,1,1" id="u593f9dc1" class="ne-image">

**如果你看着日志感觉没问题，可以再手动合并：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766934887606-717d45a9-2182-4377-8765-5a18ec602071.png" width="309.6" title="" crop="0,0,1,1" id="u132fd014" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766935027151-a59fd54c-5480-4b58-aa52-ccb5a410c0ec.png" width="421.6" title="" crop="0,0,1,1" id="u60be5f0c" class="ne-image">

`Merge`的作用是：**将另一个分支的更改整合到当前分支**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766935131783-4162d88c-6a01-4615-a026-69060b033533.png" width="364.8" title="" crop="0,0,1,1" id="u738057cd" class="ne-image">

---

## 克隆远程仓库的项目

操作步骤非常简单，直接点击 Git，然后选择 Clone：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766935268090-cee0bae5-d3e2-405d-9945-d7d9555db9cf.png" width="304.8" title="" crop="0,0,1,1" id="ucd846f5c" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766935376954-13b81bb9-5466-4513-8708-5234b78b764e.png" width="790.4" title="" crop="0,0,1,1" id="u1bd2f361" class="ne-image">

克隆之后的效果就是新建一个项目：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766935417058-61f713c5-5441-4556-8e90-592bb7e6a74d.png" width="552" title="" crop="0,0,1,1" id="uc29a6c48" class="ne-image">

