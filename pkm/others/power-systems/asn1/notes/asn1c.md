# asn1c + PER 编解码完整上手指南

> 工具：`asn1c v0.9.21` · 编译器：MSYS2 ucrt64 GCC · 平台：Windows  
> 场景：用 ASN.1 定义电力设备状态上报报文，生成 C 代码，完成 UPER 编码 → 解码 → 验证全流程。

---

## 1. 前置条件

| 软件 | 路径 | 说明 |
|---|---|---|
| asn1c | `D:\program\asn1c\` | 含 `bin\asn1c.exe` 和 `skeletons\` |
| GCC (ucrt64) | `D:\program\msys64\ucrt64\bin\gcc.exe` | MSYS2 UCRT64 工具链 |

将 asn1c 的 `bin` 目录加入 PATH，或在命令里使用完整路径。

---

## 2. ASN.1 定义文件

文件名：`example.asn1`

```asn1
-- 简单的测量报文结构，模拟电力/工业场景中的数据上报
MeasureModule DEFINITIONS IMPLICIT TAGS ::= BEGIN

  -- 设备状态上报报文
  MeasureReport ::= SEQUENCE {
    deviceId    INTEGER,          -- 设备编号
    voltage     INTEGER,          -- 电压，单位 mV（毫伏）
    current     INTEGER,          -- 电流，单位 mA（毫安）
    status      BOOLEAN           -- 设备是否在线
  }

END
```

**几个关键点：**
- `SEQUENCE` 对应 C 的 `struct`。
- `INTEGER` 对应 asn1c 的 `INTEGER_t`（内部是 `BIT STRING`，需用 `asn_long2INTEGER` / `asn_INTEGER2long` 存取）。
- `BOOLEAN` 对应 C 的 `BOOLEAN_t`（本质是 `int`，非零即真）。
- `IMPLICIT TAGS` 在 PER 下影响不大，但是标准写法。

---

## 3. 生成 C 代码

在 `example.asn1` 所在目录打开终端，执行：

```powershell
# 创建输出目录
mkdir per_demo

# 生成 PER 代码
D:\program\asn1c\bin\asn1c.exe `
    -gen-PER `
    -pdu=all `
    -S D:\program\asn1c\skeletons `
    -D per_demo `
    example.asn1
```

| 参数 | 含义 |
|---|---|
| `-gen-PER` | 生成 PER 编解码接口（默认只生成 BER） |
| `-pdu=all` | 把所有顶层类型都作为 PDU |
| `-S <path>` | 指定 skeleton 源文件目录（Windows 下必须显式指定，否则 symlink 无效） |
| `-D per_demo` | 输出到指定目录 |

执行后，`per_demo/` 中会出现：
- `MeasureReport.c` / `MeasureReport.h` — 由 ASN.1 生成的核心类型文件
- 大量 `*.c` / `*.h` — asn1c runtime skeleton（INTEGER、BOOLEAN、NativeInteger 等基础类型）

---

## 4. Windows 特有问题处理

### 4.1 Skeletons 变成 `.lnk` 文件

**问题**：asn1c 在 Linux/macOS 下用 symlink 指向 skeleton，Windows 没有 symlink 权限，会生成无用的 `.lnk` 文件，导致编译找不到源文件。

**解决**：手动把 skeleton 目录里所有 `.c` 和 `.h` 复制进来（用 `-S` 参数后一般已经是直接复制，若还有问题就手动补）：

```powershell
Copy-Item D:\program\asn1c\skeletons\*.c per_demo\ -Force
Copy-Item D:\program\asn1c\skeletons\*.h per_demo\ -Force
```

### 4.2 排除两个不兼容的文件

`GeneralizedTime.c` 和 `UTCTime.c` 使用了 POSIX 的 `setenv`/`unsetenv`，在 Windows UCRT 下不存在，会导致编译失败。

**解决**：编译时把这两个文件排除（我们的演示程序用不到时间类型）。

### 4.3 缺少 `ntohl` 符号

`ntohl`（网络字节序转换）在 Windows 上位于 `Winsock2` 库，需要手动链接：

```
-lws2_32
```

---

## 5. 主程序 main.c

将以下文件保存为 `per_demo/main.c`：

```c
/*
 * ASN.1 UPER（Unaligned PER）编码/解码演示
 * 场景：模拟电力设备状态上报报文的编码与解码
 *
 * 流程：
 *   1. 构造一个 MeasureReport 结构体（填入数据）
 *   2. 用 uper_encode() 编码成字节流
 *   3. 打印字节流（模拟"传输"阶段）
 *   4. 用 uper_decode() 把字节流解码还原成新的结构体
 *   5. 读出字段值并验证与原始数据一致
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "MeasureReport.h"
#include "per_encoder.h"
#include "per_decoder.h"

/* ---- 辅助：给 INTEGER_t 赋一个 long 值 ---- */
static void set_integer(INTEGER_t *target, long value) {
    asn_long2INTEGER(target, value);
}

/* ---- 辅助：从 INTEGER_t 读出 long 值 ---- */
static long get_integer(const INTEGER_t *src) {
    long out = 0;
    asn_INTEGER2long(src, &out);
    return out;
}

/* ---- PER 编码缓冲区回调：把字节流收集到动态内存 ---- */
typedef struct {
    uint8_t *buf;
    size_t   len;
} DynBuf;

static int encode_cb(const void *buffer, size_t size, void *app_key) {
    DynBuf *b = (DynBuf *)app_key;
    b->buf = (uint8_t *)realloc(b->buf, b->len + size);
    memcpy(b->buf + b->len, buffer, size);
    b->len += size;
    return 0; /* 0 = 继续 */
}

int main(void) {

    /* ========== 第一步：构造原始数据 ========== */
    MeasureReport_t report;
    memset(&report, 0, sizeof(report));

    set_integer(&report.deviceId, 42);       /* 设备 #42   */
    set_integer(&report.voltage,  220000);   /* 220.000 V（单位 mV） */
    set_integer(&report.current,  5000);     /* 5.000 A（单位 mA）  */
    report.status = 1;                       /* TRUE = 在线          */

    printf("===== [原始数据] =====\n");
    printf("deviceId : %ld\n", get_integer(&report.deviceId));
    printf("voltage  : %ld mV  (= %.3f V)\n",
           get_integer(&report.voltage),
           get_integer(&report.voltage) / 1000.0);
    printf("current  : %ld mA  (= %.3f A)\n",
           get_integer(&report.current),
           get_integer(&report.current) / 1000.0);
    printf("status   : %s\n", report.status ? "ONLINE" : "OFFLINE");

    /* ========== 第二步：UPER 编码 ========== */
    DynBuf encoded = { NULL, 0 };

    asn_enc_rval_t enc_rval = uper_encode(
        &asn_DEF_MeasureReport,
        &report,
        encode_cb,
        &encoded
    );

    if (enc_rval.encoded == -1) {
        fprintf(stderr, "编码失败，类型：%s\n", enc_rval.failed_type->name);
        return 1;
    }

    printf("\n===== [UPER 编码结果] =====\n");
    printf("编码比特数：%zd\n", (ssize_t)enc_rval.encoded);
    printf("字节长度  ：%zu 字节\n", encoded.len);
    printf("字节流    ：");
    for (size_t i = 0; i < encoded.len; i++) {
        printf("%02X ", encoded.buf[i]);
    }
    printf("\n");

    /* ========== 第三步：UPER 解码 ========== */
    /*
     * v0.9.21 的 uper_decode 签名：
     *   uper_decode(ctx, type, &ptr, buf, size, skip_bits, unused_bits)
     * skip_bits=0, unused_bits=0 表示整包对齐解码
     */
    MeasureReport_t *decoded = NULL;   /* asn1c 负责 malloc */

    asn_dec_rval_t dec_rval = uper_decode(
        NULL,                          /* opt_codec_ctx，不限制栈深度 */
        &asn_DEF_MeasureReport,
        (void **)&decoded,
        encoded.buf,
        encoded.len,
        0,                             /* skip_bits */
        0                              /* unused_bits */
    );

    if (dec_rval.code != RC_OK) {
        fprintf(stderr, "解码失败，错误码：%d\n", dec_rval.code);
        free(encoded.buf);
        return 1;
    }

    printf("\n===== [解码还原数据] =====\n");
    printf("deviceId : %ld\n", get_integer(&decoded->deviceId));
    printf("voltage  : %ld mV  (= %.3f V)\n",
           get_integer(&decoded->voltage),
           get_integer(&decoded->voltage) / 1000.0);
    printf("current  : %ld mA  (= %.3f A)\n",
           get_integer(&decoded->current),
           get_integer(&decoded->current) / 1000.0);
    printf("status   : %s\n", decoded->status ? "ONLINE" : "OFFLINE");

    /* ========== 验证一致性 ========== */
    int ok = (get_integer(&decoded->deviceId) == get_integer(&report.deviceId))
          && (get_integer(&decoded->voltage)  == get_integer(&report.voltage))
          && (get_integer(&decoded->current)  == get_integer(&report.current))
          && (decoded->status == report.status);

    printf("\n===== [验证] =====\n");
    printf("编解码数据一致：%s\n", ok ? "YES (pass)" : "NO  (fail)");

    /* ========== 释放资源 ========== */
    /* decoded 是 uper_decode 分配的堆内存，FREE 会连带释放内部字段 */
    ASN_STRUCT_FREE(asn_DEF_MeasureReport, decoded);

    /* report 是栈上结构，只释放内部动态字段（不 free 结构体本身） */
    ASN_STRUCT_FREE_CONTENTS_ONLY(asn_DEF_MeasureReport, &report);

    free(encoded.buf);

    return ok ? 0 : 1;
}
```

---

## 6. 编译

### 方式一：build.ps1（推荐，放在 `per_demo/` 下）

```powershell
# build.ps1
$env:PATH = "D:\program\msys64\ucrt64\bin;" + $env:PATH

$EXCLUDE = @("converter-sample.c", "GeneralizedTime.c", "UTCTime.c")
$files = (Get-ChildItem "." -Filter "*.c" |
          Where-Object { $_.Name -notin $EXCLUDE } |
          ForEach-Object { $_.Name }) -join " "

$cmd = "gcc -I. -o per_demo.exe $files -Wall " +
       "-Wno-unused-variable -Wno-pointer-to-int-cast " +
       "-Wno-tautological-compare -Wno-unused-value -lws2_32"

Write-Host ">> $cmd"
Invoke-Expression "$cmd 2>&1"

if (Test-Path "per_demo.exe") {
    Write-Host "`n编译成功！运行："
    Write-Host "  .\per_demo.exe"
} else {
    Write-Host "`n编译失败，请检查上方错误信息。"
}
```

执行：
```powershell
cd per_demo
.\build.ps1
```

### 方式二：手动一行命令

```powershell
cd per_demo
$env:PATH = "D:\program\msys64\ucrt64\bin;" + $env:PATH
gcc -I. -o per_demo.exe $(
    Get-ChildItem *.c |
    Where-Object { $_.Name -notin @("converter-sample.c","GeneralizedTime.c","UTCTime.c") } |
    Select-Object -ExpandProperty Name
) -Wall -Wno-unused-variable -Wno-pointer-to-int-cast -Wno-tautological-compare -Wno-unused-value -lws2_32
```

---

## 7. 运行结果

```
===== [原始数据] =====
deviceId : 42
voltage  : 220000 mV  (= 220.000 V)
current  : 5000 mA  (= 5.000 A)
status   : ONLINE

===== [UPER 编码结果] =====
编码比特数：73
字节长度  ：10 字节
字节流    ：01 2A 03 03 5B 60 02 13 88 80

===== [解码还原数据] =====
deviceId : 42
voltage  : 220000 mV  (= 220.000 V)
current  : 5000 mA  (= 5.000 A)
status   : ONLINE

===== [验证] =====
编解码数据一致：YES (pass)
```

4 个字段只用了 **10 字节 / 73 比特**，UPER 对 INTEGER 不做字节对齐，极其紧凑。

---

## 8. 核心知识点

### 8.1 PER vs BER

| 维度 | BER（Basic Encoding Rules） | PER（Packed Encoding Rules） |
|---|---|---|
| 用途 | 通用，X.509/SNMP/LDAP | 通信协议（LTE/5G/IEC 61850） |
| 编码风格 | TLV，带类型标签和长度字段 | 紧凑比特流，无冗余元数据 |
| 大小 | 较大 | 极小 |
| 可读性 | 相对可调试 | 二进制，不可直读 |

### 8.2 UPER vs APER

| | UPER（Unaligned） | APER（Aligned） |
|---|---|---|
| 比特对齐 | 不对齐，能省最多空间 | 某些字段强制字节对齐 |
| 适用场景 | 空口协议（3GPP）、IEC 61850 | 其他需要字节对齐的场景 |

### 8.3 INTEGER_t 的存取

asn1c 的 `INTEGER_t` 底层是变长 `BIT STRING`，**不能直接读 `.buf`**，必须用辅助函数：

```c
asn_long2INTEGER(&obj, value);   // 写入
asn_INTEGER2long(&obj, &out);    // 读出
```

### 8.4 内存管理

| 场景 | 释放方式 |
|---|---|
| `uper_decode` 分配的结构体 | `ASN_STRUCT_FREE(type, ptr)` — 递归释放内部字段 + free 自身 |
| 栈上声明的结构体 | `ASN_STRUCT_FREE_CONTENTS_ONLY(type, &obj)` — 只释放内部动态字段，不 free 自身 |
| 编码缓冲区 | `free(buf)` 普通堆内存 |

### 8.5 工作流总结

```
example.asn1
     │
     ▼  asn1c -gen-PER -pdu=all -S skeletons -D per_demo
  per_demo/
  ├── MeasureReport.c/h     ← 由 ASN.1 生成
  ├── INTEGER.c/h           ┐
  ├── BOOLEAN.c/h           │ runtime skeleton
  ├── per_encoder.c/h       │ (来自 asn1c/skeletons)
  ├── per_decoder.c/h       ┘
  └── main.c                ← 手写业务逻辑
     │
     ▼  gcc -I. -o per_demo.exe *.c -lws2_32
  per_demo.exe
     │
     ▼  运行
  编码结果：01 2A 03 03 5B 60 02 13 88 80
  验证：YES (pass)
```
