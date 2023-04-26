# UDS

2023.4.19

[toc]

> 参考文章：
>
> * https://zhuanlan.zhihu.com/p/37310388
> * https://blog.csdn.net/miracle8510/article/details/94144705

## 背景与缩写

> 每辆汽车都有一个VIN码，每个汽车上有很多ECU，ECU彼此（主要）通过CAN总线连接，总线对外的接口是OBD接口。我们要诊断汽车ECU就需要用到tester-VCI，监测过程使用的协议是UDS。UDS（其中的ISO-14229-1部分）由26种服务组成，每一种服务有自己的SID。
>
> UDS协议是客户端服务器模式的，客户端是tester-VCI，进行请求，服务器是ECU，进行响应。申请的报文时[SID，DID]，DID是数据标识符。响应有肯定与否定两种。如果肯定，返回的第一个字节就是请求的SID+0x50，后边跟着数据。如果否定，返回的就是[0x7F，SID，NRC]，其中NRC是否定响应码。
>
> 如果系统检测到了一个错误，它将存储为DTC。

1. **VIN**：Vehicle Identification Number，车辆识别码

   VIN码（车架号码）是一辆车的唯一身份证明，一般在车辆的挡风玻璃处，有的在车辆防火墙上，或B柱铭牌上。按照国际SAE国际规定，VIN码（车架号）由17位字符组成，其中包含了车辆的生产厂家、年代、车型、车身型式及代码、发动机代码及组装地点等信息。

2. **PIN**

   汽车pin码在发动机的电子防盗系统里。每辆车都会有一个专门的pin码，新车交车时返还给车主，4s店留存一份。

   汽车的pin码由8位字母和数字组成，每一位代表不同的含义，如车型、生产年份、生产序列号等。车辆发动机防盗、故障码清除、车钥匙匹配后期需要，属于车辆识别码。

   汽车pin码的主要作用是防止汽车被盗或防盗转换器损坏。出现故障时，4s店可以根据汽车pin码进行维修。

3. **ECU**：Electronic Control Unit，电子控制单元

   整车上有很多电子控制单元即车载电脑，由微控制器和外围电路组成，每一个都是一个ECU，可以类比成一个个“单片机”。

4. **CAN**：Controller Area Network

   不同的ECU之间使用CAN总线进行通信，CAN总线是一种实时应用的串行通讯协议总线，CAN协议用于汽车中各种不同元件之间的通信，在OSI第一层第二层。

5. **OBD**：On-Board-Diagnose

   OBD是CAN总线对外的接口。

6. **VCI**：Vehicle communication interface，汽车诊断设备

   VCI连接OBD接口，检查汽车信息。

7. **UDS**：Unified Diagnostic Services，统一的诊断服务

   诊断协议是在汽车电子ECU环境下的一种诊断通信协议。ISO 14229也就是UDS协议仅对应用层、会话层做出了定义。诊断方(VCI)向ECU发送请求，ECU回复响应。

8. **PDU**：Protocol Data Unit，协议数据单元

9. **DTC**：Diagnostic Trouble Code，诊断故障码

   如果系统检测到了一个错误，它将存储为DTC。DTC可以揭示错误的位置和错误类型。通常DTC占用3个字节。UDS协议中的19服务是读DTC。

10. **NVM**：Non-Volatile Memory，非易失性存储器

   DTC（故障码）存储在NVM中。UDS-2E服务可以进行清除NVM操作。

11. **SID**：Service Identifier，诊断服务ID

   * UDS的服务包含6大类，共26种。每种服务都有自己独立的ID，即SID。

   * 肯定响应：【SID+0x40】【数据】
   * 否定响应：【0x7F】【SID】【否定响应码NRC】

11. **NRC**：Negative Response Code，否定响应码

    ECU回复响应，如果否定，需要告知原因。

    https://blog.csdn.net/weixin_47890316/article/details/106181730

12. **DID**: Data Identifier，数据标识符

    在很多诊断协议中，比如UDS-22，UDS-2E，DID用来表示该服务的内容。比如SID=0x22是读，DID=0xF190，就是读VIN码。SID=0x2E是写，DID=0xF18C，就是写ECU序列号。

   

## UDS简介

1. UDS寻址
   1. 物理寻址：一对一（VCI - ECU），比如刷写Reflash
   2. 逻辑寻址：一对多（VCI - 多个ECU），比如清除DTC
2. 「10」Diagnostic Session Control：诊断会话
   
   > https://mp.weixin.qq.com/s/K9kdouASyLl11mK5faWE5g
3. 「22」 Read Data By Identifier（通过ID读数据）
4. 「14」 Clear Diagnostic Information（清除诊断信息），「19」 Read DTC Information，「27」 Security Access（安全访问），「2E」 Write Data By Identifier（通过ID写数据），「3E」 Tester Present（待机握手）

![img](https://img-blog.csdnimg.cn/c7a09dc6756447d28936bf4b15eaf4e1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rG96L2m572R57uc6YKj5Lqb5LqL5YS_,size_20,color_FFFFFF,t_70,g_se,x_16)