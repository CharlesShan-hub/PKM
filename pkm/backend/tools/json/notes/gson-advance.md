
## Part 3：高级场景与二次开发

> 目标：掌握自定义适配器、流式解析、框架集成等高级用法，能解决真实项目中的复杂场景。

---

## 3.1 压力测试

按照官方文档：反序列化的字符串可支持 25MB，已序列化包含 140 万个对象的数据集，反序列化了包含 87,000 个对象的集合。（下面是[原文](https://google.github.io/gson/UserGuide.html)） 

* 该台机配备了双 Opteron 处理器、8GB 内存，操作系统为 64 位版本的 Ubuntu。在测试过程中，我们还同时运行了其他应用程序。您可以通过使用类 `PerformanceTest` 来重新运行这些测试。
- Strings: Deserialized strings of over 25MB without any problems (see `disabled_testStringDeserializationPerformance` method in `PerformanceTest`)  
    字符串：反序列化的字符串大小超过 25MB，但没有任何问题（参见 `PerformanceTest` 中的 `disabled_testStringDeserializationPerformance` 方法）
- Large collections:
    - 已序列化包含 140 万个对象的数据集（详情请参阅 `PerformanceTest` 中的 `disabled_testLargeCollectionSerialization` 方法）
    - 已反序列化了包含 87,000 个对象的集合（详情请参阅 `disabled_testLargeCollectionDeserialization` 中的 `PerformanceTest` ）
- Gson 1.4 版本将字节数组和集合的反序列化限制从 80KB 提高到了超过 11MB。








### 3.1 自定义 `TypeAdapter` / `JsonSerializer` / `JsonDeserializer`

#### 三者区别

| 接口 | 作用 | 使用场景 |
|------|------|---------|
| `JsonSerializer<T>` | 只控制序列化（对象 → JSON） | 只想改输出格式，不关心解析 |
| `JsonDeserializer<T>` | 只控制反序列化（JSON → 对象） | 只想改解析逻辑，不关心输出 |
| `TypeAdapter<T>` | 同时控制序列化和反序列化 | 需要对类型完全掌控 |

#### 示例 1：自定义 `JsonSerializer`（脱敏手机号）

```java
public class PhoneSerializer implements JsonSerializer<String> {
    @Override
    public JsonElement serialize(String phone, Type typeOfSrc, JsonSerializationContext context) {
        if (phone == null || phone.length() < 7) {
            return new JsonPrimitive(phone);
        }
        // 138****5678
        String masked = phone.substring(0, 3) + "****" + phone.substring(7);
        return new JsonPrimitive(masked);
    }
}

// 使用
public class User {
    @JsonAdapter(PhoneSerializer.class)
    private String phone;
}
```

#### 示例 2：自定义 `JsonDeserializer`（处理日期多种格式）

```java
public class FlexibleDateDeserializer implements JsonDeserializer<Date> {
    private static final String[] FORMATS = {
        "yyyy-MM-dd HH:mm:ss",
        "yyyy-MM-dd",
        "yyyy/MM/dd"
    };

    @Override
    public Date deserialize(JsonElement json, Type typeOfT, JsonDeserializationContext context)
            throws JsonParseException {
        String dateStr = json.getAsString();
        for (String format : FORMATS) {
            try {
                return new SimpleDateFormat(format).parse(dateStr);
            } catch (ParseException e) {
                // 继续尝试下一种格式
            }
        }
        throw new JsonParseException("无法解析日期: " + dateStr);
    }
}

// 使用
Gson gson = new GsonBuilder()
    .registerTypeAdapter(Date.class, new FlexibleDateDeserializer())
    .create();
```

#### 示例 3：自定义 `TypeAdapter`（处理不可变类）

```java
public class Point {
    public final int x;
    public final int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class PointAdapter extends TypeAdapter<Point> {
    @Override
    public void write(JsonWriter out, Point point) throws IOException {
        out.beginObject();
        out.name("x").value(point.x);
        out.name("y").value(point.y);
        out.endObject();
    }

    @Override
    public Point read(JsonReader in) throws IOException {
        int x = 0, y = 0;
        in.beginObject();
        while (in.hasNext()) {
            String name = in.nextName();
            switch (name) {
                case "x": x = in.nextInt(); break;
                case "y": y = in.nextInt(); break;
                default: in.skipValue(); break;
            }
        }
        in.endObject();
        return new Point(x, y);  // 直接构造，不走反射
    }
}

// 使用
Gson gson = new GsonBuilder()
    .registerTypeAdapter(Point.class, new PointAdapter())
    .create();
```

---

### 3.2 自定义 `TypeAdapterFactory`：批量拦截

```java
// 场景：把所有 LocalDateTime 统一转成时间戳
public class LocalDateTimeFactory implements TypeAdapterFactory {
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
        if (type.getRawType() != LocalDateTime.class) {
            return null;  // 返回 null 表示不处理，交给下一个 Factory
        }
        return (TypeAdapter<T>) new TypeAdapter<LocalDateTime>() {
            @Override
            public void write(JsonWriter out, LocalDateTime value) throws IOException {
                if (value == null) {
                    out.nullValue();
                } else {
                    out.value(value.atZone(ZoneId.systemDefault()).toInstant().toEpochMilli());
                }
            }

            @Override
            public LocalDateTime read(JsonReader in) throws IOException {
                return LocalDateTime.ofInstant(
                    Instant.ofEpochMilli(in.nextLong()), ZoneId.systemDefault());
            }
        };
    }
}

// 使用
Gson gson = new GsonBuilder()
    .registerTypeAdapterFactory(new LocalDateTimeFactory())
    .create();
```

> 💡 **Factory 比单个 Adapter 更强大**：可以基于类型做条件判断，且注册顺序影响优先级。

---

### 3.3 `@JsonAdapter` 注解：局部指定

```java
public class User {
    @JsonAdapter(FlexibleDateDeserializer.class)
    private Date birthday;   // 只对 birthday 字段生效

    private Date createdAt;  // 使用全局配置
}
```

> 注解优先级 > `registerTypeAdapter()` 全局注册。

---

### 3.4 流式解析：`JsonReader` / `JsonWriter`

#### 什么时候用流式？
- 处理超大 JSON（几十 MB 以上），避免 OOM
- 只需要 JSON 中的某几个字段，不想全部加载

```java
// 流式读取：只取 name 字段
try (JsonReader reader = new JsonReader(new FileReader("large.json"))) {
    reader.beginObject();
    while (reader.hasNext()) {
        String name = reader.nextName();
        if ("name".equals(name)) {
            System.out.println("name: " + reader.nextString());
            break;
        } else {
            reader.skipValue();  // 跳过不需要的值
        }
    }
    reader.endObject();
}
```

```java
// 流式写入：边生成边写，不占内存
try (JsonWriter writer = new JsonWriter(new FileWriter("output.json"))) {
    writer.setIndent("  ");  // 美化输出
    writer.beginArray();
    for (int i = 0; i < 1000000; i++) {
        writer.beginObject();
        writer.name("id").value(i);
        writer.name("name").value("user_" + i);
        writer.endObject();
    }
    writer.endArray();
}
```

---

### 3.5 与框架集成

#### Spring Boot 替换默认 Jackson

```java
@Configuration
public class GsonConfig {

    @Bean
    public Gson gson() {
        return new GsonBuilder()
            .serializeNulls()
            .setDateFormat("yyyy-MM-dd HH:mm:ss")
            .setLongSerializationPolicy(LongSerializationPolicy.STRING)
            .create();
    }

    @Bean
    public GsonHttpMessageConverter gsonHttpMessageConverter() {
        return new GsonHttpMessageConverter(gson());
    }
}
// 注意：如果同时存在 Jackson 和 Gson，需要 @Primary 或排除 JacksonAutoConfiguration
```

#### Retrofit 使用 Gson

```java
Retrofit retrofit = new Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create(gson))
    .build();
```

---

### 3.6 性能对比与优化

| 库 | 优点 | 缺点 | 适用场景 |
|----|------|------|---------|
| **Gson** | 简单易用、注解丰富、Google 出品 | 反射导致性能一般 | 中小型项目、快速开发 |
| **Jackson** | 性能好、生态好（Jackson-databind） | 配置相对复杂 | 大型项目、高并发 |
| **Fastjson** | 性能极好 | 安全问题频出（反序列化漏洞） | 阿里巴巴系项目（不建议新项目用） |

#### 性能优化建议

```java
// 1. 全局复用 Gson 实例（不要每次 new）
private static final Gson gson = new GsonBuilder().create();

// 2. 使用 .create() 而非 new Gson()（后者有历史遗留配置）

// 3. 对热对象预生成 TypeAdapter 缓存
private static final TypeAdapter<User> userAdapter =
    new Gson().getAdapter(User.class);
// 后续直接 userAdapter.toJson(user) / userAdapter.fromJson(json)
// 避免每次调用都走一次 Adapter 查找
```

---

### 3.7 实战场景设计

#### 场景 1：接口版本兼容

```java
public class User {
    @Since(1.0)
    private String name;

    @Since(2.0)
    private String nickname;  // 2.0 才有的字段

    @Until(1.5)
    private String oldField;  // 1.5 之后废弃
}

Gson gsonV1 = new GsonBuilder().setVersion(1.0).create();
Gson gsonV2 = new GsonBuilder().setVersion(2.0).create();
```

#### 场景 2：字段脱敏（全局配置）

```java
public class SensitiveFieldProcessor implements JsonSerializer<Object> {

    @Override
    public JsonElement serialize(Object value, Type typeOfSrc, JsonSerializationContext context) {
        if (value instanceof CharSequence && isSensitive(typeOfSrc.getTypeName())) {
            String str = (String) value;
            if (str.length() > 8) {
                return new JsonPrimitive(str.substring(0, 4) + "****" + str.substring(str.length() - 4));
            }
        }
        return context.serialize(value, typeOfSrc);
    }

    private boolean isSensitive(String typeName) {
        // 可以根据字段名/类型判断，如 phone、idCard、password 等
        return typeName.toLowerCase().contains("phone")
            || typeName.toLowerCase().contains("idcard")
            || typeName.toLowerCase().contains("password");
    }
}
```

#### 场景 3：统一 null 处理

```java
// 场景：后端不想输出 null，想统一输出空字符串或空数组
public class NullToEmptyAdapterFactory implements TypeAdapterFactory {

    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
        Class<T> rawType = (Class<T>) type.getRawType();

        // 基础类型交给默认处理
        if (rawType == String.class) {
            return (TypeAdapter<T>) new TypeAdapter<String>() {
                @Override
                public void write(JsonWriter out, String value) throws IOException {
                    out.value(value == null ? "" : value);
                }

                @Override
                public String read(JsonReader in) throws IOException {
                    if (in.peek() == JsonToken.NULL) {
                        in.nextNull();
                        return "";
                    }
                    return in.nextString();
                }
            };
        }
        return null;  // 其他类型不处理
    }
}
```

---

### 3.8 小结

到这里你已经掌握了 Gson 的全部核心知识：

- **Part 1**：会用 —— 基本 API、常见场景
- **Part 2**：懂原理 —— 核心类、注解、内部机制、常见坑
- **Part 3**：能扩展 —— 自定义适配器、流式解析、框架集成、实战场景

以后遇到 Gson 不够用的场景，你已经知道该怎么"二次开发"了。
