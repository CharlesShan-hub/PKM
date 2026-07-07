# PKM - Personal Knowledge Map  
---

![image text](./resources/title_small.webp)

* 💻 Practise
	* Backend
		* systems: [windows](pkm/backend/systems/windows/README.md), [linux](pkm/backend/systems/linux/README.md), [docker](pkm/backend/systems/docker/README.md), k8s
		* Language: [javase](pkm/backend/languages/javase/README.md), kotlin, go
		* Specs: ⭐[JDBC](pkm/backend/specs/jdbc/README.md), [Servlet](pkm/backend/specs/servlet/README.md), JPA, JMS
		* Design: [Design Pattern](pkm/backend/design/design-pattern/README.md), Coding Standards
		* database
			* relational database: [mysql](pkm/backend/database/mysql/README.md), postgresql, sqlite, oracle
			* nosql database: ⭐[Redis](pkm/backend/database/redis/README.md), MongoDB, ElasticSearch
		* package: ⭐[maven](pkm/backend/package/maven/README.md), [gradle](pkm/backend/package/gradle/README.md)
		* version: [git](pkm/backend/version/git/README.md), ⭐[SVN](pkm/backend/version/svn/README.md)
		* java web: [Spring](pkm/backend/javaweb/spring/README.md), [SpringBoot](pkm/backend/javaweb/springboot/README.md)
		* orm：Hibernate, [MyBatis](pkm/backend/orm/mybatis/README.md), [MyBatisPlus](pkm/backend/orm/mybatisplus/README.md), Easy-Query, Spring Data JPA
		* message-queue: [RabbitMQ](pkm/backend/message-queue/rabbitmq/README.md), [RocketMQ](pkm/backend/message-queue/rocketmq/README.md), Kafka, Pulsar
		* cron-job: ⭐[xxl-job](pkm/backend/javaweb/xxl-job/README.md), quartz, Elastic-Job
		* tools: ⭐[markdown](pkm/backend/tools/markdown/README.md), ⭐[json](pkm/backend/tools/json/README.md), ⭐[XML](pkm/backend/tools/xml/README.md), [yaml](pkm/backend/tools/yaml/README.md), toml, [re](pkm/backend/tools/regular-expression/README.md)
		* microservices
			* framework
				* SpringCloud
				* Dubbo
				* gRPC
				* zookeeper
			* service-mesh
				* Istio
				* Linkerd
			* service-registry
				* Nacos
				* Eureka
				* Consul
	* Frontend
		* [Frontend Trio](pkm/frontend/frontend-trio/frontend-trio.md)
		* [vue](pkm/frontend/vue.md)
		* [electron](pkm/frontend/electron/README.md)
	* Artificial Intelligence
		* [Python](pkm/ai/python/README.md)
		* [Machine Learning](pkm/ai/machine-learning/README.md)
		* [Knowledge Graph](pkm/ai/knowledge-graph/README.md)
	* Embedded
		* [c](pkm/embedded/c/README.md)
		* [cpp](pkm/embedded/cpp/README.md)
		* [rust](pkm/embedded/rust/README.md)
		* [esp](pkm/embedded/esp8266/README.md)
	* Others
		* [Minecraft](pkm/others/minecraft/README.md)
		* [Ethereum](pkm/others/ethereum/README.md)
		* [Vehicle Diagnostics](pkm/others/vehicle-diagnostics/README.md)
* 📖 Theory
	* Math
		* [Probability](pkm/math/probability/README.md)
		* [Calculus](pkm/math/calculus/README.md)
		* [Linear Algebra](pkm/math/linear-algebra/README.md)
	* Computer Science
		* ⭐[Computer Network](pkm/theory/computer-network/README.md)
		* ⭐[Data Structure](pkm/theory/data-structure/README.md)
		* ⭐[Computer Organization](pkm/theory/computer-organization/README.md)
		* ⭐[Operating System](pkm/theory/operating-system/README.md)
		* [DataBase](pkm/theory/database/README.md)
		* [Digital Image Processing](pkm/theory/digital-image-processing/README.md)
* 🎨 Hobbies and Life
	* Life Skill
		* [Driving License](pkm/hobbies/life-skill/driving-license/README.md)
	* Humanities
		* ⭐[Modern China](pkm/hobbies/humanities/modern-china/README.md)
		* ⭐[Mao Zedong Thought](pkm/hobbies/humanities/mao-zedong-thought/README.md)
		* ⭐[Ideological Cultivation](pkm/hobbies/humanities/ideological-cultivation/README.md)
		* ⭐[Marxism](pkm/hobbies/humanities/marxism/README.md)
		* [Social Psychology](pkm/hobbies/humanities/social-psychology/README.md)
---
Todo
* sql-索引
* sql-优化
* redis
    * jmeter，压测工具
* javase
	* strictfp关键字
	* 多线程：volatile

## 开发环境梳理

### windows

Scoop 统管工具链：
  包管理 → 版本管理 → 项目管理 → C → Java → Python
Docker 管服务：
  数据库 → node → redis

😋包管理器：（√）**scoop**，（x 淘汰）chocolatey，（x 包少，需要手动添加PATH）winget
```powershell
# 允许执行脚本（只对当前用户，安全）
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
# 装 Scoop
irm get.scoop.sh | iex
```

😋终端：（√ ）**powershell**，（x 淘汰）cmd，（x 需要linux子系统）fish

😋版本管理：（√ 个人使用）**git**，（√ 团队使用）**svn**
```powershell
scoop install git
```
svn使用TortoiseSVN客户端，自动安装svn命令。

😋项目管理：（√ 项目构建编排）**just**
```powershell
scoop install just
```

😋C 语言工具链：（√）**cmake**，（√）**gcc**，（√）**mingw32-make**
```powershell
scoop install cmake mingw # mingw 包自带 gcc + mingw32-make
```

😋Java 语言工具链：（√）**maven**，（x 暂时不用）gradle
```powershell
scoop install maven
scoop bucket add java # java需要加载扩展包
scoop install corretto8-jdk corretto21-jdk # 安装指定版本java

# 切换版本需要两步：scoop reset + 更新 JAVA_HOME（Maven 强制要求）
scoop reset corretto21-jdk  # 切到 Java 21（日常开发）
$env:JAVA_HOME = "$env:USERPROFILE\scoop\apps\corretto21-jdk\current"
[Environment]::SetEnvironmentVariable("JAVA_HOME", $env:JAVA_HOME, "User")

scoop reset corretto8-jdk   # 切到 Java 8（编译 CMS 项目）
$env:JAVA_HOME = "$env:USERPROFILE\scoop\apps\corretto8-jdk\current"
[Environment]::SetEnvironmentVariable("JAVA_HOME", $env:JAVA_HOME, "User")
```

😋Python 语言工具链：（√）**pixi**，（x 淘汰）uv
```powershell
scoop install pixi      # main bucket 中的 pixi
#uv self uninstall              # 卸载 uv（原手动安装在 ~\.local\bin\）
```

😋数据库相关：（√）**mysql**，（√）dameng
* mysql版本管理使用docker
* dameng数据库需要安装驱动，目前没有版本管理

## Resources
* [Java 全栈知识体系](https://pdai.tech/)