```c
#include <stdio.h>

int main()
{

    for (int i = 0; i < 3; ++i)
    {
        for (int j = 0; j < 3; ++j)
        {
            for (int k = 0; k < 3; ++k)
            {
                printf("i: %d, j: %d, k: %d\n", i, j, k);
                // 假设当 i == 1, j == 2, k == 2 时，我们需要跳出所有循环
                if (i == 1 && j == 2 && k == 2)
                {
                    goto end_of_loops;
                }
            }
        }
    }

end_of_loops:
    printf("跳出所有循环。\n");
test:
    printf("不调用也会 print\n");

    return 0;
}
```

```shell
(base) kimshan@MacBook-Pro output % ./"a"
i: 0, j: 0, k: 0
i: 0, j: 0, k: 1
i: 0, j: 0, k: 2
i: 0, j: 1, k: 0
i: 0, j: 1, k: 1
i: 0, j: 1, k: 2
i: 0, j: 2, k: 0
i: 0, j: 2, k: 1
i: 0, j: 2, k: 2
i: 1, j: 0, k: 0
i: 1, j: 0, k: 1
i: 1, j: 0, k: 2
i: 1, j: 1, k: 0
i: 1, j: 1, k: 1
i: 1, j: 1, k: 2
i: 1, j: 2, k: 0
i: 1, j: 2, k: 1
i: 1, j: 2, k: 2
跳出所有循环。
不调用也会 print
```