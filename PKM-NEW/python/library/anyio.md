# anyio

AnyIO 是一个用于异步网络和并发处理的 Python 库，它可以在 asyncio 或 trio 之上运行。这个库实现了类似于 trio 的结构化并发（SC），并且与 trio 本身的本地 SC 相协调。使用 AnyIO 编写的应用程序和库可以在 asyncio 或 trio 上无修改地运行。此外，AnyIO 也可以集成到其他项目中。 AnyIO 要求 Python 3.8 或更高版本。为了开发或试验 AnyIO，建议设置一个虚拟环境。安装 AnyIO 只需运行 `pip install anyio`。如果你还需要支持 Trio，可以像这样安装：`pip install anyio[trio]`。 AnyIO 的基本用法包括运行异步程序。一个简单的 AnyIO 程序可能如下所示：

```python
from anyio import run
async def main():
    print('Hello, world!')
run(main)
```

这个程序将在默认后端（asyncio）上运行。如果你想在其他支持的后端上运行它，比如 Trio，你可以使用 `backend` 参数。 需要注意的是，AnyIO 代码不一定必须通过 `run()` 函数运行。你也可以使用后端库的本地 `run()` 函数。例如，如果你使用 Trio，你可以这样做：

```python
import sniffio
import trio
from anyio import sleep
async def main():
    print('Hello')
    await sleep(1)
    print("I'm running on", sniffio.currentasynclibrary())
trio.run(main)
```

从版本 4.0.0 开始，在 asyncio 后端上，`anyio.run()` 现在在 Python 3.11 之前的版本上使用一个后向移植的版本 of `asyncio.Runner`。 更多详细信息和文档可以在 AnyIO 的官方文档中找到。
