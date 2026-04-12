# Docker 集成

##  compose

* 上线：`docker compose up -d`
* 下线：`docker compose down`
* 启动：`docker compose start x1 x2 x3`
* 停止：`docker compose stop x1 x3`
* 扩容：`docker compose scale x2=3`

案例：创建一个博客系统。

首先建立一个网络“blog”

```bash
docker network create blog
```

然后创建一个mysql数据库容器

```bash
^^/w/d/dockerdemo >>> mkdir myconf
^^/w/d/dockerdemo >>> chmod 777 ./myconf 
^^/w/d/dockerdemo >>> pwd
/home/parallels/workspace/data/dockerdemo
```

```bash
 docker run \
-d -p 3306:3306 \
-e MYSQL_ROOT_PASSWORD=123456 \
-e MYSQL_DATABASE=wordpress \
-v mysql-data:/var/lib/mysql \
-v /home/parallels/workspace/data/dockerdemo/myconf:/etc/mysql/conf.d \
--restart always \
--name mysql \
--network blog \
mysql:8.0
```

最后创建一个开源博客系统容器

```bash
docker run \
-d -p 8080:80 \
-e WORDPRESS_DB_HOST=mysql \
-e WORDPRESS_DB_USER=root \
-e WORDPRESS_DB_PASSWORD=123456 \
-e WORDPRESS_DB_NAME=wordpress \
-v wordpress:/var/www/html \
--restart always \
--name wordpress-app \
--network blog \
wordpress:latest
```

## compose.yaml

上面的方法需要手动的创建和开启一个个的容器。我们也可以通过编写`compose.yaml`进行

``` bash
name: bolg

networks:
  blog:
    driver: bridge
    name: blog

volumes:
  mysql-data:
    name: mysql-data
  wordpress:
    name: wordpress

services:
  mysql:
    image: mysql:8.0
    ports:
      - "3306:3306"  # 主机端口:容器端口
    environment:
      MYSQL_ROOT_PASSWORD: 123456
      MYSQL_DATABASE: wordpress
    container_name: mysql
    restart: always
    volumes:
      - mysql-data:/var/lib/mysql
      - /media/psf/Home/workspace/data/dockerdemo/myconf:/etc/mysql/conf.d
    networks:
      - blog

  wordpress-app:
    image: wordpress:latest
    container_name: wordpress-app
    restart: always
    ports:
      - "8080:80"  # 主机端口:容器端口
    environment:
      WORDPRESS_DB_HOST: mysql:3306
      WORDPRESS_DB_USER: root
      WORDPRESS_DB_PASSWORD: 123456
      WORDPRESS_DB_NAME: wordpress
    volumes:
      - wordpress:/var/www/html
    networks:
      - blog
    depends_on:
      - mysql
```

上线的运行案例

```bash
/m/p/H/w/d/dockerdemo >>> vi compose.yaml
/m/p/H/w/d/dockerdemo >>> docker rm -f $(docker ps -aq) 
f338940de01d
6bba279df740
fc8ad77a4b69
24b8195b925e
0430445d23ea
/m/p/H/w/d/dockerdemo >>> docker volume ls
DRIVER    VOLUME NAME
local     mysql-data
local     ngconf
local     wordpress
/m/p/H/w/d/dockerdemo >>> docker volume rm mysql-data wordpress
mysql-data
wordpress
/m/p/H/w/d/dockerdemo >>> docker network ls
NETWORK ID     NAME      DRIVER    SCOPE
642bf0641e2a   blog      bridge    local
35c2ac707868   bridge    bridge    local
24c3de86af4a   host      host      local
272e849499d6   mynet     bridge    local
f097d2b7c757   none      null      local
/m/p/H/w/d/dockerdemo >>> docker network rm blog
blog
/m/p/H/w/d/dockerdemo >>> docker compose -f ./compose.yaml up -d
[+] up 5/5
 ✔ Network blog            Created   0.0s 
 ✔ Volume wordpress        Created   0.0s 
 ✔ Volume mysql-data       Created   0.0s 
 ✔ Container mysql         Created   0.1s 
 ✔ Container wordpress-app Created   0.0s 
/m/p/H/w/d/dockerdemo >>>  
```

如果修改其中的地方，我们只需要修改对应位置的`compose.yaml`还是去up就可以了，docker会自动判断哪些是要修改的。

最后如果要删除 容器的时候把镜像也删除，可以运行

`docker compose -f compose.yaml down --rmi all -v`
