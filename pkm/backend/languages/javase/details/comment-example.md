````java
package top.charles.basic;

import java.util.Optional;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Comment {
    public static void main(String[] args) {
        // 0. 先定义变量
        int a = 1, b = 2, c = 3, d = 4;
        String user = null;
        Stream<Integer> stream = Stream.of(1, 2, 3, 15, 20);

        // 1. 三元表达式换行 + 注释
        boolean condition = false;
        int result = condition
                ? 100   // 条件为 true
                : 200;  // 条件为 false

        // 2. 链式调用 + 注释
        stream
            .filter(x -> x > 10)    // 过滤大于10
            .map(x -> x * 2)        // 翻倍
            .collect(Collectors.toList());  // 收集结果

        // 3. 复杂表达式
        int total = a
                + b     // 基础值
                + c     // 附加值
                - d;    // 扣减

        // 4. Optional 链
        Optional.ofNullable(user)
                .map(String::length)    // 获取长度
                .orElse(0);       // 默认值
    }
}
```