# 创建user分支

git branch user

```

可以从硬盘文件中查看分支：`.git\refs\heads`

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766971499676-9b5d1c0c-c139-4c56-b665-d31574cfb8dc.png" width="179.2" title="" crop="0,0,1,1" id="ua3bb919e" class="ne-image">

### 查看当前分支状态

```shell

git branch -v

```

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766971595334-f61d0b53-aaf7-4ac6-911d-1c2c5900594c.png" width="356.8" title="" crop="0,0,1,1" id="u73180d76" class="ne-image">

上图表示当前正在 master 分支上。

### 切换分支

```shell

git checkout user
git branch -v

```

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766971708381-a710c49c-6648-48f1-8733-d37d86cc1b0b.png" width="334.4" title="" crop="0,0,1,1" id="u2cd9bbed" class="ne-image">

### 创建分支的同时切换分支

```shell

git checkout -b order

```

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766971858926-eeb81773-4c5d-4d70-a835-644c10bb89ab.png" width="560" title="" crop="0,0,1,1" id="u3bf325b6" class="ne-image">

### 删除分支

```shell

git branch -d user

```

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766971875628-5cf1e48f-4b51-42a9-a29c-82d84d8e02c0.png" width="581.6" title="" crop="0,0,1,1" id="u662d2b7f" class="ne-image">

### 基于某个历史记录创建分支

```shell

git checkout -b <新分支名> <历史提交id>

