
https://blog.csdn.net/m0_53022813/article/details/128813298

https://www.yuque.com/dujubin/ltckqu/kipzgd?#p1WjS


## OCP：开闭原则

比如表示层，业务层，持久层，依次调用。如果修改某一层的内容，不需要修改依赖他的其他层。

## DIP：依赖倒置原则

倡导面向接口编程

## IoC：控制反转

这就解释了，为啥要注入，而不是写死。使用 DI（依赖注入）的方式实现了 IoC（控制反转）。
```java
package com.charlesshan.helloworld.service.impl;

import com.charlesshan.helloworld.entity.User;
import com.charlesshan.helloworld.mapper.UserMapper;
import com.charlesshan.helloworld.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserServiceImpl implements UserService {
    // ✅Good
    @Autowired // 自动注入
    private UserMapper userMapper; // 不需要写死，让框架去做这些，实现了控制反转

	// ❌Bad
	// private UserMapper userMapper = new UserMapperImpl();
	
    @Override
    public List<User> findAll() {
        return userMapper.selectAllUsers();
    }
}
```