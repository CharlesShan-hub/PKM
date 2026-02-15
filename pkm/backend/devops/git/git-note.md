# Git

## Note

* 配置命令——git config

```bash
# 列出所有的全局设置
git config --list

# 用户邮箱
git config --user.name "Your Name"
git config --user.email "Your Email"
```

* 配置文件在哪里：不管是 mac 还是 linux，都是 home/XXX 下的 `.gitconfig`
* clash 对 git 的影响\[2]：`git config --global http.proxy 127.0.0.1:(vpn代理端口号）`，clash的端口号是 7890

## Reference

\[1] git 教程：[https://git-scm.com/docs/git-config](https://git-scm.com/docs/git-config
\[2] [https://blog.csdn.net/qq\_45934285/article/details/130559069](https://blog.csdn.net/qq\_45934285/article/details/130559069)
