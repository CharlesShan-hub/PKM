```java
/**
 * 演示所有Javadoc标签的最小化示例
 * @author 示例作者
 * @version 1.0
 * @since 1.0
 */
public class AllJavadocTags {
    /** 
     * 示例常量
     * {@value}
     */
    public static final String CONSTANT = "VALUE";

    /**
     * 示例字段
     * @serial
     */
    private int field;

    /**
     * @deprecated 已弃用的方法
     */
    @Deprecated
    public void deprecatedMethod() {}

    /**
     * 示例方法
     * @param param 参数说明
     * @return 返回值说明
     * @throws Exception 异常说明
     * @exception RuntimeException 运行时异常
     * @see Object
     * {@link String}
     * {@linkplain Integer}
     * {@inheritDoc}
     * @serialData 序列化数据说明
     * @serialField 字段名 字段类型 字段说明
     */
    public String exampleMethod(String param) throws Exception {
        return param;
    }

    /**
     * 主方法
     * @param args 命令行参数
     * {@docRoot}
     */
    public static void main(String[] args) {
        System.out.println("包含所有Javadoc标签的最小示例");
    }
}
```