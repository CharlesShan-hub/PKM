# 计算机网络 

2022.08.14

[TOC]
## 目录与题目类型

图例说明

**加粗：章标题**

[链接：笔记超链接]()

*斜体：题型*



目录

* **总论与周边**
  * [计算机网络概述](./notes/计算机网络体系结构/计算机网络概述.md)
    * *计算机网络性能指标（时延，信道利用率等）*

  * [标准化组织](./notes/计算机网络体系结构/标准化组织.md)
* **计算机网络体系结构**
  * [计算机网络体系结构](./notes/计算机网络体系结构/计算机网络体系结构.md)
    * *功能与计算机网络某一层关系*
  * [主干ISP、地区ISP、本地ISP？](./notes/计算机网络体系结构/主干ISP、地区ISP、本地ISP？.md)
* **物理层**
  * [物理层](./notes/物理层/物理层.md)
    * *四种特性（机电功过）*
    * *数据编码方式*
    * *几个通信公式*
    * *物理层设备(5-4-3原则，是否隔离冲突与广播域)*
* **数据链路层**
  * [数据链路层](./notes/数据链路层/数据链路层.md)
  * [组帧](./notes/数据链路层/组帧.md)
    * *字符计数、字符填充、零比特填充、违规编码*
  * [差错控制](./notes/数据链路层/差错控制.md)
    * *奇偶校验码、CRC、海明码*
  * [流量控制与可靠传输机制](./notes/数据链路层/流量控制.md)
    * *三种协议：停止等待、后退N帧、选择重传*
    * *n种指标：利用率、帧序号比特数、窗口大小、帧长*
  * [介质访问控制](./notes/数据链路层/介质访问控制.md)
    * *静态划分信道：FDM、TDM、STDM、WDM、CDM*
    * *ALOHA：两种ALOHA、计算负载G*
    * *CSMA：三种CSMA*
    * *CSMA/CD：争用期与以太网最大最小帧长、指数退避算法*
    * *CSMA/CA：三种IFS、RTS与CTS*
  * [局域网](./notes/数据链路层/局域网.md)
    * *标准以太网与高速以太网*
    * *以太网MAC帧格式背诵(8662数4)*
    * *无线局域网MAC帧格式背诵(1234，收发目源)*
  * [广域网](./notes/数据链路层/广域网.md)
    * *PPP协议：帧格式、一些性质*
  * [数据链路层设备](./notes/数据链路层/数据链路层设备.md)
    * *交换机*
* **网络层**
  * [网络层的功能](./notes/网络层/网络层的功能.md)
    * *SDN（2022新考点）*
  * [路由算法](./notes/网络层/路由算法.md)
    * *距离向量+RIP、链路状态+OFPS、层次路由+BGP*
  * [IPv4](./notes/网络层/IPv4.md)
    * *IPv4分组：帧格式、分片、传统分类、NAT*
    * *子网与超网：子网划分与子网掩码、CIDR、路由聚合/构成超网*
    * *ARP*
    * *DHCP*
    * *ICMP*
  * [IPv6](./notes/网络层/IPv6.md)
  * [IP组播](./notes/网络层/IP组播.md)
  * [移动IP](./notes/网络层/移动IP.md)
  * [网络层设备](./notes/网络层/网络层设备.md)
* **传输层**
  * [传输层的功能](./notes/传输层/传输层的功能.md)
  * [UDP](./notes/传输层/UDP.md)
  * [TCP](./notes/传输层/TCP.md)
  * [TCP源码分析](https://www.cnblogs.com/RichardTAO/p/12097469.html#%E4%B8%89%E6%AC%A1%E6%8F%A1%E6%89%8B%E8%BF%87%E7%A8%8B)(外链)
* **应用层**
  * [应用层的功能](./notes/应用层/应用层的功能.md)
  * [网络应用模型](./notes/应用层/网络应用模型.md)
  * [域名系统DNS](./notes/应用层/域名系统DNS.md)
  * [文件传输协议FTP](./notes/应用层/文件传输协议FTP.md)
  * [电子邮件E-mail](./notes/应用层/电子邮件E-mail.md)
  * [万维网WWW](./notes/应用层/万维网WWW.md)


## 介绍

计算机网络按照408考研辅导进行梳理。
## 资源
链接: https://pan.baidu.com/s/1M34LB98BsKdHGby2eMC_Qw?1cv1  
提取码: 1cv1  如果资源失效请联系我

* **[网友笔记](https://blog.csdn.net/weixin_45067603/article/details/106974036)**
  * 链接：https://pan.baidu.com/s/16NJVC2-vQu2HcJqb6nJQFw 提取码：djqm
  * [【计算机网络笔记Part1 概述】](https://blog.csdn.net/weixin_45067603/article/details/106974036)
  * [【计算机网络笔记Part2 物理层（Physical Layer）】](https://blog.csdn.net/weixin_45067603/article/details/106974965)
  * [【计算机网络笔记Part3 数据链路层（Data Link Layer）】](https://blog.csdn.net/weixin_45067603/article/details/106980441)
  * [【计算机网络笔记Part4 网络层（Network Layer）】](https://blog.csdn.net/weixin_45067603/article/details/106993253)
  * [【计算机网络笔记Part5 传输层（Transport Layer）】](https://blog.csdn.net/weixin_45067603/article/details/107034202)
  * [【计算机网络笔记Part6 应用层（Application Layer）】](https://blog.csdn.net/weixin_45067603/article/details/107053479)




* __2023王道计算机网络资料__ : 2023王道配套视频与习题解答

  标注*的暂未收录

  1. *2023计算机网络知识点
  2. *2022计算机网络知识点课件
  3. *2023计算机网络知识点习题讲解
  4. *2023计算机网络知识点思维导图
  5. *2023计算机网络强化直播
  6. *2023计算机网络考研真题讲解
  7. 2023王道计算机网络.pdf（课本）
  8. *2023计算机网络新增考点补充文档.pdf
  9. *23版计算机网络勘误.pdf
  10. *408真题原题与解析



* __2022王道计算机网络资料__ : 2022王道配套视频与习题解答

  1. 2022计算机网络知识点
  2. 2022计算机网络知识点课件
  3. 2022计算机网络知识点习题讲解
  4. 2022计算机网络知识点思维导图
  5. 2022计算机网络强化直播
  6. 2022计算机网络考研真题讲解
  7. 2022王道计算机网络.pdf（课本）
  8. 2022计算机网络新增考点补充文档.pdf
  9. 22版计算机网络勘误.pdf
  10. 408真题原题与解析



* __2022天勤计算机网络.pdf__: 2022年408考研辅导教材  



* [**计算机网络（第7版）谢希仁**](http://yx.51zhy.cn/mtrcsRes/phei_cnetwork.jsp)：考研标准教材

  1. 计算机网络（第7版）-谢希仁.pdf
  2. 计算机网络（第7版）-谢希仁-课件

  

* __计算机网络(自顶向下)__: 国际经典教材

  1. Computer Networking A Top-Down Approach, 7th Edition by James Kurose, Keith Ross.pdf
  2. 中文计算机网络.pdf（翻译）
  2. 中国教材答案
  2. 英文教材答案

  

* __TCP/IP详解__：国际经典著作

  卷1:原理
  卷2:实现
  卷3:扩展

  

* **计算机网络其他书籍**

  * tcp源码分析.pdf
  * HTTP权威指南（中文版）.pdf
  * 图解网络（公众号）
  * 图解TCPIP（第5版） (竹下隆史, 村山公保, 荒井透, 苅田幸雄) 

  

* __CSAM协议族__

  1191044A_scan.pdf

  

* **计算机网络实验课程与工具**

  1. ns3: https://www.nsnam.org/
  	* （官方教程）ns-3-tutorial.pdf
  	
  2. nse教程
  	* 如何学习ns3: https://blog.csdn.net/Mary19920410/article/details/72520674
  	* NS3官网（Tutorial, Manual, ns-3: ns-3 Documentation, ns-3 Model Library）https://www.nsnam.org/
  	* NS3 Google论坛： http://groups.google.com/forum/#!forum/ns-3-users
  	* 大牛的博客等： zhua0404.blogspot.com/s， ns-3 | Luiz Felipe Perrone，
  	* NS3 Project网址： ns3simulation.com/
  	
  3. Cisco Packet Tracer - 需要注册账户（免费）
  	* Packet Tracer软件：https://www.packettracernetwork.com/download/download-packet-tracer.html
  	* Cisco官方课程：https://www.netacad.com/courses/all-courses
  	
  4. 计算机网络实验（计算机网络 思科Cisco Packet Tracer仿真实验-哔哩哔哩）：https://b23.tv/WbUfNDR

  5. 计算机网络实验教程 计算机网络实验教程 by （美）Emad Aboelela.pdf

  6. Wireshark网络分析就这么简单.pdf

     

* [计算机网络顶会链接](https://blog.csdn.net/niutianzhuang/article/details/79995929)

  |                             简称                             |                           会议全称                           | 出版社 |
  | :----------------------------------------------------------: | :----------------------------------------------------------: | :----: |
  |     [MOBICOM](http://dblp.uni-trier.de/db/conf/mobicom/)     | ACM International Conference on Mobile Computing and Networking |  ACM   |
  | [SIGCOMM](http://dblp.uni-trier.de/db/conf/sigcomm/index.html) | ACM International Conference on the applications, technologies, architectures, and protocols for computer communication |  ACM   |
  |     [INFOCOM](http://dblp.uni-trier.de/db/conf/infocom/)     |   IEEE International Conference on Computer Communications   |  IEEE  |

  

## 版本

* **V1 2021.8.24**

  按照《2022年计算机网络考研复习指导》与相关课程进行整理，完成全部知识框架搭建  

* **V2 2021.11.23**

  按照2022年408考纲，《2022年计算机网络考研复习指导》与相关课程进行整理，进行习题归纳与知识整合  

* **V3 2022.3.17**

  按照《2023年计算机网络考研复习指导》和《计算机网络（第7版）》-谢希仁，进一步完善，增加了文档式专题笔记
