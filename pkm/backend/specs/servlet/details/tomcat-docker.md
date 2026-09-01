
# Tomcat docker 部署

我更想要docker部署tomcat服务器，下边是具体操作流程。如果是直接给windows下载安装tomcat看这个：[tomcat-download](tomcat-download.md)

`01-init.sh`：直接映射，外边的空目录会覆盖掉里面的文件，所以要先启动一个临时tomcat将内容复制出来。注意：docker版本的tomcat里面的案例是`webapps.dist`而不是`webapps`，所以复制目录的时候需要改一下！（真实踩坑记录！）

```bash
# 创建临时容器
docker run -d --name temp-tomcat tomcat:10.1-jdk17

# 复制 webapps 因为 docker 版本的把默认项目放到了webapps.dist而不是webapps
docker cp temp-tomcat:/usr/local/tomcat/webapps.dist/ ./webapps

# 复制 conf
docker cp temp-tomcat:/usr/local/tomcat/conf ./conf

# 复制 log（可能为空，但先创建目录）
mkdir -p ./log

# 删除临时容器
docker rm -f temp-tomcat
```

compose.yaml

```yaml
version: '3.8'

services:
  tomcat:
    image: tomcat:10.1-jdk17
    container_name: my-tomcat
    ports:
      - "8080:8080"
    volumes:
      - ./webapps:/usr/local/tomcat/webapps
      - ./conf:/usr/local/tomcat/conf
      - ./log:/usr/local/tomcat/log
    restart: unless-stopped
```

清空然后重新部署
  
```powershell
# 停止并删除：容器 + 网络 + 匿名卷
docker-compose down -v

# 删除当前容器（防止残留）
docker rm -f my-tomcat

# 删除镜像（强制重新下载）
docker rmi -f tomcat:10.1-jdk17

# 清理本地卷目录（重新同步）
rm -rf conf webapps logs
mkdir -p conf webapps logs

# 用临时容器把默认 conf 同步到本地
docker run -d --name temp-config tomcat:10.1-jdk17
sleep 3
docker cp temp-config:/usr/local/tomcat/conf/. ./conf/
docker rm -f temp-config

# 启动（会使用 ./conf ./webapps ./logs 这三个挂载）
docker-compose up -d
sleep 3
docker-compose ps
```

更新配置（停掉容器再启动，使配置生效）

```powershell
# 修改 ./conf 下的配置文件后执行
docker-compose down
docker-compose up -d
  
# 验证
docker-compose ps
docker-compose logs tomcat --tail 50
```

进入容器 bash（排障/查看容器内文件）

```powershell
docker-compose exec tomcat bash
```

内部的一些内容

```shell
root@508c495fad77:/usr/local# ls
bin  etc  games  include  lib  man  sbin  share  src  tomcat
root@508c495fad77:/usr/local# cd tomcat/
root@508c495fad77:/usr/local/tomcat# ls
bin           CONTRIBUTING.md  LICENSE         NOTICE         RUNNING.txt    webapps
BUILDING.txt  filtered-KEYS    logs            README.md      temp           webapps.dist
conf          lib              native-jni-lib  RELEASE-NOTES  upstream-KEYS  work
root@508c495fad77:/usr/local/tomcat# cd bin
root@508c495fad77:/usr/local/tomcat/bin# ls
bootstrap.jar       ciphers.sh                    configtest.sh  makebase.sh      shutdown.sh      tool-wrapper.sh
catalina.sh         commons-daemon.jar            daemon.sh      migrate.sh       startup.sh       version.sh
catalina-tasks.xml  commons-daemon-native.tar.gz  digest.sh      setclasspath.sh  tomcat-juli.jar
root@508c495fad77:/usr/local/tomcat/bin# cd ../conf
root@508c495fad77:/usr/local/tomcat/conf# ls
Catalina         catalina.properties  jaspic-providers.xml  logging.properties  tomcat-users.xml  web.xml
catalina.policy  context.xml          jaspic-providers.xsd  server.xml          tomcat-users.xsd
root@508c495fad77:/usr/local/tomcat/conf#
```

webapps/docs/META-INF/content.xml：因为我们用的docker的tomcat，所以很多项目外面要看需要允许全部ip
```xml
<Context antiResourceLocking="false" privileged="true">
  <!-- 注释掉限制，允许所有 IP 访问 -->
  <!--
  <Valve className="org.apache.catalina.valves.RemoteAddrValve"
         allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1" />
  -->
</Context>
```

---

## Tomcat 目录介绍

### `bin`（Binary）

- **作用**：存放 Tomcat 的可执行脚本和启动/停止相关的文件。
- **关键内容**：
    - **启动/停止脚本**：如 `startup.sh`（Linux/macOS）和 `startup.bat`（Windows）用于启动 Tomcat；`shutdown.sh`/`shutdown.bat`用于停止。
    - 其他工具：如 `catalina.sh`（核心脚本）、`version.sh`（版本检查）等。

### `conf`（Configuration）

- **作用**：存放 Tomcat 的全局配置文件。
- **关键文件**：
    - `server.xml`：主配置文件，定义**服务器端口（默认 8080）**、虚拟主机（Host）、连接器（Connector）等。
    - `web.xml`：所有 Web 应用的默认部署描述符（如默认 Servlet、MIME 类型）。

### `lib`（Libraries）

- **作用**：存放 Tomcat 运行所需的全局 Java 库（JAR 文件）。
- **关键内容**：Tomcat 核心库：如 `servlet-api.jar`、`jsp-api.jar`、`catalina.jar`等。

### `logs`

- **作用**：存放 Tomcat 运行日志和应用日志
- **关键文件**：
    - `catalina.out`**/**`catalina.log`：核心引擎日志（启动/停止错误等）。
    - `localhost.log`：应用部署相关的日志（如 Context 加载失败）。
- **注意**：日志是排查问题的首要位置，可通过 `conf/logging.properties`配置格式和级别。

### `temp`

- **作用**：存放临时文件（如上传的文件、Session 持久化数据等）。

### `webapps`

- **作用**：默认的 Web 应用部署目录。我们开发的 webapp 默认都放到这个目录下。
- 这里新建一个文件夹就是新的一个项目，可以去先部署一个准备工作，后边的案例需要用到：[static-website-development](static-website-development.md)

### `work`

- **作用**：存放运行时生成的临时文件（主要是 JSP 编译后的 Servlet 类文件和 Session 数据）。
- **JSP 编译结果**：如 `org/apache/jsp/index_jsp.java`和 `.class`文件。

