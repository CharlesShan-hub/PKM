# 直接使用地址也可以，使用名字也可以。配置文件中的名字叫做：origin

git push origin  

```

你会发现因为权限不足而导致推送失败。

### 解决权限不足问题

**第一步：**执行以下命令生成 SSH 安全证书（生成公钥文件）

```shell

ssh-keygen -t rsa -Cgit@gitee.com:du-jubin/remote-gitee-test.git

```

询问你保存位置：一路回车即可。

**第二步：**找到这个公钥，默认位置在：`用户主目录\.ssh\id_rsa.pub`，打开这个文件

```plain

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCqKHFj6S2UDdd7/+dToSSpGhTbiag2rGidwnNsGfLeWrbZFfa7LnL6S82ofFtMP52xjplCw6E7tP6199T+bx2VrPvzFqozHtzAz7gZrLJmItlFrVbyqmrpDHJbg37YYNsOGvobMkMf0NB1s/Agzql9fg6YxBX+jBMdprTFtsDgxGx1V4Zu9GzW1Pi42ExUBDxq75/92Gfo2jkxRrSwhwszkqx4L08ZYFEsRScFscLobhs/szkbasxHjFl8pbQ7ysAfq5d/KfDwucoU+MlnZWZUbRAq6B+uHrJJZkeB+c3lsl4PXY5ln9/lCKwzUIVEjJlzdOY6L8zkmbBGgDlPJ1XGG1dxM3MIlufwa+gsYmK3N/xDTyQnO+1/eN9APSEz/HW1jPXtF+6lErB2Aoq5slfIBrpeGzeLA75PGVOgQJ46xnHyjrXYezdCi9dCBIWcYSzcuYW5idN+U/tnGiyF4yygXIPmV01aun2kwqp06dh3FgKhalOzzsqAiiNek+FJtsM= git@gitee.com:du-jubin/remote-gitee-test.git

```

**第三步：**把这个文件中的公钥复制一下，打开 gitee 的后台，找到 SSH 公钥位置，添加公钥并保存。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766977034481-0e748596-1609-4e0e-a69a-f56c1de39d30.png" width="156.8" title="" crop="0,0,1,1" id="u369e1ab7" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766977048738-70c02506-1925-4f33-bbc6-985691c81255.png" width="219.2" title="" crop="0,0,1,1" id="u0a8d39f9" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1766977080465-fde58f04-4b64-46e3-80a4-6fc95c52951c.png" width="820" title="" crop="0,0,1,1" id="ua2112233" class="ne-image">

### 再次推送

```shell

git push origin

```

查看远程仓库内容是否更新。

### 拉取合并

远程仓库中的文件修改一下，然后通过以下命令将远程仓库中的数据拉取到本地并进行自动合并：

```shell

git pull origin

```

