# 字符编码

---

## 主要编码标准

### 1. ASCII码（American Standard Code for Information Interchange）
- **发布时间**：1967年
- **编码大小**：1字节（8位）
- **实际使用**：使用7位，最高位固定为0
- **字符数量**：128个字符（0-127）
- **包含内容**：
  - 控制字符（0-31）：回车、换行、制表符等
  - 可打印字符（32-126）：英文、数字、标点符号
  - 删除字符（127）：DEL
- **局限性**：只能表示英文字符，无法表示其他语言
- **参考资料**：[百度百科ASCII](https://baike.baidu.com/item/ASCII/309296)

### 2. Unicode（统一码）
- **设计目标**：为世界上所有字符提供唯一的数字编码
- **编码大小**：通常2-4字节（变长）
- **字符数量**：理论上可表示超过100万个字符
- **版本发展**：
  - Unicode 1.0（1991年）：7,161个字符
  - Unicode 15.0（2022年）：149,186个字符
- **与ASCII兼容**：Unicode的前128个字符与ASCII完全一致

#### Unicode与ASCII对比
| 字符 | Unicode编码 | ASCII编码 | 说明 |
|------|-------------|-----------|------|
| 'a' | U+0061 | 0x61 | 小写字母a |
| 'A' | U+0041 | 0x41 | 大写字母A |
| '0' | U+0030 | 0x30 | 数字0 |
| '学' | U+5B66 | 无 | 中文字符 |
| '🎉' | U+1F389 | 无 | 表情符号 |

#### Unicode实现方式
- **UTF-8**：变长编码（1-4字节），兼容ASCII
- **UTF-16**：变长编码（2或4字节），Java内部使用
- **UTF-32**：固定4字节编码，空间效率低

**参考资料**：
- [Unicode详细介绍](https://blog.csdn.net/m0_47841624/article/details/127283939)
- [Java中Unicode字符存储问题](https://zhuanlan.zhihu.com/p/106379925)

### 3. UTF-8（Unicode Transformation Format - 8-bit）
- **设计原则**：向后兼容ASCII，变长编码
- **编码规则**：
  - 1字节：ASCII字符（0-127）
  - 2字节：扩展拉丁字母等
  - 3字节：大部分汉字、日文、韩文
  - 4字节：特殊符号、表情符号等

#### UTF-8编码示例
| 字符类型  | 字符示例 | UTF-8编码             | 字节数 |
| ----- | ---- | ------------------- | --- |
| ASCII | 'A'  | 0x41                | 1字节 |
| 拉丁扩展  | 'é'  | 0xC3 0xA9           | 2字节 |
| 中文    | '中'  | 0xE4 0xB8 0xAD      | 3字节 |
| 表情    | '😀' | 0xF0 0x9F 0x98 0x80 | 4字节 |

### 4. 中文相关编码

#### GB2312（1980年）
- **字符集**：6,763个汉字
- **编码范围**：一级汉字3,755个，二级汉字3,008个
- **特点**：中国大陆最早的汉字编码标准

#### GBK（1995年）
- **全称**：汉字内码扩展规范
- **字符集**：21,886个汉字和符号
- **特点**：
  - 兼容GB2312
  - 包含繁体字和日韩汉字
  - 字母1字节，汉字2字节

#### GB18030（2000年）
- **最新标准**：强制性国家标准
- **字符集**：70,244个汉字
- **特点**：兼容GBK，支持少数民族文字

#### Big5
- **使用地区**：台湾、香港、澳门
- **字符集**：13,060个汉字
- **特点**：繁体中文编码标准

### 5. 编码对比总结
| 编码标准   | 字节数   | 兼容性      | 使用场景           |
| ------ | ----- | -------- | -------------- |
| ASCII  | 1字节   | -        | 早期英文系统         |
| UTF-8  | 1-4字节 | 兼容ASCII  | 现代Web、跨平台      |
| UTF-16 | 2/4字节 | -        | Java、Windows内部 |
| GBK    | 1-2字节 | 兼容GB2312 | 中文Windows系统    |
| Big5   | 1-2字节 | -        | 繁体中文系统         |

**参考资料**：[Unicode, UTF-8, UTF-16, UTF-32详细解析](https://www.cnblogs.com/malecrab/p/5300503.html)

---

## Java编码问题与解决方案

### 问题现象
在Java开发中，特别是使用EditPlus等编辑器时，经常遇到：
1. 源代码中的中文显示为乱码
2. 编译时出现编码错误
3. 程序运行时输出乱码

### 问题根源
编码不一致导致：
- **EditPlus默认**：GBK编码
- **Java编译器默认**：UTF-8编码（Java 21+）
- **系统控制台默认**：可能使用其他编码

### 解决方案

#### 方案一：编译时指定编码（推荐临时方案）
```bash
# 如果源文件是GBK编码
javac -encoding GBK Hello.java

# 如果源文件是UTF-8编码
javac -encoding UTF-8 Hello.java
```

#### 方案二：统一编辑器编码为UTF-8（推荐长期方案）

**EditPlus设置步骤**：
1. 打开EditPlus
2. 菜单：`工具` → `首选项`
3. 选择`文件`选项卡
4. 将`默认编码`改为`UTF-8`
5. 点击`确定`保存

**其他编辑器设置**：
- **VSCode**：文件 → 首选项 → 设置 → 搜索"files.encoding"
- **IntelliJ IDEA**：File → Settings → Editor → File Encodings
- **Eclipse**：Window → Preferences → General → Workspace

#### 方案三：Java源代码中指定编码
```java
// 编译时指定编码（在构建工具中配置）
// Maven pom.xml
<properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
</properties>

// Gradle build.gradle
tasks.withType(JavaCompile) {
    options.encoding = "UTF-8"
}
```

#### 方案四：运行时处理编码
```java
public class EncodingExample {
    public static void main(String[] args) {
        // 设置控制台输出编码
        System.setOut(new PrintStream(System.out, true, "UTF-8"));
        
        // 读取文件时指定编码
        try {
            BufferedReader reader = new BufferedReader(
                new InputStreamReader(
                    new FileInputStream("file.txt"), "UTF-8"
                )
            );
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### 编码检测与转换工具

#### 1. 检测文件编码
```bash
# 使用file命令（Linux/Mac）
file -I filename.java

# 输出示例：filename.java: text/plain; charset=utf-8
```

#### 2. 转换文件编码
```bash
# 使用iconv命令
iconv -f GBK -t UTF-8 input.java > output.java

# 使用Java程序转换
java -Dfile.encoding=UTF-8 MyProgram
```

#### 3. 在线检测工具
- [编码检测工具](https://tool.chinaz.com/tools/encoding.aspx)
- [文件编码检测](https://www.webtoolkitonline.com/file-encoding-detector.html)

---

## 最佳实践指南

### 1. 项目编码规范
- **统一使用UTF-8**：现代项目的标准选择
- **明确声明**：在项目配置文件中指定编码
- **团队一致**：确保所有开发者使用相同编码

### 2. 开发环境配置
```bash
# 设置环境变量（Linux/Mac）
export JAVA_TOOL_OPTIONS="-Dfile.encoding=UTF-8"
export LANG="en_US.UTF-8"

# Windows命令提示符
chcp 65001  # 设置为UTF-8代码页
```

### 3. 构建工具配置示例

**Maven配置**：
```xml
<project>
    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    </properties>
    
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <configuration>
                    <encoding>UTF-8</encoding>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

**Gradle配置**：
```gradle
tasks.withType(JavaCompile) {
    options.encoding = 'UTF-8'
}

tasks.withType(Test) {
    systemProperty "file.encoding", "UTF-8"
}
```

### 4. 常见问题排查

#### 问题：编译时出现" unmappable character"
**原因**：源代码编码与编译器编码不匹配
**解决**：
```bash
# 查看文件实际编码
file -I YourClass.java

# 使用正确编码编译
javac -encoding [实际编码] YourClass.java
```

#### 问题：运行时输出乱码
**原因**：控制台编码与程序输出编码不匹配
**解决**：
1. 设置控制台编码为UTF-8
2. 在Java程序中指定输出编码
3. 使用支持UTF-8的终端

---

## 编码转换示例代码

```java
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;

public class EncodingDemo {
    public static void main(String[] args) {
        // 1. 获取系统默认编码
        System.out.println("系统默认编码: " + Charset.defaultCharset());
        
        // 2. 支持的编码列表
        System.out.println("\n支持的字符集:");
        Charset.availableCharsets().keySet().stream()
                .sorted()
                .forEach(System.out::println);
        
        // 3. 字符串编码转换
        String text = "Hello, 世界!";
        
        // UTF-8编码
        byte[] utf8Bytes = text.getBytes(StandardCharsets.UTF_8);
        System.out.println("\nUTF-8字节: " + bytesToHex(utf8Bytes));
        
        // GBK编码
        byte[] gbkBytes = text.getBytes("GBK");
        System.out.println("GBK字节: " + bytesToHex(gbkBytes));
        
        // 4. 解码
        String decoded = new String(gbkBytes, "GBK");
        System.out.println("解码后: " + decoded);
    }
    
    private static String bytesToHex(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%02X ", b));
        }
        return sb.toString();
    }
}
```

---

## 总结要点

1. **编码选择**：
   - 现代项目统一使用 **UTF-8**
   - 中文Windows传统项目可能使用 **GBK**
   - Java内部使用 **UTF-16**

2. **问题核心**：
   - 所有乱码问题都是**编码不一致**导致的
   - 解决方案的核心是**统一编码**

3. **实践建议**：
   - 开发环境、编辑器、编译器、运行环境编码一致
   - 在项目配置中明确指定编码
   - 使用工具检测和转换编码

4. **Java特定**：
   - Java源代码文件建议保存为UTF-8
   - 编译时使用 `-encoding` 参数指定编码
   - 运行时注意控制台编码设置

通过遵循这些原则和实践，可以避免大多数编码相关问题，确保Java程序的跨平台兼容性和正确性。