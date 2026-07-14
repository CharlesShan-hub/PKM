# Mac 环境配置

Homebrew 统管工具链：
  包管理 → 版本管理 → 项目管理 → C → Java → Python
Docker 管服务：
  数据库 → redis → 其他服务

* 前置依赖：(✅) Xcode Command Line Tools, (✅) brew

Xcode
```shell
# 安装
xcode-select --install
# 验证安装
xcode-select -p && clang --version
```

brew
```shell
# 安装 Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# 验证安装
brew --version
```

* 命令行：(❌) zsh, (❌)bash, (✅)fish

```shell
# 安装 fish
brew install fish
# 设置 fish 为默认 shell
echo /opt/homebrew/bin/fish | sudo tee -a /etc/shells
chsh -s /opt/homebrew/bin/fish
# 验证安装
fish --version
echo $SHELL
```

* 版本管理：(✅)git, (❌)svn

```shell
# 安装 Git（Xcode CLI Tools 已自带，但 Homebrew 版本更新）
brew install git
# 验证安装
git --version
```

* 项目管理：(✅)just

```shell
# 安装 just
brew install just
# 验证安装
just --version
```

* c语言工具链：(✅) cmake, (❌)gcc, (✅) clang: xcode默认已经安装

```shell
# 安装 CMake
brew install cmake

# Clang 已通过 Xcode CLI Tools 安装，无需额外安装

# 验证安装
cmake --version
clang --version
```

* java工具链: (✅)maven, (✅)jenv

```shell
# 安装 Maven
brew install maven

# 安装多版本 JDK
brew install openjdk@17
brew install openjdk@21

# 安装 jEnv（Java 版本管理）
brew install jenv

# 验证安装
mvn --version
java --version
```

```shell
# jenv配置
# 安装 jEnv
brew install jenv

# 配置 jEnv（写入 ~/.config/fish/config.fish）
echo 'set -gx PATH $HOME/.jenv/bin $PATH' >> ~/.config/fish/config.fish
echo 'jenv init - | source' >> ~/.config/fish/config.fish

# 重新加载配置
source ~/.config/fish/config.fish

# 添加 JDK 到 jEnv（先查看实际路径）
/usr/libexec/java_home -V

# 然后根据实际路径添加，通常是这样：
jenv add /Library/Java/JavaVirtualMachines/amazon-corretto-8.jdk/Contents/Home/
jenv add /Library/Java/JavaVirtualMachines/amazon-corretto-21.jdk/Contents/Home/

# 查看所有版本
jenv versions

# 设置全局默认版本
jenv global 21

# 验证
java -version
echo $JAVA_HOME
```
