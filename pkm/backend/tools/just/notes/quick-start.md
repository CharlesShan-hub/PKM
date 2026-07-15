# Just a Quick Start

> see: https://just.systems/man/zh/%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B.html
> 速查表：https://cheatography.com/linux-china/cheat-sheets/justfile/

在项目根目录创建 `justfile` 或者 `.justfile` 文件作为所有的命令定义。

最简案例
```txt
hello:
    echo "hello world"

welcome:
    @echo "welcome to just"
```

指定命令名称可以输出并执行命令
```powershell
PS D:\project\playground\learn-just> just hello
echo "hello world"
hello world
```

`@`开头的命令不显示命令本身
```powershell
PS D:\project\playground\learn-just> just welcome
welcome to just
```

默认运行第一个命令
```powershell
PS D:\project\playground\learn-just> just
echo "hello world"
hello world
```

命令会自动执行，如果遇到错误就会停止执行。（比如 build 只有 test 通过了才会执行）
```
publish:
  cargo test
  # 前面的测试通过才会执行 publish!
  cargo publish
```

