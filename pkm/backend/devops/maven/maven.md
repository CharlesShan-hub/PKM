

# maven

---

## 简介

1. maven是什么
2. 本地仓库（自己电脑）、远程仓库（私服、中央仓库）
3. 构建过程：主要环节【背】、插件可以自定义
4. 依赖管理【两大核心功能：依赖管理+项目构建】

---

## 概念

1. pom
   1. parent（父工程 GAV）
   2. 本项目GAV：group，artifact，version（SNAPSHOT临时，RELEASE发布）
   3. 打包方式（jar：普通java项目与springboot项目 因为springboot里边已经有tomcat了，war：web项目）
   4. properties：集中化管理版本号，重点在“集中化”（ex：定义springboot版本号3.5.4）
   5. dependencyManagement：管理版本（并不会 真正的加载包），相当于一个父模块（ex：定义需要springboot-data，springboot-sequrity等）
   6. dependency：依赖。这里就不用写version了，如果写version就把dependencyManagement的覆盖了（ex：作为子模块，可能之引入了springboot-data）
   7. build：项目自动化构建弄
      1. plugins:插件
      2. modules:聚合工程（只有父项目才能写）
      3. resources：配置文件
2. 工程的目录结构
   1. src
      1. main：java/resources。java和resources这两个文件夹里边的内容都等于是根路径下的文件。
      2. test：java/resources
   2. pom.xml
3. 仓库：存构件（artifact）的位置。默认用户的根目录。
   1. 中央仓库：https://repo.maven.apache.org/maven2
   2. 找坐标：http://mvnrepository.com/

4. 生命周期与插件
   1. default：项目构建+部署
   2. clean：清理构建产物
   3. site：生成文档

5. 安装与配置
   1. 不用idea的本地配置：新建环境变量 MAVEN_HOME（不要带bin的路径），然后保证也要有JAVA_HOME（到jdkxxx这一层），最后把上边两个加到PATH里，`%JAVA_HOME%\bin`，`%MAVEN_HOME%\bin`
   2. 可以指定本地仓库目录：localRepository
   3. 默认的远程仓库：mirros
   4. jdk自适应构建，这样编译的时候可以默认使用某一个版本的java

6. 

---

## 命令



---

## 使用



---

## 依赖



---

## 继承



---

## 私服









































---

## Maven核心

### Maven概述

Maven是一个项目管理和构建工具，用于管理Java项目的依赖关系和构建过程。它提供了一个标准的项目结构和构建生命周期，使得开发人员可以更方便地管理和构建Java项目。

Maven是一个开源项目，由Apache Software Foundation开发和维护。

Maven提供了
1. 依赖管理：Maven可以管理项目的依赖关系，包括第三方库和其他项目的依赖。
    ```xml
    /* pom.xml */
    <dependencies>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.13.2</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
    ```
2. 构建流程：Maven提供了一个标准的构建流程，包括编译、测试、打包和部署等步骤。
3. 项目结构：Maven提供了一个标准的项目结构，包括src/main/java、src/test/java、src/main/resources等目录。

Maven的核心

* 项目对象模型（POM），它定义了一个项目的元数据，包括项目的依赖关系、构建配置和插件配置等。
* 依赖管理模型（Depencency），它定义了项目的依赖关系，包括第三方库和其他项目的依赖。
* 仓库管理模型（Repository），它定义了项目的仓库，包括本地仓库，中央仓库（Maven官方）和远程仓库（公司自己的）。
* 生命周期阶段，依靠各种插件，它提供了各种功能，包括编译，测试，打包，部署等。

### 依赖管理

* Maven配置阿里源： https://blog.csdn.net/xiaowang_lj/article/details/133207138
* IDEA找不到Maven： https://www.cnblogs.com/wobushitiegan/p/13156130.html
* 检查每个包的版本： https://mvnrepository.com/

Maven坐标
```xml
<groupId>com.charles</groupId>  
<artifactId>backend</artifactId>  
<version>1.0-SNAPSHOT</version>
```
* groupId：项目的组织标识符，通常使用公司的域名倒写。
* artifactId：项目的名称，通常使用项目的名称。
* version：项目的版本号，通常使用语义化版本号。SNAPSHOT表示快照版本，用于开发过程中的测试。

如果是第三方库的依赖，需要在pom.xml中添加依赖dependencies。
```xml
<dependencies>
    <dependency>
        <groupId>junit</groupId>
        <artifactId>junit</artifactId>
        <version>4.13.2</version>
    </dependency>
</dependencies>
```

排除依赖
```xml
<dependencies>  
    <dependency>  
        <groupId>org.springframework</groupId>  
        <artifactId>spring-context</artifactId>  
        <version>6.2.5</version>  
        <exclusions>  
            <exclusion>  
                <groupId>io.micrometer</groupId>  
                <artifactId>micrometer-observation</artifactId>  
            </exclusion>  
        </exclusions>  
    </dependency>  
</dependencies>
```

### 生命周期

1. clean：清理目标，用于清理项目的输出目录。
   * pre-clean：清理前的生命周期，用于清理项目的输出目录。
    * **clean**：清理生命周期，用于清理项目的输出目录。
    * post-clean：清理后的生命周期，用于清理项目的输出目录。
2. default: 默认生命周期，用于编译，测试，打包，部署等。
   * validate  
   * initialize  
   * generate-sources  
   * process-sources  
   * generate-resources  
   * process-resources  
   * **compile**：编译源代码，生成字节码。
   * process-classes  
   * generate-test-sources  
   * process-test-sources  
   * generate-test-resources  
   * process-test-resources  
   * test-prest-  
   * process-test-classes  
   * **test**：测试源代码，生成测试报告。
   * prepare-package  
   * **package**：打包源代码，生成可执行的jar或war文件。
   * verify  
   * **install**：安装可执行的jar或war文件到本地仓库。
   * deploy
3. site：生成项目的站点文档，包括项目的概述，API文档，测试报告等。
   * pre-site
   * site
   * post-site
   * site-deploy

### 单元测试

#### 简介

测试的阶段
1. 单元测试：测试单个类或方法的正确性。
2. 集成测试：测试多个类或方法的组合是否正确。
3. 系统测试：测试整个系统的功能是否正确。
测试的方法
4. 验收测试：测试用户的需求是否正确。

测试的方法
1. 白盒测试：测试代码的内部结构是否正确。
2. 黑盒测试：测试代码的外部行为是否正确。
3. 灰色测试：测试代码的内部结构和外部行为是否正确。

测试的工具
1. JUnit：Java语言的单元测试框架。【推荐】
2. Mockito：Java语言的模拟框架。
3. TestNG：Java语言的测试框架。
4. Selenium：Java语言的Web测试框架。

使用Maven引入Junit
```xml
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.8.1</version>
</dependency>
```
#### 断言

断言是一种测试方法，用于验证程序的正确性。断言是一种测试方法，用于验证程序的正确性。
断言的方法（一部分）
1. assertEquals：验证两个值是否相等。
2. assertTrue：验证一个值是否为真。
3. assertFalse：验证一个值是否为假。
4. assertNull：验证一个值是否为null。
5. assertNotNull：验证一个值是否不为null。

```java
package com.charles;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, Maven!");
    }

    @Test
    public void test(){
        int result = 1+2;
        assertEquals(3, result);
    }
}
```

#### 常见注解

|          注解          |            说明             |        备注        |
| :------------------: | :-----------------------: | :--------------: |
|       `@Test`        |  修饰测试类中的方法使其成为可启动执行的测试方法  |       单元测试       |
| `@ParameterizedTest` | 参数化测试注解，可使单个测试多次运行且每次参数不同 | 无需再使用 `@Test` 注解 |
|    `@ValueSource`    |       为参数化测试提供参数来源        |   配合参数化测试注解使用    |
|    `@DisplayName`    |  指定测试类、方法显示名称（默认类名、方法名）   |                  |
|    `@BeforeEach`     |   修饰实例方法，在每个测试方法执行前执行一次   |   初始化资源（准备工作）    |
|     `@AfterEach`     |   修饰实例方法，在每个测试方法执行后执行一次   |    释放资源（清理工作）    |
|     `@BeforeAll`     |   修饰静态方法，在所有测试方法前只执行一次    |   初始化资源（准备工作）    |
|     `@AfterAll`      |   修饰静态方法，在所有测试方法后只执行一次    |    释放资源（清理工作）    |

```java
package com.charles;

import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }

    // 在所有测试方法前执行一次（必须是静态方法）
    @BeforeAll
    static void initAll() {
        System.out.println("初始化测试环境 - 只执行一次");
    }

    // 在每个测试方法前执行
    @BeforeEach
    void init() {
        System.out.println("准备测试数据...");
    }

    @Test
    public void testAddition() {
        int result = 1 + 1;
        assertEquals(2, result, "1+1应该等于2");
    }

    @Test
    public void testSubtraction() {
        int result = 5 - 3;
        assertEquals(2, result);
    }

    // 在每个测试方法后执行
    @AfterEach
    void tearDown() {
        System.out.println("清理测试数据...");
    }

    // 在所有测试方法后执行一次（必须是静态方法）
    @AfterAll
    static void tearDownAll() {
        System.out.println("清理测试环境 - 只执行一次");
    }
}
```

#### 案例

通过身份证获取信息

```java
// UserProfile.java
package com.charles;  
  
import java.time.LocalDate;  
import java.time.Period;  
import java.time.format.DateTimeFormatter;  
  
public class UserProfile {  
    /**  
     * 根据身份证号获取性别  
     * @param idCard 身份证号  
     * @return 性别（男/女）  
     */  
    public static String getGender(String idCard) {  
        if (!isValidIdCard(idCard)) {  
            throw new IllegalArgumentException("无效的身份证号: " + idCard);  
        }        char genderCode = idCard.charAt(16);  
        return (genderCode % 2 == 0) ? "女" : "男";  
    }  
    /**  
     * 根据身份证号获取年龄  
     * @param idCard 身份证号  
     * @return 年龄  
     */  
    public static int getAge(String idCard){  
        if (!isValidIdCard(idCard)) {  
            throw new IllegalArgumentException("无效的身份证号: " + idCard);  
        }        String birthDateStr = idCard.substring(6, 14);  
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyyMMdd");  
        LocalDate birthDate = LocalDate.parse(birthDateStr, formatter);  
        LocalDate currentDate = LocalDate.now();  
        return Period.between(birthDate, currentDate).getYears();  
    }  
    /**  
     * 验证身份证号有效性  
     * @param idCard 身份证号  
     * @return 是否有效  
     */  
    public static boolean isValidIdCard(String idCard) {  
        return idCard != null && idCard.length() == 18;  
    }
}
```

```java
// UserProfileTest.java
package com.charles;  
  
import org.junit.jupiter.api.BeforeAll;  
import org.junit.jupiter.api.DisplayName;  
import org.junit.jupiter.api.Test;  
  
import java.time.LocalDate;  
  
import static org.junit.jupiter.api.Assertions.*;  
  
class UserProfileTest {  
    private static final String MALE_ID_CARD = "110105199003072634"; // 男性身份证  
    private static final String FEMALE_ID_CARD = "110105199003072624"; // 女性身份证  
    private static final int CURRENT_YEAR = LocalDate.now().getYear();  
  
    @BeforeAll  
    static void init() {  
        System.out.println("通过身份证获取信息测试");  
    }  
    @Test  
    @DisplayName("测试获取男性性别")  
    void testGetGenderMale() {  
        assertEquals("男", UserProfile.getGender(MALE_ID_CARD));  
    }  
    @Test  
    @DisplayName("测试获取女性性别")  
    void testGetGenderFemale() {  
        assertEquals("女", UserProfile.getGender(FEMALE_ID_CARD));  
    }  
    @Test  
    @DisplayName("测试获取年龄")  
    void testGetAge() {  
        int expectedAge = CURRENT_YEAR - 1990;  
        assertEquals(expectedAge, UserProfile.getAge(MALE_ID_CARD));  
    }  
    @Test  
    @DisplayName("测试身份证有效性")  
    void testIsValidIdCard() {  
        assertTrue(UserProfile.isValidIdCard(MALE_ID_CARD));  
        assertFalse(UserProfile.isValidIdCard("12345")); // 过短  
        assertFalse(UserProfile.isValidIdCard(null)); // 空值  
    }  
  
    @Test  
    @DisplayName("测试无效身份证获取性别时抛出异常")  
    void testGetGenderWithInvalidId() {  
        assertThrows(IllegalArgumentException.class, () -> UserProfile.getGender("123"));  
    }  
    @Test  
    @DisplayName("测试无效身份证获取年龄时抛出异常")  
    void testGetAgeWithInvalidId() {  
        assertThrows(IllegalArgumentException.class, () -> UserProfile.getAge(null));  
    }
}
```

可以去运行 UserProfileTest 的 Run UserProfileTest with Coverage.

#### 依赖范围

可以使用scope标签来指定依赖的范围。

```xml
<dependencies>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter</artifactId>
        <version>5.8.1</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```

* test：测试范围，只在测试时使用。最典型的就是JUnit。
* compile：编译范围，在编译和运行时都使用。(默认就是这个)
* provided：提供范围，在编译和运行时都使用，但由容器提供。
* runtime：运行范围，在运行时使用，但不参与编译。
* system：系统范围，由本地文件系统提供。
* import：导入范围，由其他POM文件提供。

## Maven进阶

### 分模块设计

### 继承

### 聚合

### 私服

