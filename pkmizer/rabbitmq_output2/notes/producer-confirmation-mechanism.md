80b1-05b8cfd064c6.png" width="264" title="" crop="0,0,1,1" id="u13c2cf2f" class="ne-image">

这个机制是用来确认**<font style="color:rgb(15, 17, 21);">消息是否成功到达 RabbitMQ（Broker）</font>**

**<font style="color:rgb(15, 17, 21);">生产者发送消息后，Broker会异步返回一个确认信号，确保</font>****<font style="color:#DF2A3F;">消息已收到并持久化到磁盘</font>****<font style="color:rgb(15, 17, 21);">，从而实现可靠的消息投递。</font>**

**<font style="color:rgb(15, 17, 21);">解决了什么问题？</font>**<font style="color:rgb(15, 17, 21);"> 防止消息在传输过程中（Broker接收后、存盘前）因服务器宕机而丢失。</font>

**<font style="color:rgb(15, 17, 21);">典型场景？</font>**<font style="color:rgb(15, 17, 21);"> 用在金融交易、订单处理等不允许消息丢失的业务中。</font>

<font style="color:rgb(15, 17, 21);"></font>

# <font style="color:rgb(15, 17, 21);">SpringBoot 整合 RabbitMQ</font>
开发中最常用的是基于路由模式。因此我们就基于路由模式来编写代码：

## 创建<font style="color:#DF2A3F;">消费端</font> SpringBoot 项目引入依赖
我们使用的 SpringBoot 的版本 `3.5.8`，引入以下依赖：

```xml
<dependencies>
    <!--RabbitMQ的客户端程序-->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-amqp</artifactId>
    </dependency>
    <!--引入它的目的是让消费端启动之后不关闭。这样可以对RabbitMQ的队列进行不停的监听。-->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <!--方便开发-->
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <optional>true</optional>
    </dependency>
</dependencies>
```

## 编写消费端 yml 配置文件
```yaml
spring:
  rabbitmq:
    host: localhost
    port: 5672
    username: admin
    password: 123456
    virtual-host: /
logging:
  lev