
## 使用Navicat for MySQL初始化数据
### 建库
使用Navicat for MySQL创建一个MySQL数据库，起名：jdbc
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702356898211-79878d20-d32a-4764-b2d9-fa7de3c24053.png#averageHue=%23f0eeed&clientId=u0cd9c8dc-062f-4&from=paste&height=487&id=ub2f26cb2&originHeight=487&originWidth=293&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24944&status=done&style=none&taskId=u71f5ac6e-a9cc-4a75-b621-4f724c14131&title=&width=293)
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702356942314-e5cb2d8a-3e9c-46b4-91b6-6ab59e7fbb0a.png#averageHue=%23f9f8f8&clientId=u0cd9c8dc-062f-4&from=paste&height=390&id=u4f4cc83e&originHeight=390&originWidth=438&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10115&status=done&style=none&taskId=u51c78507-6467-4fce-ae75-1c842cebf05&title=&width=438)

### 建表
执行jdbc.sql脚本：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702357035951-94877536-4153-4399-a6ae-9672bf97e062.png#averageHue=%23f0edeb&clientId=u0cd9c8dc-062f-4&from=paste&height=374&id=u41c592a0&originHeight=374&originWidth=293&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21222&status=done&style=shadow&taskId=u6da02b5b-0bc8-49b2-88a1-806cbe27063&title=&width=293)
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702357083312-51eff97d-6686-4559-b15b-5069e5ed60ba.png#averageHue=%23f7f7f6&clientId=u0cd9c8dc-062f-4&from=paste&height=392&id=ued9efd1d&originHeight=392&originWidth=561&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14995&status=done&style=shadow&taskId=u60682216-3bf0-4eda-9e71-9fb70795456&title=&width=561)

最终创建的表：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702357196196-5a9db89b-b896-4bf0-88bb-c4d5aabd411b.png#averageHue=%23f6f6f5&clientId=u0cd9c8dc-062f-4&from=paste&height=284&id=ua74bad36&originHeight=284&originWidth=863&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22932&status=done&style=shadow&taskId=u14f0bfdf-c432-4493-a95c-d82bea257b9&title=&width=863)

### 插入数据
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702357446508-4d4cdf35-d996-4fa2-b823-afe81b1e9c50.png#averageHue=%23f3f2f0&clientId=u0cd9c8dc-062f-4&from=paste&height=190&id=uf0f4611c&originHeight=190&originWidth=579&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18948&status=done&style=shadow&taskId=u4c353718-bc1f-4e17-ae48-47401a0371d&title=&width=579)
注意：这里我将主键设置为了自增：auto_increment。其实这个也可以在PowerDesigner中设计时指定自增：勾选上它即可。
![image.png](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702357560943-84503c36-4205-42bc-b488-6cca2f4dd16c.png#averageHue=%23f3f2f1&clientId=u0cd9c8dc-062f-4&from=paste&height=444&id=ude5a2110&originHeight=444&originWidth=540&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23459&status=done&style=shadow&taskId=u795b2b6b-d5a5-40bc-a0a4-7672112dd8a&title=&width=540)
