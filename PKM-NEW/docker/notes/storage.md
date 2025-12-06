# Docker存储

> https://www.yuque.com/taijuanlebaai/fh01mx/co4xtf0ht8w65ik2?singleDoc#

## 目录挂载

比如docker内部创建的容器，连vim都不会安装。修改文件会很麻烦。我们可以提供docker提供的目录挂载，docker容器运行在内存中，文件则挂载在本地电脑，彼此分离。

使用`docker run -v [外部目录：内部目录]`或者`docker run -v [外部文件：内部文件]`
案例，我们把容器内部的`/usr/share/nginx/html`挂载到本地的`~/workspace/data/dockerdemo`然后在本地创建html。
```bash
charles@Charless-MacBook-Pro ~> cd ~/workspace/data
charles@Charless-MacBook-Pro ~/w/data> mkdir dockerdemo; cd dockerdemo
charles@Charless-MacBook-Pro ~/w/d/dockerdemo> docker run -d -p 80:80 -v ~/workspace/data/dockerdemo:/usr/share/nginx/html --
name mynginx nginx
36ce366ab7c8c12679bb7648d5ce344c219b276f147b6907e728ab430d2e5c67
charles@Charless-MacBook-Pro ~/w/d/dockerdemo> echo "<h1>Hello World!</h1>" > index.html
charles@Charless-MacBook-Pro ~/w/d/dockerdemo> 
```

## 卷映射

卷映射可以自动创建文件，比如nginx对应的配置文件。如果我们使用目录挂载，就需要那里本来就有需要的文件。

卷映射也叫做匿名目录挂载，系统会隐藏名字，如果宿主机器是linux机会放在`/usr/lib/docker`里边。但是我用的mac就会放在`/Users/charles/Library/Containers/com.docker.docker/Data/vms/0/data`这里边，然后里边是一个raw文件，不能直接查看。

所以我干脆在linux里边也装了一个docker
```bash
parallels@ubuntu-linux-2404 ~> sudo docker pull nginx:latest
latest: Pulling from library/nginx
88770be1d442: Pull complete 
b89cf3ec7a3e: Pull complete 
2254fb813b11: Pull complete 
40b6fc5618c6: Pull complete 
bb8ecb62799c: Pull complete 
cc57e8335c98: Pull complete 
cf9a807fe41d: Pull complete 
b1207165c1c8: Download complete 
d5fdc9d962cd: Download complete 
Digest: sha256:553f64aecdc31b5bf944521731cd70e35da4faed96b2b7548a3d8e2598c52a42
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest
parallels@ubuntu-linux-2404 ~> docker image ls
permission denied while trying to connect to the docker API at unix:///var/run/docker.sock
parallels@ubuntu-linux-2404 ~ [1]> sudo docker image ls
                                                                                          i Info →   U  In Use
IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-world:latest   f7931603f70e       22.5kB         10.2kB    U   
nginx:latest         553f64aecdc3        247MB         61.1MB        
parallels@ubuntu-linux-2404 ~> sudo docker run -p 80:80 -d -v ngconf:/etc/nginx -v ~/workspace/data/dockerdemo/assets:/usr/share/nginx/html --name app01 nginx
a5b8fda00eceb48ac73fa8c2d6d1a31260085475e20c92e3f6c6a3bf82b9c19d

```

要注意，docker默认都需要sudo，我们使用root用户可以查看挂载卷的内容
```bash
root@ubuntu-linux-2404 /v/l/d/v/n/_data# pwd
/var/lib/docker/volumes/ngconf/_data
root@ubuntu-linux-2404 /v/l/d/v/n/_data# ls
conf.d/  fastcgi_params  mime.types  modules@  nginx.conf  scgi_params  uwsgi_params

```

