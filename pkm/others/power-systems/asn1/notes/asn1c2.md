# IEC 61850 MMS ASN.1 转换 C 快速指南

## 已完成的工作
1. ✅ 使用 asn1c v0.9.21 将 `mms.asn` 转换为 C 代码
2. ✅ 解决 Windows/MSYS2 环境所有编译问题
3. ✅ 编译完成：0 错误，0 警告
4. ✅ 生成 68 个 `.o` 对象文件

## 核心问题与解决方案
| 问题 | 解决方案 | 备注 |
|------|----------|------|
| bool 字段冲突 | `-Dbool=mms_bool` | GCC -std=gnu11 下 bool 是关键字 |
| Windows symlink | 手动复制骨架文件 | 复制 `asn1c/skeletons/` 下所有文件 |
| ntohl 未定义 | `-lws2_32` | 链接 Windows Socket 库 |
| POSIX API 缺失 | 排除 `GeneralizedTime.c` `UTCTime.c` | 不影响 MMS 核心功能 |

## 1.0 从asn1文件生成c

（技术备份，后边有更新的脚本，这个版本不能进行静态代码库的打包）

```powershell
# 1. 进入 mms_c 目录
cd d:\program\msys64\home\17428\temp\mms_c

# 2. 编译所有代码
.\build_mms.ps1

# 3. 在您的项目中使用
gcc -I./mms_c your_app.c mms_c/*.o -lws2_32 -Dbool=mms_bool
```

`build_mms.ps1`
```powershell
# IEC 61850 MMS ASN.1 C 代码构建脚本 (Windows/MSYS2)
# 针对 Windows UCRT/MSYS2 环境，解决 asn1c 生成代码的编译问题

$env:PATH = "D:\program\msys64\ucrt64\bin;" + $env:PATH

# 需要排除的文件（POSIX API 在 Windows 上不可用）
$EXCLUDE = @("converter-sample.c", "GeneralizedTime.c", "UTCTime.c")

# 获取所有需要编译的 .c 文件
$c_files = (Get-ChildItem "." -Filter "*.c" | Where-Object { $_.Name -notin $EXCLUDE } | ForEach-Object { $_.Name }) -join " "

if ($c_files.Length -eq 0) {
    Write-Host "错误：未找到 .c 文件" -ForegroundColor Red
    exit 1
}

# 编译命令
# 关键：-Dbool=mms_bool 解决 bool 字段名与 GCC 关键字冲突问题
# -lws2_32 链接 Windows Socket 库（ntohl 等函数）
$cmd = "gcc -I. -c $c_files -Dbool=mms_bool -Wall -Wno-unused-variable -Wno-pointer-to-int-cast -Wno-tautological-compare -Wno-unused-value"

Write-Host "正在编译 MMS ASN.1 C 代码..." -ForegroundColor Cyan
Write-Host "命令: $cmd" -ForegroundColor Gray

# 执行编译
Invoke-Expression "$cmd 2>&1" | ForEach-Object {
    if ($_ -match "error|错误") {
        Write-Host $_ -ForegroundColor Red
    } elseif ($_ -match "warning|警告") {
        Write-Host $_ -ForegroundColor Yellow
    } else {
        Write-Host $_
    }
}

# 检查编译结果
$object_count = (Get-ChildItem -Filter "*.o" | Measure-Object).Count
Write-Host "`n编译完成，生成 $object_count 个 .o 文件" -ForegroundColor Green

# 创建静态库（可选）
Write-Host "`n创建静态库 mms_c.a ..." -ForegroundColor Cyan
$ar_cmd = "ar rcs mms_c.a *.o"
Invoke-Expression "$ar_cmd 2>&1"

if (Test-Path "mms_c.a") {
    $lib_size = (Get-Item "mms_c.a").Length / 1KB
    Write-Host "静态库创建成功: mms_c.a ($([math]::Round($lib_size, 2)) KB)" -ForegroundColor Green
}

# 验证编译结果
Write-Host "`n验证关键头文件..." -ForegroundColor Cyan
if (Test-Path "MMSpdu.h") {
    Write-Host "✓ MMSpdu.h 存在 - 主 PDU 定义" -ForegroundColor Green
}
if (Test-Path "Data.h") {
    Write-Host "✓ Data.h 存在 - 数据类型定义" -ForegroundColor Green
}
if (Test-Path "constr_SEQUENCE.h") {
    Write-Host "✓ constr_SEQUENCE.h 存在 - ASN.1 结构支持" -ForegroundColor Green
}
if (Test-Path "per_encoder.h") {
    Write-Host "✓ per_encoder.h 存在 - PER 编码器" -ForegroundColor Green
}
if (Test-Path "per_decoder.h") {
    Write-Host "✓ per_decoder.h 存在 - PER 解码器" -ForegroundColor Green
}

Write-Host "`n构建完成！" -ForegroundColor Cyan
Write-Host "生成的 C 代码已准备就绪，可用于您的 IEC 61850 MMS 项目。" -ForegroundColor Cyan
Write-Host ""
Write-Host "使用说明：" -ForegroundColor Yellow
Write-Host "1. 在您的项目中包含 mms_c/ 目录中的所有 .h 文件" -ForegroundColor White
Write-Host "2. 链接时使用: -L/path/to/mms_c -lmms_c -lws2_32" -ForegroundColor White
Write-Host "3. 或者直接使用编译好的 .o 文件: gcc -I/path/to/mms_c your_app.c *.o -lws2_32" -ForegroundColor White
Write-Host "4. 关键编译标志: -Dbool=mms_bool (必须添加！)" -ForegroundColor White
```

## 2.0 asn1生成c并打包dll

下边第二个脚本我进行了简化，从asn1文件，编译成c文件，然后打包成动态链接库，方便后续java调用

```powershell
# ASN.1 → DLL 构建脚本
# 一键从 ASN.1 文件生成可用的 DLL

# ============ 配置参数 ============
$asn1_file = "D:\program\msys64\home\17428\temp\mms.asn"
$asn1c_path = "D:\program\asn1c\bin\asn1c.exe"
$skeletons_dir = "D:\program\asn1c\skeletons"
$output_dir = "D:\program\msys64\home\17428\temp\mms_dll_output"

$env:PATH = "D:\program\msys64\ucrt64\bin;" + $env:PATH

# ============ 清理输出目录 ============
Write-Host "清理输出目录..." -ForegroundColor Yellow
if (Test-Path $output_dir) { Remove-Item $output_dir -Recurse -Force }
New-Item -ItemType Directory -Path $output_dir | Out-Null

# ============ 生成 C 代码 ============
Write-Host "生成 C 代码..." -ForegroundColor Yellow
$gen_cmd = "$asn1c_path -gen-PER -pdu=all -S $skeletons_dir -D $output_dir $asn1_file"
Invoke-Expression $gen_cmd 2>&1 | Out-Null

# ============ 复制骨架文件 ============
Write-Host "复制骨架文件..." -ForegroundColor Yellow
Copy-Item "$skeletons_dir\*.c" $output_dir
Copy-Item "$skeletons_dir\*.h" $output_dir

# ============ 编译所有 .c 文件 ============
Set-Location $output_dir

Write-Host "编译所有 C 文件..." -ForegroundColor Yellow
$exclude_files = "converter-sample.c", "GeneralizedTime.c", "UTCTime.c"
$c_files = Get-ChildItem -Filter "*.c" | Where-Object { $_.Name -notin $exclude_files }
$c_file_names = ($c_files | ForEach-Object { $_.Name }) -join " "

if ($c_file_names.Length -eq 0) {
    Write-Host "错误：未找到 .c 文件" -ForegroundColor Red
    exit 1
}

$compile_cmd = "gcc -I. -c $c_file_names -Dbool=mms_bool -fPIC -Wall"
Invoke-Expression $compile_cmd 2>&1 | Out-Null

# ============ 创建 DLL ============
Write-Host "创建 mms.dll..." -ForegroundColor Yellow
$dll_cmd = "gcc -shared -o mms.dll *.o -lws2_32"
Invoke-Expression $dll_cmd 2>&1 | Out-Null

# ============ 验证结果 ============
if (Test-Path "mms.dll") {
    $size = (Get-Item "mms.dll").Length / 1KB
    Write-Host "`n✅ 成功创建: mms.dll ($([math]::Round($size, 2)) KB)" -ForegroundColor Green
    Write-Host "   位置: $output_dir\mms.dll" -ForegroundColor Gray
    
    $object_count = (Get-ChildItem -Filter "*.o" | Measure-Object).Count
    Write-Host "   编译文件: $object_count 个 .o 文件" -ForegroundColor Gray
    Write-Host "   头文件: $( (Get-ChildItem -Filter "*.h" | Measure-Object).Count ) 个 .h 文件" -ForegroundColor Gray
    
    Write-Host "`n🚀 Java JNI 使用:" -ForegroundColor Cyan
    Write-Host "   System.loadLibrary(`"mms`")" -ForegroundColor White
    Write-Host "   DLL 路径添加到 JVM: -Djava.library.path=$output_dir" -ForegroundColor White
    Write-Host "   JNI 头文件: #include `"MMSpdu.h`"" -ForegroundColor White
} else {
    Write-Host "`n❌ 创建 DLL 失败" -ForegroundColor Red
}

Write-Host "`n🏁 构建完成" -ForegroundColor Cyan
```

## 关键文件
- `MMSpdu.h` - 主 PDU 定义入口
- `Data.h` - 数据类型定义
- `per_encoder.h/per_decoder.h` - PER 编解码器

## 内存管理
```c
// 分配
MMSpdu_t *pdu = calloc(1, sizeof(MMSpdu_t));

// 释放
ASN_STRUCT_FREE(asn_DEF_MMSpdu, pdu);
```

## 编码示例
```c
#include "MMSpdu.h"
#include "per_encoder.h"

// 填充 pdu...
DynBuf buf = { NULL, 0 };
asn_enc_rval_t r = uper_encode(&asn_DEF_MMSpdu, &pdu, encode_cb, &buf);
```

## 下一步建议
1. 编写简单的 MMS 消息测试程序
2. 集成到您的 IEC 61850 项目
3. 验证协议一致性
4. 性能调优和内存优化

---
**生成时间**: 2026-04-14  
**状态**: 准备就绪 ✅