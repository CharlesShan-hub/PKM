# Linux 环境配置


```
硬件：Parallels Desktop 虚拟机，128G 硬盘
系统：Ubuntu（桌面版）
用途：主力开发环境（后端、系统编程、Rust、Java 等）
```

---

## 一、系统维护

常用命令

```bash
# 日常更新（每周一次）
sudo apt update && sudo apt upgrade -y

# 清理无用包（每月一次）
sudo apt autoremove -y
sudo apt autoclean

# 查看磁盘使用情况
df -h

# 查看内存使用
free -h

# 查看系统负载
htop  # 没装的话：sudo apt install htop
```

目录规划

```bash
# 建议的项目目录结构
~/projects/
├── work/          # 工作项目
├── personal/      # 个人项目
├── labs/          # 实验/学习代码
└── tools/         # 手动安装的工具

# 创建目录
mkdir -p ~/projects/{work,personal,labs,tools}
```

---

## 环境配置

* 包管理：(✅) apt, (❌) apt-get

```shell
# 更新系统
sudo apt update && sudo apt upgrade -y
# 其他详见系统维护
```

* 命令行：(✅) fish

```shell
# 安装
sudo apt install -y fish

# 验证
fish --version

# 配置默认
echo $SHELL # 查看当前 shell
which fish # 查看 fish 路径
which fish | sudo tee -a /etc/shells # 将 fish 添加到可用 shell 列表
chsh -s /usr/bin/fish # 切换默认 shell 为 fish
fish # 重新登录后生效，或直接启动

```

fish配置文件（`~/.config/fish/config.fish`）

```shell
if status is-interactive
  # Commands to run in interactive sessions can go here
  # fish
  set -g fish_greeting # 关闭默认的 fish 提示信息

  # System - platform
  if test (uname -m) = "arm64" || test (uname -m) = "aarch64"
    echo "⚙️  platform: linux ARM64"
  else
    echo "⚙️  platform: linux x86_64"
  end

  # System - proxy
  set -gx switch_proxy "on" # "on" or "off"
  if test $switch_proxy = "on"
    set -gx no_proxy "localhost,127.0.0.1,localaddress,.localdomain.com"
    set -gx http_proxy "http://127.0.0.1:7897"
    set -gx https_proxy $http_proxy
    set -gx all_proxy "socks5://127.0.0.1:7897"
    echo "✈️  proxy: $http_proxy"
  else
    echo "✈️  proxy: off"
  end

  # fnm
  set FNM_PATH "/home/parallels/.local/share/fnm"
  if [ -d "$FNM_PATH" ]
    set PATH "$FNM_PATH" $PATH
    fnm env | source
 end

  printf "🐢 "
  fnm env --use-on-cd | source
  set -gx nodev 22
  if test $nodev = 16
    fnm use 16.20.2
    set -e NODE_OPTIONS # node 16需要开这个
  end
  if test $nodev = 18
    fnm use 18.16.0
  end
  if test $nodev = 22
    fnm use 22.15.0
  end

  # docker
  if groups | grep -q docker
      echo "🐳 Docker permissions enabled"
  else
      echo "⚠️  Please re-login to enable Docker permissions (sudo usermod -aG docker parallels) && newgrp docker && sudo reboot"
  end
end
```

* c语言：(✅) gcc, (✅) cmake

```shell
sudo apt install -y gcc g++ cmake make
```

* java语言

```shell
# 下载 Corretto 的 GPG 公钥
wget -O - https://apt.corretto.aws/corretto.key | sudo gpg --dearmor -o /usr/share/keyrings/corretto-keyring.gpg
# 添加 Corretto 软件源
echo "deb [signed-by=/usr/share/keyrings/corretto-keyring.gpg] https://apt.corretto.aws stable main" | sudo tee /etc/apt/sources.list.d/corretto.list
# 安装 Java 21（日常开发主力）
sudo apt install -y java-21-amazon-corretto-jdk
# 安装 Java 8（照顾老项目，可选）
sudo apt install -y java-1.8.0-amazon-corretto-jdk
# 查看所有已安装的 Corretto
ls /usr/lib/jvm/ | grep corretto
# 列出系统中的java版本
sudo update-alternatives --config java # 然后按照内容选择 1 2 3这样
```

* Rust

```shell
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

* 编辑器 trae

```shell
sudo apt install ./TraeCN-linux-x64.deb
```

* Obsidian：下载 AppImage

```shell
sudo apt install appimagelauncher
```