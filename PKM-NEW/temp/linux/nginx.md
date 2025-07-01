# nginx

---
## 简介

nginx = 「Web服务器」 + 「方向代理服务器」 + 「IMAP/POP3/SMTP代理服务器」

* 官网: https://nginx.org/en/
* 视频（19年尚硅谷）: https://www.bilibili.com/video/BV1zJ411w7SV
* 视频（22年尚硅谷-比较啰嗦）: https://www.bilibili.com/video/BV1yS4y1N76R
* 短视频（反向代理比喻）: https://www.bilibili.com/video/BV16h411L7NK 

---
## 概念

* 优点
	* 高性能（事件驱动，支持高并发，根据实验支持五万个连接）
	* 多功能（静态托管/反向代理/负载均衡）
	* 低资源占用、配置灵活、热部署无缝重启、安全可靠
* 反向代理
	* 正向代理：保护客户端。比如翻墙用的梯子就是正向代理。
	* 反向代理：保护服务器。隐藏正式服务器的地址，对于客户端的视角，反向代理服务器和服务器本身是为一个整体。
	* 作用：负载均衡，防止攻击，通过缓存降低服务器压力
* 负载均衡
	* 定义：将网络请求或计算任务​​动态分配​​到多个服务器（或资源）上，避免单点过载。
	- 算法
		- 轮询法；加权轮询法
		- 根据服务器当前负载调整分配情况
		- 根据IP分配服务器
- 动静分离：动态资源放在服务器，静态资源比如网页放在nginx，减轻服务器的压力。
- 常见问题
	- worker_processes 设置多少比较好：worker 数量最好和 cpu 数量一致。
	- 一次请求会用到多少 worker_connections（连接数）： 2 或者 4
	- nginx 有一个 master 和 worker_processes 个woker，每个 worker 支持的最大连接数是worker_connections，支持的最大并发数是多少
		- 普通连接：worker_processes * worker_connections / 2
		- 反向代理：worker_processes * worker_connections / 4

---
## 基本使用

本文档使用ubuntu24系统

* 安装（主要是一些前置配置）: https://nginx.org/en/docs/install.html
	```bash
	sudo apt install nginx
	```
* 版本
	```shell
	nginx -v
	```
* 启动，启动失败两种方法，第一种关闭，第二种去看看那个进程用到了nginx然后kill
	```shell
	sudo nginx
	```
* 关闭
	```shell
	sudo nginx -s stop
	```
* 查看用到nginx的进程并kill
	```shell
	sudo nginx -s stop
	sudo kill -9 需要kill的进程id
	```
* 启动
	```shell
	ps -ef | grep nginx
	```
* 重载（不需重启服务器，重新加载config）
	```shell
	nginx -s reload
	```

---
## 配置文件

* 找到nginx配置文件，比如`/etc/nginx/nginx.conf`
	* 主配置文件：`/etc/nginx/nginx.conf`
	- 子配置目录：`/etc/nginx/conf.d/`（推荐存放自定义配置）
	- 默认网站配置：`/etc/nginx/sites-enabled/`（通常软链接到 `sites-available/`）
	```shell
	whereis nginx
	```
* 配置文件结构
	```json
		...              #全局块
		
		events {         #events块
		   ...
		}
		
		http      #http块
		{
		    ...   #http全局块
		    server        #server块
		    { 
		        ...       #server全局块
		        location [PATTERN]   #location块
		        {
		            ...
		        }
		        location [PATTERN] 
		        {
		            ...
		        }
		    }
		    server
		    {
		      ...
		    }
		    ...     #http全局块
		}
	```
* 全局块
	```conf
		user www-data; # 运行 Nginx 的用户/组 
		worker_processes auto; # 工作进程数，越大支持的并发数量也越多
		error_log /var/log/nginx/error.log warn; # 错误日志路径和级别 
		pid /run/nginx.pid; # 存储主进程 PID 的文件
	```
* event块：nginx与用户网络简介的配置
	```conf
		events { 
			worker_connections 1024; # 每个 worker 进程的最大连接数 
			use epoll; # 事件驱动模型（Linux 推荐 epoll） 
			multi_accept on; # 允许一次性接受多个连接 
		}
	```
* http块（配置最频繁的部分，负载均衡等内容都在这里），http块包含http全局块和server块
* http块中的http全局块
	```conf
	http { 
		include       mime.types;   #文件扩展名与文件类型映射表
	    default_type  application/octet-stream; #默认文件类型，默认为text/plain
	    #access_log off; #取消服务日志    
	    log_format myFormat '$remote_addr–$remote_user [$time_local] $request $status $body_bytes_sent $http_referer $http_user_agent $http_x_forwarded_for'; #自定义格式
	    access_log log/access.log myFormat;  #combined为日志格式的默认值
	    sendfile on;   #允许sendfile方式传输文件，默认为off，可以在http块，server块，location块。
	    sendfile_max_chunk 100k;  #每个进程每次调用传输数量不能大于设定的值，默认为0，即不设上限。
	    keepalive_timeout 65;  #连接超时时间，默认为75s，可以在http，server，location块。

		server{
			# 这个就是http块中的server块了
		}
	}
	```
* http块中的server块重点
	```conf
	server {
	    listen 80;
	    server_name example.com www.example.com;  # 支持的域名
	    root /var/www/example;                    # 网站根目录
	    index index.html;
	
	    # 错误页面
	    error_page 404 /404.html;
	    error_page 500 502 503 504 /50x.html;
	}
	```

---
## 反向代理

* 需求：客户端请求 `example.com/api/user` → 代理到 `http://127.0.0.1:8080/user`
* `proxy_pass`：配置转跳的 url
* locationk块：用来配置某个 url 对应不同的转跳的 url

```txt
server {
    listen 80;
    server_name example.com;

    location /api/ {
        # 去掉 `/api/`，将请求代理到后端的 `/`
        proxy_pass http://127.0.0.1:8080/;  # 注意末尾的 `/`
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---
## 负载均衡

- ​**​后端服务器​**​：2 台（`192.168.1.101:8080` 和 `192.168.1.102:8080`）
- ​**​负载均衡器​**​：Nginx 监听 `80` 端口，轮询分发请求
* 轮询法（默认）：在http 块进行配置
```shell
http {
	# 定义后端服务器组
	upstream my_backend {
		# 默认就是轮询，无需额外参数
		server 192.168.1.101:8080;  # 后端服务器1
		server 192.168.1.102:8080;  # 后端服务器2
	}

	# 负载均衡服务器
	server {
		listen 80;
		location / {
			proxy_pass http://my_backend;  # 转发到后端
		}
	}
}
```
* ip 哈希（IP Hash）
```shell
upstream my_backend { 
	ip_hash; # 同一客户端固定访问同一后端 
	server 192.168.1.101:8080; 
	server 192.168.1.102:8080; 
}
```
* 加权轮询
```shell
upstream backend { 
	server 192.168.1.101:8080 weight=3; # 3/5 的请求 
	server 192.168.1.102:8080 weight=2; # 2/5 的请求 
}
```
* 最少连接（Least Connections）​
```shell
upstream backend {
    least_conn;  # 最少连接优先
    server 192.168.1.101:8080;
    server 192.168.1.102:8080;
}
```
* 以上四种完整版案例
```shell
events {}  # 必须有 events 块

http {
    # 策略1：轮询
    upstream backend_round_robin {
        server 192.168.1.101:8080;
        server 192.168.1.102:8080;
    }

    # 策略2：加权轮询
    upstream backend_weighted {
        server 192.168.1.101:8080 weight=3;
        server 192.168.1.102:8080 weight=1;
    }

    # 策略3：IP哈希
    upstream backend_ip_hash {
        ip_hash;
        server 192.168.1.101:8080;
        server 192.168.1.102:8080;
    }

    # 监听80端口，测试不同策略
    server {
        listen 80;

        # 测试路径1：轮询
        location /round {
            proxy_pass http://backend_round_robin;
        }

        # 测试路径2：加权
        location /weight {
            proxy_pass http://backend_weighted;
        }

        # 测试路径3：IP哈希
        location /iphash {
            proxy_pass http://backend_ip_hash;
        }
    }
}
```

---
## 动静分离

* 严格理解，是把静态请求和动态请求分离，而并不只是页面。
* 方案一，静态资源单独放在一个服务器
* 方案二，混合发布，通过 nginx 分开，使用 location指定不同后缀名进行转发(下边是案例)
```shell
server {
    listen 80;
    server_name example.com;
    
    # 静态资源目录
    root /var/www/html;
    
    # 动态请求转发到后端
    location /api/ {
        proxy_pass http://backend_server:8080;
        proxy_set_header Host $host;
    }
    
    # 静态资源直接处理
    location ~* \.(jpg|jpeg|png|gif|css|js|ico)$ {
        expires 7d;          # 缓存7天
        access_log off;      # 不记录静态资源日志
        add_header Cache-Control "public";
    }
    
    # 其他请求（如HTML）也由Nginx处理
    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

|​**​配置项​**​|​**​作用​**​|
|---|---|
|`location /api/`|所有以 `/api/` 开头的请求转发到后端应用服务器|
|`location ~* \.(扩展名)$`|正则匹配静态资源（`~*` 表示不区分大小写）|
|`expires 7d`|设置浏览器缓存时间（减少服务器压力）|
|`access_log off`|静态资源不记录访问日志（降低磁盘IO）|
|`try_files`|优先查找文件，不存在则返回 `index.html`（适合单页应用）|

---
## 高可用

* https://www.cnblogs.com/wenxuehai/p/15013654.html

当 nginx 宕机，整个系统就会失效。这就需要我们配置成高可用的 nginx 。
使用方案：主从架构 + Keepalived。使用 ​**​Keepalived​**​ 管理虚拟 IP（VIP），主节点故障时 VIP 自动漂移到备用节点。

需要配置`keepalived`
```shell
sudo apt update 
sudo apt install nginx keepalived -y
```
编辑主服务器里边的`/etc/keepalived/keepalived.conf`
```shell
vrrp_instance VI_1 {
    state MASTER                  # 主节点标识
    interface ens33               # 网卡名称（通过 ip a 查看）
    virtual_router_id 51          # 集群唯一 ID（0-255）
    priority 100                  # 优先级（主节点高于备节点）
    advert_int 1                 # 心跳间隔（秒）

    authentication {
        auth_type PASS            # 认证方式
        auth_pass 1111            # 密码（所有节点需一致）
    }

    virtual_ipaddress {
        192.168.1.100/24         # 虚拟 IP + 子网掩码
    }
}
```
编辑从服务器里边的`/etc/keepalived/keepalived.conf`
```shell
vrrp_instance VI_1 {
    state BACKUP       # 标识为备用节点
    priority 50        # 优先级更低
    interface eth0     # 网卡名与主节点一致
    virtual_router_id 51  # 必须与主节点相同
    authentication {
        auth_type PASS
        auth_pass 1111  # 密码与主节点一致
    }
    virtual_ipaddress {
        192.168.1.100/24  # 相同的VIP
    }
}
```


---
##  DEBUG：权限问题
403错误大概率因为路径没有权限。当我们修改 server 块里边的路径信息，如果路径并没有让 nginx 访问，就会出现 403 错误。

```bash
sudo chmod 755 /home/charles
sudo systemctl restart nginx
```


