
# Smile

## Links

* \[1] wiki：[https://en.wikipedia.org/wiki/Smile\_(data\_interchange\_format)](https://en.wikipedia.org/wiki/Smile\_\(data\_interchange\_format\))
* \[2]specification：[https://github.com/FasterXML/smile-format-specification](https://github.com/FasterXML/smile-format-specification)

## Notes

{% hint style="info" %}
**总的来讲这还是一个比较小众的标记类型，主要目标是原生的 json 的序列化版本，不加功能，只追求效率**
{% endhint %}

> Wiki\[1] 上边说的比较少，我们从官方介绍\[2]里边进行总结

1. 为什么要再弄一个 Smile 而不用 BSON？ 因为BSON不完全兼容JSON，他提供了很多新的数据类型。
2. 目标
   * MUST support all logical JSON events; should not add extensions beyond what existing [Jackson API](https://github.com/FasterXML/jackson) offers.\
     必须支持所有逻辑JSON事件;不应添加超出现有杰克逊API提供的扩展。
   * SHOULD be reasonably space-efficient (compact); to reduce "fluff"; especially to degree this can help processing efficiency.\
     应合理节省空间（紧凑）;以减少“绒毛”;特别是在一定程度上，这可以帮助处理效率。
   * SHOULD be both efficient to read (deserialize) AND write (serialize): many binary formats make significant sacrifices in write speed.\
     读（串行化）和写（串行化）都应该高效：许多二进制格式在写速度上做出了重大牺牲。
   * SHOULD avoid overly complex structures and algorithms\
     应避免过于复杂的结构和算法
   * SHOULD avoid fragility:  应避免脆性：
     * Keep enough redundancy to allow for some self-consistency checks; specifically, there should be byte sequences that are invalid, to make detection of invalid content possible.\
       保持足够的冗余以允许一些自一致性检查;特别是，应该有无效的字节序列，以使检测无效内容成为可能。
     * Add explicit format version number (nothing drastic, even a nibble will do)\
       添加明确的格式版本号（没有什么激烈的，甚至一个半字节将做）
   * MUST support auto-detection: Use a unique header ("magic cookie")\
     必须支持自动检测：使用一个唯一的头（“魔法cookie”）
   * SHOULD allow simple concatenation of content; that is, concatenation of valid properly nested sequences (that is, no open start object or start array markers) must be legal format in itself\
     应该允许简单的内容连接;也就是说，正确嵌套的有效序列的连接（即，没有打开的开始对象或开始数组标记）本身必须是法律的格式
     * Aimed to allow chunked content output\
       旨在允许分块内容输出
   * SHOULD allow proper streaming: that is, amount of required buffering can not exceed some fixed constant, size of which is related to low-level buffering, not to length of content to encoded. Note, however, that in cases where Jackson API itself imposes limits (case for embedded binary data; as well as for String values to output), implementation can make use of this existing limitation\
     应该允许正确的流：也就是说，所需的缓冲量不能超过某个固定常数，该常数的大小与低级缓冲有关，而与要编码的内容的长度无关。但是，请注意，在杰克逊API本身施加限制的情况下（嵌入的二进制数据的情况;以及要输出的String值的情况），实现可以利用此现有限制
     * This specifically prevents pervasive use of length-prefix for Strings: to know byte-length of a Java String, one would need to either do additional passes (first to calculate length, second to encode), or to buffer encoded output in memory.\
       这特别防止了对String的长度前缀的普遍使用：要知道Java String的字节长度，需要进行额外的传递（首先计算长度，其次编码），或者在内存中缓冲编码的输出。
   * SHOULD support simple framing through the use of byte 0xFF (end marker) -- ability to separate binary-encoded content segments from each other AND efficiently scan to find these boundaries _without_ having to parse/decode contents. Framing is easy to do with textual JSON by using something as simple as linefeed, since linefeeds are always quoted in String values, as long as no indentation is used.\
     应该通过使用字节0xFF（结束标记）来支持简单的成帧--能够将二进制编码的内容段彼此分离，并有效地扫描以找到这些边界_，而不必_解析/解码内容。使用文本JSON很容易实现框架化，只需使用像linefeed这样简单的东西，因为只要不使用缩进，linefeed总是在String值中引用。
     * Means that effort should be made to avoid use of end marker byte when encoding content\
       表示在编码内容时应尽量避免使用结束标记字节
3. 非目标
   * SHOULD NOT over-optimize for minimal compactness: that's what compression can be used for.\
     **不应该为了最小的紧凑性而过度优化**：这就是压缩的用途。
   * SHOULD NOT extend model beyond basic JSON data types; with exception of natively supporting binary content (which for textual JSON is supported using Base64 encoded text).\
     **不应该将模型扩展到基本JSON数据类型之外**;除了原生支持二进制内容（对于文本JSON，使用Base64编码文本支持）。
   * NEED NOT design for random-access: low-level Jackson APIs are designed for sequential access; can implement "low-hanging fruits" if that makes sense.\
     不需要为随机访问而设计：低级杰克逊API是为顺序访问而设计的;如果有意义，可以实现“低垂的果实”。
   * NEED NOT support extensive configurability: only settings that are considered obviously useful (or requested) should be added.\
     不需要支持广泛的可配置性：只应添加被认为明显有用（或请求）的设置。

