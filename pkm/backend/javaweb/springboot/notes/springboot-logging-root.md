# 全局根日志记录器,影响所有未单独配置的包和类

logging.level.root=DEBUG

```

执行结果：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1731729136927-1440a2bf-8b96-49c1-9d78-aa9f270a7deb.png" width="205" title="" crop="0,0,1,1" id="ua6eca803" class="ne-image">

更改为最低级别，会打印所有日志信息：

```properties

logging.level.root=TRACE

```

执行结果：

<img src="https://cdn.nlark.com/yuque/0/2024/png/21376908/1731729214172-ae5c8ba3-c73e-40c6-a450-7511953a1402.png" width="204" title="" crop="0,0,1,1" id="ub79457dc" class="ne-image">

---

## 丰富启动日志（了解）

```properties

debug=true

```

**这个配置项用于控制**Spring Boot 框架自身**的启动期日志与诊断信息，**不影响**应用程序的业务日志。**

+ `**debug=true**`**：启用调试模式，输出更详细的启动日志，并显示自动配置报告。仅作用于框架启动阶段**，启动完成后不再生效。**

---

## 日志的粗细粒度

```properties

logging.level.root=WARN                     # 全局默认WARN
logging.level.com.jkweilai.service=INFO     # 明确指定service包为INFO
logging.level.com.jkweilai.service.OrderService=DEBUG # 明确指定该类的日志信息要更加详细

```

**效果：对OrderService这个类开启详细调试日志，对其他业务类只记录重要信息，全局默认只记录警告和错误。**

---

## 日志的分组

### 日志组的定义和使用

**日志组让多个包/类的日志级别可以**统一设置和批量修改**，避免重复配置，提升管理效率。**

```properties
