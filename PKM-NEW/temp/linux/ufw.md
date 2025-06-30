# ufw

`ufw`（​**​Uncomplicated Firewall​**​）是 Ubuntu 系统上默认的防火墙管理工具，用于简化 `iptables`（Linux 内核的防火墙系统）的配置。它通过命令行提供直观的规则管理，适合新手和日常使用。

---

### ​**​核心特性​**​

1. ​**​简单易用​**​
    
    - 通过 `allow`/`deny` 等简单命令管理规则，无需直接操作复杂的 `iptables`。
    - 例如开放 HTTP 端口：
        
        ```
        sudo ufw allow 80
        ```
        
2. ​**​基于规则链​**​
    
    - 底层仍依赖 `iptables`，但抽象了细节，规则按顺序匹配（先匹配的规则生效）。
3. ​**​默认安全​**​
    
    - 初始状态为 ​**​禁用​**​，启用后默认 ​**​拒绝所有入站流量​**​，​**​允许所有出站流量​**​。
4. ​**​支持 IPv4/IPv6​**​
    
    - 自动兼容双栈网络。

---

### ​**​常用命令​**​

|命令|作用|
|---|---|
|`sudo ufw enable`|启用防火墙|
|`sudo ufw disable`|禁用防火墙|
|`sudo ufw status`|查看规则和状态|
|`sudo ufw allow 22/tcp`|允许 TCP 22 端口（SSH）|
|`sudo ufw deny 3306`|拒绝 MySQL 默认端口|
|`sudo ufw delete allow 80`|删除允许 80 端口的规则|
|`sudo ufw reset`|重置所有规则|

---

### ​**​配置示例​**​

#### ​**​1. 允许特定服务​**​

```
sudo ufw allow http      # 允许 HTTP（80）
sudo ufw allow https     # 允许 HTTPS（443）
sudo ufw allow ssh       # 允许 SSH（22）
```

#### ​**​2. 按 IP 限制​**​

```
sudo ufw allow from 192.168.1.100 to any port 22  # 仅允许特定 IP 访问 SSH
sudo ufw deny from 10.0.0.0/24                    # 拒绝整个子网
```

#### ​**​3. 日志管理​**​

```
sudo ufw logging on      # 启用日志（存储在 `/var/log/ufw.log`）
sudo ufw logging off     # 关闭日志
```

---

### ​**​注意事项​**​

1. ​**​启用前确保允许 SSH​**​
    
    - 若未允许 SSH 端口（22）直接启用 `ufw`，可能导致无法远程连接：
        
        ```
        sudo ufw allow ssh  # 先放行 SSH！
        sudo ufw enable
        ```
        
2. ​**​规则优先级​**​
    
    - 规则按添加顺序生效，例如：
        
        ```
        sudo ufw allow 80
        sudo ufw deny 80    # 此规则无效（前一条已允许）
        ```
        
3. ​**​应用生效​**​
    
    - 修改规则后无需重启，立即生效。

---

### ​**​高级功能​**​

- ​**​自定义规则文件​**​：  
    编辑 `/etc/ufw/*.rules` 手动添加复杂规则。
- ​**​限速防护​**​：  
    通过 `limit` 防止暴力破解：
    
    ```
    sudo ufw limit ssh  # 限制 SSH 连接频率
    ```
    

---

### ​**​与其他工具对比​**​

|工具|适用场景|复杂度|
|---|---|---|
|`ufw`|日常管理|⭐⭐|
|`iptables`|高级定制|⭐⭐⭐⭐|
|`firewalld`（RHEL/CentOS）|动态规则|⭐⭐⭐|

---

### ​**​总结​**​

- ​**​推荐使用场景​**​：个人服务器、小型项目快速配置防火墙。
- ​**​学习建议​**​：掌握基础命令后，可通过 `man ufw` 或 `sudo ufw --help` 探索更多参数。

遇到问题可检查日志：

```
sudo tail -f /var/log/ufw.log
```