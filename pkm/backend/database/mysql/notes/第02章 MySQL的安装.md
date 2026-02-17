# MySQL安装

---
## MySQL概述

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1619752945028-dbcb73aa-50e2-4b1c-947d-21da8d742e6d.png#averageHue=%23fef8f1&height=138&id=feuEs&originHeight=138&originWidth=209&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7176&status=done&style=shadow&title=&width=209)

- MySQL是一个关系型数据库管理系统，由瑞典MySQL AB公司开发，MySQL AB公司被Sun公司收购，Sun公司又被Oracle公司收购，目前属于Oracle公司。
- MySQL是目前最流行的关系型数据库管理系统，在WEB应用方面MySQL是最好的RDBMS应用软件之一。 国内淘宝网站就使用的是MySQL集群。
- MySQL特点
   - MySQL有开源版本和收费版本，你使用开源版本是不收费的。
   - MySQL支持大型数据库，可以处理上千万记录的大型数据库。
   - MySQL使用标准的SQL数据库语言形式。
   - MySQL在很多系统上面都支持。
   - MySQL对Java，C都有很好的支持，当然其他的语言也支持比如Python、PHP。
   - MySQL是可以定制的，采用了GPL协议，你可以修改源码来开发自己的MySQL系统。

---
## MySQL的下载

### 官网下载

- 第一步：打开MySQL官网[https://www.mysql.com/](https://www.mysql.com/)

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1619753207824-f47a5a2c-3ee1-4d73-881d-be1bb67a8019.png#averageHue=%23f7f9e1&height=414&id=LIcyu&originHeight=990&originWidth=1875&originalType=binary&ratio=1&rotation=0&showTitle=false&size=521061&status=done&style=shadow&title=&width=784)

- 第二步：点击"DOWNLOADS"

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1619754075151-2e1900d9-0ee0-4905-b3dc-97b5598061f1.png#averageHue=%239ca199&height=196&id=XJGNj&originHeight=392&originWidth=1073&originalType=binary&ratio=1&rotation=0&showTitle=false&size=67160&status=done&style=shadow&title=&width=536.5)

- 第三步：当前页继续下拉，直到找到下图链接

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1619754206255-ee47b52c-e183-4401-a8e7-7b0e51452a00.png#averageHue=%23fdfbfa&height=177&id=NI75H&originHeight=353&originWidth=966&originalType=binary&ratio=1&rotation=0&showTitle=false&size=43043&status=done&style=shadow&title=&width=483)

- 第四步：点击上图链接，进入下面页面，其中“MySQL Community Server”是解压版mysql，“MySQL Installer for Windows”是安装版，这里我们选择解压版

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1619754239811-b4151058-268c-406b-bcd3-72a6d5771e4b.png#averageHue=%23fefefd&height=336&id=za1XY&originHeight=672&originWidth=1035&originalType=binary&ratio=1&rotation=0&showTitle=false&size=89127&status=done&style=shadow&title=&width=517.5)

- 第五步：点击上图“MySQL Community Server”

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620375449949-470a5fb1-8af6-4130-a424-129b8961cb8c.png#averageHue=%23d8e6c3&height=354&id=c5iWO&originHeight=707&originWidth=1228&originalType=binary&ratio=1&rotation=0&showTitle=false&size=154716&status=done&style=shadow&title=&width=614)

- 第六步：点击上图第1个“Download”

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1619754349149-75c6289e-0461-4c82-bf0b-388471535683.png#averageHue=%23fafaf9&height=395&id=loI9w&originHeight=789&originWidth=1001&originalType=binary&ratio=1&rotation=0&showTitle=false&size=102325&status=done&style=shadow&title=&width=500.5)

- 第七步：点击上图“No thanks, just start my download.”开始下载，直到下载完毕。

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620375547996-62d248ee-f33d-41a5-ba14-50cf38405d9b.png#averageHue=%23f6f2ed&height=33&id=H39JS&originHeight=33&originWidth=245&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2768&status=done&style=shadow&title=&width=245)
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=nc7GP&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)
### 网盘下载
链接：[https://pan.baidu.com/s/1lRWC069K8GE-8rxr259ArQ?pwd=2009](https://pan.baidu.com/s/1lRWC069K8GE-8rxr259ArQ?pwd=2009) 提取码：2009

---
## MySQL安装与配置

- 将下载的zip压缩包解压，我这里直接解压到C盘的根目录下

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620375547996-62d248ee-f33d-41a5-ba14-50cf38405d9b.png#averageHue=%23f6f2ed&height=33&id=PdFDW&originHeight=33&originWidth=245&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2768&status=done&style=shadow&title=&width=245)
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620376986790-01106d3e-b89f-453a-98cb-f2a86d4b2544.png#averageHue=%23f6f1ef&height=205&id=VR5Fm&originHeight=205&originWidth=305&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10933&status=done&style=shadow&title=&width=305)
mysql的根目录为：C:\mysql-8.0.24-winx64

- 将C:\mysql-8.0.24-winx64\bin目录配置到环境变量path当中

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620377142769-f797dd2c-4f82-4c8f-b5a2-d97bfbe52225.png#averageHue=%23f5f4f4&height=551&id=wovpn&originHeight=551&originWidth=515&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23226&status=done&style=shadow&title=&width=515)

- 初始化data目录

使用管理员身份打开dos命令窗口（按win键，输入cmd，点击管理员身份运行）
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620377404683-4ed7c1d7-c8f1-44a3-ae32-0005183fcd09.png#averageHue=%23e3e3e3&height=635&id=enGFN&originHeight=635&originWidth=779&originalType=binary&ratio=1&rotation=0&showTitle=false&size=55630&status=done&style=shadow&title=&width=779)
cd命令切换到mysql的bin目录下，执行mysqld --initialize --console进行data目录初始化，此时会在控制台生成一个随机密码，下图红框中就是随机密码
![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620379266865-b043168d-8825-44e9-99ab-35ce6f8c8e25.png#averageHue=%232d2d2d&height=298&id=RFgFN&originHeight=298&originWidth=1034&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28139&status=done&style=shadow&title=&width=1034)
技巧：左键选中密码，直接点击右键，此时密码已经复制到剪贴板中了，
然后随便找一个文件，将密码粘贴到文件中保存起来。

- 安装MySQL服务：cd命令切换到bin目录下，执行命令mysqld -install

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620379567159-f63f3527-3ba9-48fe-8a19-57e4c3767662.png#averageHue=%23181818&height=61&id=RZu5G&originHeight=61&originWidth=352&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2866&status=done&style=shadow&title=&width=352)

- 查看mysql服务名称：此电脑-右键-管理-服务和应用程序-服务-找MySQL服务，如下图mysql服务名称：MySQL

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620379678662-4b14e7a5-d17c-4c2b-917d-cc4d73b94ae5.png#averageHue=%23f6f4f2&height=521&id=P0jsU&originHeight=695&originWidth=796&originalType=binary&ratio=1&rotation=0&showTitle=false&size=117316&status=done&style=shadow&title=&width=597)

- 启动MySQL服务：net start mysql，注意start后面是mysql服务的名称

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620379806288-826de76c-2827-419e-ab16-b6fc72afdbca.png#averageHue=%231c1c1c&height=69&id=JLnqX&originHeight=69&originWidth=353&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3632&status=done&style=shadow&title=&width=353)
停止mysql服务的命令：net stop mysql
注意：启停mysql服务也可以在上一步的图中点击右键进行启停服务。

- 登录mysql：输入mysql -uroot -p，然后回车，输入刚才的随机密码，然后回车，看到下图表示成功登录mysql

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620379936249-1bfaef7c-9ca7-4ddd-978a-b518acd834b0.png#averageHue=%23141313&height=305&id=EiQKK&originHeight=305&originWidth=649&originalType=binary&ratio=1&rotation=0&showTitle=false&size=17739&status=done&style=shadow&title=&width=649)

- 修改MySQL的root账户密码：ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '新密码';

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620382836782-5a7fef8d-15ce-4dca-a5d0-831b6f60f56e.png#averageHue=%23282828&height=293&id=dVHAz&originHeight=293&originWidth=760&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18567&status=done&style=shadow&title=&width=760)

- 使用新密码登录mysql

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620382883258-875c0c1a-00c7-40f8-a8dd-edb1d39e94e0.png#averageHue=%232a2a2a&height=310&id=WAkW8&originHeight=310&originWidth=687&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21698&status=done&style=shadow&title=&width=687)

---
## MySQL卸载

- 停止mysql的服务

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620383089030-497a3bfc-74d5-43a6-9689-8f9e0b24dd73.png#averageHue=%231a1a1a&height=74&id=pHyXZ&originHeight=74&originWidth=362&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3592&status=done&style=shadow&title=&width=362)

- 删除mysql服务

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620383158420-3d5117c6-0c0f-421c-9570-407dac8c6612.png#averageHue=%23171717&height=58&id=OrAHb&originHeight=58&originWidth=407&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2850&status=done&style=shadow&title=&width=407)

- 删除mysql的目录

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620383199727-89d46dc3-b4cf-4883-9a18-b0ee0c0fe6e8.png#averageHue=%23faf4f2&height=207&id=A4FLD&originHeight=207&originWidth=343&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12988&status=done&style=shadow&title=&width=343)

---
## 登录MySQL

### 本地登录

- 如果mysql的服务是启动的，打开dos命令窗口，输入：mysql -uroot -p，回车，然后输入root账户的密码

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620389190451-81319065-6d04-4094-97d0-13236236ad32.png#averageHue=%231c1b1a&height=414&id=EMVUZ&originHeight=552&originWidth=1067&originalType=binary&ratio=1&rotation=0&showTitle=false&size=51645&status=done&style=shadow&title=&width=800)
解释“mysql -uroot -p”：
mysql是一个命令，在bin目录下，对应的命令文件是mysql.exe，如果将bin目录配置到环境
变量path中，才可以在以上位置使用该命令。
-uroot 表示登录的用户是root，u实际上是user单词的首字母。
-p 表示登录时使用密码，p实际上是password单词的首字母。

- 也可以将密码以明文的形式写到-p后面，这样做可能会导致你的密码泄露

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620389582655-74210644-318a-4e71-a242-192d61ef9fd9.png#averageHue=%231d1b1a&height=355&id=AthqC&originHeight=473&originWidth=1006&originalType=binary&ratio=1&rotation=0&showTitle=false&size=52443&status=done&style=shadow&title=&width=755)

### 远程登录

- 假设mysql安装在A机器上，现在你要在B机器上连接mysql数据库，此时需要使用远程登录，远程登录时加上远程机器的ip地址即可

![image.png](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620389951870-e1585ee0-d1cd-4b89-973b-b3e6c4a20539.png#averageHue=%23211f1e&height=330&id=Zncdu&originHeight=440&originWidth=994&originalType=binary&ratio=1&rotation=0&showTitle=false&size=52747&status=done&style=shadow&title=&width=746)
-h中的h实际上是host单词的首字母。在-h后面的是远程计算机的ip地址。
127.0.0.1是计算机默认的本机IP地址。
127.0.0.1又可以写作：localhost，他们是等效的。
注意：mysql默认情况下root账户是不支持远程登录的，其实这是一种安全策略，
为了保护root账户的安全。如果希望root账户支持远程登录，这是需要进行设置的。

- mysql8 开放root账户远程登录权限（危险动作）

  第一步：现在本地使用root账户登录mysql

  第二步：use mysql;

  第三步：update user set host = '%' where user = 'root';

  第四步：flush privileges;
