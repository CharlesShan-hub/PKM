# 程序员的一天

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg" width="4308" title="" crop="0,0,1,1" id="TnDmi" class="ne-image">

**核心理念**：**“永远在正确的分支上做正确的事，先拉后推。”**

---

## 第一步：早上一来，更新代码（防冲突）

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766979051598-001c1a4a-cb24-4e69-b3de-9ebd62e31a73.png" width="311.2" title="" crop="0,0,1,1" id="ud1f919fa" class="ne-image">

`**Update Project**`**更智能、更安全**，**`**Pull**`**是直接执行默认的合并。公司一般推荐**`**Update Project...**`

---

## 第二步：开始新功能？创建分支（隔离开发）

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766979208679-012e3665-f830-4ab5-a055-f4772d234c9d.png" width="309.6" title="" crop="0,0,1,1" id="ud9b4116a" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766979231174-aa6c83eb-5938-4f96-bfca-f26875cdce7a.png" width="367.2" title="" crop="0,0,1,1" id="u38c55531" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766979253245-bc448fb3-ab9a-42c3-ab47-7db4bc29498a.png" width="424.8" title="" crop="0,0,1,1" id="u1929e107" class="ne-image">

_命名规则：_`feature/功能`_、_`fix/修复`_、_`hotfix/紧急修复`_。_

**自动切换到新分支**，开始 coding。

---

## 第三步：日常提交（细粒度，多提交）

**写一部分代码就提交**，别等到下班。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766979727746-4e6c3c11-e79f-45b6-9c39-5c029173e962.png" width="338.4" title="" crop="0,0,1,1" id="u789b51f0" class="ne-image">

+ **勾选**要提交的文件。
+ **写清晰的提交信息**，例如：“新增用户登录验证逻辑”。
+ **点击 **`Commit`（仅本地）或 `Commit and Push`（提交并推送到远程）。

---

## 第四步：推送代码到远程（备份与协作）

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766979686730-0368e693-4779-4881-a114-ed744a0b512d.png" width="292" title="" crop="0,0,1,1" id="ud7e112d9" class="ne-image">

_**注意：push 推送到远程仓库只是推送到远程仓库的对应分支上了。所以你不需要担心。你需要关注的是在远程仓库中你的分支与 master 主分支的合并，这个千万不要随便来。**_

_**推送之后 git 仓库中就有你创建的分支了：**_

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766979664823-53f445df-e5bc-426c-85b9-ee3ea312ab0e.png" width="413.6" title="" crop="0,0,1,1" id="uc075016b" class="ne-image">

---

## 第五步：功能完成，发起合并（Pull Request/Merge Request）

1. 去公司的 **GitLab/Gitee/GitHub 网站**。
2. 找到你的分支，点击 `New Merge Request`。【github 上是 New Pull Request】
3. 选择：`源分支`（你的feature分支） -> `目标分支`（通常是 `master` 或 `develop`）。
4. 填写标题和描述，**指定同事给你评审（Review）**。
5. **等待评审通过后，由负责人或你自己点击合并（Merge）**。

---

## 第六步：处理合并冲突（一定会遇到，别慌）

**你推送时或合并时被告知有冲突。

1. **先更新代码**（第一步的 `Update`）。
2. 如果冲突弹出框出现：
+ **双击冲突文件**，IDEA 会打开一个**三窗格对比视图**。
+ **中间是结果**，用鼠标点击选择要保留的版本（左侧你的，右侧别人的），或直接手动编辑。
+ **解决完后，点击 **`Apply`。
3. **重新提交并推送**（`Commit and Push`）。

---

## 第七步：更新主分支，准备下一个任务

1. 回到 IDEA，**切换回 **`master` 分支。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766980289804-7d4cf4d9-1b95-477b-9a62-0777e9389aa0.png" width="282.4" title="" crop="0,0,1,1" id="u953ba2ff" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766980323640-39219f53-bfb9-4370-a966-5e79d17973a0.png" width="556" title="" crop="0,0,1,1" id="uc738bd10" class="ne-image">

2. 对 `master` 执行 **第一步的 **`Update`，拉取刚才合并的新代码。
3. 基于最新的 `master`，**回到第二步**，创建下一个功能分支。**注意哈：以上说的更新是更新主分支哈。**+**第一步：手动切换到主分支上。**+**第二步：**`**Update Project**`**更新主分支。**+**第三步：将最新的主分支合并到当前工作分支。以上三步联合起来就完成了代码更新。

---

## 黄金法则（公司生存指南）

1. **永远在功能分支开发，禁止直接在主分支（master/main）上写代码。**
2. **每天早上的第一件事：更新代码（Pull）。先更新 master，将 master 合并到自己的工作分支上，基于自己的工作分支继续开发。**
3. **推送前的最后一件事：再次更新代码（Pull），解决可能的新冲突。**
4. **提交信息要像小标题一样清晰，禁用“修复bug”、“更新”这种废话。**
5. **遇到冲突不要怕，这是常态，冷静对比，必要时找同事一起看。**
6. **合并（Merge Request）不是结束，必须等同事评审通过。**
7. **IDEA的右键菜单很强大：**`Git -> Rollback`**（回滚更改）、**`Show History`**（查看历史）、**`Compare with Branch`**（对比分支）。**
