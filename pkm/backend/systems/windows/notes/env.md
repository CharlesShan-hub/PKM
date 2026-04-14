# Windows环境配置踩坑指南

## 编译C代码

首先下载类unix子系统msys：<https://www.msys2.org/>

然后运行包更新和编译器链下载：

```bash
# 首先更新
pacman -Syu

# 然后安装工具链
pacman -S mingw-w64-ucrt-x86_64-toolchain
```