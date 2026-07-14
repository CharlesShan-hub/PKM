## jEnv - Java 版本管理

### 安装
```bash
brew install jenv
```

### 配置（fish）
```bash
echo 'set -gx PATH $HOME/.jenv/bin $PATH' >> ~/.config/fish/config.fish
echo 'jenv init - | source' >> ~/.config/fish/config.fish
source ~/.config/fish/config.fish
```

### 添加已安装的 JDK
```bash
jenv add /opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home/
jenv add /opt/homebrew/opt/openjdk@8/libexec/openjdk.jdk/Contents/Home/
```

### 常用命令
| 命令 | 说明 |
|------|------|
| `jenv versions` | 列出所有版本 |
| `jenv version` | 查看当前版本 |
| `jenv global 21` | 全局切换到 Java 21 |
| `jenv global 8` | 全局切换到 Java 8 |
| `jenv local 8` | 当前目录切换到 Java 8（生成 .java-version） |
| `jenv shell 8` | 当前终端会话切换到 Java 8 |

### 验证
```bash
java -version
echo $JAVA_HOME
```

