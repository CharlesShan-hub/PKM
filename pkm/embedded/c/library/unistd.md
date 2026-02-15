# unistd.h

## APIs

> unistd.h是用于linux/unix系统的调用。 `#include <unistd.h>`是POSIX标准定义的unix类系统定义符号常量的头文件，包含了许多UNIX系统服务的函数原型，例如read函数、write函数和getpid函数。

## getopt

```c
#include <unistd.h>

int getopt(int argc, char * const argv[], const char *optstring);

extern char *optarg;
extern int optind, opterr, optopt;
```
- `optarg`: 指向当前选项参数的指针
- `optind`: 下一个要处理的 `argv` 索引
- `opterr`: 错误输出标志（非0时打印错误信息）
- `optopt`: 存储无法识别的选项字符

```c
//basic_getopt.c
#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    int opt;
    
    // 单个字符表示选项
    // 字符后跟 :表示需要参数
    // 字符后跟 ::表示可选参数（GNU扩展）
    while ((opt = getopt(argc, argv, "ab:c::")) != -1) {
        // 检查返回值是否为 -1
        // 处理 ?情况（未知选项）
        // 验证必需参数是否存在
        switch (opt) {
            case 'a':
                printf("选项 -a 被指定\n");
                break;
            case 'b':
                printf("选项 -b 被指定，参数为: %s\n", optarg);
                break;
            case 'c':
                if (optarg != NULL) {
                    printf("选项 -c 被指定，带有参数: %s\n", optarg);
                } else {
                    printf("选项 -c 被指定，没有参数\n");
                }
                break;
            case '?':
                printf("未知选项: %c\n", optopt);
                break;
        }
    }
    
    // 处理非选项参数
    // 使用 optind访问非选项参数
    // 非选项参数必须出现在所有选项之后
    for (int i = optind; i < argc; i++) {
        printf("非选项参数: %s\n", argv[i]);
    }
    
    return 0;
}

// gcc -o basic_getopt basic_getopt.c
// 
// 测试示例1: ./basic_getopt -a -b Hello -cNew -d World
// 预期输出:（注意 -c和后边的的参数不能有空格）
// (playground) (TraeAI-11) ~/P/p/p/e/getopt [0] $ ./basic_getopt -a -b Hello -cNew -d World
// 选项 -a 被指定
// 选项 -b 被指定，参数为: Hello
// 选项 -c 被指定，带有参数: New
// ./basic_getopt: illegal option -- d
// 未知选项: d
// 非选项参数: World
// 
// 测试示例2: ./basic_getopt -a -b Hello -c
// (playground) (TraeAI-11) ~/P/p/p/e/getopt [0] $ ./basic_getopt -a -b Hello -c
// 选项 -a 被指定
// 选项 -b 被指定，参数为: Hello
// 选项 -c 被指定，没有参数
// 
// 测试示例3: ./basic_getopt -a -b Hello
// (playground) (TraeAI-11) ~/P/p/p/e/getopt [0] $ ./basic_getopt -a -b Hello
// 选项 -a 被指定
// 选项 -b 被指定，参数为: Hello

```

1. **选项字符串中的字符顺序无关紧要**
   - 例如 `"ab:c::"` 和 `"b:ac::"` 功能相同

2. **没有 `:`，代表选项没有参数**
   - 示例：`"a"` 表示 `-a` 选项不需要参数
   - 调用方式：`./program -a`

3. **有单个 `:`，代表选项需要参数**
   - 示例：`"b:"` 表示 `-b` 选项必须带有参数
   - 调用方式：`./program -b value` 或 `./program -bvalue`
   - 参数可以与选项直接连接或用空格分隔

4. **有双冒号 `::`，代表选项参数可选（GNU扩展）**
   - 示例：`"c::"` 表示 `-c` 选项的参数是可选的
   - 调用方式：
     - 不带参数：`./program -c`
     - 带参数：`./program -cvalue`（**注意：参数必须与选项直接连接，不能有空格**）
5. **非选项参数的处理**
   * 所有非选项参数必须出现在所有选项之后，或者在 `--` 分隔符之后
   * 可以通过 `optind` 变量访问第一个非选项参数的索引

## Reference

1. wiki: https://en.wikipedia.org/wiki/Unistd.h 
2. unistd官方介绍: https://man7.org/linux/man-pages/man0/unistd.h.0p.html
3. getopt官方介绍: https://www.gnu.org/software/libc/manual/html_node/Using-Getopt.html