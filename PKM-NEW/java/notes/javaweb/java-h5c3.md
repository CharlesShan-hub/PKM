# H3C3

## 资料

* 文档去找mdn： https://developer.mozilla.org/en-US/
* 综合案例：[[PKM-NEW/java/notes/javaweb/assets/ex_h5c3/main.html|main]]
* vue案例：[[PKM-NEW/java/notes/javaweb/assets/ex_vue_basic/main.html|main]]

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

### 常见标签

#### 段落

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
* iframe：内嵌框架标签，用于显示内嵌框架
    * src：指定内嵌框架的地址
    * width：指定内嵌框架的宽度
    * height：指定内嵌框架的高度
    ```html
    <iframe src="URL_ADDRESS" width="100%" height="300"></iframe>
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
#### 链接
	
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
* video：视频标签，用于显示视频
    * src：指定视频的地址
    * controls：指定是否显示视频的控制栏，默认为false，即不显示
    * width：指定视频的宽度
    * height：指定视频的高度
    ```html
    <video src="URL_ADDRESS" controls width="100%" height="300px">
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
#### 格式

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
#### 表单

* form：表单标签，用于显示表单
    * action：指定表单提交的地址
    * method：指定表单提交的方式，默认为get，即GET请求，post为POST请求
      * get：GET请求，将表单数据以查询字符串的形式附加到URL地址后面，数据会暴露在URL地址中，不安全，适合用于查询操作
      * post：POST请求，将表单数据以请求体的形式发送到服务器，数据不会暴露在URL地址中，安全，适合用于提交操作
    ```html
    <form action="URL_ADDRESS" method="get">
        <input type="text" name="username" placeholder="请输入用户名">
        <input type="password" name="password" placeholder="请输入密码">
        <input type="submit" value="提交">
    </form>
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
* button：按钮标签，用于显示按钮
    * type：指定按钮的类型，默认为submit，即提交按钮，button为普通按钮
    ```html
    <button type="submit">提交</button>
    <button type="button">普通按钮</button>
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
* textarea：文本域标签，用于显示文本域
    * rows：指定文本域的行数
    * cols：指定文本域的列数
    ```html
    <textarea rows="5" cols="30" placeholder="请输入文本"></textarea>
    ```
* label：标签标签，用于显示标签
    * for：指定标签的id，用于绑定标签和输入框
    ```html
    <label for="username">用户名：</label>
    <input type="text" id="username" name="username" placeholder="请输入用户名">
    ```

## CSS
### 引入CSS方式

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

### 颜色的表示方式
1. 颜色名
	```css
	color: red;
	```
2. 十六进制
	```css
	color: #ff0000;
	```
3. RGB
	```css
	color: rgb(255, 0, 0);
	```
4. RGBA
	```css
	color: rgba(255, 0, 0, 0.5);
	```

###  盒子模型

* 盒子模型的组成
	* 内容区
	* 内边距
	* 边框
	* 外边距
* 盒子模型的属性
	* width：指定盒子的宽度
	* height：指定盒子的高度
	* padding：指定盒子的内边距
	* border：指定盒子的边框
	* margin：指定盒子的外边距
	```css
	div{
		width: 100px;
		height: 100px;
		padding: 10px;
		border: 1px solid #000000;
		margin: 10px;
	}
	```
* 注意默认情况下，盒子模型的宽度和高度是由内容区的宽度和高度决定的，但是如果设置了内边距和边框，盒子模型的宽度和高度会增加。
* 我们也可以通过设置box-sizing属性来改变盒子模型的宽度和高度的计算方式。
* box-sizing: content-box; 盒子模型的宽度和高度是由内容区的宽度和高度决定的
* box-sizing: border-box; 盒子模型的宽度和高度是由内容区的宽度和高度加上内边距和边框决定的

### 弹性布局

强烈建议去看： https://www.ruanyifeng.com/blog/2015/07/flex-grammar.html

flex布局是一种用于创建灵活的布局的方式，它可以让我们更方便地控制元素的排列方式和大小。

* 弹性容器
    * display: flex; 使元素成为弹性容器
* 元素方向
    ```css
    flex-direction: row; /*元素从左到右排列*/
    flex-direction: row-reverse; /*元素从右到左排列*/
    flex-direction: column; /*元素从上到下排列*/
    flex-direction: column-reverse; /*元素从下到上排列*/
    ```
* 元素换行
    * flex-wrap: nowrap; 元素不换行
    * flex-wrap: wrap; 元素换行
    * flex-wrap: wrap-reverse; 元素换行，第一行在下方
* 对齐方式
    * justify-content: flex-start; 元素左对齐
    * justify-content: flex-end; 元素右对齐
    * justify-content: center; 元素居中
    * justify-content: space-between; 元素两端对齐，元素之间的间隔相等
    * justify-content: space-around; 元素两端对齐，元素之间的间隔相等，元素与容器之间的间隔是元素之间间隔的一半

## JS

* 组成
    * ECMAScript: 定义了JS的语法
    * DOM: 文档对象模型，用于操作HTML元素, 比如：document.getElementById()
    * BOM: 浏览器对象模型，用于操作浏览器，比如：window.alert()

### 核心语法

#### JS的引入
 1. 内部引入
    ```html
    <script>
        // JS代码
    </script>
    ```
 2. 外部引入
    ```html
    <script src="JS_FILE_PATH"></script>
    ```
 3. 行内引入
    ```html
    <h1 onclick="alert('Hello World')">Hello World</h1>
    ```

#### 变量
1. 变量的声明
   ```js
   var a = 10;
   let b = 20;
   alert(a);
   ```

2. var和let的区别（现在不推荐var了）
在JavaScript中，`var`和`let`都是用于声明变量的关键字，但它们有几个重要区别：

   1. **作用域范围**：
      - `var`是函数作用域(function-scoped)
      - `let`是块级作用域(block-scoped)
      ```javascript
      function example() {
         if(true) {
         var a = 10;  // 函数作用域
         let b = 20;  // 块级作用域
         }
         console.log(a); // 10 (可以访问)
         console.log(b); // ReferenceError: b is not defined
      }
      ```

   2. **变量提升(Hoisting)**：
      - `var`声明的变量会被提升到函数/全局作用域的顶部
      - `let`声明的变量也会提升，但不会被初始化(暂时性死区)

      ```javascript
      console.log(a); // undefined (变量提升)
      var a = 10;

      console.log(b); // ReferenceError: Cannot access 'b' before initialization
      let b = 20;
      ```
   3. **重复声明**：
      - `var`允许重复声明同一个变量
      - `let`不允许重复声明

      ```javascript
      var x = 1;
      var x = 2; // 允许

      let y = 1;
      let y = 2; // SyntaxError: Identifier 'y' has already been declared
      ```

   4. **全局对象属性**：
      - `var`在全局作用域声明时会成为window对象的属性
      - `let`不会

      ```javascript
      var globalVar = 10;
      let globalLet = 20;

      console.log(window.globalVar); // 10
      console.log(window.globalLet); // undefined
      ```
3. 变量的类型
   * number: 数字
   * string: 字符串
        ```javascript
        let s1 = "a";
        let s2 = 'b';
        let s3 = `d${s1}e`;// 模板字符串，用来简化字符串的拼接
        alert(s3); // dae 
        ```
   * boolean: 布尔值
   * null: 空值
   * undefined: 未定义
   * typeof运算符: 用于获取变量的类型
    ```js
    var a = 10;
    alert(typeof a); // number
    ```

#### 函数

这三种JavaScript函数定义方式有以下主要区别：

1. **普通函数（函数声明）**：
    ```javascript
    function add(a, b) {
    return a + b;
    }
    ```
    - 会被提升(hoisting)，可以在声明前调用
    - 有自己独立的`this`绑定
    - 可以使用`arguments`对象
    - 适合需要命名且需要提升的场景

2. **函数表达式（匿名函数）**：
    ```javascript
    let add = function(a, b) {
    return a + b;
    }
    ```
    - 不会被提升，必须先定义后使用
    - 有自己独立的`this`绑定
    - 可以使用`arguments`对象
    - 适合需要将函数作为值赋给变量的场景

3. **箭头函数**：
    ```javascript
    let add = (a, b) => {
    return a + b;
    }
    ```
    - 不会被提升
    - 没有自己的`this`，继承外层作用域的`this`
    - 不能使用`arguments`对象
    - 没有`prototype`属性
    - 不能用作构造函数（不能用`new`调用）
    - 适合需要保持`this`绑定或需要简洁语法的场景

**简化版箭头函数**（当函数体只有一行时）：
    ```javascript
    let add = (a, b) => a + b;
    ```

**使用建议**：
   - 优先使用箭头函数（特别是回调函数中）
   - 需要`this`绑定或构造函数时用普通函数
   - 函数表达式适合需要动态赋值的情况

#### 自定义对象

```js
let person = {
    name: "John",
    age: 30,
    sayHello: function() {
        alert("Hello, my name is " + this.name);
    } // 可以这样声明方法
    sayBye() {
        alert("Bye, my name is " + this.name);
    } // 也可以这样声明方法
    sayBad: () => {
        alert("Ops " + this.name);
    } // 也可以这样声明方法，但是this指向的是window对象，所以不推荐使用
};
console.log(person.name); // John
console.log(person.age); // 30
person.sayHello(); // Hello, my name is John
person.sayBye(); // Bye, my name is John
```

#### JSON IN JS

```javascript
let person = {
    name: "John",
    age: 30,
    sayHello: function() {
        alert("Hello, my name is " + this.name);
    }
}
let json = JSON.stringify(person); // 将对象转换为JSON字符串
alert(json); // {"name":"John","age":30}
let person2 = JSON.parse(json); // 将JSON字符串转换为对象
alert(person2.name); // John
alert(person2.age); // 30
```
#### DOM
* 文档对象模型（Document Object Model，简称DOM）是W3C组织推荐的处理可扩展置标语言的标准编程接口。
* 文档对象模型的核心是文档对象，文档对象是一个树形结构，每个节点都是一个对象，节点之间有父子关系，根节点是document对象。
* DOM提供了一系列的方法和属性，用于操作文档对象，比如：
    * Document：文档对象
    * Element：元素对象
    * Attribute：属性对象
    * Text：文本对象
    * Comment：注释对象

现在推荐querySelector和querySelectorAll来操作DOM，因为它们更简洁，更方便。
```javascript
let div = document.querySelector("#div1"); // 获取id为div1的元素
let divs = document.querySelectorAll("div"); // 获取所有div元素
```


### 事件监听

早期

```javascript
let button = document.getElementById("button1");
button.onclick = function() {
    alert("Hello World");
}
button.onclick = function() {
    alert("Hello World2");
}
// 只有最后一个事件会被触发
```

现在：可以多次绑定同一个事件，不会覆盖之前的事件

```javascript
let button = document.querySelector("#button1");
button.addEventListener("click", function() {
    alert("Hello World");
})
button.addEventListener("click", function() {
    alert("Hello World2");
})
// 两个事件都会被触发
```

* 鼠标事件
  * click：鼠标点击
  * mouserenter：鼠标进入
  * mouseleave：鼠标离开
* 键盘事件
  * keydown：键盘按下
  * keyup：键盘抬起
* 表单事件
  * submit：表单提交
  * input：输入框内容改变
* 窗口事件
  * load：窗口加载完成
  * resize：窗口大小改变
* 焦点事件
  * focus：获得焦点
  * blur：失去焦点

### 模块化js

```javascript
// module.js
export let a = 10;
export let b = 20;
export function add(a, b) {
    return a + b;
}
```

```javascript
// main.js
import {a, b, add} from "./module.js";
alert(a); // 10
alert(b); // 20
alert(add(a, b)); // 30
```

```html
<script type="module" src="main.js"></script>
```

## Vue

### Vue简介与快速入门

Vue是一款渐进式JavaScript框架，用于构建用户界面。它采用了组件化的开发模式，使得开发人员可以将页面划分为多个组件，每个组件都有自己的模板、逻辑和样式。
* 构建用户界面：基于数据渲染出用户看到的界面
* 渐进式：可以通过声明式的API、组建系统等内容，循序渐进的构建应用

案例：通过返回的一个message，渲染出一个加大加粗的标题

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Vue Demo</title>
    </head>
    <body>
        <div id="app">
            <h1>{{ message }}</h1>
        </div>
    </body>
    <script src="script.js" type="module"></script>
</html>
```

```javascript
// 使用CDN方式引入Vue
import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'
// 或者使用本地文件方式（需要先下载vue.esm-browser.js）
// import { createApp } from './vue.esm-browser.js'
const app = createApp({
    data() {
        return {
            message: 'Hello Vue!'
        }
    }
})
app.mount('#app')
```


### Vue常用指令

* v-for：用于遍历数组或对象
* v-bind：用于绑定属性
* v-on：用于绑定事件
* v-if，v-else-if，v-else：用于条件渲染
* v-show：用于条件渲染
* v-model：用于双向绑定

#### v-for

作用：列表渲染，遍历容器的元素或者对象的属性

语法案例：
```html
<tr v-for="(item,index) in items" :key="item.id">{{item}}</tr>
```

参数说明：
- items：为遍历的数组
- item：为遍历出来的元素
- index：为索引/下标，从0开始；可以省略

省略index语法：
```html
v-for="item in items"
```

key：
作用：给元素添加的唯一标识，便于vue进行列表项的正确排序复用，提升渲染性能
推荐使用id作为key（唯一），不推荐使用index作为key（会变化，不对应）

注意：
1. 遍历的数组，必须在data中定义
2. 要想让哪个标签循环展示多次，就在哪个标签上使用v-for指令

#### v-bind 和 v-on
作用：用于绑定属性和事件
语法案例：
```html
<img v-bind:src="imgUrl">
<button v-on:click="handleClick">按钮</button>
```
也可以简写
```html
<img :src="imgUrl">
<button @click="handleClick">按钮</button>
```

#### v-if 和 v-show

作用：这两类指令，都是用来控制元素的显示与隐藏的

v-if
语法：`v-if="表达式"`，表达式值为true，显示；false，隐藏
原理：基于条件判断，来控制创建或移除元素节点（条件渲染）
场景：要么显示，要么不显示，**不频繁切换的场景**
其它：可以配合 `v-else-if` / `v-else` 进行链式调用条件判断

v-show
语法：`v-show="表达式"`，表达式值为true，显示；false，隐藏
原理：基于CSS样式display来控制显示与隐藏
场景：**频繁切换显示隐藏的场景**

### Ajax与Axios

AJAX全称是Asynchronous JavaScript and XML，即异步JavaScript和XML。

作用：
* 数据交换：用于在浏览器和服务器之间交换数据
* 异步交互：在不重新加载整个页面的情况下，更新页面的一部分内容。比如，表单提交、数据加载等。

Axios是一个基于Promise的HTTP客户端，用于在浏览器和Node.js中发送HTTP请求。
作用：
* 简化HTTP请求：Axios提供了简洁的API，使得发送HTTP请求变得更加容易。
* 支持Promise：Axios返回的是Promise对象，可以使用then()方法来处理响应数据。

引入：

```javascript
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

使用：

```javascript
axios({
    method: 'GET',
    url: 'URL_ADDRESS',
    params: {
        name: 'John',
        age: 30
    }
}).then(function (response) {
	console.log(response.data);
}).catch(function (error) {
	alert(error);
});
```

```javascript
axois({
    method: 'POST',
    url: 'URL_ADDRESS',
    data: {
        name: 'John',
        age: 30
    }
}).then((response) => { // 也可以使用箭头函数，简化了函数的写法
	console.log(response.data);
}).catch((error) => {
	alert(error);
});
```

axios的简化方式【推荐】

```javascript
axios.get('URL_ADDRESS', {
    params: {
        name: 'John',
        age: 30
    }
}).then((response) => {
	console.log(response.data);
}).catch((error) => {
	alert(error);
});

axios.post('URL_ADDRESS', {
    name: 'John',
    age: 30
}).then((response) => {
	console.log(response.data);
}).catch((error) => {
	alert(error);
});
```

### Vue生命周期

Vue生命周期是指Vue实例从创建到销毁的过程，每个阶段都有对应的钩子函数，开发者可以在这些钩子函数中编写逻辑。
Vue生命周期的钩子函数：
* 创建
  * beforeCreate：在实例初始化之后，数据观测和事件配置之前被调用
  * created：在实例创建完成后被立即调用
* 挂载
  * beforeMount：在挂载开始之前被调用
  * mounted：在挂载完成后被调用
* 更新
  * beforeUpdate：在数据更新之前被调用
  * updated：在数据更新之后被调用
* 销毁
  * beforeUnmount：在卸载之前被调用
  * unmounted：在卸载之后被调用