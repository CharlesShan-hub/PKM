# clash

## Note

1. clash可执行文件
   1. 下载 clash压缩包：[clash github link](https://github.com/Dreamacro/clash/releases/download/v1.14.0/clash-linux-amd64-v1.14.0.gz)
   2. 把解压的文件重命名为 clash
   3. 为 clash 可执行文件添加权限：`chmod u+x clash`
   4. 把加完权限的 clash 可执行文件放到`/usr/local/bin`
2. 文件配置
   1. 新建文件夹`/etc/clash`
   2. 命令行执行`clash`，（就是执行刚才的可执行文件），会自动下载Country.mmdb
   3. 自己的 VPN 平台导入windows 或mac的 clash 会有一个 config.yaml，把这个也拿到
   4. 把刚才的Country.mmdb和config.yaml放在新建好的文件夹中
3. 系统配置
   1. 去 ununtu 的设置->网络->proxy，改成手动
   2. HTTP HTTPS 的 proxy 都改成 127.0.0.1:7890
   3. SOCKS 的 proxy 改成 127.0.0.1:7891
   4. Ignored host 改成：`localhost, 127.0.0.0/8, ::1`

## Reference

\[1] [https://blog.iswiftai.com/posts/clash-linux/](https://blog.iswiftai.com/posts/clash-linux/)
