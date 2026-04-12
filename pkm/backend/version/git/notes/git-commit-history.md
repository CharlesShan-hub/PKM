# 你提交代码后，别人查看历史时会看到：

Commit: 修复了登录bug
Author: zhangsan <zhangsan@email.com>
Date:   2023-10-01

```

**不填的后果**：Git 会拒绝你提交代码，提示“请设置 user.username 和 user.email”。当我们填写了名字和邮箱地址之后，跳转到这个页面：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766907932602-7a6fba4a-9d13-41f6-8ba1-c50d8c412093.png" width="952.8" title="" crop="0,0,1,1" id="u64f405ca" class="ne-image">

1. `**Clone a repository..**`**： 下载**别人（或你自己）在 GitHub 上已有的项目到本地电脑。**
2. `**Create a New Repository..**`**： 在本地电脑**新建一个空项目文件夹**，并设置为 Git 仓库（可随后上传到 GitHub）。**
3. `**Add an Existing Repository..**`**： 将本地电脑上**已有项目文件夹**（比如你之前写的代码）纳入 Git 管理/关联到 GitHub。总结这三个操作：本质上都是在本地电脑上创建 Git 仓库。一个是从外网下载的，一个是创建新的，一个是导入本地存在的。**

---

## **GitHub Desktop 创建仓库**

### 创建仓库

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766908809162-14e8368c-9c01-48ed-9f00-0c0cc45ada1a.png" width="448" title="" crop="0,0,1,1" id="ufe177159" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766908942789-89a209e5-1037-4237-b6b6-67ecf2ce7ebf.png" width="391.2" title="" crop="0,0,1,1" id="u1b2e4b63" class="ne-image">

### 切换仓库

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766909018022-b8d289c2-834d-405d-92b9-dead6faa24c9.png" width="335.2" title="" crop="0,0,1,1" id="u0f8b837e" class="ne-image">

### 浏览本地仓库

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766909065469-d81f9796-be5e-4638-84a6-3b63ef6f5f4c.png" width="951.2" title="" crop="0,0,1,1" id="u7eb45f97" class="ne-image">

**仓库中的**`**.git**`**目录中的东西不要动：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766909168074-12bb2007-f318-4d3d-87d7-21a57041e453.png" width="217.6" title="" crop="0,0,1,1" id="uc09a9db8" class="ne-image">

### 删除仓库

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766909217596-68b681be-ce74-48b1-a0f6-e23785ce114e.png" width="272" title="" crop="0,0,1,1" id="u2723c80f" class="ne-image">

**仅从 GitHub Desktop**左侧仓库列表**中删除，**不删除电脑里的实际文件**。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766909244523-fcba9ed4-b746-4f3e-911a-45b2c93e116e.png" width="437.6" title="" crop="0,0,1,1" id="u67b12cdf" class="ne-image">

**不仅从列表移除，还会把整个项目文件夹扔进电脑回收站**（可清空彻底删除）。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766909383714-fe64da82-d1ca-469e-9678-4c605e60aefd.png" width="438.4" title="" crop="0,0,1,1" id="ud8350c62" class="ne-image">

### 拖拽仓库

从列表中移除之后，将硬盘上的仓库目录直接拖拽到 GitHub Desktop 也是可以的：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766909469195-1c00c7d3-7987-463d-87d8-3b0139720b09.png" width="750.4" title="" crop="0,0,1,1" id="u41509b04" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766909547525-3f43becb-ec60-43fc-9236-08bbb1e7bfd7.png" width="583.2" title="" crop="0,0,1,1" id="u177a38d9" class="ne-image">

---

## Git 仓库中文件的操作

### 将文件添加到仓库

直接在仓库中创建的文件，并没有添加到 git 仓库中（**等于把物品放到了仓库，但是没有登记到物品清单上**）

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766910476647-87480889-57ca-4b58-b76d-44df37177e44.png" width="290.4" title="" crop="0,0,1,1" id="uc4777b2a" class="ne-image">

**但由于这个文件是创建在仓库目录下的，可以被 Git 客户端工具自动发现。Git 客户端工具发现新物品但没有登记到清单，会有提示，如下图。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766910858092-74f21c72-1bee-4d26-8988-e3243ac753f9.png" width="339.2" title="" crop="0,0,1,1" id="u33dbd8f3" class="ne-image">

**注意：在仓库外面创建的文件，Git 客户端工具是不会发现的。通过下面的方式可以将文件添加到 git 仓库：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766910707895-192ca279-0f37-4679-bc83-f0c5f798284d.png" width="292" title="" crop="0,0,1,1" id="u142beb5b" class="ne-image">

### 将文件添加到仓库的原理

文件添加到仓库有**三个关键角色（状态）:**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766911672804-89dc05bc-28ca-4fe5-9e1d-05204b1421ec.png" width="741.6" title="" crop="0,0,1,1" id="ue718e8fa" class="ne-image">

**工作区：**工作区的位置是**你的仓库文件夹里**。在工作区**编辑**文件**之后**，通过**`**git add**`**命令将其放到**暂存区**。暂存区：**又叫做 **Git 临时缓存区。在 GitHub Desktop 客户端软件中，文件左侧复选框打上对钩则表示执行**`**git add**`**命令，此时文件就在暂存区中。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766911979148-fa7ce4db-589a-462a-a28c-9f7743508e37.png" width="284" title="" crop="0,0,1,1" id="uf5e4811f" class="ne-image">

**Git 仓库：**`**.git**`**隐藏文件夹里的数据库。对暂存区的文件执行**`**git commit**`**命令，文件将被永久存储在 Git 仓库中。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766912158995-a6f828b3-d94e-4814-ace0-af7f46fbbc94.png" width="253.6" title="" crop="0,0,1,1" id="uc68cfcbe" class="ne-image">

**当提交后，文件将被永久存储到 Git 仓库当中，并为该**提交操作**生成一个独一无二的哈希值：**也可以叫做提交 ID。或者也可以叫做**版本号**。在下图位置可以看到它的版本号，版本号采用 40 个长度的十六进制表示。**另外也可以看到操作的历史记录**：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766912505497-60662e24-1d85-4503-bfbb-3faba611b303.png" width="648.8" title="" crop="0,0,1,1" id="udb21119a" class="ne-image">

**这个版本号在 **`**.git**`**文件夹中也可以找到：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766912620772-324e3321-a175-4dc1-8c69-ff966f636471.png" width="305.6" title="" crop="0,0,1,1" id="u3fc135b8" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766912582013-4c2acc2e-ef9c-41d9-be5c-502c831363fd.png" width="664.8" title="" crop="0,0,1,1" id="u5d7ad52f" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766912599849-60f71e6c-9524-4f0f-a148-99db51ba47c9.png" width="342.4" title="" crop="0,0,1,1" id="u62b42da5" class="ne-image">

### Git 的存储原理**具体原理：**1.**每次提交**：Git 会为**每个文件**生成一个哈希值（**基于文件内容**）**
2.**检查去重**：如果这个哈希值在**`**.git/objects**`**中**已存在**，就**不再存储新的副本**3.**如果仓库中没有这个哈希值**：生成一个新文件，并且以新的哈希值命名。假设你有**`**User.java**`**文件：**|**提交**|**文件内容**|**Git 操作**|
| --- | --- | --- |
|**第一次提交**| `**public class User { }**` | **存储内容，哈希为**`**abc123**` |
|**第二次提交**（未修改文件）** | `**public class User { }**` |**发现**`**abc123**`**已存在，不存储**|
|**第三次提交**（修改了文件）** | `**public class User { private String name; }**` | **存储新内容，哈希为**`**def456**` |

**注意：新文件中保存了当下文件的全部内容，而不仅仅是存储修改那一部分。（不用担心空间问题，git 底层会自动压缩。）**

### 文件的修改

**修改工作区中的文件：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766913705455-ecc7f800-28a4-4e79-a0ba-e28478d9cfe7.png" width="296.8" title="" crop="0,0,1,1" id="u067df7e4" class="ne-image">

**观察 GitHub Desktop 工具：复选框自动选中，已经将文件加入到暂存区了。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766913785889-8ca8b77f-5dd3-40f7-8f61-58e253857087.png" width="492" title="" crop="0,0,1,1" id="u278d8ae8" class="ne-image">

**然后再通过提交按钮，将其提交到 git 仓库：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766913851328-a55e9f01-a49a-48d7-8a8f-867166ac5e03.png" width="291.2" title="" crop="0,0,1,1" id="ud72b4513" class="ne-image">

**可以再次查看操作历史记录，查看生成了新的提交 ID：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766913896184-abd5b08d-18a1-4e79-afdc-b8abd97b0ab6.png" width="699.2" title="" crop="0,0,1,1" id="u2ea29de1" class="ne-image">

**可以再次通过这个提交 ID，从 **`**.git**`**仓库中看到一个新的文件：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766914050804-958f95d6-dac7-49cd-93ce-c590bcaf2bb0.png" width="205.6" title="" crop="0,0,1,1" id="u9a8e6d95" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766914031691-f75182ca-0524-4341-bf34-6d7cee7535a3.png" width="640" title="" crop="0,0,1,1" id="ue4f36358" class="ne-image">

### 文件的删除

**我们将 **`**a.txt**`**文件删除，观察客户端工具，客户端工具又将复选框自动选中了，等于客户端工具又执行了 **`**git add**`**，将删除操作放到了暂存区：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766914292292-b1c510de-d55a-482b-aab2-a340ffccf566.png" width="468" title="" crop="0,0,1,1" id="ued62c901" class="ne-image">

**虽然是删除文件，但这个删除的动作也要提交给 git 仓库，点击提交按钮：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766914361522-32651920-115c-4ba7-8a37-c3978686e06c.png" width="274.4" title="" crop="0,0,1,1" id="ucb19f65f" class="ne-image">

**查看操作记录：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766914424786-f83eac56-dd03-4be2-a793-d02c133d7254.png" width="565.6" title="" crop="0,0,1,1" id="u3986d090" class="ne-image">

**删除动作也会在 git 仓库中生成一个文件，如下：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766914886502-17adbc5d-2f7b-4d02-b89c-ac6aa4e1ce12.png" width="305.6" title="" crop="0,0,1,1" id="u6e690241" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766914914067-e30e2d86-d495-4ab5-81d9-3b4a61137095.png" width="679.2" title="" crop="0,0,1,1" id="uc7bf7c20" class="ne-image">

**这个文件中存储了：**“删除了 a.txt”这个动作的元数据**```plain

tree 新目录树哈希
parent 旧提交ID
author ...

删除了a.txt

```**新目录树对象**：生成一个新的目录树对象，这个树里**不再包含 a.txt 的引用**---

## **Git 分支的理解**

软件版本控制工具都有分支的概念，不是 git 特有的。SVN、CVS 等都有。

### 没有分支的情况（就像一条单行车道）

想象一下，实际开发中是多个人开发同一个项目。假设没有分支，只有一个主仓库。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766916901764-559f74d5-327b-44a3-bc68-e7cbbf8cfb94.png" width="745.6" title="" crop="0,0,1,1" id="ued6fc7a6" class="ne-image">**问题出现了：**1.**必须排队**：你正在开发“个人中心”，没做完就不能提交，因为你提交到主仓库上的话，等于提交了半成品，别的同事以为能用呢，结果一用就崩，为了避免，大家只能排队。（**所谓的排队是：你别动！等我做完的！**）**
2.**无法隔离风险**：小明的“支付功能”有bug提交了，大家共享一个仓库，你拉下来的代码很可能导致你的“个人中心”也跟着崩了。**
3.**无法并行实验**：你想试试用新技术重写登录，但一旦开始，所有人都得用你这个实验版，因为共享同一个仓库。这就是没有分支的情况——所有人挤在一条时间线上。

### **有分支的情况（就像有了“平行宇宙”）Git 允许你创建**分支**，本质上是**从某个时间点复制一条独立的时间线**。分支本质上其实将主仓库复制一份，你在复制品上随便折腾。等你折腾完了，测试功能没问题，将你折腾的成果最终再合并到主仓库中。利用分支来开发新的功能，这是最常用的。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766917635674-e21ea094-42b8-428f-8b92-f77c13520ef6.png" width="1382.4" title="" crop="0,0,1,1" id="ua4b6f1ae" class="ne-image">

+ **你和小明**同时从主分支复制了一条自己的时间线**。**
+ **你在你的分支上随便折腾，不影响小明，也不影响主分支。**
+ **你们都完成后，**分别**把各自稳定的代码合并回主分支。**

### **用现实比喻理解分支想象你们在合作写一本小说：**

+ **没有分支**：所有人围着一份手稿改，你改一页，我改一页，经常写乱套。**
+ **有分支**：**
    1. **主分支是**正式出版的小说**。**
    2. **你想写一个“外传”，就**复印一份**手稿，在复印件上随便写（这就是创建分支）。**
    3. **写完后，如果大家觉得好，就把“外传”章节**抄进**正式手稿里（这就是合并分支）。**
    4. **另一个人同时也可以复印一份去写“前传”。分支就是复印稿，让你可以安全地并行创作。**

### **分支对Java开发者的好处**

1. `**main**`**分支**：永远放着**稳定、可运行的代码**，随时能打包发布。**
2. `**feat/xxx**`**分支**：开发新功能（如**`**feat/user-login**`**），做完合并。**
3. `**fix/xxx**`**分支**：修复Bug。修复 bug 的时候可以复制一个分支，在分支上修复。修复完再合并回去。**
4. `**release/xxx**`**分支**：准备发布新版本。你每天的工作就是：**

1. **从**`**main**`**拉一个新分支**`**feat/add-order**`**。**
2. **在这个分支上安心写3天订单功能。**
3. **写完，测试通过，合并回**`**main**`**。**
4. **删除**`**feat/add-order**`**分支。分支就是你的“安全沙盒”，玩坏了也不影响别人。**

---

## **分支功能演示**

### 创建仓库（自带主分支）

**创建主库 **`**repo-2**`**：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766918577866-0de53b55-574b-4774-9a3e-79cfa9e61ac7.png" width="357.6" title="" crop="0,0,1,1" id="u57973f87" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766918615930-2e5bee49-8819-405b-9697-fc155c9c6064.png" width="392.8" title="" crop="0,0,1,1" id="u79600df2" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766918729571-e98ba087-14c7-4784-a34b-11d9ec91f84b.png" width="664" title="" crop="0,0,1,1" id="u92fca812" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766918768118-2806ecc4-add4-445e-9f45-6935e5ac424a.png" width="268.8" title="" crop="0,0,1,1" id="u96b23c65" class="ne-image">

**注意：创建仓库时，每个新建的仓库默认自带一个主分支。**

### 创建 user 分支

项目经理为开发**用户模块**的同事创建 user 分支：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766918901962-b34e6e8e-c2f2-49d5-b867-4ab52c642c71.png" width="354.4" title="" crop="0,0,1,1" id="ucc125c1f" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766918929984-143ccb6d-483e-46ca-9160-1c9daebab669.png" width="391.2" title="" crop="0,0,1,1" id="u2c21fd73" class="ne-image">

创建完 user 分支被自动选中：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766918957800-d95cab34-313b-4101-9c39-4887b9f4d410.png" width="268.8" title="" crop="0,0,1,1" id="ufbe48c20" class="ne-image">

### 在 user 分支上开发并提交

**打开分支对应的位置：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766919022356-edfbfd57-7060-4d9a-b842-daed15e6c000.png" width="675.2" title="" crop="0,0,1,1" id="u1413bc7b" class="ne-image">

**在该分支上开发：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766919116644-72086099-37b0-49f7-82c7-0e37078803d8.png" width="488" title="" crop="0,0,1,1" id="u31170fe0" class="ne-image">

**提交分支：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766919186680-b03f1645-5a96-429e-9b61-ce0824ec2715.png" width="572.8" title="" crop="0,0,1,1" id="uc53960c0" class="ne-image">

**到这里user 分支就完成了开发，并将分支中的开发成果提交到分支仓库中了。**你可以看一下：主分支中没有，user 分支中有。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766919344079-5fdcd1b6-c249-4582-bfee-071a09f3f1ec.png" width="357.6" title="" crop="0,0,1,1" id="ub15351e3" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766919365334-dcfa9424-3593-42a7-8447-19518592f07a.png" width="298.4" title="" crop="0,0,1,1" id="uc44001b9" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766919378798-260183e4-8bb9-4c5d-9247-8a07e8875c82.png" width="627.2" title="" crop="0,0,1,1" id="ue611ba12" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766919415688-7838d442-5734-4bfa-a77d-df76db7b7ce0.png" width="364.8" title="" crop="0,0,1,1" id="u17b9766a" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766919424972-49b0ede7-31a2-46de-aa83-2fe89974862d.png" width="185.6" title="" crop="0,0,1,1" id="ub1e04d32" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766919440117-c9e5fb6d-7857-4e85-9be5-71e03c2e5f22.png" width="520.8" title="" crop="0,0,1,1" id="uea948cb3" class="ne-image">

### 创建 order 分支

和创建 user 分支方式相同。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766919891975-3e456797-e48c-4939-9009-f65c424dbb7f.png" width="396" title="" crop="0,0,1,1" id="u69316b5e" class="ne-image">

### 在 order 分支上开发并提交

和 user 分支上的开发一样，按照之前的步骤操作一遍。

### user 分支合并到主分支

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766920037096-906885b8-b031-4450-becb-ed44ebecd392.png" width="377.6" title="" crop="0,0,1,1" id="ufab678a7" class="ne-image">

**通过以上方式，可以选择一个分支合并到主分支：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766920104901-c49ea602-c669-482c-af5b-e9f5a406f9d0.png" width="445.6" title="" crop="0,0,1,1" id="uf915dd1c" class="ne-image">

**合并之后，去主分支上看看有没有 user 分支的数据：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766920148022-d3502ce2-e49d-48ab-b444-f7b8db5247c4.png" width="210.4" title="" crop="0,0,1,1" id="uae6cc7e3" class="ne-image">

### order 分支合并到主分支

合并方式和 user 分支的合并方式相同。

**合并之后，可以看到主分支的数据如下：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766920254817-fc724050-3c87-4271-b5b0-d9e99f8750bb.png" width="226.4" title="" crop="0,0,1,1" id="ufabf49d7" class="ne-image">

### 合并冲突的解决

**第一步：**在 user 分支上创建 `common.txt`文件，编写内容 `user`并提交。

**第二步：**在 order 分支上创建 `common.txt`文件，编写内容 `order`并提交。

**第三步：**将 user 分支合并到主分支。

**第四步：**将 order 分支合并到主分支：此时就会出现文件冲突问题，如下图：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766920687100-16525974-e5a1-4cde-baea-6cc75f0dec3a.png" width="442.4" title="" crop="0,0,1,1" id="u069472b6" class="ne-image">

**第五步：解决冲突，git 这个时候是无法自动处理的，需要人为介入**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766920736411-e76afa59-d418-46b7-b8cd-2202cc8e61ce.png" width="492.8" title="" crop="0,0,1,1" id="u30fe4446" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766920769982-eb5dd030-0a8a-4485-b5d3-d48cda910cc4.png" width="485.6" title="" crop="0,0,1,1" id="u11bb57a5" class="ne-image">

**编辑器显示如下：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766920797215-d9368993-e5b8-4e23-90e2-166a054363a9.png" width="275.2" title="" crop="0,0,1,1" id="ud3d1f1cd" class="ne-image">

**内容怎么修改？你说了算：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766920844927-9161b041-af21-4c7f-8ba7-0a80575b9b56.png" width="253.6" title="" crop="0,0,1,1" id="u07bfa381" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766920870224-c98af3a1-4312-4353-a4d3-8713a430e331.png" width="487.2" title="" crop="0,0,1,1" id="ub1a59de8" class="ne-image">

**合并后，查看主分支中文件的内容，如下：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766920904447-168c0b42-786f-4f13-bf8b-489d7fe77c1e.png" width="251.2" title="" crop="0,0,1,1" id="ub0fd5fae" class="ne-image">

---

## 标签功能

在提交代码的时候有注释，在合并的时候没有注释，怎么办？我们可以给每一个操作历史记录打标签，这样就会更加清晰。

**第一步：打开历史记录**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766921112663-3732bf56-0748-4541-a777-954b584ba269.png" width="434.4" title="" crop="0,0,1,1" id="u7e7f59a7" class="ne-image">

**第二步：在历史记录上打标签**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766921155379-e9e80b37-1cad-4907-8dc8-dafae49d86f0.png" width="392" title="" crop="0,0,1,1" id="ufad3ad35" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766921170662-8593d4e8-9596-459f-9e2f-ec221c7f89dd.png" width="391.2" title="" crop="0,0,1,1" id="ud9aaeb04" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766921183861-8e2226dd-3cd1-4f77-b946-2aff094258c8.png" width="258.4" title="" crop="0,0,1,1" id="u5ae919b4" class="ne-image">

**第三步：标签也可以删除**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766921212820-cc974d03-f9ac-4c2e-bc5d-45d0e58766ee.png" width="396" title="" crop="0,0,1,1" id="u3e46bd4e" class="ne-image">

---

## 操作远程仓库 GitHub

### 本地仓库与远程仓库的区别

**Git的本地仓库和远程仓库是代码协作中两个核心但角色不同的概念。简单来说，**本地仓库是你个人计算机上的“私人工作区”，而远程仓库是团队成员共享的“中央服务器”**<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766923397785-85745b69-b51f-47db-b95f-b5e2c4e4c746.png" width="326.20001220703125" title="" crop="0,0,1,1" id="ue777f6ec" class="ne-image">

**列表格对比一下：**

|**特性**|**本地仓库 (Local Repository)**|**远程仓库 (Remote Repository)**|
| --- | --- | --- |
|**位置**| **位于**你的个人电脑**上，**`**.git**`**隐藏文件夹。** | **位于**独立的服务器或云端**，如GitHub、GitLab、Gitee、公司自建服务器等。** |
|**核心用途**|**个人工作区**：让你可以离线工作、频繁提交、创建分支进行实验，而不会影响他人。** |**协作中心与备份**：团队共享的代码，用于集成所有人的工作、备份历史记录。** |
|**访问与权限**| **仅限你自己**完全控制**，所有操作（增删改提交历史）都瞬间完成。** |**团队共享**，有权限控制。**`**push**`**（推送）操作需要网络和相应权限。** |
|**网络需求**|**无需网络**，绝大多数操作（提交、分支切换、查看历史）都可离线进行。** |**依赖网络**，**`**push**`**、**`**pull**`**、**`**fetch**`**、**`**clone**`**等与远程交互的操作都需要联网。** |
|**内容构成**| **包含项目的**完整历史记录、所有分支、标签**以及Git的所有对象数据库。** | **本质上是本地仓库的一个**镜像或快照**，通常内容与某个本地仓库同步。** |**本地仓库和远程仓库的这种分离与协作模式，正是Git“分布式”版本控制系统最核心、最生动的体现**。当你执行**`**git clone**`**时，你得到的是**整个项目历史、所有分支和标签的完整副本**。这意味着：**

+**你可以离线工作**：所有提交、查看历史、创建合并分支等操作都瞬间完成，无需连接服务器。**
+**你拥有全部历史**：可以自由探索任何时期的代码状态，不受服务器是否在线的限制。因此，即使中央服务器坏掉了，也没有关系，代码不会丢。**### **GitHub 创建远程仓库**

公司可以自建中央仓库，我们也可以使用云端的中央仓库，现代的开发一般都是使用云端的，例如 GitHub。

**第一步：注册并登录 GitHub。这个自己操作即可。（如果比较慢，可以考虑梯子。）第二步：创建远程仓库**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766924137327-ae53f649-5632-43db-8411-dd30ed99697f.png" width="1506.4" title="" crop="0,0,1,1" id="u2d9da6f3" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766924222948-24a64faf-db98-4be6-bb94-151d82ff971c.png" width="762.4" title="" crop="0,0,1,1" id="u9961548b" class="ne-image">**public对所有人可见，private仅自己或授权者可见。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766924265224-8fa12634-2f3a-4f24-9716-748dd633f9e4.png" width="1519.2" title="" crop="0,0,1,1" id="ud11f7066" class="ne-image">

### 创建文件

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766924499902-c438697d-2cb1-47ef-96c7-78b54cee9bd5.png" width="1369.6" title="" crop="0,0,1,1" id="u85cbeb46" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766924534238-463b0212-6803-4416-8c24-f3f30e4cfee6.png" width="530.4" title="" crop="0,0,1,1" id="u0f8b22b3" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766924608875-1ed5438b-3991-4635-8493-5b32d64ac31c.png" width="1514.4" title="" crop="0,0,1,1" id="u247bc131" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766924688064-139f0734-7059-48fd-bd10-f90ecf6da989.png" width="471.2" title="" crop="0,0,1,1" id="uc1396b19" class="ne-image">

**然后，你可以看到你创建的文件：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766924744827-c2511c89-eee6-47f3-8edf-7c7296fe6fcf.png" width="788.8" title="" crop="0,0,1,1" id="u20be3f67" class="ne-image">

### 修改文件

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766924827748-566e8584-5a54-419c-b167-27911e9a1a8f.png" width="360" title="" crop="0,0,1,1" id="u0a8317aa" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766924846537-e4b73e40-683e-4f41-b48f-f854b4a5507b.png" width="1491.2" title="" crop="0,0,1,1" id="u7aedda0d" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766924875968-b9b6df9a-336f-41fb-9f3a-44fc261f14b5.png" width="1507.2" title="" crop="0,0,1,1" id="u057a736f" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766924893552-992b5a71-4994-434b-bb2b-0a969f865f46.png" width="468.8" title="" crop="0,0,1,1" id="ufc3a404b" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766924938622-adaf2c69-dab5-428e-9b13-8549a644b0aa.png" width="1516" title="" crop="0,0,1,1" id="u6c0ef658" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766925000622-903b3750-16a6-4b20-975a-ccf360dc3fbf.png" width="1354.4" title="" crop="0,0,1,1" id="ub702b2ac" class="ne-image">

### 创建分支

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766925137390-af99bd37-d12c-4d75-be50-ee29e1c95b9b.png" width="521.6" title="" crop="0,0,1,1" id="ued7ba2c4" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766925156089-9496a588-3975-450b-964b-5632c5ba36c0.png" width="1421.6" title="" crop="0,0,1,1" id="u5782abda" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766925167871-9b410c82-960f-4e90-8b44-b3543e103ba7.png" width="468" title="" crop="0,0,1,1" id="ue04531ee" class="ne-image">

**切换分支：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766925215848-ec39948d-76da-4b56-a1ba-8b801707d72c.png" width="528" title="" crop="0,0,1,1" id="ud1725988" class="ne-image">

### 删除仓库

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766925306149-89ed076b-bb49-4a9f-9876-47a23dd3a8df.png" width="1123.2" title="" crop="0,0,1,1" id="u745c9b5e" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766925332201-6be5acc7-106d-4466-a905-a22e38736b4c.png" width="823.2" title="" crop="0,0,1,1" id="u9def4208" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766925366715-d2cbd19d-bdf1-47f4-a3d9-afdf97e27a54.png" width="464" title="" crop="0,0,1,1" id="u8ce2fa92" class="ne-image">

### 从远程仓库下载代码

**第一步：**创建远程仓库，提供一个文件，随便向文件中写点内容。

**第二步：**打开 GitHub Desktop 工具，关联 GitHub 账号。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766925588296-f0ce54ac-7c5e-439d-8c9c-ea15b8328971.png" width="208.8" title="" crop="0,0,1,1" id="uc944dd76" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766925601460-cb9aebec-86cb-48de-be5c-5a3a1117895d.png" width="448" title="" crop="0,0,1,1" id="u98999f01" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766925611830-d62f8550-f248-4f36-b025-0909e0e63460.png" width="398.4" title="" crop="0,0,1,1" id="u4146e6de" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766925626574-89114c80-2983-436e-b923-500ba4f04e5a.png" width="390.4" title="" crop="0,0,1,1" id="u99274677" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766925661737-fe786adf-8718-4a4f-9b62-c4738d6a4f75.png" width="514.4" title="" crop="0,0,1,1" id="u11ef5879" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766925693335-b1586459-89a2-4901-b222-6db20c4e3ed2.png" width="576" title="" crop="0,0,1,1" id="ude1596db" class="ne-image">

**第三步：从远程仓库克隆项目到本地仓库**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766925878623-5d09ed3c-5f5c-451f-a759-768a9f93d031.png" width="205.6" title="" crop="0,0,1,1" id="u0fafd3bb" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766925950916-fa7a3590-0baf-4bb4-9a93-c2f4758456a4.png" width="488" title="" crop="0,0,1,1" id="qT6Bz" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766926021428-356f2987-04df-472a-9645-099589cda2e3.png" width="915.2" title="" crop="0,0,1,1" id="u57b2784f" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766926030473-229c3a17-599a-46a5-9c7e-887c1fd882ea.png" width="239.2" title="" crop="0,0,1,1" id="u0138306a" class="ne-image">

**第四步：在本地仓库中开发并提交到本地仓库。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766926070078-4f583dfa-c5c2-419e-9b1d-ef6fdc203521.png" width="489.6" title="" crop="0,0,1,1" id="u6c18166d" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766926095166-763768e8-db83-46f8-8f98-0dc412e5d150.png" width="359.2" title="" crop="0,0,1,1" id="u2cb7308b" class="ne-image">

**第五步：推送到远程仓库。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766926121230-fa1c7fa8-d9da-4ffe-85df-ac3ec1002dc5.png" width="957.6" title="" crop="0,0,1,1" id="u66adf0d8" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766926150326-5b23b40f-1f61-479c-881f-4b0028f15928.png" width="543.2" title="" crop="0,0,1,1" id="u7428274a" class="ne-image">

### 操作远程仓库 Gitee

国内的开发者也可以使用 Gitee 创建远程仓库，GitHub 国外的网站，有时比较慢。

**第一步：注册 Gitee 账号，并创建仓库，创建文件。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766926716639-689b7113-e312-4a08-a6d1-36b41f1b705d.png" width="752" title="" crop="0,0,1,1" id="u67760709" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766926777706-20488b59-cc9c-49a3-b9a8-4496e92ad480.png" width="780.8" title="" crop="0,0,1,1" id="ud13812df" class="ne-image">

**public对所有人可见，private仅自己或授权者可见。**第二步：将 Gitee 的仓库克隆到本地。**

先拿到 URL：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766927299762-dff44d0f-3811-4419-812a-98734d4fb736.png" width="699.2" title="" crop="0,0,1,1" id="uf2167c9d" class="ne-image">

打开客户端工具：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766927232990-ccc32cd0-ba28-420c-96e2-096ac54ef314.png" width="204.8" title="" crop="0,0,1,1" id="u0fa00666" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766927279268-f54d2d80-e76d-49da-a7b9-4f86e897382a.png" width="497.6" title="" crop="0,0,1,1" id="ubece2f91" class="ne-image">第三步：在本地修改，提交到本地仓库。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766927330008-2811413b-a78e-44eb-9057-cdb13acb0959.png" width="949.6" title="" crop="0,0,1,1" id="uc284fc1b" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766927350828-6bd0b080-3977-488f-8d46-53d491a93bac.png" width="558.4" title="" crop="0,0,1,1" id="uee12905d" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766927368300-40879608-ef22-48eb-9ce2-8061feea808e.png" width="459.2" title="" crop="0,0,1,1" id="ufbd2fb71" class="ne-image">



**第四步：推送到远程仓库。**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766927392216-2db88509-9c83-4fd7-a54c-3d3c4c76a3ce.png" width="949.6" title="" crop="0,0,1,1" id="uc6ca3641" class="ne-image">

**提示需要输入用户名和密码。此时输入 Gitee 的用户名和密码即可。**

---

## Readme 文件

**README文件就是项目的“产品说明书”或“使用手册”。README是别人打开你项目时看到的第一个页面，告诉人家“这是啥、怎么用、谁负责”。具体作用（四个核心）：**

### 项目名片（这是啥？）

```plain
