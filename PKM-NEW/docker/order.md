# Docker命令

## 下载镜像

* 检索：`docker search`
* 下载：`docker pull`
* 列表：`docker images`
* 删除：`docker rmi`

部署一个nginx容器案例，首先查看所有的nginx，然后分别下载了最新的nginx和指定版本的1.26.0，查看目前的镜像，删除了一个，然后再查看目前的镜像
```bash
charles@Charless-MacBook-Pro ~/w/p/welcome-to-docker (main)> docker search nginx
NAME                                     DESCRIPTION                                     STARS     OFFICIAL
nginx                                    Official build of Nginx.                        21086     [OK]
nginx/nginx-ingress                      NGINX and  NGINX Plus Ingress Controllers fo…   111       
nginx/nginx-prometheus-exporter          NGINX Prometheus Exporter for NGINX and NGIN…   50        
nginx/unit                               This repository is retired, use the Docker o…   66        
nginx/nginx-ingress-operator             NGINX Ingress Operator for NGINX and NGINX P…   3         
nginx/nginx-quic-qns                     NGINX QUIC interop                              1         
nginx/nginxaas-loadbalancer-kubernetes                                                   1         
nginx/unit-preview                       Unit preview features                           0         
bitnami/nginx                            Bitnami Secure Image for nginx                  201       
ubuntu/nginx                             Nginx, a high-performance reverse proxy & we…   133       
bitnamicharts/nginx                      Bitnami Helm chart for NGINX Open Source        2         
kasmweb/nginx                            An Nginx image based off nginx:alpine and in…   8         
rancher/nginx                                                                            2         
linuxserver/nginx                        An Nginx container, brought to you by LinuxS…   233       
dtagdevsec/nginx                         T-Pot Nginx                                     0         
paketobuildpacks/nginx                                                                   0         
vmware/nginx                                                                             3         
chainguard/nginx                         Build, ship and run secure software with Cha…   5         
gluufederation/nginx                      A customized NGINX image containing a consu…   1         
intel/nginx                                                                              0         
antrea/nginx                             Nginx server used for Antrea e2e testing        0         
circleci/nginx                           This image is for internal use                  2         
docksal/nginx                            Nginx service image for Docksal                 1         
cleanstart/nginx                         Secure by Design, Built for Speed, Hardened …   0         
corpusops/nginx                          https://github.com/corpusops/docker-images/     1         
charles@Charless-MacBook-Pro ~/w/p/welcome-to-docker (main)> docker pull nginx
Using default tag: latest
latest: Pulling from library/nginx
cf9a807fe41d: Pull complete 
40b6fc5618c6: Pull complete 
bb8ecb62799c: Pull complete 
2254fb813b11: Pull complete 
88770be1d442: Pull complete 
b89cf3ec7a3e: Pull complete 
cc57e8335c98: Pull complete 
Digest: sha256:553f64aecdc31b5bf944521731cd70e35da4faed96b2b7548a3d8e2598c52a42
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest
charles@Charless-MacBook-Pro ~/w/p/welcome-to-docker (main)> docker pull nginx:1.26.0
1.26.0: Pulling from library/nginx
8468a6b663f0: Pull complete 
77f9c49c64aa: Pull complete 
99f52b91c1b3: Pull complete 
24c63b8dcb66: Pull complete 
b046e9e37505: Pull complete 
e1de6ca4e153: Pull complete 
66f3b31fa55b: Pull complete 
Digest: sha256:192e88a0053c178683ca139b9d9a2afb0ad986d171fae491949fe10970dd9da9
Status: Downloaded newer image for nginx:1.26.0
docker.io/library/nginx:1.26.0
charles@Charless-MacBook-Pro ~/w/p/welcome-to-docker (main)> docker image ls
                                                                                               i Info →   U  In Use
IMAGE          ID             DISK USAGE   CONTENT SIZE   EXTRA
nginx:1.26.0   192e88a0053c        275MB         67.7MB        
nginx:latest   553f64aecdc3        244MB         58.3MB        
charles@Charless-MacBook-Pro ~/w/p/welcome-to-docker (main)> docker rmi 192e88a0053c
Untagged: nginx:1.26.0
Deleted: sha256:192e88a0053c178683ca139b9d9a2afb0ad986d171fae491949fe10970dd9da9
charles@Charless-MacBook-Pro ~/w/p/welcome-to-docker (main)> docker image ls
                                                                                               i Info →   U  In Use
IMAGE          ID             DISK USAGE   CONTENT SIZE   EXTRA
nginx:latest   553f64aecdc3        244MB         58.3MB        
charles@Charless-MacBook-Pro ~/w/p/welcome-to-docker (main)> 
```

## 启动容器

### 常见命令
* 运行：`docker run`
* 查看：`docker ps`
* 停止：`docker stop`
* 启动：`docker start`
* 重启：`docker restart`
* 状态：`docker status`
* 日志：`docker logs`
* 进入：`docker exec -it`
* 删除：`docker rm`

案例：第一个控制台中，我们运行了`docker run nginx`，这时候docker会去运行最新的nginx，对应我们已经下载的nginx:latest。启动后，我们打开第二个控制台输入`docker ps`就可以看到目前运行的容器了。我们使用`docker stop [名字]`或者 `docker stop [ID前三位]`，可以停止目前的容器，这时候运行`docker ps`就看不到他了，如果想看到运行和停止运行的所有容器需要输入`docker ps -a`。我们可以使用`docker start [名字]`或者 `docker start [ID前三位]`来重新开启一个容器。我们也可以使用`docker logs [名字]`或者 `docker logs [ID前三位]`来获取对应容器的日志。最后我们使用`docker rm [名字]`或者 `docker rm [ID前三位]`删掉指定容器。
```bash
charles@Charless-MacBook-Pro ~/w/p/welcome-to-docker (main)> docker run nginx
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2025/12/03 17:03:44 [notice] 1#1: using the "epoll" event method
2025/12/03 17:03:44 [notice] 1#1: nginx/1.29.3
2025/12/03 17:03:44 [notice] 1#1: built by gcc 14.2.0 (Debian 14.2.0-19) 
2025/12/03 17:03:44 [notice] 1#1: OS: Linux 6.12.54-linuxkit
2025/12/03 17:03:44 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2025/12/03 17:03:44 [notice] 1#1: start worker processes
...
2025/12/03 17:05:09 [notice] 1#1: worker process 32 exited with code 0
2025/12/03 17:05:09 [notice] 1#1: exit
charles@Charless-MacBook-Pro ~/w/p/welcome-to-docker (main)> 
```
```bash
⚙️  platform: MacOS ARM64
✈️  proxy: http://127.0.0.1:7897
🐢 Using Node v22.15.0
charles@Charless-MacBook-Pro ~> docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS     NAMES
22c3e7823f3e   nginx     "/docker-entrypoint.…"   21 seconds ago   Up 21 seconds   80/tcp    optimistic_grothendieck
charles@Charless-MacBook-Pro ~> docker ps -a
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS                     PORTS     NAMES
22c3e7823f3e   nginx     "/docker-entrypoint.…"   About a minute ago   Exited (0) 4 seconds ago             optimistic_grothendieck
charles@Charless-MacBook-Pro ~> docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
charles@Charless-MacBook-Pro ~> docker start optimistic_grothendieck
optimistic_grothendieck
charles@Charless-MacBook-Pro ~> docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS     NAMES
22c3e7823f3e   nginx     "/docker-entrypoint.…"   2 minutes ago   Up 4 seconds   80/tcp    optimistic_grothendieck
charles@Charless-MacBook-Pro ~> docker stop optimistic_grothendieck
optimistic_grothendieck
charles@Charless-MacBook-Pro ~> docker logs optimistic_grothendieck
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2025/12/03 17:03:44 [notice] 1#1: using the "epoll" event method
2025/12/03 17:03:44 [notice] 1#1: nginx/1.29.3
2025/12/03 17:03:44 [notice] 1#1: built by gcc 14.2.0 (Debian 14.2.0-19) 
2025/12/03 17:03:44 [notice] 1#1: OS: Linux 6.12.54-linuxkit
2025/12/03 17:03:44 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
...
2025/12/03 17:05:09 [notice] 1#1: exit
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: IPv6 listen already enabled
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2025/12/03 17:05:41 [notice] 1#1: using the "epoll" event method
2025/12/03 17:05:41 [notice] 1#1: nginx/1.29.3
2025/12/03 17:05:41 [notice] 1#1: built by gcc 14.2.0 (Debian 14.2.0-19) 
2025/12/03 17:05:41 [notice] 1#1: OS: Linux 6.12.54-linuxkit
2025/12/03 17:05:41 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
...
2025/12/03 17:05:54 [notice] 1#1: exit
charles@Charless-MacBook-Pro ~> docker rm optimistic_grothendieck
optimistic_grothendieck
charles@Charless-MacBook-Pro ~> docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
charles@Charless-MacBook-Pro ~> 
```

### run的命令参数
* -d：后台运行容器
* --name：指定容器名称
* -p：指定端口映射

案例，使用后台启动，指定容器名称为mynginx，映射端口为8080:80
```bash
charles@Charless-MacBook-Pro ~> docker run -d -p 80:80 --name mynginx nginx
d4387d39328032faefd5e7c041d8dc6fdf413e2743d74dc6fec5c00c27d9fa77
```
现在再去127.0.0.1，就可以看到nginx的默认欢迎页面了

### 进入容器内部的命令行
* `docker exec`：进入容器内部的命令行

案例，进入容器内部的命令行，修改nginx容器内部的文件
```bash
charles@Charless-MacBook-Pro ~> docker exec -it mynginx /bin/bash
root@d4387d393280:/# ls /
bin   dev   docker-entrypoint.sh  home  media  opt   root  sbinsys  usr
boot  docker-entrypoint.d  etc lib   mnt    proc  run   srvtmp  var
root@d4387d393280:/# cd usr/share/nginx/html/
root@d4387d393280:/usr/share/nginx/html# ls
50x.html  index.html
root@d4387d393280:/usr/share/nginx/html# echo "<h1>Hello Nginx</h1>" > index.html
root@d4387d393280:/usr/share/nginx/html# cat index.html
<h1>Hello Nginx</h1>
root@d4387d393280:/usr/share/nginx/html# 
```

### 快速删除所有的容器

* `docker ps -aq`：a代表所有，q代表只显示id
```bash
charles@Charless-MacBook-Pro ~> docker run -d -p 80:80 --name mynginx nginx
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
Digest: sha256:553f64aecdc31b5bf944521731cd70e35da4faed96b2b7548a3d8e2598c52a42
Status: Downloaded newer image for nginx:latest
459f89f75d92162627838cb5f766258a9f46f5a942a4251c9d98208a1eff13a5
charles@Charless-MacBook-Pro ~> docker ps -a
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                 NAMES
459f89f75d92   nginx     "/docker-entrypoint.…"   13 seconds ago   Up 13 seconds   0.0.0.0:80->80/tcp, [::]:80->80/tcp   mynginx
charles@Charless-MacBook-Pro ~> docker ps -aq
459f89f75d92
charles@Charless-MacBook-Pro ~> docker rm -f $(docker ps -aq)
459f89f75d92
charles@Charless-MacBook-Pro ~> 
```

## 保存镜像

* 提交：`docker commit`
* 保存：`docker save`
* 加载：`docker load`

案例：我们可以提交某一个镜像到自己的仓库。比如，把修改了index.html的改了的保存成myginx:v1.0。然后也可以保存某一个镜像到本地。比如把刚才的myginx:v1.0保存成本地的mynginx.tar。最后可以导入本地的mynginx.tar。首先我们删除所有的容器和镜像，然后使用docker load进行导入。
```bash
charles@Charless-MacBook-Pro ~> docker commit --help
Usage:  docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]

Create a new image from a container\'s changes

Aliases:
  docker container commit, docker commit

Options:
  -a, --author string    Author (e.g., "John Hannibal Smith <hannibal@a-team.com>")
  -c, --change list      Apply Dockerfile instruction to the created image
  -m, --message string   Commit message
      --no-pause         Disable pausing container during commit
charles@Charless-MacBook-Pro ~> docker commit -m "update index.html" mynginx mynginx:v1.0
sha256:0856ddb965df7e3ee2c725d54786f780972619944d0d7d7b18bc91f136ffd676
charles@Charless-MacBook-Pro ~> docker image ls
                                                                                                         i Info →   U  In Use
IMAGE          ID             DISK USAGE   CONTENT SIZE   EXTRA
mynginx:v1.0   0856ddb965df        244MB         58.3MB        
nginx:latest   553f64aecdc3        244MB         58.3MB    U   
charles@Charless-MacBook-Pro ~> docker save --help
Usage:  docker save [OPTIONS] IMAGE [IMAGE...]

Save one or more images to a tar archive (streamed to STDOUT by default)

Aliases:
  docker image save, docker save

Options:
  -o, --output string      Write to a file, instead of STDOUT
      --platform strings   Save only the given platform(s). Formatted as a comma-separated list of
                           "os[/arch[/variant]]" (e.g., "linux/amd64,linux/arm64/v8")
charles@Charless-MacBook-Pro ~> docker save -o mynginx.tar mynginx:v1.0
charles@Charless-MacBook-Pro ~> ls
Applications/Library/Parallels/
Applications (Parallels)/Movies/Pictures/
Desktop/Music/Public/
Documents/Nutstore Files/mynginx.tar
Downloads/NutstoreCloudBridge/workspace/
charles@Charless-MacBook-Pro ~> docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                 NAMES
d4387d393280   nginx     "/docker-entrypoint.…"   21 minutes ago   Up 21 minutes   0.0.0.0:80->80/tcp, [::]:80->80/tcp   mynginx
charles@Charless-MacBook-Pro ~> docker rm -f mynginx
mynginx
charles@Charless-MacBook-Pro ~> docker image ls
                                                                                                         i Info →   U  In Use
IMAGE          ID             DISK USAGE   CONTENT SIZE   EXTRA
mynginx:v1.0   0856ddb965df        244MB         58.3MB        
nginx:latest   553f64aecdc3        244MB         58.3MB    U   
charles@Charless-MacBook-Pro ~> docker rmi 0856ddb965df
Untagged: mynginx:v1.0
charles@Charless-MacBook-Pro ~> docker rm 18e3794743a1
18e3794743a1
charles@Charless-MacBook-Pro ~> docker rmi 553f64aecdc3
Untagged: nginx:latest
Deleted: sha256:553f64aecdc31b5bf944521731cd70e35da4faed96b2b7548a3d8e2598c52a42
charles@Charless-MacBook-Pro ~> docker load --help
Usage:  docker load [OPTIONS]

Load an image from a tar archive or STDIN

Aliases:
  docker image load, docker load

Options:
  -i, --input string       Read from tar archive file, instead of STDIN
      --platform strings   Load only the given platform(s). Formatted as a comma-separated list of
                           "os[/arch[/variant]]" (e.g., "linux/amd64,linux/arm64/v8").
  -q, --quiet              Suppress the load output
charles@Charless-MacBook-Pro ~> docker load -i ./mynginx.tar 
Loaded image: mynginx:v1.0
charles@Charless-MacBook-Pro ~> docker image ls
                                                                                                         i Info →   U  In Use
IMAGE          ID             DISK USAGE   CONTENT SIZE   EXTRA
mynginx:v1.0   0856ddb965df        244MB         58.3MB        
charles@Charless-MacBook-Pro ~> 
```

## 分享社区

* 注册：`docker login`
* 命名：`docker tag`
* 推送：`docker push`
* 拉取：`docker pull`

案例：我用的docker的客户端的命令行，所以直接docker login就可以登陆，如果在命令行，需要输入账户密码。然后我们需要创建tag，最后把这个打上tag的镜像推送到自己的云。我们可以去网站上看到自己上传的镜像。最后推荐也上传一个latest版本。
```bash
charles@Charless-MacBook-Pro ~> docker login
Authenticating with existing credentials... [Username: charlesshan]

i Info → To login with a different account, run 'docker logout' followed by 'docker login'


Login Succeeded
charles@Charless-MacBook-Pro ~> docker tag --help
Usage:  docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]

Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE

Aliases:
  docker image tag, docker tag
charles@Charless-MacBook-Pro ~> docker tag mynginx:v1.0 charlesshan/mynginx:v1.0
charles@Charless-MacBook-Pro ~> docker image ls
                                                                                                         i Info →   U  In Use
IMAGE                      ID             DISK USAGE   CONTENT SIZE   EXTRA
charlesshan/mynginx:v1.0   0856ddb965df        244MB         58.3MB        
mynginx:v1.0               0856ddb965df        244MB         58.3MB        
charles@Charless-MacBook-Pro ~> docker push charlesshan/mynginx:v1.0
The push refers to repository [docker.io/charlesshan/mynginx]
2254fb813b11: Pushed 
40b6fc5618c6: Pushed 
88770be1d442: Pushed 
b89cf3ec7a3e: Pushed 
892ee1f6f3ef: Pushed 
cc57e8335c98: Pushed 
bb8ecb62799c: Pushed 
cf9a807fe41d: Pushed 
v1.0: digest: sha256:0856ddb965df7e3ee2c725d54786f780972619944d0d7d7b18bc91f136ffd676 size: 2037
charles@Charless-MacBook-Pro ~> 
```