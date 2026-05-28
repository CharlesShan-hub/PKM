# OAuth2
## OAuth2 简介
### OAuth2 是什么
“Auth” 表示 “授权” Authorization

“O” 是 Open 的简称，表示 “开放”

“2”是版本号

连在一起就表示 **“开放授权”**，OAuth2 是一种**开放授权协议**。

### 用 OAuth2 完成什么功能
用 OAuth2 能完成这样的功能：你在京东商城登录页上使用微信扫一扫授权登录。使用流程是这样的：

**第一步：打开京东商城登录页，点击微信登录**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759392453624-b62c8a59-135f-409e-adab-d46b5cf5a434.png" width="681.3333333333334" title="" crop="0,0,1,1" id="u893a893e" class="ne-image" style="font-size: 16px">

**第二步：拿起手机扫一扫**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759392556739-260e31cf-907b-41f9-b8e3-2abb7a9c44a1.png" width="361.77777777777777" title="" crop="0,0,1,1" id="u10e3b930" class="ne-image" style="font-size: 16px">

**第三步：手机上点击允许（当然，也可以拒绝）**

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1759392733907-33594c9c-a977-4014-a138-4ea6c84d526e.jpeg" width="232" title="" crop="0,0,1,1" id="u815308a6" class="ne-image" style="font-size: 16px">

你点击允许之后，**授权服务器** 会颁发一个**令牌**给京东商城。



**第四步：京东商城登录成功。**

京东拿到授权服务器颁发的令牌之后，将令牌发给资源服务器，资源服务器判断你的令牌是否有效，如果令牌有效会将微信的昵称和头像等信息发送给京东商城，京东商城根据这些信息去数据库中查找该信息绑定的京东账号，然后登录成功。

### OAuth2 的角色
**OAuth 2 协议包含以下角色：**

1. 资源所有者（Resource Owner）
2. 客户应用（Client）
3. 授权服务器（Authorization Server）
4. 资源服务器（Resource Server）



初次接触四个角色肯定比较懵，我们把 4 个角色代入到京东扫码登录的例子中，你会秒懂：

1. **<font style="color:rgb(15, 17, 21);">你（资源所有者）</font>**<font style="color:rgb(15, 17, 21);"> </font><font style="color:rgb(15, 17, 21);">在</font>**<font style="color:rgb(15, 17, 21);">电脑京东（客户应用）</font>**<font style="color:rgb(15, 17, 21);"> </font><font style="color:rgb(15, 17, 21);">点击微信登录，出现二维码。</font>
2. <font style="color:rgb(15, 17, 21);">你用手机微信扫二维码，实际上是跳转到了</font>**<font style="color:rgb(15, 17, 21);">微信的授权页面（授权服务器）</font>**<font style="color:rgb(15, 17, 21);">。</font>
3. **<font style="color:rgb(15, 17, 21);">微信授权服务器</font>**<font style="color:rgb(15, 17, 21);">问你：“同意京东使用你的信息吗？”你点击</font>**<font style="color:rgb(15, 17, 21);">同意</font>**<font style="color:rgb(15, 17, 21);">。</font>
4. <font style="color:rgb(15, 17, 21);">微信授权服务器告诉京东：“用户同意了，这是凭证。”</font>
5. <font style="color:rgb(15, 17, 21);">京东拿着凭证，去找</font>**<font style="color:rgb(15, 17, 21);">微信的资源服务器</font>**<font style="color:rgb(15, 17, 21);">说：“我有凭证，把扫码用户的昵称头像给我。”</font>
6. **<font style="color:rgb(15, 17, 21);">微信资源服务器</font>**<font style="color:rgb(15, 17, 21);">验证凭证有效，就把你的基本信息发给京东。</font>
7. <font style="color:rgb(15, 17, 21);">京东根据你的微信信息，找到对应的京东账号，让你成功登录。</font>



**<font style="color:#DF2A3F;">OAuth2.0 到底是什么？</font>**

**<font style="color:rgb(15, 17, 21);">OAuth 2.0 是一个授权标准，它定义了一套规范，允许第三方应用（</font>****<font style="color:#DF2A3F;">京东</font>****<font style="color:rgb(15, 17, 21);">）在用户授权的前提下，安全地访问用户在另一个服务商</font>****<font style="color:#DF2A3F;">（微信服务器）</font>****<font style="color:rgb(15, 17, 21);">存储的资源，而无需获取用户的密码</font>****<font style="color:#DF2A3F;">（不需要获取用户的微信密码）</font>****<font style="color:rgb(15, 17, 21);">。</font>**<img src="assets/image-20231222124053994.png" title="null" crop="0,0,1,1" id="thHtP" class="ne-image" style="font-size: 16px">



### OAuth2 的使用场景
#### 场景一：第三方登录（**一键登录**）
+ 在知乎上，你不想重新注册账号，而是点击“微信登录”按钮。
+ 知乎把你 redirect 到微信。
+ 你在微信那里输入密码（信息只交给微信，知乎看不到），并同意授权。
+ 微信告诉知乎：“验明正身了，这是他自己”。
+ 知乎就用这个信息给你创建一个账号或让你登录。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759396501063-ca06961d-879f-460d-8956-a681a7185021.png" width="748" title="" crop="0,0,1,1" id="u5a5d9d9d" class="ne-image" style="font-size: 16px">

#### 场景二：第三方数据授权（**允许APP读取你的数据**）
+ 假设你在用一个“旅行规划APP”，它要读取你“百度网盘”里存的旅行照片。
+ 旅行APP向百度网盘请求访问照片的权限。
+ 你在百度网盘的授权页点击“同意”。
+ 百度网盘给旅行APP一个令牌。
+ 旅行APP之后就可以用这个令牌，在不问你密码的情况下，从百度网盘拉取你的照片。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759396660468-6b87630c-8162-4070-a678-79f18c95b2c4.png" width="888.4444444444445" title="" crop="0,0,1,1" id="u1f023751" class="ne-image" style="font-size: 16px">

#### 场景三：服务器对服务器（微服务之间）的授权
+ 你在京东下单时，它的“订单服务”需要去调用“库存服务”来扣减库存。
+ “订单服务”向一个中央的“授权服务器”申请令牌。
+ 授权服务器验证“订单服务”的身份后，发给它一个令牌。
+ “订单服务”拿着这个令牌去调用“库存服务”。
+ “库存服务”验证令牌有效后，执行扣减库存操作。
+ **<font style="color:#DF2A3F;">为什么用</font>**：在复杂的微服务系统中，确保服务之间的调用是合法、受控的，防止内部服务被恶意调用。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759396757268-6451b1f3-af3a-4179-a327-ad44ae54163a.png" width="557.7777777777778" title="" crop="0,0,1,1" id="u2f9c32e1" class="ne-image" style="font-size: 16px">

****

**总结一句话：**

凡是需要 **A应用** 在 **不碰你B服务密码** 的前提下，去 **代表你** 访问你在 **B服务** 的资源或身份，就是用了 `OAuth 2.0`。

### OAuth2 的四种授权模式
OAuth2 提供了四种授权模式：

+ 授权码模式（authorization-code）
+ 隐式模式（implicit）**OAuth2.1 中已废弃**
+ 密码模式（password）**不推荐**
+ 客户端凭证模式（client credentials）

#### 授权码模式
这是**最常见、最安全**的模式。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759406030175-ba2ff046-aed1-4119-bc4d-558ca1de7896.png" width="783.5555555555555" title="" crop="0,0,1,1" id="ud1f18d0f" class="ne-image" style="font-size: 16px">

**核心关键流程描述**：用户确认授权后（用户扫码点了确认），**授权服务器**生成授权码，**授权服务器**保留一份授权码，并将授权码响应给**客户应用**（此授权码虽然在浏览器上传输，可能会被黑客拿到，但拿到也没有关系），然后**客户应用**会使用自己的**后端服务器**调用**授权服务器**提供的 API 接口，通过该接口提交**客户端秘钥+授权码**，**授权服务器**验证**客户端秘钥和授权码**，如果没问题，**授权服务器**生成**令牌**，将令牌响应给**客户应用的后端服务器**，**客户应用的后端服务器**将令牌保存下来。



什么是**客户端秘钥**，理解它非常关键：假设**客户应用**是知乎，**授权服务器**是微信平台，**客户端秘钥**是当时知乎留给微信平台的“营业执照”，一串高度绝密的字符串，只有知乎平台它自己有，黑客是不知道的，**客户端秘钥**是通过后端服务器提交给微信平台的。因此即使黑客拿到授权码，也没有关系，因为只有授权码，**授权服务器**是不会颁发令牌的。**<font style="color:#DF2A3F;">（客户端秘钥如何获取？知乎平台（客户应用）的开发者在开发的时候需要向微信平台（授权服务器）申请客户端秘钥 ClientSecret，另外，向微信平台申请客户端秘钥的不止有知乎，可能还会有其他平台，因此授权服务器会给每个客户应用再分配一个 ClientId，当客户应用向授权服务器发送请求时，也会携带这个 clientId，这样授权服务器很快就可以通过 clientId 找到当时保存在授权服务器中的客户端秘钥，然后拿着这个客户端秘钥和客户应用提交的客户端秘钥进行比对。）</font>**



举个例子：比如你中奖了，领奖环节安排在公共场合下不安全（令牌直接走浏览器不安全），所以颁奖方会给你一个兑奖券（授权码），然后告诉你带上你的身份证（客户端秘钥）和兑奖券（授权码）到安全的地方领奖。但你可能会有疑问：那如果兑奖券被**张三**偷走了，张三同样也可以拿着自己的身份证和兑奖券去兑奖呀！那是不可能的，因为张三的身份证并没有在颁奖方登记（颁奖方不认张三）。



**ClientId 与 redirect_uri：**

另外，我们再来看看，当我们在京东登录页，点击了微信登录，浏览器地址栏上的地址是怎样的？

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759412747427-46be2d4d-ca55-47a5-8289-46de36854518.png" width="364" title="" crop="0,0,1,1" id="u80ef8aa0" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759412773409-ecf8d51c-0ee5-4e46-82ed-4230e674dd05.png" width="500.8888888888889" title="" crop="0,0,1,1" id="u341a5c2b" class="ne-image" style="font-size: 16px">

我把地址拷贝下来了，大家可以看一下：

```plain
https://open.weixin.qq.com/connect/qrconnect?
appid=wx827225356b689e24
&
state=BEB28B99624523F6BFFBAC8EF6AF0CB2687B22DB8A3C59C2024746E209555ADE8E82DB14D7B0853546CF0465FB3E2A19
&
redirect_uri=https%3A%2F%2Fqq.jd.com%2Fnew%2Fwx%2Fcallback.action%3F%26uuid%3D72200605386c4eb99624c883e76f37a7
&
response_type=code
&
scope=snsapi_login#wechat_redirect
```

其中有一个 `appid`，还有一个 `redirect_uri`：

+ `**<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">appid</font>**`**<font style="color:rgb(15, 17, 21);"> </font>****<font style="color:rgb(15, 17, 21);">(wx827225356b689e24)</font>**<font style="color:rgb(15, 17, 21);">：就是</font><font style="color:rgb(15, 17, 21);"> </font>`**<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">client_id</font>**`<font style="color:rgb(15, 17, 21);">。这是京东应用在微信开放平台注册后获得的</font>**<font style="color:rgb(15, 17, 21);">公开身份标识</font>**<font style="color:rgb(15, 17, 21);">，用于告诉微信“是哪个应用在请求登录”。</font>
+ `**<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">redirect_uri</font>**`<font style="color:rgb(15, 17, 21);">：这是一个回调 URL，将来授权服务器要通过调用这个 URL 给京东传 </font>**<font style="color:rgb(15, 17, 21);">授权码</font>**<font style="color:rgb(15, 17, 21);">。</font>

#### 隐式模式
隐式模式的核心问题，是它完全跳过了“授权码”这个中间环节。隐藏了这个环节。以前的纯前端应用经常会使用这种方式，因为纯前端应用没有后端，传不了客户端秘钥。

这个模式**已被OAuth 2.1最佳实践指南明确废弃**。

+ **流程**：与授权码模式类似，但授权服务器直接在前端重定向的URL片段中返回**访问令牌**，不经过授权码这一步。
+ **缺点**：令牌直接暴露在浏览器和URL中，有很高的安全风险。只能用于一些安全要求不高的场景，并且令牌的有效期必须非常短，通常就是会话期间有效，浏览器关掉，令牌就失效了。
+ **现状**：**已过时**。纯前端应用 的替代方案：**授权码模式 + PKCE扩展**。

#### 密码模式
用户直接将用户名和密码交给客户端应用，客户端应用再用这些信息去换取令牌。

+ **缺点**：**极不安全**。用户需要完全信任客户端应用，违背了OAuth“第三方授权”的初衷。会将用户的凭证暴露给第三方应用。
+ **适用场景**：仅适用于**高度信任的环境**，例如自家公司内部的应用。**绝不适用于普通的第三方应用**。

#### 客户端凭证模式
这种模式用于**机器对机器的认证**，没有用户的参与。

+ **流程**：客户端应用使用自己的客户端ID和客户端密钥，直接向授权服务器请求一个访问令牌。
+ **适用场景**：微服务之间的API调用。

#### 补充：授权码模式 + PKCE
**<font style="color:rgb(15, 17, 21);">PKCE 的作用就像客户端秘钥一样。</font>**

<font style="color:rgb(15, 17, 21);">对比：传统客户端密钥 vs. PKCE</font>

| **<font style="color:rgb(15, 17, 21);">特性</font>** | **<font style="color:rgb(15, 17, 21);">传统客户端密钥</font>** | **<font style="color:rgb(15, 17, 21);">PKCE (code_verifier)</font>** |
| --- | --- | --- |
| **<font style="color:rgb(15, 17, 21);">本质</font>** | <font style="color:rgb(15, 17, 21);">一个</font>**<font style="color:rgb(15, 17, 21);">长期的、固定的</font>**<font style="color:rgb(15, 17, 21);">秘密字符串</font> | <font style="color:rgb(15, 17, 21);">一个</font>**<font style="color:rgb(15, 17, 21);">临时的、一次性的</font>**<font style="color:rgb(15, 17, 21);">随机字符串</font> |
| **<font style="color:rgb(15, 17, 21);">适用对象</font>** | <font style="color:rgb(15, 17, 21);">有</font>**<font style="color:rgb(15, 17, 21);">后端服务器</font>**<font style="color:rgb(15, 17, 21);">的Web应用</font> | **<font style="color:rgb(15, 17, 21);">纯前端应用</font>**<font style="color:rgb(15, 17, 21);"></font> |
| **<font style="color:rgb(15, 17, 21);">存储位置</font>** | **<font style="color:rgb(15, 17, 21);">安全的后端服务器</font>**<font style="color:rgb(15, 17, 21);"></font> | **<font style="color:rgb(15, 17, 21);">前端内存</font>**<font style="color:rgb(15, 17, 21);">中生成和使用（用后即弃）</font> |
| **<font style="color:rgb(15, 17, 21);">验证方式</font>** | <font style="color:rgb(15, 17, 21);">授权服务器对比它</font>**<font style="color:rgb(15, 17, 21);">数据库里存储的</font>**<font style="color:rgb(15, 17, 21);">固定密钥</font> | <font style="color:rgb(15, 17, 21);">授权服务器对比它</font>**<font style="color:rgb(15, 17, 21);">本次会话中暂存的</font>**<font style="color:rgb(15, 17, 21);"> </font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">code_challenge</font>`<font style="color:rgb(15, 17, 21);">的哈希值</font> |


**<font style="color:rgb(15, 17, 21);"></font>**

**<font style="color:rgb(15, 17, 21);">授权码模式+PKCE 流程是这样的：</font>**

1. <font style="color:rgb(15, 17, 21);">用户访问应用，应用在</font>**<font style="color:rgb(15, 17, 21);">本地</font>**<font style="color:rgb(15, 17, 21);">生成一个随机的</font><font style="color:rgb(15, 17, 21);"> </font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">code_verifier</font>`<font style="color:rgb(15, 17, 21);">（比如是字符串</font><font style="color:rgb(15, 17, 21);"> </font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">"my_secret_123"</font>`<font style="color:rgb(15, 17, 21);">），并计算出对应的</font><font style="color:rgb(15, 17, 21);"> </font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">code_challenge</font>`<font style="color:rgb(15, 17, 21);">（比如是</font><font style="color:rgb(15, 17, 21);"> </font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">"abc123hash"</font>`<font style="color:rgb(15, 17, 21);">）。</font>
2. <font style="color:rgb(15, 17, 21);">应用带着 </font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">code_challenge</font>`<font style="color:rgb(15, 17, 21);"> 去向授权服务器申请授权码。</font>
3. <font style="color:rgb(15, 17, 21);">用户登录并授权，授权服务器返回一个</font>**<font style="color:rgb(15, 17, 21);">授权码</font>**<font style="color:rgb(15, 17, 21);">。</font>
4. <font style="color:rgb(15, 17, 21);">应用用这个</font>**<font style="color:rgb(15, 17, 21);">授权码</font>**<font style="color:rgb(15, 17, 21);"> + </font>**<font style="color:rgb(15, 17, 21);">原始的 </font>**`**<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">code_verifier</font>**`**<font style="color:rgb(15, 17, 21);"> ("my_secret_123")</font>**<font style="color:rgb(15, 17, 21);"> 去兑换令牌（</font>**<font style="color:rgb(15, 17, 21);">这里基于 HTTPS 加密协议传输</font>**<font style="color:rgb(15, 17, 21);">）。</font>
5. <font style="color:rgb(15, 17, 21);">授权服务器验证通过，发放令牌。</font>

**<font style="color:rgb(15, 17, 21);"></font>**

**<font style="color:rgb(15, 17, 21);">黑客能拦截到什么？</font>**

**<font style="color:rgb(15, 17, 21);">├── 步骤2: code_challenge = "abc123hash" </font>**✅**<font style="color:rgb(15, 17, 21);"> 能</font>**

**<font style="color:rgb(15, 17, 21);">├── 步骤3: 授权码 = "AUTH_CODE_XYZ" </font>**✅**<font style="color:rgb(15, 17, 21);"> 能</font>**

**<font style="color:rgb(15, 17, 21);">└── 步骤4: code_verifier = "my_secret_123" </font>**✅**<font style="color:rgb(15, 17, 21);"> 能（HTTPS加密）</font>**

**<font style="color:rgb(15, 17, 21);"></font>**

**<font style="color:rgb(15, 17, 21);">黑客能成功吗？</font>**

**<font style="color:rgb(15, 17, 21);">└── 需要同时持有授权码和code_verifier</font>**

**<font style="color:rgb(15, 17, 21);">    ├── 如果只拦截到授权码 → </font>**❌**<font style="color:rgb(15, 17, 21);"> 失败（缺code_verifier）</font>**

**<font style="color:rgb(15, 17, 21);">    ├── 如果只拦截到code_verifier → </font>**❌**<font style="color:rgb(15, 17, 21);"> 失败（缺授权码）</font>**

**<font style="color:rgb(15, 17, 21);">    └── 如果两个都拦截到 → </font>**⚠️**<font style="color:rgb(15, 17, 21);"> 但HTTPS加密很难破解，且一次性使用（授权码和 code_verifier 的配对只能使用一次，用完立即失效）</font>**

### 授权模式的选择
| **<font style="color:rgb(15, 17, 21);">模式名称</font>** | **<font style="color:rgb(15, 17, 21);">客户端类型</font>** | **<font style="color:rgb(15, 17, 21);">是否有用户参与</font>** | **<font style="color:rgb(15, 17, 21);">安全性</font>** | **<font style="color:rgb(15, 17, 21);">推荐使用场景</font>** |
| --- | --- | --- | --- | --- |
| **<font style="color:rgb(15, 17, 21);">授权码模式</font>** | <font style="color:rgb(15, 17, 21);">机密客户端</font> | **<font style="color:rgb(15, 17, 21);">是</font>** | **<font style="color:rgb(15, 17, 21);">高</font>** | <font style="color:rgb(15, 17, 21);">有后端的传统Web应用</font> |
| **<font style="color:rgb(15, 17, 21);">隐式模式</font>** | <font style="color:rgb(15, 17, 21);">公开客户端</font> | **<font style="color:rgb(15, 17, 21);">是</font>** | **<font style="color:rgb(15, 17, 21);">低（已过时）</font>** | **<font style="color:rgb(15, 17, 21);">不推荐新项目使用</font>**<font style="color:rgb(15, 17, 21);">，用PKCE替代</font> |
| **<font style="color:rgb(15, 17, 21);">密码模式</font>** | <font style="color:rgb(15, 17, 21);">受信任的客户端</font> | **<font style="color:rgb(15, 17, 21);">是</font>** | **<font style="color:rgb(15, 17, 21);">中（需高度信任）</font>** | <font style="color:rgb(15, 17, 21);">第一方/官方应用</font> |
| **<font style="color:rgb(15, 17, 21);">客户端凭证模式</font>** | <font style="color:rgb(15, 17, 21);">机密客户端</font> | **<font style="color:rgb(15, 17, 21);">否</font>** | **<font style="color:rgb(15, 17, 21);">高</font>** | <font style="color:rgb(15, 17, 21);">机器对机器（M2M），后端API调用</font> |
| **<font style="color:rgb(15, 17, 21);">授权码+PKCE</font>** | **<font style="color:rgb(15, 17, 21);">公开客户端</font>** | **<font style="color:rgb(15, 17, 21);">是</font>** | **<font style="color:rgb(15, 17, 21);">最高（对公开客户端）</font>** | **<font style="color:rgb(15, 17, 21);">单页应用、移动App</font>** |


## Spring Security 中的 OAuth2
### 回顾 OAuth2 的 4 个角色
1. 资源所有者（Resource Owner）
2. 客户应用（Client）
3. 资源服务器（Resource Server）
4. 授权服务器（Authorization Server）

### Spring Security 中的实现
Spring Security 框架中 OAuth2 的文档：[https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html](https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html)

#### 客户应用 (OAuth2 Client)
**归属：Spring Security 核心项目**

```xml
<!-- 如果你要开发 OAuth2 的客户应用，请引入以下这个依赖： -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-oauth2-client</artifactId>
</dependency>
```

+ ✅ **内置在 Spring Security 主项目中（Spring Security 下的子项目）**
+ ✅ **有官方 Spring Boot Starter**
+ ✅ **版本与 Spring Security 同步**

#### 资源服务器 (OAuth2 Resource Server)
**归属：Spring Security 核心项目**

```xml
<!-- 如果你要开发 OAuth2 的资源服务器，请引入以下这个依赖： -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-oauth2-resource-server</artifactId>
</dependency>
```

+ ✅ **内置在 Spring Security 主项目中（Spring Security 下的子项目）**
+ ✅ **有官方 Spring Boot Starter**
+ ✅ **版本与 Spring Security 同步**

#### 授权服务器 (OAuth2 Authorization Server)
**归属：独立项目**

```xml
<!-- 如果你要开发 OAuth2 的授权服务器，请引入以下这个依赖： -->
<dependency>
    <groupId>org.springframework.security</groupId> <!-- groupId 和其它两个不一样 -->
    <artifactId>spring-security-oauth2-authorization-server</artifactId>
    <version>1.5.2</version> <!-- 需要手动指定版本号 -->
</dependency>
```

+ ❌ **不在 Spring Security 主项目中**
+ ❌ **没有官方 Spring Boot Starter**
+ ❌ **有独立的版本号和发布周期**

****

**<font style="color:#DF2A3F;">在实际开发中，我们多数是开发客户应用，比如我们开发的客户应用中登录功能的实现是交给 github 的，它已经将资源服务器的功能实现了，也将授权服务器的功能实现了。我们只需要开发客户应用就行了。</font>**

## GitHub社交登录案例
### 四个角色在该场景中的对应关系及全部 URL
1. **资源所有者**： 就是你，用户。
2. **客户应用**： 就是你开发的 Spring Boot 应用程序。在客户应用中你需要给 github 提供一个回调的 URL，github 将来通过这个 URL 给你传递授权码。回调 URL 通常是 `http://localhost:8080/login/oauth2/code/github`
3. **授权服务器**： GitHub 的授权端点（`https://github.com/login/oauth/authorize`）和令牌端点（`https://github.com/login/oauth/access_token`）。
    1. **授权端点**：当用户在页面上点击使用 github 进行登录时，重定向到 github 上的授权页面的地址。（**这个 URL 是客户应用通过浏览器的重定向方式发送给 github 的**）
    2. **令牌端点**：当客户应用收到授权码之后，使用类似于 HTTP Client 的技术发送一个服务器对服务器（不经过浏览器）的请求，该请求的 URL 就是 github 提供的令牌端点，请求中会携带**授权码 + ClientID + Client Secrets**，授权服务器验证通过后颁发令牌（服务器对服务器直接响应令牌字符串）给客户应用。
4. **资源服务器**： GitHub 的 API 服务器（例如 `https://api.github.com/user`），它存放着你的用户信息等受保护资源。
    1. 客户应用授权成功后，发送该 URL 请求去资源服务器上获取对应的资源。



**<font style="color:#DF2A3F;">总结：一共 4 个 URL</font>**

1. <font style="color:#DF2A3F;">授权服务器给客户应用提供的授权端点 URL（客户应用使用浏览器重定向的方式发送该请求）</font>
2. <font style="color:#DF2A3F;">授权服务器给客户应用提供的令牌端点 URL（客户应用使用 HTTP Client 在后端给授权服务器发送该请求）</font>
3. <font style="color:#DF2A3F;">客户应用给授权服务器提供的回调 URL（授权服务器使用浏览器重定向的方式发送给客户应用，传递授权码）</font>
4. <font style="color:#DF2A3F;">资源服务器给客户应用提供的资源 URL（客户应用携带令牌，通过 HTTP Client 方式在后端发送请求获取资源）</font>

### 详细的执行流程（编号步骤）
#### 第一阶段：准备工作
**步骤 0： 在 GitHub 上注册你的应用（Client）**  
在你写代码之前，需要先告诉 GitHub 有一个应用要使用它的 OAuth 服务。

1. 登录 GitHub -> Settings -> Developer settings -> OAuth Apps -> “New OAuth App”。
2. 填写应用信息：
    - **Authorization callback URL**： 这就是**回调 URL**。你需要填写你 Spring Boot 应用的一个地址，例如 `http://localhost:8080/login/oauth2/code/github`。这个 URL 的作用是：**当用户在 GitHub 上成功授权后，GitHub 会将浏览器重定向到这个地址，并附上授权码。**
3. 注册成功后，GitHub 会为你提供 **Client ID** 和 **Client Secret**。这两个东西相当于你应用的“用户名”和“密码”，需要配置到你的 Spring Boot 应用中。

#### 第二阶段：运行时交互流程
假设你的 Spring Boot 应用已经启动在 `http://localhost:8080`，并且有一个页面 (“/”) 上有一个 “Login with GitHub” 的链接。

**步骤 1： 用户发起登录请求**

1. 你（资源所有者）在浏览器中访问 `http://localhost:8080`。
2. 你点击了 “Login with GitHub” 的按钮/链接。

**步骤 2： 客户端将用户重定向至授权服务器**  
3.  你的 Spring Boot 应用（客户端）会构建一个指向 GitHub 授权服务器的 URL，并引导浏览器重定向过去。

    - URL 示例： `https://github.com/login/oauth/authorize?client_id=你的ClientID&redirect_uri=http://localhost:8080/login/oauth2/code/github&scope=user:email&response_type=code&state=某个随机字符串`
    - 参数解释：
        * `client_id`： 你的应用标识。
        * `redirect_uri`： 就是步骤 0 中设置的回调 URL，必须完全一致。
        * `response_type=code`： 表明我们使用授权码模式，要求返回一个授权码。
        * `scope`： 请求的权限范围，例如读取用户信息、邮箱等。
        * `state`： 一个随机字符串，用于防止 CSRF 攻击。

**步骤 3： 用户在授权服务器上进行认证和授权**  
4.  浏览器被重定向到 GitHub，你会看到 GitHub 的登录页面（如果你还没登录的话）。  
5.  你输入你的 GitHub 账号和密码进行登录（这是在向授权服务器证明你的身份）。  
6.  登录成功后，GitHub 会显示一个授权页面，询问你是否授权给 “你的应用名称” 访问你所请求的权限（例如访问你的公开资料）。  
7.  你点击 “Authorize”（授权）按钮。

**步骤 4： 授权服务器将用户重定向回客户端（携带授权码）**  
8.  GitHub（授权服务器）处理你的授权同意。它会让浏览器重定向到你在步骤 2 中提供的 `redirect_uri`（回调 URL），并在 URL 的查询参数中附带一个**授权码**。

    - 重定向的 URL 示例： `http://localhost:8080/login/oauth2/code/github?code=一串很长的授权码字符串&state=之前发送的随机字符串`

9.  **【回调 URL 的核心作用在此刻体现】**：你的 Spring Boot 应用必须有一个控制器（Controller）来监听这个回调 URL。Spring Security OAuth2 客户端模块已经帮你自动实现了这个端点。这个端点的任务是**接收 GitHub 发回来的授权码**。

**步骤 5： 客户端用授权码向授权服务器交换访问令牌**  
10. 你的 Spring Boot 应用（客户端）在后台（服务器对服务器的通信，不经过浏览器）向 GitHub 的令牌端点（`https://github.com/login/oauth/access_token`）发起一个 POST 请求。这个请求会携带以下关键信息：

    - `grant_type=authorization_code`
    - `code`： 从上一步回调 URL 中获取的授权码。
    - `redirect_uri`： 必须与之前的值一致。
    - `client_id` 和 `client_secret`： 用来向 GitHub 证明客户端的身份。

11. GitHub（授权服务器）验证这个请求。如果一切正常（授权码有效、客户端身份正确、redirect_uri 匹配），它会返回一个 JSON 响应，其中包含最重要的信息——**访问令牌**。

**步骤 6： 客户端使用访问令牌向资源服务器请求资源**  
12. 你的 Spring Boot 应用（客户端）现在拿到了访问令牌。  
13. 它可以使用这个令牌，去访问 GitHub 的资源服务器（资源服务器）的 API，例如获取用户信息。

    - 请求示例： `GET https://api.github.com/user`
    - 在 HTTP 头中携带令牌： `Authorization： Bearer 你的访问令牌`

14. GitHub 的资源服务器验证令牌的有效性，如果有效，则返回请求的资源，例如你的 GitHub 用户名、ID、头像等 JSON 数据。

**步骤 7： 客户端完成用户登录**  
15. 你的 Spring Boot 应用收到用户信息后，可以根据这些信息在你的应用内部为你创建一个本地账户（如果首次登录）或者建立一个会话（Session）。  
16. 最后，它将你重定向到应用的首页或其他成功页面。此时，你在你自己的应用中已经处于登录状态。



**总结与要点：**

+ **回调 URL 的核心作用**：它是整个流程的“桥梁”。授权服务器（GitHub）和你的客户端（Spring Boot 应用）通过它来完成关键信息的传递（授权码）。它是一个**预先约定好的接头地点**，确保授权码能安全地送回到你的应用手中。
+ **授权码模式的优势**：访问令牌的交换是在后端服务器之间进行的，客户端的 `client_secret` 不会暴露给前端浏览器，因此更加安全。
+ **Spring Boot 的简化**：通过引入 `spring-boot-starter-oauth2-client` 依赖并进行简单配置，上述的步骤 2、4、5、6 大部分都由 Spring Security 自动处理了。你主要需要配置 `application.yml` 并提供回调 URL 对应的控制器逻辑（通常是自动的）以及成功后的处理逻辑。

### 注册客户应用
客户应用要使用 github 作为授权服务器的话，首先需要在 github 上进行登记注册。也就是要获取 **Client ID** 和 **Client Secrets**。



**没有 github 账号的先注册一个：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759537513604-9acdf497-38be-4f79-8a20-5f592c8213b1.png" width="1234.2857142857142" title="" crop="0,0,1,1" id="u5b3922e8" class="ne-image" style="font-size: 16px">



**然后登录 github：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759537554738-cfa28a0b-7e07-49cd-8a76-c9c2702c774f.png" width="458.85714285714283" title="" crop="0,0,1,1" id="u75fbce81" class="ne-image" style="font-size: 16px">



**登录成功后，点右上角头像，在菜单中点击 **`**Settings**`**：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759538111374-102f87a8-b208-450b-82e9-0a850df26851.png" width="279.42857142857144" title="" crop="0,0,1,1" id="u908df12e" class="ne-image" style="font-size: 16px">



**拉到页面最下面，左侧有一个 **`**Developer Settings**`**，点击它：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759538719491-7ebd018f-4b98-4bde-96e0-c275f56b7e1f.png" width="446.2857142857143" title="" crop="0,0,1,1" id="u2e4a7774" class="ne-image" style="font-size: 16px">



**找到OAuth Apps，创建 OAuth App，为客户应用分配访问 github 的 **`**Client ID**`**和 **`**Client Secrets**`**：**

<img src="assets/image-20230510154255157.png" title="null" crop="0,0,1,1" id="xXPBd" class="ne-image" style="font-size: 16px">



**填写应用信息：**

默认的重定向URI模板为：`{baseUrl}/login/oauth2/code/{registrationId}`

registrationId 就是一个简短的、你自己起的昵称，用来在你的Spring Boot应用内部唯一标识一个OAuth2客户端配置。因为你的一个应用可能支持多种登录方式（例如，同时支持GitHub登录、Gitee登录、Google登录）。你需要给每种方式起个名字，以便在代码和配置中区分它们。规则很简单：通常使用小写，并且常取自OAuth2提供商的名称。在GitHub这个场景下，最自然、最常用的 registrationId 就是 github。



<img src="https://cdn.nlark.com/yuque/0/2026/png/21376908/1771826642985-c47c0996-8ffa-47d9-bcac-8c83e13aa6a4.png" width="577.6" title="" crop="0,0,1,1" id="u3b206b5a" class="ne-image">

<img src="assets/image-20231221000906168.png" title="null" crop="0,0,1,1" id="jQT5f" class="ne-image" style="font-size: 16px">



**获取 Client ID，生成 Client Secret：**

<img src="assets/image-20230510163101376.png" title="null" crop="0,0,1,1" id="ImDQ6" class="ne-image" style="font-size: 16px">

Client ID: `<font style="color:rgb(31, 35, 40);">Ov23liI6tnTiAd1483Wf</font>`

<font style="color:rgb(31, 35, 40);">Client Secret：</font>`<font style="color:rgb(31, 35, 40);">a2f5b6f1fc705fb919b7f973de22a626d3f5b145</font>`

<font style="color:rgb(31, 35, 40);">Client Secret 找一个地方存下来，因为它只显示一次。</font>

<font style="color:rgb(31, 35, 40);"></font>

**<font style="color:rgb(31, 35, 40);">可以选择传一个 logo</font>**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759494639750-bee29727-5714-4f72-9f3d-e34f157621b6.png" width="436" title="" crop="0,0,1,1" id="u7c7fc85b" class="ne-image" style="font-size: 16px">



**最后更新一下：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759494765524-94b627ab-b513-4406-a614-17c2804ed01e.png" width="332" title="" crop="0,0,1,1" id="u5d2f0561" class="ne-image" style="font-size: 16px">

### 创建客户应用项目
创建一个springboot项目 `oauth2-login-demo`，它就是我们的客户应用：

引入如下依赖

<img src="assets/image-20230510165314829.png" title="null" crop="0,0,1,1" id="MOdlz" class="ne-image" style="font-size: 16px">

注意：`OAuth2 Client` 依赖引入时，会自动引入 `Spring Security`。因此在创建项目时也可以不显示的引入 `Spring Security`。

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-oauth2-client</artifactId>
</dependency>
```

### 配置OAuth客户端属性
在 application.yml 中配置如下信息：

```properties
spring:
  security:
    oauth2:
      client:
        registration:
          github:
            client-id: Ov23liI6tnTiAd1483Wf
            client-secret: a2f5b6f1fc705fb919b7f973de22a626d3f5b145
            redirectUri: http://localhost:8080/login/oauth2/code/github
```

主要配置三项：

+ Client ID
+ Client Secret
+ Redirect URI

### 创建Controller
<font style="color:rgb(15, 17, 21);">这个Controller是一个展示OAuth2登录成功后显示用户信息和个人主页的控制器。</font>

**<font style="color:rgb(15, 17, 21);">详细解释：</font>**

+ <font style="color:rgb(15, 17, 21);">它处理网站根路径("/")的GET请求</font>
+ <font style="color:rgb(15, 17, 21);">通过注入的 </font>`<font style="color:rgb(15, 17, 21);">OAuth2AuthorizedClient</font>`<font style="color:rgb(15, 17, 21);"> 和 </font>`<font style="color:rgb(15, 17, 21);">OAuth2User</font>`<font style="color:rgb(15, 17, 21);"> 参数获取认证信息</font>
+ <font style="color:rgb(15, 17, 21);">将用户名、客户端名称和用户属性添加到模型中</font>
+ <font style="color:rgb(15, 17, 21);">返回"index"视图模板来展示这些信息</font>

<font style="color:rgb(15, 17, 21);">简单说就是</font>**<font style="color:rgb(15, 17, 21);">显示"登录成功"页面的控制器</font>**<font style="color:rgb(15, 17, 21);">，把从GitHub等OAuth2提供商那里获取的用户信息展示给用户看。</font>

```java
package com.jkweilai.oauth2.logindemo.controller;

import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.oauth2.client.OAuth2AuthorizedClient;
import org.springframework.security.oauth2.client.annotation.RegisteredOAuth2AuthorizedClient;
import org.springframework.security.oauth2.core.user.OAuth2User;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class IndexController {

    @GetMapping("/")
    public String index(Model model, @RegisteredOAuth2AuthorizedClient OAuth2AuthorizedClient authorizedClient, @AuthenticationPrincipal OAuth2User oauth2User) {
        model.addAttribute("userName", oauth2User.getName());
        model.addAttribute("clientName", authorizedClient.getClientRegistration().getClientName());
        model.addAttribute("userAttributes", oauth2User.getAttributes());
        return "index";
    }
}
```



当然，以上代码也可以修改以下代码，直接返回 JSON：

```java
@RestController
public class IndexController {

    @GetMapping("/")
    public Map<String, Object> index(@RegisteredOAuth2AuthorizedClient OAuth2AuthorizedClient authorizedClient, @AuthenticationPrincipal OAuth2User oauth2User) {
        Map<String, Object> map = new HashMap<>();
        map.put("userName", oauth2User.getName());
        map.put("clientName", authorizedClient.getClientRegistration().getClientName());
        map.put("userAttributes", oauth2User.getAttributes());
        return map;
    }
}
```

### 创建html页面
`resources/templates/index.html`

<font style="color:rgb(15, 17, 21);">这是一个OAuth2登录成功后的个人主页，用于展示用户信息和提供退出登录功能。</font>

**<font style="color:rgb(15, 17, 21);">详细说明：</font>**

+ <font style="color:rgb(15, 17, 21);">显示登录状态和用户信息（用户名、登录方式）</font>
+ <font style="color:rgb(15, 17, 21);">展示从OAuth2提供商（如GitHub）获取的所有用户属性</font>
+ <font style="color:rgb(15, 17, 21);">提供退出登录按钮</font>
+ <font style="color:rgb(15, 17, 21);">使用了Thymeleaf模板引擎和Spring Security标签</font>

```html
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:th="https://www.thymeleaf.org"
      xmlns:sec="https://www.thymeleaf.org/thymeleaf-extras-springsecurity5">
<head>
    <title>Spring Security - OAuth 2 Login</title>
    <meta charset="utf-8"/>
</head>
<body>
<div style="float: right" th:fragment="logout" sec:authorize="isAuthenticated()">
    <div style="float:left">
        <span style="font-weight:bold">User: </span><span sec:authentication="name"></span>
    </div>
    <div style="float:none">&nbsp;</div>
    <div style="float:right">
        <form action="#" th:action="@{/logout}" method="post">
            <input type="submit" value="Logout"/>
        </form>
    </div>
</div>
<h1>OAuth 2 Login with Spring Security</h1>
<div>
    You are successfully logged in <span style="font-weight:bold" th:text="${userName}"></span>
    via the OAuth 2 Client <span style="font-weight:bold" th:text="${clientName}"></span>
</div>
<div>&nbsp;</div>
<div>
    <span style="font-weight:bold">User Attributes:</span>
    <ul>
        <li th:each="userAttribute : ${userAttributes}">
            <span style="font-weight:bold" th:text="${userAttribute.key}"></span>: <span
                th:text="${userAttribute.value}"></span>

        </li>
    </ul>
</div>
</body>
</html>
```

### 启动应用程序
+ 启动程序并访问 `localhost:8080`。浏览器将被重定向到默认的自动生成的登录页面，该页面显示了一个用于GitHub登录的链接。点击GitHub链接，浏览器将被重定向到GitHub进行身份验证。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759495193474-92e2174f-7639-46db-bdd2-ca97bed91e83.png" width="500" title="" crop="0,0,1,1" id="u40a7729d" class="ne-image" style="font-size: 16px">

+ 使用GitHub账户凭据进行身份验证后，用户会看到授权页面，询问用户是否允许或拒绝客户应用访问GitHub上的用户数据。点击允许以授权OAuth客户端访问用户的基本个人资料信息。

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759495249427-895ca0ec-32aa-4777-ac1b-e8296030c4da.png" width="610" title="" crop="0,0,1,1" id="u48b7c755" class="ne-image" style="font-size: 16px">

+ 此时，OAuth客户端访问GitHub的获取用户信息的接口获取基本个人资料信息，并建立一个已认证的会话。最终显示页面为：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759544039957-2ee2165c-50d3-4bfd-a3fb-865c97da9257.png" width="609.7142857142857" title="" crop="0,0,1,1" id="ud84fd80a" class="ne-image" style="font-size: 16px">

### 退出与重新登录
我们在登录成功页面点击退出系统：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759544116273-c9c9e143-65d5-4a6d-a480-6ff0761c3e32.png" width="157.14285714285714" title="" crop="0,0,1,1" id="u4f25d573" class="ne-image" style="font-size: 16px">

显示已退出，也就是如下页面：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759544141680-85544e30-bef3-4686-bafc-fc6b14552b94.png" width="788" title="" crop="0,0,1,1" id="u14d73d38" class="ne-image" style="font-size: 16px">

当我们再次点击上图中的 `GitHub`再次登录时，不需要再输入用户名和密码进行登录和授权操作了，直接成功：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759544281065-c91c9789-ac0e-4680-ad32-ba79919aa406.png" width="610.2857142857143" title="" crop="0,0,1,1" id="uf2d61921" class="ne-image" style="font-size: 16px">



**这是为什么呢？****核心原因：你并没有真正完全退出。**详细解释：

1. **Spring Security 的 **`/logout`** 端点**
    - 你点击退出按钮，提交到 `/logout`，Spring Security 的默认行为是：**使当前服务器的 Session 失效，并清除本地的安全上下文（Security Context）**。
    - 这意味着，**你的应用**认为你已经退出了。
2. **GitHub (授权服务器) 的会话仍然存在**
    - 你的退出操作**只发生在你的应用内部**，并没有通知 GitHub。
    - 你在 GitHub 上已经登录并授权过，这个授权状态（以Cookie等形式）仍然保存在你的浏览器中。
3. **再次登录时的流程**
    - 当你再次点击登录时，你的应用再次将你重定向到 GitHub 的授权端点 (`/authorize`)。
    - GitHub 授权服务器检查你的浏览器会话，发现：“咦，这个用户已经登录并且之前已经授权过这个应用了”。
    - 为了提供更好的用户体验，GitHub 会**跳过再次询问你是否授权的步骤**，直接生成一个新的授权码，重定向回你的应用。
    - 你的应用拿到新的授权码，兑换新的访问令牌，然后为你创建新的会话，你又“自动”登录成功了。



**如何实现“完全退出”，让你下次需要重新输入密码？**

你需要**同时**完成以下两件事：

**1. 从你的应用退出 (你已经做了)**

+ 通过你的应用的 `/logout` 端点。

**2. 从 GitHub 退出**

+ 你需要手动或自动地也调用 GitHub 的退出端点。

我们遇到的现象是正常的，因为它遵循了OAuth2的常规用户体验设计：**一次授权，多次有效**。只有当你清除了GitHub的会话（比如手动退出GitHub，或者清除浏览器Cookie），下次登录时才会被要求重新输入用户名和密码进行授权。



**或者也可以按照以下方式操作：**

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759544850321-9891e525-0bbe-4916-9395-084fa223acfb.png" width="1205.142857142857" title="" crop="0,0,1,1" id="u035f31a1" class="ne-image" style="font-size: 16px">

这个列表中会显示所有访问过你的客户应用的合法的 github 用户。有 100 个 github 用户登录过你的客户应用，则显示 100 个。

点击 `Revoke all user tokens`，表示收回令牌。再次在客户应用中点击退出系统，再次登录时，会跳转到下面页面：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759545134150-706bf8cf-7f28-4c88-b722-249eaa775ff0.png" width="534.2857142857143" title="" crop="0,0,1,1" id="u6b056bfd" class="ne-image" style="font-size: 16px">

这是一个授权页面，为什么没有提醒你登录呢？因为现在的你已经登录过 github 了，并没有退出 github， 如果你想回到最初的登录页面，首先你自己需要退出 github，点击右上角头像，退出 github，再次刷新上面的授权页就会跳转到登录页了：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1759545266027-38686492-9518-4b31-ade7-8877aa6cbbc5.png" width="386.2857142857143" title="" crop="0,0,1,1" id="u8f4cb6ac" class="ne-image" style="font-size: 16px">

## CommonOAuth2Provider
`CommonOAuth2Provider` 是一个为常见OAuth2提供商（如Google、GitHub、Facebook等）提供预配置默认值的便利类（它是一个枚举类型）。

****

**它相当于一个“快捷设置模板”**。

当你在Spring Boot中配置OAuth2客户端时，需要填写很多参数，例如：

+ `authorizationUri`
+ `tokenUri`
+ `userInfoUri`
+ `userNameAttributeName`

对于知名的提供商（Google、GitHub等），这些地址和配置都是固定的。`CommonOAuth2Provider` 已经帮你把这些固定值预先配置好了。



**实际使用示例：**

在`application.yml`中，当你这样配置时：

```yaml
spring:
  security:
    oauth2:
      client:
        registration:
          github:
            client-id: xxx
            client-secret: xxx
```

Spring Security会在背后查找 `CommonOAuth2Provider.GITHUB` 的预配置，自动为你设置：

+ 授权URI: `https://github.com/login/oauth/authorize`
+ 令牌URI: `https://github.com/login/oauth/access_token`
+ 用户信息URI: `https://api.github.com/user`
+ 用户名属性名: `id`



**支持的提供商：**

该类预定义了以下常见提供商的配置：

+ `GOOGLE`
+ `GITHUB` 
+ `FACEBOOK`
+ `OKTA`



**总结：**

`CommonOAuth2Provider`** 的作用就是简化配置** - 你只需要提供`client-id`和`client-secret`，它自动帮你填好其他固定的配置项，让你不用去记忆或查找各个提供商的具体API地址。



**它的源码如下：**

```java
GITHUB {
    @Override
    public Builder getBuilder(String registrationId) {
        ClientRegistration.Builder builder = getBuilder(registrationId,
                ClientAuthenticationMethod.CLIENT_SECRET_BASIC, DEFAULT_REDIRECT_URL);
        // 设置默认的权限范围：读取用户信息
        builder.scope("read:user");
        // 设置GitHub的授权端点URL - 用户在此登录和授权
        builder.authorizationUri("https://github.com/login/oauth/authorize");
        // 设置GitHub的令牌端点URL - 用于兑换访问令牌
        builder.tokenUri("https://github.com/login/oauth/access_token");
        // 设置GitHub的用户信息端点URL - 用于获取用户详细信息
        builder.userInfoUri("https://api.github.com/user");
        // 设置用户名属性名为"id"，将使用GitHub用户ID作为主标识
        builder.userNameAttributeName("id");
        // 设置客户端显示名称为"GitHub"
        builder.clientName("GitHub");
        return builder;
    }
}
```



当然，这些默认值是可以修改的，直接在 `application.yml`文件中配置即可，例如使用 github 用户名作为主标识，可以这样配置：

```yaml
spring:
  security:
    oauth2:
      client:
        registration:
          github:
            client-id: Ov23lizW4zUUyyiiliDi
            client-secret: 146e72273d39bd54bbcd8d642b85742759a1a38d
            redirectUri: http://localhost:8080/login/oauth2/code/github
        provider:
          github:
            user-name-attribute: login
```

