# MSYS2 使用指南

## 安装 MSYS2

1. 下载安装程序：[https://www.msys2.org/](https://www.msys2.org/)
2. 运行安装程序，使用默认安装路径
3. 安装完成后，UCRT64 终端会自动启动

## 基本系统操作

```
# 更新包数据库和系统
pacman -Syu

# 搜索软件包
pacman -Ss 包名

# 安装软件包
pacman -S 包名

# 删除软件包
pacman -R 包名

# 列出已安装的包
pacman -Q
```

## 开发环境配置

```
# 安装完整的C/C++工具链
pacman -S mingw-w64-ucrt-x86_64-toolchain

# 或单独安装组件
pacman -S mingw-w64-ucrt-x86_64-gcc
pacman -S mingw-w64-ucrt-x86_64-g++
pacman -S mingw-w64-ucrt-x86_64-make
pacman -S mingw-w64-ucrt-x86_64-gdb
```

## 常用工具安装

```
# 文本编辑器
pacman -S vim
pacman -S nano

# 版本控制
pacman -S git
pacman -S subversion

# 构建工具
pacman -S cmake
pacman -S meson
pacman -S autoconf automake

# 压缩工具
pacman -S tar
pacman -S zip unzip
```

## 编程语言环境

```
# Python
pacman -S python

# Node.js
pacman -S nodejs

# Rust
pacman -S rust

# Go
pacman -S go
```

## 库和头文件配置

```
# 查找库文件
pacman -Ss 库名

# 安装开发库（以 openssl 为例）
pacman -S mingw-w64-ucrt-x86_64-openssl

# 查看头文件位置
pacman -Ql 库名 | grep include
```

## 编译C代码示例

```
# 简单编译
gcc -o program program.c

# 指定优化级别
gcc -O2 -o program program.c

# 包含调试信息
gcc -g -o program program.c

# 多文件编译
gcc -o program main.c util.c helper.c

# 指定库路径
gcc -I/path/to/include -L/path/to/lib -o program program.c -llibname
```

如何把库的位置添加到配置文件

```bash
# ❌ 错误：会覆盖现有值
export C_INCLUDE_PATH="/d/program/asn1c/skeletons"

# ✅ 正确：添加新路径到前面
export C_INCLUDE_PATH="/d/program/asn1c/skeletons:$C_INCLUDE_PATH"

# ✅ 正确：添加新路径到后面
export C_INCLUDE_PATH="$C_INCLUDE_PATH:/d/program/asn1c/skeletons"
```

## 环境变量配置

```
# 查看当前环境变量
printenv

# 设置包含路径
export C_INCLUDE_PATH=/path/to/include:$C_INCLUDE_PATH
export CPLUS_INCLUDE_PATH=/path/to/include:$CPLUS_INCLUDE_PATH

# 设置库路径
export LIBRARY_PATH=/path/to/lib:$LIBRARY_PATH
export LD_LIBRARY_PATH=/path/to/lib:$LD_LIBRARY_PATH

# 添加到 ~/.bashrc 永久生效
echo 'export PATH=/path/to/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

## Windows 与 MSYS2 路径映射

|Windows 路径|MSYS2 路径|
|---|---|
|C:\Users\用户名|/c/Users/用户名|
|D:\data|/d/data|
|C:\Program Files|/c/Program Files|

## 启动不同的 MSYS2 环境

```
# 启动 UCRT64 环境
msys2_shell.cmd -ucrt64

# 启动 MINGW64 环境
msys2_shell.cmd -mingw64

# 启动 MSYS2 环境
msys2_shell.cmd -msys2
```

## 常用快捷命令

```
# 查看磁盘空间
df -h

# 查看内存使用
free -h

# 查找文件
find . -name "*.c"

# 查看进程
ps aux

# 网络工具
curl https://example.com
wget https://example.com/file.zip
```

## 故障排除

```
# 检查编译器版本
gcc --version
g++ --version
make --version

# 检查路径
which gcc
which make

# 清理 pacman 缓存
pacman -Scc
```