# Mapper 代理

* 【黑马mybatis教程全套视频教程，2天Mybatis框架从入门到精通】 https://www.bilibili.com/video/BV1MT4y1k7wZ/?p=4

每一个 mapper 的 xml 都需要手动配置，比如
```xml
<mapper namespace="test">
    <select id="selectAllUsers" resultType="com.charlesshan.helloworld.entity.User">
        select * from user;
    </select>
</mapper>
```

* 不用 mapper 的方案
```java
List<User> = sqlSession.selectList("test.selectAllUsers");
```
* 使用 mapper 的方案
```java
UserMapper userMapper = sqlSession.getMapper(selectAllUsers.class);
List<User> = userMapper.selectAllUsers();
```