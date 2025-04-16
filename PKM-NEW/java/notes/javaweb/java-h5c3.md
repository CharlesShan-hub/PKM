# H3C3

## 资料

* 文档去找mdn： https://developer.mozilla.org/en-US/

## HTML

### 入门案例

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!--字符集-->
    <meta charset="UTF-8">
    <!--设置网页在移动设备上的现实宽度及缩放比例-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hello World</h1>
    <p>Hello World</p>
</body>
</html>
```

### 常见标签和样式

* 引入CSS方式
    1. 内部样式
        ```html
        <style>
            /* CSS代码 */
        </style>
        ```
    2. 外部样式
        ```html
        <link rel="stylesheet" href="CSS_FILE_PATH">
        ```
    3. 行内样式
        ```html
        <h1 style="color: red;">Hello World</h1>
        ```
    ```html
    <html>
    <head>
        <title>Document</title>
        <!--外部样式-->
        <link rel="stylesheet" href="CSS_FILE_PATH">
        <!--内部样式-->
        <style>
            p{
                color: red;
            }
        </style>
    </head>
    <body>
        <!--行内样式-->
        <h1 style="color: red;">Hello World</h1>
        <p>Hello</p>
        <span>World</span>
    </body>
    </html>
    ```
    ```css
    span{
        color: #000000;
    }
    ```

* 引入JS文件
    ```html
    <script src="JS_FILE_PATH"></script>
    ```
* h1-h6：标题标签，h1为最大标题，h6为最小标题
    ```html
    <h1>Hello World</h1>
    <h2>Hello World</h2>
    <h3>Hello World</h3>
    <h4>Hello World</h4>
    <h5>Hello World</h5>
    <h6>Hello World</h6>
    ```
* p：段落标签，不会换行
    ```html
    <p>Hello World</p>
    ```
* a：锚点标签，用于链接到其他页面
    * href：指定链接的地址
    * target：指定链接的打开方式，默认为_self，即当前窗口打开，_blank为新窗口打开
    ```html
    <a href="URL_ADDRESS">百度</a>
    <a href="URL_ADDRESS" target="_blank">百度</a>
    ```
* img：图片标签，用于显示图片
    * src：指定图片的地址
    * alt：指定图片的替代文本，用于图片加载失败时显示
    ```html
    <img src="URL_ADDRESS" alt="图片描述">
    ```
* ul：无序列表标签，用于显示一组无序列表
    * li：列表项标签，用于显示列表项
    ```html
    <ul>
        <li>列表项1</li>
        <li>列表项2</li>
        <li>列表项3</li>
    </ul>
    ```
* ol：有序列表标签，用于显示一组有序列表
    * li：列表项标签，用于显示列表项
    ```html
    <ol>
        <li>列表项1</li>
        <li>列表项2</li>
        <li>列表项3</li>
    </ol>
    ```
* table：表格标签，用于显示表格
    * tr：表格行标签，用于显示表格行
    * td：表格单元格标签，用于显示表格单元格
    ```html
    <table>
        <tr>
            <td>单元格1</td>
            <td>单元格2</td>
            <td>单元格3</td>
        </tr>
        <tr>
            <td>单元格4</td>
            <td>单元格5</td>
            <td>单元格6</td>
        </tr>
    </table>
    ```
* div：块级元素标签，用于显示一块区域
    * span：行内元素标签，用于显示一行文本
    ```html
    <div>
        <span>文本1</span>
        <span>文本2</span>
        <span>文本3</span>
    </div>
    ```
* button：按钮标签，用于显示按钮
    * type：指定按钮的类型，默认为submit，即提交按钮，button为普通按钮
    ```html
    <button type="submit">提交</button>
    <button type="button">普通按钮</button>
    ```
* input：输入框标签，用于显示输入框
    * type：指定输入框的类型，默认为text，即文本输入框，password为密码输入框，radio为单选框，checkbox为多选框，submit为提交按钮，button为普通按钮
    ```html
    <input type="text" placeholder="请输入文本">
    <input type="password" placeholder="请输入密码">
    <input type="radio" name="radio">单选框
    <input type="checkbox" name="checkbox">多选框
    <input type="submit" value="提交">
    <input type="button" value="普通按钮">
    ```
* select：下拉框标签，用于显示下拉框
    * option：下拉框选项标签，用于显示下拉框选项
    ```html
    <select>
        <option value="option1">选项1</option>
        <option value="option2">选项2</option>
        <option value="option3">选项3</option>
    </select>
    ```
* form：表单标签，用于显示表单
    * action：指定表单提交的地址
    * method：指定表单提交的方式，默认为get，即GET请求，post为POST请求
    ```html
    <form action="URL_ADDRESS" method="get">
        <input type="text" name="username" placeholder="请输入用户名">
        <input type="password" name="password" placeholder="请输入密码">
        <input type="submit" value="提交">
    </form>
    ```
* label：标签标签，用于显示标签
    * for：指定标签的id，用于绑定标签和输入框
    ```html
    <label for="username">用户名：</label>
    <input type="text" id="username" name="username" placeholder="请输入用户名">
    ```
* textarea：文本域标签，用于显示文本域
    * rows：指定文本域的行数
    * cols：指定文本域的列数
    ```html
    <textarea rows="5" cols="30" placeholder="请输入文本"></textarea>
    ```
* br：换行标签，用于换行
    ```html
    <br>
    ```
* hr：水平线标签，用于显示水平线
    ```html
    <hr>
    ```
* strong：加粗标签，用于加粗文本
    ```html
    <strong>加粗文本</strong>
    ```
* em：斜体标签，用于斜体文本
    ```html
    <em>斜体文本</em>
    ```
* i：斜体标签，用于斜体文本
    ```html
    <i>斜体文本</i>
    ```
* b：加粗标签，用于加粗文本
    ```html
    <b>加粗文本</b>
    ```
* u：下划线标签，用于下划线文本
    ```html
    <u>下划线文本</u>
    ```
* s：删除线标签，用于删除文本
    ```html
    <s>删除文本</s>
    ```
* del：删除线标签，用于删除文本
    ```html
    <del>删除文本</del>
    ```
* ins：插入线标签，用于插入文本
    ```html
    <ins>插入文本</ins>
    ```
* q：引用标签，用于引用文本
    ```html
    <q>引用文本</q>
    ```
* blockquote：引用块标签，用于引用文本块
    ```html
    <blockquote>引用文本块</blockquote>
    ```
* pre：预格式化标签，用于显示预格式化文本
    ```html
    <pre>
        这是
        预格式化
        文本
    </pre>
    ```
* code：代码标签，用于显示代码
    ```html
    <code>
        这是
        代码
    </code>
    ```
* video：视频标签，用于显示视频
    * src：指定视频的地址
    * controls：指定是否显示视频的控制栏，默认为false，即不显示
    ```html
    <video src="URL_ADDRESS" controls>
        您的浏览器不支持视频标签
    </video>
    ```
* audio：音频标签，用于显示音频
    * src：指定音频的地址
    * controls：指定是否显示音频的控制栏，默认为false，即不显示
    ```html
    <audio src="URL_ADDRESS" controls>
        您的浏览器不支持音频标签
    </audio>
    ```
* iframe：内嵌框架标签，用于显示内嵌框架
    * src：指定内嵌框架的地址
    * width：指定内嵌框架的宽度
    * height：指定内嵌框架的高度
    ```html
    <iframe src="URL_ADDRESS" width="100%" height="300"></iframe>
    ```