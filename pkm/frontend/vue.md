
# Vue

## Vue简介与快速入门

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


## Vue常用指令

* v-for：用于遍历数组或对象
* v-bind：用于绑定属性
* v-on：用于绑定事件
* v-if，v-else-if，v-else：用于条件渲染
* v-show：用于条件渲染
* v-model：用于双向绑定

### v-for

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

### v-bind 和 v-on
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

### v-if 和 v-show

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

## Ajax与Axios

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

## Vue生命周期

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