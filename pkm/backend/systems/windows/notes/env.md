
# Windows开发环境整理

---

Scoop 统管工具链：
  包管理 → 版本管理 → 项目管理 → C → Java → Python
Docker 管服务：
  数据库 → node → redis

---

😋包管理器：（√）**scoop**，（x 淘汰）chocolatey，（x 包少，需要手动添加PATH）winget
```powershell
# 允许执行脚本（只对当前用户，安全）
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
# Scoop默认安装到D盘
mkdir D:\scoop -Force  # 创建目录
 [Environment]::SetEnvironmentVariable("SCOOP", "D:\scoop", "User")
 $env:SCOOP = "D:\scoop" # 本窗口立刻生效
# 装 Scoop
irm get.scoop.sh | iex
```

😋终端：（√ ）**powershell**，（x 淘汰）cmd，（x 需要linux子系统）fish

```powershell
scoop install windows-terminal pwsh # 最新版的 poweshell 而不是自带的
scoop install oh-my-posh
scoop bucket add nerd-fonts 
scoop install JetBrainsMono-NF
scoop install terminal-icons
# 打开你的配置文件
notepad $PROFILE
```

```txt
# ============ 编码设置 ============
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::InputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8
chcp 65001 | Out-Null

# ============ Oh My Posh 主题 ============
# 【重要】把下面的路径换成你电脑上真实的路径
oh-my-posh init pwsh --config "C:\Users\你的用户名\AppData\Local\Programs\oh-my-posh\themes\jandedobbeleer.omp.json" | Invoke-Expression

# ============ 文件图标 ============
Import-Module Terminal-Icons

# ============ PSReadLine 智能补全 ============
Import-Module PSReadLine
Set-PSReadLineOption -Colors @{ 
    Command = '#FF79C6'
    Parameter = '#50FA7B'
    String = '#F1FA8C'
}
Set-PSReadLineOption -PredictionSource History
Set-PSReadLineKeyHandler -Key Tab -Function MenuComplete
```

😋版本管理：（√ 个人使用）**git**，（√ 团队使用）**svn**
```powershell
scoop install git
```
svn使用TortoiseSVN客户端，自动安装svn命令。

😋项目管理：（√ 项目构建编排）**just**
```powershell
scoop install just
```

😋C 语言工具链：（√）**cmake**，（√）**gcc**，（√）**mingw32-make**
```powershell
scoop install cmake mingw # mingw 包自带 gcc + mingw32-make
```

😋Java 语言工具链：（√）**maven**，（x 暂时不用）gradle
```powershell
scoop install maven
scoop bucket add java # java需要加载扩展包
scoop install corretto8-jdk corretto21-jdk # 安装指定版本java

# 切换版本需要两步：scoop reset + 更新 JAVA_HOME（Maven 强制要求）
scoop reset corretto21-jdk  # 切到 Java 21（日常开发）
$env:JAVA_HOME = "$env:USERPROFILE\scoop\apps\corretto21-jdk\current"
[Environment]::SetEnvironmentVariable("JAVA_HOME", $env:JAVA_HOME, "User")

scoop reset corretto8-jdk   # 切到 Java 8（编译 CMS 项目）
$env:JAVA_HOME = "$env:USERPROFILE\scoop\apps\corretto8-jdk\current"
[Environment]::SetEnvironmentVariable("JAVA_HOME", $env:JAVA_HOME, "User")
```

😋 Rust工具
```powershell
scoop install rustup
rustup default stable
```

😋Python 语言工具链：（√）**pixi**，（x 淘汰）uv
```powershell
scoop install pixi      # main bucket 中的 pixi
#uv self uninstall      # 卸载 uv（原手动安装在 ~\.local\bin\）
```

😋前端工具链：（√）nvm + node + yarn
```powershell
scoop install nvm
nvm install 22.11.0 # LTS
nvm use 22.11.0
npm install --global yarn
```

😋dart工具链
```powershell
scoop install dart
scoop install flutter
```

😋数据库相关：（√）**mysql**，（√）**dameng**
* mysql版本管理使用docker
* dameng数据库需要安装驱动，目前没有版本管理
