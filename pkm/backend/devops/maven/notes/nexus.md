# Maven私服


## 什么是私服

**Maven 私服是一种特殊的远程仓库，它是架设在局域网内的仓库服务**，用来代理位于外部的远程仓库（中央仓库、其他远程公共仓库）。一些无法从外部仓库下载到的构件，也能从本地上传到私服供其他人使用。

Maven 私服其实并不是 Maven 的核心概念，它仅仅是一种衍生出来的特殊的仓库，但这并不代表它不重要，相反由于私服具有降低中央仓库负荷、节省外网带宽、以及提高项目稳定性等优点，使得私服在实际开发过程中得到了相当普遍地使用。建立了 Maven 私服后，当局域网内的用户需要某个构件时，会先请求本地仓库，若本地仓库不存在所需构件，则请求 Maven 私服，将所需构件下载到本地仓库，若私服中不存在所需构件，再去请求外部的远程仓库，将所需构件下载并缓存到 Maven 私服，若外部远程仓库不存在所需构件，则 Maven 直接报错。

## Maven仓库管理器Nexus

### 什么是Nexus

Nexus 是 Sonatype（中央仓库实际的维护方） 公司发布的一款仓库（Repository）管理软件，常用来搭建 Maven 私服，所以也有人将 Nexus 称为“Maven仓库管理器”。 Sonatype Nexus 是当前最流行，使用最广泛的 Maven 仓库管理器。Nexus 分为开源版和专业版，开源版足以满足大部分 Maven 用户的需求。

### Nexus仓库的类型

Nexus默认内置了许多仓库，这些仓库被分为三大类，每种类型的仓库用于存放特定的`jar`包：

1. 代理仓库（proxy）：缓存下载过的依赖，避免重复从外网拉取。例如Nexus中内置的`maven-central`库就是一个代理仓库，从远程中央仓库中下载的`jar`包会被缓存到`maven-central`这个代理仓库中。
    
2. 宿主仓库（hosted）：存储本地构建的私有构件，如公司内部开发的 Jar 包。对于宿主仓库来说，包含多个子分类，例如：
    
    1. Release：存放稳定版本（如Nexus内置的`maven-releases`仓库），一旦发布到`<font style="color:rgb(64, 64, 64);">Release</font>`类型的仓库，同一个版本的构件**不允许重复部署或覆盖**。
        
    2. Snapshot：存放快照版本（如Nexus内置的`maven-snapshots`仓库），发布到`<font style="color:rgb(64, 64, 64);">Snapshot</font>`类型的仓库的构件**可以被多次覆盖**。
        
3. 仓库组（group）：将多个仓库合并为一个逻辑入口，简化客户端配置。例如Nexus中内置的`maven-public`仓库，主要是为了简化配置，这么多仓库不需要都配置，只需要配置一个仓库组就行了。
    

![](../assets/1748415005673-89afe0b0-da62-4231-b017-f4ea2c2fb0e5.png)

![](../assets/1748416008789-f89e99fa-867a-465a-b102-52e9e8af9fc9.png)

### 仓库为什么要分类

分类的目的是 **明确职责，优化管理**：

- **隔离环境**：区分快照（Snapshot）和正式版（Release），避免混淆。
- **权限控制**：可以为不同仓库设置不同的读写权限（如开发人员可上传 Snapshot，但只有管理员能发布 Release）。
- **性能优化**：代理仓库可以缓存热门依赖，而宿主仓库专注于私有构件。
- **简化客户端配置**：通过仓库组统一暴露仓库，客户端无需关心底层细节。

### 安装Nexus

#### 下载Nexus

下载地址：[https://help.sonatype.com/en/download.html](https://help.sonatype.com/en/download.html)

![](../assets/1748416143307-fbfa7646-2817-46ba-ab65-3a2572d6ebde.png)

#### 解压安装Nexus

下载后解压到一个没有中文的路径下：

![](../assets/1748417212139-306b2152-a385-46f7-915e-94d86414c884.png)

#### 启动Nexus服务

进入`C:\nexus-3.66.0-02\bin`目录下：

![](../assets/1748416328972-9a00cd53-6e6f-46e0-ba30-82889c09a3bb.png)

以管理员身份打开cmd窗口，并且`cd`到`bin`目录下，输入命令：`nexus /run`，需要等待一段时间，直到出现 `Started Sonatype Nexus OSS 3.66.0-02` 说明启动成功。

![](../assets/1748417327078-7366cef0-9e43-4f15-9622-3e6c0daa54ee.png)

并且会生成一个比较重要的`work`目录，如下：

![](../assets/1748417416853-34a37c63-e2cc-4592-bdbe-3aafc347afef.png)

#### 访问Nexus

访问地址：[http://localhost:8081](http://localhost:8081)

![](../assets/1748416595988-2b24beb1-6cd2-4e14-afb7-c991679f0621.png)

端口可以修改，在这个文件中：

![](../assets/1748416672545-14d2e604-9c45-41e6-b24c-c862d8c614e3.png)

## Nexus私服的应用

### 登录

![](../assets/1748416775783-982bc2e5-d7e2-4065-ab5d-a6e654c9b7a5.png)

用户名是：`admin`，密码在这个文件中：

![](../assets/1748417478053-d125829e-5832-4f35-b9ec-df0948119dee.png)

登录：

![](../assets/1748417582886-1ce0eac9-0671-495b-a3a0-46c528a3bc41.png)

第一次登录成功后会提示你修改密码：

![](../assets/1748417640216-18c7217e-b59d-4451-a321-5c85ff207cb6.png)

![](../assets/1748417687043-dce55a17-e3ce-422e-a08c-917c2fb2f495.png)

登录成功后的界面：

![](../assets/1748417749345-eeefe671-73ef-4237-a24e-4c823a4ab76b.png)

### 浏览仓库

![](../assets/1748417874332-867e01a3-e465-4c44-a4cc-5af47dfdc674.png)

### 设置仓库

#### 创建仓库

![](../assets/1748418119807-30a574a7-9620-4b0f-9ffd-84436d349060.png)

#### 创建代理仓库

![](../assets/1748418482049-0ba32f7f-1cda-4c17-b5b3-94e31a705ca5.png)

![](../assets/1748418706156-27e54b6e-a49b-424b-bba4-4ac44fe2d5a2.png)

阿里云 Maven 镜像：`https://maven.aliyun.com/repository/central`

![](../assets/1748418762670-c61ab893-ce50-40c3-8cb0-8ff34f9c2eda.png)

#### 创建宿主仓库：Release

![](../assets/1748418837443-c0a6356a-7834-4546-829b-2cc8dde19a05.png)

![](../assets/1748418901072-41331b13-0b44-4c42-95a2-60c4d26b543f.png)

![](../assets/1748418927704-4dbd87ec-5371-45c7-95dd-6c1851b9636d.png)

#### 创建宿主仓库：Snapshot

![](../assets/1748418837443-c0a6356a-7834-4546-829b-2cc8dde19a05.png)

![](../assets/1748419020431-465240ef-1267-4f74-9b68-888c3bda88f1.png)

![](../assets/1748418927704-4dbd87ec-5371-45c7-95dd-6c1851b9636d.png)

#### 创建仓库组

![](../assets/1748419084151-0fe17e4f-3c7b-4833-b8e1-10c775dbe7c5.png)

![](../assets/1748419158555-216555b4-a397-47f0-8442-167a79815d9b.png)

这一步非常重要，将创建的仓库放到一个仓库组当中：

![](../assets/1748419193925-86d73c38-a87e-46a7-8ccc-e3977850404e.png)

最后所有创建的仓库如下：

![](../assets/1748419530535-d55af541-5879-4732-82c7-6e34b0fd5daf.png)

### 使用Nexus下载jar包

#### 设置Maven本地仓库地址

修改`MAVEN_HOME/conf/settings.xml`文件：

<localRepository>D:\repository-nexus</localRepository>

#### 设置`<mirror>`标签

<mirror>  
  <id>nexus-jkweilai</id>  
  <mirrorOf>central</mirrorOf>  
  <name>nexusjkweilai</name>  
  <url>http://localhost:8081/repository/maven-public-jkweilai/</url>  
</mirror>

url从这里获取：

![](../assets/1748420039479-cbc13fca-3da8-42fd-8585-c217ae989353.png)

#### 设置Nexus的用户名和密码

找到 `settings.xml`文件的 `servers`标签，添加以下配置：

<server>  
  <id>nexus-jkweilai</id>  
  <username>admin</username>  
  <password>admin</password>  
</server>

注意：`<id>`必须和`<mirror>`中的`<id>`保持一致。

#### 确定IDEA中Maven指向的本地仓库地址

![](../assets/1748420366169-e927a0cd-f1c7-4838-a37a-c9ab8fc9a4dc.png)

#### 随意运行一个Maven项目的`clean`

![](../assets/1748420677388-10d3929e-df1c-4f03-9d10-b6de32f1e269.png)

![](../assets/1748420817495-b8e0dec7-375e-4351-98fb-79e553761898.png)

#### 观察本地仓库

![](../assets/1748420870835-8315dad6-74ed-4086-bcf2-3a9737ec2a8d.png)

#### 观察私服上的`maven-public-jkweilai`

![](../assets/1748420902870-e400f32c-5687-4a53-83ef-2eabaafc5699.png)

![](../assets/1748420929741-9a2aa082-dadd-4a2d-bcf3-00be740c1491.png)

### 使用IDEA部署jar包到Nexus私服

私服Nexus是部署在局域网的，是全公司共享的仓库地址，每个团队都可以将已完成的功能或测试版本发布到私服供别人来使用。

#### 设置部署路径

打开要部署的项目的pom.xml文件，设置上传路径

<distributionManagement>  
    <repository>  
        <id>nexus-jkweilai</id>  
        <url>http://localhost:8081/repository/maven-releases-jkweilai/</url>  
    </repository>  
    <snapshotRepository>  
        <id>nexus-jkweilai</id>  
        <url>http://localhost:8081/repository/maven-snapshots-jkweilai/</url>  
    </snapshotRepository>  
</distributionManagement>

url从这里拿：

![](../assets/1748421233515-e304970b-4f17-449f-9025-51dce69cb788.png)

#### 运行deploy部署命令

![](../assets/1748421306635-f4f8bdd6-4ea8-4796-9a4d-c689d1ed0dd2.png)

#### 观察私服对应仓库变化

- release项目部署
    

![](../assets/1748421447379-5c54fc63-d155-4fec-9c15-68bce03261d0.png)

- snapshot项目部署
    

![](../assets/1748421360744-05870ded-4be1-437f-955c-d298713678fc.png)