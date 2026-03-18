```xml
<!--添加父工程的引用，当前pom.xml文件中有这个配置，说明当前项目是一个子模块。从父的pom中继承配置-->
<parent>
  <groupId>com.jkweilai.bank</groupId>
  <artifactId>bank-parent</artifactId>
  <version>0.0.1-SNAPSHOT</version>
</parent>

<!--本项目的身份证号gav-->
<groupId>com.jkweilai</groupId>
<artifactId>maven_project</artifactId>	  
<version>1.0.0</version>

<!--打包方式-->
<packaging>war</packaging>

<!--使用Properties集中化管理版本号-->
<properties>
  <!--mysql驱动的依赖-->
  <mysql.version>5.1.32</mysql.version>
  <spring-core-version>5.3.23</spring-core-version>
</properties>

<!-- 主要用于统一管理依赖的版本，它本身不会引入实际的依赖，所有子模块使用相同版本的依赖，避免冲突。 -->
<!-- 子模块在引用这些依赖时，可以省略 <version> 标签 -->
<!-- 只需要在这里修改一个版本号，所有子模块都会生效 -->
<dependencyManagement>
  <dependencies>
    <!-- 声明 Spring 相关依赖 -->
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-core</artifactId>
      <version>${spring-core-version}</version>
    </dependency>
  </dependencies>
</dependencyManagement>

<!--添加依赖-->
<dependencies>
  <dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>${mysql.version}</version>
  </dependency>	    
</dependencies>

<build>
  
  <!--聚合工程-->
  <!--当前项目如果作为一个父项目的话，可以有以下的配置，用于声明该项目包含哪些子模块-->
  <modules>
    <module>bank-manager-pojo</module>
    <module>bank-manager-mapper</module>
    <module>bank-manager-service</module>
    <module>bank-manager-web</module>
  </modules>
  
  <!--插件配置-->
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-compiler-plugin</artifactId>
      <configuration>
        <source>17</source>
        <target>17</target>
        <encoding>UTF-8</encoding>
      </configuration>
    </plugin>
  </plugins>
  
  <!--指定配置文件识别路径-->
  <resources>
    <resource>
      <directory>src/main/java</directory>
      <includes>
        <include>**/*.properties</include>
        <include>**/*.xml</include>
      </includes>
    </resource>
    <resource>
      <directory>src/main/resources</directory>
      <includes>
        <include>**/*.properties</include>
        <include>**/*.xml</include>
      </includes>
    </resource>
  </resources>
</build>
```

