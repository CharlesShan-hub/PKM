# XXL-JOB

分布式任务调度平台学习笔记。

---

## 专题一：任务调度基础

了解任务调度的基本概念与常见场景，为后续学习分布式调度方案打基础。

* [任务调度概述](notes/task-scheduling-overview.md)
* [任务调度核心概念](notes/task-scheduling-core-concepts.md)：任务、触发器、调度器
* [任务调度使用场景](notes/task-scheduling-cases.md)
* [任务调度注意事项](notes/task-scheduling-notes.md)

---

## 专题二：Java 任务调度方案对比与选型

从 JDK 内置方案（Timer、ScheduledExecutorService、@Scheduled）到成熟框架（Quartz），再到为什么必须走向分布式。

* [Java 任务调度实现方案](notes/task-scheduling-implementations.md)
* [任务调度选型指南](notes/task-scheduling-selection-guide.md)
* [为什么需要分布式任务调度](notes/distributed-task-scheduling-why.md)

---

## 专题三：XXL-JOB 入门与部署

从零认识 XXL-JOB，搭建调度中心、部署执行器，跑通第一个任务。

* [XXL-JOB 介绍与架构](notes/xxljob-introduction.md)
* [调度中心部署指南](notes/xxljob-admin-deployment.md)
* [执行器部署与配置](notes/xxljob-executor-deployment.md)
* [HelloWorld 快速上手](notes/xxljob-helloworld.md)

---

## 专题四：XXL-JOB 核心特性与进阶用法

深入 XXL-JOB 在分布式场景下的核心能力：动态任务、集群去重、分片广播。

* [GLUE 模式（动态任务）](notes/xxljob-glue-mode.md)
* [集群去重与路由策略](notes/xxljob-cluster-dedup.md)
* [分片广播](notes/xxljob-sharding.md)

---

### 外部链接收集

* [美团点评许雪里：分布式任务调度平台 XXL-JOB](https://zhuanlan.zhihu.com/p/36627346)