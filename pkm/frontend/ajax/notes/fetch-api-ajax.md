# Fetch API 实现 AJAX

在之前的课程中，`fetch`函数是我们自己定义的，实际上在 2015 年的时候，浏览器提供了一套原生的 API，称为 Fetch API，基于 Promise 实现的，也就是说 2015 年之后，浏览器内置了 `fetch`函数，可以直接使用。

Fetch API 返回的对象就是一个 Promise 对象。Fetch API 的学习可以参考官方文档：[**MDN Web Docs**](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

---

## Fetch API 发送 AJAX GET 请求

### 发送 GET 请求

浏览器内置的 API，不需要引入额外的 js 库。发送 GET 请求代码如下：

```javascript
// 使用Fetch API发送ajax get请求，验证用户名是否可用
fetch(`check?username=${encodeURIComponent(username)}`)
    .then(response => response.json()) 
    .then(data => {
        if(data.success){
            showFeedback('success', '恭喜你，您的用户名可用。');
        }else{
            showFeedback('error', '您的名字太受欢迎，需要重新填写。');
        }
    })
    .catch(error => {
        showFeedback('error', error.message);
    })
```

`response.json()` 方法执行结束之后是需要 `return` 的，这里由于使用箭头函数：`return` 关键字可以省略，如果不返回，则下一个 `.then(data)`中 `data`是没有值的。

**第一个 **`**.then()**`**的参数 response**：由 fetch() 返回的 Promise 解析后得到，表示 HTTP 响应，包含**状态码、头信息、响应体**等，常用方法如下：

```javascript
.then(response => {
  response.ok      // 检查请求是否成功 (状态码 200-299)
  response.status   // HTTP 状态码 (如 200, 404)
  return response.json()  // 解析为 JSON (返回另一个 Promise)【一定要return，要不然下一个 .then(data) 中的data是undefined】
  //return response.text()  // 解析为文本
})
```

注意：response.json() 和 response.text() 都是异步方法，它们返回的是 Promise 对象，必须使用 `await`或 `.then()`来获取最终结果。这两个方法都是异步读取和解析已经接收到的响应体数据。

**第二个 **`**.then()**`**的参数 data**：是解析后的实际内容，类型由解析方法决定（如 response.json()的时候 data 是 json，response.text()的时候 data 是普通文本）。

**第三个 **`**.catch()**`**的参数 error**：可能是多种错误类型，需根据 `error.name` 或 `error.message`区分处理。

### GET 请求的参数提交问题

第一种方式：直接在 URL 后面使用 `?`追加。（不推荐）

```javascript
const url = `check?username=${encodeURIComponent(username)}`
```

第二种方式：使用 URLSearchParams 构建查询字符串（推荐）

```javascript
// 创建URLSearchParams对象添加参数
const params = new URLSearchParams();
params.append('username', username); // 自动处理编码

// 拼接URL
const url = `check?${params.toString()}`;
```

第三种方式：通过 URL API 构建完整URL（推荐）

```javascript
// 使用URL对象规范处理
const url = new URL('check', window.location.href);
url.searchParams.append('username', username); // 自动编码
url = url.toString();
```

---

## Fetch API 发送 AJAX POST 请求

### 发送 POST 请求以 JSON 格式提交

注意：这种方式，后端 Servlet 接收到数据之后，直接通过 `request.getParameter("name")`是获取不到以 `JSON` 方式提交的数据的。`request.getParameter("name")`只能获取的提交格式为：`name=value&name=value`。如果要获取提交的 `JSON`数据，你需要编写特殊的代码。这里感兴趣的可以研究一下，后面的框架一般都自动实现了接收 `JSON`数据。我们这里只需要在前端浏览器的 F12 的网络面板中查看一下，是否能够以 `JSON`格式提交数据即可。

```javascript
fetch('check', {
  method: 'POST',  // 指定为POST方法
  headers: {
    'Content-Type': 'application/json',  // 设置内容类型为JSON
  },
  body: JSON.stringify({username: username})  // 将数据转为JSON字符串
})
.then(response => {
  if (!response.ok) {  // 检查响应是否成功
    throw new Error(`HTTP错误! 状态码: ${response.status}`);
  }
  return response.json();
})
.then(data => {
  if(data.success){
    showFeedback('success', '恭喜你，您的用户名可用。');
  }else{
    showFeedback('error', '您的名字太受欢迎，需要重新填写。');
  }
})
.catch(error => {
  showFeedback('error', error.message || '请求失败，请稍后重试');
});
```

### 发送 POST 请求以 FormData 格式提交

```javascript
// 创建URLSearchParams对象并添加参数
const formData = new URLSearchParams();
formData.append('username', username);

fetch('check', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded', // 必须设置这个Content-Type
  },
  body: formData.toString() // 转换为查询字符串格式
})
.then(response => {
  if (!response.ok) {
    throw new Error(`HTTP错误! 状态码: ${response.status}`);
  }
  return response.json();
})
.then(data => {
  if(data.success){
    showFeedback('success', '恭喜你，您的用户名可用。');
  }else{
    showFeedback('error', '您的名字太受欢迎，需要重新填写。');
  }
})
.catch(error => {
  showFeedback('error', error.message || '请求失败，请稍后重试');
});
```
