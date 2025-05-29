# 数据类型

## Overview
- 数值类型
  - 位型
    - BIT：固定长度的位字段，最多64位，用的比较少
    - TINYINT：1字节，-128 ~ 127
  - 整数类型
    - TINYINT：-128 ~ 127，默认值为0，一个字节
    - SMALLINT：-32768 ~ 32767，默认值为0，两个字节
    - MEDIUMINT：-8388608 ~ 8388607，默认值为0，三个字节
    - INT：-2147483648 ~ 2147483647，默认值为0，四个字节
    - BIGINT：-9223372036854775808 ~ 9223372036854775807，默认值为0，八个字节
  - 浮点数类型
    - FLOAT：单精度浮点数，4个字节
    - DOUBLE：双精度浮点数，8个字节
    - DECIMAL：定点数，用于精确计算，存储为字符串
- 字符串类型、二进制类型
  - CHAR：固定长度字符串，最多255个字符
  - VARCHAR：可变长度字符串，最多65535（2^16 -1）个字符
  - TEXT：长文本字符串，最多65535个字符
  - LONGTEXT：更长的长文本字符串，最多4294967295（2^32 -1）个字符
  - BLOB：二进制大对象，用于存储二进制数据，如图片、音频、视频等,（2^16 -1）
  - LONGBLOB：更大的二进制大对象，用于存储更大的二进制数据，如图片、音频、视频等,（2^32 -1）
- 日期和时间类型
  - YEAR：年份，格式为YYYY
  - DATE：日期，格式为YYYY-MM-DD
  - TIME：时间，格式为HH:MM:SS
  - DATETIME：日期和时间，格式为YYYY-MM-DD HH:MM:SS
  - TIMESTAMP：时间戳，格式为YYYY-MM-DD HH:MM:SS，自动更新为当前时间
- 枚举类型
  - ENUM
- 集合类型
  - SET
- 空间类型
  - POINT
  - LINESTRING
  - POLYGON
  - GEOMETRY

## 整形

```sql
-- 创建一个名为 integer_types_demo 的表
CREATE TABLE integer_types_demo (
    -- TINYINT 类型，有符号，范围 -128 到 127
    tinyint_signed TINYINT,
    -- TINYINT 类型，无符号，范围 0 到 255
    tinyint_unsigned TINYINT UNSIGNED,
    -- SMALLINT 类型，有符号，范围 -32768 到 32767
    smallint_signed SMALLINT,
    -- SMALLINT 类型，无符号，范围 0 到 65535
    smallint_unsigned SMALLINT UNSIGNED,
    -- MEDIUMINT 类型，有符号，范围 -8388608 到 8388607
    mediumint_signed MEDIUMINT,
    -- MEDIUMINT 类型，无符号，范围 0 到 16777215
    mediumint_unsigned MEDIUMINT UNSIGNED,
    -- INT 类型，有符号，范围 -2147483648 到 2147483647
    int_signed INT,
    -- INT 类型，无符号，范围 0 到 4294967295
    int_unsigned INT UNSIGNED,
    -- BIGINT 类型，有符号，范围 -9223372036854775808 到 9223372036854775807
    bigint_signed BIGINT,
    -- BIGINT 类型，无符号，范围 0 到 18446744073709551615
    bigint_unsigned BIGINT UNSIGNED,
    -- 校验规则示例：确保 tinyint_signed 字段的值大于 0
    CONSTRAINT check_tinyint_signed_positive CHECK (tinyint_signed > 0)
);
```

## 位型
     
在 SQL 里，位类型（`BIT`）可以用来存储位值，常用于表示布尔值集合或者标志位。下面以 MySQL 为例，展示一个具有实际意义的位类型使用案例。

假设你正在开发一个游戏系统，需要记录玩家的成就信息。每个玩家可能有多个成就，例如“首次登录”、“通关第一关”、“获得 100 金币”等。我们可以使用位类型来高效存储这些成就信息，每个成就对应一个二进制位。

```sql
-- 创建一个名为 player_achievements 的表
CREATE TABLE player_achievements (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    player_name VARCHAR(50) NOT NULL,
    -- 使用 BIT(8) 类型存储 8 个成就标志位
    achievements BIT(8) DEFAULT b'00000000'
);

-- 插入一些示例数据
INSERT INTO player_achievements (player_name, achievements)
VALUES 
    ('Alice', b'00000001'),  -- 拥有“首次登录”成就
    ('Bob', b'00000011'),    -- 拥有“首次登录”和“通关第一关”成就
    ('Charlie', b'00000111'); -- 拥有“首次登录”、“通关第一关”和“获得 100 金币”成就

-- 查询拥有“首次登录”成就的玩家
SELECT player_name
FROM player_achievements
WHERE achievements & b'00000001';

-- 给玩家 'Bob' 添加“获得 100 金币”成就
UPDATE player_achievements
SET achievements = achievements | b'00000100'
WHERE player_name = 'Bob';

-- 再次查询玩家 'Bob' 的成就
SELECT player_name, BIN(achievements) AS achievements_binary
FROM player_achievements
WHERE player_name = 'Bob';
```

1. **表结构**：`player_achievements` 表包含 `player_id`、`player_name` 和 `achievements` 三个字段。`achievements` 字段使用 `BIT(8)` 类型，可以存储 8 个成就标志位。
2. **插入数据**：通过 `b'xxxxxxxxx'` 格式插入二进制值，表示玩家拥有的成就。
3. **查询数据**：使用按位与运算符 `&` 来检查玩家是否拥有某个成就。
4. **更新数据**：使用按位或运算符 `|` 来给玩家添加新的成就。

通过这种方式，位类型可以高效地存储和管理多个布尔值，节省存储空间。

## 浮点数

```sql
-- 创建一个名为 float_precision_test 的表
CREATE TABLE float_precision_test (
    id INT AUTO_INCREMENT PRIMARY KEY,
    float_column FLOAT,
    double_column DOUBLE,
    decimal_column DECIMAL(30, 25)
);

-- 插入一个有多位小数的数值
INSERT INTO float_precision_test (float_column, double_column, decimal_column)
VALUES (3.1415926535897932384626433832795, 3.1415926535897932384626433832795, 3.1415926535897932384626433832795);

-- 查询插入的数据
SELECT * FROM float_precision_test;
```

```bash
mysql> SELECT * FROM float_precision_test;
+----+--------------+-------------------+-----------------------------+
| id | float_column | double_column     | decimal_column              |
+----+--------------+-------------------+-----------------------------+
|  1 |      3.14159 | 3.141592653589793 | 3.1415926535897932384626434 |
+----+--------------+-------------------+-----------------------------+
1 row in set (0.002 sec)
```

## 字符类型

注意⚠️：`VARCHAR`保存的字符串，并不是每一个字符都占用一个字节，而是根据实际字符长度来分配空间。其中1-3个字节存储字符长度，后面的字节存储实际字符！！最多保存65535个字节。（utf最大保存 $2^{16-3}/3$ 个字符，因为其中的1-3个字节需要保存长度。）
* `gbk`编码：一个汉字占用2个字节，一个英文字母占用1个字节。对应 $(2^{16}-1 - 3)/2 = 32766$ 个字符
* `utf8`编码：一个汉字占用3个字节，一个英文字母占用1个字节。对应 $(2^{16}-1 -3)/3 = 21844$ 个字符


```sql
-- 创建一个名为 char_varchar_test 的表
CREATE TABLE char_varchar_test (
    id INT AUTO_INCREMENT PRIMARY KEY,
    char_column CHAR(10),
    varchar_column VARCHAR(10)
);
-- 插入不同长度的字符串
INSERT INTO char_varchar_test (char_column, varchar_column)
VALUES ('abc', 'abc'), ('abcdefghij', 'abcdefghij');
-- 查询插入的数据
SELECT * FROM char_varchar_test;
```

* 对比分析：
  - CHAR 类型 ：固定长度字符串类型，会用空格填充不足的长度。例如，插入 'abc' 到 CHAR(10) 字段中，实际存储为 'abc       ' （后面有 7 个空格）。**CHAR不区分字符还是汉字，都按最多的保存，比如CHAR(3)可以是'abc'也可以是'哈哈哈'**
  - VARCHAR 类型 ：可变长度字符串类型，只会存储实际长度的字符串。例如，插入 'abc' 到 VARCHAR(10) 字段中，实际存储为 'abc' 。另外，**VARCHAR(10)代表最多十个字符而不是字节，所以如果是中文的话，会多于10个字节，具体多少字节根据编码决定**。【**VARCHAR除了内部存放字符串意外以外，本身还需要一到三个字节进行长度的保存**】

* 适用场景：
  - CHAR 类型 ：适用于存储长度固定的字符串，如身份证号、手机号等。由于长度固定，查询速度可能更快。
  - VARCHAR 类型 ：适用于存储长度可变的字符串，如用户名、地址等。可以节省存储空间。

## 日期和时间类型

```sql
-- 创建一个名为 datetime_test 的表
CREATE TABLE datetime_test (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date_column DATE,
    time_column TIME,
    datetime_column DATETIME,
    timestamp_column TIMESTAMP
)
```

```sql
-- 自动更新的版本
CREATE TABLE datetime_test2 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date_column DATE,
    time_column TIME,
    datetime_column DATETIME,
    timestamp_column TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)
```

```sql
-- 插入示例数据
INSERT INTO datetime_test (date_column, time_column, datetime_column, timestamp_column)
-- 插入自动更新的版本，在这个例子中，没有为 timestamp_column 提供值，MySQL 会自动将插入时的时间戳填充到该字段。
INSERT INTO datetime_test2 (date_column, time_column, datetime_column, timestamp_column)
VALUES
    ('2024-01-01', '12:30:45', '2024-01-01 12:30:45', '2024-01-01 12:30:45'),
    ('2024-01-02', '13:30:45', '2024-01-02 13:30:45', '2024-01-02 13:30:45'),
    ('2024-01-03', '14:30:45', '2024-01-03 14:30:45', '2024-01-03 14:30:45');
```

## Example

​**​创建一个员工表 emp（课堂练习），选用适当的数据类型​**​  `createtable.sql`

|字段|属性|
|---|---|
|Id|整形|
|name|字符型|
|sex|字符型|
|birthday|日期型 (date)|
|entry_date|日期型 (date)|
|job|字符型|
|Salary|小数型|
|resume|文本型|


```sql
CREATE TABLE emp (
    Id INT PRIMARY KEY,
    name VARCHAR(50),
    sex CHAR(1),
    birthday DATE,
    entry_date DATE,
    job VARCHAR(100),
    Salary DECIMAL(10, 2),
    resume TEXT
)CHARSET utf8 COLLATE utf8_bin ENGINE INNODB;
```

