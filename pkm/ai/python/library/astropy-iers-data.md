# astropy-iers-data

`astropy-iers-data` 是一个与 `astropy` 核心包相关的 Python 库，主要用于提供国际地球自转和参考系统服务（IERS）的地球旋转和闰秒表。这个库不直接面向用户，而是作为 `astropy` 核心包的一部分使用。它的主要功能是提供访问 IERS 服务提供的表，特别是用于给定时间的 UT1-UTC 和极移值插值的文件。这些值在 `astropy.time` 中用于提供 UT1 值，在 `astropy.coordinates` 中用于确定地球定向，以进行天球坐标与地球坐标之间的转换。 从版本 1.2 开始，最新的 IERS 值（包括大约一年的预测值）在需要时会自动从 IERS 服务下载。这通常发生在需要一个不在下载缓存中的值时，大多数情况下不需要手动调用 `iers` 类。 `astropy-iers-data` 需要 Python 3.8 或更高版本。它遵循 BSD 许可证，并由 Astropy 开发者维护。更多详细信息和文档可以在 `astropy-iers-data` 的官方 PyPI 页面、Astropy 文档页面以及 Astropy 官方网站中找到。
