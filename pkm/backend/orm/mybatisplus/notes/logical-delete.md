# 逻辑删除

逻辑删除指的不是真正的删除数据，执行逻辑删除时，表中的数据仍然存在，只是这条记录被标记为`已删除`。怎么标记的？可以添加一个标记字段，例如：deleted，当deleted=1表示已删除，deleted=0表示未删除。

什么时候使用逻辑删除？数据比较重要的情况下才会考虑使用逻辑删除。实际开发中不太推荐使用逻辑删除，因为逻辑删除会导致数据量越来越大，影响查询性能。如果数据比较重要，删除时可以考虑将数据迁移到其他表以作备份。

当我们使用逻辑删除时，删除操作应该是一个update语句，例如：

```sql

update t_wx set deleted = 1 where id = ?;

```

当我们使用逻辑删除后，所有的查询语句也会受到影响，查询语句应该这样写：

```sql

select * from t_wx where deleted = 0;

```

那既然是这样 MyBatis-Plus 为我们自动生成的 SQL 语句还能用吗？当然可以用。因为mp也考虑到这一点了，你可以在`application.yml`配置文件中进行逻辑删除策略的配置，这样当删除和查询数据时，mp会自动按照逻辑删除的SQL语句生成。怎么配置？

```yaml

mybatis-plus:
  global-config:
    db-config:
      logic-delete-field: deleted # 标记逻辑删除的字段
      logic-delete-value: 1 # 已删除
      logic-not-delete-value: 0 # 未删除

```

给`t_wx`表添加一个`deleted`字段，编写代码测试一下：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744429819330-692287d2-c849-4e7b-9f71-d8c52c23d9f9.png" width="568" title="" crop="0,0,1,1" id="udcb4dcda" class="ne-image" style="font-size: 16px">

WeiXiu这个po上也要添加一个属性：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744430204264-68306fc7-939a-4d96-bfdf-133b43e0ac2c.png" width="512" title="" crop="0,0,1,1" id="ud8d03040" class="ne-image" style="font-size: 16px">

测试代码：

```java

package com.jkweilai.carmgtsys.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.jkweilai.carmgtsys.model.po.WeiXiu;

public interface WeiXiuService extends IService<WeiXiu> {
}

```

```java

package com.jkweilai.carmgtsys.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.jkweilai.carmgtsys.mapper.WeiXiuMapper;
import com.jkweilai.carmgtsys.model.po.WeiXiu;
import com.jkweilai.carmgtsys.service.WeiXiuService;

@Service
public class WeiXiuServiceImpl extends ServiceImpl<WeiXiuMapper, WeiXiu> implements WeiXiuService {
}

```

```java

@Autowired
private WeiXiuService weiXiuService;

@Test
public void logicDelete(){
    // 根据id删除数据
    weiXiuService.removeById(2L);
    // 根据id查询数据
    WeiXiu weiXiu = weiXiuService.getById(2L);
    System.out.println(weiXiu);
}

```

执行结果：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744430279990-59421d5a-b2ad-4ce0-8753-0f03a9cf3918.png" width="1029" title="" crop="0,0,1,1" id="u2ab9e092" class="ne-image" style="font-size: 16px">

数据库数据没有真正删除：

<img src="https://cdn.nlark.com/yuque/0/2025/png/21376908/1744430312146-03b05c15-36b4-46d3-ad99-699d95fc2c83.png" width="548" title="" crop="0,0,1,1" id="u0e25cce2" class="ne-image" style="font-size: 16px">

**注意：保存数据时，可以不用指定 deleted 字段的值，设计数据库表的时候，将 deleted 字段设置默认值为 0 即可。**
