# stdint.h

* _\<stdint.h>_是[_\<inttypes.h>_](https://pubs.opengroup.org/onlinepubs/009695399/basedefs/inttypes.h.html)的子集
* `stdint.h` 头文件定义了一系列与整数大小相关的宏和数据类型，这些类型在不同的平台上具有固定的大小，确保了代码的可移植性。

1. **固定宽度的整数类型**：例如 `int8_t`, `int16_t`, `int32_t`, `int64_t` 用于表示有符号整数，以及 `uint8_t`, `uint16_t`, `uint32_t`, `uint64_t` 用于表示无符号整数。
2. **最小宽度整数类型**：例如 `int_least8_t`, `int_least16_t`, `int_least32_t`, `int_least64_t` 和 `uint_least8_t`, `uint_least16_t`, `uint_least32_t`, `uint_least64_t`，它们保证至少有指定宽度的存储大小，但可能更宽。
3. **最快最小宽度整数类型**：例如 `int_fast8_t`, `int_fast16_t`, `int_fast32_t`, `int_fast64_t` 和 `uint_fast8_t`, `uint_fast16_t`, `uint_fast32_t`, `uint_fast64_t`，它们保证至少有指定宽度的存储大小，并且尽可能地快。
4. **最大宽度整数类型**：`intmax_t` 和 `uintmax_t`，它们提供了最大宽度的有符号和无符号整数类型。
5. **极限值宏**：例如 `INT8_MAX`, `INT16_MAX`, `INT32_MAX`, `INT64_MAX` 以及它们的 `MIN` 和 `UMAX` 变体，定义了对应类型可以表示的最大值和最小值。