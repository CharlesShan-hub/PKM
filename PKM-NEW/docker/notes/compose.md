# Docker 集成

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

