# Spring Security + OAuth2 + JWT 三者协作关系
1. **<font style="color:rgb(15, 17, 21);">OAuth2 负责"你是谁"</font>**<font style="color:rgb(15, 17, 21);">：通过 GitHub 等第三方平台完成用户身份认证，获取用户基本信息</font>
2. **<font style="color:rgb(15, 17, 21);">JWT 负责"你拿着什么凭证"</font>**<font style="color:rgb(15, 17, 21);">：将 OAuth2 获取的用户信息封装成自包含的令牌，由客户端保存，后续请求携带</font>
3. **<font style="color:rgb(15, 17, 21);">Spring Security 负责"怎么验证和管理"</font>**<font style="color:rgb(15, 17, 21);">：提供整套安全框架，用过滤器链拦截请求、验证 JWT、执行权限控制，并将认证状态从服务端 Session 转移到客户端 JWT，实现无状态架构</font>
